from runner import Runner
from recorder import Recorder

# CONFIG
TEST_TYPE = "error"
TEST_ID_RANGE = [0,14]
TESTCASE_DIR = "./data/" + TEST_TYPE + "_test/"


recorder = Recorder(TEST_TYPE)

for id in range(TEST_ID_RANGE[0], TEST_ID_RANGE[1]+1):
    inputPath = TESTCASE_DIR + TEST_TYPE + "_test_" + str(id) + ".txt"
    ansPath = TESTCASE_DIR + TEST_TYPE + "_ans_" + str(id) + ".txt"
    runner = Runner(input=inputPath, answer=ansPath)
    runner.run()
    result = runner.check()
    recorder.addResult(id, result)
    if not result:
        break
    print("testing "+str(id) + '/' + str(TEST_ID_RANGE[1]),end='\r')

recorder.writeToLog()       
      
