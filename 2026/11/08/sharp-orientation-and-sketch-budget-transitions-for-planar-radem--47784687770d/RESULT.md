# Sharp orientation and sketch-budget transitions for planar Rademacher Nyström selection

## Finding
Let \(b>0\), \(\kappa\ge1\), \(m\ge1\) be an integer, and let \(A_\theta=bR_\theta\operatorname{diag}(\kappa,1)R_\theta^{\mathsf T}\) be a real symmetric positive-definite \(2\times2\) matrix. Draw \(m\) independent vectors \(w_j\), each with independent equiprobable \(\pm1\) coordinates. For each, form the rank-one Nyström approximation
\[
\widehat A(w_j)=\frac{A_\theta w_jw_j^{\mathsf T}A_\theta}{w_j^{\mathsf T}A_\theta w_j}.
\]
Choose the candidate maximizing \(w_j^{\mathsf T}A_\theta w_j\), and denote its approximation by \(\widehat A_*\). Ties can be broken arbitrarily. Put \(t=|\sin(2\theta)|\) and \(q=2^{-m}\). Then, simultaneously for the nuclear, spectral and Frobenius norms, the *expected unsquared norm error* is
\[
\mathbb E\|A_\theta-\widehat A_*\|
=2b\kappa\left[\frac{1-q}{\kappa+1+(\kappa-1)t}
+\frac{q}{\kappa+1-(\kappa-1)t}\right]. \tag{1}
\]
Its sharp supremum over all orientations is
\[
\sup_\theta\mathbb E\|A_\theta-\widehat A_*\|
=b\max\left\{\frac{2\kappa}{\kappa+1},\ 1+\frac{\kappa-1}{2^m}\right\}. \tag{2}
\]
For \(\kappa>1\), the worst orientations are exactly \(t=0\) if \(\kappa+1<2^m\), exactly \(t=1\) if \(\kappa+1>2^m\), and the union of those two sets if equality holds. For \(\kappa=1\), all orientations tie.

With a single isotropic standard Gaussian probe and the same rank-one Nyström construction, the expected error is \(b\sqrt\kappa\) at every orientation. Therefore the best-of-\(m\) Rademacher method has expected error **no larger than the one-Gaussian method for every orientation** if and only if
\[
2^m\ge 1+\sqrt\kappa,
\qquad\text{equivalently}\qquad m\ge\left\lceil\log_2(1+\sqrt\kappa)\right\rceil. \tag{3}
\]
These are exact finite-dimensional thresholds, with equality cases determined by (1)–(2).

## Assumptions and scope
All arithmetic is exact. The matrix is real, symmetric, and positive definite, with ordered eigenvalues \(b\kappa\ge b>0\). Only the best *one-column* approximant among \(m\) independent single-probe candidates is retained. This is not the rank-\(m\) Nyström construction. The error is the expectation of an unsquared norm; it is not the expectation of a squared Frobenius error. Candidate selection uses a scalar quadratic score available from each matrix-vector multiplication. Independent probe signs are symmetric and each coordinate is \(\pm1\) with probability \(1/2\).

## Proof
**1. Exact residual in dimension two.** For every nonzero \(w\), the residual \(D=A-Aw(w^{\mathsf T}Aw)^{-1}w^{\mathsf T}A\) is positive semidefinite and rank one: it equals \(A^{1/2}(I-P)A^{1/2}\), where \(P\) projects onto \(A^{1/2}w\). By Cayley–Hamilton for a \(2\times2\) matrix, \(A^2=(\operatorname{tr}A)A-(\det A)I\). Consequently
\[
\operatorname{tr}D=\operatorname{tr}A-\frac{w^{\mathsf T}A^2w}{w^{\mathsf T}Aw}
=\frac{\det A\,\|w\|_2^2}{w^{\mathsf T}Aw}. \tag{4}
\]
For a positive-semidefinite rank-one matrix, its nuclear, spectral and Frobenius norms all equal its trace. For Rademacher \(w\), \(\|w\|_2^2=2\). Thus maximizing \(w^{\mathsf T}Aw\) exactly minimizes all three residual norms, with no unobserved trace information required.

**2. The two sign classes.** Multiplying \(w\) by \(-1\) does not change the approximation. The independent Rademacher vector therefore realizes the two directions \((1,1)\) and \((1,-1)\), each with probability \(1/2\). The two Rayleigh denominators are \(b[\kappa+1\pm(\kappa-1)\sin(2\theta)]\). Equation (4) makes the two possible residual norms
\[
L=\frac{2b\kappa}{\kappa+1+(\kappa-1)t},\qquad
H=\frac{2b\kappa}{\kappa+1-(\kappa-1)t},\qquad L\le H. \tag{5}
\]
All \(m\) candidates fall in the worse sign class with probability \(2^{-m}=q\). Otherwise at least one better candidate is selected. Hence \(\mathbb E\|D_*\|=(1-q)L+qH\), proving (1), including the tie case \(t=0\).

