import cloudinary
import cloudinary_storage

cloudinary.config(
    cloud_name="mlnj3amk",
    api_key="149813588799295",
    api_secret="1CBOpoVnJP_u4iTXVek_xDfoRg8 "
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
