# Exact pole-order rank classification for coordinate Toeplitz commutators on harmonic Bergman space

## Finding
On the complex harmonic Bergman space \(b^2(\mathbb D)\), let \(R\) be a rational function with no poles in the closed unit disk. For the bounded analytic symbols \(z\) and \(R'\), write the unique partial fraction decomposition
\[
R(z)=P(z)+\sum_{j=1}^{m}\sum_{\ell=1}^{d_j}\frac{a_{j,\ell}}{(1-\lambda_jz)^\ell},
\]
where \(P\) is a polynomial, the \(\lambda_j\) are distinct and satisfy \(0<|\lambda_j|<1\), and \(a_{j,d_j}\ne0\). If \(D=\deg P\), putting \(D=-1\) when \(P=0\), then
\[
\boxed{\operatorname{rank}[T_z,T_{R'}]=2\max\!\left(0,\left\lfloor\frac{D-1}{2}\right\rfloor\right)+2\sum_{j=1}^{m}\left\lceil\frac{d_j}{2}\right\rceil.}
\]
Thus different finite poles contribute additively, and increasing a pole order from an odd number to the next even number leaves the commutator rank unchanged. The commutator has square zero. All ranks refer to complex-linear operator rank.

## Assumptions and scope
The area measure on \(\mathbb D\) is normalized by \(\pi^{-1}\); \(b^2(\mathbb D)\) is the closed subspace of harmonic functions in \(L^2(dA)\), and \(T_f=QM_f\), with \(Q\) the harmonic Bergman projection. The stated decomposition has no constant \(\lambda_j=0\) terms, since those are absorbed in \(P\). The derivative \(R'\) is bounded on \(\mathbb D\), so both Toeplitz operators are bounded. For the zero polynomial contribution \(P=0\), use the stated degree convention; otherwise \(D\) is its true degree. No assumption that the poles have real locations or that their coefficients have the same phase is needed. This is a precise-rank result for coordinate commutators, not a general rank formula for arbitrary analytic Toeplitz symbol pairs.

## Proof
**Step 1: operator entries.** Write \(R(z)=\sum_{k\ge0}r_kz^k\). The mutually orthogonal spanning family of \(b^2\) is \(1,z,z^2,\ldots,\bar z,\bar z^2,\ldots\). For integers \(a,b\ge0\), direct disk integration gives
\[
Q(z^a\bar z^b)=\begin{cases}(a-b+1)z^{a-b}/(a+1),&a\ge b,\\(b-a+1)\bar z^{b-a}/(b+1),&a<b.\end{cases}
\]
Since analytic symbols act by multiplication on the analytic Bergman summand, \(C=[T_z,T_{R'}]\) vanishes on that summand. On input \(\bar z^v\), \(v\ge1\), the coanalytic and constant output components cancel. The coefficient of \(z^u\), \(u\ge1\), is exactly
\[
[C\bar z^v]_{z^u}=\frac{u-v}{v+1}\,r_{u+v}.
\]
The absolute convergence of the rational Taylor series on a neighborhood of the closed disk justifies termwise projection. Multiplying each nonzero column by \(v+1\) does not change rank, so \(\operatorname{rank}C\) equals the algebraic rank of the infinite skew-symmetric matrix
\[
K_{u,v}=(u-v)r_{u+v},\qquad u,v\ge1.
\]
This also shows \(C^2=0\), since its image lies in its analytic-input kernel.

**Step 2: separate polynomial and pole blocks.** The polynomial part contributes the finitely supported block
\(K^{\rm poly}_{u,v}=(u-v)[z^{u+v}]P\), supported where \(u,v\le D-1\). At a pole \(\lambda_j^{-1}\), the coefficients of its partial fractions are \(\lambda_j^k p_j(k)\), with \(p_j\) a polynomial of exact degree \(d_j-1\) and nonzero leading coefficient \(c_j\). The resulting contribution to \(K\) is
\[
\lambda_j^{u+v}(u-v)p_j(u+v).
\]
It factors through the \(d_j+1\) column functions \(u\mapsto u^h\lambda_j^u\), \(0\le h\le d_j\), with a skew-symmetric coefficient matrix \(B_j\). The polynomial block factors through the finitely supported coordinate functions \(u\mapsto\mathbf1_{\{u=h\}}\), \(1\le h\le D-1\).

All these feature functions are linearly independent across distinct nonzero \(\lambda_j\) and the finite-support block. One direct proof applies the finite-difference annihilators \((E-\lambda_j)^{d_j+1}\), where \(E\) is the forward shift, and uses that a nonzero exponential-polynomial cannot have finite support. Equivalently, their generating functions have disjoint pole sets. Therefore the common feature map \(U\) has full column rank, and \(K=U\operatorname{diag}(B_{\rm poly},B_1,\dots,B_m)U^{\mathsf T}\) has rank equal to the sum of the separate coefficient-matrix ranks. Indeed, a left inverse to \(U\) and surjectivity of \(U^{\mathsf T}\) reduce the rank equality to finite-dimensional linear algebra.

**Step 3: individual ranks.** For a pole of order \(d\), the highest-degree contribution is \(c(u-v)(u+v)^{d-1}\), and its coefficient matrix in degrees \(0,\ldots,d\) has zero entries above the anti-diagonal. The anti-diagonal entry in row \(h\) is
\[
c\left(\binom{d-1}{h-1}-\binom{d-1}{h}\right)=c\frac{2h-d}{d}\binom dh,
\]
with endpoint binomial coefficients interpreted as zero where appropriate. Lower-degree terms lie strictly below this anti-diagonal. If \(d\) is odd, all anti-diagonal entries are nonzero, giving rank \(d+1\). If \(d\) is even, the central anti-diagonal entry vanishes; deleting the central row and column produces an invertible anti-triangular \(d\)-by-\(d\) minor. Odd-dimensional skew-symmetry bounds the full rank by \(d\), so the rank is exactly \(d\). In either case it equals \(2\lceil d/2\rceil\).

For a polynomial of degree \(D\ge2\), the \((D-1)\)-by-\((D-1)\) skew block has anti-diagonal entries \((2u-D)r_D\), \(1\le u\le D-1\). If \(D\) is odd, all are nonzero and the rank is \(D-1\); if \(D\) is even, deletion of the central row and column gives a full-rank \((D-2)\)-minor and skew-symmetry gives the matching upper bound. The rank is \(D-2\). Degree at most two gives rank zero. Adding block ranks proves the displayed formula for every permitted rational \(R\).

## Verification
A standalone exact-arithmetic script `verify_rank.py` checks nine explicit rational/polynomial cases with one and two distinct poles, orders one through four, and selected polynomial degrees, against independent Gaussian elimination of finite skew-Hankel sections. It also checks 729 direct monomial projection coefficients for the operator commutator using the projection formula, rather than relying solely on the reduced matrix. Execute `python3 verify_rank.py` using Python 3's standard library. These finite tests do not certify the infinite theorem: independence of exponential-polynomial features and the anti-diagonal minor argument supply its proof.

## Relationship to prior work
Cui, Huang, Lu and Zu (arXiv:2611.08988, version dated 2026-11-06) characterize when harmonic Bergman Toeplitz commutators have finite rank in terms of rational primitives, and calculate a rank-two rational example. Their classification does not provide the order-by-order exact rank formula for arbitrary rational primitives. Dong and Zhou (arXiv:1411.0213) determine ranks for quasihomogeneous symbol families; in the coordinate/monomial subcase their results overlap the polynomial specialization, but their specified families do not contain arbitrary sums of distinct rational poles. Chen, Koo and Lee (2013) establish general rank parity and realizability of every even rank, consistent with but weaker than the pole-additive formula. Classical exponential-polynomial/Hankel recurrences underlie the proof; the decisive new structural statement is the exact skew-block rank and its direct relation to pole multiplicity.

## Limitations
This theorem is limited to rational \(R\) holomorphic beyond the closed disk and to the specific pair \(z,R'\). It makes no claim about full singular values, optimal norms, arbitrary analytic pairs, or rational functions with boundary poles. Bibliographic priority is qualified by possible unindexed equivalent descriptions of skew-Hankel displacement ranks; the accessible older 2013 paper's abstract was inspected but its complete text was not materially available. Independent audit has not been performed.

## References
1. P. Cui, Z. Huang, Y. Lu, C. Zu, *Finite-rank Toeplitz commutators on the harmonic Bergman space*, arXiv:2611.08988v1 (2026-11-06), https://arxiv.org/abs/2611.08988 .
2. X.-T. Dong and Z.-H. Zhou, *Ranks of commutators and generalized semicommutators of quasihomogeneous Toeplitz operators*, arXiv:1411.0213v3, https://arxiv.org/abs/1411.0213 .
3. Y. Chen, H. Koo and Y. J. Lee, *Ranks of commutators of Toeplitz operators on the harmonic Bergman space*, Integral Equations Operator Theory 75 (2013), 31–38, https://doi.org/10.1007/s00020-012-2020-6 .
