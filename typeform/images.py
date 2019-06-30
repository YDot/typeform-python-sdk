from .client import Client


class Images:
    """Typeform Forms API client"""
    def __init__(self, client: Client):
        """Constructor for Typeform Image class"""
        self.__client = client

    def create(self, image_base64: str, file_name: str, url: str = None) -> dict:
        """
        Creates an image. If the image doesn't come from a URL, it needs to be encoded in base64 format.
        """
        return self.__client.request('post', '/images', params={
            'image': image_base64,
            'file_name': file_name,
            'url': url
        })

    def delete(self, uid: str) -> str:
        """
        Deletes the image with the given image_id.
        Return a `str` based on success of deletion, `OK` on success, otherwise an error message.
        """
        return self.__client.request('delete', '/images/%s' % uid)

    def get(self, uid: str) -> dict:
        """Retrieves an image by the given image_id. Includes any image property like width, height etc..."""
        return self.__client.request('get', '/images/%s' % uid)

    def list(self) -> dict:
        """
        Retrieves a list of JSON descriptions for all images in your Typeform account.
        Images are listed in reverse-chronological order based on the date you added them to your account.
        """
        return self.__client.request('get', '/images')