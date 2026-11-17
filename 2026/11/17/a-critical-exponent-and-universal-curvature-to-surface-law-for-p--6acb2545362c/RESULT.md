# A critical exponent and universal curvature-to-surface law for power lecture-hall simplices

## Finding

For an integer \(n\ge2\) and positive real weights \(s_1,\ldots,s_n\), define the inherited-Euclidean lecture-hall simplex
\[
P_n(s)=\{x\in\mathbb R^n:0\le x_1/s_1\le\cdots\le x_n/s_n\le1\}.
\]
The exact second Steiner intrinsic-volume ratio \(C_n(s)=V_{n-2}(P_n(s))/\operatorname{Vol}_n(P_n(s))\) has an \(O(n)\)-operation formula below. In particular, with the power weights \(s_i=i^p\) for any fixed real \(p\ge0\), write \(C_n(p)=C_n(s)\) and \(A_n(p)=\mathcal H^{n-1}(\partial P_n(s))/\operatorname{Vol}_n(P_n(s))\). Then
\[
C_n(p)\sim
\begin{cases}
\dfrac{n^{4-2p}}{4(1-p)^2},&0\le p<1,\\[3pt]
\dfrac{n^2(\log n)^2}{4},&p=1,\\[3pt]
\mathcal C_p n^2,&p>1,
\end{cases}
\]
where the finite positive constant \(\mathcal C_p\) is given explicitly by an absolutely convergent series below. Moreover, for \(0\le p\le1\),
\[
\lim_{n\to\infty}\frac{C_n(p)}{A_n(p)^2}=\frac18.
\]
For \(p>1\), this limit exists and equals the explicit, generally different parameter-dependent value \(\mathcal C_p/B_p^2\) defined below. This is a transition in a genuine Euclidean Steiner coefficient, not in the Ehrhart polynomial.

## Assumptions and scope

The ambient metric is standard Euclidean \(\mathbb R^n\), with no affine or lattice normalization. Steiner intrinsic volumes are defined by \(\operatorname{Vol}_n(P+tB_n)=\sum_{k=0}^n\kappa_{n-k}V_k(P)t^{n-k}\), where \(B_n\) is the Euclidean unit ball and \(\kappa_j\) its \(j\)-dimensional volume. All weights \(s_i\) are strictly positive. Integer weights give ordinary lattice lecture-hall simplices; real power weights supply a natural continuous geometric interpolation, including the ordinary integer-power examples.

Put \(a_i=s_i^{-1}\). Introduce \(n+1\) numbers
\[
q_1=a_1,\qquad q_i=\sqrt{a_{i-1}^2+a_i^2}\ (2\le i\le n),\qquad q_{n+1}=a_n,
\]
and \(r_i=a_i^2/(q_iq_{i+1})\in(0,1)\) for \(1\le i\le n\). Define
\[
\mathcal L(s)=\frac\pi4\left[\left(\sum_{i=1}^{n+1}q_i\right)^2-\sum_{i=1}^{n+1}q_i^2\right]
+\sum_{i=1}^{n}q_iq_{i+1}\left[\sqrt{1-r_i^2}\left(\frac\pi2+\arcsin r_i\right)-\frac\pi2\right].
\]
Then the exact formulas are
\[
C_n(s)=\frac{n(n-1)}{2\pi}\mathcal L(s),\qquad
\frac{\mathcal H^{n-1}(\partial P_n(s))}{\operatorname{Vol}_n(P_n(s))}=n\sum_{i=1}^{n+1}q_i.
\]
For \(p>1\), set \(b_1=1\), \(b_i=\sqrt{(i-1)^{-2p}+i^{-2p}}\) for \(i\ge2\), \(\rho_i=i^{-2p}/(b_i b_{i+1})\), and \(B_p=\sum_{i=1}^{\infty}b_i\). The positive convergent series defining the limiting constant is
\[
\mathcal C_p=\frac{1}{2\pi}\left\{\frac\pi2\sum_{1\le i<j<\infty}b_i b_j
+\sum_{i=1}^{\infty} b_i b_{i+1}\left[\sqrt{1-\rho_i^2}\left(\frac\pi2+\arcsin\rho_i\right)-\frac\pi2\right]\right\}.
\]
All formulas hold without assuming distinct weights or an integer exponent.

## Proof

**1. Vertices, facet gradients and volume.** The vertices are \(v_0=0\) and \(v_j=(0,\ldots,0,s_j,\ldots,s_n)\) for \(1\le j\le n\). The edge matrix \([v_1\ \cdots\ v_n]\) is triangular with determinant \(\prod_i s_i\), so \(\operatorname{Vol}_n(P_n(s))=\prod_i s_i/n!\). In the normalized coordinates \(z_i=x_i/s_i\), the nonnegative barycentric coordinates, arranged in chain order, are \(z_1,z_2-z_1,\ldots,z_n-z_{n-1},1-z_n\). Denote their gradients by \(u_1,\ldots,u_{n+1}\), so
\[
u_1=a_1e_1,\quad u_i=a_ie_i-a_{i-1}e_{i-1}\ (2\le i\le n),\quad u_{n+1}=-a_ne_n.
\]
Consequently \(\|u_i\|=q_i\), \(u_i\cdot u_{i+1}=-a_i^2\), and all other distinct pairs of gradients are orthogonal. Standard facet-height volume identities give facet measure \(\operatorname{Vol}_n(P_n(s))\,nq_i\), proving the surface formula.

