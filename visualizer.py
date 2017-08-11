import pygame
import os
from size_processor import SizeProcessor
from homescreen import Homescreen
import random


class Visualizer:
    """
    Takes in file size data and visually represents it in a Treemap using
    pygame.

    === Private Members ===
    @:type _file_list: List<int,int,int,int>
        A list containing all the files to be displayed as colourful rectangles.
        Specifically, each "file" is made of <Width, Height, x-pos, y-pos>.
    @:type _screen_width: int
        The width of the main screen.
    @:type _screen_height: int
        The height of the main screen.
    """

    def __init__(self):
        pygame.init()
        self._file_list = []

        homescreen = Homescreen()
        self._size_processor = SizeProcessor(homescreen.get_filepath())

        self._screen_width = 700
        self._screen_height = 750

        self._file_display = pygame.display.set_mode(
            [self._screen_width, self._screen_height])

    def run_display(self):
        """
        Initializes a display and then makes it listen for events.

        return: None
        """

        # print(self._size_processor.calculate_rectangles(
        #     0, 0, self._screen_width, self._screen_height,
        #     self._size_processor.get_file_tree(), True))

        for rectangle in self._size_processor.calculate_rectangles(
                0, 0, self._screen_width, self._screen_height - 50,
                self._size_processor.get_file_tree(), True):
            curr_colour = self.generate_random_color()

            # To check for black bars:
            # curr_colour = (255,255,255)

            if rectangle[3] == 1:
                start_pos, end_pos = self._convert_rect_to_line(rectangle)
                pygame.draw.line(self._file_display, curr_colour, start_pos,
                                 end_pos)
            else:
                pygame.draw.rect(self._file_display, curr_colour, rectangle)

        # Current code
        self._update_text("Please click on a block to show its details!")

        self._create_user_prompts()

        pygame.display.flip()
        self.event_listener()

    def _convert_rect_to_line(self, rectangle):
        """Converts rectangles of height 1 into lines coordinates.

        @:type self: Visualizer
        @:type rectangle: (int, int, int, int)
        @:return: (int, int), (int, int)
        """
        return (rectangle[0], rectangle[1]), (
            rectangle[0] + rectangle[2], rectangle[1])

    def _update_text(self, new_text):
        """
        Updates the text in the small bar below the rectangular display.
        """
        pygame.draw.rect(self._file_display, (127, 255, 0),
                         (0, self._screen_height - 75, self._screen_width, 25))
        new_font = pygame.font.SysFont("Cambria", 12)
        new_label = new_font.render(new_text, 1, (148, 0, 211))
        self._file_display.blit(new_label, (10, self._screen_height - 70))

    def _create_user_prompts(self):
        """
        Creates the area holding the user prompt information in the bottom
        part of the screen.
        """
        pygame.draw.rect(self._file_display, (127, 133, 244),
                         (0, self._screen_height - 50, self._screen_width, 50))
        header_font = pygame.font.SysFont("Verdana", 14)
        info_font = pygame.font.SysFont("Verdana", 11)

        header_label = header_font.render("User", 1, (255, 255, 211))
        header_label2 = header_font.render("Controls:", 1, (255, 255, 211))
        left_click_label = info_font.render("Left Click: Displays the file path and size above.",
                                           1, (255, 255, 211))
        middle_click_label = info_font.render("Middle Click: Attempts to run the selected file.",
                                             1, (255, 255, 211))
        right_click_label = info_font.render("Right Click: Opens the selected file's local directory.",
                                            1, (255, 255, 211))

        self._file_display.blit(header_label, (15, self._screen_height - 44))
        self._file_display.blit(header_label2, (15, self._screen_height - 28))
        self._file_display.blit(left_click_label, (95, self._screen_height - 48))
        self._file_display.blit(middle_click_label, (95, self._screen_height - 33))
        self._file_display.blit(right_click_label, (95, self._screen_height - 18))

    def event_listener(self):
        """
        Continuously loops, waiting for user inputs.

        @:return: None
        """

        continue_running = True
        while continue_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continue_running = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    if pygame.mouse.get_pos()[1] >= 700:
                        continue
                    if event.button == 3:
                        display_text = self.process_right_click(
                            pygame.mouse.get_pos())
                    elif event.button == 2:
                        display_text = self.process_middle_click(
                            pygame.mouse.get_pos())
                    else:
                        display_text = self.process_left_click(
                            pygame.mouse.get_pos())
                    self._update_text(display_text)
                    pygame.display.flip()
        pygame.quit()

    def process_left_click(self, pos):
        """
        Processes the event for the left mouse click.

        Specifically, it will display the path, size, and number of sub-directories
        for the currently selected directory (rectangle).

        @:type pos: Tuple
            A set of x/y coordinates for the mouse's current position.
        @:return: The directory path and the file size.
        """

        selected_file = self._find_file(pos)

        return selected_file  + " (" \
            + str(self._size_processor.get_file_sizes()[selected_file]) + ")"

    def process_middle_click(self, pos):
        """
        Processes the event for the middle mouse click.

        Specifically, it will attempt to open the selected file on screen.
        If it fails, an empty command screen will open/close, and return
        you to the program again.

        @:type pos: Tuple
            A set of x/y coordinates for the mouse's current position.
        @:return: The directory path and the file size.
        """

        selected_file = self._find_file(pos)
        os.startfile(selected_file)
        return selected_file + " (" \
            + str(self._size_processor.get_file_sizes()[selected_file]) + ")"

    def process_right_click(self, pos):
        """
        Processes the event for the right mouse click.

        Specifically, it will open the local directory that contains the
        selected file.

        @:type pos: Tuple
            A set of x/y coordinates for the mouse's current position.
        @:return: The directory path and the file size.
        """

        selected_file = self._find_file(pos)
        path = selected_file.split("/")
        directory = ""
        if len(path) > 1:
            for item in path[:-1]:
                directory += item + "/"
        os.startfile(directory)
        return selected_file + " (" \
            + str(self._size_processor.get_file_sizes()[selected_file]) + ")"

    def _find_file(self, pos):
        x, y = pos
        file_rectangles = self._size_processor.get_file_rectangles()

        # Linear search since the list is unsorted.
        for rect in list(file_rectangles):
            # if str(type(rect[0])) == "<class 'str'>":
            #     print(rect)
            if (rect[0] <= x < rect[0] + rect[2]) and (
                    rect[1] <= y < rect[1] + rect[3]):
                return file_rectangles[rect]

    def generate_random_color(self):
        """
        Uses the python random module to generate a random colour.
        return: A random colour tuple (of 3 ints).

        @:return: int,int,int
        """
        red_value = random.randint(0, 255)
        green_value = random.randint(0, 255)
        blue_value = random.randint(0, 255)
        return red_value, green_value, blue_value


if __name__ == "__main__":
    v = Visualizer()
    v.run_display()
