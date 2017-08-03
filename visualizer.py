import pygame
from size_processor import SizeProcessor
from homescreen import Homescreen
import random


class Visualizer:
    """
    Takes in file size data and visually represents it in a Treemap using
    pygame.

    === Private Members ===
    @type _file_list: List<int,int,int,int>
        A list containing all the files to be displayed as colourful rectangles.
        Specifically, each "file" is made of <Width, Height, x-pos, y-pos>.
    @type _screen_width: int
        The width of the main screen.
    @type _screen_height: int
        The height of the main screen.
    """

    def __init__(self):
        pygame.init()
        self._file_list = []

        homescreen = Homescreen()
        self._size_processor = SizeProcessor(homescreen.get_filepath())

        self._screen_width = 800
        self._screen_height = 600

        self._file_display = pygame.display.set_mode(
            [self._screen_width, self._screen_height])

    def run_display(self):
        """
        Initializes a display and then makes it listen for events.

        return: None
        """
        print(self._size_processor.calculate_rectangles(
                0, 0, self._screen_width, self._screen_height,
                self._size_processor.get_file_tree(), True))

        for rectangle in self._size_processor.calculate_rectangles(
                0, 0, self._screen_width, self._screen_height,
                self._size_processor.get_file_tree(), True):
            curr_colour = self.generate_random_color()
            pygame.draw.rect(self._file_display, curr_colour, rectangle)


        # Code to generate a footer and starter text
        #
        # Code for generating a random coloured footer + complementory coloured text
        # For now it's scrapped because some combinations look kind of bad
        #
        # footer_colour = self.generate_random_color()
        # pygame.draw.rect(file_display, (footer_colour[0], footer_colour[1], footer_colour[2]),
        #                  (0, self._screen_height - 25, self._screen_width, 25))
        # footer_label = self._update_text("Please click on a block to show its details!", footer_colour)

        # Current code
        self._update_text("Please click on a block to show its details!")

        pygame.display.flip()
        self.event_listener()

    def _update_text(self, new_text):
        """
        Stub for the update text method.
        """
        pygame.draw.rect(self._file_display, (127, 255, 0),
                         (0, self._screen_height - 25, self._screen_width, 25))
        new_font = pygame.font.SysFont("Cambria", 12)
        new_label = new_font.render(new_text, 1, (148, 0, 211))
        self._file_display.blit(new_label, (10, self._screen_height - 20))

        # If you ever want to try random footer colour generation again (code below)
        # new_label = new_font.render(new_text, 1, (255 - footer_colours[0], 255 - footer_colours[1],
        #                                           255 - footer_colours[2]))

    def event_listener(self):
        """
        Continuously loops, waiting for user inputs.

        return: None
        """
        display_text = ""
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

        @type pos: Tuple
            A set of x/y coordinates for the mouse's current position.
        return: None
        """
        text_to_display = "Oh wait right now it doesn't work..."
        # selected_file = find_file(pos[0], pos[1], self._screen_width,
        #                           self._screen_height)
        # text_to_display = selected_file.path_name + " " + selected_file.file_size + " " + \
        #                   selected_file.subfolders.size + " subfolders"
        return text_to_display

    def generate_random_color(self):
        """
        Uses the python random module to generate a random colour.
        return: A random colour tuple (of 3 ints).
        rtype: int,int,int
        """
        red_value = random.randint(0, 255)
        green_value = random.randint(0, 255)
        blue_value = random.randint(0, 255)
        return red_value, green_value, blue_value


if __name__ == "__main__":
    v = Visualizer()
    v.run_display()
