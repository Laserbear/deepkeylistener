from mffc_converter import convert
counter = 1
def pull_data_chunk():
	#hard code data path, i guess
	global counter #gross syntax but necessary
	path = "data/audio"+str(counter)+".wav"
	counter += 1
	return convert(path)