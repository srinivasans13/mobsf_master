from OutDocument.mobsf_assesment_generation import createManifest,createPermissions,createCodeAnalysis,createCertificate,createAppSummary,createPermissioniOS,createATSandBinary,fileAnalysis
from OutDocument.front_page import return_pdf
from OutDocument.confidentiality_agreement import returnpdf
import OutDocument.glossary as glossary
import Constants

import PyPDF2
import os

def generate_report(report_json):
    platform = ""
    try:
        if report_json['manifest']:
            generate_android_report(report_json,platform = "Android")

    except KeyError:
        generate_report_ipa(report_json, platform="iOS")
        platform ="iOS"

def generate_android_report(report_json,platform):
    returnpdf()
    glossary.return_pdf()
    createAppSummary(report_json,platform)

    return_pdf(Constants.NAME_WITHOUT_EXTN,platform)
    createCertificate(report_json['certinfo'])
    createManifest(report_json['manifest'])
    createPermissions(report_json['permissions'])
    createCodeAnalysis(report_json['findings'])

    pdf_list = Constants.pdf_list_android
    pdf_write_object = PyPDF2.PdfFileWriter()
    for i in pdf_list:
        pdf_read_object = PyPDF2.PdfFileReader(i)

        for page in range(pdf_read_object.numPages):
            pdf_write_object.addPage(pdf_read_object.getPage(page))
    for name in pdf_list:
        os.remove(name)
    file_destination = "pdf_related_files/{}_report.pdf".format(Constants.NAME_WITHOUT_EXTN)
    final_file_object = open(file_destination, 'wb')
    pdf_write_object.write(final_file_object)

    final_file_object.close()

def generate_report_ipa(report_json,platform):
    platform = ""
    try:
        if report_json['plist']:
            platform = "iOS"
    except KeyError:
        platform ="Android"

    returnpdf()
    glossary.return_pdf()
    createAppSummary(report_json,platform)
    return_pdf(Constants.NAME_WITHOUT_EXTN,platform)
    createATSandBinary(report_json)
    createPermissioniOS(report_json['permissions'])
    fileAnalysis(report_json)


    pdf_list = list()
    if platform =="iOS":

        pdf_list = Constants.pdf_list_ios

    pdf_write_object = PyPDF2.PdfFileWriter()
    for i in pdf_list:
        pdf_read_object = PyPDF2.PdfFileReader(i)

        for page in range(pdf_read_object.numPages):
            pdf_write_object.addPage(pdf_read_object.getPage(page))
    for name in pdf_list:
        os.remove(name)
    file_destination = "pdf_related_files/{}_report.pdf".format(Constants.NAME_WITHOUT_EXTN)
    final_file_object = open(file_destination, 'wb')
    pdf_write_object.write(final_file_object)

    final_file_object.close()
