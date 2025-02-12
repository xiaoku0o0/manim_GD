from manim import *
import numpy as np


class M3(ThreeDScene):
    def construct(self):
        def func(x, y):
            """测试函数"""
            return (5 * ((y - (x ** 2) * 5.1 / (4 * np.pi ** 2) + 5 / np.pi * x - 6) ** 2 + 10 * (
                        1 - 1 / (8 * np.pi)) * np.cos(x)) + 20)/100
        axes = ThreeDAxes()
        init_point = np.array([5,12,func(5,12)])
        surface = Surface(
            lambda u,v:np.array([u,v,func(u,v)])-init_point,
            u_range=[-5,10],v_range=[0,15],
            checkerboard_colors=[BLUE_B,BLUE_C],
            resolution=(100,100),
            fill_opacity=0.9,
            stroke_opacity=0.9
        )
        self.set_camera_orientation(phi=75*DEGREES,theta=-120*DEGREES,zoom=0.4)
        self.add(surface)
        self.add(axes)
        self.wait()
        # TODO M3.1
        self.move_camera(zoom=4)    # 摄像机拉进
        self.wait()
        """绘制切平面"""
        h = 1e-7
        pian_f_x = (func(init_point[0]+h,init_point[1])-func(init_point[0],init_point[1]))/h
        pian_f_y = (func(init_point[0],init_point[1]+h)-func(init_point[0],init_point[1]))/h
        pian_f_z = -1
        def cut_plain_func(x,y):
            return (-pian_f_x * x - pian_f_y * y) / pian_f_z
        cut_plain = Surface(
            lambda u,v:np.array([u,
                                 v,
                                 cut_plain_func(u,v)]),
            u_range=[-2, 2], v_range=[-2, 2],
            checkerboard_colors=[YELLOW_B, YELLOW_C],
            resolution=(5, 5),
            fill_opacity=0.4,
            stroke_opacity=0.4
        )
        # TODO M3.2
        self.begin_3dillusion_camera_rotation(rate=0.1)
        self.play(FadeOut(surface),FadeIn(cut_plain))

        h_vt = ValueTracker(0.5)
        circle = Circle(radius=h_vt.get_value()).set_color(RED_E)
        # TODO M3.3
        self.play(Write(circle))
        self.wait()
        alpha_vt = ValueTracker(0)  # 单位：弧度
        dot_up = Dot3D(point=np.array([h_vt.get_value()*np.cos(alpha_vt.get_value()),
                                       h_vt.get_value()*np.sin(alpha_vt.get_value()),
                                       0]),
                       radius = 0.01).set_color(ORANGE)
        dot_down = Dot3D(point=np.array([h_vt.get_value()*np.cos(alpha_vt.get_value()),
                                         h_vt.get_value()*np.sin(alpha_vt.get_value()),
                                         cut_plain_func(h_vt.get_value()*np.cos(alpha_vt.get_value()),h_vt.get_value()*np.sin(alpha_vt.get_value()))]),
                         radius=0.01).set_color(ORANGE)
        arrow_h = Arrow3D(start=ORIGIN, end=dot_up.get_center(),
                          thickness=0.01,height=h_vt.get_value()/5,base_radius=0.03).set_color(YELLOW_D)
        arrow_down = Arrow3D(start=dot_up.get_center(), end=dot_down.get_center(),
                             thickness=0.01,height=h_vt.get_value()/5,base_radius=0.03).set_color(YELLOW_B)
        alpha_angle = Arc(
            angle=alpha_vt.get_value(),radius=0.3
        ).set_color(BLUE_E).add_updater(lambda x:x.become(Arc(angle=alpha_vt.get_value(),radius=0.3).set_color(BLUE_E)))
        alpha_angle.stroke_width = 0.2
        def show_delta_z_tex():
            '''展示z高度变化量'''
            temp = Tex(rf"$\Delta g$={dot_down.get_z()-dot_up.get_z():.3f}").set_color(YELLOW_B).next_to(arrow_down,buff=SMALL_BUFF)
            temp.font_size = 35
            return temp
        delta_z_tex = show_delta_z_tex()
        delta_z_tex.add_updater(lambda x:x.become(show_delta_z_tex()))
        # TODO M3.4
        self.add_fixed_orientation_mobjects(delta_z_tex)
        self.play(FadeIn(dot_up),FadeIn(dot_down),FadeIn(arrow_h),FadeIn(arrow_down), FadeIn(delta_z_tex),FadeIn(alpha_angle))
        self.wait()
        dot_up.add_updater(lambda x:x.become(Dot3D(point=np.array([h_vt.get_value()*np.cos(alpha_vt.get_value()),
                                                                   h_vt.get_value()*np.sin(alpha_vt.get_value()),
                                                                   0]),
                                                    radius=0.01).set_color(ORANGE)))
        dot_down.add_updater(lambda x:x.become(Dot3D(point=np.array([h_vt.get_value()*np.cos(alpha_vt.get_value()),
                                                                     h_vt.get_value()*np.sin(alpha_vt.get_value()),
                                                                     cut_plain_func(h_vt.get_value()*np.cos(alpha_vt.get_value()), h_vt.get_value()*np.sin(alpha_vt.get_value()))]),
                                                     radius=0.01).set_color(ORANGE)))
        arrow_h.add_updater(lambda x:x.become(Arrow3D(start=ORIGIN, end=dot_up.get_center(),
                                                      thickness=0.01,height=h_vt.get_value()/5,base_radius=0.03).set_color(YELLOW_D)))
        arrow_down.add_updater(lambda x:x.become(Arrow3D(start=dot_up.get_center(), end=dot_down.get_center(),
                                                         thickness=0.01,height=h_vt.get_value()/5,base_radius=0.03).set_color(YELLOW_B)))
        circle.add_updater(lambda x:x.become(Circle(radius=h_vt.get_value()).set_color(RED_E))) # 圆形更新
        # TODO M3.5
        self.stop_3dillusion_camera_rotation()
        self.move_camera(theta=50*DEGREES,added_anims=[alpha_vt.animate.set_value(90*DEGREES)],run_time=3)
        self.wait()
        # TODO M3.6
        self.move_camera(theta=-40*DEGREES,added_anims=[alpha_vt.animate.set_value(30 * DEGREES)],run_time=3)
        self.wait()
        beta_angle = Arc(start_angle=90*DEGREES,angle=90*DEGREES-alpha_vt.get_value(),radius=0.3
                         ).set_color(GREEN_E).add_updater(lambda x:x.become(Arc(start_angle=90*DEGREES,angle=alpha_vt.get_value()-90*DEGREES,radius=0.3)).set_color(GREEN_E))
        beta_angle.stroke_width = 0.2
        alpha_tex = Tex(r"$\alpha$").move_to(np.array([0.3,-0.2,0])).set_color(BLUE_A)
        beta_tex = Tex(r"$\beta$").move_to(np.array([-0.2,0.3,0])).set_color(GREEN_A)
        alpha_tex.font_size = 32
        beta_tex.font_size = 32
        # TODO M3.7
        self.add_fixed_orientation_mobjects(alpha_tex,beta_tex)
        self.play(Write(beta_angle),Write(alpha_tex),Write(beta_tex))
        self.wait()
        # TODO M3.8
        self.play(Unwrite(beta_angle),FadeOut(alpha_tex),FadeOut(beta_tex))
        self.wait()
        '''梯度展示'''
        # TODO M3.9
        self.move_camera(theta=-120*DEGREES,zoom=0.9,
                         added_anims=[alpha_vt.animate.set_value(np.arctan(pian_f_y/pian_f_x)),
                                      h_vt.animate.set_value((pian_f_x**2+pian_f_y**2)**0.5)],run_time=3)
        self.wait()
        # TODO M3.10
        self.play(alpha_vt.animate.set_value(np.arctan(pian_f_y / pian_f_x)+180*DEGREES),run_time=3)
        self.wait()
        dot_down2 = Dot3D(point=np.array([h_vt.get_value()*np.cos(alpha_vt.get_value()),
                                         h_vt.get_value()*np.sin(alpha_vt.get_value()),
                                         func(h_vt.get_value()*np.cos(alpha_vt.get_value())+init_point[0],
                                              h_vt.get_value()*np.sin(alpha_vt.get_value()))
                                          +init_point[1]-init_point[2]]),
                          radius=0.01).set_color(ORANGE)
        arrow_down2 = Arrow3D(start=dot_up.get_center(), end=dot_down2.get_center(),
                              thickness=0.01,height=h_vt.get_value()/5,base_radius=0.03).set_color(YELLOW_B)
        dot_down2.add_updater(lambda x:x.become(Dot3D(point=np.array([h_vt.get_value()*np.cos(alpha_vt.get_value()),
                                                      h_vt.get_value()*np.sin(alpha_vt.get_value()),
                                                      func(h_vt.get_value()*np.cos(alpha_vt.get_value())+init_point[0],h_vt.get_value()*np.sin(alpha_vt.get_value())+init_point[1])-init_point[2]]),
                                                      radius=0.01).set_color(ORANGE)))
        arrow_down2.add_updater(lambda x:x.become(Arrow3D(start=dot_up.get_center(), end=dot_down2.get_center(),
                                                          thickness=0.01,height=h_vt.get_value()/5,base_radius=0.03).set_color(YELLOW_B)))
        # TODO M3.11
        self.play(FadeOut(cut_plain), Unwrite(alpha_angle), Unwrite(circle), FadeOut(dot_down), FadeOut(delta_z_tex), FadeOut(arrow_down), FadeIn(surface))  # 回到曲面
        self.play(FadeIn(dot_down2), FadeIn(arrow_down2))
        # TODO M3.12
        self.play(h_vt.animate.set_value((pian_f_x**2+pian_f_y**2)**0.5 * 1.5),run_time=3)   # 展示变化量变大变小
        # TODO M3.13
        self.play(h_vt.animate.set_value((pian_f_x**2+pian_f_y**2)**0.5 * 0.5),run_time=3)
        self.wait()
