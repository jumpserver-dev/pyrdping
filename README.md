## pyrdping

使用 python c 扩展模块实现的 RDP 账号密码检测工具

### 依赖
需要安装 freerdp 库

Ubuntu 下安装命令
```
sudo apt-get install -y freerdp2-dev
```

Centos 下安装命令
```
sudo yum install -y freerdp-devel
```

Macos 下安装命令
```
brew install freerdp
```

alpine 下安装命令
```
apk add freerdp-dev
```

### 编译
```
make all
```

### 使用
```
# check_connectivity(ip, port, username, password, domain, security_level)
import pyrdping
ret = pyrdping.check_connectivity("localhost", 3389, "administrator", "password", "domain", 0)
print(ret)
```
