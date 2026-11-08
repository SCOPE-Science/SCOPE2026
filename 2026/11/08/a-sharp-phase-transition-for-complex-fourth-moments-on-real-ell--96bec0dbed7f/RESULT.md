# A sharp phase transition for complex fourth moments on real \(\ell_p\) balls

## Finding

Let \(n\ge2\), \(1\le p\le\infty\), and let \(X\) be uniform with respect to normalized real volume on the unit ball \(B_p^n=\{x\in\mathbb R^n:\sum_j |x_j|^p\le1\}\) (the cube \([-1,1]^n\) when \(p=\infty\)). For \(0\ne z\in\mathbb C^n\), put \(f_z(x)=\sum_jz_jx_j\) and
\[
K_{n,p}(z)=\frac{\mathbb E|f_z(X)|^4}{(\mathbb E|f_z(X)|^2)^2}.
\]
For finite \(p\), define
\[
H_{n,p}=\frac{\Gamma(1+(n+2)/p)^2}{\Gamma(1+n/p)\Gamma(1+(n+4)/p)},\qquad
R_p=\frac{\Gamma(5/p)\Gamma(1/p)}{\Gamma(3/p)^2},\qquad d_p=R_p-3.
\]
For \(p=\infty\), set \(H_{n,\infty}=1\), \(R_\infty=9/5\), \(d_\infty=-6/5\). The complete sharp interval of \(K_{n,p}\) is
\[
\begin{array}{c|c|c}
\text{range}&K_{\min}&K_{\max}\\\hline
1\le p<2&H_{n,p}(2+d_p/n)&H_{n,p}(3+d_p)=H_{n,p}R_p\\
p=2&2H_{n,2}&3H_{n,2}\\
2<p\le\infty&H_{n,p}(2+d_p/2)&H_{n,p}(3+d_p/n).
\end{array}
\]
All bounds are attained, and the image of \(K_{n,p}\) is the entire stated interval.

All equality classes are as follows (global nonzero complex scaling is immaterial).

* For \(p<2\), **minimizers** satisfy equal nonzero coefficient moduli and \(\sum_j z_j^2=0\); **maximizers** have exactly one nonzero coefficient.
* For \(p=2\), **minimizers** satisfy \(\sum_j z_j^2=0\); **maximizers** satisfy \(|\sum_jz_j^2|=\sum_j|z_j|^2\), meaning all nonzero coefficient squares share a common phase.
* For \(p>2\), **minimizers** have exactly two nonzero, equal-modulus coefficients with relative phase \(\pi/2\) modulo \(\pi\); **maximizers** have equal nonzero moduli in every coordinate and all coefficient squares share a phase.

Let \(E_{n,p}\subset L^4(B_p^n;\mathbb C)\) be the complex-linear space of these coordinate functionals. Its **complex-linear multiplicative Banach--Mazur distance** to complex Euclidean space is exactly
\[
d_{\mathrm{BM}}(E_{n,p},\ell_2^n(\mathbb C))^4=\frac{K_{\max}}{K_{\min}}
=\begin{cases}
\displaystyle\frac{R_p}{2+(R_p-3)/n},&1\le p<2,\\[4pt]
\displaystyle\frac32,&p=2,\\[4pt]
\displaystyle\frac{3+(R_p-3)/n}{2+(R_p-3)/2},&2<p\le\infty.
\end{cases}
\]
For instance, in dimension \(n=2\) the diamond \(p=1\) and square \(p=\infty\) both have sharp moment range \([7/5,12/5]\) and fourth-power Euclidean distortion \(12/7\), whereas the disk \(p=2\) has range \([4/3,2]\) and distortion fourth power \(3/2\). These values follow from the formulas and are not separate assumptions.

The natural coefficient Euclidean norm is optimal, including among all non-diagonal Hermitian inner products. Thus the minimizing coefficient geometry changes sharply at \(p=2\): for \(p<2\), minimum requires support in all coordinates, whereas for \(p>2\), it requires exactly two quadrature-phase coordinates.

## Assumptions and scope

All balls are **real** coordinate balls; coefficients are complex and the function norm uses the absolute value of the complex output. The measure is normalized real Lebesgue volume, not complex ball volume, cone measure, or boundary measure. The exponent of the function norm is always four; \(p\) controls the domain's shape. Norms and Banach--Mazur distance are over \(\mathbb C\). The statement includes \(n=2\), both closed endpoints \(p=1,\infty\), and the transition \(p=2\).

