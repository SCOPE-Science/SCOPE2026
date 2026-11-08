# Exact first-order symmetry breaking for the \(\ell_2\)-to-\(\ell_q\) six-cycle incidence norm

## Finding

Let \(A=J_3-I_3\), the \(3\times3\) incidence matrix of the six-cycle viewed as a bipartite graph, and use the **unnormalized counting-measure** \(\ell_q\) norms on \(\mathbb C^3\). Put
\[
q_*=\frac{\log 4}{\log(4/3)}=4.818841679306418\ldots,
\qquad N_q=\|A:\ell_2^3\to\ell_q^3\|.
\]
For every finite \(2\le q<\infty\), the complete exact one-variable reduction is
\[
N_q^q=\max_{t\ge0}\frac{2^q+2(1+t)^q}{(2+t^2)^{q/2}}.
\tag{1}
\]
Here the displayed maximum is attained at finite \(t>0\). The sharp symmetry-breaking transition is
\[
N_q=2\,3^{1/q-1/2}\quad(2\le q\le q_*),
\qquad N_q>2\,3^{1/q-1/2}\quad(q>q_*).
\tag{2}
\]
For \(2\le q<q_*\), the only unit extremizers are the constant-modulus vectors \(e^{i\theta}(1,1,1)/\sqrt3\). At \(q=q_*\), precisely two permutation/phase orbits attain the norm:
\[
e^{i\theta}(1,1,1)/\sqrt3
\quad\text{and}\quad
e^{i\theta}(1,2,2)/3.
\tag{3}
\]
For \(q>q_*\), every extremizer is nonuniform and (after permutation and multiplication by a unit scalar) has the form \((t,1,1)/\sqrt{t^2+2}\) for a positive maximizer of (1). No uniqueness of this positive maximizer is asserted. Finally, \(N_\infty=\sqrt2\), with extremizers supported on the two neighbors of one output vertex, of equal modulus and phase. Thus the extremizing input has a discontinuous symmetry change at the exact transcendental exponent \(q_*\), rather than becoming asymmetric by a perturbation of the uniform input.

## Assumptions and scope

The matrix has zeros on the diagonal and ones off the diagonal. The left and right vertex sets each have three elements, and the associated bipartite graph is connected, two-regular, and edge-transitive. Scalars may be real or complex; the theorem is for arbitrary complex input vectors. \(\ell_q\) norms are defined by \(\|x\|_q=(\sum_{j=1}^3|x_j|^q)^{1/q}\) with the usual \(\ell_\infty\) convention. The graph-to-shape correspondence in the initiating literature uses its own entropy and operator-norm normalizations; we claim exact counting-measure matrix norms here, not an unverified normalized shape formula.

## Proof

**1. Positivity, interiority, and a two-level reduction.** Since all matrix entries are nonnegative, \(|Ax|\le A|x|\) coordinatewise. A norm maximizer can therefore be chosen nonnegative. It must in fact have all three entries strictly positive. At a nonnegative unit vector with one zero entry, adding a small positive amount at that position changes its Euclidean norm only to second order, but increases at least one nonzero output of \(A\) to first order. Thus the \(\ell_q\) output strictly increases for every finite \(q\ge2\). For \(q=2\), \(A^2=I_3+J_3\) proves \(N_2=2\) and forces the uniform vector.

Fix \(q>2\), and let a positive maximizer be \(x=(x_1,x_2,x_3)\) with \(\|x\|_2=1\). Write \(S=\sum x_i\), \(y_i=S-x_i>0\), and \(F(x)=\sum_i y_i^q\). The Lagrange equations imply, for any two unequal entries,
\[
\frac{\mu}{q}=
\frac{y_j^{q-1}-y_i^{q-1}}{y_j-y_i},
\tag{4}
\]
where \(\mu\) is a common multiplier. If all three entries of \(x\) were distinct, the three values \(y_i\) would also be distinct, but strict convexity of \(y\mapsto y^{q-1}\) makes the secant slopes across successive intervals strictly unequal. This contradicts (4). Therefore at least two coordinates coincide. Every maximizer is, up to permutation, \((t,1,1)/\sqrt{t^2+2}\), and applying \(A\) gives (1). Complex equality requires the phases in each pairwise sum to agree. Since all three input moduli are positive, all phases must agree, proving the stated phase rigidity.

