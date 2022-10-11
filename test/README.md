# 自动测试程序使用说明

## 错误处理部分测试

错误处理部分已经实现了15组针对单个错误的测试数据，可以直接进行测试。

1. 将你的编译器程序打包成jar包，命名为"Compiler.jar"，放在test/目录下
2. 运行test程序 `python test.py`
3. 控制台将输出结果，也可以到 test/testlog/error_testlog 中查看测试结果

注意：

- 请确保你的编译器从testfile.txt读入，并**输出到output.txt**（和错误处理作业有所不同）。
- 请确保你的jar包命名为"Compiler.jar"
- 如果某一测试样例出现错误，则测试程序将会输出相应信息并**停止后续测试**，你可以：
  - 在test/testfile.txt中查看出现错误的输入样例
  - 在test/ansfile.txt中查看对应的期望输出
  - 在test/output.txt中查看对应的实际输出

## 其他部分测试

你可以在test/data/中补充自己的测试数据。

例如，要进行$NAME测试

1. 在test/data/中创建$NAME_test目录
2. 在test/data/\$NAME_test/目录中创建对应id的测试样例，包括
   - 输入样例 \$NAME_test_id.txt 
   - 期望输出 $NAME_ans_id.txt
3. 修改test.py中的CONFIG部分。
   - 将TEST_TYPE改为$NAME
   - 将TEST_ID_RANGE改为你的测试样例的id范围
4. 运行test程序 `python test.py`

