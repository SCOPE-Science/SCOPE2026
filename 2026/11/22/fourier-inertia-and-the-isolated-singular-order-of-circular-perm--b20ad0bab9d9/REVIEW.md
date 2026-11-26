# Independent mathematical audit

## correctness

PASS

The signature uses cyclic positions and cyclic values, and counts all permutations with counting-measure normalization. A proper set of j designated edges fixes consecutive-value runs; a circular order of the n-j distinct runs and any of the n value choices at a fixed position reconstruct a unique permutation, also when there is one run. All n edges instead force a rotation. Expanding the sign product gives the stated two formulas and binomial weight multiplicities. For proper weights the difference F(r,k)-F(r,k+1)=2F(r-1,k), the positive r=4 row and F(r,r)=r! S_r prove the monotonicity and positivity claims: alternating terms from j=2 onward yield 1/15<=S_r<=1/3 at r>=5. For full weight the generating function e^(-2z)[-log(1-z)] yields n b_n=S_(n-1)-2b_(n-1). The exact base b_9=11/756 and these bounds give 0<b_n<1/30 at n>=9. For odd n>=13, the previous recurrence yields b_(n-1)<1/[3(n-1)] and hence b_n>1/(90n)>2^n/n!; the latter is exact at n=13 and n*2^n/n! decreases thereafter. The even tail is automatically positive. Independent replay `python3 /workspace/review_replay.py 2` reconstructed all frequencies from permutations at n=2..9, recovered the five listed small-order inertia triples, and verified b_9 and the full weights at n=7..12 by rational arithmetic. At n>=7 the trivial multiplier n! is maximal by the triangle inequality and proper weights decrease strictly, so only the penultimate and full weight compete for the minimum. No finite check is used to extrapolate inertia.

## originality

PASS

Credit the full incidence distribution and its direct Walsh transform to existing enumeration. The surviving distinct claim is the joint all-order classification of spectral signs and singularity and the sharp two-weight reduction of the positive minimum.

## value

PASS

For the standard cyclic succession incidence law, the distinguishable questions of losing modes, preserving signs, and exact stability are answered for infinitely many orders. A unique singular order and several isolated indefinite orders emerge from a nontrivial all-order sign argument on the same enumerator, not a small table or a Poisson-limit restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
