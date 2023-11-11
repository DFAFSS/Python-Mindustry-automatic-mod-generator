#引用
import os
import zipfile
import time
import shutil
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
root = tk.Tk()
root.withdraw()
#变量
#初始化
Disposition = ""
create = 0
mod_type = 0
json_encode = ""

test = ""
initialize_name = ""
initialize_author = ""
initialize_description = ""
initialize_version = 136
initialize_minGameVersion = 136
#物品
item_name = ""
item_description = ""
item_hardness = 0
item_cost = 0
item_color = ""
item_healthScaling = 0
item_alwaysUnlocked = ""
item_alwaysUnlocked_1 = 0
item_radioactivity = 0
item_explosiveness = 0
item_flammability = 0
item_research = ""
#方块
block_type = 0
#墙
block_wall_steps = 0
block_wall_name = ""
block_wall_description = ""
block_wall_size = 0
block_wall_health = 0
block_wall_category = 0
block_wall_category_Str = ""
block_wall_jump_1 = True
block_wall_jump_1_Str = ""
block_wall_requirements = ""
block_wall_requirements_num = ""
block_wall_research = ""
#矿石
block_ore_steps = 0
block_ore_name = ""
block_ore_playerUnmineable = ""
block_ore_playerUnmineable_Str = ""
block_ore_variants = ""
block_ore_itemDrop = ""
block_ore_useColor = ""
block_ore_useColor_Str = ""
block_ore_mapColor = ""
block_ore_oreDefault = ""
block_ore_oreDefault_Str = ""
block_ore_oreThreshold = ""
block_ore_oreScale = ""

Turret_type = 0
#物品炮塔
Item_Turret_jump = True
Item_Turret_jump_item = True
Item_Turret_jumpStr = ""
Item_Turret_jump_item_Str = ""
Item_Turret_steps = 0
Item_Turret_name = ""
Item_Turret_description = ""
Item_Turret_shootSound = ""
Item_Turret_targetAirStr = ""
Item_Turret_targetAir = ""
Item_Turret_targetGroundStr = ""
Item_Turret_targetGround = ""
Item_Turret_health = ""
Item_Turret_reloadTime = ""
Item_Turret_size = ""
Item_Turret_spread = ""
Item_Turret_shootCone = ""
Item_Turret_recoilAmount = ""
Item_Turret_maxAmmo = ""
Item_Turret_rotateSpeed = ""
Item_Turret_inaccuracy = ""
Item_Turret_range = ""

Item_Turret_ammo_item = ""
Item_Turret_ammo_type = ""#暂时没用
Item_Turret_ammo_speed = ""
Item_Turret_ammo_damage = ""
Item_Turret_ammo_width = ""
Item_Turret_ammo_height = ""
Item_Turret_ammo_lifetime = ""

Item_Turret_requirements = ""
Item_Turret_requirements_item = ""

Item_Turret_category = ""
Item_Turret_category_Str = ""
Item_Turret_research = ""
#液体
liquid_steps = 0
liquid_name = ""
liquid_description = ""
liquid_color = ""
liquid_barColor = ""
liquid_flammability = ""
liquid_temperature = ""
liquid_heatCapacity = ""
liquid_viscosity = ""
liquid_explosiveness = ""
#函数
def file_write(row,content,File_address):
    """
    Args:
        row (_number_): _行数_
        content (_content_): _内容_
        File_address (_File_address_): _文件地址_
    """
    File = open(File_address, 'r')
    File_contents = File.readlines()
    if (len(File_contents) < row ):
        File_contents.insert(row,"null")
    File_contents[row-1] = content+'\n'
    File = open(File_address, 'w')
    File.writelines(File_contents)
    File.close()
    pass
