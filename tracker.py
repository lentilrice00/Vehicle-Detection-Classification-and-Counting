import math


class Tracker:
    def __init__(self):
        self.center_points = {} #Store center points
        self.id_count = 0


    def update(self, objects_rect):
        # Boundary box ids
        objects_bbs_ids = []
        for rect in objects_rect:
            x, y, w, h, c = rect
            cx = (x + x + w) // 2 #Center of x
            cy = (y + y + h) // 2 #Center of y
            same_object_detected = False
            for id, center_pt in self.center_points.items():
                dist = math.hypot(cx - center_pt[0], cy - center_pt[1])

                if dist < 35:
                    self.center_points[id] = (cx, cy)
                    objects_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break
            if same_object_detected is False:
                #i.e. if same object is detected we will need to assign id count to that object
                self.center_points[self.id_count] = (cx, cy)
                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1

        new_center_points = {}
        for obj_bb_id in objects_bbs_ids:
            _, _, _, _, object_id = obj_bb_id
            center = self.center_points[object_id]
            new_center_points[object_id] = center

        # Update dictionary with IDs not used removed
        self.center_points = new_center_points.copy()
        return objects_bbs_ids,c