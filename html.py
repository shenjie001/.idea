import unittest
import  os
import HtmlTestRunner

from send_email import info
def allcase():
    case_dir=r"E:\PYproject\.idea\testcase\web"
    #case_path=os.path.join(os.getcwd(),"case")
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir,
                                                 pattern='test*.py',
                                                 top_level_dir=None)

    for test_suite in discover:
       for test_case in test_suite:
            #添加用例到testcase
        print(test_case)
        testcase.addTest(test_case)
    return testcase


if __name__=="__main__":
     # runner=unittest.TextTestRunner()
    # runner.run(allcase())

     report_path= "E:\\result.html"
     fp=open(report_path,'w',)
     runner= HtmlTestRunner.HTMLTestRunner(stream=fp,report_title='测试报告',descriptions='用例执行情况：')

     runner.run(allcase())
     fp.close()
     info()
