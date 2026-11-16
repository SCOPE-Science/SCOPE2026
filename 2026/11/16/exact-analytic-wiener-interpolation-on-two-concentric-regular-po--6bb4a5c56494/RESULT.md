# Exact analytic-Wiener interpolation on two concentric regular polygons

## Finding

Let \(n\ge1\) be an integer and \(0<u<v<1\). Define two full regular \(n\)-gons in the open unit disk by
\[
W_{n;u,v}=\{z:z^n=u\}\cup\{z:z^n=v\}.
\]
In the analytic Wiener algebra \(\ell_A^1=\{f(z)=\sum_{j\ge0}a_jz^j:\sum_{j\ge0}|a_j|<\infty\}\), set
\[
\mathcal A_n(u,v)=\min_{f(0)=1,\ f|_{W_{n;u,v}}=0}\sum_{j\ge0}|a_j|.
\]
For every integer \(k\ge2\), put
\[
D_k=uv^k-vu^k,\qquad P_k=\frac{v^k-u^k}{D_k},\qquad Q_k=\frac{v-u}{D_k},\qquad L_k=P_k+Q_k.
\]
All denominators and \(P_k,Q_k\) are strictly positive. Then
\[
\boxed{\mathcal A_n(u,v)=1+\min_{k\ge2} L_k}.
\]
If the minimizing index is uniquely \(k\), the **unique** norm minimizer is
\[
\boxed{f(z)=1-P_kz^n+Q_kz^{nk}}.
\]
The minimizing indices form either one integer or two consecutive integers. In the two-index case \(\{k,k+1\}\), **all** norm minimizers are precisely the convex combinations of the two displayed trinomials.

The first phase is explicit: the unique minimizing index is \(2\) when \(u+v+uv<1\); exactly \(2,3\) tie at \(u+v+uv=1\); and the optimal index is at least \(3\) when \(u+v+uv>1\). For a fixed \(u\in(0,1)\), as \(v\uparrow1\), the optimal index satisfies
\[
k=\frac{\log(1/(1-v))}{\log(1/u)}+O_u(1),\qquad \mathcal A_n(u,v)\longrightarrow\frac2u.
\]
Thus the sparsity *degree* of the sharp interpolant diverges logarithmically as the outer polygon approaches the boundary, even though the minimal norm remains finite.

## Assumptions and scope

The zero constraints prescribe vanishing **at least** at every node of the two polygons. The result does not assert that a minimizer has no additional zeros. The parameters are real with \(0<u<v<1\), and no restriction is placed on additional Taylor terms or complex coefficient phases. The norm is the unweighted sum of coefficient moduli, and the constant coefficient is exactly one. No finite-degree restriction is imposed. The integer \(n\) controls the polygon cardinality but not the optimal norm. The terminology “unique” includes arbitrary complex-valued competitors, not only real or rotationally invariant ones.

## Proof

**1. Reduction to one variable and rigidity of the reduction.** Write \(\omega=e^{2\pi i/n}\). The cyclic average
\[
\widetilde f(z)=\frac1n\sum_{s=0}^{n-1}f(\omega^sz)=\sum_{j\ge0}a_{nj}z^{nj}
\]
has the same constant coefficient and vanishes at every member of \(W_{n;u,v}\), because rotation permutes each polygon. Its coefficient norm equals \(\sum_{j\ge0}|a_{nj}|\), never exceeding that of \(f\). If a minimizer had any coefficient outside degrees divisible by \(n\), its average would have strictly smaller norm. Thus **every** minimizer is of the form \(F(z^n)\), where \(F(t)=1+\sum_{j\ge1}c_jt^j\), \(F(u)=F(v)=0\). This identifies both the minimum and every minimizer with the two-point problem.

**2. Feasible trinomials.** Since \(D_k>0\), direct substitution verifies that
\[
F_k(t)=1-P_kt+Q_kt^k
\]
vanishes at both \(u,v\), and its coefficient norm is \(1+L_k\). As \(k\to\infty\), \(L_k\to+\infty\), so some integer \(k\ge2\) minimizes \(L_k\).

**3. A sharp all-degree dual certificate.** Fix such a minimizing integer \(k\), and set
\[
\lambda=-\frac{v^k+v}{D_k},\qquad
\mu=\frac{u^k+u}{D_k},\qquad h_j=\lambda u^j+\mu v^j\quad(j\ge1).
\]
By construction, \(h_1=-1\), \(h_k=1\), and \(-\lambda-\mu=L_k\). For any integer \(j\ge2\), apply the two interpolation equalities for \(F_j\) to obtain
\[
L_k=P_j+Q_jh_j.
\]
Since \(L_j=P_j+Q_j\ge L_k\) and \(Q_j>0\), it follows that \(h_j\le1\) for every \(j\ge2\).

It remains to establish the opposite inequality, including **every** untested Taylor degree. On real \(t\ge1\), write \(h(t)=-A u^t+B v^t\) for \(A=-\lambda>0\), \(B=\mu>0\). The derivative
\[
h'(t)=A\log(1/u)u^t-B\log(1/v)v^t
\]
changes sign at most once, from positive to negative, because the ratio of its positive summand to the absolute value of its negative summand decreases strictly with \(t\). Since \(h(1)=-1<h(k)=1\), the derivative is positive somewhere between these two points. Consequently \(h\) first increases, then decreases toward \(0\) as \(t\to\infty\); in particular \(h(t)\ge-1\) for all \(t\ge1\), with equality only at \(t=1\). Combining the bounds yields \(|h_j|\le1\) for every integer \(j\ge1\).

