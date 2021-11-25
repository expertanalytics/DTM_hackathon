from divided_at_birth import DividedAtBirth
from plotting import plot_result


if __name__ == "__main__":
    import os

    path = "."
    files = [os.path.join(path, infile) for infile in os.listdir(path)]

    dab = DividedAtBirth(files)

    file_to_compare = "path/to/desired/file"
    img, lookalike_img = dab.get_distance(fname=file_to_compare,
                                          resize_image=False)

    plot_result(img, lookalike_img)