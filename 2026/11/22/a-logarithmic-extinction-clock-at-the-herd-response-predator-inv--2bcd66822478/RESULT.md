# A logarithmic extinction clock at the herd-response predator invasion threshold

## Finding

For the positive discrete herd-response predator–prey map defined below, at the critical invasion parameter \(b=d\), every orbit in an explicit sufficiently small positive invariant wedge has a finite second-order reciprocal-population clock:

\[
\frac{1}{y_n}=\frac{ad}{2}n+\frac{3a(d+1)}4\log n+C(x_0,y_0)+o(1).
\]

The positive coefficient of \(\log n\) is universal for fixed \(a,d\) and cannot be eliminated by choosing initial data in the wedge. The slaved prey deficit has the companion expansion

\[
1-x_n=a y_n+\frac{a^2(d+1)}2 y_n^2+O(y_n^3).
\]

Consequently \(ny_n\to2/(ad)\) and \(n(1-x_n)\to2/d\). The latter leading-order conclusions do not by themselves entail the finite renormalized limit in the displayed clock.

## Assumptions and scope

Let \(a,d>0\) and set \(b=d\) in the map of Li and Li [1]:

\[
x_{n+1}=x_n\exp\left(1-x_n-\frac{a y_n}{\sqrt{x_n}}\right),\qquad
 y_{n+1}=y_n\exp\left(d(\sqrt{x_n}-1)\right).
\]

For **every** prescribed \(K>a\), there exists \(\varepsilon=\varepsilon(a,d,K)>0\) such that the conclusion holds for **every** initial state

\[
0<y_0<\varepsilon,\qquad 0\le 1-x_0<K y_0.
\]

One can take \(\varepsilon\) small enough that \(K\varepsilon<1\); all subsequent states are strictly positive and obey \(0\le1-x_n<Ky_n\), with \(0<y_n\le y_0\). The open interior \(0<1-x_0<Ky_0\) is nonempty. The constant \(C(x_0,y_0)\) depends on the orbit and both parameters, and is the convergent limit of the difference between \(1/y_n\) and its displayed linear and logarithmic terms. No global-basin or off-threshold assertion is made.

## Proof

Write \(v_n=y_n\), \(\delta_n=1-x_n\). In the neighborhood \(0\le\delta<Kv\), the exact map becomes

\[
\begin{aligned}
\mathcal D(\delta,v)&=1-(1-\delta)\exp\left(\delta-\frac{av}{\sqrt{1-\delta}}\right),\\
\mathcal V(\delta,v)&=v\exp\left(d(\sqrt{1-\delta}-1)\right).
\end{aligned}
\]

**Forward wedge and convergence.** The inequality \((1-\delta)e^{\delta}\le1\) for \(0\le\delta<1\) ensures \(\mathcal D\ge0\), and \(0<\mathcal V\le v\). Uniform Taylor estimates for \(0\le\delta\le Kv\), \(v\to0\), give \(\mathcal D=av+O(v^2)\) and \(\mathcal V=v+O(v^2)\). Since \(K>a\), for sufficiently small \(\varepsilon\) we have \(\mathcal D<K\mathcal V\), proving forward invariance. In fact the same estimates give \(\mathcal D\ge (a/2)v\). As \(v_n\) is monotone, it has a limit. A strictly positive limit would imply \(\delta_{n+1}\ge(a/2)v_n\), hence an eventual uniform strict exponential contraction of \(v_{n+1}=v_n e^{d(\sqrt{1-\delta_n}-1)}\), a contradiction. Thus \(v_n\downarrow0\) and \(\delta_n\to0\). Also \(v_{n+1}/v_n\to1\), and the relation \(\delta_{n+1}=av_n+O(v_n^2)\) yields \(\delta_n/v_n\to a\).

**Quadratic slaving with a controlled remainder.** Set \(H(v)=av+Bv^2\). Direct Taylor expansion of \(\mathcal D(H(v),v)-H(\mathcal V(H(v),v))\) has quadratic coefficient \([a^2(d+1)-2B]/2\). Choosing \(B=a^2(d+1)/2\) makes this invariance defect \(O(v^3)\). Define \(e_n=\delta_n-H(v_n)\). On the wedge, both \(\partial_\delta\mathcal D\) and \(\partial_\delta\mathcal V\) are \(O(v)\), uniformly as \(v\to0\). By the mean-value theorem and the invariance defect,

\[
|e_{n+1}|\le C_1 v_n|e_n|+C_2 v_n^3.
\]

