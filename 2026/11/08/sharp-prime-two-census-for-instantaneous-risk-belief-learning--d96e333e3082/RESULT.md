# Sharp prime-two census for instantaneous risk-belief learning

## Finding

For the risk-sensitive multiplicative-weights map with instantaneous belief adjustment, the complete set of **primitive interior period-two orbits** consists of either zero or exactly one orbit. The exact phase boundary depends only on an effective feedback strength and the interior equilibrium:

\[
 m=\frac{b-cp_0}{1+cp_1},\qquad r=cp_1,\qquad
 a_{\mathrm{flip}}=\frac{2}{m(1-m)(1-r)}.
\]

If \(m\notin(0,1)\), or \(r\ge1\), no such orbit exists, for any learning aggressiveness \(a>0\). For \(0<m<1\) and \(0\le r<1\), exactly one exists if and only if \(a>a_{\mathrm{flip}}\). In particular there is **no nontrivial period-two orbit at equality**. The orbit has exactly the form

\[
 (m+d,p_0+p_1(m-d))\longleftrightarrow
 (m-d,p_0+p_1(m+d)),
\]

where \(d\in(0,\min\{m,1-m\})\) is the unique root of

\[
 \frac{\operatorname{logit}(m+d)-\operatorname{logit}(m-d)}{d}=a(1-r),
 \qquad \operatorname{logit}(x)=\log\frac{x}{1-x}.
\]

The emergence is continuous and obeys the sharp square-root amplitude law as \(a\downarrow a_{\mathrm{flip}}\) from above,

\[
 d^2=\frac{3(1-r)}{2m^{-3}+2(1-m)^{-3}}
 (a-a_{\mathrm{flip}})+O((a-a_{\mathrm{flip}})^2).
\]

At the equilibrium the multiplier \(-1\) occurs precisely at this threshold; the other multiplier is \(-2r/(1-r)\). For \(0\le r<1/3\), the emerging unique cycle is linearly attracting for all sufficiently small positive \(a-a_{\mathrm{flip}}\). For \(1/3<r<1\) it is **not** linearly attracting immediately above the threshold. The borderline \(r=1/3\) is not assigned a stability type by this assertion.

## Assumptions and scope

The map is

\[
 F(x,q)=\left(\frac{x}{x+(1-x)\exp(a(x-b+cq))},\quad p_0+p_1x\right).
\]

