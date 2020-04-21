# 导入handler模块
from flash_handler import handler
# 将Excel文件所在的文件夹路径赋值给一个变量
path = r'C:\Users\terre\Desktop\python\flash_program'#可以放你自己文件夹的路径
handler.set_path(path)
# 构造增加函数
def auto_add():
    """向工作目录下的部分或全部Excel文件添加新的一行数据，然后打印新增的行等信息。所需要的全部
    信息会要求用户进行输入。"""
    # 打印文件夹下的文件名称
    handler.excel_files()
    # 终端输入需要添加的文件名序号
    table_index = input('输入需要添加的文件序号（多个文件用逗号隔开）：')
    # 添加数据
    handler.excel_add(table_index)
# 构造搜索函数
def auto_search():
    """对工作目录下的部分或全部Excel文件中的数据进行搜索，打印搜索结果。所需要的全部信息会要求
    用户进行输入。"""
    # 输出空行,美化显示效果
    print()
    # 获取搜索主要关键字key1
    key1 = input('请输入你要查询的主要关键词: ')
    # 获取搜索的次要关键字key2
    key2 = input('请输入你要查询的次要关键词(若无请直接回车): ')  # 不输入，为空字符串
    # 调用handler的search 帮助查找
    res = handler.excel_search(key1, key2)
    if res == None:
        print('抱歉，没有找到相关数据！')
    else:
        print('太棒了！Excel小助手为你搜索到了如上结果~')
    # 将结果作为函数返回值
    return res
# 构造删除函数
def auto_delete():
    """删除工作目录下的部分或全部Excel文件中符合特定条件的行，随后打印删除操作是否成功等结果
    信息。所需要的全部信息会要求用户进行输入。"""
    # 执行搜索函数，并获取搜索结果
    res = auto_search()
    # 获取想要删除的表格编号
    table_index = input('请输入需要删除的表格编号(可输入多个,用逗号隔开): ')
    # 删除内容
    handler.excel_delete(res, table_index)
# 构造修改函数
def auto_update():
    """对工作目录下的部分或全部Excel文件中符合特定条件的行，随后打印更新操作产生的效果等
    结果信息。所需要的全部信息会要求用户进行输入。"""
    # 获取搜索结果
    res = auto_search()
    # 获取需要修改的表格编号
    table_index = input('请输入需要修改的表格编号(可输入多个，用逗号隔开): ')
    # 显示表头
    handler.excel_headers(table_index)
    # 获取需要修改的表头column
    column = input('请输入需要修改的信息所对应的表头(只可输入一个): ')
    # 执行修改
    handler.excel_update(res, table_index, column)
# 定义pro_controller函数，作为第五关的代码。
def pro_controller():
    """入口函数。在终端上提供菜单，让用户选择欲进行的Excel操作，并调用相应函数（上面所列函数）。
    """
    # 美化控制台打印效果，先打印一个空行
    print()
    # 美化控制台打印效果，打印温馨提示，注意事项
    print('''
          ********************************************************************
                                    温馨提示                         
              1. 使用前请先确认您需要处理表格的第一行为表头（列名）。 
              2. 请您在使用过程中按照屏幕上的指示选择操作。          
              3. 为了避免不必要的bug，请您确保在使用程序时，Excel处于关闭状态。
              4. 祝您使用愉快。                                     
          ********************************************************************
          ''')
    # 打印空行,美化控制器
    print()
    # # 显示文件下的所有文件
    # handler.show_all_files(path)
    # # 打印空行,美化控制器
    print()
    # 进入控制器操作界面
    # 进入Excel助手
    print('--------- 欢迎使用Excel助手工具 ---------')
    # 通过循环实现自动化批量操作
    while True:
        # 打印空行,美化控制器
        print()
        # print('---------     Excel助手工具       --------')
        print("请选择功能：1.查找  2.增加  3.删除  4.修改  5.数据图  6.邮件  0.退出")
        # 获取用户输入选项
        switch = int(input('请输入功能编号(数字): '))
        # 退出选项判断
        if switch == 0:
            print('正在退出')
            break
        # 查找功能判断
        elif switch == 1:
            # 调用查找函数
            auto_search()
        # 增加功能判断
        elif switch == 2:
            # 调用增加函数
            auto_add()
        # 删除功能判断
        elif switch == 3:
            # 调用删除函数
            auto_delete()
        # 修改功能判断
        elif switch == 4:
            # 调用修改函数
            auto_update()
        # 柱状图功能判断
        elif switch == 5:
            handler.auto_picture()
        # 邮件功能判断
        elif switch == 6:
            handler.auto_email()
        # 异常数字排查
        else:
            print('没有这项功能，请输入合理的功能编号！')
    print("欢迎下次使用哦")


if __name__ == '__main__':
    pro_controller()