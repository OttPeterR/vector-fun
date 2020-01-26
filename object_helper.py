import anki_vector
from anki_vector.objects import CustomObjectMarkers, CustomObjectTypes

all_funcs = []



def make_bluetooth_speaker(robot):
    obj = robot.world.define_custom_box(custom_object_type=CustomObjectTypes.CustomType00,
        marker_front=CustomObjectMarkers.Triangles2,  # front
        marker_back=CustomObjectMarkers.Circles2,     # back
        marker_top=CustomObjectMarkers.Hexagons4,     # top (not used)
        marker_bottom=CustomObjectMarkers.Hexagons5,  # bottom (not used)
        marker_left=CustomObjectMarkers.Diamonds2,    # left
        marker_right=CustomObjectMarkers.Hexagons2,   # right
        depth_mm=50.0,
        width_mm=50.0,
        height_mm=65.0,
        marker_width_mm=20.0,
        marker_height_mm=20.0,
        is_unique=True)
    return obj
all_funcs.append(make_bluetooth_speaker)


# def make_fake_cube(robot):
#     obj = robot.world.define_custom_cube(custom_object_type=CustomObjectTypes.CustomType01,
#         marker_front=CustomObjectMarkers.Triangles4,   # front
#         marker_back=CustomObjectMarkers.Triangles5,    # back
#         marker_top=CustomObjectMarkers.Hexagons4,     # top
#         marker_bottom=CustomObjectMarkers.Hexagons5,  # bottom
#         marker_left=CustomObjectMarkers.Circles4,   # left
#         marker_right=CustomObjectMarkers.Circles5,  # right
#         size_mm=44.0,
#         marker_width_mm=20.0,
#         marker_height_mm=20.0,
#         is_unique=True)
#     return obj
# all_funcs.append(make_fake_cube)

def make_dremmel_wall(robot):
    obj = robot.world.define_custom_wall(custom_object_type=CustomObjectTypes.CustomType02,
        marker=CustomObjectMarkers.Hexagons3,
        width_mm=290,
        height_mm=85,
        marker_width_mm=20,
        marker_height_mm=20,
        is_unique=True)
    return obj
all_funcs.append(make_dremmel_wall)


def make_macbook_wall(robot):
    obj = robot.world.define_custom_wall(custom_object_type=CustomObjectTypes.CustomType03,
        marker=CustomObjectMarkers.Triangles3,
        width_mm=310,
        height_mm=100,
        marker_width_mm=20,
        marker_height_mm=20,
        is_unique=True)
    return obj
all_funcs.append(make_macbook_wall)


def make_cardboard_wall_00(robot):
    obj = robot.world.define_custom_wall(custom_object_type=CustomObjectTypes.CustomType04,
        marker=CustomObjectMarkers.Circles5,
        width_mm=260,
        height_mm=135,
        marker_width_mm=20,
        marker_height_mm=20,
        is_unique=True)
    return obj
all_funcs.append(make_cardboard_wall_00)

def make_cardboard_wall_01(robot):
    obj = robot.world.define_custom_wall(custom_object_type=CustomObjectTypes.CustomType05,
        marker=CustomObjectMarkers.Triangles5,
        width_mm=260,
        height_mm=135,
        marker_width_mm=20,
        marker_height_mm=20,
        is_unique=True)
    return obj
all_funcs.append(make_cardboard_wall_01)


def create_all_objects(robot):
    for f in all_funcs:
        f(robot)