Assume \(a>0\), \(c>0\), \(0<b<1\), \(p_0,p_1\ge0\), and \(p_0+p_1\le1\). Its domain is the population strip \(x\in(0,1)\), \(q\in[0,1]\). The second coordinate is the \(k=1\) endpoint of the original adaptive rule \(q'=(1-k)q+k(p_0+p_1x)\), which permits \(0<k\le1\). The word period-two denotes a **least-period-two orbit in the entire two-dimensional state**, not merely oscillations of its first coordinate. The boundary points \(x=0\) and \(x=1\), if included, cannot lie on a nonconstant period-two orbit because their first coordinates remain fixed and their belief coordinates become constant after one update.

## Proof

**Step 1: the exact two-cycle constraint.** Write \(L(x)=\operatorname{logit}(x)\). A single update satisfies

\[
 L(x')-L(x)=-a(x-b+cq).
\]

On a two-cycle, the instantaneous update enforces \(q_0=p_0+p_1x_1\) and \(q_1=p_0+p_1x_0\). Adding the two log-odds increments gives

\[
 0=-a\bigl[(1+r)(x_0+x_1)-2(b-cp_0)\bigr].
\]

Thus \(x_0+x_1=2m\). If \(x_0=x_1\), both beliefs are equal and the state is fixed. Every nonconstant orbit may therefore be written, up to phase rotation, with \(x_0=m+d\), \(x_1=m-d\), and \(0<d<d_{\max}=\min\{m,1-m\}\). The log-odds equation for the first step becomes

\[
 L(m+d)-L(m-d)=a(1-r)d.
\]

Conversely, a root of this equation gives both log-odds steps (the sum is zero by construction), and the displayed beliefs satisfy both belief updates, so it gives an actual two-cycle. If \(m\notin(0,1)\) the required positive arithmetic mean is impossible.

**Step 2: strict monotonicity and completeness.** For \(0<m<1\), define

\[
 H_m(d)=\frac{L(m+d)-L(m-d)}d
 =\int_{-1}^{1}L'(m+td)\,dt.
\]

Here \(L'(x)=1/[x(1-x)]\) and \(L'''(x)=2/x^3+2/(1-x)^3>0\). Differentiating gives

\[
 H_m'(d)=\int_0^1 t\bigl[L''(m+td)-L''(m-td)\bigr]dt>0.
\]

It increases continuously from \(H_m(0+)=2/[m(1-m)]\) to infinity as \(d\uparrow d_{\max}\). Consequently \(H_m(d)=a(1-r)\) has one root precisely when \(r<1\) and \(a(1-r)>2/[m(1-m)]\), and none otherwise. No other primitive two-cycle is possible. The equality is excluded because monotonicity is strict for \(d>0\).

**Step 3: amplitude and local stability.** Taylor expansion, with \(s=m(1-m)\), yields

\[
 H_m(d)=\frac2s+\frac{L'''(m)}3d^2+O(d^4).
\]

Inversion proves the stated amplitude expansion. At the equilibrium, with \(r=cp_1\), the Jacobian is

\[
 J_*=\begin{pmatrix}1-as&-acs\\p_1&0\end{pmatrix},\quad
 \chi_*(\lambda)=\lambda^2-(1-as)\lambda+ars.
\]

Its \(-1\) multiplier condition is \(2-as(1-r)=0\), and the other eigenvalue at that threshold is \(-2r/(1-r)\). For the nontrivial cycle, denote \(s_+=(m+d)(1-m-d)\) and \(s_-=(m-d)(1-m+d)\). The two-step Jacobian has exact trace and determinant

\[
 T=1-a(1+r)(s_++s_-)+a^2s_+s_-,\qquad
 D=a^2r^2s_+s_-.
\]

An exact identity gives

\[
 1-T+D=a(1+r)s_+s_-\left(\frac1{s_+}+\frac1{s_-}-a(1-r)\right)>0.
\]

The strict inequality follows from strict convexity of \(L'\) and the trapezoidal integral inequality
\(H_m(d)<L'(m+d)+L'(m-d)\). At the birth point the two-step multipliers tend to \(1\) and \((2r/(1-r))^2\). When \(r<1/3\), continuity gives \(D<1\) and \(1+T+D>0\) for small \(d>0\), while the identity ensures \(1-T+D>0\). The strict planar Schur inequalities prove attraction. When \(r>1/3\), \(D>1\) for small \(d>0\), preventing both multipliers from lying strictly inside the unit disk. No claim is made at the double-critical \(r=1/3\).

## Verification

A fully explicit admissible example is \(b=3/5\), \(c=2\), \(p_0=1/20\), \(p_1=1/10\), \(a=15\log 2\), with \(m=5/12\), \(r=1/5\). Direct rational substitution gives the exact orbit

\[
 (1/2,1/12)\longleftrightarrow(1/3,1/10).
\]

The logarithmic learning rate is above the sharp threshold \(a_{\mathrm{flip}}=72/7\). In this example \(s_+=1/4\) and \(s_-=2/9\); direct substitution yields \(T=1-17a/30+a^2/18\) and \(D=a^2/450\), whose three strict Schur inequalities hold. The checker establishes these inequalities with a rational enclosure of \(\log2\) from the positive series \(\log2=2\sum_{j\ge0}3^{-(2j+1)}/(2j+1)\), not solely from floating point. The standalone \(\texttt{verification/check.py}\) script verifies the exact arithmetic identities, symbolic Floquet formulas, numerical reconstructed cycles over 491 admissible parameter samples, the explicit attracting example, and the square-root onset. Run using Python 3 with SymPy installed.

## Relationship to prior work

Metaxas and Sapsis (2026, arXiv:2606.29967), equations (5) and (9), introduce this two-dimensional risk-perception learning map and allow the \(k=1\) endpoint. Their Proposition 1 already establishes the Cesàro mean \(m\) of interior trajectories, so the two-cycle mean constraint is not new. Their bifurcation plots describe period-two branches and several resonance mechanisms for sampled interior parameter values, but the checked analysis does not furnish a complete exact interior primitive-two-cycle count and threshold at \(k=1\). The present exact classification specializes to this natural, maximal-response boundary; it is not a classification for \(k<1\). Chotibut, Falniowski, Misiurewicz and Piliouras (2018, arXiv:1807.06831) analyze the memory-free, one-dimensional multiplicative-weights map, including its special symmetric period-two branch, which is not claimed as new. The positive endogenous belief-feedback parameter \(r>0\), and particularly the absolute no-two-cycle regime \(r\ge1\) together with the \(r=1/3\) stability split, are features of the present lagged two-dimensional map.

## Limitations

The theorem is restricted to exactly instantaneous updating \(k=1\) and genuine period-two states. It gives no classification of longer cycles, chaotic sets, global basins, or nonperiodic trajectories. The local-attraction assertion is only near the period-two birth and only for \(r<1/3\); no stability classification is claimed at \(r=1/3\) or at arbitrary large \(a\). Priority is provisional, subject to comparison with later revisions and possibly unindexed prior studies. The software checks are finite corroborations, not independent proof or certification.

## References

1. K. Metaxas and T. P. Sapsis, *Risk-Sensitive Learning in Population Games under Extreme Events: Bifurcations and Chaotic Dynamics*, arXiv:2606.29967 (first posted 2026-06-29), https://arxiv.org/abs/2606.29967 .
2. T. Chotibut, F. Falniowski, M. Misiurewicz, and G. Piliouras, *Family of chaotic maps from game theory*, arXiv:1807.06831 (first posted 2018-07-18), https://arxiv.org/abs/1807.06831 .
