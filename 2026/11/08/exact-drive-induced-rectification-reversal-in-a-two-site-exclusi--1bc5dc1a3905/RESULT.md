# Exact drive-induced rectification reversal in a two-site exclusion channel

## Finding
Consider a two-site, open, continuous-time hard-core exclusion process with positive site-departure rates \(u\ne v\), positive internal-to-contact hopping factor \(d\), and two particle reservoirs of densities \(\ell=(1+\delta)/2\), \(r=(1-\delta)/2\), where \(-1<\delta<1\). Reservoir insertion rates are \(\ell,r\); reservoir removal rates are respectively \(u(1-\ell),v(1-r)\); the sole internal edge has hopping rates \(du\) from left to right and \(dv\) from right to left. Write \(J(\delta)\) for its stationary left-to-right particle current, and \(E(\delta)=J(\delta)+J(-\delta)\) for its even (rectifying) part.

Put \(h=u-v\) and
\[
H=(u+v+2)^2+4d(uv-1).
\]
For every \(0<\delta<1\), the sign of the exact, finite-driving rectification is
\[
\boxed{\operatorname{sgn}E(\delta)=\operatorname{sgn}\bigl(h[H-\delta^2h^2]\bigr),}
\]
with zero precisely when the displayed product vanishes. In particular, if \(uv\ge1\) there is no reversal: \(\operatorname{sgn}E(\delta)=\operatorname{sgn}(u-v)\) for every positive bias. For \(uv<1\), define two **distinct, sharp** kinetic thresholds
\[
d_1=\frac{(u+1)(v+1)}{1-uv},\qquad
d_0=\frac{(u+v+2)^2}{4(1-uv)},\qquad d_1<d_0.
\]
If \(d\le d_1\), the sign is \(\operatorname{sgn}(u-v)\) for all \(0<\delta<1\); if \(d\ge d_0\), it is \(-\operatorname{sgn}(u-v)\) for all such biases. Precisely for \(d_1<d<d_0\), there is one **drive-induced rectification inversion**, at
\[
\boxed{\delta_* = \frac{\sqrt{(u+v+2)^2+4d(uv-1)}}{|u-v|}\in(0,1),}
\]
with the original sign below \(\delta_*\), zero at \(\delta_*\), and reversed sign above it. At \(d=d_0\), the leading even response is quartic rather than quadratic.

For the rational example \(u=1/2\), \(v=3/2\), \(d=63/4\), one has \(d_1=15\), \(d_0=16\), and **exactly** \(\delta_*=1/2\). Thus the very same asymmetric channel has opposite rectification signs at biases \(\delta=1/4\) and \(\delta=3/4\).

## Assumptions and scope
Each occupation is \(0\) or \(1\). The states, in order, are \((0,0),(1,0),(0,1),(1,1)\). A jump is allowed only when its destination is vacant. All three kinetic parameters \(u,v,d\) are strictly positive, and reservoir densities lie strictly between zero and one. The geometric rates are time-homogeneous, with \(d\) controlling the kinetic scale of internal exchanges relative to contacts; no external directional field acts on a bond. At equal reservoir densities, the stationary measure is reversible with single-site occupation odds \(1/u\) and \(1/v\). The conclusion concerns stationary mean current, not current fluctuations or thermodynamic-limit transport.

## Proof
Let \(\ell=(1+\delta)/2\), \(r=(1-\delta)/2\). The generator, acting on row probability vectors from the right, is
\[
Q=\begin{pmatrix}
-\ell-r&\ell&r&0\\
u(1-\ell)&-u(1-\ell)-r-du&du&r\\
v(1-r)&dv&-v(1-r)-\ell-dv&\ell\\
0&v(1-r)&u(1-\ell)&-v(1-r)-u(1-\ell)
\end{pmatrix}.
\]
Every permitted edge has positive rate for \(|\delta|<1\), and this four-state directed graph is strongly connected. For each index \(i\) let \(T_i\) be the principal cofactor of \(-Q\) obtained by deleting row and column \(i\). The finite-state matrix-tree theorem gives the unique stationary weight \(\pi_i=T_i/T\), where \(T=\sum_iT_i>0\). The internal current is \(J=d(u\pi_{10}-v\pi_{01})\).

