from manim import *

class DragonCurve(Scene):
    def construct(self):
        # Khởi tạo các biến
        order = 10 # Số lần lặp để tạo ra Dragon Curve
        length = 2 # Độ dài mỗi đoạn thẳng
        angle = PI/2 # Góc quay

        # Tạo Dragon Curve
        path = self.dragon_curve(order, length, angle)

        # Tạo đường vẽ
        dragon_curve = VMobject()
        dragon_curve.set_points_smoothly(path)

        # Hiển thị Dragon Curve
        self.play(Create(dragon_curve))

    def dragon_curve(self, order, length, angle):
        """
        Hàm tạo Dragon Curve
        """
        # Khởi tạo
        path = [(0, 0), (length, 0)]
        directions = [1]

        for _ in range(order):
            # Lật ngược danh sách và thêm vào hình chiếu của mỗi vector
            directions = directions + [1] + [x * -1 for x in reversed(directions)]
            
            # Lặp qua mỗi phần tử trong directions để tạo ra các điểm mới
            new_path = []
            for i, direction in enumerate(directions):
                dx = length * np.cos(angle)
                dy = length * np.sin(angle)
                last_point = path[-1]
                new_point = (last_point[0] + dx, last_point[1] + dy)
                
                # Thêm điểm mới vào path
                path.append(new_point)

                # Cập nhật góc quay
                if direction == 1:
                    angle -= PI/2
                else:
                    angle += PI/2

        return path

