import os


class SizeProcessor:
    """
    A Processing Object containing the necessary methods to calculate file sizes,
    directory subfolders, and even positions of a clicked directory (on screen)

    @type divider: char
        A directory path dividing symbol.
    @type _file_sizes: List<int>
        A list of file sizes for a directory's subfolders.
    @type _file_tree: Tuple<string, List<Tuple>>
        A directory, compriesed of its path and its subfolders.
    """
    def __init__(self, folder_path, divider="/"):
        self._divider = divider
        self._file_sizes = {}
        self._file_tree = self._add_subtrees(folder_path)
        self._decimal_addon = 0.0

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
                subtrees.append((item_path, []))
                self._file_sizes[item_path] = item_size
                folder_size += item_size

        self._file_sizes[folder_path] = folder_size

        return folder_path, subtrees

    def get_file_tree(self):
        """
        Gets the path for this directory (I think...?)
        """
        return self._file_tree

    def get_file_sizes(self):
        """
        Gets the list of subfolder sizes for this directory.
        """
        return self._file_sizes

    def calculate_rectangles(self, x, y, width, height, file_tree, into_column):
        """
        A loop that uses the original/root directory, and creates rectangular tuples
        out of itself and its subfolders recursively.
        It later returns the list to be visualized on screen.
        """
        # Loop through subtrees of
        rect_list = []
        for item in file_tree[1]:
            # if item is not a directory, add its proportion
            # otherwise recurse.
            print(item[0])
            proportion = self._file_sizes[item[0]] / \
                         self._file_sizes[file_tree[0]]

            # Unimplemented code for decimal rounding
            # Accounts for decimal roundoffs
            # whole_proportion = proportion[:]
            # dec_proportion = 0.0
            # if proportion % 1 != 0:
            #     dec_proportion = proportion - int(proportion)
            #     whole_proportion -= dec_proportion

            if not os.path.isdir(item[0]):
                rect_list.append((x, y, proportion * width, height))
            else:
                rect_list += self.calculate_rectangles(x, y, proportion * width,
                                                       height, item,
                                                       not into_column)

            x += proportion*width

            # Unimplemented code for decimal rounding
            # x += whole_proportion*width
            # self._decimal_addon += dec_proportion

        return rect_list


if __name__ == "__main__":
    # Test by adding a filepath below:
    s = SizeProcessor("Add filepath here")
    print(s.get_file_tree())
    print(list(s.get_file_sizes().items()))
    print(s.calculate_rectangles(0, 0, True))
