import Dependencies.pdfkit as pdfkit

def modified_code(string):

    modified_html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" type="text/css" href="modified.css">
</head>
<body>
<div class="box-header">
                   <!-- /.box-header -->
                    <h3 class="box-title"><i class="fa fa-certificate"></i>{}</h3>
                  </div>
<div style="overflow-x:auto;">
<table>
""".format(string)
    return modified_html_code

def createManifest(json_file):
    modified_html_code = modified_code("Manifest Analysis")
    modified_html_code += """
            <tr>
    <th>Issue</th>
    <th>Severity</th>
    <th>Description</th>
    </tr>
            """
    file_name = "OutDocument/temp.htm"
    for i in json_file:

        code = ""
        if i['stat'] == "high":

            code = """<tr><td>{}</td><td class="label label-danger">{}</td><td>{}</td></tr>""".format(i['title'],
                                                                                                      i['stat'],
                                                                                                      i['desc'])
        elif i['stat'] == "medium":
            code = """<tr><td>{}</td><td class="label label-warning">{}</td><td>{}</td></tr>""".format(i['title'],
                                                                                                       i['stat'],
                                                                                                       i['desc'])
        elif i['stat'] == "info":
            code = """<tr><td>{}</td><td class="label label-info">{}</td><td>{}</td></tr>""".format(i['title'],
                                                                                                    i['stat'],
                                                                                                    i['desc'])
        modified_html_code = modified_html_code + code



    modified_html_code = modified_html_code + """
