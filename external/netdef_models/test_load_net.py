'''
Description load the net from controller.py
LastEditTime 2021-08-20 19:23:33
'''
import netdef_slim as nd
nd.load_module('FlowNet3/css/controller.py')
c = nd.Controller() 
out = c.net_actions.eval(img0, img1)
# out is an OrderedDict with the following structure
#OrderedDict(['flow[0].fwd',     np.array[...],
            #   'occ[0].fwd',      np.array[...],
            #   'occ_soft[0].fwd', np.array[...],
            #   'mb[0].fwd',       np.array[...],
            #   'mb_soft[0].fwd',  np.array[...],
            #   ])     