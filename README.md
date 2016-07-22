# deepkeylistener

Deep learning model to reconstruct keystrokes from audio

TODO:
(maybe)Split up audio deterministically into keystrokes
Convert that audio into MFCCs
Find suitable training data or generate it
Train deep RNN to reconstruct groups of audio into keystrokes in small batches (to allow for looking ahead slightly for better prediction of previous characters)
