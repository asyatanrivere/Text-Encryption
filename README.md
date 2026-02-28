<h1>Text Encryption Tool (Python)</h1>

<p>
A simple substitution-based text encryption tool implemented in Python.
<br>
Demonstrates string processing, list manipulation, and algorithmic mapping logic.
</p>

<hr>

<h2>Overview</h2>

<p>
This project implements a basic <strong>substitution cipher encryption system</strong> 
using Python. The program generates a randomized character mapping and encrypts 
user-provided text by substituting each character with a shuffled equivalent.
</p>

<p>
The encryption process is deterministic within a single runtime session and 
demonstrates fundamental concepts of:
</p>

<ul>
  <li>Algorithm design</li>
  <li>Index-based character mapping</li>
  <li>Randomization techniques</li>
  <li>String manipulation</li>
  <li>List operations</li>
</ul>

<hr>

<h2>How It Works</h2>

<ol>
  <li>A character pool is created including:
    <ul>
      <li>Whitespace</li>
      <li>Punctuation symbols</li>
      <li>Uppercase and lowercase letters</li>
      <li>Digits</li>
    </ul>
  </li>
  <li>The character list is copied to create a <strong>key</strong>.</li>
  <li>The key is shuffled randomly using <code>random.shuffle()</code>.</li>
  <li>Each character in the input sentence is:
    <ul>
      <li>Located in the original character list</li>
      <li>Mapped to the corresponding index in the shuffled key</li>
    </ul>
  </li>
  <li>The encrypted message is constructed using index-based substitution.</li>
</ol>

<hr>

<h2>Technical Concepts Demonstrated</h2>

<ul>
  <li><strong>Substitution Cipher Logic</strong></li>
  <li>Randomized key generation</li>
  <li>Index-based lookup operations</li>
  <li>List copying and mutation</li>
  <li>Iterative string construction</li>
  <li>Python standard libraries: <code>random</code>, <code>string</code></li>
</ul>

<hr>

<h2>Requirements</h2>

<ul>
  <li>Python 3.x</li>
</ul>

<hr>

<h2>Usage</h2>

<pre>
python encryption.py
</pre>

Example:

<pre>
Enter the sentence: Hello World!
Original message: Hello World!
Encrypted message: %k22@]X@p2q#
</pre>

<hr>

<h2>Educational Purpose</h2>

<p>
This project was developed to strengthen understanding of:
</p>

<ul>
  <li>Data transformation techniques</li>
  <li>Algorithmic thinking</li>
  <li>Character encoding logic</li>
  <li>Control flow structures in Python</li>
</ul>

<p>
While this implementation is not intended for real-world cryptographic security, 
it provides a clear demonstration of substitution-based encryption mechanics.
</p>

<hr>

<h2>Future Improvements</h2>

<ul>
  <li>Add decryption functionality</li>
  <li>Store and reuse generated keys</li>
  <li>Improve error handling for unsupported characters</li>
  <li>Convert into a modular, function-based structure</li>
</ul>

<hr>

<p align="center">
Developed as part of Python programming practice and algorithm exploration.
</p>