**2. Two exact endpoint comparisons.** Define
\[
f_q(t)=\frac{2^q+2(1+t)^q}{(2+t^2)^{q/2}},
\qquad R_q(t)=\frac{f_q(t)}{f_q(1)}.
\]
At \(q=2\) and \(q=4\), respectively, direct polynomial identities give
\[
4(t^2+2)-\bigl(4+2(1+t)^2\bigr)=2(t-1)^2,
\]
\[
\frac{16}{3}(t^2+2)^2-\bigl(16+2(1+t)^4\bigr)
=\frac23(t-1)^2(5t^2-2t+5).
\tag{5}
\]
Both are strictly positive for \(t\ne1\). This also proves that the uniform vector is the unique maximizing orbit at these two exponents.

**3. Exact transition at \(q_*\).** Differentiating \(f_q\), its derivative has the sign of
\[
h_q(t)=(2-t)\bigl((1+t)/2\bigr)^{q-1}-t.
\tag{6}
\]
For \(t\ge2\), this is negative. On \(1<t<2\), a nonuniform critical point would require
\[
q=1+\frac{\log(t/(2-t))}{\log((1+t)/2)}.
\]
Writing \(u=t-1\in(0,1)\), the quotient is \(2\operatorname{artanh}(u)/\log(1+u/2)>4\), since \(\operatorname{artanh}u>u\) and \(\log(1+u/2)<u/2\). Hence \(f_{q_*}\) strictly decreases for \(t>1\), because \(q_*<5\).

