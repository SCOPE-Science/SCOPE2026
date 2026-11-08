# Two sharp condition-number frontiers for Euclidean nonexpansion of three-coordinate Gauss–Seidel

## Finding
Consider the equicorrelated symmetric matrix
\[
H_\rho=(1-\rho)I_3+\rho\mathbf1\mathbf1^T,
\qquad -\frac12<\rho<1,
\]
and exact cyclic coordinate minimization of the positive-definite quadratic \(f(x)=\tfrac12x^TH_\rho x-b^Tx\), equivalently forward Gauss–Seidel applied to \(H_\rho x=b\). Denote by \(B_\rho\) its full-sweep error propagation matrix, in the ordinary, unweighted Euclidean norm. Define
\[
P(t)=6t^4+2t^2-t-1,
\]
and let \(\rho_-\in(-1/2,0)\) and \(\rho_+\in(0,1)\) be its two real zeros. Then, for **every** \(-1/2<\rho<1\),
\[
\boxed{\quad\|B_\rho\|_2\le1\iff\rho_-\le\rho\le\rho_+\quad}
\]
with equality exactly at the two endpoints. The roots, isolated by rational intervals, are
\[
\rho_-=-0.4289330764835166\ldots,\qquad
\rho_+=0.6150319598254620\ldots.
\]
Outside that closed interval, some initial Euclidean error grows strictly in one complete sweep even though the quadratic objective decreases and the iteration converges asymptotically. All six permutations of the coordinate update order have exactly the same singular values, so changing the order cannot avert expansion in this symmetric family.

The condition number \(\kappa=\kappa_2(H_\rho)\) leads to **two distinct sharp frontiers**, depending on the sign of the correlation:
\[
\kappa_+=\frac{1+2\rho_+}{1-\rho_+}=5.792854696820678\ldots,
\qquad
\kappa_- =\frac{1-\rho_-}{1+2\rho_-}=10.053432777008336\ldots.
\]
For a given \(\kappa>1\), the positive-correlation member is Euclidean-nonexpansive iff \(\kappa\le\kappa_+\), whereas the negative-correlation member is Euclidean-nonexpansive iff \(\kappa\le\kappa_-\). Hence in the entire interval \(\kappa_+<\kappa\le\kappa_-\), the two matrices have **identical condition number but different one-sweep Euclidean nonexpansion behavior**. The rational witness \(\kappa=6\) has \(\rho=5/8\), which expands, and \(\rho=-5/13\), which contracts.

The exact singular-norm profile is
\[
\boxed{
\|B_\rho\|_2^2=\frac{\rho^2}{2}
\left[S(\rho)+\sqrt{S(\rho)^2-4(1+2\rho^2)}\right],
\quad S(t)=2t^4-6t^3+7t^2-2t+3.
}
\]
In particular, with \(\varphi=(1+\sqrt5)/2\), the norm satisfies
\[
\|B_\rho\|_2=\varphi|\rho|+O(\rho^2)
\qquad(\rho\to0),
\]
while for positive \(\rho\), the exact nonzero spectral eigenvalue modulus is only \(\rho^{3/2}\). The singular-to-spectral ratio therefore diverges as \(\varphi/\sqrt\rho\) toward the decoupled limit.

## Assumptions and scope
All matrices are real and all arithmetic is exact. The strict interval \(-1/2<\rho<1\) is precisely the positive-definite range, since \(H_\rho\) has eigenvalues \(1-\rho\) twice and \(1+2\rho\) once. A sweep makes one exact scalar minimization for each coordinate; the error is measured in \(\ell_2^3\), not the \(H_\rho\)-energy norm. The condition-number comparison uses the unique positive- and negative-correlation matrices in this normalized equicorrelation family at fixed \(\kappa>1\). No claim is made for arbitrary three-dimensional positive-definite matrices, different coordinate norms, or inexact updates.

