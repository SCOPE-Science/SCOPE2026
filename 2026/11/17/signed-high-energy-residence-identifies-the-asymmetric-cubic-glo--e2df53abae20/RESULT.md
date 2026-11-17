# Signed high-energy residence identifies the asymmetric cubic global center

## Finding
Consider the globally periodic cubic Hamiltonian flow
\[
\dot x=(1+2ax+kx^2)y,\qquad
\dot y=-x+ax^2-kx^3-(a+kx)y^2,
\]
with \(a\in\mathbb R\) and \(k>a^2\). Let \(T_+(E)\) and \(T_-(E)\) be the **original physical times** spent at \(x>0\) and \(x<0\), respectively, along the energy-\(E\) orbit. Let \(A_\pm(E)\) be the corresponding Euclidean areas enclosed in the respective half-planes, and set \(T=T_++T_-\), \(A=A_++A_-\). The following limits exist for every fixed admissible parameter pair:
\[
\begin{aligned}
L&:=\lim_{E\to\infty}\frac{\sqrt E\,T(E)}{\log E}=\frac{1}{\sqrt{2k}},\\
B&:=\lim_{E\to\infty}\sqrt E\,[T_+(E)-T_-(E)]
=-2\sqrt{\frac2k}\,\operatorname{artanh}\!\left(\frac{a}{\sqrt k}\right),\\
\lim_{E\to\infty}\frac{A_+(E)-A_-(E)}{\sqrt E}&=2B.
\end{aligned}
\]
Consequently the two signed residence probabilities have the **sharp first asymmetry term**
\[
\frac{T_+(E)}{T(E)}
=\frac12-\frac{2\operatorname{artanh}(a/\sqrt k)}{\log E}
+o(1/\log E),\qquad
\frac{A_+(E)}{A(E)}
=\frac12-\frac{2\operatorname{artanh}(a/\sqrt k)}{\log E}
+o(1/\log E).
\]
There is also an **all-energy strict geometric ordering**: for every \(E>0\), \(A_+(E)<A_-(E)\) when \(a>0\), \(A_+(E)>A_-(E)\) when \(a<0\), and equality holds exactly when \(a=0\). Therefore the sign of the asymmetry coefficient is already visible from a single finite-energy oriented area comparison, even though no unsigned observation can distinguish the reflected pair.

The map \((a,k)\mapsto(L,B)\) is a real-analytic diffeomorphism from \(\{(a,k):k>a^2\}\) onto \(\{(L,B):L>0,\ B\in\mathbb R\}\), with explicit inverse
\[
\boxed{\ k=\frac1{2L^2},\qquad
 a=\sqrt k\,\tanh\!\left(-\frac{B\sqrt k}{2\sqrt2}\right).\ }
\]
Thus two **high-energy physical-time measurements**, one unsigned and one signed, recover both coefficients. By contrast the **entire unsigned period and area functions**, not merely their leading asymptotics, agree exactly for the reflected parameter pairs \((a,k)\) and \((-a,k)\); hence those unsigned measurements cannot identify the sign of \(a\).