**3. Sharp orientation supremum.** The right side of (1), viewed as a function of \(t\in[0,1]\), is convex, and it is strictly convex when \(\kappa>1\): each reciprocal affine term has positive second derivative (both coefficients \(q\) and \(1-q\) are positive). Its supremum therefore occurs only at the endpoints. Direct substitution gives \(F(0)=2b\kappa/(\kappa+1)\) and \(F(1)=b[1+(\kappa-1)2^{-m}]\). Their difference has the sign of \(\kappa+1-2^m\) for \(\kappa>1\), because
\[
\frac{F(1)-F(0)}{b}
=\frac{(\kappa-1)(\kappa+1-2^m)}{2^m(\kappa+1)}. \tag{6}
\]
Every \(t\in[0,1]\) is attained by an angle \(\theta\). This proves (2) and all maximizer classifications.

**4. Exact Gaussian benchmark.** Let \(g\) have two independent standard normal components. Its direction is uniform on the circle, and the length cancels in (4). Diagonalizing \(A\) and using the classical trigonometric substitution \(u=\tan\phi\) in each quadrant yields
\[
\mathbb E\operatorname{tr}(A-\widehat A(g))
=\frac{\det A}{2\pi}\int_0^{2\pi}
\frac{d\phi}{b\kappa\cos^2\phi+b\sin^2\phi}
=\sqrt{\det A}=b\sqrt\kappa. \tag{7}
\]
Finally \(2\kappa/(\kappa+1)\le\sqrt\kappa\) by the arithmetic–geometric mean inequality. For \(\kappa>1\), the other endpoint in (2) is at most \(\sqrt\kappa\) precisely when \(2^m\ge(\kappa-1)/(\sqrt\kappa-1)=\sqrt\kappa+1\). For \(\kappa=1\) all errors equal \(b\). This proves (3).

## Verification
Run `python3 verification/check.py` with Python 3 standard libraries. Its recorded output in `verification/output.txt` is `PASS: 33062 assertions; exact rational, direct matrix and angular-integral checks`. The script independently evaluates the original \(2\times2\) matrix residuals at representative angles, exactly compares the endpoint bound for integer condition ratios using rational arithmetic, checks the candidate-count threshold, and numerically integrates the Gaussian benchmark. The exact equalities for arbitrary real parameters and all integer \(m\ge1\) are established analytically above; these finite tests are not a substitute for the proof.

## Relationship to prior work
Saibaba and Międlar (arXiv:2308.05814, first posted 2023-08-10) analyze Gaussian and non-Gaussian low-rank sketches; their Section 3 gives distribution-class guarantees and Appendix D applies sufficient conditions to randomized Nyström approximation. Those bounds require conditions on sketch width and do not state the exact planar one-column **best-of-independent-candidates** orientation risk or the Gaussian-comparison threshold (3). Dereziński, Liang, Liao and Mahoney (arXiv:2006.10653, first posted 2020-06-18) give an approximate expected residual-projection formula in a high-stable-rank regime for Gaussian and Rademacher sketches. Their stated fixed stable-rank-to-sketch-size conditions and approximation are not the exact two-dimensional, rank-one extremal calculation here. Exact orientation dependence, the optimizer switch at \(\kappa+1=2^m\), and the logarithmic threshold (3) are the specific assessed contribution. These comparisons do not amount to a claim of exhaustive publication priority.

## Limitations
The statement applies only to the exact-arithmetic \(2\times2\) positive-definite setting, a one-column rank-one approximation, fair independent Rademacher probes and best-of-\(m\) selection. The \(m\) independent candidate sketches require \(m\) matrix-vector products, whereas the Gaussian comparator uses one; (3) is an error benchmark, not a cost-equivalent superiority claim. It does not assert a high-dimensional result, a squared-error bound, or improvement from combining all candidate columns. It is possible that related exact two-direction evaluations appear in specialist work not identified here; independent publication-priority review remains outstanding.

## References
1. A. K. Saibaba and A. Międlar, *Randomized low-rank approximations beyond Gaussian random matrices*, arXiv:2308.05814 (first public version 2023-08-10), https://arxiv.org/html/2308.05814v1 ; Section 3 and Appendix D.
2. M. Dereziński, F. Liang, Z. Liao and M. W. Mahoney, *Precise expressions for random projections: Low-rank approximation and randomized Newton*, arXiv:2006.10653 (first posted 2020-06-18), https://arxiv.org/abs/2006.10653 ; Introduction and Theorem 1.
