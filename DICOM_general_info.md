## <center>Mc3File

- Mc3File is an application that is used to generate images in *DICOM* format(inside MC3File directory).

- It takes in as args __service and command name__ which can be viewed by using -l flag and __number of images__ to be generated.

- The generated file will have an extension of __*.00x*__ which should be renamed to __*.img*__ 
for Sender application.

- Mc3File folder has the mc3file.exe and the required dll's and lib files to run the stor_scu exe file.

- ex: mc3file BASIC_FILM_BOX N_DELETE_RSP 1

<br>

## <center>  STORE_SCP & Sender

 __*stor_scp*__ is an application used to recieve generated dicom images(inside Receiver folder).

 __*Sender*__ is an application used to send generated Dicom images over to the server(required c files are within sender folder and already build exe file is placed inside mc3file directory).
