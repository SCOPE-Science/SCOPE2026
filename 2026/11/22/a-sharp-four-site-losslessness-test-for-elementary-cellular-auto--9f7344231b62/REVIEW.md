# Independent mathematical audit

## correctness

PASS

On the no-11 input shift the only possible triples are 000,001,010,100,101; each effective mask therefore represents eight Wolfram rules. Failure of the tests c≠e, not(b=c=d), and not(a=c and b=d) gives collisions of cyclic words (01,10), (001,010), and (1000,0010), respectively, hence also distinct bi-infinite periodic inputs. The successive exclusions have sizes 16,4,2 in mask space, leaving 4,6,7,12,13,18,19,24,25,27. Mask 4 copies the center. For masks 6 and 7, a center 1 guarantees y_i=1 and y_(i+1)=0 because the next triple is 100 or 101. If the center is 0 with y_i=1, the triple is 001 or (for 7) 000, in either case forcing y_(i+1)=1. This proves the right-looking decoder. Reflection gives the left-looking decoder for 12 and 13; bit complement gives the other five masks. These pointwise arguments hold on every allowed input and on all periodic extensions, including repeated indices on short rings. For masks 6 and 7, 010 and 001 give the same new center for different old centers; the reflected and complemented cases inherit the obstruction. Thus only masks 4 and 27 admit radius zero, giving 16 rules. An independent exact loop over all 256 rules, retaining length-n bit strings with no adjacent ones including wraparound and looking for equal encoded outputs, found 128 first collisions at n=2, 32 at n=3, 16 at n=4, and 80 rules without a collision at n≤4. The n=4 failures are masks 5 and 26, including Rule 5; it passes n=1,2,3 and 1000 versus 0010 collides at n=4. Replay: frozen RESULT.md lines 28–54, cyclic bit-code loop just described; VERIFICATION.md and verify.py inspected, not executed. No infinite conclusion is extrapolated from the ring enumeration.

## originality

PASS

The supported distinct contribution is the all-rule constrained-source classification, including its three Boolean tests, universal four-site cutoff, sharpness and exact decoder-radius census. Known or companion single-rule results overlap their cases, not the full classification.

## value

PASS

One-step lossless decoding of a canonical constrained binary source is a natural exact problem. The four-site sharp cutoff gives a practical complete test for a statement over bi-infinite inputs, and the explicit decoders and minimal-radius census convert classification into uniform reconstruction. Unrestricted reversibility or the existence of any uniquely invertible block cannot answer this question. The result concerns input restriction, not preservation of the source shift or invertibility of an unrestricted update.

The dated certificate retains the supplied scientific assessment, sources and limitations.
