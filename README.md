# deepkeylistener

Deep learning model to reconstruct keystrokes from audio

TODO:<br>
Split up audio into keystrokes<br>
Figure out a way to auto-detect good threshold for identifying keypress<br>
Change RNN model slightly (concatenated model in tensorflow is slower)<br>
Find suitable training data or generate it<br>
Modify audio chunking script for more meaningful logs (pull audio in batches)<br>
Construct deep bi-dir RNN<br>
Train deep bi-dir RNN to reconstruct groups of audio into sentences in small batches (to allow for looking ahead slightly for better prediction of previous characters)