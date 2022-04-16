print("""
@Author:w01f
@github:https://github.com/W01fh4cker
@version 1.0
@2022/3/18
 ██      ██                    ██                        ██████████                ████████                          ██
░██     ░██                   ░██                       ░░░░░██░░░                ░██░░░░░                          ░██
░██     ░██ ██   ██ ███████  ██████  █████  ██████          ░██      ██████       ░██       ██   ██  █████   █████  ░██
░██████████░██  ░██░░██░░░██░░░██░  ██░░░██░░██░░█ █████    ░██     ██░░░░██ █████░███████ ░░██ ██  ██░░░██ ██░░░██ ░██
░██░░░░░░██░██  ░██ ░██  ░██  ░██  ░███████ ░██ ░ ░░░░░     ░██    ░██   ░██░░░░░ ░██░░░░   ░░███  ░██  ░░ ░███████ ░██
░██     ░██░██  ░██ ░██  ░██  ░██  ░██░░░░  ░██             ░██    ░██   ░██      ░██        ██░██ ░██   ██░██░░░░  ░██
░██     ░██░░██████ ███  ░██  ░░██ ░░██████░███             ░██    ░░██████       ░████████ ██ ░░██░░█████ ░░██████ ███
░░      ░░  ░░░░░░ ░░░   ░░    ░░   ░░░░░░ ░░░              ░░      ░░░░░░        ░░░░░░░░ ░░   ░░  ░░░░░   ░░░░░░ ░░░ 

""")
import requests
import base64
from pprint import pprint
import json
import xlwt
import time
localtime = time.localtime(time.time())
make_time = time.strftime("%Y%m%d%H%M%S", time.localtime())

def make_sheet():
    global workbook
    workbook = xlwt.Workbook(encoding='utf-8')
    global worksheet
    worksheet = workbook.add_sheet('鹰图平台数据')
    # 创建颜色
    pattern = xlwt.Pattern()  # 创建模式对象
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 5  # 设置模式颜色为黄色
    style = xlwt.XFStyle()  # 创建样式对象
    style.pattern = pattern  # 将模式加入到样式对象
    # 设置单元格的宽度
    worksheet.col(1).width = 400 * 20
    worksheet.col(2).width = 400 * 20
    worksheet.col(4).width = 400 * 20
    worksheet.col(5).width = 400 * 20
    worksheet.col(7).width = 400 * 20
    worksheet.col(8).width = 400 * 20
    worksheet.col(9).width = 400 * 20
    worksheet.col(12).width = 400 * 20
    worksheet.col(13).width = 400 * 20
    worksheet.col(14).width = 400 * 20
    worksheet.col(17).width = 800 * 20
    worksheet.col(18).width = 400 * 20
    worksheet.col(19).width = 400 * 20
    worksheet.col(20).width = 400 * 20
    # 写第一行的标题
    worksheet.write(0, 0, '是否危险', style)
    worksheet.write(0, 1, '网址', style)
    worksheet.write(0, 2, 'IP地址', style)
    worksheet.write(0, 3, '端口', style)
    worksheet.write(0, 4, '网站标题', style)
    worksheet.write(0, 5, '域名', style)
    worksheet.write(0, 6, '状态码', style)
    worksheet.write(0, 7, '系统名称', style)
    worksheet.write(0, 8, '公司名称', style)
    worksheet.write(0, 9, '备案号', style)
    worksheet.write(0, 10, '协议名称', style)
    worksheet.write(0, 11, '基础协议', style)
    worksheet.write(0, 12, '国家', style)
    worksheet.write(0, 13, '省份', style)
    worksheet.write(0, 14, '城市', style)
    worksheet.write(0, 15, '运营商', style)
    worksheet.write(0, 16, 'AS组织', style)
    worksheet.write(0, 17, 'banner', style)
    worksheet.write(0, 18, '更新日期', style)
    worksheet.write(0, 19, '应用名称', style)
    worksheet.write(0, 20, '应用版本', style)

