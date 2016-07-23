# deepkeylistener

Deep learning model to reconstruct keystrokes from audio

TODO:<br>
Split up audio deterministically into keystrokes<br>
Convert that audio into MFCCs <br>
Find suitable training data or generate it<br>
Train deep bi-dir RNN to reconstruct groups of audio into sentences in small batches (to allow for looking ahead slightly for better prediction of previous characters)
