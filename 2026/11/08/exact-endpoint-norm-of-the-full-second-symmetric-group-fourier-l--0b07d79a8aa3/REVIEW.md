# Independent mathematical audit

## correctness

PASS

The pair-subset permutation character subtracts the natural character to give chi_A=F(F-3)/2+C_2. Exterior square of the standard module gives chi_B=(F-1)(F-2)/2-C_2. Degrees d_A=n(n-3)/2, d_B=(n-1)(n-2)/2 differ by one, so their weighted sum is the exact central kernel K=d_A F(F-3)/2+d_B(F-1)(F-2)/2-C_2. For F=1,2 it equals -d_A-C_2<0; for F=0 or 3 it equals d_B-C_2>0 (all n>=4), and for F>=4 all positive. Both characters have zero group mean. Count marked transpositions among permutations with r=1 or 2 fixed points using choose(n,r)choose(n-r,2)D_{n-r-2} and derangement inclusion-exclusion to derive norm=(3(n^2-3n+1)/2)E_{n-2}+(-1)^(n-2)(5-n^2)/(2(n-1)!). Alternating-series bounds prove 3/(2e); at the identity the complementary kernel is positive because other irreducibles exist. Independent exhaustive enumeration for 4<=n<=8 covered 46,224 permutations, all signs/zero mass and exact norms (e.g. n=4 17/6, n=5 71/12, n=8 114053/5040). Finite checks corroborate the character proof.

## originality

PASS

Published one-block (n-2,2) endpoint norm is based on fixed points AND transpositions; the full two-block sum has a different sign support due to the weighted C_2 coefficient -1 and its limit 3/(2e), not the one-block 3e^-3/2/2. Published two-subset permutation-band result includes trivial and standard and (n-2,2), not (n-2,1,1), and thus is not this projection. Johnson spherical degree-two acts on a homogeneous subset action rather than regular S_n. The general equivariant projection principle and character polynomials predate the claim; the exact two-block absolute norm is the best-of-knowledge new content.

## value

PASS

A complete sharp endpoint norm for a natural full second representation level, with exact C_2-cancellation, a strict two-fixed-point sign law, and a different asymptotic constant than single-block or Johnson projections, is a motivated and nontrivial Fourier-algebra stability calculation. Its absolute value cannot be obtained by summing known individual norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