## Proof

**1. Exact moments.** For finite \(p\), change variables \(y_j=|x_j|^p\) on every orthant. Dirichlet integration gives, for even nonnegative coordinate powers \(q_j\),
\[
\mathbb E\prod_j |X_j|^{q_j}
=\frac{\Gamma(1+n/p)}{\Gamma(1+(n+\sum_jq_j)/p)}
\prod_j\frac{\Gamma((q_j+1)/p)}{\Gamma(1/p)}.
\]
Let \(\alpha=\mathbb E X_1^2\), \(\beta=\mathbb E X_1^4\), \(\gamma=\mathbb E X_1^2X_2^2\). All odd-coordinate moments vanish, since independent sign changes preserve the measure. The formula gives \(\gamma/\alpha^2=H_{n,p}\) and \(\beta/\gamma=R_p\). For the cube, independent coordinates have \((\alpha,\beta,\gamma)=(1/3,1/5,1/9)\), giving the stated limits.

Set
\[
S=\sum_j|z_j|^2>0,\quad T=\sum_j|z_j|^4,\quad Q=\sum_jz_j^2.
\]
Expand \(\left|\sum_j z_jX_j\right|^4\) and retain only even coordinate exponents. Pairing the four factors yields
\[
\mathbb E|f_z|^2=\alpha S,\qquad
\mathbb E|f_z|^4=\gamma(2S^2+|Q|^2)+(\beta-3\gamma)T.
\]
Consequently,
\[
\boxed{\ K_{n,p}(z)/H_{n,p}=2+\frac{|Q|^2}{S^2}+d_p\frac{T}{S^2}.\ }
\tag{1}
\]
This identity holds also for the cube.

**2. Shape parameter and its exact transition.** Write \(x=1/p>0\) and \(R(x)=\Gamma(5x)\Gamma(x)/\Gamma(3x)^2\). The standard convergent digamma series yields
\[
\frac{d}{dx}\log R(x)
=5\psi(5x)+\psi(x)-6\psi(3x)
=\sum_{k=1}^{\infty}\frac{8kx}{(k+x)(k+3x)(k+5x)}>0.
\]
Since \(R(1/2)=3\) and \(\lim_{x\downarrow0}R(x)=9/5\), the parameter \(d_p\) is positive for \(p<2\), zero at \(p=2\), and lies strictly between \(-6/5\) and zero for finite \(p>2\) (equals \(-6/5\) at infinity). In particular, whenever \(p>2\), write \(d=-d_p\), so \(0<d\le6/5<2\).

**3. Exact nonnegative endpoint deficits.** The inequalities \(S^2/n\le T\le S^2\) and \(0\le|Q|^2\le S^2\) follow from Cauchy--Schwarz and the triangle inequality. For \(p<2\), equation (1) gives **both** exact deficits:
\[
\frac{K-K_{\min}}H=\frac{|Q|^2}{S^2}+d_p\frac{T-S^2/n}{S^2},\quad
\frac{K_{\max}-K}H=\frac{S^2-|Q|^2}{S^2}+d_p\frac{S^2-T}{S^2}.
\]
Here and below \(H=H_{n,p}\). Each numerator term is nonnegative. The first vanishes exactly when \(|z_j|\) are all equal and \(Q=0\); the second exactly for one-coordinate support. Equal moduli and \(Q=0\) are achievable, for instance, by \(z_j=\exp(\pi i(j-1)/n)\).

For \(p>2\), put \(d=-d_p\). Another exact identity is
\[
|Q|^2+S^2-2T
=4\sum_{i<j}\bigl(\operatorname{Re}(z_i\overline z_j)\bigr)^2\ge0.
\tag{2}
\]
Using (1) and (2) yields **both** endpoint deficits:
\[
\frac{K-K_{\min}}H
=\left(1-\frac d2\right)\frac{|Q|^2}{S^2}
+\frac{2d}{S^2}\sum_{i<j}\bigl(\operatorname{Re}(z_i\overline z_j)\bigr)^2,
\]
\[
\frac{K_{\max}-K}H
=\frac{S^2-|Q|^2}{S^2}+d\frac{T-S^2/n}{S^2}.
\]
All terms are nonnegative. Equality in the first identity forces \(Q=0\) and pairwise real-orthogonality of distinct nonzero complex coefficients, regarded as vectors in \(\mathbb R^2\). There can be at most two such coefficients; \(Q=0\) rules out just one and forces equal magnitude and quadrature phase for the two. In the upper identity equality demands all moduli equal and all nonzero coefficient squares aligned. At \(p=2\), (1) reduces to \(K/H=2+|Q|^2/S^2\), with the stated equality conditions. The unit sphere of \(\mathbb C^n\) is connected and \(K\) continuous, so all intermediate values occur.

