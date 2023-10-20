### Dingtalk Robot
Dingtalk Documents: 
* https://open.dingtalk.com/document/robots/customize-robot-security-settings
* https://open.dingtalk.com/document/robots/custom-robot-access

### Files:
* **main.py**: To handle the logic to send messages
* **robot.py**: Robot classes which implemented MDRobot and TextRobot. Each robot can send either Markdown content or Plain Text content.

### Quick Start:

In main.py

Import robots
```python
from robot import MDRobot, TextRobot
```
Initialize a robot
```python
md_robot = MDRobot("your secret", "your access token")
```
Note: According to the Document (https://open.dingtalk.com/document/robots/custom-robot-access), you can get access token from the webhook address, and get secret from the field of 加签.

```python
md_robot.send_message("""
#### 杭州天气
> 9度，西北风1级，空气良89，相对温度73%
> ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)
> ###### 10点20分发布 [天气](https://www.dingtalk.com) 
""")

text_robot.send_message("测试一下")
```

### Supported Markdown Format:
```text
支持以下格式：
标题
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题

引用
> A man who stands for nothing will fall for anything.

文字加粗、斜体
**bold**
*italic*

链接
[this is a link](http://name.com)

图片
![](http://name.com/pic.jpg)
```