# Independent mathematical audit

## correctness

PASS

PASS: Multiplicativity and Omega<=3 exhaust exactly 2^a (a=1,2,3), 2p, 4p, 2p², 2pq. A power of 2 has σ=2^{a+1}-1 !=4φ=2^{a+1}; 2p gives p=7, 4p gives p=15 composite, 2p² gives discriminant61. For squarefree 2pq the equation is (p-7)(q-7)=48; all ordered positive factor pairs yield only primes (11,19), giving n=418. Verify σ(14)=24=4φ(14) and σ(418)=720=4φ(418). These exhaustive symbolic cases, not the supplied bounded n<200000 experiment, prove all even Omega<=3.

## originality

FAIL

FAIL: The existing OEIS A292422 subtable a292422_1.gp.txt, published prior to this submission, explicitly states "There are exactly 1 terms of the form 2^1 * p * q" and identifies that unique term as 418=2*11*19. Broughan--Zhou 2014 already classify the even two-distinct-prime-support branch, including 14; single-prime powers are immediately impossible. Thus the conjunction of a pre-existing complete k=1 exact classification with the stronger existing two-prime theorem covers the submitted full Omega<=3 result; new (p-7)(q-7)=48 algebra only reproves an exact previously documented classification. No distinct novel remainder survives.

## value

FAIL

FAIL: The complete claimed answer {14,418} is a routine repackaging of an explicitly complete, published first-exponent OEIS census for 2*p*q and a published full even two-support classification. The short five-factor-pair calculation is correct, but supplies no unknown exact invariant or genuine mathematically new boundary; the attempted natural Omega cutoff is already completely covered by these stronger results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
