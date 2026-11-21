import math

def local_to_world(local, offset):
    """局部到世界。"""
    raise NotImplementedError("TODO: local_to_world")

def rotate_vec(vec, angle_deg):
    """速度随门旋转。"""
    raise NotImplementedError("TODO: rotate_vec")

def quaternion_continuity(q, prev):
    """四元数连续。"""
    raise NotImplementedError("TODO: quaternion_continuity")

def collision_space(is_portal_frame):
    """碰撞空间。"""
    raise NotImplementedError("TODO: collision_space")

def camera_snap(pos):
    """相机瞬移。"""
    raise NotImplementedError("TODO: camera_snap")

def clip_sides(two_sided):
    """双面裁剪。"""
    raise NotImplementedError("TODO: clip_sides")

def allow_depth(depth):
    """递归深度上限。"""
    raise NotImplementedError("TODO: allow_depth")

def teleport_kind(kind):
    """传送同步方式。"""
    raise NotImplementedError("TODO: teleport_kind")

def rotate_gravity(angle_deg):
    """重力随门旋转。"""
    raise NotImplementedError("TODO: rotate_gravity")

def portal_key(a, b):
    """传送门对键。"""
    raise NotImplementedError("TODO: portal_key")

def inverse_angle(angle_deg):
    """反向角。"""
    raise NotImplementedError("TODO: inverse_angle")

def is_valid_depth(depth):
    """深度有效性。"""
    raise NotImplementedError("TODO: is_valid_depth")

def velocity_scale(speed, factor):
    """速度缩放。"""
    raise NotImplementedError("TODO: velocity_scale")

def dot(a, b):
    """四元数点积。"""
    raise NotImplementedError("TODO: dot")

def wrap_deg(angle_deg):
    """角度归一。"""
    raise NotImplementedError("TODO: wrap_deg")