def JSON_encoding(json_name,json_value,json_type,end):
    if (int(json_type) == 0):
        #中文自动转换成Unicode编码
        json_encode = (json_value.encode("unicode_escape"))
        json_value = str(json_encode)[2 : len(str(json_encode))-1]
        json_encode1 = json_value.split("\\\\")
        json_value = ""
        for json_num in range(len(json_encode1)):
            json_value += json_encode1[json_num]+"\\"
            pass
        json_value = json_value[0 : len(json_value)-1]
        JSON_value_put_0 = '"'+json_name+'":'+'"'+json_value+'"'
        pass
        #json编码
    if (int(json_type) == 1):
        JSON_value_put_0 = '"'+json_name+'":'+json_value
        pass
    if (int(end) == 0):
        JSON_value_put = JSON_value_put_0+','
        pass 
    if (int(end) == 1):
        JSON_value_put = JSON_value_put_0
        pass 
    return JSON_value_put
def zipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')
 
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))

if (not os.path.exists("disposition.txt")):
    test_1 = open("disposition.txt",'w')
    test_1.close()
    pass
else:
    test_1 = open("disposition.txt",'r')
    Disposition = test_1.read()
    test_1.close()
    pass
#file_write(行数,内容,文件地址)
#mod_name = Path("D:\VSCode代码\自动生成模组\disposition.txt").stem
#print(mod_name)
while True :
    test_1 = open("disposition.txt",'r')
    Disposition = test_1.read()
    test_1.close()
    create = int(input("创建模组:1 添加内容:2 导出模组:3"))
    if (create == 1):
        initialize_name = input("请输入名称")
        initialize_author = input("请输入模组作者")
        initialize_description = input("请输入简介")
        initialize_version = input("请输入游戏版本")
        initialize_minGameVersion = input("请输入模组最低游戏版本")
        os.mkdir(initialize_name)
        test = open(initialize_name+'\\'+'mod.json','w')
        test.close()
        test = open("disposition.txt",'w')
        test.write(initialize_name)
        test.close()
        test_1 = open("mod_mkdir",'w')
        test_1.close()
        test_1 = open("mod_mkdir",'r')
        if (not test_1.readline == 'true'):
            test = open("mod_mkdir",'w')
            test.write("true")
            os.makedirs(initialize_name + "\\content\\blocks")
            os.makedirs(initialize_name + "\\content\\items")
            os.makedirs(initialize_name + "\\content\\liquids")
            os.makedirs(initialize_name + "\\sprites\\blocks")
            os.makedirs(initialize_name + "\\sprites\\items")
            os.makedirs(initialize_name + "\\sprites\\liquids")
            pass
        test.close()
        test_1.close()
        
        file_write(1,"{",(initialize_name+"\\mod.json"))
        time.sleep(0.2)
        file_write(2,'"name"'+':'+'"'+initialize_name+'"'+',',(initialize_name+"\\mod.json"))
        time.sleep(0.2)
        file_write(3,'"author"'+':'+'"'+initialize_author+'"'+',',(initialize_name+"\\mod.json"))
        time.sleep(0.2)
        file_write(4,'"description"'+':'+'"'+initialize_description+'"'+',',(initialize_name+"\\mod.json"))
        time.sleep(0.2)
        file_write(5,'"version"'+':'+initialize_version+',',(initialize_name+"\\mod.json"))
        time.sleep(0.2)
        file_write(6,'"minGameVersion"'+':'+initialize_minGameVersion,(initialize_name+"\\mod.json"))
        time.sleep(0.2)
        file_write(7,"}",(initialize_name+"\\mod.json"))
        time.sleep(0.2)
        print("创建成功！")
        time.sleep(2)
        create = 0
        pass
    elif (create == 2):
        mod_type = int(input("物品:1 方块:2  液体:3"))
        if (mod_type == 1):
            item_name = input("请输入物品名称:")
            item_description = input("请输入物品简介:")
            item_hardness = input("请输入作为矿物时的钻探难度:")
            item_cost = input("请输入建造耗时:")
            item_color = input("请输入颜色(16进制颜色)")
            item_healthScaling = input("请输入影响方块的默认生命值:")
            item_alwaysUnlocked_1 = int(input ("默认是否解锁: 是:1 不是:2"))
            if (item_alwaysUnlocked_1 == 1):
                item_alwaysUnlocked = "true"
                pass
            elif (item_alwaysUnlocked_1 == 2):
                item_alwaysUnlocked = "false"
                pass
            item_radioactivity = (int(input("请输入放射性:")))/100
            item_explosiveness = (int(input("请输入爆炸性:")))/100
            item_flammability = (int(input("请输入可燃性:")))/100
            if (item_alwaysUnlocked_1 == 2):
                item_research = input("请输入科技树")
                pass
            #复制选中的文件，到指定文件夹并重命名
            print("请选择物品贴图")
            file_name = filedialog.askopenfilename()
            shutil.copy(file_name,Disposition+"\\sprites\\items")
            os.rename(Disposition+"\\sprites\\items\\"+(os.path.basename(file_name)),Disposition+"\\sprites\\items\\"+item_name+".png")
            test = open(Disposition+"\\content\\items\\"+item_name+".json",'w')
            test.close()
            #json生成
            file_write(1,"{",Disposition+"\\content\\items\\"+item_name+".json")
            file_write(2,'"name":'+'"'+item_name+'",',Disposition+"\\content\\items\\"+item_name+".json")
            file_write(3,'"description":'+'"'+item_description+'",',Disposition+"\\content\\items\\"+item_name+".json")
            file_write(4,'"hardness":'+item_hardness+',',Disposition+"\\content\\items\\"+item_name+".json")
            file_write(5,'"cost":'+item_cost+',',Disposition+"\\content\\items\\"+item_name+".json")
            file_write(6,'"color":'+'"'+item_color+'",',Disposition+"\\content\\items\\"+item_name+".json")
            file_write(7,'"healthScaling":'+item_healthScaling+',',Disposition+"\\content\\items\\"+item_name+".json")
            file_write(8,'"alwaysUnlocked":'+item_alwaysUnlocked+',',Disposition+"\\content\\items\\"+item_name+".json")
            file_write(9,'"radioactivity":'+str(item_radioactivity)+',',Disposition+"\\content\\items\\"+item_name+".json")
            file_write(10,'"explosiveness":'+str(item_explosiveness)+',',Disposition+"\\content\\items\\"+item_name+".json")
            file_write(11,'"flammability":'+str(item_flammability),Disposition+"\\content\\items\\"+item_name+".json")
            file_write(12,"}",Disposition+"\\content\\items\\"+item_name+".json")
            print("创建成功！")
            pass
        elif (mod_type == 2):
            block_type = int(input("墙:1 矿石:2 炮台:3"))
            if (block_type == 1):
                block_wall_steps = 2
                #名字
                block_wall_name = input("请输入名字:")
                test = open(Disposition+"\\content\\blocks\\"+block_wall_name+".json",'w')
                test.close()
                file_write((block_wall_steps-1),"{",Disposition+"\\content\\blocks\\"+block_wall_name+".json")
                file_write(block_wall_steps,JSON_encoding("name",block_wall_name,0,0),Disposition+"\\content\\blocks\\"+block_wall_name+".json")
                block_wall_steps += 1
                #简介
                block_wall_description = input("请输入简介")
                file_write(block_wall_steps,JSON_encoding("description",block_wall_description,0,0),Disposition+"\\content\\blocks\\"+block_wall_name+".json")
                block_wall_steps += 1
                #大小
                block_wall_size = (input("请输入大小:"))
                file_write(block_wall_steps,JSON_encoding("size",block_wall_size,1,0),Disposition+"\\content\\blocks\\"+block_wall_name+".json")
                block_wall_steps += 1
                #血量
                block_wall_health = (input("请输入血量:"))
                file_write(block_wall_steps,JSON_encoding("health",block_wall_health,1,0),Disposition+"\\content\\blocks\\"+block_wall_name+".json")
                block_wall_steps += 1
                #界面分类
                block_wall_category = (input("请输入分类子页面:\n炮塔子页面:1 钻头子页面:2 墙子页面:3 电力子页面:4\n逻辑子页面:5 单位子页面:6 液体子页面:7 传送带子页面:8\n 修复仪子页面:9"))
                if (block_wall_category == "1"):
                    block_wall_category_Str = "turret"
                    pass
                elif (block_wall_category == "2"):
                    block_wall_category_Str = "production"
                    pass
                elif (block_wall_category == "3"):
                    block_wall_category_Str = "defense"
                    pass
                elif (block_wall_category == "4"):
                    block_wall_category_Str = "power"
                    pass
                elif (block_wall_category == "5"):
                    block_wall_category_Str = "logic"
                    pass
                elif (block_wall_category == "6"):
                    block_wall_category_Str = "units"
                    pass
                elif (block_wall_category == "7"):
                    block_wall_category_Str = "liquid"
                    pass
                elif (block_wall_category == "8"):
                    block_wall_category_Str = "distribution"
                    pass
                elif (block_wall_category == "9"):
                    block_wall_category_Str = "effect"
                    pass
                file_write(block_wall_steps,JSON_encoding("category",block_wall_category_Str,0,0),Disposition+"\\content\\blocks\\"+block_wall_name+".json")
                block_wall_steps +=1
                file_write(block_wall_steps,'"requirements": [',Disposition+"\\content\\blocks\\"+block_wall_name+".json")
                block_wall_steps +=1
                #消耗
                while block_wall_jump_1:
                    block_wall_requirements = input("请输入消耗的物品:")
                    block_wall_requirements_num = input("请输入要消耗的数量")
                    file_write(block_wall_steps,'"'+block_wall_requirements+'/'+block_wall_requirements_num+'",',Disposition+"\\content\\blocks\\"+block_wall_name+".json")
                    block_wall_steps +=1
                    block_wall_jump_1_Str = input("是否继续添加: 是:1 否:2 ")
                    if (block_wall_jump_1_Str == "1"):
                        block_wall_jump_1 == True
                    elif (block_wall_jump_1_Str == "2"):
                        block_wall_jump_1 == False
                        file_write(block_wall_steps,"],",Disposition+"\\content\\blocks\\"+block_wall_name+".json")
                        block_wall_steps +=1
                        break
                #科技树
                block_wall_research = input("请输入科技树:")
                file_write(block_wall_steps,JSON_encoding("research",block_wall_research,0,0),Disposition+"\\content\\blocks\\"+block_wall_name+".json")
                block_wall_steps +=1
                #结尾
                print("请选择方块贴图:")
                file_name = filedialog.askopenfilename()
                shutil.copy(file_name,Disposition+"\\sprites\\blocks")
                os.rename(Disposition+"\\sprites\\blocks\\"+(os.path.basename(file_name)),Disposition+"\\sprites\\blocks\\"+block_wall_name+".png")
                file_write((block_wall_steps),'"type":"wall"',Disposition+"\\content\\blocks\\"+block_wall_name+".json")
                file_write(block_wall_steps+1,"}",Disposition+"\\content\\blocks\\"+block_wall_name+".json")
                pass
            elif (block_type == 2):
                block_ore_steps = 3
                #名字
                block_ore_name = input("请输入名字:")
                test = open(Disposition+"\\content\\blocks\\"+block_ore_name+".json",'w')
                test.close()
                file_write((block_ore_steps-2),"{",Disposition+"\\content\\blocks\\"+block_ore_name+".json")
                file_write((block_ore_steps-1),'"type":"OreBlock",',Disposition+"\\content\\blocks\\"+block_ore_name+".json")
                file_write(block_ore_steps,JSON_encoding("name",block_ore_name,0,0),Disposition+"\\content\\blocks\\"+block_ore_name+".json")
                block_ore_steps += 1
                #是否可以被单位挖掘
                block_ore_playerUnmineable_Str = input("单位是否可以被挖掘: 可以:1 不可以:2 ")
                if (block_ore_playerUnmineable_Str == "1"):
                    block_ore_playerUnmineable = "true"
                    pass 
                elif (block_ore_playerUnmineable_Str == "2"):
                    block_ore_playerUnmineable = "false"
                    pass
                file_write(block_ore_steps,JSON_encoding("playerUnmineable",block_ore_playerUnmineable,1,0),Disposition+"\\content\\blocks\\"+block_ore_name+".json")
                block_ore_steps += 1
                #贴图数量
                block_ore_variants = input("请输入贴图数量:")
                file_write(block_ore_steps,JSON_encoding("variants",block_ore_variants,1,0),Disposition+"\\content\\blocks\\"+block_ore_name+".json")
                block_ore_steps += 1
                #挖掘获得的矿物
                block_ore_itemDrop = input("请输入挖掘获得的物品:")
                file_write(block_ore_steps,JSON_encoding("itemDrop",block_ore_itemDrop,0,0),Disposition+"\\content\\blocks\\"+block_ore_name+".json")
                block_ore_steps += 1
                #地图颜色
                block_ore_mapColor = input("请输入地图颜色(十六进制):")
                file_write(block_ore_steps,JSON_encoding("mapColor",block_ore_mapColor,0,0),Disposition+"\\content\\blocks\\"+block_ore_name+".json")
                block_ore_steps += 1
                #是否启用颜色
                block_ore_useColor_Str = input("是否启用颜色: 启用:1 不启用:2 ")
                if (block_ore_useColor_Str == "1"):
                    block_ore_useColor = "true"
                    pass 
                elif (block_ore_useColor_Str == "2"):
                    block_ore_useColor = "false"
                    pass
                pass
                file_write(block_ore_steps,JSON_encoding("useColor",block_ore_useColor,1,0),Disposition+"\\content\\blocks\\"+block_ore_name+".json")
                block_ore_steps += 1
                #默认生成
                block_ore_oreDefault_Str = input("默认生成: 生成:1 不生成:2 ")
                if (block_ore_oreDefault_Str == "1"):
                    block_ore_oreDefault = "true"
                    pass 
                elif (block_ore_oreDefault_Str == "2"):
                    block_ore_oreDefault = "false"
                    pass
                pass
                file_write(block_ore_steps,JSON_encoding("oreDefault",block_ore_oreDefault,1,0),Disposition+"\\content\\blocks\\"+block_ore_name+".json")
                block_ore_steps += 1
                #矿石生成阈值
                block_ore_oreThreshold = input("请输入矿石生成阈值:")
                file_write(block_ore_steps,JSON_encoding("oreThreshold",block_ore_oreThreshold,1,0),Disposition+"\\content\\blocks\\"+block_ore_name+".json")
                block_ore_steps += 1
                #矿石生成规模
                block_ore_oreScale = input("请输入矿石生成规模:")
                file_write(block_ore_steps,JSON_encoding("oreScale",block_ore_oreScale,1,1),Disposition+"\\content\\blocks\\"+block_ore_name+".json")
                block_ore_steps += 1
                #结尾
                for Number_of_maps in range(int(block_ore_variants)):
                    print("请选择矿石贴图--"+str(Number_of_maps+1))
                    file_name = filedialog.askopenfilename()
                    shutil.copy(file_name,Disposition+"\\sprites\\blocks")
                    os.rename(Disposition+"\\sprites\\blocks\\"+(os.path.basename(file_name)),Disposition+"\\sprites\\blocks\\"+block_ore_name+str(Number_of_maps+1)+".png")
                    pass
                file_write(block_ore_steps,"}",Disposition+"\\content\\blocks\\"+block_ore_name+".json")
                pass
            elif (block_type == 3):
                #炮台制作（极为困难）
                Turret_type = int(input("物品炮台:1 液体炮台:2"))
                if (Turret_type == 1):
                    #物品炮台
                    #名字
                    Item_Turret_steps = 3
                    Item_Turret_name = input("请输入名字:")
                    test = open(Disposition+"\\content\\blocks\\"+Item_Turret_name+".json",'w')
                    test.close()
                    file_write(Item_Turret_steps-2,"{",Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    file_write(Item_Turret_steps-1,'"type": "ItemTurret",',Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    file_write(Item_Turret_steps,JSON_encoding("name",Item_Turret_name,0,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #简介
                    Item_Turret_description = input("请输入简介:")
                    file_write(Item_Turret_steps,JSON_encoding("description",Item_Turret_description,0,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #炮台声音
                    Item_Turret_shootSound = input("请输入炮台声音:")
                    file_write(Item_Turret_steps,JSON_encoding("shootSound",Item_Turret_shootSound,0,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #是否攻击空军
                    Item_Turret_targetAirStr = input("是否攻击空军: 是:1 不是:2")
                    if (Item_Turret_targetAirStr == "1"):
                        Item_Turret_targetAir = "true"
                        pass
                    elif (Item_Turret_targetAirStr == "2"):
                        Item_Turret_targetAir = "false"
                        pass
                    file_write(Item_Turret_steps,JSON_encoding("targetAir",Item_Turret_targetAir,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #是否攻击陆军
                    Item_Turret_targetGroundStr = input("是否攻击陆军: 是:1 不是:2")
                    if (Item_Turret_targetGroundStr == "1"):
                        Item_Turret_targetGround = "true"
                        pass
                    elif (Item_Turret_targetGroundStr == "2"):
                        Item_Turret_targetGround = "false"
                        pass
                    file_write(Item_Turret_steps,JSON_encoding("targetGround",Item_Turret_targetGround,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #血量
                    Item_Turret_health = input("请输入血量:")
                    file_write(Item_Turret_steps,JSON_encoding("health",Item_Turret_health,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #射速
                    Item_Turret_reloadTime = input("请输入射速:")
                    file_write(Item_Turret_steps,JSON_encoding("reloadTime",Item_Turret_reloadTime,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #尺寸
                    Item_Turret_size = input("请输入尺寸:")
                    file_write(Item_Turret_steps,JSON_encoding("size",Item_Turret_size,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #炮口
                    Item_Turret_shootCone = input("请输入炮口尺寸:")
                    file_write(Item_Turret_steps,JSON_encoding("shootCone",Item_Turret_shootCone,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #后坐力
                    Item_Turret_recoilAmount = input("请输入后坐力:")
                    file_write(Item_Turret_steps,JSON_encoding("recoilAmount",Item_Turret_recoilAmount,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #弹夹容量
                    Item_Turret_maxAmmo = input("请输入弹夹容量:")
                    file_write(Item_Turret_steps,JSON_encoding("maxAmmo",Item_Turret_maxAmmo,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #炮口转速
                    Item_Turret_rotateSpeed = input("请输入炮口转速:")
                    file_write(Item_Turret_steps,JSON_encoding("rotateSpeed",Item_Turret_rotateSpeed,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #子弹偏移
                    Item_Turret_inaccuracy = input("请输入子弹偏移:")
                    file_write(Item_Turret_steps,JSON_encoding("inaccuracy",Item_Turret_inaccuracy,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #检测范围
                    Item_Turret_range = input("请输入炮台检测范围:")
                    file_write(Item_Turret_steps,JSON_encoding("range",Item_Turret_range,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #子弹部分（困难）
                    file_write(Item_Turret_steps,'"ammoTypes":{',Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    while Item_Turret_jump:
                        #子弹物品
                        Item_Turret_ammo_item = input("请输入子弹物品")
                        file_write(Item_Turret_steps,'"'+Item_Turret_ammo_item+'":{',Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                        Item_Turret_steps += 1
                        #射速
                        Item_Turret_ammo_speed = input("请输入子弹射速")
                        file_write(Item_Turret_steps,JSON_encoding("speed",Item_Turret_ammo_speed,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                        Item_Turret_steps += 1
                        #伤害
                        Item_Turret_ammo_damage = input("请输入子弹伤害")
                        file_write(Item_Turret_steps,JSON_encoding("damage",Item_Turret_ammo_damage,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                        Item_Turret_steps += 1
                        #子弹宽度
                        Item_Turret_ammo_width = input("请输入子弹宽度")
                        file_write(Item_Turret_steps,JSON_encoding("width",Item_Turret_ammo_width,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                        Item_Turret_steps += 1
                        #子弹高度
                        Item_Turret_ammo_height = input("请输入子弹高度")
                        file_write(Item_Turret_steps,JSON_encoding("height",Item_Turret_ammo_height,1,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                        Item_Turret_steps += 1
                        #子弹存在时间
                        Item_Turret_ammo_lifetime = input("请输入子弹存在时间")
                        file_write(Item_Turret_steps,JSON_encoding("lifetime",Item_Turret_ammo_lifetime,1,1),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                        Item_Turret_steps += 1
                        #结尾
                        file_write(Item_Turret_steps,'},',Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                        Item_Turret_steps += 1
                        Item_Turret_jumpStr = input("是否继续添加 继续:1 不:2")
                        if (Item_Turret_jumpStr == "1"):
                            Item_Turret_jump = True
                            print("继续")
                        elif (Item_Turret_jumpStr == "2"):
                            Item_Turret_jump = False
                            file_write(Item_Turret_steps,'},',Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                            Item_Turret_steps += 1
                            print("取消")
                            break
                    #物品消耗
                    file_write(Item_Turret_steps,'"requirements": [',Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps +=1
                    while Item_Turret_jump_item:
                        Item_Turret_requirements_item = input("请输入消耗的物品:")
                        Item_Turret_requirements = input("请输入要消耗的数量")
                        file_write(Item_Turret_steps,'"'+Item_Turret_requirements_item+'/'+Item_Turret_requirements+'",',Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                        Item_Turret_steps +=1
                        Item_Turret_jump_item_Str = input("是否继续添加: 是:1 否:2 ")
                        if (Item_Turret_jump_item_Str == "1"):
                            Item_Turret_jump_item = True
                        elif (Item_Turret_jump_item_Str == "2"):
                            Item_Turret_jump_item = False
                            file_write(Item_Turret_steps,"],",Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                            Item_Turret_steps +=1
                            break
                    #界面分类
                    Item_Turret_category_Str = (input("请输入分类子页面:\n炮塔子页面:1 钻头子页面:2 墙子页面:3 电力子页面:4\n逻辑子页面:5 单位子页面:6 液体子页面:7 传送带子页面:8\n 修复仪子页面:9"))
                    if (Item_Turret_category_Str == "1"):
                        Item_Turret_category = "turret"
                        pass
                    elif (Item_Turret_category_Str == "2"):
                        Item_Turret_category = "production"
                        pass
                    elif (Item_Turret_category_Str == "3"):
                        Item_Turret_category = "defense"
                        pass
                    elif (Item_Turret_category_Str == "4"):
                        Item_Turret_category = "power"
                        pass
                    elif (Item_Turret_category_Str == "5"):
                        Item_Turret_category = "logic"
                        pass
                    elif (Item_Turret_category_Str == "6"):
                        Item_Turret_category = "units"
                        pass
                    elif (Item_Turret_category_Str == "7"):
                        Item_Turret_category = "liquid"
                        pass
                    elif (Item_Turret_category_Str == "8"):
                        Item_Turret_category = "distribution"
                        pass
                    elif (Item_Turret_category_Str == "9"):
                        Item_Turret_category = "effect"
                        pass
                    file_write(Item_Turret_steps,JSON_encoding("category",Item_Turret_category,0,0),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps +=1
                    #科技树
                    Item_Turret_research = input("请输入研究:")
                    file_write(Item_Turret_steps,JSON_encoding("research",Item_Turret_research,0,1),Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    Item_Turret_steps += 1
                    #结尾
                    file_write(Item_Turret_steps,"}",Disposition+"\\content\\blocks\\"+Item_Turret_name+".json")
                    print("请选择炮台贴图")
                    file_name = filedialog.askopenfilename()
                    shutil.copy(file_name,Disposition+"\\sprites\\blocks")
                    os.rename(Disposition+"\\sprites\\blocks\\"+(os.path.basename(file_name)),Disposition+"\\sprites\\blocks\\"+Item_Turret_name+".png")
                    print("生成完毕")
                    pass
                pass
        elif (mod_type == 3):
            liquid_steps = 2
            #名字
            liquid_name = input("请输入名字:")
            test = open(Disposition+"\\content\\liquids\\"+liquid_name+".json",'w')
            test.close()
            file_write(liquid_steps-1,"{",Disposition+"\\content\\liquids\\"+liquid_name+".json")
            file_write(liquid_steps,JSON_encoding("name",liquid_name,0,0),Disposition+"\\content\\liquids\\"+liquid_name+".json")
            liquid_steps += 1
            #简介
            liquid_description = input("请输入简介:")
            file_write(liquid_steps,JSON_encoding("description",liquid_description,0,0),Disposition+"\\content\\liquids\\"+liquid_name+".json")
            liquid_steps += 1
            #颜色
            liquid_color = input("请输入颜色:")
            file_write(liquid_steps,JSON_encoding("color",liquid_color,0,0),Disposition+"\\content\\liquids\\"+liquid_name+".json")
            liquid_steps += 1
            #颜色条
            liquid_barColor = input("请输入颜色条:")
            file_write(liquid_steps,JSON_encoding("barcolor",liquid_barColor,0,0),Disposition+"\\content\\liquids\\"+liquid_name+".json")
            liquid_steps += 1
            #流速
            liquid_viscosity = input("请输入流速:")
            file_write(liquid_steps,JSON_encoding("viscosity",liquid_viscosity,1,0),Disposition+"\\content\\liquids\\"+liquid_name+".json")
            liquid_steps += 1
            #爆炸性
            liquid_explosiveness = input("请输入爆炸性:")
            file_write(liquid_steps,JSON_encoding("explosiveness",liquid_explosiveness,1,0),Disposition+"\\content\\liquids\\"+liquid_name+".json")
            liquid_steps += 1
            #易燃性
            liquid_flammability = input("请输入易燃性:")
            file_write(liquid_steps,JSON_encoding("flammability",liquid_flammability,1,0),Disposition+"\\content\\liquids\\"+liquid_name+".json")
            liquid_steps += 1
            #温度
            liquid_temperature = input("请输入温度:")
            file_write(liquid_steps,JSON_encoding("temperature",liquid_temperature,1,0),Disposition+"\\content\\liquids\\"+liquid_name+".json")
            liquid_steps += 1
            #热比容
            liquid_heatCapacity = input("请输入热比容:")
            file_write(liquid_steps,JSON_encoding("heatCapacity",liquid_heatCapacity,1,1),Disposition+"\\content\\liquids\\"+liquid_name+".json")
            liquid_steps += 1
            #结尾
            print("请选择液体贴图:")
            file_name = filedialog.askopenfilename()
            shutil.copy(file_name,Disposition+"\\sprites\\liquids")
            os.rename(Disposition+"\\sprites\\liquids\\"+(os.path.basename(file_name)),Disposition+"\\sprites\\liquids\\"+liquid_name+".png")
            file_write(liquid_steps,"}",Disposition+"\\content\\liquids\\"+liquid_name+".json")
            print("生成完毕")
            pass
    elif (create == 3):
        File_askdirectory = filedialog.askdirectory()
        zipDir(Disposition,File_askdirectory+'\\'+Disposition+".zip")
        print("导出成功")
        pass

