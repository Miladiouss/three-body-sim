import numpy as np
# [ m1 ]--MWMWMWMW-k12-MWMWMWMW--[ m2 ]--MWM-k23-WMWMW--[ m3 ]

rs = np.random.RandomState(42)
m1, m2, m3 = rs.uniform(4, 10, 3)
k12, k23 = 2*tuple(np.random.uniform(4, 10, 1))
l12, l23 = 2*tuple(np.random.uniform(4, 10, 1))

x1_0 = 0. + rs.uniform(-1, 1)
x2_0 = 0. + l12 + rs.uniform(-1, 1)
x3_0 = 0. + l12 + l23 + rs.uniform(-1, 1)

v1_0, v2_0, v3_0 = 0., 0., 0.

x1_hist = [x1_0]
x2_hist = [x2_0]
x3_hist = [x3_0]

v1_hist = [v1_0]
v2_hist = [v2_0]
v3_hist = [v3_0]

def calc_accel(x1, x2, x3):
    dx12 = x2 - x1 - l12 
    dx23 = x3 - x2 - l23

    a1 = (0)            - (-dx12*k12/m1)
    a2 = (-dx12*k12/m2) - (-dx23*k23/m2) 
    a3 = (-dx23*k23/m3) - (0)

    return a1, a2, a3


# k1, k2, k3, k4 = 4*tuple(np.random.uniform(0, 10, 1))
# l1, l2, l3, l4 = 4*tuple(np.random.uniform(0, 10, 1))

# dx1 = x1 - x0 - l1
# dx2 = x2 - x1 - l2
# dx3 = x3 - x2 - l3
# dx4 = x4 - x3 - l4

# a1 = -dx1*k1/m1 - -dx2*k2/m1
# a2 = -dx1*k2/m2 - -dx2*k3/m2
# a3 = -dx1*k3/m3 - -dx2*k4/m3


