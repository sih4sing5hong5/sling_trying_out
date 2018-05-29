import sling

parser = sling.Parser("sempar.flow")

text = raw_input("text: ")
doc = parser.parse(text)
print doc.frame.data(pretty=True)
for m in doc.mentions:
  print "mention", doc.phrase(m.begin, m.end)
