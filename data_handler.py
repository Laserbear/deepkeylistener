from mffc_converter import convert
counter = 1
def pull_data_chunk():
	#hard code data path, i guess
	global counter #gross syntax but necessary
	path = "data/audio"
	return convert(path+str(counter)+".wav")