import pytest
import math
from gameplay import portal_teleport as mod

CASES = [
    ("world", 'm.local_to_world((1, 2), (10, 20)) == (11, 22)'),
    ("rotate", 'm.rotate_vec((1, 0), 90) == approx((0, 1))'),
    ("same", 'm.quaternion_continuity((1, 0, 0, 0), (1, 0, 0, 0)) == (1, 0, 0, 0)'),
    ("flip", 'm.quaternion_continuity((1, 0, 0, 0), (-1, 0, 0, 0)) == (-1, 0, 0, 0)'),
    ("space", 'm.collision_space(True) == "portal"'),
    ("snap", 'm.camera_snap((1, 2)) == (1, 2)'),
    ("sides", 'm.clip_sides(True) == 2'),
    ("depth", 'm.allow_depth(3) is False'),
    ("kind", 'm.teleport_kind("portal") == "snap"'),
    ("gravity", 'm.rotate_gravity(180) == approx((0, 1))'),
    ("key", 'm.portal_key("A", "B") == "A->B"'),
    ("inverse", 'm.inverse_angle(30) == 330'),
    ("valid", 'm.is_valid_depth(-1) is False'),
    ("speed", 'm.velocity_scale(2, 3) == 6'),
    ("dot", 'm.dot((1, 2, 3, 4), (1, 2, 3, 4)) == 30')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
