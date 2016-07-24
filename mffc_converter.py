import numpy as np
import scipy.io.wavfile
from scikits.talkbox.features import mfcc

def convert(path):
	data = {}
	data["sample_rate"], X = scipy.io.wavfile.read(path)
	data["ceps"], data["mspec"], data["spec"] = mfcc(X) #save everything it gives us in case it's useful lmao

	cep_count = len(data["ceps"])
	input_vector = np.array([np.mean(data["ceps"][int(cep_count / 10):int(cep_count * 9 / 10)], axis=0)])
	return input_vector
