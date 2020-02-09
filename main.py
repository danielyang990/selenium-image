import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_opts(is_visible=False, *args, **kwargs):
    # 启动参数列表:  https://peter.sh/experiments/chromium-command-line-switches/
    # selenium启动Chrome配置参数问题 https://zhuanlan.zhihu.com/p/60852696
    opts = Options()
    if not is_visible:
        opts.add_argument("log-level=3")
        # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        opts.add_argument("--headless")
        # 以最高权限运行
        opts.add_argument('--no-sandbox')

    # 先把 args 中的值填充到 arguments 中，其它有的命名参数如果有，优先级更高
    for arg in args:
        opts.add_argument(arg)

    # 添加代理服务
    if 'host_port' in kwargs:
        opts.add_argument('--proxy-server=http://%s' % kwargs.get('host_port'))

    # user-agent
    if 'user_agent' in kwargs:
        opts.add_argument('user-agent="%s"' % kwargs.get('user_agent'))

    # 手动指定浏览器位置
    if 'binary_location' in kwargs:
        opts.binary_location = kwargs.get('binary_location')

    # 设置开发者模式启动，该模式下 window.navigator.webdriver 属性为正常值，否则会被网站监测到
    opts.add_experimental_option('excludeSwitches', ['enable-automation'])

    # 最大化运行（全屏窗口）
    opts.add_argument("--start-maximized")
    # # 指定浏览器分辨率
    # opts.add_argument('window-size=1920x3000')
    # 解决跨域问题
    opts.add_argument("--disable-web-security")
    # # 禁用浏览器正在被自动化程序控制的提示
    # opts.add_argument("--disable-infobars")
    # 谷歌文档提到需要加上这个属性来规避bug
    opts.add_argument("--disable-gpu")
    # 解决混合内容问题，不看到不安全内容的提示
    opts.add_argument("--allow-running-insecure-content")
    # # 隐藏滚动条, 应对一些特殊页面
    # opts.add_argument('--hide-scrollbars')
    # # 不加载图片, 提升速度
    # opts.add_argument('blink-settings=imagesEnabled=false')

    # # 添加扩展应用
    # opts.add_extension()
    # opts.add_encoded_extension()
    #
    # # 设置调试器地址
    # opts.debugger_address()
    #
    # # 添加crx插件
    # opts.add_extension('d:\crx\AdBlock_v2.17.crx')
    #
    # # 禁用JavaScript
    # opts.add_argument("--disable-javascript")
    #
    #
    # # 禁用浏览器弹窗
    # prefs = {
    #     'profile.default_content_setting_values': {
    #         'notifications': 2
    #     }
    # }
    # opts.add_experimental_option('prefs', prefs)

    return opts


def get_host_port():
    host_port = ""
    r = requests.get('http://xxx.xxx.xx.xx:xx', verify=False, allow_redirects=False).text
    return host_port


if __name__ == '__main__':
    opts = get_opts(False)
    capabilities = webdriver.DesiredCapabilities.CHROME
    driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=opts,
                               desired_capabilities=capabilities)
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(30)

    try:
        driver.get('http://www.cip.cc')
        print(driver.page_source)
        # time.sleep(500)
    finally:
        driver.quit()
