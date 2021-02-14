from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

i_amount = float(input("Hey user, Enter the Bill amount: "))
i_period = input("Enter period: ")

print("good now we need the flatmate information: ")

i_name1 = input("Enter your name: ")
i_days1 = int(input(f"How many days did {i_name1} stay in the house during the bill period: "))

i_name2 = input("Enter name of the second flatmate: ")
i_days2 = int(input(f"How many days did {i_name2} stay in the house during the bill period: "))

the_bill = Bill(i_amount, i_period)
flatmate1 = Flatmate(i_name1, i_days1)
flatmate2 = Flatmate(i_name2, i_days2)

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
