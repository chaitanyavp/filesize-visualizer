import pygame


class Visualizer:
    """
    Takes in file size data and visually represents it in a Treemap using
    pygame.
    """

    def __init__(self):
        pygame.init()

    def run_display(self):
        """
        Initializes a display and then makes it listen for events.
        :return:
        :rtype:
        """
        pygame.display.set_mode([800, 600])
        self.event_listener()

    def event_listener(self):
        """
        Continuously loops, waiting for user inputs.

        return: None
        """
        continue_running = True
        while continue_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    continue_running = False
        pygame.quit()


if __name__ == "__main__":
    v = Visualizer()
    v.run_display()
