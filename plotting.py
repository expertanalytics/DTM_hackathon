import face_recognition

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def plot_result(input_img, lookalike_image):
    fig, axs = plt.subplots(figsize=(12, 6), ncols=2, nrows=1)
    axs[0].imshow(input_img)
    axs[1].imshow(lookalike_image)
    plt.axis("off")
    plt.show()
    plt.close()


def show_face_rect(file):
    image = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(image)
    first_face = face_locations[0]
    y1, x1, y2, x2 = first_face

    # Create a Rectangle patch
    rect = Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=1, edgecolor='r', facecolor='none')

    # Create figure and axes
    fig, ax = plt.subplots()
    ax.add_patch(rect)
    plt.imshow(image)
