import random

# 生成随机值
random_taus = [random.uniform(0.8, 1.5) for _ in range(8)]

# 构建路由文件内容
route_file_content = f'''
<routes>
<vType accel="1.0" decel="1.5" id="Car" length="5.0" delta="4.0" maxSpeed="15" carFollowModel="IDM" minGap="2" />

<route id="r1" edges="edge1"/>
'''
for i, tau in enumerate(random_taus): 
    route_file_content += f'''
<vehicle depart='0.0' departPos="{100-10*i}" id="veh{i}" route="r1" type="Car" departSpeed="0" tau = "{tau}"/>'''

route_file_content +='''

</routes>
'''

# 将内容写入路由文件
with open('sumo_test2.rou.xml', 'w') as file:
    file.write(route_file_content)
