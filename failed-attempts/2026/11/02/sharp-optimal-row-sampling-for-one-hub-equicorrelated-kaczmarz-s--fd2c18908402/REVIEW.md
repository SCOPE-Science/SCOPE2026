# Independent mathematical audit

## correctness

PASS

For a unit-row projection the conditional squared decrement is e^T A^T diag(p) A e; this sharp one-step objective is concave and invariant under leaf permutations. For common leaf probability q, the radial block in the weighted Gram matrix has trace p_0+cq and determinant (c−ma²)p_0 q, and the contrast eigenvalue is (1−b)q. With alpha=c/m and delta=alpha−a²>0, the characteristic polynomial at lambda_R=delta/(1+alpha+2a) expands to −delta[p_0−(alpha+a)/(1+alpha+2a)]²; at zero of this square lambda_R is the smaller radial eigenvalue. Concavity in a fixed radial covariance basis implies strict increase until its unique maximum. After dividing by q, the determinant at the contrast level is m[t(b−a²)−b(1−b)]. For b≤0 the radial level is always smaller by its diagonal entry c; for 0<b≤a² the determinant is negative; for b>a² it crosses once before or after the radial maximizer. Comparison with t_0 gives the stated switch inequality, and substitution gives the rates and the limiting cases. For an arbitrary optimum, symmetrizing fixes its hub probability, so its Rayleigh quotient on a radial minimizing eigenvector equals rho_* exactly. This entails the full eigenvector equation for the unsymmetrized law; subtraction and invertibility of A force equal weights since a>0 and positive optimal weights ensure both row response types are nonzero. The reasoning holds at the crossing. The supporting script was inspected, not executed; numeric comparisons are not proofs of uniqueness.

## originality

FAIL

Two earlier statements cover the full domain. The 2026/10/26 equicorrelated-block theorem gives the exact two branches, values, threshold and unrestricted uniqueness for all b>0. An earlier inverse-positive optimization theorem gives the supposedly remaining b≤0 case after changing the hub row sign, which leaves every sampling objective unchanged. The frozen objection that the unsigned inverse has negative hub–leaf entries does not rule out this equivalence. The asymptotic and dimension-ratio observations are algebraic consequences of the existing allocation formulas. This is affirmative prior coverage, not a retrieval failure or a claim about historical authorship.

## value

FAIL

An exact allocation and active-mode threshold are useful for understanding this Gram family, but those facts are already supplied by the positive-correlation theorem; the remaining computation is a two-entry evaluation of the signed inverse-positive theorem, and the limits are immediate from the displayed laws. No independently useful unknown fact remains in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
