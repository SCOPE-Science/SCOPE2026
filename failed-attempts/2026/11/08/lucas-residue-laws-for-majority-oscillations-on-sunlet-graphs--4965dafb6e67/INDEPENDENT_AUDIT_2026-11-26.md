# Independent mathematical audit

## correctness

PASS

The two-time spin energy is nonincreasing by symmetry, with strict decrease unless the states two times apart agree, since all degrees are odd. Thus no eventual period exceeds two. Under return after two updates the first rim equals the old leaf word; the two majority identities are equivalent to each bit occurring among the opposite-layer adjacent bits. This gives a bijection between labelled cyclic pair words and based closed walks, with no rotation quotient. Fixed states restrict to equal rim and leaf words, while pure states restrict to complementary rim and leaf words and hence exclude cyclic constant triples. Independently checked the degree-16 and both degree-4 characteristic polynomials by fraction-free integer determinant evaluations at degree+1 distinct points; independently enumerated the actual dynamics for 3≤n≤8. Replay: python3 /workspace/audit_work/sunlet_check.py. The three polynomial identities all matched and all six censuses matched the formulas. The uploaded scripts and captured outputs under code/ and results/ were inspected, not run. Evaluating trace powers by the roots gives the stated residue terms, with the octic contribution zero for odd n, −2L_n for n≡2,4 and 4L_n for n≡0 modulo 6. Orbit division by two and the asymptotic ratios follow. For the auxiliary undecorated-cycle comparison the proof uses the standard tie-retains-current-opinion convention (equivalently radius-one majority including self); that convention should be explicit, and is unnecessary on the sunlet itself.

## originality

FAIL

The earlier indexed sunlet result directly gives the fixed, total returning, and primitive two-cycle populations and their leading asymptotics, in an equivalent parity-factorized form. The possible remainder, the all-flipping population, follows mechanically by specializing that prior local constraint and applying the exact known labelled cyclic-word count in OEIS A007040. The fraction and contrast then follow from these known counts. The alternative transfer factorization does not supply a new census.

## value

FAIL

The periodic and pure-state populations are natural invariants, but the frozen finding repeats the prior census and mechanically translates an exact cyclic-word count for the sole residual statistic. The alternate finite determinant computation and the resulting direct ratios do not establish a distinct valuable mathematical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
