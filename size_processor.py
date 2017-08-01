import os


class SizeProcessor:

    def __init__(self, folder_path, divider="/"):
        self._divider = divider
        self._file_sizes = {}
        self._file_tree = self._add_subtrees(folder_path)

    def _add_subtrees(self, folder_path):
        subtrees = []
        folder_size = 0
        for item in os.listdir(folder_path):
            item_path = folder_path + self._divider + item
            if os.path.isdir(item_path):
                subtrees.append(self._add_subtrees(item_path))
                folder_size += self._file_sizes[item_path]
            else:
                item_size = os.path.getsize(item_path)
                subtrees.append(item_path)
                self._file_sizes[item_path] = item_size
                folder_size += item_size

        self._file_sizes[folder_path] = folder_size

        return (folder_path, subtrees)

    def get_file_tree(self):
        return self._file_tree

    def get_file_sizes(self):
        return self._file_sizes


if __name__ == "__main__":
    # Test by adding a filepath below:
    s = SizeProcessor("Add filepath here")
    print(s.get_file_tree())
    print(list(s.get_file_sizes().items()))