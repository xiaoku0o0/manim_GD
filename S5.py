from manim import *
import numpy as np


class M8(ThreeDScene):
    def construct(self):
        def func(x, y):
            """测试函数"""
            return (5 * ((y - (x ** 2) * 5.1 / (4 * np.pi ** 2) + 5 / np.pi * x - 6) ** 2 + 10 * (
                        1 - 1 / (8 * np.pi)) * np.cos(x)) + 20)/100
        x_lim = [-5, 10]
        y_lim = [0, 15]
        axes = ThreeDAxes(x_range=(*x_lim,2),y_range=(*y_lim,2))
        init_point = np.array([5, 12, func(5, 12)])
        surface = Surface(
            lambda u, v: np.array([u, v, func(u, v)]),
            u_range=x_lim, v_range=y_lim,
            checkerboard_colors=[BLUE_B, BLUE_C],
            resolution=(100, 100),
            fill_opacity=0.9,
            stroke_opacity=0.9
        )
        BOLL_COLOR = PURPLE_E
        BOLL_RADIUS = 0.04
        self.set_camera_orientation(phi=50 * DEGREES, theta=-100 * DEGREES, zoom=1)
        dot_beg = Dot3D(point=init_point,radius=BOLL_RADIUS).set_color(BOLL_COLOR)
        self.add(dot_beg)
        self.move_camera(frame_center=dot_beg.get_center())
        self.remove(dot_beg)
        self.play(Write(axes),Write(surface))
        self.play(Write(dot_beg))
        self.wait()
        dot_queue = [dot_beg]  # 路线上点的queue
        x_vt = ValueTracker(dot_beg.get_x())  # x坐标
        y_vt = ValueTracker(dot_beg.get_y())  # y坐标
        alpha_vt = ValueTracker(0.5)    # 学习率
        times_vt = ValueTracker(0)      # 迭代次数
        def show_label():
            label = Tex(rf"$\alpha$={alpha_vt.get_value():.2f},"+f"当前坐标({x_vt.get_value():.2f}, {y_vt.get_value():.2f}, {func(x_vt.get_value(),y_vt.get_value()):.4f}),迭代次数{times_vt.get_value():.0f}",
                        tex_template=TexTemplateLibrary.ctex).to_edge(UL,buff=0.05).set_color(RED_D)
            label.font_size = 30
            return label
        label = show_label()
        label.add_updater(lambda x:x.become(show_label()))
        self.add_fixed_in_frame_mobjects(label)
        self.wait()
        def func_grad(x,y):
            '''求数值负梯度，返回ndarray'''
            h = 0.1
            return np.array([-(func(x+h,y)-func(x,y))/h,
                             -(func(x,y+h)-func(x,y))/h])
        while np.linalg.norm(func_grad(x_vt.get_value(),y_vt.get_value())) > 0.1:    # np.linalg.norm求范数
            x_will, y_will = alpha_vt.get_value()*func_grad(x_vt.get_value(),y_vt.get_value()) + \
                             np.array([dot_queue[-1].get_x(),dot_queue[-1].get_y()])
            dot_queue.append(Dot3D(point=np.array([x_will,y_will,func(x_will,y_will)]),
                                   radius=BOLL_RADIUS).set_color(BOLL_COLOR))
            x_vt.set_value(x_will)
            y_vt.set_value(y_will)
            # TODO M8.1
            self.move_camera(frame_center=dot_queue[-1].get_center(),added_anims=[FadeIn(dot_queue[-1])])
            times_vt.set_value(times_vt.get_value()+1)
            self.wait(0.1)
            if x_vt.get_value()>x_lim[1] or x_vt.get_value()<x_lim[0] or y_vt.get_value()>y_lim[1] or y_vt.get_value()<y_lim[0]:
                break
        self.wait(2)


class gd_info():
    """M10分镜需要用到此class"""
    def add_point(self,point_add):
        point_add_3dim = np.array([*point_add,self.func(*point_add)])
        self.dot_queue.append(Dot3D(point=point_add_3dim,radius=0.04,color=self.color))
        self.point_queue.append(point_add)
    def __init__(self,color,tex_color,alpha,init_point,func):
        self.color = color
        self.tex_color = tex_color
        self.alpha = alpha
        self.init_point = init_point
        self.dot_queue = []
        self.point_queue = []   # 含x,y的ndarray
        self.func = func
        self.add_point(init_point)
        self.finish = False
    def get_grad(self,point) -> np.ndarray:
        '''计算负梯度'''
        h = 0.01
        func = self.func
        pian_x = (func(point[0]+h,point[1]) - func(point[0],point[1]))/h
        pian_y = (func(point[0],point[1]+h) - func(point[0],point[1]))/h
        return -np.array([pian_x,pian_y])
    def get_next_point(self) -> np.ndarray:
        '''获得下一点'''
        grad = self.get_grad(self.point_queue[-1])
        x_will = self.point_queue[-1][0] + self.alpha * grad[0]
        y_will = self.point_queue[-1][1] + self.alpha * grad[1]
        return np.array([x_will,y_will])
    def iteration(self) -> Dot3D:
        '''迭代一次，返回点对象'''
        if self.finish:
            return None
        self.add_point(self.get_next_point())
        if np.linalg.norm(self.get_grad(self.point_queue[-1])) < 0.0001:
            self.finish = True
        return self.dot_queue[-1]


