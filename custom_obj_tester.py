import time

import anki_vector
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes

import object_helper

def main():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial,
                           default_logging=False,
                           show_viewer=True,
                           show_3d_viewer=True,
                           enable_custom_object_detection=True,
                           enable_nav_map_feed=True) as robot:

        # init all objects from the helper
        object_helper.create_all_objects(robot)


        # just let it run...
        try:
            while True:
                time.sleep(0.25)
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
