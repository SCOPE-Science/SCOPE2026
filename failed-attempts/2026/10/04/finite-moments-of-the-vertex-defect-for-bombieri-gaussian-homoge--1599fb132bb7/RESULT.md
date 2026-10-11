# Finite moments of the vertex defect for Bombieri Gaussian homogeneous polynomials
## Finding
Fix an integer \(m\ge 1\) and a real number \(q\ge 1\). Let \(P_n\) be distributed according to the Bombieri Gaussian measure \(\gamma_{m,n}\) on the real \(m\)-homogeneous polynomials on \(\mathbb R^n\). Define
\[
M(P_n)=\max_{x\in[-1,1]^n}|P_n(x)|,
\qquad
V(P_n)=\max_{\varepsilon\in\{-1,1\}^n}|P_n(\varepsilon)|,
\]
and, outside the null event \(P_n=0\),
\[
Z_n=1-\frac{V(P_n)}{M(P_n)}.
\]
Set \(Z_n=0\) on that null event. Then there is a constant \(C_{m,q}<\infty\), depending only on \(m\) and \(q\), such that for all sufficiently large \(n\),
\[
\|Z_n\|_{L^q(\gamma_{m,n})}\le C_{m,q}n^{-1/2}.
\]
Equivalently,
\[
\mathbb E Z_n^q\le C_{m,q}^q n^{-q/2}.
\]
For \(m=1\), \(Z_n=0\) identically. In particular, for every fixed degree the expected relative vertex loss satisfies
\[
\mathbb E Z_n=O(n^{-1/2}).
\]

## Assumptions and scope
The degree \(m\) and moment exponent \(q\) are fixed while \(n\to\infty\). The Gaussian law is exactly the Bombieri Gaussian law used by Pinasco and Zalduendo. The result concerns the relative defect between the supremum on the cube and the maximum over cube vertices. It does not assert that the vertices attain the exact norm with high probability, and it does not claim a matching lower bound for any moment.

## Proof
Write the Pinasco--Zalduendo decomposition
\[
P_n=Q_n+R_n,
\]
where \(Q_n\) is the square-free multilinear part and \(R_n\) contains every monomial with a repeated variable. Their deterministic comparison gives, outside the null event \(Q_n=0\),
\[
Z_n\le 2\frac{M(R_n)}{M(Q_n)}.
\]
Their lower-bound argument for the multilinear part gives constants \(a_m,b_m>0\), depending only on \(m\), such that
\[
\mathbb P\!\left(M(Q_n)<a_m n^{(m+1)/2}\right)\le e^{-b_m n}
\]
for all sufficiently large \(n\). Indeed, their Sudakov estimate gives \(\mathbb E M(Q_n)\ge A_m n^{(m+1)/2}\), their Lipschitz constant is at most \(n^{m/2}\), and Gaussian concentration at half the mean gives the displayed exponential lower tail.

It remains to upgrade the repeated-variable estimate from boundedness in probability to a fixed-moment estimate. In the source decomposition, for each \(1\le r\le m-1\) and each exponent pattern \(a\) there is an \(r\)-linear Gaussian form whose vertex maximum \(Y_{n,r,a}\) dominates the corresponding block of \(R_n\). The source proves the explicit union-bound tail
\[
\mathbb P(Y_{n,r,a}>t)
\le 2^{rn+1}\exp\!\left(-\frac{t^2}{2c_a^2 n^r}\right).
\]
This is the tail of the maximum of at most \(2^{rn}\) centered Gaussian variables whose variances are at most \(c_a^2n^r\). Integrating the tail, or equivalently applying the standard finite-Gaussian-maximum estimate derived from that union bound, yields for every fixed \(q\ge1\)
\[
\|Y_{n,r,a}\|_{L^q}
\le C_{m,q} n^{(r+1)/2}.
\]
There are only finitely many values of \(r\) and exponent patterns when \(m\) is fixed. Minkowski's inequality and the deterministic domination of each repeated-variable block therefore give
\[
\|M(R_n)\|_{L^q}
\le C_{m,q} n^{m/2},
\]
because the largest exponent \((r+1)/2\) occurs at \(r=m-1\).

Let
\[
G_n=\left\{M(Q_n)\ge a_m n^{(m+1)/2}\right\}.
\]
On \(G_n\), the deterministic comparison and the preceding moment bound imply
\[
\mathbb E\!\left[Z_n^q\mathbf 1_{G_n}\right]
\le C_{m,q} n^{-q(m+1)/2}\mathbb E M(R_n)^q
\le C_{m,q} n^{-q/2}.
\]
Since \(0\le Z_n\le1\), the complement contributes at most
\[
\mathbb E\!\left[Z_n^q\mathbf 1_{G_n^c}\right]
\le \mathbb P(G_n^c)
\le e^{-b_m n},
\]
which is bounded by a constant times \(n^{-q/2}\) for large \(n\). Combining the two estimates proves the claim. For \(m=1\), every polynomial is linear and is normed at a cube vertex, so \(Z_n=0\).

## Verification
The proof uses no finite enumeration or numerical experiment. The nonstandard inputs were checked directly in arXiv:2609.32526v1: the deterministic defect reduction, the exponential lower-tail estimate for the multilinear norm, the block decomposition of the repeated-variable part, and the explicit Gaussian union-bound tail for each multilinearized block. The only added step is tail integration for a finite Gaussian maximum and then Minkowski's inequality across the finitely many blocks. The bound is for each fixed finite \(q\); no uniformity as \(q\to\infty\) is asserted.

## Relationship to prior work
Pinasco and Zalduendo prove
\[
Z_n=O_{\mathbb P}(n^{-1/2}),
\]
which gives tightness of the scaled defect but does not, by itself, imply convergence of expectations or uniform integrability. Their proof contains stronger quantitative ingredients: an exponentially small lower-tail event for \(M(Q_n)\) and explicit sub-Gaussian union bounds for every block of \(R_n\). Integrating those tails yields the finite-moment estimate above. Searches for the same-object statement in terms of expected relative loss, \(L^q\) control, moments of the vertex defect, and Bombieri Gaussian cube maxima did not locate a published or indexed theorem with this conclusion.

Earlier work of Pinasco and Zalduendo studies probabilities of local extrema or related polynomial inequalities, rather than the global cube-versus-vertices relative defect considered here. Thus those results do not imply the displayed moment estimate.

## Limitations
The result is an upper bound only. It does not show that \(n^{1/2}Z_n\) has a nondegenerate limiting law, nor that the order \(n^{-1/2}\) is sharp in expectation. The constants depend on the fixed degree and on the fixed moment exponent. The literature search cannot exclude an equivalent formulation hidden under different Gaussian-process terminology, and the focal preprint is recent.

## References
1. D. Pinasco and I. Zalduendo, *Almost norming vertices for homogeneous polynomials on the cube*, arXiv:2609.32526v1, first public 26 September 2026.
2. D. Pinasco and I. Zalduendo, *A probabilistic approach to polynomial inequalities*, Israel Journal of Mathematics 190 (2012), 283--303, DOI 10.1007/s11856-011-0193-3.
3. D. Pinasco and I. Zalduendo, *On the measure of polynomials attaining maxima on a vertex*, Mathematical Inequalities & Applications 22 (2019), 945--953.