</table>
</div>
</body>
</html>
    """
    with open(file_name, 'w') as file:

        file.write(modified_html_code)

    pdfkit.from_file("OutDocument/temp.htm","pdf_related_files/assessment_details.pdf")

def createPermissions(json_file):
    modified_html_code = modified_code("Permissions")
    modified_html_code += """
    <tr>
    <th>Permission</th>
    <th>Status</th>
    <th>Info</th>
    <th>Description</th>
    </tr>
    """
    file_name = "OutDocument/temp.htm"
    for permission_name,details_dictionary in json_file.items():
        if json_file[permission_name]['status'] == "dangerous":
            modified_html_code += """<tr><td>{}</td><td class="label label-danger">{}</td><td>{}</td><td>{}</td></tr>""".format(permission_name,
                                                                                                                                json_file[permission_name]['status'],
                                                                                                                                json_file[permission_name]['info'],
                                                                                                                                json_file[permission_name]['description'])
        elif json_file[permission_name]['status'] == "normal":
            modified_html_code += """<tr><td>{}</td><td class="label label-info">{}</td><td>{}</td><td>{}</td></tr>""".format(permission_name,
                                                                                                                                json_file[permission_name]['status'],
                                                                                                                                json_file[permission_name]['info'],
                                                                                                                                json_file[permission_name]['description'])
        else:
            modified_html_code += """<tr><td>{}</td><td class="label label-success">{}</td><td>{}</td><td>{}</td></tr>""".format(permission_name,
                                                                                                                                json_file[permission_name]['status'],
                                                                                                                                json_file[permission_name]['info'],
                                                                                                                                 json_file[permission_name]['description'])
    modified_html_code = modified_html_code + """
           </table>
           </div>
           </body>
           </html>
               """
    with open(file_name,'w') as file:
        file.write(modified_html_code)
    pdfkit.from_file("OutDocument/temp.htm", "pdf_related_files/permissions.pdf")

def createCodeAnalysis(json_file):
    modified_html_code = modified_code("Code Analysis")
    modified_html_code += """
        <tr>
        <th>Issue</th>
        <th>Severity</th>
        <th>Files</th>
        </tr>
        """
    file_name = "OutDocument/temp.htm"
    for issue, details_dictionary in json_file.items():
        if json_file[issue]['level'] == "high" or json_file[issue]['level'] == "warning":
            x=""
            for m in json_file[issue]['path']:
                x= x+"<br>"+m
            modified_html_code += """<tr><td>{}</td><td class="label label-danger">{}</td><td>{}</td></tr>""".format(str(issue).title(),json_file[issue]['level'],
                                                                                                      x)

    modified_html_code = modified_html_code + """
               </table>
               </div>
               </body>
               </html>
                   """
    with open(file_name,'w') as file:
        file.write(modified_html_code)
    pdfkit.from_file(file_name, "pdf_related_files/code_analysis.pdf")

def createCertificate(cert_info):
    modified_html_code = modified_code("")
    modified_html_code +="""
     <section >
        <h2 class="page-header"></h2>
         <div class="box-header">
                   <!-- /.box-header -->
                    <h3 class="box-title"><i class="fa fa-certificate"></i> Signer Certificate</h3>
                  </div>
       <pre class="hierarchy bring-up"><code>{} </code></pre>
      </section>
    """.format(cert_info)
    file_name = "OutDocument/temp.htm"
    modified_html_code = modified_html_code + """
               </table>
               </div>
               </body>
               </html>
                   """
    with open(file_name,'w') as file:
        file.write(modified_html_code)
    pdfkit.from_file(file_name,"pdf_related_files/certificate.pdf")


def createAppSummary(json_file,platform):
    if platform =="Android":
        modified_html_code = ""
        modified_html_code += """
            <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="modified.css">
        </head>
        <body>
        <div class="box-header">
                           <!-- /.box-header -->
                            <h3 class="box-title"><i class="fa fa-certificate"></i>File Summary</h3>
                          </div>
        <div style="overflow-x:auto;">

            <table class"table-center">
                    <tr>
                        <th>Item</th>
                        <th>Value</th>
                    </tr> 
            """
        modified_html_code += """
                <tr><td>Name</td><td>{}</td><tr>
                <tr><td>Size</td><td>{}</td><tr>
                <tr><td>MD5</td><td>{}</td><tr>
                <tr><td>SHA1</td><td>{}</td><tr>
                <tr><td>SHA256</td><td>{}</td><tr>
            """.format(json_file['name'], json_file['size'], json_file['md5'], json_file['sha1'], json_file['sha256'])

        modified_html_code += """ </table>
            <div class="box-header">
                           <!-- /.box-header -->
                            <h3 class="box-title"><i class="fa fa-certificate"></i>{}</h3>
                          </div>
            <table class"table-center">
                    <tr>
                        <th>Item</th>
                        <th>Value</th>
                    </tr> 
            """.format("App Information")
        modified_html_code += """
            <tr><td>Package Name</td><td>{}</td><tr>
             <tr><td>Main Activity</td><td>{}</td><tr>
              <tr><td>Target SDK</td><td>{}</td><tr>
               <tr><td>Min SDK</td><td>{}</td><tr>
                <tr><td>Max SDK</td><td>{}</td><tr>
                 <tr><td>Android Version Name</td><td>{}</td><tr>
                  <tr><td>Android Version Code</td><td>{}</td><tr>
            """.format(json_file['packagename'], json_file['mainactivity'], json_file['targetsdk'], json_file['minsdk'],
                       json_file['maxsdk'], json_file['androvername'], json_file['androver'])
        modified_html_code = modified_html_code + """
                       </table>
                       </div>
                       </body>
                       </html>
                           """
        file_name = "OutDocument/temp.htm"
        with open(file_name, 'w') as file:
            file.write(modified_html_code)
        pdfkit.from_file(file_name, "pdf_related_files/appsummary.pdf")

    else:
        modified_html_code = ""
        modified_html_code += """
                   <!DOCTYPE html>
               <html>
               <head>
               <meta name="viewport" content="width=device-width, initial-scale=1.0">
               <link rel="stylesheet" type="text/css" href="modified.css">
               </head>
               <body>
               <div class="box-header">
                                  <!-- /.box-header -->
                                   <h3 class="box-title"><i class="fa fa-certificate"></i>File Summary</h3>
                                 </div>
               <div style="overflow-x:auto;">

                   <table class"table-center">
                           <tr>
                               <th>Item</th>
                               <th>Value</th>
                           </tr> 
                   """
        modified_html_code += """
                       <tr><td>Name</td><td>{}</td><tr>
                       <tr><td>Size</td><td>{}</td><tr>
                       <tr><td>MD5</td><td>{}</td><tr>
                       <tr><td>SHA1</td><td>{}</td><tr>
                       <tr><td>SHA256</td><td>{}</td><tr>
                   """.format(json_file['name'], json_file['size'], json_file['md5'], json_file['sha1'],
                              json_file['sha256'])

        modified_html_code += """ </table>
                   <div class="box-header">
                                  <!-- /.box-header -->
                                   <h3 class="box-title"><i class="fa fa-certificate"></i>{}</h3>
                                 </div>
                   <table class"table-center">
                           <tr>
                               <th>Item</th>
                               <th>Value</th>
                           </tr> 
                   """.format("App Information")
        modified_html_code += """
                   <tr><td>App Name</td><td>{}</td><tr>
                    <tr><td>Identifier</td><td>{}</td><tr>
                     <tr><td>Version</td><td>{}</td><tr>
                      <tr><td>SDK Name</td><td>{}</td><tr>
                       <tr><td>Platform Version</td><td>{}</td><tr>
                        <tr><td>Min OS Version</td><td>{}</td><tr>
                   """.format(json_file['bin_name'], json_file['id'], json_file['ver'],
                              json_file['sdk'],
                              json_file['pltfm'], json_file['min'])
        modified_html_code = modified_html_code + """
                              </table>
                              </div>
                              </body>
                              </html>
                                  """
        file_name = "OutDocument/temp.htm"
        with open(file_name, 'w') as file:
            file.write(modified_html_code)
        pdfkit.from_file(file_name, "pdf_related_files/appsummary.pdf")

def createPermissioniOS(json_file):
    modified_html_code = modified_code("Permissions")
    modified_html_code += """
    <tr>
    <th>Permissions</th>
    <th>Description</th>
    <th>Reason in Manifest</th>
    </tr>
    """
    file_name = "OutDocument/temp.htm"
    for i in json_file:
        for j in range(0,3):
            modified_html_code += """<tr><td>{}</td><td>{}</td><td>{}</td></tr>""".format(i[0],i[1],i[2])
    modified_html_code = modified_html_code + """
           </table>
           </div>
           </body>
           </html>
               """.encode('utf-8').decode('utf-8')
    with open(file_name,'w') as file:
        file.write(modified_html_code.replace(u"\u2018", "'").replace(u"\u2019", "'"))
    pdfkit.from_file("OutDocument/temp.htm", "pdf_related_files/permissions.pdf")

def createATSandBinary(json_file):
    modified_html_code = modified_code("App Transport Security")
    modified_html_code +="""
      <tr>
    <th>Issue</th>
    <th>Status</th>
    <th>Description</th>
    </tr>
    """


    if len(json_file['insecure_connections']) > 0:
        modified_html_code +="""
        <tr>
                       <td>
                         Exception in NSAppTransportSecurity found.
                       <td>
                         Insecure
                       </td>
                       <td>
                         App Transport Security (ATS) is disabled on the domain '{}'. Disabling ATS can allow insecure communication with particular servers or allow insecure loads for web views or for media, while maintaining ATS protections elsewhere in your app.
                       </td>
                     </tr>
        """.format(json_file['insecure_connections'])
    else:
        modified_html_code +="""
        <tr>
                     <td>
                       None
                     <td>
                       Secure
                     </td>
                     <td>
                       No insecure connections configured. App Transport Security (ATS) is enabled.
                     </td>
                   </tr>
        """

    modified_html_code +="""</table>
    <div class="box-header">
                   <!-- /.box-header -->
                    <h3 class="box-title"><i class="fa fa-certificate"></i>{}</h3>
                  </div>
<div style="overflow-x:auto;">
<table>
      <tr>
    <th>Issue</th>
    <th>Status</th>
    <th>Description</th>
    </tr>
{}""".format("Binary Analysis",json_file['bin_anal'])
    modified_html_code = modified_html_code + """
               </table>
               </div>
               </body>
               </html>
                   """
    file_name = "OutDocument/temp.htm"
    with open(file_name, 'w') as file:
        file.write(modified_html_code)
    pdfkit.from_file("OutDocument/temp.htm", "pdf_related_files/ats_and_binary.pdf")


def fileAnalysis(json_file):
    modified_html_code = modified_code("File analysis")
    modified_html_code +="""
    {}
    """.format(json_file['file_analysis'])
    modified_html_code = modified_html_code + """
               </table>
               </div>
               </body>
               </html>
                   """
    file_name = "OutDocument/temp.htm"
    with open(file_name, 'w') as file:
        file.write(modified_html_code)
    pdfkit.from_file("OutDocument/temp.htm", "pdf_related_files/fileanalysis.pdf")




