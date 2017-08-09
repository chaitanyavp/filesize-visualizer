import pygame
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

        self._screen_width = 800
        self._screen_height = 800

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
                0, 0, self._screen_width, self._screen_height,
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
        Stub for the update text method.
        """
        pygame.draw.rect(self._file_display, (127, 255, 0),
                         (0, self._screen_height - 25, self._screen_width, 25))
        new_font = pygame.font.SysFont("Cambria", 12)
        new_label = new_font.render(new_text, 1, (148, 0, 211))
        self._file_display.blit(new_label, (10, self._screen_height - 20))

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
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
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
        @:return: None
        """

        selected_file = self._find_file(pos)
        text_to_display = selected_file + " (" \
            + str(self._size_processor.get_file_sizes()[selected_file]) + ")"

        return text_to_display

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
