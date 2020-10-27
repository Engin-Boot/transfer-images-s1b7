# Deployment Details

## Sender(SCU) and Receiver(SCP)

  - __*Directory : sender and receiver*__

  - Hence SCP related files were not modified stor_scp.exe is already there inside receiver folder with required dll's
  
  - To build SCU, files are inside sender folder
  
  - include files are in mc3inc directory
	
  - library files and dll files are in mclib directory
  
  - after building SCU place the .exe file in MC3File directory and run

## <center> EmailSender Python Utility

  - __*Directory : EmailSender*__
  
  - *filePollingAndSendMail.py* poll the Receiver Directory continuosly to detect new files that are received and send mail to Radiologist if new images received.

  - *mail_credendials.py* has mail sender and Radiologist mail credentials.

## Creating CSV file that has image name and status(Diagonose Pending)
 
  - __*Directory : SendImageNameFromScpToScu*__
  
  - *pubishImageName.py* will publish received image name in topic *"WritingImageName"*
  
  - *SubcribeImageNameAndWriteIntoCsv.py* will subscribe to topic *"WritingImageName"* and write image name and image status(Pending) into CSV file 
  
## Updating Image status as Diagonise completed

  - __*Directory : DiagonosisStatus*__
  
  - *PublishDiagonisedImageName.py* when doctor diagonose specific image, he/she will excute this file and nter the image name to publish in topic *"DiagonosedImageName"*
  
  - *subscribeDiagonisedImageNameAndUpdateStatus.py* will subscribe to topic *"DiagonosedImageName"* and change the status of received image name to *Diogonose Completed*
