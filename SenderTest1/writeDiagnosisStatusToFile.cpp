#include "writeDiagnosisStatusToFile.h"
using namespace std;

void checkFileIsEmpty()
{
	fstream fout;
	fout.open("Status.csv", ios::in | ios::out);
	if (fout.is_open())
	{
		string line;
		getline(cin, line);
		if (line.length() == 0)
		{
			fout << "IMAGE_NAME" << "," << "DIAGNOSIS_STATUS" << "\n";
		}
		fout.close();
	}
	else
	{
		cout << "CSV file cannot be opened to write\n";
	}
}
void WriteDiagnosisStatusOfImageToFile(int startImage, int stopImage)
{
	fstream fout;
	void checkFileIsEmpty();
	fout.open("Status.csv", ios::app);
	if (fout.is_open())
	{
		for (int currentImage = startImage; currentImage <= stopImage; currentImage++)
		{
			fout << currentImage << ".img" << "," << "PENDING" << "\n";
		}
		fout.close();
	}
	else
	{
		cout << "CSV file cannot be opened to write\n";
	}
}