Introduce \(p=u+v\), \(q=uv\), \(h=u-v\). Direct expansion of the four \(3\)-by-\(3\) cofactors gives the following **polynomial identities**, which can also be checked coefficient by coefficient from the displayed generator:
\[
8T=D(\delta),\qquad
2d(uT_{10}-vT_{01})=duv\delta(p+2-\delta h),
\]
where
\[
\begin{aligned}
D(\delta)={}&(u+1)(v+1)(4dp+p+2)\\
&-\delta h\,[4d(q+p-1)+q+3p+5]\\
&+\delta^2[3p^2-pq-10q+p-2]\\
&+\delta^3h(q-p+1).
\end{aligned}
\]
Consequently
\[
\boxed{J(\delta)=\frac{4duv\delta(p+2-\delta h)}{D(\delta)}.}
\]
Positivity of \(D(\delta)\) is not a guess about the displayed polynomial: it follows from \(D=8T\) and positivity of the rooted-tree sums. Replacing \(\delta\) by \(-\delta\), adding the two rational currents, and expanding the numerator yields the exact identity
\[
\boxed{
E(\delta)=\frac{16duv\delta^2h\{(p+2)^2+4d(q-1)-\delta^2h^2\}}{D(\delta)D(-\delta)}.}
\]
The denominator is strictly positive, hence the asserted sign formula follows without any perturbative approximation.

If \(q\ge1\), then \(H\ge(p+2)^2>h^2\) for positive \(u,v\), so no sign change is possible. If \(q<1\), \(H\) decreases strictly as \(d\) grows. The equation \(H=h^2\) gives \(d=d_1\), because \((p+2)^2-h^2=4(u+1)(v+1)\). The equation \(H=0\) gives \(d=d_0\). Their difference is \(d_0-d_1=h^2/[4(1-q)]>0\). Therefore \(0<H<h^2\) holds exactly for \(d_1<d<d_0\), producing precisely one \(\delta_*\) in \((0,1)\). The endpoint thresholds have the claimed constant signs on this open interval. This proves the complete classification.

Finally, with \(D_0=(u+1)(v+1)(4dp+p+2)>0\), the quadratic even coefficient of \(J\) is
\[
c_2=\frac{8duvhH}{D_0^2}.
\]
At \(d=d_0\), \(H=0\) and the first nonzero even coefficient is
\[
c_4=-\frac{8duvh^3}{D_0^2}\ne0.
\]
The critical response is therefore genuinely quartic. For the stated rational example, \(q=3/4\), \(p=2\), \(h=-1\), \(H=1/4\), so the inversion bias is exactly \(1/2\).

## Verification
The standalone \`verify.py\` constructs the displayed generator, computes all four exact directed-tree cofactors symbolically, and checks the two cofactor identities, the full rational factorization of \(E\), and the quadratic Taylor coefficient. It separately solves the four stationary balance equations using standard-library rational Gaussian elimination and compares currents on 288 positive-rational parameter/bias combinations. The rational inversion witness is independently checked on both sides and at the exact zero. Execute \`python verify.py\` with SymPy installed (version 1.13 or later). These finite checks support, rather than replace, the symbolic matrix-tree proof.

## Relationship to prior work
Sakai and Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process* (arXiv:2609.03560, first submitted September 3, 2026), introduce the site-dependent residence-time and reservoir mechanism and discuss nonlinear rectification using approximate steady-state closures. The present two-site theorem is an exact full-bias classification with an independently tunable internal-to-contact kinetic factor; it does **not** claim first discovery of sample-specific exclusion rectification. Their earlier *Symmetry breaking of current response in disordered exclusion processes* (arXiv:2512.03316) treats a periodic externally biased model rather than the open reservoir-inversion problem. An earlier exact matched-contact two-site channel with internal jump rates equal to the corresponding site-dependent contact-removal prefactors has a fixed rectification sign at every drive. Its generator coincides with this one only at \(d=1\); it cannot be reparametrized to preserve both reservoir directions when \(d\ne1\). The new phenomenon is precisely the sign inversion after separating the internal hopping timescale from those contact prefactors. Earlier four-site open-chain and periodic-ring rectification calculations have different state spaces or contact mechanisms and do not imply these two-site kinetic thresholds.

## Limitations
This is an exactly solvable two-site channel and does not show that the inversion persists in larger systems. The internal-to-contact factor \(d\) is a genuine extra kinetic control and need not equal the conventional nearest-neighbor hopping normalization. The result is a stationary mean-current statement, not a claim about nonlinear dynamical bifurcations or experimentally measured large-system rectification. Available descriptions of the motivating preprint include its abstract and a detailed third-party exposition, but its primary full text was not obtained for a complete same-parameter comparison. This is a residual priority risk, as is possible unindexed earlier work on small Markovian transport channels.

## References
1. I. Sakai and T. Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560 (2026), https://arxiv.org/abs/2609.03560 . First public version: September 3, 2026.
2. I. Sakai and T. Akimoto, *Symmetry breaking of current response in disordered exclusion processes*, arXiv:2512.03316 (2025), https://arxiv.org/abs/2512.03316 .
3. I. Sakai and T. Akimoto, *Unexpected Effects of Disorder on Current Fluctuations in the Symmetric Simple Exclusion Process*, arXiv:2408.11364 (2024), https://arxiv.org/abs/2408.11364 .
4. T. Chou, *How fast do fluids squeeze through microscopic single-file pores?*, Physical Review Letters **80**, 85 (1998).