**2. Every ridge and its exterior angle.** The ridge \(F_i\cap F_j\), opposite barycentric vertices \(i,j\), has \((n-2)\)-measure
\[
\mathcal H^{n-2}(F_i\cap F_j)
=\frac{\prod_{k=1}^n s_k}{(n-2)!}
\sqrt{q_i^2q_j^2-(u_i\cdot u_j)^2}.
\]
This follows directly from the Gram determinant of the remaining \(n-1\) vertices, or equivalently the complementary-minor identity for the inverse edge matrix. The exterior angle is \(\arccos[(u_i\cdot u_j)/(q_iq_j)]\): it equals \(\pi/2\) for nonadjacent facet labels, and \(\pi/2+\arcsin r_i\) for adjacent labels \(j=i+1\). Because the second Steiner coefficient \(\pi V_{n-2}\) equals one half the sum of ridge measures times their exterior angles, summing the right-angle baseline and replacing exactly the \(n\) adjacent terms yields \(\mathcal L(s)\) and the exact expression for \(C_n(s)\). The formula also covers \(n=2\), with zero-dimensional ridge measures equal to one.

**3. Divergent harmonic regime.** For fixed \(p\ge0\) and \(s_i=i^p\), the chain-gradient lengths satisfy \(q_i\sim\sqrt2\,i^{-p}\) as \(i\to\infty\), apart from the two harmless endpoint terms. Write \(S_n=\sum_{i=1}^{n+1}q_i\). For \(0\le p\le1\), \(S_n\to\infty\) and \(\sum_iq_i^2=o(S_n^2)\). The entire adjacent correction is bounded in magnitude by a universal constant times \(\sum_iq_iq_{i+1}\le\sum_iq_i^2\), since \(0<r_i<1\) and the bracketed function is bounded. Thus
\[
\mathcal L(s)=\frac\pi4 S_n^2(1+o(1)),\quad
C_n(p)=\frac{n^2}{8}S_n^2(1+o(1)).
\]
The power-sum estimates give \(S_n\sim\sqrt2\,n^{1-p}/(1-p)\) for \(p<1\), and \(S_n\sim\sqrt2\log n\) for \(p=1\). Substitution proves the first two branches. Since \(A_n(p)=nS_n\) exactly, the universal ratio tends to \(1/8\).

**4. Summable harmonic regime.** For fixed \(p>1\), the sequence of left-hand chain-gradient lengths converges termwise to \(b_i\), and \(\sum_i b_i<\infty\). The terminal extra length \(q_{n+1}=n^{-p}\) vanishes; the bounded adjacent-angle correction and the right-angle pair sum are dominated by a constant times \(\sum_{i<j}b_i b_j+\sum_i b_i^2\). Dominated convergence gives \(\mathcal L(s)\to2\pi\mathcal C_p\) and \(S_n\to B_p\), hence \(C_n(p)\sim\mathcal C_p n^2\) and \(C_n(p)/A_n(p)^2\to\mathcal C_p/B_p^2\). The limit is strictly positive because at least one nonadjacent facet pair has positive ridge measure and exterior angle \(\pi/2\); every summand in the original exterior-angle expression is nonnegative. Absolute convergence follows from \(\sum_i b_i<\infty\).

## Verification

The included `CHECK.py` uses Python standard-library exact rational Gaussian elimination to compute the barycentric-gradient Gram matrix and every ridge Gram determinant directly from the vertices. It checks 60 independently generated integer-weight profiles in dimensions 2–6 and all 660 pairs of opposite facets. It separately reproduces the previously published \(n=3\), equal-leg intrinsic volume \(V_1=1+1/\sqrt2+1/\sqrt3\), checks the \(n=2\) normalization, and evaluates the three asymptotic regimes numerically through dimension 10,000. Run `python3 CHECK.py`. These finite checks are corroboration; the proof above is unrestricted.

## Relationship to prior work

Olsen's 2018 survey defines the exact lecture-hall simplex and summarizes its Ehrhart, Gorenstein, triangulation and related algebraic invariants. Brändén–Solus (2019) develop algebraic properties of the same family, not metric Steiner coefficients. The older Gao–Vitale theorem (2000) computes all intrinsic volumes for the equal-leg orthoscheme, corresponding precisely to \(p=0\), so this known special case is **not claimed as new**. The present contribution is the exact weighted-ridge expression combined with the full power-weight asymptotic classification and universal curvature-to-surface limit. The existing covariance-spectrum work for power lecture-hall simplices concerns a different measure (uniform on the vertices), and does not determine the boundary curvature coefficient considered here.

## Limitations

This is a self-review, not independent validation. Literature comparisons are best-knowledge and do not prove absolute historical priority. The real-power interpolation is not a lattice polytope for general noninteger powers. The result concerns only the second intrinsic-volume coefficient and surface area; no asymptotic assertion is made for other Steiner coefficients. For \(p>1\), the constant is defined by an absolutely convergent explicit series, not an asserted elementary closed form.

## References

1. McCabe Olsen, *Polyhedral Geometry for Lecture Hall Partitions*, arXiv:1808.06131, first public version 2018-08-18. https://arxiv.org/abs/1808.06131
2. Petter Brändén and Liam Solus, *Some Algebraic Properties of Lecture Hall Polytopes*, arXiv:1911.12459, first public version 2019-11-27. https://arxiv.org/abs/1911.12459
3. Fuchang Gao and Richard A. Vitale, *Intrinsic Volumes of the Brownian Motion Body*, arXiv:math/0011052, first public version 2000-11-08, especially Theorem 2 for the equal-leg orthoscheme. https://arxiv.org/abs/math/0011052