## Assumptions and scope
The parameters \(a,k\) are fixed real numbers with \(k>a^2\). Define
\[
p(x)=1+2ax+kx^2,\quad
V(x)=\frac{x^2}{2}-\frac{ax^3}{3}+\frac{kx^4}{4},\quad
H(x,y)=\frac{p(x)y^2}{2}+V(x).
\]
Since \(p(x)>0\) and \(1-ax+kx^2>0\), the identity \(V'(x)=x(1-ax+kx^2)\) shows that \(V\) is decreasing on the negative half-line, increasing on the positive half-line, and tends to infinity at both ends. Thus each \(E>0\) has exactly two turning points \(-r_-(E)<0<r_+(E)\) with \(V(-r_-)=V(r_+)=E\). Each positive-energy level is a smooth compact oval; its minimal period is \(T(E)\). The sets \(x=0\) have zero time and area, so half-plane partitions are unambiguous. \(A_\pm\) are **Euclidean** areas in the displayed canonical coordinates. All limits are at fixed \(a,k\), with \(E\to\infty\); none is asserted uniformly near \(k=a^2\).

## Proof
**1. Hamiltonian geometry and exact quadratures.** Direct differentiation gives \(\dot x=H_y=p(x)y\) and \(\dot y=-H_x=-V'(x)-(a+kx)y^2\). Therefore each positive-energy oval is traversed once in minimal physical period. On either half of the plane, write \(V_s(r)=V(sr)=r^2/2-sa r^3/3+kr^4/4\), \(p_s(r)=p(sr)=1+2sa r+kr^2\), for \(s\in\{+1,-1\}\). The positive turning distance \(r_s(E)\) is the unique root \(V_s(r)=E\). The time and area in side \(s\) are
\[
T_s(E)=\sqrt2\int_0^{r_s(E)}\frac{dr}{\sqrt{p_s(r)}\sqrt{E-V_s(r)}},\qquad
A_s(E)=2\sqrt2\int_0^{r_s(E)}\sqrt{\frac{E-V_s(r)}{p_s(r)}}\,dr.
\tag{1}
\]
Differentiating the area integral (the vanishing endpoint and integrable square-root singularity justify differentiation) gives the exact identity \(A_s'(E)=T_s(E)\).

**2. A finite signed mass at infinity.** Define the truncated mass and its energy derivative by
\[
F_s(E)=\int_0^{r_s(E)}\frac{dr}{\sqrt{p_s(r)}},\qquad
F_s'(E)=\frac{1}{\sqrt{p_s(r_s(E))}\,V_s'(r_s(E))}.
\tag{2}
\]
The substitution \(u=V_s(r)\) in (1) gives the exact Abel representation
\[
T_s(E)=\sqrt2\int_0^E\frac{F_s'(u)}{\sqrt{E-u}}\,du.
\tag{3}
\]
Set \(\Delta=k-a^2>0\). Elementary integration yields
\[
F_s(E)=\frac1{\sqrt k}\left[
\operatorname{arsinh}\left(\frac{k r_s(E)+sa}{\sqrt\Delta}\right)
-\operatorname{arsinh}\left(\frac{sa}{\sqrt\Delta}\right)\right].
\tag{4}
\]
With \(R(E)=(4E/k)^{1/4}\), polynomial inversion gives
\[
r_s(E)=R(E)+\frac{sa}{3k}+O(R(E)^{-1}),
\qquad F_s'(E)=\frac{1}{4\sqrt k\,E}+O(E^{-5/4}).
\tag{5}
\]
Both error estimates follow directly by substitution into \(V_s(r_s)=E\), then expansion of the exact expression (2); the constants depend on fixed \(a,k\). Thus \(r_+(E)/r_-(E)\to1\), and the two large-argument \(\operatorname{arsinh}\) terms in (4) cancel in their difference. Consequently
\[
\lim_{E\to\infty}[F_+(E)-F_-(E)]
=-\frac2{\sqrt k}\operatorname{arsinh}\left(\frac a{\sqrt\Delta}\right)
=-\frac2{\sqrt k}\operatorname{artanh}\left(\frac a{\sqrt k}\right).
\tag{6}
\]
Here the inverse-hyperbolic identity holds for \(|a|<\sqrt k\). Note that the signed difference is **order one**, although each individual \(F_s(E)\) diverges logarithmically.

**3. Abel concentration and the signed clock.** Let \(g(u)=F_+'(u)-F_-'(u)\). Near zero, inversion of \(V_s(r)\) gives \(r_s(E)=\sqrt{2E}+(2sa/3)E+O(E^{3/2})\) and hence \(F_s(E)=\sqrt{2E}-(sa/3)E+O(E^{3/2})\); thus \(g\) is bounded near zero. At infinity, (5) gives \(g(u)=O(u^{-5/4})\). In particular \(g\in L^1(0,\infty)\) and \(\int_0^\infty g=\lim(F_+-F_-)\). By (3),
\[
\frac{\sqrt E}{\sqrt2}(T_+(E)-T_-(E))
=\int_0^E\frac{g(u)}{\sqrt{1-u/E}}\,du.
\tag{7}
\]
On \([0,E/2]\), the integrand is bounded by \(\sqrt2|g(u)|\), so dominated convergence applies after zero extension. On \([E/2,E]\), the bound \(|g(u)|\le C u^{-5/4}\) implies that the integral is \(O(E^{-1/4})\). Hence (7) tends to \(\int_0^\infty g\), and (6) proves the stated formula for \(B\), including \(a=0\).

**4. Unsigned scale and the area clock.** For each \(s\), (5) and (3) give
\[
\frac{\sqrt E}{\sqrt2}T_s(E)
=\frac{\log E}{4\sqrt k}+O(1).
\tag{8}
\]
To justify the logarithm, split (3) at a fixed \(u_0>0\) and at \(E/2\). The term \((4\sqrt k\,u)^{-1}\) integrated over \([u_0,E/2]\) contributes \((4\sqrt k)^{-1}\log E+O(1)\); the \(O(u^{-5/4})\) error has finite integral, and the remaining Abel endpoint range contributes \(O(1)\). Sum (8) over both signs to obtain \(L=1/\sqrt{2k}\). Since \(A_s(0)=0\) and \(A_s'=T_s\), integration of the asymptotics \(T_+-T_-=B E^{-1/2}+o(E^{-1/2})\) and \(T=L E^{-1/2}\log E+O(E^{-1/2})\) proves
\[
A_+(E)-A_-(E)=2B\sqrt E+o(\sqrt E),\qquad
A(E)=2L\sqrt E\log E+O(\sqrt E).
\tag{9}
\]
Dividing the differences by the sums proves both first-order signed probability formulas. The \(o\)-statements remain valid when \(a=0\), where the signed differences vanish identically.

**5. Global strict signed-area ordering.** The signed area ordering does not follow merely from the high-energy expansion. Introduce the **mass coordinate** \(z=\int_0^r p_s(t)^{-1/2}dt\). Its exact inverse is
\[
r_s(z)=\frac{\sinh(\sqrt k z)}{\sqrt k}
+\frac{sa}{k}[\cosh(\sqrt k z)-1],\qquad z\ge0.
\]
Indeed its derivative is \(\sqrt{p_s(r_s(z))}\) and \(r_s(0)=0\). Let \(\beta=a/\sqrt k\), \(h=\cosh(\sqrt k z)-1>0\), and \(S=\sinh(\sqrt k z)>0\). The mass-coordinate potentials \(W_s(z)=V_s(r_s(z))\) satisfy the **exact factorization**
\[
k[W_+(z)-W_-(z)]=\frac{2\beta S h}{3}
[3h^2+5h+1+3\beta^2h(h-1)].
\tag{10}
\]
For \(h\ge1\) the bracket is positive. For \(0<h<1\), the inequality \(\beta^2<1\) bounds it below by \(6h^2+2h+1>0\). Hence \(\operatorname{sgn}(W_+-W_-)=\operatorname{sgn}(a)\) at every positive mass coordinate. Each \(W_s\) is strictly increasing from zero to infinity, so its inverse energy coordinate is \(F_s(E)\). Thus \(\operatorname{sgn}(F_+(E)-F_-(E))=-\operatorname{sgn}(a)\) for every \(E>0\). Integrating the area form of (1) by parts gives
\[
A_s(E)=\sqrt2\int_0^E\frac{F_s(u)}{\sqrt{E-u}}\,du.
\tag{11}
\]
Its kernel is strictly positive. Therefore the exact strict area ordering follows for every positive energy. This proof does **not** claim the same global sign assertion for the unintegrated half-periods.

**6. Exact reflection obstruction and inverse.** Replacing \(a\) by \(-a\) and \((x,y)\) by \((-x,-y)\) preserves the Hamiltonian and canonical form: \(H_{-a}(-x,-y)=H_a(x,y)\). This maps each full energy oval to the reflected oval preserving its physical period and total enclosed area, while exchanging positive and negative residence measurements. Thus \(T(E;a,k)=T(E;-a,k)\) and \(A(E;a,k)=A(E;-a,k)\) for **every** \(E>0\). Finally the explicit formulas for \(L\) and \(B\) invert as claimed: \(L>0\) determines \(k\), and strict monotonicity of \(\operatorname{artanh}(a/\sqrt k)\) identifies \(a\) over its full admissible interval. The inverse \(\tanh\) formulas are analytic and cover all \(B\in\mathbb R\), proving the global diffeomorphism.

## Verification
The accompanying stand-alone Python 3 standard-library script `check_signed_residence.py` verifies the Hamiltonian identities exactly with rational arithmetic and checks the finite-energy physical-time quadratures using a nonsingular turning-point substitution and adaptive Simpson integration. For \(a=1/2\), \(k=1\), it verifies convergence of \(\sqrt E(T_+-T_-)\) toward \(-2\sqrt2\operatorname{artanh}(1/2)\) across three energies, checks exact inverse-formula identities, checks equality of the two half-periods at \(a=0\), and checks the algebraic mass-coordinate factorization of (10) with exact rational inputs.  Its output is `SIGNED_CUBIC_CENTER_RESIDENCE_INVERSE_OK`. Finite computations corroborate but do not prove infinite-energy assertions; the Abel estimate in Step 3 is the proof.

## Relationship to prior work
Llibre and Rondón [1] classified this precise cubic system as a global center (their Theorem 2(c), equation (23), with \(a=a_1\), \(k=-c_1\)). The published mathematical note [2] proves the **total** physical-period two-term asymptotic and the fair-sign limiting logarithmic occupation law for the same parameters, but neither its stated theorem nor its proof supplies the finite **signed** difference \(B\), global half-area ordering, high-energy Euclidean half-area bias, or complete sign-sensitive inverse. Its total-period information is reflection invariant, and cannot infer the sign of \(a\). Ghose-Choudhury and Guha [3] prove general position-dependent-mass period quadratures and monotonicity criteria, rather than the signed Abel limit and inverse here. The model-specific sharp signed coefficient, all-energy strict area ordering, area companion, and sign-recovery statement constitute the claimed addition; elementary Abel transforms and inverse-hyperbolic integration are not claimed as new techniques.

## Limitations
The claim concerns a fixed two-parameter family and \(E\to\infty\), with no uniformity at \(k=a^2\). It does not assert strict sign of \(T_+-T_-\) at **every** finite energy, global period monotonicity, perturbative robustness beyond the family, or a new center classification. The limit \(B\) vanishes at \(a=0\); the inverse remains mathematically injective, but finite-data statistical conditioning is not analyzed. The total-period two-term formula and fair-sign leading occupation are prior published results [2], not claimed here. Novelty comparisons are best-knowledge and do not constitute an independent priority certification.

## References
1. J. Llibre and G. Rondón, *Global centers of a class of cubic polynomial differential systems*, arXiv:2310.07454v1, public 2023-10-11, Theorem 2(c), equation (23). https://arxiv.org/abs/2310.07454
2. *Logarithmic occupation and the two-term high-energy period of a cubic global center*, published mathematical research note, 2026-10-11, identifier `8be50b06b677`. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-logarithmic-occupation-and-the-two-term-high-energy-period-of-a--8be50b06b677
3. A. Ghose-Choudhury and P. Guha, *Monotonicity of the period function of the Liénard equation of second kind*, arXiv:1608.02910v1 (2016), Section 2, formula (2.1). https://arxiv.org/abs/1608.02910
