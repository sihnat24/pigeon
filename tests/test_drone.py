from drone import Drone2D



def test_drone_initializes_at_correct_position():
    drone = Drone2D()
    assert drone.x == 4
    assert drone.y == 4

def test_drone_strafe():
    drone = Drone2D()
    start_x = drone.x
    start_y = drone.y
    drone.apply_strafe(1,1)
    drone.update(1)
    assert start_x != drone.x
    assert start_y == drone.y

def test_drone_thrust():
    drone = Drone2D()
    start_x = drone.x
    start_y = drone.y
    drone.apply_thrust(1,1)
    drone.update(1)
    assert start_x == drone.x
    assert start_y != drone.y