For \(0<t<1\) set \(u=1-t\) and
\[
Q(u)=1+\frac{2\operatorname{artanh}u}{-\log(1-u/2)}.
\tag{7}
\]
Then \(h_{q_*}(t)=0\) precisely when \(Q(u)=q_*\). We verify rigorously that \(Q\) decreases once and then increases once as \(u\) runs from zero to one. Set \(B(u)=-\log(1-u/2)\) and
\[
H(u)=(2-u)B(u)-(1-u^2)\operatorname{artanh}u.
\]
The derivative \(Q'(u)\) has the sign of \(H(u)\). Direct differentiation gives
\[
H'(u)=G(u):=\log(1-u/2)+2u\operatorname{artanh}u,
\]
\[
G''(u)=-\frac{1}{(2-u)^2}+\frac{2}{1-u^2}
+\frac{2(1+u^2)}{(1-u^2)^2}>0.
\tag{8}
\]
Also \(G(0)=0\), \(G'(0)=-1/2\), and \(G(u)\to+\infty\) as \(u\uparrow1\). Therefore \(G\) has precisely one zero in \((0,1)\), and \(H\), which starts at zero, initially decreases and then strictly increases. Since \(H(1-)=\log2>0\), it crosses zero exactly once. This proves the asserted unique minimum of \(Q\). Furthermore,
\[
H(1/2)=\frac38\log(256/243)>0,
\qquad Q(1/2)=1+\frac{\log3}{\log(4/3)}=q_*<5=Q(0+).
\tag{9}
\]
Consequently the equation \(Q(u)=q_*\) has exactly two roots: \(u=1/2\), on the increasing side, and one root in \((0,1/2)\), on the decreasing side. Formula (6) shows that \(f_{q_*}\) rises to \(t=1/2\), falls to the other nonuniform critical point, rises to \(t=1\), and falls for \(t>1\). Hence its only possible global maxima are \(t=1/2\) and \(t=1\).

They have equal value **exactly**, without numerical approximation. Indeed, as \((4/3)^{q_*}=4\),
\[
R_{q_*}(1/2)=\frac{1+2(3/4)^{q_*}}{3}
\left(\frac43\right)^{q_*/2}
=\frac{1+1/2}{3}\cdot2=1.
\tag{10}
\]
This proves the equality classification (3) and the sharp formula at the transition.

**4. All exponents and the discontinuous switch.** For fixed \(t\ne1\), \(\log R_q(t)\) is strictly convex in \(q\): it is a log-sum-exp of two unequal positive output values minus an affine function of \(q\). By (5), \(R_2(t)<1\), and by step 3, \(R_{q_*}(t)\le1\) for every \(t\ge0\). Strict log-convexity yields \(R_q(t)<1\) whenever \(2<q<q_*\); the endpoint \(q=2\) was already settled. For \(q>q_*\), use the explicit nonuniform test vector \(t=1/2\). Writing \(r=(4/3)^{q/2}>2\), we have
\[
R_q(1/2)=\frac{r+2/r}{3}>1.
\tag{11}
\]
Thus every norm maximizer must be nonuniform above \(q_*\), whereas at \(q_*\) the optimizer \((1,2,2)/3\) remains a positive distance from the uniform orbit: this is first-order symmetry breaking, not an infinitesimal bifurcation. Finally, the \(\ell_2\to\ell_\infty\) norm is the Euclidean norm of the largest row, \(\sqrt2\), by Cauchy–Schwarz, with the stated equality class. The monotone finite-dimensional \(\ell_q\)-to-\(\ell_\infty\) limit completes the proof.

## Verification

The standalone Python verifier `verify.py` uses exact rational arithmetic to check the two polynomial identities in (5) at 81 rational inputs each, and tests the critical exponent equations, the candidate equality, and 4,193 further numerical profile inequalities at specified finite grids. It returns `EXACT_C6_CHECK_OK 4366`. These finite checks are corroboration of the formulas, **not** an exhaustive proof of (1)–(11). The infinite and continuum claims are proved in the displayed analytical argument.

To reproduce: run `python verify.py` with a standard Python 3 interpreter from a directory containing the accompanying source file.

## Relationship to prior work

Matveev's 2026 theorem identifies the shape function of a uniformly supported homogeneous bipartite graph with an incidence-matrix Lebesgue operator norm. The six-cycle is the smallest non-complete connected homogeneous bipartite graph, and (1)–(11) evaluate an entire non-Hilbert exponent line for its incidence matrix. That identification alone does not provide the sharp transition or its two equality orbits. Matveev and Romashchenko introduced the shape-function framework and related spectral estimates; those do not evaluate this exact norm line. General finite matrix Perron–Frobenius and Hölder results recover only particular exponents, not the transition. Published searches for triangle/crown/six-cycle induced norms, relevant mathematical records, and the directly accessible initiating manuscript revealed no implication covering this sharp coefficient. Publication priority is not independently certified.

## Limitations

The theorem treats the one-parameter exponent line with Euclidean input and output exponent at least two, and does not give a closed elementary expression for the nonuniform optimizer at arbitrary \(q>q_*\). A one-variable *maximization* in (1) is exact but is not presented as a unique optimizer classification for those exponents. The graph-to-shape correspondence involves separate normalization and is not itself recomputed here. Literature coverage cannot exclude an older equivalent formula under different terminology; independent mathematical verification is pending.

## References

1. R. Matveev, *Shapes and Norms of Random Pairs*, arXiv:2608.08039v1, publicly submitted August 8, 2026; accessible full text at https://arxiv.org/abs/2608.08039 .
2. R. Matveev and A. Romashchenko, *Beyond Mutual Information: Extension Profiles and Shape Functions of Random Variable Pairs*, arXiv:2606.23849v1, publicly submitted June 22, 2026, https://arxiv.org/abs/2606.23849 .
