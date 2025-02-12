from manim import *
import numpy as np


class M1(Scene):
    """展示目标函数"""
    def construct(self):
        # 目标函数
        aim_func_text_obj = Tex(r"$\text{目标函数:}g(x,y)=[5(y-\frac{5.1}{4\pi ^{2}}x^{2}+\frac{5}{\pi}x-6)^{2}+10(1-\frac{1}{8\pi})\cos{x}+20]/100$",tex_template=TexTemplateLibrary.ctex)
        # 当前坐标
        now_point_text_obj = Tex(r"$\text{当前坐标:}(x,y,z)=(5,12,6.0908)$",tex_template=TexTemplateLibrary.ctex)
        aim_func_text_obj.font_size = 35
        now_point_text_obj.font_size = 35
        group = VGroup(aim_func_text_obj,now_point_text_obj)
        group.arrange(DOWN,aligned_edge=LEFT).to_edge(UL,buff=0.3)
        # TODO M1.1
        self.play(Write(aim_func_text_obj),Write(now_point_text_obj))
        self.wait()
        # TODO M1.2
        self.play(Unwrite(aim_func_text_obj))
        self.wait()


class M4(Scene):
    """展示梯度描述过程中的表达式"""
    def construct(self):
        '''展示平面方程'''
        lines = VGroup(
            Tex("$g=$","$A$","$x$","$+$","$B$","$y$","$+g_0$"),
            Tex(r"$\frac{\partial g}{\partial x}$","$=$","$A$","$,$",r"$\frac{\partial g}{\partial y}$","$=$","$B$"),
            Tex(r"$\frac{\partial f}{\partial x}$","$=$",r"$\frac{\partial g}{\partial x}$","$,$",r"$\frac{\partial f}{\partial y}$","$=$",r"$\frac{\partial g}{\partial y}$"),
            Tex("$A$","$=$",r"$\frac{\partial f}{\partial x}$","$,$","$B$","$=$",r"$\frac{\partial f}{\partial y}$")
        )
        lines.arrange(DOWN, buff=SMALL_BUFF)
        g_line = Tex("$g=$",r"$\frac{\partial f}{\partial x}$","$x$","$+$",r"$\frac{\partial f}{\partial y}$","$y$","$+g_0$")
        g_line.move_to([0, 3, 0])
        '''x微小位移'''
        gx_line = Tex("$g(x_0+h,y_0)$","$=$",r"$\frac{\partial f}{\partial x}$","$($","$x$","$+$","$h$","$)$","$+$",r"$\frac{\partial f}{\partial y}$","$y$","$+g_0$")
        dgx_line = Tex(r"$\Delta g_x$","$=$",r"$\frac{\partial f}{\partial x}$","$h$")
        '''y微小位移'''
        gy_line = Tex("$g(x_0,y_0+h)$","$=$",r"$\frac{\partial f}{\partial x}$","$x$","$+$",r"$\frac{\partial f}{\partial y}$","$($","$y$","$+$","$h$","$)$","$+g_0$")
        dgy_line = Tex(r"$\Delta g_y$","$=$",r"$\frac{\partial f}{\partial y}$","$h$")
        VGroup(gx_line,dgx_line,gy_line,dgy_line).arrange(DOWN,buff=SMALL_BUFF)
        play_kw = {"run_time": 1}
        # TODO M4.1
        self.play(Write(lines[0]), **play_kw)
        self.wait()
        self.play(Write(lines[1]), **play_kw)
        self.wait()
        self.play(Write(lines[2]), **play_kw)
        self.wait()
        # TODO M4.2
        self.play(TransformMatchingTex(VGroup(lines[1].copy(),lines[2].copy()),lines[3]), path_arc=90 * DEGREES, **play_kw)
        self.wait()
        self.play(TransformMatchingTex(lines,g_line,path_arc=90*DEGREES,**play_kw))
        self.wait()
        # TODO M4.3
        self.play(TransformMatchingTex(g_line.copy(), gx_line), **play_kw)    # 显示x微小位移
        self.play(TransformMatchingTex(gx_line.copy(),dgx_line), **play_kw)  # 显示x微小位移下的改变量
        self.wait()
        # TODO M4.4
        self.play(TransformMatchingTex(g_line.copy(), gy_line), **play_kw)  # 显示y微小位移
        self.play(TransformMatchingTex(gx_line.copy(), dgy_line), **play_kw)  # 显示y微小位移下的改变量
        self.wait()
        self.play(FadeOut(gx_line),FadeOut(dgx_line),FadeOut(gy_line),FadeOut(dgy_line))
        '''任意方向变化'''
        g_any_line = Tex(r"$g(x_0+h\cos{\alpha},y_0+h\cos{\beta})$", "$=$", r"$\frac{\partial f}{\partial x}$",
                         "$($", "$x$", "$+$", r"$\Delta h$",r"$\cos{\alpha}$", "$)$",  "$+$",
                         r"$\frac{\partial f}{\partial y}$",
                         "$($", "$y$", "$+$", r"$\Delta h$",r"$\cos{\beta}$", "$)$", "$+g_0$")
        g_any_line.font_size = 30
        dg_any_line = Tex(r"$\Delta g$", "$=$", r"$\frac{\partial f}{\partial x}$", r"$\Delta h$",r"$\cos{\alpha}$",
                                          "$+$",r"$\frac{\partial f}{\partial y}$", r"$\Delta h$",r"$\cos{\beta}$")
        dg_any_line.font_size = 30
        diff_g_any_line0 = Tex(r"$\frac{\Delta g}{\Delta h}$","$=$")
        diff_g_any_line1 = Tex(r"$\frac{\partial f}{\partial x}$",
                               r"$\cos{\alpha}$","$+$"r"$\frac{\partial f}{\partial y}$",r"$\cos{\beta}$")
        diff_g_any_line2 = Tex("$($",r"$\frac{\partial f}{\partial x}$",r"$\hat{\vec{i}}$","$+$",
                               r"$\frac{\partial f}{\partial y}$",r"$\hat{\vec{j}}$","$)$",r"$\cdot$",
                               "$($",r"$\cos{\alpha}$",r"$\hat{\vec{i}}$","$+$",r"$\cos{\beta}$",
                               r"$\hat{\vec{j}}$","$)$")
        diff_g_any_line3 = Tex(r"$\nabla$","$f$",r"$\cdot$",r"$\hat{\vec{e_h}}$")
        g_any_line.move_to([0, 2, 0])
        dg_any_line.next_to(g_any_line, DOWN)
        diff_g_any_line0.next_to(g_any_line, DOWN, buff=LARGE_BUFF).shift(3*LEFT)
        diff_g_any_line1.next_to(diff_g_any_line0, RIGHT, buff=SMALL_BUFF)
        diff_g_any_line2.next_to(diff_g_any_line0, RIGHT, buff=SMALL_BUFF)
        diff_g_any_line3.next_to(diff_g_any_line0, RIGHT, buff=SMALL_BUFF)
        # TODO M4.5
        self.play(TransformMatchingTex(g_line.copy(),g_any_line),**play_kw)
        self.wait()
        self.play(TransformMatchingTex(g_any_line.copy(),dg_any_line),**play_kw)
        self.wait()
        self.play(TransformMatchingTex(dg_any_line.copy(),VGroup(diff_g_any_line0,diff_g_any_line1)),**play_kw)
        self.wait()
        # TODO M4.6
        self.play(TransformMatchingTex(diff_g_any_line1,diff_g_any_line2),**play_kw)
        self.wait()
        self.play(TransformMatchingTex(diff_g_any_line2,diff_g_any_line3),**play_kw)
        self.wait()
        tip_line = Tex(r"当$\nabla f$与$\hat{\vec{e_n}}$同向时,$\frac{\Delta g}{\Delta h}$取最大值", tex_template=TexTemplateLibrary.ctex)
        tip_line.font_size = 30
        tip_line.next_to(diff_g_any_line3,DOWN,buff=SMALL_BUFF)
        self.play(Write(tip_line))
        self.wait()


