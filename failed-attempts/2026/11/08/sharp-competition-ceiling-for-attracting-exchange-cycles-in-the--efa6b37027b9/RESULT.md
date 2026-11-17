# Sharp competition ceiling for attracting exchange cycles in the symmetric Ricker map

## Finding

For the competitive Ricker map
\[
F_{r,a}(x,y)=\bigl(rx\exp(-x-ay),\;ry\exp(-ax-y)\bigr),
\qquad r>0,\quad a>0,
\]
a **positive exchange cycle** is an orbit of least period two consisting of \((u,v)\) and \((v,u)\), where \(u>v>0\). For each \(0<a<1\), such a cycle exists uniquely if and only if
\[
r>r_{\mathrm{birth}}(a):=\exp\!\left(\frac{2(1+a)}{1-a}\right).
\]
There is no such positive exchange cycle when \(a\geq1\). When it exists, there is exactly one \(t>0\) such that
\[
\log r=\frac{2(1+a)}{1-a}\,t\coth t,\qquad
S=\frac{4t\coth t}{1-a},\qquad
u=\frac{S(1+\tanh t)}2,\quad v=\frac{S(1-\tanh t)}2.
\]

For \(0<a<1\), let \(t_1=t_1(a)>0\) be the unique solution of
\[
\frac{2t_1}{\sinh(2t_1)}=\frac{1-a}{1+a},
\]
and let \(t_2=t_2(a)>0\) be the unique solution of
\[
(1+a)\left(\frac{t_2}{\sinh t_2}\right)^2-t_2\coth t_2+\frac{1-a}{2}=0.
\]
**Both two-step Floquet multipliers lie strictly in the open unit disk if and only if**
\[
t_1(a)<t<t_2(a).
\]
These two inequalities admit a solution precisely for \(0<a<a_*\), with exact ceiling
\[
a_*:=\frac{1-h(t_*)}{1+h(t_*)}=0.277839040264087151\ldots,
\quad h(t)=\frac{2t}{\sinh(2t)},
\quad \sinh^3t_*=t_*\cosh t_*,\quad t_*>0.
\]
The critical equation has exactly one positive solution, \(t_*=0.976988986309677152\ldots\). The complete **linearly attracting exchange-cycle window in the growth parameter** is
\[
\exp\!\left(\frac{2(1+a)}{1-a}t_1\coth t_1\right)<r<
\exp\!\left(\frac{2(1+a)}{1-a}t_2\coth t_2\right)
\quad(0<a<a_*).
\]
At either endpoint a Floquet multiplier is on the unit circle; when \(a=a_*\), no strictly linearly attracting exchange cycle exists. Statements of nonlinear behavior at nonhyperbolic equality are outside this theorem.

## Assumptions and scope

All coordinates are strictly positive; the parameters satisfy \(r>0\), \(a>0\). The term exchange cycle refers **only** to a two-cycle mapped by the coordinate swap, not to an arbitrary period-two orbit. Stability means the spectral radius of the derivative of \(F_{r,a}^2\) at the orbit is strictly less than one. It therefore implies local asymptotic attraction; unit-modulus multiplier cases are deliberately not classified as attracting or repelling. No global basin or other period classification is claimed.

## Proof

**1. Exact exchange-cycle parametrization.** The exchange conditions are
\[
v=ru e^{-u-av},\qquad u=rv e^{-au-v}.
\]
Put \(t=\frac12\log(u/v)>0\) and \(S=u+v\). Taking the sum and difference of their logarithms gives the identities
\[
\log r=\frac{1+a}{2}S,\qquad (1-a)(u-v)=4t.
\]
Since \(u-v=S\tanh t>0\), these force \(0<a<1\) and the displayed formulas for \(S,u,v,r\). Conversely those formulas satisfy both original exchange equations for every \(t>0\). The function \(t\coth t\) increases strictly from \(1\) to infinity: its derivative has the positive numerator \(\sinh t\cosh t-t\). Thus the parametrization is one-to-one and proves the existence and uniqueness claims, including the strict boundary at \(r_{\mathrm{birth}}\).

**2. Exact Floquet reduction.** At the first exchange point set \(A=DF_{r,a}(u,v)\) and let \(P\) exchange the two coordinates. Since \(F_{r,a}(v,u)=P F_{r,a}(u,v)\), one has \(DF_{r,a}(v,u)=PAP\). Using the exchange equations to simplify the derivative gives
\[
A=\begin{pmatrix}
(v/u)(1-u)&-av\\-au&(u/v)(1-v)
\end{pmatrix},\quad
K:=PA=\begin{pmatrix}
-au&(u/v)(1-v)\\(v/u)(1-u)&-av
\end{pmatrix},\quad
D(F^2)(u,v)=K^2.
\]
Consequently the two-step multipliers have modulus strictly less than one exactly when both eigenvalues of \(K\) have modulus strictly less than one. Direct expansion yields
\[
\operatorname{tr}K=-aS,\qquad
\det K=S-1-(1-a^2)uv,
\qquad uv=\frac{4t^2}{(1-a)^2\sinh^2t}.
\]
For a real monic quadratic \(\lambda^2-(\operatorname{tr}K)\lambda+\det K\), the strict Schur/Jury conditions are
\[
1+\operatorname{tr}K+\det K>0,\quad
1-\operatorname{tr}K+\det K>0,\quad1-\det K>0.
\]
The first two factor exactly as
\[
1+\operatorname{tr}K+\det K=(1-a)[S-(1+a)uv],\qquad
1-\operatorname{tr}K+\det K=(1+a)[S-(1-a)uv].
\]
For \(0<a<1\), the first strict inequality implies the second. The first reduces to
\[
h(t):=\frac{2t}{\sinh(2t)}<\frac{1-a}{1+a},
\]
while the remaining inequality is equivalently
\[
\frac{1-a}{4}(1-\det K)=J_a(t)>0,
\quad J_a(t)=(1+a)(t/\sinh t)^2-t\coth t+(1-a)/2.
\]
The function \(h\) strictly decreases from \(1\) to zero. Both \(t/\sinh t\) and its positive square strictly decrease, whereas \(t\coth t\) strictly increases; hence \(J_a\) strictly decreases from \((1+a)/2>0\) to minus infinity. Therefore the three Schur conditions are equivalent to \(t>t_1(a)\) and \(t<t_2(a)\), with each defining equation having exactly one positive root.