def traversal_and_write_data():
    global i
    global number
    number = 1
    i =0
    for i in range(len(res["data"]["arr"])):
        try:
            is_risk = res["data"]["arr"][i]["is_risk"]  # 是否危险
            its_url = res["data"]["arr"][i]["url"]  # 网址
            ip = res["data"]["arr"][i]["ip"]  # IP地址
            port = res["data"]["arr"][i]["port"]  # 端口
            web_title = res["data"]["arr"][i]["web_title"]  # 网站标题
            domain = res["data"]["arr"][i]["domain"]  # 域名
            status_code = res["data"]["arr"][i]["status_code"]  # 状态码
            os = res["data"]["arr"][i]["os"]  # 系统名称
            company = res["data"]["arr"][i]["company"]  # 公司名称
            record_number = res["data"]["arr"][i]["number"]  # 备案号
            protocol = res["data"]["arr"][i]["protocol"]  # 协议名称
            base_protocol = res["data"]["arr"][i]["base_protocol"]  # 基础协议
            country = res["data"]["arr"][i]["country"]  # 国家
            province = res["data"]["arr"][i]["province"]  # 省份
            city = res["data"]["arr"][i]["city"]  # 城市
            isp = res["data"]["arr"][i]["isp"]  # 运营商
            as_org = res["data"]["arr"][i]["as_org"]  # AS组织
            banner = res["data"]["arr"][i]["banner"]  # Banner
            updated_at = res["data"]["arr"][i]["updated_at"]  # 更新日期
            for j in range(len(res["data"]["arr"][i]["component"])):
                component_name = res["data"]["arr"][i]["component"][j]["name"]  # 应用名称
                component_version = res["data"]["arr"][i]["component"][j]["version"]  # 应用版本
                print(component_name)
                print(component_version)
            print(is_risk, its_url, ip, port, web_title, domain, status_code, os, company, record_number, protocol,
                  base_protocol, country, province, city, isp, as_org, banner, updated_at)
        except:
            i = i +1
        # 写入数据
        worksheet.write(number, 0, is_risk)
        worksheet.write(number, 1, its_url)
        worksheet.write(number, 2, ip)
        worksheet.write(number, 3, port)
        worksheet.write(number, 4, web_title)
        worksheet.write(number, 5, domain)
        worksheet.write(number, 6, status_code)
        worksheet.write(number, 7, os)
        worksheet.write(number, 8, company)
        worksheet.write(number, 9, record_number)
        worksheet.write(number, 10, protocol)
        worksheet.write(number, 11, base_protocol)
        worksheet.write(number, 12, country)
        worksheet.write(number, 13, province)
        worksheet.write(number, 14, city)
        worksheet.write(number, 15, isp)
        worksheet.write(number, 16, as_org)
        worksheet.write(number, 17, banner)
        worksheet.write(number, 18, updated_at)
        worksheet.write(number, 19, component_name)
        worksheet.write(number, 20, component_version)
        number = number + 1
def main():
    api_key = input("[*]请输入您的api-key：")
    query_sentence = input("[*]请输入查询语法：")
    search = base64.urlsafe_b64encode(query_sentence.encode("utf-8"))
    search_result = str(search, 'utf8')
    page = input("[*]请输入所查询页码：")
    page_size = input("[*]请输入每页资产条数：")
    is_web = input("[*]请选择资产类型（资产类型，1代表web资产，2代表非web资产，3代表全部）：")
    cookie = input("[*]请输入cookie：(方法：打开http://hunter.qianxin.com/登录之后，按F12，在console控制台里面输入document.cookie，双击下方的红色部分，把所有内容连同两个单引号复制下来，粘贴过来。)")
    url = 'https://hunter.qianxin.com/openApi/search?api-key='+ str(api_key) + '&search='+ str(search_result) + '&page=' + str(page) + '&page_size=' + str(page_size) + '&is_web=' + str(is_web)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'Cookie': cookie #填入自己的cookie
    }
    resp = requests.get(url=url, headers=headers)
    global res
    res = json.loads((resp.content).decode('utf-8'))

    # 调用写好的函数
    make_sheet()
    traversal_and_write_data()
    workbook.save(make_time +'.xls')
if __name__ == '__main__':
    main()
