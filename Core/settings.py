from yaml import load, dump, Loader, Dumper


def load_setting(setting_name):
    with open('./settings.yaml', 'r') as f:
        data = load(f, Loader=Loader)
        if data != None:
            return data[setting_name]
