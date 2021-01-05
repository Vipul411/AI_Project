"""
Models factor
"""

from models import alexnet
from models import resnet
from models import jigen_alexnet

nets_map = {
    'alexnet': alexnet.alexnet,
    'resnet18': resnet.resnet18,
    'jigen_alexnet': jigen_alexnet.jigen_alexnet
}


def get_network(name):
    if name not in nets_map:
        raise ValueError('Name of network unknown %s' % name)

    def get_network_fn(**kwargs):
        return nets_map[name](**kwargs)

    return get_network_fn