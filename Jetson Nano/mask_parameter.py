import numpy as np

# roi_corners_0 = np.array([[(146, 84), (257, 84), (556, 306), (324, 292), (204, 85), (195, 85), (196, 200), (48, 168)]],
#                          dtype=np.int32)
# roi_corners_1 = np.array([[(243, 178), (304, 175), (480, 289), (343, 321), (278, 266), (151, 257)]],
#                          dtype=np.int32)
#
# roi_corners_2 = np.array([[(140, 214), (337, 211), (427, 211), (562, 331), (148, 346), (225, 291), (78, 285)]],
#                          dtype=np.int32)
#
# roi_corners_3 = np.array([[(91, 157), (373, 157), (564, 250), (299, 297), (280, 246), (80, 283)]], dtype=np.int32)

roi_corners_1 = np.array([[(184, 355), (474, 278), (474, 205), (704, 205), (704, 576), (404, 572)]])
roi_corners_2 = np.array([[(275, 372), (450, 355), (455, 300), (704, 300), (704, 576), (436, 571)]])
roi_corners_3 = np.array([[(241, 339), (486, 308), (486, 260), (704, 260), (704, 576), (366, 571)]])
roi_corners_4 = np.array([[(309, 358), (530, 310), (530, 268), (704, 268), (704, 576), (498, 572)]])

split_1 = (184, 205)
split_2 = (275, 300)
split_3 = (241, 260)
split_4 = (309, 268)
