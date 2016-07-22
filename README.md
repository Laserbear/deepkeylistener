# deepkeylistener

Deep learning model to reconstruct keystrokes from audio

TODO:<br>
(maybe)Split up audio deterministically into keystrokes<br>
Convert that audio into MFCCs <br>
Find suitable training data or generate it<br>
Train deep RNN to reconstruct groups of audio into keystrokes in small batches (to allow for looking ahead slightly for better prediction of previous characters)
