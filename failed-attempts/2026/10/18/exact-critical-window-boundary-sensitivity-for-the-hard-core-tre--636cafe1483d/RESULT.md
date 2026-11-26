# Exact critical-window boundary sensitivity for the hard-core tree shift

## Finding

Fix an integer branching number \(b\ge 2\). Let \(\mathcal T_{b,n}\) be the rooted complete \(b\)-ary tree whose vertices have depths \(0,\ldots,n\). Give each labeling \(\omega:V\to\{0,1\}\) with \(\omega(u)\omega(v)=0\) for every edge \(uv\) probability proportional to \(\lambda^{\sum_v\omega(v)}\). Let \(p_n^{\mathrm F}(\lambda)\) be the occupied-root probability when leaves are unrestricted, and \(p_n^{\mathrm E}(\lambda)\) the occupied-root probability when all depth-\(n\) vertices are fixed empty. Define
\[
\lambda_c=\frac{b^b}{(b-1)^{b+1}},\qquad
\lambda_n(t)=\lambda_c\left(1+\frac{t}{n}\right),\qquad a_b=\frac{b-1}{b}.
\]
For every real \(t\) and every integer \(b\ge2\),
\[
\boxed{\lim_{n\to\infty}(-1)^n\sqrt n\left[p_n^{\mathrm F}(\lambda_n(t))-p_n^{\mathrm E}(\lambda_n(t))\right]
=\frac{2\sqrt{6(b-1)}}{b\sqrt{b+1}}
\sqrt{\frac{a_b t}{1-e^{-a_b t}}}.}
\]
The square-root factor is defined to be \(1\) at \(t=0\); it is positive for every real \(t\). The convergence is uniform when \(t\) ranges over any fixed compact subset of \(\mathbb R\). In particular, precisely at the infinite-tree uniqueness threshold, the difference alternates by parity and has sharp magnitude
\[
\left|p_n^{\mathrm F}(\lambda_c)-p_n^{\mathrm E}(\lambda_c)\right|
\sim \frac{2\sqrt{6(b-1)}}{b\sqrt{b+1}}\,n^{-1/2}.
\]

## Assumptions and scope

The branching number \(b\) is a fixed integer \(\ge2\) as \(n\to\infty\). Heights count edges from the root; a height-zero tree has one vertex. Free and empty-leaf conditions are imposed on the same height-\(n\) vertex set, including its leaves. The parameter \(t\) is real, independent of \(n\), and \(\lambda_n(t)>0\) once \(n>\max\{0,-t\}\). Occupation probabilities refer to the finite-volume Gibbs distribution, not an arbitrary infinite-volume Gibbs state. At \(t=0\) both boundary prescriptions have the same infinite-volume limit, yet their leading finite-height discrepancy is nonzero.

## Proof

**1. Exact finite-tree recursion.** Let \(Z_h^{(j)}\) be the partition sum of an admissible height-\(h\) subtree with its root fixed to \(j\in\{0,1\}\). For a subtree with unconstrained leaves, \(Z_0^{(0)}=1\), \(Z_0^{(1)}=\lambda\); for an empty-leaf subtree, \(Z_0^{(0)}=1\), \(Z_0^{(1)}=0\). For \(h\ge1\), independence of the \(b\) subtrees yields
\[
Z_h^{(0)}=(Z_{h-1}^{(0)}+Z_{h-1}^{(1)})^b,
\qquad Z_h^{(1)}=\lambda(Z_{h-1}^{(0)})^b.
\]
Thus, writing \(r_h=Z_h^{(1)}/Z_h^{(0)}\), the exact recursion and observable are
\[
F_\lambda(r)=\frac{\lambda}{(1+r)^b},\qquad
r_n^{\mathrm F}=F_\lambda^n(\lambda),\qquad
r_n^{\mathrm E}=F_\lambda^n(0),\qquad
p_n=\sigma(r_n),\quad \sigma(r)=\frac r{1+r}.
\]
Here \(F_\lambda^n\) denotes the \(n\)-fold iterate, with \(F_\lambda^0\) the identity.