**3. Sharp coupling ceiling.** At \(t=t_1(a)\), the first Jury factor vanishes, so \(\det K=aS-1\). Therefore \(t_1<t_2\) holds exactly when \(J_a(t_1)>0\), equivalently \(aS(t_1)<2\). Solving \(h(t_1)=(1-a)/(1+a)\) for \(a\) gives
\[
\frac{aS(t_1)}2=\cosh^2t_1-t_1\coth t_1.
\]
It follows that
\[
t_1<t_2\iff\sinh^3t_1<t_1\cosh t_1.
\]
The ratio \(\sinh^3t/(t\cosh t)\) strictly increases from zero to infinity because
\[
\frac{d}{dt}\log\!\left(\frac{\sinh^3t}{t\cosh t}\right)
=3\coth t-\tanh t-\frac1t>0.
\]
The last inequality follows, for example, from \(\coth t>1/t\) and \(2\coth t>\tanh t\). Thus the equality has exactly one positive solution \(t_*\). Because \(h(t_1(a))=(1-a)/(1+a)\) and \(h\) decreases, \(t_1(a)\) strictly increases in \(a\). Accordingly \(t_1<t_2\) precisely when \(a<a_*\), proving the global sharp ceiling. Finally \(r\) strictly increases in \(t\), converting the amplitude window into the displayed growth-rate window.

## Verification

A standalone program `verify.py` symbolically checks the exchange Jacobian, the three Jury factorizations, the \(t\)-parametrization identities, and the numerical root of the unique critical equation; it independently evaluates the original two-step map and its actual Jacobian at representative parameters, checking stability both inside and outside the predicted intervals. Invoke with `python verify.py`. The checks are finite and diagnostic; the strict monotonicity and global classification are proved analytically above.

## Relationship to prior work

Goldar et al. (first publicly available 2026-09-16) analyze this Ricker competition family, including general two-cycle Jacobian conditions, and numerical bifurcation diagrams, but do not provide the displayed closed one-dimensional exchange-cycle criterion or the sharp universal coupling ceiling. Kulakov, Neverova and Frisman (2022), with full relevant text inspected, discuss out-of-phase period-two dynamics, including their stability transitions, in this same ecological map. The present claim does **not** regard exchange cycles, qualitative stability transitions, or generic Jury tests as newly discovered; it is the exact all-parameter exchange-symmetric census together with the explicit necessary-and-sufficient stability window and computable sharp coupling ceiling.

Jiang and Rogers (1987) study **the same symmetric competition family**: their formulation \(x_{n+1}=x_n\exp[\rho(1-x_n)-\sigma y_n]\), with its exchanged companion equation, becomes the map here under \(X=\rho x\), \(Y=\rho y\), \(r=e^\rho\), and \(a=\sigma/\rho\). and report a parameter region for a stable Hopf bifurcation of a pair of symmetric period-two points. Their abstract establishes substantial prior qualitative coverage. Their full mathematical text could not be obtained despite attempts via publicly available sources and institutional access; thus possible overlap in unstated implicit parameter conditions is a material unresolved historical-priority risk. No theorem of noncoverage is asserted for that paper.

## Limitations

The classification covers positive exchange two-cycles only; other non-exchange periodic orbits, higher periods, basin geometry, and global survival questions are not addressed. At equality of the strict inequalities, the orbit is nonhyperbolic and nonlinear attraction is not determined. Historical originality is provisional because the full Jiang–Rogers treatment (1987) could not be read. The exact ceiling is an analytic statement; its decimal expansion is an illustration, not the proof.

## References

1. S. Goldar, S. S. Hassan, R. Pati, A. A. Mohsen, and M. Izadi, *Dynamics and Bifurcations in a Two-Species Ricker Competition Model With Nonmonotonic Growth*, Discrete Dynamics in Nature and Society (2026), 7255117, DOI: 10.1155/ddns/7255117; first published 2026-09-16.
2. A. N. Kulakov, G. P. Neverova, and E. Ya. Frisman, *The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability*, Mathematics **10** (2022), 1076, DOI: 10.3390/math10071076.
3. H. Jiang and T. D. Rogers, *The discrete dynamics of symmetric competition in the plane*, Journal of Mathematical Biology **25** (1987), 573–596, DOI: 10.1007/BF00275495 (abstract examined; full text not accessible).
