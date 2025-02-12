from manim import *
import numpy as np


class M5(Scene):
    def construct(self):
        # 绘制坐标轴
        axes = Axes(
            y_range=[0, 4, 0.5],
            x_range=[-2, 2],
            axis_config={"stroke_color": "#FFFFFF"},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 4.01, 2),
                "numbers_with_elongated_ticks": np.arange(0, 4.01, 2),
            },
        )
        axes.add_coordinates()
        labels = axes.get_axis_labels(
            x_label=Tex("$x$"),
            y_label=Tex("$f(x)$")
        )
        origin = Tex("$O$")
        origin.next_to(axes.get_origin(), DOWN)
        # TODO M5.1
        self.play(Create(axes), runtime=2)
        self.play(Create(labels), Create(origin))
        # 绘制函数
        def func(x):
            return x ** 4 - x**3 + x
        graph = axes.plot(func)
        graph.color = '#00FFFF'
        self.play(Create(graph))
        # 显示函数标签
        tex = Tex("$f(x)=x^4-x^3+x$")
        tex.font_size = 25
        tex.move_to(axes.coords_to_point(1.9, 4))
        self.play(Create(tex))
        self.wait(0.1)
        # 生成点
        t = ValueTracker(1)
        dot = Dot(axes.coords_to_point(t.get_value(), func(t.get_value())))
        dot.color = YELLOW
        dot.add_updater(lambda x: x.move_to(axes.c2p(t.get_value(), func(t.get_value()))))
        # TODO M5.2
        self.play(Write(dot))
        # 切线
        def func2(x):
            return 4*x**3 - 3*x**2 + 1
        def get_cut_line():
            '''获得切线'''
            beg_point = [t.get_value()+3,func(t.get_value())+3*func2(t.get_value())]
            end_point = [t.get_value()-3,func(t.get_value())-3*func2(t.get_value())]
            temp = Line(start=axes.coords_to_point(*beg_point),
                        end=axes.coords_to_point(*end_point),
                        stroke_width=0.8).set_color(PURPLE_B)
            return temp
        cut_line = get_cut_line()
        cut_line.add_updater(lambda x:x.become(get_cut_line()))
        k_tex = MathTex(f"k={func2(t.get_value()):.3f}").set_color(PURPLE_B).next_to(dot,buff=SMALL_BUFF)
        k_tex.add_updater(lambda x:x.become(
            MathTex(f"k={func2(t.get_value()):.3f}").set_color(PURPLE_B).next_to(dot,buff=SMALL_BUFF)))
        self.play(Write(cut_line), Write(k_tex))
        self.wait()
        # 点移动
        # TODO M5.3
        self.play(t.animate.set_value(-0.2))
        self.wait()
        # TODO M5.4
        self.play(t.animate.set_value(1.4))
        self.wait()


class M7(Scene):
    def construct(self):
        # 绘制坐标轴
        axes = Axes(
            y_range=[0, 4, 0.5],
            x_range=[-2, 2],
            axis_config={"stroke_color": "#FFFFFF"},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 10.01, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            y_axis_config={
                "numbers_to_include": np.arange(0, 4.01, 2),
                "numbers_with_elongated_ticks": np.arange(0, 4.01, 2),
            },
        )
        axes.add_coordinates()
        labels = axes.get_axis_labels(
            x_label=Tex("$x$"),
            y_label=Tex("$f(x)$")
        )
        origin = Tex("$O$")
        origin.next_to(axes.get_origin(), DOWN)
        self.play(Create(axes), runtime=2)
        self.play(Create(labels), Create(origin))
        # 绘制函数
        def func(x):
            return x ** 4 - x**3 + x
        graph = axes.plot(func)
        graph.color = '#00FFFF'
        self.play(Create(graph))
        # 显示函数标签
        tex = Tex("$f(x)=x^4-x^3+x$")
        tex.font_size = 25
        tex.move_to(axes.coords_to_point(1.9, 4))
        self.play(Create(tex))
        self.wait(0.1)
        # 生成点
        t = ValueTracker(1)
        dot = Dot(axes.coords_to_point(t.get_value(), func(t.get_value())))
        dot.color = YELLOW
        dot.add_updater(lambda x: x.move_to(axes.c2p(t.get_value(), func(t.get_value()))))
        self.play(Write(dot))
        self.wait(0.3)
        # 点动示意
        self.play(t.animate.set_value(-0.4554))
        self.wait(0.1)
        self.play(t.animate.set_value(1))
        self.wait(0.5)
        def func2(x):
            # 这是目标函数的导数
            return 4*x**3 - 3*x**2 + 1
        alpha_vt = ValueTracker(0.05)
        times_vt = ValueTracker(0)
        # 虚线示意
        def refresh_tex():
            temp = Tex(fr"学习率$\alpha = ${alpha_vt.get_value():.2f},当前迭代次数{times_vt.get_value():.0f}",
                       tex_template=TexTemplateLibrary.ctex).set_color(PURPLE_B).to_edge(UL,buff=0.1)
            temp.font_size = 30
            return temp
        alpha_text = refresh_tex()
        alpha_text.add_updater(lambda x:x.become(refresh_tex()))
        self.play(Write(alpha_text))
        self.wait()
        def show_gd():
            '''展示GD过程'''
            times_vt.set_value(0)
            while abs(func2(t.get_value())) > 0.05 and -2<t.get_value()<2:
                dx = alpha_vt.get_value() * func2(t.get_value())
                xx = t.get_value() - dx
                dot2 = Dot(axes.coords_to_point(xx, func(t.get_value())))
                dot2.set_y(dot.get_y())
                line_h = Arrow(dot.get_center(), dot2.get_center(),
                               stroke_width=2.0,
                               buff=0.0,
                               tip_length=1.0
                               )
                dx_tex = MathTex(r"\Delta x={:.3f}".format(dx))
                po_tex = MathTex(r"x={:.3f},f(x)={:.3f}".format(xx, func(xx)))
                dx_tex.font_size = 30
                po_tex.font_size = 30
                dx_tex.to_edge(UL, buff=0.1)
                po_tex.to_edge(UL, buff=0.1)

                dx_tex.shift(0.6 * DOWN)
                po_tex.shift(1.2 * DOWN)
                self.play(Create(line_h), Write(dx_tex))
                self.wait(0.1)
                self.play(t.animate.set_value(xx), Write(po_tex),times_vt.animate.set_value(times_vt.get_value()+1))
                self.wait(0.2)
                self.play(FadeOut(line_h),FadeOut(dx_tex),FadeOut(po_tex))
            self.wait()
        def reset():
            '''重置'''
            t.set_value(1)
        # TODO M7.1
        show_gd()
        reset()
        # TODO M7.2
        self.play(alpha_vt.animate.set_value(1))
        show_gd()
        reset()
        # TODO M7.3
        self.play(alpha_vt.animate.set_value(0.3))
        show_gd()
        self.wait(5)
