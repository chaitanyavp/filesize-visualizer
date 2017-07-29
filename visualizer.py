import pygame


def run_display():
    """
    Initializes a display and then makes it listen for events.
    :return:
    :rtype:
    """
    print()
    pygame.init()
    pygame.display.set_mode([800, 600])
    event_listener()


def event_listener():
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
    run_display()
