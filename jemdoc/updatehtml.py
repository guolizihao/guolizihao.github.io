orifilename = "index.html"
newfilename = "index.html"
f1 = open(orifilename,"r")
content = f1.read()
f1.close()

t = content.replace("</td>"+'\n'+"</tr>"+'\n'+"</table>"+'\n'+"</body>"+'\n'+"</html>",
                    "<div align='center'>"+'\n'+"<a href='https://clustrmaps.com/site/1b715'  title='Visit tracker'><img src='//clustrmaps.com/map_v2.png?"+'\n'+"cl=ffffff&w=a&t=m&d=m5aO9dNvH6LyLHvyXUkm3wCe9J3vedk30RpJKnS48rM'/></a>"+'\n'+"</div>"+'\n'+"</td>"+'\n'+"</tr>"+'\n'+"</table>"+'\n'+"</body>"+'\n'+"</html>")
with open(newfilename,"w") as f2:
    f2.write(t)

for file_name in ["publications_topic.html", "publications_year.html"]:
    orifilename = file_name
    newfilename = file_name
    f1 = open(orifilename,"r")
    content = f1.read()
    f1.close()

    t1 = content.replace("<li><p>[",
                        "<li><p>[<font color='red'>")
    t2 = t1.replace("] ",
                        "]"+"</font> ")
    t3 = t2.replace("<b>(CCF B)</b>",
                        "(<font color='red'>CCF B</font>)")
    t4 = t3.replace("<b>(CCF A)</b>",
                        "(<font color='red'>CCF A</font>)")
    t5 = t4.replace("<b>(JCR Q1)</b>",
                        "(<font color='red'>JCR Q1</font>)")

    with open(newfilename,"w") as f3:
        f3.write(t5)