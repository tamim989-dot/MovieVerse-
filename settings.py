'cloudinary',
'cloudinary_storage',


import cloudinary

cloudinary.config(
    cloud_name="mlnj3amk",
    api_key="149813588799295",
    api_secret="তোমার নতুন secret"
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
