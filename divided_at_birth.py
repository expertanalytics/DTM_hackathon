import cv2
import face_recognition

import numpy as np

from typing import List, Union
from pathlib import Path


class DividedAtBirth:
    def __init__(self,
                 file_names: List[Union[Path, str]],
                 resize_images: bool = True):
        """
        Parameters
        ----------
        file_names | List[Union[Path, str]]
            List with file paths
        """
        self.file_names = file_names
        self._set_encodings(resize_images)

    def _set_encodings(self, resize_images: bool):
        """
        Loops through the file names set in __init__ and fills in known encodings and images for
        the other functions to reach.

        Parameters
        ----------
        resize_images | bool
            Whether to resize the images or not
        """
        known_images = list()
        known_encodings = list()
        for fname in self.file_names:
            im, locations = self._get_face_locations(fname, resize_images=resize_images)
            known_images.append(im)
            if len(locations) > 1:
                print(f"{fname} has more than one face. Ignoring")
                continue
        enc = face_recognition.face_encodings(im, known_face_locations=locations)[0]
        known_encodings.append(enc)
        self.known_encodings = known_encodings
        self.known_images = known_images

    def _get_face_locations(self, fname: Union[Path, str],
                            resize_x_direction: float = 0.1,
                            resize_y_direction: float = 0.1,
                            resize_images: bool = True):
        """
        Loads images, resizes and

        Parameters
        ----------
        fname | Union[Path, str]
            File path to desired image
        resize_x_direction | float
            The factor to resize in x-direction. Defaults to 0.1
        resize_y_direction | float
            The factor to resize in y-direction. Defaults to 0.1

        Returns
        -------
        im | np.ndarray
            image object
        locations | np.ndarray
            locations of faces
        """
        im = face_recognition.load_image_file(fname)
        if resize_images:
            im = cv2.resize(im,  (0,0), fx=resize_x_direction, fy=resize_y_direction)
        locations = face_recognition.face_locations(im)
        return im, locations

    def get_distance(self, fname, resize_x_direction=0.1, resize_y_direction=0.1, resize_image=True):
        """
        Find the person the face is most similar to

        Parameters
        ----------
        fname | Union[Path, str]
            File path to desired image
        resize_x_direction | float
            The factor to resize in x-direction. Defaults to 0.1
        resize_y_direction | float
            The factor to resize in y-direction. Defaults to 0.1
        resize_image | bool
            Whether to resize the image or not


        Returns
        -------
        img | np.ndarray
            Loaded input image
        lookalike_image | np.ndarray
            Loaded lookalike image
        """
        img, face_locations = self._get_face_locations(fname, resize_x_direction, resize_y_direction, resize_image)
        try:
            image_to_test_encoding = face_recognition.face_encodings(img)[0]
            face_distances = face_recognition.face_distance(self.known_encodings, image_to_test_encoding)
            lookalike_image = self.known_images[np.argsort(face_distances)[0]]
            return img, lookalike_image
        except IndexError:
            raise IndexError("No face was recognized!")
