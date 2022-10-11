import subprocess

class Runner:

    def __init__(self, input, answer):
        self.inputPath = input # 输入文件路径
        self.answerPath = answer # 答案路径

    def writeToTestFile(self):
        # 将输入写入testfile
        inputFile = open(self.inputPath,"r",encoding="utf-8")
        inputs = inputFile.readlines()
        testfile = open("./testfile.txt","w")
        for s in inputs:
            testfile.write(s)
        inputFile.close()
        testfile.close()    

    def writeToAnsFile(self):
        # 将答案写入ansfile
        ansFile = open(self.answerPath,"r")
        inputs = ansFile.readlines()
        ansFile.close()
        ansFile = open("./ansfile.txt","w")
        for s in inputs:
            ansFile.write(s) 
        ansFile.close()  

    def check(self):
        # 比较ansfile和outputfile
        ansFile = open("./ansfile.txt","r")
        outputFile = open("./output.txt","r")
        ans = ansFile.readlines()
        outputs = outputFile.readlines()
        if len(ans) != len(outputs):
            return False
        for i in range(0,len(ans)):
            if ans[i].split() != outputs[i].split():
                return False
        return True                  

    def run(self):
        ## read input
        self.writeToTestFile()
        self.writeToAnsFile()
        cmd = "java -jar Compiler.jar"
        cwd = "./"
        subprocess.run(cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=cwd)

     







