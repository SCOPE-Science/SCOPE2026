# Independent mathematical audit

## correctness

PASS

At fixed q,u,v, unitary conjugation gives the lower-triangular kernel r^(j−i)√(d_j/d_i)/j, r=√q, a compact diagonal times a bounded geometrically summable operator. In odd/even blocks the even-to-odd transfer starts at lag one and the odd-to-even transfer at lag zero, giving F(z)=(1−qz)⁻¹[[1,ar z],[r/a,1]]. Discarding the first block and replacing the remaining paired diagonal by 1/(2k) changes the operator only by finite rank and a summable O(k⁻²) diagonal times a bounded operator. For the counting lemma in RESULT.md lines 47–59 I checked the limit without assuming uniform convergence of symbol counts at atoms: for a banded symbol, cut the block indices at finitely many fixed scaled points x=tk on [ε,R], chosen at continuity points of the symbol distribution. Separating the pieces costs rank bounded independently of t. The head costs at most dε/t+O(1) rank, and the tail has norm below t for R>||B_F||. On each middle piece, the smallest and largest diagonal values sandwich the weighted singular numbers by scaled unweighted singular numbers; block circulants differ by bounded rank and sample the symbol on a Fourier grid. Upper and lower sums converge to the integral of the symbol counting function as the scaled mesh shrinks and ε→0. Uniform approximation by band symbols then uses tN(ηt;D(B_F−B_M))≤d||B_F−B_M||/η and the singular counting inequalities at (1±η)t. Trace-class errors have tN(t)→0; count inversion applies since the coefficient is positive. With two indices per block the coefficient is (4π)⁻¹∫||F||_*; the determinant modulus is 1/Δ and the Frobenius norm squared is [2+q(a²+a⁻²)]/Δ². The two-by-two nuclear norm identity gives the displayed integral. Its strict increase in a²+a⁻² gives absolute log-contrast only, not parity. The neutral pair folds to the scalar symbol; equal Bloch singular values force equal column norms and zero inner product, i.e. a=1 and z=−1. At z=−1 the squared difference is q(a−a⁻¹)²/(1+q)². Compactness reduces the nonzero spectrum to eigenvalues, and the first nonzero coordinate plus the explicit polynomial-growth binomial eigenvectors give exactly 1/j. The Schatten and log-average consequences follow from s_n∼K/n. The supplied checker was inspected, not run; there is no required finite computational proof step.

## originality

FAIL

The leading indexed law is a direct specialization of the existing Birman–Solomyak classical matrix-valued pseudodifferential Weyl law (as stated in Ponge §2.3, and also obtained from his Theorem 4.1). The circle/positive-frequency realization meets the hypotheses and gives exactly the claimed contrast-dependent integral, not just a finite-section distribution or the scalar subcase. The strict recovery of absolute contrast and the band meeting/splitting follow by elementary two-by-two matrix identities for the same symbol; the spectral and summability consequences do not provide a distinct new remainder. This is positive prior-implication evidence, not a finding of an identical earlier printed weighted Cesàro formula or a rejection based on inaccessible literature.

## value

FAIL

The geometric alternating weights and contrast diagnostic are natural, and the elementary counting proof can be helpful exposition. As a research finding, however, the purported new invariant is determined mechanically by a prior indexed matrix-symbol theorem through the two-cell representation. Strict contrast sensitivity follows at once from the two-by-two trace norm, and the gap is the direct zone-edge eigenvalue calculation. There is no separate substantial result outside that coverage: no nonneutral remainder estimate, finite-index characterization, or recovery of the parity phase. Thus the record does not establish an independently valuable new exact fact under the stated standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
