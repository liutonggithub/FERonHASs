from .gcn_a_dataset import GCNADataset

__factory__ = {
    'gcn_a': GCNADataset,
}


def build_dataset(model_type, cfg):
    if model_type not in __factory__:
        raise KeyError("Unknown dataset type:", model_type)
    return __factory__[model_type](cfg)
