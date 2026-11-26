# Independent mathematical audit

## correctness

PASS

In RESULT.md §§1–4 split n=a2^r+s with the same padded suffix before and after the shift. For a>0 that is not all ones, write a=U0^e1^j with U ending in 1. If j>0, the old and new internal zero runs have lengths e and e-1; if j=0 the new internal run forces e odd and the unchanged suffix's leading run must be even, giving an odd joined run in the old word. Thus a=2^j-1, allowing j=0. When j>0, both the suffix's leading zero length h and h+j must be even; for j=0 the incremented word supplies the required leading-zero condition even if n=0. Other zero runs must be even, and the converse follows by concatenation. The strict upper bound is exactly 2t+r<m with j=2t, and tiling gives F_(r+1) suffixes. Summing F_i for positive support lengths and adding zero gives F_(m+2), so the scale conclusions follow. The independent check `python3 /workspace/reproductions/exact_checks.py 3` uses recursive support generation and verifies 78 complete sets through m=12. The proof, not finite checks, gives the unbounded claim.

## originality

PASS

The distinct claim is the exact set and count of all forward support pairs at dyadic lags. The closest same-support records determine consecutive-gap statistics instead. Neither those results nor inspected automatic-sequence bounds supply the carry classification needed here. Priority is assessed only against inspected evidence.

## value

PASS

Powers-of-two shifts probe carry at prescribed binary scales in a standard sparse automatic support. The exact positions as well as counts explain the contrast between logarithmic growth at fixed lag and the positive support-relative incidence at half-block lag. This is a useful correlation benchmark distinct from consecutive gaps or single-point density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