class M10(ThreeDScene):
    """3D多起点梯度下降"""
    def construct(self):
        x_lim = [0,10]
        y_lim = [-5,0]
        axes = ThreeDAxes(
            x_range=(*x_lim,1),y_range=(*y_lim,0.5),z_range=(-10,25,5)
        )
        def func(x,y):
            return x*y*np.cos(np.sin(x))*np.sin(np.cos(y))/10
        surface = Surface(
            lambda u,v:np.array([u,v,func(u,v)]),
            u_range=[0,10],v_range=[-7,2],
            checkerboard_colors=[BLUE_B, BLUE_C],
            resolution=(100, 100),
            fill_opacity=0.9,
            stroke_opacity=0.9
        )
        number = 4
        color_map = [YELLOW_D,RED_D,PURPLE_D,MAROON_D]
        tex_color_map = [YELLOW_E,RED_E,PURPLE_E,MAROON_E]
        init_point = [(6,-3),(2.7,-3.2),(7.1,-3.2),(9.3,-2.9)]  # 初始点
        alpha_ls = [0.8,3,1,0.5]    # 每个点设定不同的学习率
        gd_infp_ls = [gd_info(color_map[i],tex_color_map[i],alpha_ls[i],np.array(init_point[i]),func) for i in range(number)]
        def get_z_tex_ls():
            res = []
            for i in range(number):
                temp = MathTex(f"z={func(*gd_infp_ls[i].point_queue[-1]):.3f}",
                               color=gd_infp_ls[i].tex_color).next_to(gd_infp_ls[i].dot_queue[-1].get_center(),
                                                                  direction=OUT, buff=0.5)
                temp.font_size = 30
                self.add_fixed_orientation_mobjects(temp)
                res.append(temp)
            return res
        z_tex_ls = get_z_tex_ls()
        self.set_camera_orientation(theta=125*DEGREES,phi=30*DEGREES,zoom=1)
        self.move_camera(frame_center=axes.coords_to_point(8,-3,18))
        self.add(axes, surface, *z_tex_ls, *(gd_infp_ls[i].dot_queue[0] for i in range(number)))
        times = ValueTracker(0)
        def times_text_flash():
            temp = Tex(f"迭代次数:{times.get_value():.0f}",tex_template=TexTemplateLibrary.ctex,color=BLUE_A).to_edge(UL,buff=SMALL_BUFF)
            temp.font_size = 30
            return temp
        times_text = times_text_flash()
        times_text.add_updater(lambda x:x.become(times_text_flash()))
        self.add_fixed_in_frame_mobjects(times_text)
        while True:
            '''判断是否所有点都完成迭代'''
            flag = True
            for grad_info in gd_infp_ls:
                if not grad_info.finish:
                    flag = False
                    break
            if flag:
                break
            '''迭代次数显示更新'''
            times.set_value(times.get_value()+1)
            '''每个点迭代'''
            dot_ls = []
            for i in range(number):
                add_will = gd_infp_ls[i].iteration()
                if add_will is not None:
                    dot_ls.append(add_will)
            '''动画部分'''
            write_dot_an = [FadeIn(dot_ls[i]) for i in range(len(dot_ls))]
            out_tex_an = [z_tex_ls[i] for i in range(len(z_tex_ls))]
            # TODO M10.1
            self.play(*write_dot_an)
            self.remove(*out_tex_an)
            z_tex_new = get_z_tex_ls()
            z_tex_ls = z_tex_new[:]
            self.wait()
        '''寻找最小值'''
        min_idx = 0
        for i in range(1,number):
            if func(*gd_infp_ls[i].point_queue[-1]) < func(*gd_infp_ls[min_idx].point_queue[-1]):
                min_idx = i
        '''隐藏其他点'''
        oper_obj = []
        for i in range(number):
            if i == min_idx:
                continue
            oper_obj.extend(gd_infp_ls[i].dot_queue)
            oper_obj.append(z_tex_ls[i])
        # TODO M10.2
        self.play(*(FadeOut(oper_obj[i]) for i in range(len(oper_obj))))
        self.wait()