**2. Critical flip and cubic normal form.** The strictly increasing map \(r\mapsto r(1+r)^b\) gives a unique positive fixed point \(r_*(\lambda)\), analytic near \(\lambda_c\). At \(\lambda_c\), \(r_c=1/(b-1)\) and \(F_{\lambda_c}'(r_c)=-1\). Put \(\delta=\lambda/\lambda_c-1\) and
\[
G_\delta(x)=F_\lambda^2\big(r_*(\lambda)+x\big)-r_*(\lambda).
\]
Direct differentiation at \(r_c\) gives
\[
F''_{\lambda_c}(r_c)=\frac{(b+1)(b-1)}b,
\qquad F'''_{\lambda_c}(r_c)=-\frac{(b+1)(b+2)(b-1)^2}{b^2}.
\]
If \(A=F''_{\lambda_c}(r_c)/2\) and \(B=F'''_{\lambda_c}(r_c)/6\), composition of \(-x+Ax^2+Bx^3+O(x^4)\) with itself gives \(x-2(A^2+B)x^3+O(x^4)\). Hence
\[
C_b=2(A^2+B)=\frac{(b+1)(b-1)^3}{6b^2}>0.
\]
Moreover \(\frac{d}{d\delta}r_*(\lambda_c(1+\delta))\big|_{\delta=0}=1/[2(b-1)]\), so
\[
\frac{d}{d\delta}\big(F'_\lambda(r_*(\lambda))^2\big)\Big|_{\delta=0}=\frac{b-1}{b}=a_b.
\]
Analyticity and the cancellation of the quadratic coefficient of \(G_0\) therefore give, uniformly for \(\delta,x\) near zero,
\[
G_\delta(x)=\left(1+a_b\delta+O(\delta^2)\right)x
+O(\delta)x^2-C_bx^3+O(\delta x^3+x^4).
\tag{1}
\]

**3. Attraction into the critical neighborhood.** The critical two-step map \(F_{\lambda_c}^2\) is strictly increasing and has \(r_c\) as its sole nonnegative fixed point (the classical uniqueness condition at the critical hard-core tree activity). It sends every initial point from \([0,\lambda_c]\) monotonically toward \(r_c\) along its two-step subsequence. For completeness, the absence of a distinct two-cycle follows from the standard hard-core tree uniqueness inequality: if \(u<v\) form a two-cycle, the strict flip threshold \(\lambda>\lambda_c\) is necessary (see Galvin--Martinelli--Ramanan--Tetali, Section 2.2). At equality no such pair exists. Since \(F_\lambda^2\) depends continuously on \(\lambda\), for each sufficiently small neighborhood of \(r_c\), both initial points \(0\) and \(\lambda\) enter that neighborhood after a fixed even number of iterations, uniformly for \(\delta\to0\). By \(F_\lambda^2\) increasing, they remain respectively below and above \(r_*(\lambda)\). From (1), choosing the neighborhood small and \(|\delta|\) small also makes it forward invariant during all subsequent iterates up to height \(n\). No centered orbit crosses zero.

**4. Critical-window inverse-square limit.** Now set \(\delta=t/n\), with \(t\) ranging over a fixed compact set, and let \(x_j^\pm\) be the centered ratios after \(2j\) updates, with \(+\) for initially free leaves and \(-\) for initially empty leaves. Once in the common small neighborhood from step 3, the signs remain fixed. Define \(w_j^\pm=(x_j^\pm)^{-2}>0\). Expanding (1) in inverse squares yields
\[
w_{j+1}^\pm=\left(1-\frac{2a_bt}{n}+O(n^{-2})\right)w_j^\pm+2C_b+
O\left(|x_j^\pm|+\frac{1}{n|x_j^\pm|}+\frac{1}{n}+\frac{w_j^\pm}{n^2}\right).
\tag{2}
\]
All implied constants can be fixed uniformly on compact \(t\)-sets and for the chosen \(b\). The local expansion first bounds \(w_{j+1}\) between \((1-O(1/n))w_j+c\) and \((1+O(1/n))w_j+C\) with constants \(c,C>0\) after the fixed entry time. Discrete comparison implies
\[
c'(j+1)\le w_j^\pm\le C'(j+1),\qquad j\le\lfloor n/2\rfloor,
\]
with \(c',C'>0\) uniform in \(n\) and compact \(t\)-sets. Consequently the sum of the error terms in (2), through \(j\le n/2\), is \(O(\sqrt n)\), while the multiplier perturbation \(O(n^{-2})w_j\) contributes only \(O(1)\). The initial finite number of steps contributes \(O(1)\). Thus the difference between \(w_{\lfloor n/2\rfloor}^\pm/n\) and the solution to the linear recursion
\[
u_{j+1}=\left(1-\frac{2a_bt}{n}\right)u_j+2C_b,\qquad u_0=O(1),
\]
vanishes uniformly. Summing the geometric progression gives
\[
\frac{w_{\lfloor n/2\rfloor}^\pm}{n}\longrightarrow
C_b\frac{1-e^{-a_bt}}{a_bt},
\tag{3}
\]
with limit \(C_b\) at \(t=0\). Indeed, there are asymptotically \(n/2\) two-step updates, whence the exponential factor \(e^{-a_bt}\). The positive limit yields
\[
\sqrt n\,x_{\lfloor n/2\rfloor}^{\pm}\longrightarrow
\pm\sqrt{\frac{a_bt}{C_b(1-e^{-a_bt})}}.
\tag{4}
\]
For odd \(n\), applying one further update multiplies each centered displacement by \(-1+o(1)\); the same amplitude and opposite parity follow. Since \(\sigma'(r_c)=(b-1)^2/b^2\), (4) and the mean-value theorem show the scaled root-probability difference is
\[
2\frac{(b-1)^2}{b^2}\sqrt{\frac{a_bt}{C_b(1-e^{-a_bt})}},
\]
which simplifies to the displayed formula. All comparisons were uniform on compact \(t\)-sets, establishing local uniformity. \(\square\)

## Verification

Run `python verify.py` with Python 3.10 or later. The supplied stand-alone program uses exact rational enumeration of all independent sets in 42 small finite trees to corroborate the two boundary partition recurrences; independently checks 10 exact cubic normal-form coefficient identities and compares 48 large finite-height ratios against the limiting scaling function for four arities and three critical-window positions, checking both even and odd heights. The observed maximum relative discrepancy in this sample is approximately \(0.001228\). The proof, not those finite calculations, establishes the infinite-limit statement.

## Relationship to prior work

The tree hard-core model, its root-message recurrence, the uniqueness threshold \(\lambda_c\), and critical flip behavior are classical. Galvin, Martinelli, Ramanan and Tetali (2011; earlier preprint 2010) derive the tree recursion and phase transition. Ban and Chang (2015) study nonlinear tree-shift block-count recurrences and effects of boundary conditions on tree-shift entropy. Efthymiou and collaborators (2016) analyze message passing and correlation decay in the strictly subcritical uniqueness region. The present claim is the explicitly normalized, locally uniform **finite-height critical-window boundary-response profile** at \(\lambda=\lambda_c(1+t/n)\), simultaneously for all integer arities, including the exact amplitude at criticality. It is not a new derivation of the classical uniqueness threshold, a statement about entropy itself, or a subcritical exponential correlation-decay theorem. Known general analytic parabolic/flip normal-form techniques underlie the method and may provide independent routes to the same profile.

## Limitations

The asymptotic fixes \(b\) and scales the activity with height \(n\). It compares only two specific homogeneous boundary conditions (unrestricted leaves versus leaves fixed empty); it does not give the maximal influence of arbitrary leaf configurations or mixing-time results. The profile makes no claim about finite-height errors uniform as \(|t|\to\infty\) or simultaneous growth of \(b\). Priority relative to unindexed or inaccessible critical-tree calculations remains unresolved and requires independent assessment.

## References

1. J.-C. Ban and C.-H. Chang, *Tree-Shifts: The entropy of tree-shifts of finite type*, arXiv:1509.08325v1 (public 2015-09-28), particularly nonlinear recurrences and boundary-entropy comparisons.
2. D. Galvin, F. Martinelli, K. Ramanan and P. Tetali, *The multi-state hard core model on a regular tree*, arXiv:1007.4806 (public 2010-07-27), *SIAM Journal on Discrete Mathematics* **25** (2011), 894–915, doi:10.1137/09075514X. See Section 2.2 for the capacity-one uniqueness threshold.
3. C. Efthymiou, T. P. Hayes, D. Stefankovic, E. Vigoda and Y. Yin, *Convergence of MCMC and Loopy BP in the Tree Uniqueness Region for the Hard-Core Model*, arXiv:1604.01422v1 (public 2016-04-05); the strict uniqueness-region analysis.