## Proof
**1. Exact sweep and eigenvalues.** For errors measured relative to the exact minimizer, the sequential coordinate equations are
\[
e_1^+=-\rho(e_2+e_3),\quad
e_2^+=-\rho(e_1^++e_3),\quad
e_3^+=-\rho(e_1^++e_2^+).
\]
Thus
\[
B_\rho=\begin{pmatrix}
0&-\rho&-\rho\\
0&\rho^2&\rho(\rho-1)\\
0&\rho^2(1-\rho)&\rho^2(2-\rho)
\end{pmatrix}.
\]
Direct expansion gives
\[
\det(\lambda I-B_\rho)
=\lambda[\lambda^2-\rho^2(3-\rho)\lambda+\rho^3].
\]
For \(0<\rho<1\), the quadratic discriminant \(\rho^3(\rho-1)^2(\rho-4)\) is negative, so the two nonzero eigenvalues are conjugate with modulus \(\rho^{3/2}\). For \(-1/2<\rho<0\), it is positive and the two nonzero eigenvalues are real with opposite signs. The standard strict coordinate-minimization descent identity supplies \(\rho(B_\rho)<1\) throughout the positive-definite range: any nonzero starting error incurs at least one strict decrease in the positive energy \(e^TH_\rho e\), because unchanged coordinates over the entire sweep would imply \(H_\rho e=0\). Thus \(e^TH_\rho e\) is strictly decreasing under the complete sweep for every nonzero \(e\), excluding all eigenvalues of modulus at least one.

**2. Gram determinant and the exact norm.** The first column of \(B_\rho\) vanishes, so its nonzero singular values are those of the remaining \(3\times2\) block. Let \(G\) be this block's \(2\times2\) Gram matrix. Direct polynomial multiplication gives
\[
\operatorname{tr}G=\rho^2 S(\rho),\qquad
\det G=\rho^4(1+2\rho^2),
\]
\[
\det(I_2-G)=(\rho-1)P(\rho).
\]
Solving the quadratic for the eigenvalues of \(G\) gives the claimed exact norm formula, including its value zero when \(\rho=0\).

**3. Sharp global sign classification.** Since
\[
P''(t)=72t^2+4>0,
\]
\(P\) is strictly convex. Its values at \(-1/2,0,1\) are \(3/8,-1,6\), respectively. Thus its only real zeros are exactly \(\rho_-\in(-1/2,0)\) and \(\rho_+\in(0,1)\); \(P(t)\le0\) exactly between them. More precisely, evaluating \(P\) at the rational endpoints \(-4290/10000,-4289/10000,6150/10000,6151/10000\) certifies the indicated enclosures. Moreover \(P(2/3)=11/27>0\), so both roots lie inside \((-2/3,2/3)\). Whenever \(P(\rho)\le0\), therefore,
\[
\det G\le\left(\frac23\right)^4\left(1+2\left(\frac23\right)^2\right)
=\frac{272}{729}<1.
\]
Because \(\rho-1<0\), the sign of \(\det(I_2-G)\) is opposite the sign of \(P(\rho)\). A nonnegative \(\det(I_2-G)\), together with \(G\succeq0\) and \(\det G<1\), forces **both** eigenvalues of \(G\) to lie at most one; their product below one excludes the alternative that both are at least one. At a root of \(P\), one is exactly one and the other is strictly below one. When \(P>0\), \(\det(I_2-G)<0\), forcing one singular value above one. This proves the iff criterion with all boundaries.

**4. Condition numbers, orderings, and small coupling.** The two eigenvalues of \(H_\rho\) yield
\[
\kappa=\begin{cases}
(1+2\rho)/(1-\rho),&\rho>0,\\
(1-\rho)/(1+2\rho),&\rho<0.
\end{cases}
\]
Both branches increase strictly as the magnitude of the correlation grows. Hence the two frontiers follow from the already-proved interval and the distinct eigenvalue denominators. At \(\kappa=6\), the two parameter values are \(5/8\) and \(-5/13\); the exact polynomial values are \(P(5/8)=147/2048>0\) and \(P(-5/13)=-5376/28561<0\). Every change of cyclic order is conjugation of the sweep matrix by a permutation, since \(H_\rho\) is invariant under all permutations; the induced matrices have identical singular values. Finally, the leading \(3\times2\) block after dividing by \(\rho\) has nonzero singular values \(\varphi\) and \(\varphi^{-1}\) as \(\rho\to0\), giving the claimed first-order norm law and its spectral comparison.

