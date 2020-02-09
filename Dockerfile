FROM centos/python-36-centos7

USER root

# 安装 chrome 和 chromedriver
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm -O ~/google.rpm
RUN wget http://npm.taobao.org/mirrors/chromedriver/2.36/chromedriver_linux64.zip -O ~/chromedriver.zip

# 安装chrome需要的字体（否则中文无法显示）
RUN wget http://js.xiazaicc.com/down2/msyh_downcc.com.zip -O ~/msyh.ttf && \
yum install -y freetype freetype-devel fontconfig fontconfig-devel && \
mkdir -p /usr/share/fonts/chinese/TrueType/ && \
cp ~/msyh.ttf /usr/share/fonts/chinese/TrueType/ && \
fc-cache -fv

# 清理缓存
RUN yum localinstall -y ~/google.rpm && unzip ~/chromedriver.zip -d /usr/bin && rm -f ~/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

CMD [ "python", "main.py"]