Because \(v_{n+1}/v_n\to1\) and \(v_n\to0\), choosing a late starting index and a sufficiently large multiplicative constant in a one-step induction proves \(e_n=O(v_n^3)\). This does not require that the original orbit lie exactly on any center manifold. It gives \(\delta_n=av_n+[a^2(d+1)/2]v_n^2+O(v_n^3)\).

**Cubic scalar reduction.** Substituting the established slaving estimate into \(\mathcal V\) and expanding the square root and exponential through cubic order gives, with uniform fourth-order remainder,

\[
v_{n+1}=v_n-cv_n^2+e v_n^3+O(v_n^4),\qquad
 c=\frac{ad}{2},\quad e=-\frac{a^2d(d+3)}8.
\]

This polynomial identity can be independently recomputed by the script `check.py`. In particular, letting \(r_n=1/v_n\), reciprocal expansion yields

\[
r_{n+1}-r_n=c+(c^2-e)v_n+O(v_n^2).
\]

The positivity of \(c\) first implies \(r_n/n\to c\), hence \(v_n=1/(cn)+o(1/n)\). Then \(r_{n+1}-r_n=c+O(1/n)\) shows \(r_n=cn+O(\log n)\), so

\[
v_n=\frac1{cn}+O\left(\frac{\log n}{n^2}\right).
\]

Consequently,

\[
r_{n+1}-r_n=c+\frac{c^2-e}{c}\frac1n+O\left(\frac{\log n}{n^2}\right),
\]

whose last remainder is summable. Since \(\sum_{k=1}^{n-1}k^{-1}-\log n\) has a finite limit, \(r_n-cn-[(c^2-e)/c]\log n\) converges to a finite constant. Finally

\[
\frac{c^2-e}{c}=\frac{3a(d+1)}4>0.
\]

This completes the proof including existence of the finite constant and the uniformity of the stated assumptions.

## Verification

The included standalone `check.py` recomputes the quadratic invariance defect, the cubic predator coefficient and the rational simplification of the logarithmic coefficient with exact symbolic arithmetic. It additionally iterates positive data at two parameter settings and checks numerical stabilization of the renormalized clock and convergence of the scaled prey slaving residual. The mathematical proof above, not the finite experiment, establishes the infinite-time assertions. To reproduce, run `python check.py` with Python 3 and SymPy installed.

## Relationship to prior work

Li and Li [1], publicly available on January 22, 2024, introduced the map (their equation (1.7)), proved a transcritical bifurcation at \(b=d\) (Theorem 3.1), and calculated a quadratic center-manifold coefficient corresponding to \(B=a^2(d+1)/2\) together with the quadratic term \(-ad v^2/2\). These **are not new claims here**. Their paper's inspected transcritical derivation, other main theorems, numerical section and conclusion do not state the cubic scalar correction or a finite, logarithmically renormalized extinction clock on a positive-data wedge. Standard parabolic normal-form techniques motivate inverse-time decay, but without the model-specific cubic coefficient and a controlled global-in-time slaving error they do not give the displayed numerical logarithmic coefficient. Searches of nearby published results found critical extinction clocks for different predator–prey maps; none inspected implies this map-specific coefficient.

## Limitations

The conclusion is local at the neutral invasion threshold \(b=d\) and proven on a concrete nonempty wedge, not for arbitrary positive initial states. It is a deterministic mathematical asymptotic, not a validated ecological forecast. A broader unindexed theorem could conceivably contain the formula as a specialization; a negative literature search does not prove uniqueness or publication priority. No independent mathematical audit has been performed.

## References

[1] Danyang Li and Xianyi Li, *Transcritical bifurcation and Neimark–Sacker bifurcation of a discrete predator-prey model with herd behaviour and square root functional response*, Mathematical and Computer Modelling of Dynamical Systems **30** (2024), 31–50. Published online January 22, 2024. DOI: https://doi.org/10.1080/13873954.2024.2304798. Primary full text: https://www.tandfonline.com/doi/pdf/10.1080/13873954.2024.2304798.

[2] *Global critical extinction with a cancellable logarithmic clock in an exponential predator-prey map*, 2026: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-global-critical-extinction-with-a-cancellable-logarithmic-clock--5fcebfadc8fa. Compared via indexed summary as an analogous but distinct system, not as a source for the present theorem.

[3] *Universal two-term critical extinction and a saturation-independent prey correction in a discrete plankton map*, 2026: https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-universal-two-term-critical-extinction-and-a-saturation-independ--2ba15cb5a76c. Compared via indexed summary, with a different predator exponent and map.