For any admissible \(F=1+\sum_{j\ge1}c_jt^j\), absolute convergence and \(F(u)=F(v)=0\) give
\[
\sum_{j\ge1}c_jh_j
=\lambda\sum_{j\ge1}c_ju^j+\mu\sum_{j\ge1}c_jv^j
=-\lambda-\mu=L_k.
\]
Thus \(\sum_{j\ge1}|c_j|\ge L_k\), with equality for \(F_k\). This proves the exact norm formula against **all** complex analytic-Wiener competitors.

**4. Complete equality classification.** Equality in the displayed dual inequality requires every nonzero \(c_j\) to align with the real certificate: \(c_1\le0\), and for \(j\ge2\) a nonzero coefficient can occur only when \(h_j=1\), in which case \(c_j\ge0\). The strict rise-and-fall shape of \(h(t)\) implies that if \(h_j=h_l=1\) for integers \(2\le j<l\), then necessarily \(l=j+1\) (otherwise the integer between them would have \(h>1\)). Since \(L_k=P_j+Q_jh_j\), the equality \(h_j=1\) holds precisely for minimizing indices \(j\). With only one such index, the two vanishing equations uniquely determine \(F_k\). With two adjacent indices, the nonnegative feasible coefficient cone cut by the two vanishing equations is the line segment joining \(F_k\) and \(F_{k+1}\). This proves the assertion for *all* minimizers, including complex ones.

**5. The phase transition and the boundary limit.** To show global one-valley behavior of the objective, interpolate \(k\) by a real variable \(t>1\). Set \(r=u/v\), \(d=v-u\), \(\eta=\log v/\log r>0\), and \(x=r^t\). Then
\[
L(t)=\frac{1-x+d x^{-\eta}}{u-vx}.
\]
The derivative with respect to \(x\) has the sign of
\[
G(x)=x^{\eta+1}+(1+\eta)vx-\eta u.
\]
On \(0<x<r\), the function \(G\) is strictly increasing, \(G(0^+)<0\), and \(G(r)>0\). Thus \(L(t)\) decreases to one minimum and then increases. It follows that its minimizing integers are one or two consecutive integers. Straight algebra yields
\[
L_2-L_3=\frac{u+v+uv-1}{uv(u+v)},
\]
which, together with one-valley behavior, proves the three cases at the first transition.

Finally, with \(u\) fixed and \(v\uparrow1\), put \(\alpha=\log(1/u)\), \(\beta=\log(1/v)\), so \(\eta=\beta/(\alpha-\beta)\). The unique stationary root satisfies \(x_*\sim u\eta/2\) as \(\eta\downarrow0\), by the defining equation \(G(x_*)=0\). Hence the continuous minimizing exponent is \(t_*=\log x_*/\log(u/v)=\log(1/\beta)/\alpha+O_u(1)\), and any minimizing integer differs from \(t_*\) by less than one, apart from the trivial endpoint clipping to \(2\). Since \(\beta\sim1-v\), the asserted logarithmic law follows. Moreover \(u^{k}\to0\), \(v^{k}\to1\), so \(P_k\to1/u\), \(Q_k\to(1-u)/u\), and \(1+L_k\to2/u\). The proof is complete.

## Verification

The standalone `CHECK.py` uses exact rational arithmetic for 45 distinct pairs of radii, checks the two interpolation identities for every candidate index, constructs the dual certificate and checks its finite initial segment of 64 indices, tests the exact first-transition identity, verifies a nontrivial tie at \((u,v)=(1/5,2/3)\), and exhibits a high-degree optimum at \((u,v)=(4/5,9/10)\), where the minimizing index is \(9\). Execute with `python3 CHECK.py` from this directory. No optional dependencies are needed. The analytic all-degree certificate and one-valley proof, not the finite checks, establish the infinite-degree result.

## Relationship to prior work

Abakumov, Chalendar and Poltoratski (2026, arXiv:2611.02159v1, §§1.3, 3.1, 4) introduced a sharp general moment duality for analytic coefficient norms and analyzed zero sets built from infinitely many regular polygons. Their general identity \(\min\|f-1\|_1=\delta_\infty(W)^{-1}\) provides context but does not evaluate the two-shell two-radius infimum, determine its sparse minimizers, or identify the discrete index transitions. The present result explicitly solves that finite-node extremal problem and constructs a supporting dual certificate. Cheng, Mashreghi and Ross (2018, arXiv:1802.04646v2, §§5–7) studied general zero-set extremal problems in \(\ell_A^p\), chiefly for \(1<p<\infty\); their displayed results do not supply this sharp endpoint two-radius classification. No assertion is made about complete historical priority beyond the sources materially inspected.

## Limitations

This is the analytic-Wiener endpoint \(p=1\), not an all-\(p\) theorem. The two polygons have the same number of vertices and aligned positive radial powers. Unaligned or unequal-cardinality rings are not classified. The vanishing constraints need not be the *exact* zero set of the minimizer. Numerical checks are finite illustrations; they do not certify claims for arbitrary real radii or unbounded Taylor degrees. Independent mathematical verification and an exhaustive historical search have not been performed. In particular, a classical infinite-dimensional linear-programming formulation may hide an equivalent special-case result under different terminology.

## References

1. E. Abakumov, I. Chalendar, A. Poltoratski, *Zero sets in spaces of analytic functions with p-summable Taylor coefficients*, arXiv:2611.02159v1 (public 2026-11-01), https://arxiv.org/html/2611.02159v1 . Specifically §§1.3, 3.1, 4, 8.
2. R. Cheng, J. Mashreghi, W. T. Ross, *Inner functions and zero sets for ℓ_A^p*, arXiv:1802.04646v2 (2018), https://arxiv.org/html/1802.04646v2 . Specifically §§5–7.
