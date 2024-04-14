from ctypes import cdll

# 加载DLL
lib = cdll.LoadLibrary('./example.dll')

# 调用函数
lib.hello_from_c()