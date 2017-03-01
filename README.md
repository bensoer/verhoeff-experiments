#verhoeff-experiments

verhoeff-experiments is a testing app that plays around with the verhoeff
algorithm. This algorithm is deemed better then the Luhn algorithm which
is currently used for credit card checksum validation (yes, 2017 last
digit of your credit card, is a checksum of the Luhn algorithm)

Luhn algorithm has a number of interesting flaws wikipedia can tell you
all about:
[https://en.wikipedia.org/wiki/Luhn_algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm)

The Verhoeff algorithm fixes some of these. Its strenghts and weaknesses
can also be found on wikipedia:

https://en.wikipedia.org/wiki/Verhoeff_algorithm

The code used in this program is taken respectfully from this page:
https://en.wikibooks.org/wiki/Algorithm_Implementation/Checksums/Verhoeff_Algorithm

I take no credit for any of the algorithm design and work. All content within
the `verhoeff.py` file is from the wiki link above

This application tests the verhoeff resistance to "twins" which is when
2 values beside eachother increment or decrement by 1. The verhoeff algorithm
is able to detect this change, and that's precisely what this program tests

#Installation

##Prerequisites
You will need python3 installed and available on your system

#Usage
To generate a verhoeff checksum for a given number execute the following command
```bash
python3 main.py -m GENCHECK -v 123345556
```
Substitute the `123345556` number with your own, or use it for demo. This
call will generate the checksum value and then append it to your passed in
number. Using this whole number, you can now start testing the verhoeff
checksum against "twins" with the following command
```bash
python3 main.py -m TESTCHECK -v 1233455562
```
This will go through and find all duplicate pairs in the passed in value.
From our above example it should test 33 and 55 and 55 (as there are 3 fives)
and then verify whether the checksum holds or not. Output is simply printed
out to the console stating whether the checksum is valid or not