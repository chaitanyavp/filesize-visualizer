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
        self._file_rectangles = {}
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
                subtrees.append((item_path, []))
                self._file_sizes[item_path] = item_size
                folder_size += item_size

        self._file_sizes[folder_path] = folder_size

        return folder_path, subtrees

    def get_file_tree(self):
        """
        Gets a tree containing the folder path heirarchy.
        """
        return self._file_tree

    def get_file_sizes(self):
        """
        Gets the list of subfolder sizes for this directory.
        """
        return self._file_sizes

    def get_file_rectangles(self):
        """
        Gets the dictionary mapping filepaths to corresponding rectangles.
        """
        return self._file_rectangles

    def calculate_rectangles(self, x, y, width, height, file_tree, into_column):
        """
        A loop that uses the original/root directory, and creates rectangular
        tuples out of itself and its subfolders recursively.
        It later returns the list to be visualized on screen.
        """
        width = int(width)
        height = int(height)

        init_x = x
        init_y = y

        # Loop through subtrees of
        rect_list = []
        for item in file_tree[1][:-1]:

            # Check for folders containing only empty subfolders
            if self._file_sizes[file_tree[0]] == 0:
                continue

            # Calculate proportion of current item
            proportion = self._file_sizes[item[0]] / \
                self._file_sizes[file_tree[0]]

            # Use this to calculate the height and width of its rectangle
            if into_column:
                new_width = round(proportion * width)
                new_height = height
            else:
                new_width = width
                new_height = round(proportion * height)

            # If the resulting rectangle is invisible, then just skip it.
            # If the item is a file, add its rectangle to the list and record it
            #  in the dictionary.
            # otherwise recurse within it.
            if new_width == 0 or new_height == 0:
                continue
            elif not os.path.isdir(item[0]):
                rect_list.append((x, y, new_width, new_height))

                self._file_rectangles[(x, y, new_width, new_height)] = item[0]
            else:
                rect_list += self.calculate_rectangles(x, y,
                                                       new_width,
                                                       new_height, item,
                                                       not into_column)
            # Update x and y
            if into_column:
                x += new_width
            if not into_column:
                y += new_height

        # Adding a seperate case for the final square to account for rounding.
        if self._file_sizes[file_tree[0]] == 0:
            return rect_list

        item = file_tree[1][-1]

        # Since this is the last rectangle, it should fill until the end.
        if into_column:
            new_width = width - (x - init_x)
            new_height = height
        else:
            new_width = width
            new_height = height - (y - init_y)

        # If the resulting rectangle is invisible, then just skip it.
        if new_width == 0 or new_height == 0:
            return rect_list
        elif not os.path.isdir(item[0]):
            rect_list.append((x, y, new_width, new_height))
            self._file_rectangles[(x, y, new_width, new_height)] = item[0]
        else:
            rect_list += self.calculate_rectangles(x, y,
                                                   new_width,
                                                   new_height, item,
                                                   not into_column)
        return rect_list


def round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

if __name__ == "__main__":
    # Sanity check by adding a filepath below:
    s = SizeProcessor("Add filepath here")
    print(s.get_file_tree())
    print(list(s.get_file_sizes().items()))
    print(s.calculate_rectangles(0, 0, 800, 600, s.get_file_tree(), True))
