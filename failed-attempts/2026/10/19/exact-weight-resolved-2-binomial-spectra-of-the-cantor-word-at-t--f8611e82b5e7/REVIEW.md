# Independent mathematical audit

## correctness

PASS

A length-3^k window crosses at most one substitution-block boundary. The only source adjacencies are 00, 01 and 10, all occurring, so the all-zero block, padded prefixes and padded suffixes are exhaustive and all cuts occur. Palindromicity makes the last two families reversals. For weight w the scattered 01 count is the position sum minus binom(w,2), and the other scattered counts are determined by that count, n and w. Thus the fixed-weight cut interval [p_(w−1)+1,p_w] gives precisely the two displayed profile sets. Matching the two position sums requires cuts t,t' with t+t'=n+1+2U_w/w; counting integer cuts in the resulting intersection gives the stated I_w. The binary carry gives p_w−p_(w−1)=3^ν₂(w)+1 and the gaps telescope to n−1. All zeros and the whole Cantor block each give one endpoint profile, also when k=0. The bit-count formula for U_w follows from complete bit periods followed by the final incomplete period. Independent code (`/workspace/reproductions/5.py`) generated the word by ternary digit tests and directly accumulated all six scattered counts in every window of a 9·3^k prefix, then compared complete profiles at k=0,…,6, yielding 2,5,17,50,154,466,1402. It also checked the two length-27 examples. The supplied verifier was inspected, not executed, and its larger finite ranges are reported in the frozen source, not claimed as independent replay. The block proof, not the scan, establishes completeness for all k.

## originality

FAIL

A distinct indexed result states the same complete profiles in scattered-01 coordinates and the same overlap-based count for all nontrivial levels. The change of coordinates is invertible at fixed weight. The length-one endpoint, expanded gap formula and digit-sum bookkeeping do not supply a distinct substantive finding. The indexed record has a later catalog date, so the comparison establishes current equivalent coverage, not historical priority or derivation direction.

## value

FAIL

The triadic scale is natural for this substitution and the complete spectrum is useful for distinguishing scattered equivalence from contiguous equivalence. As a separate finding, however, the whole nontrivial spectrum and its total are already covered. The alternative coordinate, carry expansion and length-one boundary do not resolve an additional mathematical question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
