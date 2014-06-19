#!/usr/bin/env python
# Filename: SockServer.py
#encoding=utf-8
__author__ = 'MrLiu'

import os
import sys
import time
import traceback
import threading
import cPickle as p
from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler

class EdgeStatus:

    def __init__(self, filename='edge.status'):
        self.filename = filename
        if os.path.exists(self.filename):
            f = file(self.filename)
            self.list = p.load(f)
            f.close()
        else:
            self.list = []

    def save_to_file(self):
        f = file(self.filename, 'w')
        p.dump(self.list, f)
        f.close()

    def add_item(self, item):
        if item not in self.list:
            self.list.append(item)
            #self.list.sort()

    def del_item(self,item):
        if item in self.list:
            self.list.remove(item)

    def query_all(self):
        self.list.sort()
        return self.list

    def query_by_core(self, core):
        edgelist = []
        for item in self.list:
            ip = item.split(',', 1)
            if ip[1] == core:
                edgelist.append(ip[0])
        return edgelist

    def query_by_edge(self, edge):
        corelist = []
        for item in self.list:
            ip = item.split(',', 1)
            if ip[0] == edge:
                corelist.append(ip[1])
        return corelist

    def count_by_edge(self, edge):
        count = 0
        for item in self.list:
            ip = item.split(',', 1)
            if ip[0] == edge:
                count = count + 1
        return count

class  SockServer(TCPServer,ThreadingMixIn):
    pass

class dataHandle(StreamRequestHandler):

    def handle(self):
        global list
        _t = time.strftime('%Y-%m-%d %H:%M:%S')
        client_ip = self.client_address[0]
        client_port = self.client_address[1]
        print '\n%s Client Connected: %s:%s' % (_t, client_ip, client_port)
        while True:
            try:
                _exit = False
                commands = self.request.recv(1024).strip()
                if len(commands) == 0:
                    continue
                for cmd in commands.split('\r\n'):
                    result = 'Success'
                    str = cmd.split(',', 1)
                    if str[0] == 'exit' or str[0] == 'quit':
                        _exit = True
                        break
                    if len(str) ==1:
                        if str[0] =='qa':
                            for item in list.query_all():
                                ip = item.split(',', 1)
                                r =  'Edge: ' + ip[0] + '\tCore: ' + ip[1] + '\n'
                                self.request.sendall(r)
                        elif str[0] == 'save':
                            list.save_to_file()
                            self.request.sendall('Data had been sync to disk!\n')
                        else:
                            result = 'Error: Data formate incorrect!'
                    elif len(str) == 2:
                        item = str[1] + ',' + client_ip
                        if str[0] == 'a':
                            mutex.acquire()
                            list.add_item(item)
                            mutex.release()
                            #n = '%d' % list.count_by_edge(str[1])
                            #self.request.sendall(n)
                        elif str[0] == 'd':
                            mutex.acquire()
                            list.del_item(item)
                            mutex.release()
                            #n = '%d' % list.count_by_edge(str[1])
                            #self.request.sendall(n)
                        elif str[0] == 'qc':
                            for item in list.query_by_core(str[1]):
                                print '%s' % item
                                self.request.sendall(item + '\n')
                        elif str[0] == 'qe':
                            for item in list.query_by_edge(str[1]):
                                print '%s' % item
                                self.request.sendall(item + '\n')
                        else:
                            result = 'Error: Data formate incorrect!'
                    else:
                        self.request.sendall('Error: Data formate incorrect!\n')
                        result = 'Error: Data formate incorrect!'

                    r = 'Command: ' + cmd + '\tResult: ' + result + '\n'
                    self.request.sendall(r)
                    print 'Command: %s \t Result: %s' % (cmd, result)
                if _exit == True:
                    break
            except:
                #traceback.print_exc()
                break

def _script_real_path():
    return os.path.split(os.path.realpath(__file__))[0]

def _fix_run_path():
    _path = os.path.split(os.path.realpath(__file__))[0]
    os.chdir(_path)


if __name__ == '__main__':
    _fix_run_path()
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError, e:
        print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror)
        sys.exit(1)

    os.setsid()
    os.umask(0)

    try:
        pid = os.fork()
        if pid > 0:
            print "Daemon PID %d" % pid
            sys.exit(0)
    except OSError, e:
        print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror)
        sys.exit(1)

    host='0.0.0.0'
    port=60000
    addr=(host, port)

    filename='edge.status'
    list = EdgeStatus(filename)
    mutex = threading.Lock()
    try:
        server = SockServer(addr,dataHandle)
    except OSError, msg:
         print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    server.serve_forever()
