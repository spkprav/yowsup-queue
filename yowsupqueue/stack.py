import queue
import threading

from yowsup.layers.network import YowNetworkLayer
from yowsup.layers import YowLayerEvent
from yowsup.stacks import YowStackBuilder
from yowsup.layers.auth import AuthError

from .layer import QueueLayer
from yowsupqueue.beanstalkstack import BeanstalkStack

class QueueStack():
    def __init__(self):
        pass

    def start(self,config):


        yowsupConfig = config['Yowsup']
        credentials = (yowsupConfig["Username"], yowsupConfig["Password"])  # replace with your phone and password



        beanstalkdConfig = config['Beanstalkd']
        beanstalkdStack = BeanstalkStack()
        self.beanstalkStack = beanstalkdStack
        stackBuilder = YowStackBuilder()
        self.stack = stackBuilder \
            .pushDefaultLayers(True) \
            .push(QueueLayer(self.beanstalkStack)) \
            .build()

        self.beanstalkStack.setConnectParams(beanstalkdConfig["Host"], beanstalkdConfig["Port"])








        self.stack.setCredentials(credentials)
        connectEvent = YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT)
        self.stack.broadcastEvent(connectEvent)

        try:

            #self.stack.loop(timeout = 0.5, discrete = 0.5)
            self.stack.loop(timeout = 0.5)
        except AuthError as e:
            print("Auth Error, reason %s" % e)




