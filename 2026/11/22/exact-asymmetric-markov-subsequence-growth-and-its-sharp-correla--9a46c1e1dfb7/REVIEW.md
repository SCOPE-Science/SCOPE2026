# Independent mathematical audit

## correctness

PASS

Appending b replaces the set of words ending in b by all old subsequence strings (including the empty one) with b appended, leaving the other ending class unchanged. Conditioning on the last bit gives the displayed recurrence with stationary forcing. Independently, a greedy first-match transfer gives the same scalar law: set A=1-(1-p)z and B=1-(1-q)z; the successive-match entries H01=pz/A and H10=qz/B, H00=(1-p)z+pqz²/B and H11=(1-q)z+pqz²/A encode first hitting times. The initial row is zL(q/B,p/A)/s; summing all nonempty target lengths and then all host lengths gives the numerator zL[s(1-z)L+2pqz] and the stated denominator. The characteristic factors leave exactly one eigenvalue above one, from the minus-square-root factor. Since p,q>0, the four-state matrix is irreducible even at p=q=1. Using a strictly positive left Perron vector, the forced geometric sum bounds the observed total above and below by constant multiples of the Perron sum; no primitivity or cancellation assumption is needed. Implicit differentiation at fixed frequency gives t²/[s(2t+s(1-c))]>0 for t=Lambda-1 and c=sqrt(theta(1-theta)); the admissible upper endpoint is where the minority cannot repeat. A separate exact enumeration matched the claimed series for (p,q)=(1/2,1/3) through n=7 and for the alternating endpoint through n=10. The package verifier was read, not run.

## originality

PASS

Credit the known stationary binary Markov recurrence and the already evaluated iid and symmetric cases. The distinct result is the evaluated asymmetric scalar law with a quadratic Perron root and its strict fixed-composition comparison. The strongest primary match specifically leaves solving the recurrence and computing growth rates as questions, and the strongest catalogue match requires symmetry.

## value

PASS

The result evaluates a natural statistic previously left in four coupled Markov recurrences, giving a usable closed rate rather than a generic quartic. It separates serial dependence from letter composition and identifies the unique maximizing chain and the strict position of iid between persistence and antipersistence. Those comparisons are useful without treating known symmetric or iid formulas as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
