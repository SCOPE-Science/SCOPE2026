# Independent mathematical audit

## correctness

PASS

Inserting the next label into an existing cycle or a new singleton of either colour gives the total (n+1)!. A prescribed j-position singleton set contributes 2^j(n−j+1)!, so expansion of the character as a product of (1−2 1_fixed) gives the displayed multiplier under unnormalized XOR convolution. The multiplicity of shell k is binomial(n,k). With density x exp(−x) on x>0 the moment representation is E[X^(n−k)(X−4)^k]. Subtracting adjacent shells inserts a factor 4, giving 4 times the shell k multiplier at order n−1. Integration by parts gives E[X f′]=E[(X−2)f]; for f(x)=(x−4)^n this yields M_(n+1)=(n−2)M_n+4n M_(n−1). The boundary spectra through n=8 give the sole null shell n=3,k=1 (nullity 3, rank 5), the negative shell at n=7 and the other claimed finite signs. The positive n=8 row and diagonal values M_8=15744, M_9=71936 start the joint induction: the next row strictly decreases, and its last entry stays positive by the recurrence. In positive dimensions k=0 is maximal by nonnegative counting mass; the sharp minima at n=6 and 8 are 112 at k=5 and 12928 at k=7, giving condition numbers 45 and 2835/101. For n≥9 the minimum is M_n. Dividing its sum by (n+1)! bounds each zero-extended term by 4^j/j! and gives termwise limit (−4)^j/j!, so the normalized minimum tends to e^−4. From /workspace, python3 reproductions/algebra.py walsh independently enumerated cycle-weighted permutations and applied an integer fast Walsh transform to the entire fixed-position histogram for n=1–8, matching all claimed rows. The frozen verifier was inspected, not executed. Neither finite check proves the all-order classification; the recurrence and domination argument do. No other number of cycle colours or non-Euclidean condition number is asserted.

## originality

PASS

Pass the supported all-order two-colour Walsh sign and exact conditioning classification. Ewens enumeration, the weighted fixed-set coefficients, and the equivalent weighted-derangement moment transform are prior or close deductions, not standalone novelty. The closest inspected full-set spectral record is for unweighted permutations; it does not cover the two-colour exceptional dimensions or sharp minima.

## value

PASS

The fixed-position incidence of a canonical nonuniform permutation measure is a natural recovery observable. The complete result distinguishes invertibility from positive definiteness, exhibits the isolated positivity and subsequent failure at n=6 and 7, and gives sharp stable recovery constants rather than a bound or a few numerical spectra. This adds substantive information beyond weighted-derangement counting and beyond the uniform-permutation spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
