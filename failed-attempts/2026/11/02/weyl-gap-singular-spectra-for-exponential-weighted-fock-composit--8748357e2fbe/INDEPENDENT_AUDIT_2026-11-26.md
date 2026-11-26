# Independent mathematical audit

## correctness

PASS

Direct Weyl substitution gives W=lambda U_v D_a U_w with the stated v,w and |lambda|=N. Multiplying the two factorizations leaves the middle displacement w_1-w_2 in W_1W_2^* and v_2-v_1 in W_1^*W_2 (irrelevant projective phases). For D_a U_t D_{c-bar}, the affine parameters are a*c-bar, -c-bar*t and a*t-bar; the scalar prefactor is exp(-|t|^2/2). Applying the normalization gives v=a-bar*(1-|c|^2)t/(1-|ac|^2), hence the claimed scalar penalty by direct cancellation. The monomial singular values of the remaining dilation are |ac|^k in decreasing order. The scalar penalty is nonzero, so when either slope vanishes the product has rank exactly one, not zero. Weyl unitarity and the Schatten geometric series prove the edge cases and the equal-slope reversal as stated. No finite truncation needed for these analytical claims; checker.py was inspected, not run.

## originality

FAIL

The formulas are correct but mechanically covered by Fatehi's 2018 kernel-weight theory, not merely neighboring single-factor results. The proof of Proposition 2.3 explicitly makes every such operator a scalar times an unweighted affine composition by unitary conjugation. Each cross-product and its positive square belong to the very same class by the kernel adjoint formula. Applied to a positive square, the translated unweighted affine composition must have zero translation: the scalar is positive by testing on constants, and self-adjointness and C1=1 give C^*1=K_b=1. Thus the square is unitarily equivalent to ||S||^2 D_{|slope(S)|^2}. Theorem 4.2 supplies ||S|| for each cross-product. Completing the square in this known norm, or substituting a*c-bar, -c-bar*t and a*t-bar for the compressed Weyl factor, gives exactly the two Gaussian penalties. The qualitative reversal independently follows from ordinary compactness and Weyl translation, as below. No distinct claim survives beyond the covered specialization and presentation.

## value

FAIL

The normalized two-gap packaging is a useful explanatory calculation, but its quantitative data are directly read off from the existing norm and unitary reduction for a class already closed under the operations. Unbounded ratio reversal is an immediate compact-sandwich observation once the known Weyl factors are chosen. The record supplies no independently unknown exact datum or nonroutine structural remainder to retain as a research finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
