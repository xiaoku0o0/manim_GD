此处提供梯度下降演示视频的全部manim源码，使用者可免费且无条件地使用所有开源内容。

[![cc0][cc0-image]][cc0]

[cc0]: https://creativecommons.org/public-domain/cc0/
[cc0-image]: https://licensebuttons.net/p/zero/1.0/88x31.png

[![Python](https://camo.githubusercontent.com/36a52016e02020b1b2b3a4b07812957a13bf404e03a8793f1793415a6a40be22/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d76332e31312d677265656e2e7376673f7374796c653d666c6174)](https://www.python.org/) [![manim](https://camo.githubusercontent.com/5d142d7c8431408522b6a907e828d11de85f9ff8e0d679b134dc5e3af1319886/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d616e696d2d76302e31382e302d677265656e2e7376673f7374796c653d666c6174)](https://github.com/3b1b/manim)



## 分镜表与代码清单

<!DOCTYPE html>
    <head>
        <meta charset="UTF-8">
    </head>
    <style type="text/css">
        body{margin: 0;}
        #table1 tbody tr:hover {
        background-color: rgb(226, 230, 255);
    }
    </style>
    <body>
        <table id="table1" width="99%" border="1px" style="border-collapse: collapse;" align="center">
            <caption>manim镜头分镜设计表</caption>
            <thead>
                <td align="center">镜号</td>
                <td align="center">开始时间<br>时:分:秒:帧</td>
                <td align="center">镜头</td>
                <td align="center" colspan="2">画面描述</td>
                <td align="center">文件名</td>
                <td align="center">py类名</td>
            </thead>
            <tbody>
                <!-- M1 -->
                <tr>
                    <td align="center" rowspan="2">M1</td>
                    <td align="center" rowspan="2">00:00:12:17</td>
                    <td rowspan="2">目标函数展示</td>
                    <td align="center">1</td>
                    <td>书写目标函数与当前坐标</td>
                    <td rowspan="2">S1</td>
                    <td rowspan="2">M1</td>
                </tr>
                <tr>
                    <td align="center">2</td>
                    <td>擦去目标函数</td>
                </tr>
                <!-- M2 -->
                <tr>
                    <td align="center" rowspan="4">M2</td>
                    <td align="center" rowspan="4">00:00:27:29</td>
                    <td rowspan="4">展示盲杖倾角和地面斜率的关系</td>
                    <td align="center">1</td>
                    <td>书写地面斜率计算公式</td>
                    <td rowspan="4">S2</td>
                    <td rowspan="4">M2</td>
                </tr>
                <tr>
                    <td align="center">2</td>
                    <td>盲杖倾角变至40°</td>
                </tr>
                <tr>
                    <td align="center">3</td>
                    <td>盲杖倾角变至10°</td>
                </tr>
                <tr>
                    <td align="center">4</td>
                    <td>盲杖倾角变至89°，同时盲杖长度变至2.01</td>
                </tr>
                <!-- M3 -->
                <tr>
                    <td align="center" rowspan="13">M3</td>
                    <td align="center" rowspan="13">00:00:59:23</td>
                    <td rowspan="13">展示曲面下的梯度</td>
                    <td align="center">1</td>
                    <td>摄像机拉进</td>
                    <td rowspan="13">S3</td>
                    <td rowspan="13">M3</td>
                </tr>
                <tr>
                    <td align="center">2</td>
                    <td>隐藏曲面，展示切平面</td>
                </tr>
                <tr>
                    <td align="center">3</td>
                    <td>绘制半径为h的圆</td>
                </tr>
                <tr>
                    <td align="center">4</td>
                    <td>展示向x正方向前进时的变化量</td>
                </tr>
                <tr>
                    <td align="center">5</td>
                    <td>展示向y正方向前进时的变化量</td>
                </tr>
                <tr>
                    <td align="center">6</td>
                    <td>展示向任意方向前进时的变化量</td>
                </tr>
                <tr>
                    <td align="center">7</td>
                    <td>书写alpha与beta角</td>
                </tr>
                <tr>
                    <td align="center">8</td>
                    <td>隐藏alpha与beta角</td>
                </tr>
                <tr>
                    <td align="center">9</td>
                    <td>展示向梯度方向前进时的变化量</td>
                </tr>
                <tr>
                    <td align="center">10</td>
                    <td>展示向负梯度方向前进时的变化量</td>
                </tr>
                <tr>
                    <td align="center">11</td>
                    <td>隐去切平面，展示曲面</td>
                </tr>
                <tr>
                    <td align="center">12</td>
                    <td>展示学习率为1.5时的变化量</td>
                </tr>
                <tr>
                    <td align="center">13</td>
                    <td>展示学习率为0.5时的变化量</td>
                </tr>
                <!-- M4 -->
                <tr>
                    <td align="center" rowspan="6">M4</td>
                    <td align="center" rowspan="6">00:01:03:09</td>
                    <td rowspan="6">展示曲面下梯度的推导过程</td>
                    <td align="center">1</td>
                    <td>书写切平面方程与偏导数</td>
                    <td rowspan="6">S1</td>
                    <td rowspan="6">M4</td>
                </tr>
                <tr>
                    <td align="center">2</td>
                    <td>推导出切平面方程</td>
                </tr>
                <tr>
                    <td align="center">3</td>
                    <td>书写沿x正方向前进时的变化量</td>
                </tr>
                <tr>
                    <td align="center">4</td>
                    <td>书写沿y正方向前进时的变化量</td>
                </tr>
                <tr>
                    <td align="center">5</td>
                    <td>书写沿任意方向前进时的变化量</td>
                </tr>
                <tr>
                    <td align="center">6</td>
                    <td>展示向量写法，引出梯度</td>
                </tr>
                <!-- M5 -->
                <tr>
                    <td align="center" rowspan="4">M5</td>
                    <td align="center" rowspan="4">00:02:09:02</td>
                    <td rowspan="4">展示不同位置前进的距离与切线斜率的关系</td>
                    <td align="center">1</td>
                    <td>绘制坐标轴与曲线</td>
                    <td rowspan="4">S4</td>
                    <td rowspan="4">M5</td>
                </tr>
                <tr>
                    <td align="center">2</td>
                    <td>绘制当前点、切线，书写当前导数</td>
                </tr>
                <tr>
                    <td align="center">3</td>
                    <td>点移至x=-0.2处</td>
                </tr>
                <tr>
                    <td align="center">4</td>
                    <td>点移至x=1.4处</td>
                </tr>
                <!-- M6 -->
                <tr>
                    <td align="center" rowspan="2">M6</td>
                    <td align="center" rowspan="2">00:02:33:01</td>
                    <td rowspan="2">引出学习率</td>
                    <td align="center">1</td>
                    <td>书写前进距离</td>
                    <td rowspan="2">S1</td>
                    <td rowspan="2">M6</td>
                </tr>
                <tr>
                    <td align="center">2</td>
                    <td>修改alpha颜色，书写“学习率”</td>
                </tr>
                <!-- M7 -->
                <tr>
                    <td align="center" rowspan="3">M7</td>
                    <td align="center" rowspan="3">00:02:40:06</td>
                    <td rowspan="3">一维梯度下降演示</td>
                    <td align="center">1</td>
                    <td>展示学习率为0.05时的GD过程</td>
                    <td rowspan="3">S4</td>
                    <td rowspan="3">M7</td>
                </tr>
                <tr>
                    <td align="center">2</td>
                    <td>展示学习率为1时的GD过程</td>
                </tr>
                <tr>
                    <td align="center">3</td>
                    <td>展示学习率为0.3时的GD过程</td>
                </tr>
                <!-- M8 -->
                <tr>
                    <td align="center" rowspan="1">M8</td>
                    <td align="center" rowspan="1">00:03:07:09</td>
                    <td rowspan="1">三维梯度下降演示</td>
                    <td align="center">1</td>
                    <td>展示三维GD过程</td>
                    <td rowspan="1">S5</td>
                    <td rowspan="1">M8</td>
                </tr>
                <!-- M9 -->
                <tr>
                    <td align="center" rowspan="1">M9</td>
                    <td align="center" rowspan="1">00:03:50:09</td>
                    <td rowspan="1">展示更多自变量下的梯度表达式</td>
                    <td align="center">1</td>
                    <td>展示更多自变量下的梯度表达式</td>
                    <td rowspan="1">S1</td>
                    <td rowspan="1">M9</td>
                </tr>
                <!-- M10 -->
                <tr>
                    <td align="center" rowspan="2">M10</td>
                    <td align="center" rowspan="2">00:04:09:24</td>
                    <td rowspan="2">多起点三维梯度下降演示</td>
                    <td align="center">1</td>
                    <td>展示多起点三维梯度下降演示</td>
                    <td rowspan="2">S5</td>
                    <td rowspan="2">M10</td>
                </tr>
                <tr>
                    <td align="center">2</td>
                    <td>隐去其他点，保留最小点的路径</td>
                </tr>
            </tbody>
        </table>
    </body>

## 渲染命令

```
manim S1.py M1
```

其中，S1.py为文件名，M1为类名

亦可在该文件下补充以下代码，直接运行文件：

```python
if __name__ == '__main__':
    import os
    os.system('manim S1.py M1')
```

