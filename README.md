# cuckoo-forlinux
修改cuckoo-master版本,令其适应linux系统
1,安装完成后,令cuckoo.py替换系统/usr/bin/cuckoo
2,安装完成后,部署guest时候创建/root/.cuckoo目录,将agent.sh agent.py以及monitor_linux中的strace.stp,cuckoo
  放入guest中.cuckoo放入开机自启动项,strace.stp使用systemtap生成stap_开头,.ko结尾的模块.(guest中python保证为2.7以上版本)

