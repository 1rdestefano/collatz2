When I initially learned about the Collatz conjecture, the video claimed that each number had a unique number of steps in the sequence. My first thought was that the upward bumps of 3x+1 could make an interesting encryption key if we changed that to ax+b, where a, x, and b are natural numbers and b must be an odd number.
However, the unique claim proves to be untrue. Multiple numbers have the same number of steps in their sequence, so the encryption idea isn't going to work.
I want to take this program one step further: To be able to check large ranges of natural numbers for sequences, and only report sequences that do not end in the (...4,2,1) pattern.
In this step, the number of bumps up and down will no longer apply, so I will trim that code out and just add a boolean check for one as the last natural of the sequence.
I also noted that 10,000,000 searches took over a minute, so I added a timer. Below are a couple noted time factors to give you an idea of how long each range will run.
  * 2 - 1,000,000 tests = 27.4 seconds
  * 1,000,000 - 2,000,000 = 29.4 seconds
  * 2 - 10,000,000 = 311.8 seconds