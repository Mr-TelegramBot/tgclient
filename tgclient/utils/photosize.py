
def large_photo(photosize):
    if 'file_id' in photosize[0]:
        return photosize[(len(photosize) - 1)]

def small_photo(photosize):
    if 'file_id' in photosize[0]:
        return photosize[0]
