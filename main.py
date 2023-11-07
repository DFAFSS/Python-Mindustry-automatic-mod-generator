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

#函数
def file_write(row,content,File_address):
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
        JSON_value_put_0 = '"'+json_name+'":'+'"'+json_value+'"'
        pass
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
            os.makedirs(initialize_name + "\\sprites\\blocks")
            os.makedirs(initialize_name + "\\sprites\\items")
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
        mod_type = int(input("物品:1 方块:2"))
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
            block_type = int(input("墙:1 矿石:2"))
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
        pass
    elif (create == 3):
        File_askdirectory = filedialog.askdirectory()
        zipDir(Disposition,File_askdirectory+'\\'+Disposition+".zip")
        pass
    
