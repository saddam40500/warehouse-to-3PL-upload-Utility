# Warehouse to 3PL Bulk Allocation Upload Utility

Overview:

We propose the implementation of an automated system for Warehouse to 3PL bulk allocation, replacing the manual process currently in place. This system aims to streamline and expedite the allocation process, reducing manual errors and improving efficiency.

Objectives:

•	Automation of Allocation Process:
o	Implement a web-based tool allowing Inventory Planners to directly upload allocation files.
o	Automate data validation and export processes to eliminate manual errors.
Current Process:

1.	Inventory planners raise a support request for bulk allocation.
2.	Support team acknowledge the support request.
3.	Open the uploaded file and copy the data from the sheet.
4.	Paste the data into “details” sheets of allocation.xlsm workbook located at \\SharedDrive\data\wh_to_3pl_allocation_excel.
5.	Go to “Validate & Generate” sheet
6.	click “Validate Details” button to run check for errors in the copied data.
7.	When no errors found in the uploaded data allocation file will be created at \\SharedDrive\data\wh_to_3pl_allocation_excel\extract
8.	Above steps has to be followed for all the sheets inside the uploaded file.
9.	When all the sheets are completed, support team share the allocation numbers with IP and close the ticket.

    ![image](https://github.com/user-attachments/assets/c50a340a-1882-4d30-b40b-9ac53886570b)


Proposed Process:

1.	Instead of raising a support ticket, Inventory planner can directly access the Warehouse to 3PL bulk upload utility through a web URL.
2.	The allocation file can have single/multiple sheets.
3.	IP can browse & select the file which they want to create allocation
4.	After file has been selected, user click on upload.
5.	The background process checks for number of sheets in the uploaded file
6.	If the no of sheets greater than one, then it will split the sheets into separate excel files and move the uploaded file to backup folder.
7.	Each file will be checked for errors like data type, required fields, qty, etc.
8.	If any error found it will show the error details with filename, row number & column name to user.
9.	When no errors found allocation file will be created in extracts folder with allocation number as filename.
10.	This process will run in a loop for all files and shows a success message.

    ![image](https://github.com/user-attachments/assets/9d3eab16-47e6-484d-937b-f12225f95d99)

 
Benefits:

Efficiency: Drastically reduce the time required for allocation processes.
Accessibility: Enable Inventory Planners to directly upload files from any location.