**4. Exact optimal Euclidean geometry.** The signed-permutation group acts complex-linearly and isometrically on \(E_{n,p}\). For any positive-definite Hermitian quadratic form \(J\), a candidate Hilbert comparison is characterized by optimal constants \(0<a\le b\) with \(aJ(z)\le\|f_z\|_4^2\le bJ(z)\) for all \(z\). Average \(J\) over all coordinate sign changes and permutations. The inequalities persist with the same \(a,b\); the average must be \(cS\), since signs eliminate off-diagonal terms and permutations equalize diagonal entries. Hence no candidate beats the standard Euclidean form. Since \(\|f_z\|_2^2=\alpha S\), the ratio of maximal to minimal \(\|f_z\|_4^4/S^2\) equals \(K_{\max}/K_{\min}\), proving the displayed Banach--Mazur formula.

## Verification

The accompanying `verify.py` independently expands fourth-order coordinate monomials with exact rational arithmetic for \(p=1,2,\infty\), dimensions \(2\) through \(7\), and 65 coefficient arrays in each case. It verifies both endpoint deficits exactly, independently checks (2), checks the gamma parameter regimes numerically, and samples from the exact Dirichlet/gamma ball representation for five noninteger cases. The exact computation and samples support the algebra; the infinite-parameter assertions are proved above, not inferred from finite tests.

## Relationship to prior work

Barthe, Guédon, Mendelson and Naor (arXiv:math/0503650, first verified public posting March 29, 2005), §2 and in particular §2.2, give a probabilistic description of the real \(\ell_p\) ball and moment comparisons for **real** linear functionals. Their integration machinery supplies foundational moment information, but their stated coefficient space is \(\mathbb R^n\), and the inspected section does not provide the complex phase-sensitive sharp endpoints, two-coordinate quadrature minimizers above \(p=2\), or the complex-linear optimal Banach--Mazur distance here. The exact fourth moment is elementary once the mixed-coordinate integrals are known; the new content claimed is the global complex optimization, equality and stability for all \(n,p\), and optimal Hilbert geometry, not discovery of the Dirichlet integral.

Known sharp complex zero-sum \(\ell_4\) hyperplane norm calculations and complex centered-simplex norm calculations concern different coefficient constraints and different measures; their statements do not imply (1) or the \(p=2\) transition. Classical complex Rademacher Khintchine inequalities concern a product distribution and therefore do not determine the finite-volume gamma factor \(H_{n,p}\). This is a best-knowledge literature comparison rather than a proof of historical uniqueness.

## Limitations

Only degree-one complex coefficient functionals, fourth moments, and real \(\ell_p\) ball volume are addressed. No result is claimed for general nonuniform unconditional measures, higher-degree functions, higher moments, or complex \(\ell_p\) balls. The gamma moment formulas are established here directly; prior literature already supplies them for real coefficients. The published bibliography may contain equivalent descriptions under different terminology, and no independent mathematical audit has been carried out.

## References

1. F. Barthe, O. Guédon, S. Mendelson and A. Naor, *A probabilistic approach to the geometry of the \(\ell_p^n\)-ball*, arXiv:math/0503650 (first verified public posting 2005-03-29); *Annals of Probability* **33** (2005), 480–513. https://arxiv.org/abs/math/0503650 ; open author PDF https://web.math.princeton.edu/~naor/homepage%20files/LPBALL.pdf . Specifically §2.2, including Lemma 6 (p. 10) and Theorem 7 (p. 13).
2. R. M. G. Young, *On the Best Possible Constants in the Khintchine Inequality*, *Journal of the London Mathematical Society* **s2-14** (1976), 496–504. https://doi.org/10.1112/jlms/s2-14.3.496 . Context for sharp moment comparisons; not used as a proof of the complex result.
