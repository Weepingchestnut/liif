import copy


datasets = {}


def register(name):
    def decorator(cls):
        datasets[name] = cls
        return cls
    return decorator


def make(dataset_spec, args=None):      # dataset_spec: {'name': 'image-folder', 'args': {'root_path': './load/div2k/DIV2K_train_HR', 'repeat': 20, 'cache': 'bin'}}
    if args is not None:
        dataset_args = copy.deepcopy(dataset_spec['args'])
        dataset_args.update(args)
    else:
        dataset_args = dataset_spec['args']
    dataset = datasets[dataset_spec['name']](**dataset_args)
    return dataset
