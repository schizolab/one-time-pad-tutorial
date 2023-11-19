# one-time-pad-tutorial
How to use one time pad to encrypt and decrypt easily with hand, with just pen and paper.

schizolab@tiktok

## Why one time pad?

Because it is so KISS (keep it simple stupid), the attacker can only seethe, it is theoretically impeccable if you do it strictly. Never use used keys.

## How it works

You have

1. `plain text`
2. `key`
3. `cipher text`

### Encoding

First You convert your plain text to binary base 6 using this Encoding LUT (`LUT1`) (LUT is Look Up Table)

|      |0 |1 |2 |3 |4 |5 |
|------|---|---|---|---|---|---|
|0    |0  |1  |2  |3  |4  |5  |
|1    |6  |7  |8  |9  |A  |B  |
|2    |C  |D  |E  |F  |G  |H  |
|3    |I  |J  |K  |L  |M  |N  |
|4    |O  |P  |Q  |R  |S  |T  |
|5    |U  |V  |W  |X  |Y  |Z  |

I'm going to index vertically first, then horizontally.

So `SZL` is 44, 55, 33. Wait those are all doubles, is the name `schizolab` blessed?

Ok, so `A` is 41. That's your `plain text`.

### Key generation

Then you XOR this with a table of `key`s, your one time pad, you can generate with 

```
head -c 256 /dev/random | xxd -p | tr -dc '0-5' | fold -w 6
```

Run it on Linux of course.

This takes 256 bytes from kernel hardware entropy source, converts them into hex, filter 0-5, then converts them into 6 digit groups.

This should look like this:

```
405201
415255
041512
350505
223232
315551
150425
223453
014244
412052
521450
214323
044245
```

This is your one-time-pad, you and your partner(😭 nobody to use it with) should note this down with you. 

Be mindful of what's under your paper, did you imprint your keys onto the paper below? Don't be lazy and use a printer, they remember stuff.

The reason why it's called **one time** pad is because you should only use it ONCE, cross the key you've used with a pen ~~405201~~ and never use it again.

### Encryption

Then you XOR your message with the one time pad using the XOR LUT (`LUT2`) below:

|   | 0 | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 1 | 2 | 3 | 4 | 5 |
| 1 | 1 | 0 | 3 | 2 | 5 | 4 |
| 2 | 2 | 3 | 0 | 1 | 6 | 7 |
| 3 | 3 | 2 | 1 | 0 | 7 | 6 |
| 4 | 4 | 5 | 6 | 7 | 0 | 1 |
| 5 | 5 | 4 | 7 | 6 | 1 | 0 |


So to encrypt `A`(41) is like, we have 40 in the `key` right? 4 XOR 4 = 0, 1 XOR 0 = 1. Your `cipher text` is 01.

### Decryption

To decrypt, you take 0, from the row header, then look at your keys, which is 4, index with the column header, that gives you 4, that's you `plain text`. Do the same with 1, you get 1. 

Now you have 41, look up in the `LUT1`, YESSSS you have the orignal `A`!!

#### You might end up with a 6 or 7 in encryption but that's ok

Let's say
A XOR B == C

Then it is true that: C XOR B == A, and C XOR A == B

Therefore, you find the 6 or 7 in the middle of the LUT, not the headers, and input the key from the vertical or horizontal header, and in another header it appears.

Let's say you cipher 7, your key is 5, you find 7 in the middle, there are 4 instances. Then you input 5 from the horizontal header, you get 2 in the vertical header.

### Protocol header

You can say: ok imma bout to use the key starting at line 5. Then you tell your encrypted message.

## The Python scripts in this repo

I use them to generate the XOR LUT (`LUT2`), I didn't want to calculate them by hand, prone to error, also provides no sauce of reference.

Just run

```
python gen-base6-xor-csv.py 
```

or

```
python gen-base6-xor-markdown.py
```

to generate `xor-lut.csv` or `xor-lut.md` into this root folder.

## Sauce that inspired me

https://en.wikibooks.org/wiki/Cryptography/One_time_pads