## Verification
The accompanying Python 3 standard-library script `artifacts/verify_gs3.py` reconstructs the sweep polynomially, verifies the characteristic trace and determinant, and proves the three Gram identities by exact coefficient arithmetic. It checks the threshold brackets and samples the full parameter range with exact rational data; separate direct coordinate-sweep tests use independent rational vectors and independent update code. A small-coupling limit check verifies the golden-ratio coefficient numerically. Its output is embedded as `artifacts/verification.txt`. These finite tests support the proof but do not establish the all-parameter sign theorem; that theorem rests on the displayed exact polynomial identities, strict convexity, and the Gram-eigenvalue argument.

## Relationship to prior work
The sweep matrix and its complex positive-correlation spectrum **are already explicitly present** in the published three-block symmetric-quadratic momentum analysis [3], with the same \(\rho=c=(1+m)^{-1}\in(0,1)\); neither matrix nor spectral modulus alone is presented as new. That study instead finds the stability boundary of a lifted global-momentum recurrence. The result here concerns the ordinary (zero-momentum) sweep's **Euclidean singular norm**, covers the full positive-definite interval including negative correlations, and gives two sharp correlation-dependent condition-number frontiers.

Kamri–Hendrickx–Glineur [1] analyze worst-case performance estimation of cyclic block coordinate algorithms, using last-iterate objective and gradient measures, rather than giving this exact equicorrelation Euclidean-error phase diagram. Mohlenkamp–Young–Bárány [2] analyze transient block-coordinate dynamics in narrow or flat valleys; their symmetric three-coordinate flat-valley case is singular, corresponding to the boundary \(\rho=-1/2\) after diagonal normalization, not the strict positive-definite family studied here. An earlier published two-coordinate Gauss–Seidel result [4] gives a sharp best-order Euclidean threshold over arbitrary \(2\times2\) SPD systems; it neither implies the three-coordinate Gram determinant nor the two sign-dependent thresholds, and the complex nonzero spectrum is absent in two dimensions. Generic Gauss–Seidel convergence on SPD matrices guarantees an energy reduction, but cannot imply Euclidean one-sweep nonexpansion. Specialized historical linear-iteration literature may contain equivalent unlocated formulas; this is a best-knowledge publication comparison, not a uniqueness certificate.

## Limitations
The classification concerns a symmetric one-parameter family of exactly solved three-coordinate quadratics, not a minimax bound over every \(3\times3\) SPD matrix. Nonexpansion is for full sweeps in the Euclidean error norm; it says nothing about monotonicity at every individual coordinate update in that norm. Positive-definite strict endpoints are excluded, but equality thresholds inside the domain are included. The complex-spectrum and exact-sweep formulas for positive correlation are prior known; the assessed new claim is strictly the complete Euclidean-norm nonexpansion phase with its condition-number asymmetry. No numerical conditioning or finite-precision error guarantee is established.

## References
1. Y. Kamri, J. M. Hendrickx, and F. Glineur, *On the Worst-Case Analysis of Cyclic Coordinate-Wise Algorithms on Smooth Convex Functions*, arXiv:2211.17018, first posted 2022-11-30. https://arxiv.org/abs/2211.17018
2. M. Mohlenkamp, T. R. Young, and B. Bárány, *Transient Dynamics of Block Coordinate Descent in a Valley*, International Journal of Numerical Analysis and Modeling 17 (2020), 557–591. https://doi.org/10.4208/ijnam.v17.n4.p557 ; open text: https://www.math.ualberta.ca/ijnam/Volume-17-2020/No-4-20/2020-04-06.pdf
3. *Three blocks create a sharp momentum-stability barrier for cyclic alternating minimization*, published 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-three-blocks-create-a-sharp-momentum-stability-barrier-for-cycli--ae67f1db4df3
4. *Sharp minimax Euclidean transient bound for two-coordinate Gauss-Seidel ordering*, published 2026. https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-two-coordinate-gauss-seidel-euclidean-transient-threshold--21774554697b
