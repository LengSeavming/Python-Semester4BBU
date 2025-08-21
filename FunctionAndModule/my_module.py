import pywhatkit
from rembg import remove
from PIL import Image

data = []

def append_item(item):
    data.append(item)

def insert_item(index, new_item):
    data.insert(index, new_item)

def remove_item(item):
    result = False
    try:
        if item in data:
            data.remove(item)
            print("Succeeded!")
            result = True
        else:
            print(f"Item does not exist!")

    except Exception as e:
        print(f"{e}")
    return result

# print(data)


def get_datas():
    return data

def get_data(index):
    if index < len(data):
        return data[index]
    else:
        print("Index out of rang list Data")
        return ""

def play_video(title):
    if title == "":
        print("Please input your song you want to play!")
    else:
        try:
            title = str(title).lower()
            title = title.replace("open", "")
            title = title.replace("please", "")
            pywhatkit.playonyt(title)
            print("Video is playing!")
        except Exception as e:
            print(f"{e}")

def remove_background(input_image, output_image):
    try:
        open_image = Image.open(input_image)
        new_image = remove(open_image)
        new_image.save(output_image)
    except Exception as ex:
        print(f"{ex}")



