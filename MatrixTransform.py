from manim import *

class MatrixAnimation(Scene):
    def construct(self):
        # Tạo văn bản giới thiệu
        IntroText = Text("Matrix Transformation in 2D/3D space")
        self.play(Write(IntroText))
        self.wait(2)
        self.play(FadeOut(IntroText))

        # Tạo văn bản "Translation Matrix"
        Text1 = Text("Translation Matrix")
        self.play(Write(Text1))
        self.wait(2)
        self.play(FadeOut(Text1))

         # Tạo hệ trục tọa độ 2D
        axes = Axes(
            x_range=[-10, 10, 1],  # Phạm vi và bước trên trục x
            y_range=[-10, 10, 1],  # Phạm vi và bước trên trục y
            axis_config={"color": BLUE},  # Màu của các trục
        )

        # Nhãn trục
        labels = axes.get_axis_labels(x_label="x", y_label="y")

          # Nhãn trục
        labels = axes.get_axis_labels(x_label="x", y_label="y")

        # Vẽ hệ trục và nhãn
        self.play(Create(axes), Write(labels))

        # Danh sách các điểm và nhãn
        points_data = [(2, 3), (3, 4), (0, 5)]
        points = []
        labels = []

        # Tạo các điểm và nhãn tương ứng
        for (x, y) in points_data:
            point = Dot(axes.coords_to_point(x, y), color=RED)
            label = MathTex(f"({x}, {y})").next_to(point, UP)
            label.font_size = 15
            points.append(point)
            labels.append(label)

            # Hiển thị điểm và nhãn của nó
            self.play(FadeIn(point), Write(label))

            # Kết nối các điểm A, B, C bằng vòng lặp
        for i in range(len(points)):
            # Kết nối điểm hiện tại với điểm tiếp theo (sử dụng modulo để quay lại POINT đầu) để  nối lại điểm xuát phát ban đầu
            line = Line(start=points[i].get_center(), end=points[(i + 1) % len(points)].get_center(), color=YELLOW)
            self.play(Create(line))
        self.wait()

        # Tạo ma trận dịch chuyển
        Matrix = MathTex(
            r"\begin{bmatrix} 2 & 3 & 1 \\ 3 & 4 & 1 \\ 0 & 5 & 1 \end{bmatrix}"
        )
         # Tạo dấu nhân giữa hai ma trận
        multiplication_sign = MathTex(r"\times").next_to(Matrix, RIGHT, buff=0.5)

        
        MatrixTranslation = MathTex(

            r"\begin{bmatrix} 1 & 0 & -2 \\ 0 & 1 & -3 \\ 0 & 0 & 1 \end{bmatrix}"
        )
         # Di chuyển ma trận đến góc trên bên trái (điểm (x, y) sẽ là (-screen_width/2, screen_height/2))
         # Lấy kích thước màn hình
        screen_width = config.frame_width
        screen_height = config.frame_height
        #
        Matrix.move_to(LEFT * (screen_width / 2 - 2) + UP * (screen_height / 2 - 2))
        #
        multiplication_sign.next_to(Matrix, RIGHT, buff=0.5)
         #
        MatrixTranslation.next_to(multiplication_sign, RIGHT, buff=0.5)  # buff là khoảng cách giữa hai ma trận


        self.play(Write(Matrix))
        self.wait(2)
        self.play(Write(multiplication_sign))
        self.wait(0.5)
        self.play(Write(MatrixTranslation))
        self.wait(1)
        self.play(FadeOut(Matrix,MatrixTranslation,multiplication_sign))

        # Tạo văn bản "Scaling Matrix"
        Text2 = Text("Scaling Matrix")
        self.play(Write(Text2))
        self.wait(2)
        self.play(FadeOut(Text2))

        # Tạo văn bản "Rotation Matrix"
        Text3 = Text("Rotation Matrix")
        self.play(Write(Text3))
        self.wait(2)
        self.play(FadeOut(Text3))
