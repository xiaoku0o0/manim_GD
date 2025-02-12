from manim import *
import numpy as np


class M2(Scene):
    """盲杖倾角与斜率的关系"""
    def construct(self):
        alpha_value = ValueTracker(30)
        length_value = ValueTracker(4)
        """图形部分"""
        head_dot = np.array([1,2,0])
        foot_dot = np.array([1,0,0])
        body_line = Line(head_dot,foot_dot).set_color(YELLOW_E)
        stick_end_point_init = np.array([-3,2,0])
        stick_line = Line(head_dot,stick_end_point_init).set_color(YELLOW_C)
        # stick_line_ref = stick_line.copy()
        stick_line.rotate(alpha_value.get_value() * DEGREES, about_point=head_dot)
        angle_arc_alpha = Angle(stick_line, body_line, radius=0.5, other_angle=False)
        tex_alpha = MathTex(r"\alpha").move_to(
            Angle(stick_line,body_line,radius=0.5+3*SMALL_BUFF,other_angle=False).point_from_proportion(0.5)
        )
        ground_line = Line(foot_dot+300*(stick_line.get_end()-foot_dot),foot_dot-300*(stick_line.get_end()-foot_dot)).set_color(BLUE_A)
        self.add(stick_line, body_line, angle_arc_alpha, tex_alpha,ground_line)
        self.wait()
        '''盲杖旋转'''
        stick_line.add_updater(
            lambda x: x.become(Line(head_dot,head_dot-np.array([length_value.get_value(),0,0]))).set_color(YELLOW_C).rotate(
                alpha_value.get_value() * DEGREES, about_point=head_dot
            )
        )
        '''angle更新'''
        angle_arc_alpha.add_updater(
            lambda x: x.become(Angle(stick_line, body_line, radius=0.5, other_angle=False,quadrant=(1,1)))
        )
        '''tex更新'''
        tex_alpha.add_updater(
            lambda x: x.move_to(
                Angle(stick_line,body_line,radius=0.5+3*SMALL_BUFF,other_angle=False).point_from_proportion(0.5)
            )
        )
        '''地面更新'''
        ground_line.add_updater(
            lambda x:x.become(Line(foot_dot+300*(stick_line.get_end()-foot_dot),foot_dot-300*(stick_line.get_end()-foot_dot)).set_color(BLUE_A))
        )
        """表达式部分"""
        alpha = 90 - alpha_value.get_value()
        theta = 180/np.pi*np.arctan((stick_line.get_length()*np.cos(alpha*np.pi/180)-body_line.get_length())/(stick_line.get_length()*np.sin(alpha*np.pi/180)))
        func_tex = Tex(r"地面斜率$\tan{\theta} = \frac{l\cos{\alpha}-h}{l\sin{\alpha}}$", tex_template=TexTemplateLibrary.ctex)
        func_explain = Tex(r"式中$l$为盲杖长度，$h$为手离地高度", tex_template=TexTemplateLibrary.ctex)
        func_tex.font_size = 30
        func_explain.font_size = 30
        group1 = VGroup(func_tex, func_explain)
        group1.arrange(DOWN,aligned_edge=LEFT).move_to([-3,-3,0])
        func_frame_box = SurroundingRectangle(func_tex, buff=0.1)
        alpha_tex = MathTex(r"\alpha = {:.2f}^\circ".format(alpha))
        theta_tex = MathTex(r"\theta = {:.2f}^\circ".format(theta))
        group2 = VGroup(alpha_tex,theta_tex)
        group2.arrange(DOWN,aligned_edge=LEFT).move_to([3,-3,0])
        alpha_tex_ref = alpha_tex.copy()
        theta_tex_ref = theta_tex.copy()
        # TODO M2.1
        self.play(Write(func_tex))
        self.play(Create(func_frame_box), Write(func_explain),Write(alpha_tex),Write(theta_tex))
        '''数值更新'''
        alpha_tex.add_updater(
            lambda x:x.become(MathTex(r"\alpha = {:.2f}^\circ".format(90 - alpha_value.get_value())).move_to(alpha_tex_ref.get_point_mobject()))
        )
        theta_tex.add_updater(
            lambda x:x.become(MathTex(r"\theta = {:.2f}^\circ".format(180/np.pi*np.arctan((stick_line.get_length()*np.cos((90 - alpha_value.get_value())*np.pi/180)-body_line.get_length())/(stick_line.get_length()*np.sin((90 - alpha_value.get_value())*np.pi/180)))))).move_to(theta_tex_ref.get_point_mobject())
        )
        self.wait()
        # TODO M2.2
        self.play(alpha_value.animate.set_value(40))
        self.wait()
        # TODO M2.3
        self.play(alpha_value.animate.set_value(10))
        self.wait()
        # TODO M2.4
        self.play(alpha_value.animate.set_value(89),length_value.animate.set_value(2.01))
        self.wait()
