import aspose.words as aw

# load TXT document
doc = aw.Document("extracted.txt")

# save TXT as PDF file
doc.save("txt-to-pdf.pdf", aw.SaveFormat.PDF)
