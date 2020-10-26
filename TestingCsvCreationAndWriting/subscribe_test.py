import SubcribeImageNameAndWriteIntoCsv as subscriber
import unittest

class subscribeTest(unittest.TestCase):
    def test_When_file_is_empty_first_write_topic_and_then_image_name(self):
        testsamplefilename = 'temp-samples-test.csv'
        DiagnosedImageName ="0.img"
        subscriber.OpenAndUpdateCSVFile(DiagnosedImageName,testsamplefilename)
        with open(testsamplefilename, 'r') as samplefile:
            read=subscriber.csv.DictReader(samplefile)
            for row in read:
                self.assertTrue("IMAGE_NAME,DIAGNOSIS_STATUS")
                if(row==1):
                    self.assertEqual(row['IMAGE_NAME'],"0.img")
                    self.assertEqual(row['DIAGNOSIS_STATUS'], "PENDING")

    def test_When_file_is_not_empty_directly_write_image_name(self):
        testsamplefilename = 'temp-samples-test.csv'
        DiagnosedImageName ="1.img"
        subscriber.OpenAndUpdateCSVFile(DiagnosedImageName,testsamplefilename)
        subscriber.OpenAndUpdateCSVFile(DiagnosedImageName,testsamplefilename)
        with open(testsamplefilename, 'r') as samplefile:
            read=subscriber.csv.DictReader(samplefile)
            for row in read:
                if(row==2):
                    self.assertEqual(row['IMAGE_NAME'],"1.img")
                    self.assertEqual(row['DIAGNOSIS_STATUS'], "PENDING")

if __name__ == '__main__':
    unittest.main()
