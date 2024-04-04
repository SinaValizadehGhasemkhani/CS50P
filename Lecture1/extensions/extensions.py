def main():
    extension()


def extension():
   sufix = input('File name: ').lower().strip()

   gif_png = ['gif', 'png']
   jpeg_jpg = ('.jpeg', '.jpg')

   if (sufix in ['cat', 'myfile'] or sufix.endswith('.bin')):
       print('application/octet-stream')

   elif (sufix.split('.')[1] in gif_png):
       print(f"image/{sufix.split('.')[1]}")

   elif (sufix.endswith(jpeg_jpg)):
       print("image/jpeg")

   elif (sufix.endswith(".zip")):
       print("application/zip")

   elif (sufix.endswith(".pdf")):
       print("application/pdf")

   elif (sufix == 'plain.txt'):
       print("text/plain")


main()