class M6(Scene):
    """展示前进距离与学习率"""
    def construct(self):
        tex = Tex(r"$\Delta r $= ", r"$\alpha$", r"$\times \left \| \nabla f \right \| $")
        # TODO M6.1
        self.play(Write(tex))
        self.wait()
        alpha_tex = tex[1].set_color(PURPLE_B)
        # TODO M6.2
        self.play(Write(alpha_tex))
        self.wait()
        text = Text("学习率").set_color(PURPLE_B).next_to(alpha_tex,DOWN,buff=SMALL_BUFF)
        text.font_size = 30
        self.play(Write(text))
        self.wait()


class M9(Scene):
    """展示梯度定义式"""
    def construct(self):
        tex_lines = [MathTex(r"\nabla f(", "x_1", ",x_2", ")=",
                             r"\frac{\partial f}{\partial x_1} \hat{\vec{e_1}}", "+",
                             r"\frac{\partial f}{\partial x_2} \hat{\vec{e_2}}"),
                     MathTex(r"\nabla f(", "x_1", ",x_2", ",x_3", ")=",
                             r"\frac{\partial f}{\partial x_1} \hat{\vec{e_1}}", "+",
                             r"\frac{\partial f}{\partial x_2} \hat{\vec{e_2}}", "+",
                             r"\frac{\partial f}{\partial x_3} \hat{\vec{e_3}}"),
                     MathTex(r"\nabla f(", "x_1", ",x_2", ",x_3", ",x_4", ")=",
                             r"\frac{\partial f}{\partial x_1} \hat{\vec{e_1}}", "+",
                             r"\frac{\partial f}{\partial x_2} \hat{\vec{e_2}}", "+",
                             r"\frac{\partial f}{\partial x_3} \hat{\vec{e_3}}", "+",
                             r"\frac{\partial f}{\partial x_4} \hat{\vec{e_4}}"),
                     MathTex(r"\nabla f(", "x_1", ",x_2", ",x_3", ",x_4", ",x_5", ")=",
                             r"\frac{\partial f}{\partial x_1} \hat{\vec{e_1}}", "+",
                             r"\frac{\partial f}{\partial x_2} \hat{\vec{e_2}}", "+",
                             r"\frac{\partial f}{\partial x_3} \hat{\vec{e_3}}", "+",
                             r"\frac{\partial f}{\partial x_4} \hat{\vec{e_4}}", "+",
                             r"\frac{\partial f}{\partial x_5} \hat{\vec{e_5}}"),
                     ]
        '''批量修改字号'''
        for obj in tex_lines:
            obj.font_size = 30
        self.play(Write(tex_lines[0]))
        self.wait()
        # TODO M9.1
        for i in range(1,len(tex_lines)):
            self.play(TransformMatchingTex(tex_lines[i-1],tex_lines[i]))
            self.wait()
