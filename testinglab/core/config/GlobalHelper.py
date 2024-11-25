import os
from pathlib import Path

class GlobalHelper:
    _framework_prop = {}

    @staticmethod
    def load_property():
        try:
            testinglab_dir = Path.cwd().parent.parent
            prop_file_path = os.path.join(testinglab_dir, "core", "resources", "Global.properties")
            print(prop_file_path)
            with open(prop_file_path, 'r') as prop_file:
                for line in prop_file:
                    if line.strip() and not line.startswith('#'):  # Skip blank lines and comments
                        key, value = line.split('=', 1)
                        GlobalHelper._framework_prop[key.strip()] = value.strip()
        except Exception as ex:
            print(f"Error: {ex}")

    @staticmethod
    def get_property(prop_name):
        return GlobalHelper._framework_prop.get(prop_name, None)
