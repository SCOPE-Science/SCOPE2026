# Three positive-step bands for third-order Radau IIA diffusion on large stars

## Finding

Let \(K_{1,m}\) be the simple unweighted star with one hub and \(m\ge2\) leaves. For heat diffusion \(y'=-L_my\), where \(L_m\) is the unnormalized combinatorial Laplacian, apply the two-stage, order-three Radau IIA scheme and write the completed-step map as
\[
T_m(h)=(6I-2hL_m)(6I+4hL_m+h^2L_m^2)^{-1},\qquad h\ge0.
\]
Define the quadratic and quartic
\[
\begin{aligned}
H_m(h)&=(m+1)h^2+(4-2m)h+6,\\
F_m(h)&=(m+1)h^4+(-2m^2+2m+10)h^3\\
&\quad +(6m^2+4m+16)h^2+(24m+12)h+36.
\end{aligned}
\]

**Theorem.** For \(2\le m\le10\), the matrix \(T_m(h)\) is entrywise nonnegative for every \(h\ge0\), and is strictly positive for every \(h>0\). For \(m\ge11\), let
\[
\alpha_m=\frac{m-2-\sqrt{m^2-10m-2}}{m+1},\qquad
\beta_m=\frac{m-2+\sqrt{m^2-10m-2}}{m+1},
\]
and let \(\gamma_m<\delta_m\) be the two distinct positive roots of \(F_m\). Then
\[
0<\alpha_m<\beta_m<2<3<\gamma_m<m<\delta_m
\]
and the **complete** positivity set is
\[
\boxed{T_m(h)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad
h\in[0,\alpha_m]\cup[\beta_m,\gamma_m]\cup[\delta_m,\infty).}
\]
Precisely the hub diagonal becomes negative for \(\alpha_m<h<\beta_m\), and precisely the leaf diagonals become negative for \(\gamma_m<h<\delta_m\); all off-diagonal entries are strictly positive whenever \(h>0\). Thus the set of admissible positive time steps has **three connected components** for every \(m\ge11\).

For example, at \(m=11\) the hub thresholds are exactly \(1/2\) and \(1\), and the two leaf thresholds are approximately \(6.068411604176\) and \(11.764257595354\). Hence arbitrarily increasing a step size can both destroy and restore positivity twice, although the rational integrator is A-stable and L-stable.

## Assumptions and scope

The graph has \(m+1\) vertices, each edge has unit conductance, the heat equation is \(y'=-L_my\), and \(h\) is the nonnegative dimensionless step length. No forcing or boundary constraints are introduced. This is the completed Radau IIA step, not a statement about internal stages. Matrix inequalities mean entrywise inequalities, rather than positive semidefiniteness. The result is exact for all integers \(m\ge2\) and all real \(h\ge0\); it makes no claim for nonuniform spokes, general trees, or other Runge–Kutta methods.

## Proof

**1. Exact spectral projectors.** Order the hub before the leaves. The star Laplacian has eigenvalues \(0\), \(1\) with multiplicity \(m-1\), and \(m+1\) with multiplicity one. Denote the corresponding orthogonal projectors by
\[
\Pi_0=\frac{\mathbf{1}\mathbf{1}^{\mathsf T}}{m+1},\quad
\Pi_1=\begin{pmatrix}0&0\\0&I_m-\mathbf{1}_m\mathbf{1}_m^{\mathsf T}/m\end{pmatrix},\quad
\Pi_{m+1}=\frac{vv^{\mathsf T}}{m(m+1)},\quad v=(m,-1,\ldots,-1)^{\mathsf T}.
\]
The Radau IIA scalar stability function at a negative real argument is
\[
R(-z)=\frac{6-2z}{6+4z+z^2}.
\]
Consequently \(T_m(h)=\Pi_0+R(-h)\Pi_1+R(-(m+1)h)\Pi_{m+1}\). This is an identity for every permitted \(m,h\), since the two quadratic denominators are positive.

**2. Four entry types.** Put
\[
d_1(h)=h^2+4h+6,\qquad d_m(h)=(m+1)^2h^2+4(m+1)h+6.
\]
Direct substitution into the projectors and expansion yield the exact formulas
\[
\begin{aligned}
(T_m)_{00}&=\frac{H_m(h)}{d_m(h)},\\
(T_m)_{0j}&=\frac{h((m+1)h+6)}{d_m(h)}\quad(j\ge1),\\
(T_m)_{jj}&=\frac{F_m(h)}{d_1(h)d_m(h)}\quad(j\ge1),\\
(T_m)_{ij}&=\frac{h^2((m+1)h^2+6(m+2)h+18)}{d_1(h)d_m(h)}
\quad(1\le i\ne j\le m).
\end{aligned}
\]
The off-diagonal entries are strictly positive for all \(h>0\), and both denominators remain strictly positive on \([0,\infty)\). The diagonal signs therefore equal the signs of \(H_m\) and \(F_m\), respectively.

**3. Hub-diagonal interval.** The discriminant of \(H_m\) is \(4(m^2-10m-2)\). For integer \(2\le m\le10\) it is negative, hence \(H_m(h)>0\) for all \(h\). For \(m\ge11\) the two simple roots are \(\alpha_m,\beta_m\); they are positive because \(0<\sqrt{m^2-10m-2}<m-2\), and \(\beta_m<2\). Since the leading coefficient is positive, the hub diagonal is negative exactly for \(\alpha_m<h<\beta_m\).

**4. Leaf-diagonal interval.** Regroup the quartic by powers of \(m\):
\[
\begin{aligned}
F_m(h)&=2h^2(3-h)m^2\\
&\quad +(h^4+2h^3+4h^2+24h)m\\
&\quad +h^4+10h^3+16h^2+12h+36.
\end{aligned}
\]
Every term on the right is nonnegative, and the last is positive, for \(0\le h\le3\). For \(h>3\), it is a concave quadratic in the real variable \(m\). Therefore, when \(2\le m\le10\), its value is at least the smaller endpoint value at \(m=2\) or \(m=10\). Both are strictly positive for all \(h\ge0\), because
\[
F_2(h)=3h^4+6h^3+48h^2+60h+36
\]
and
\[
F_{10}(h)=11h^2(h-8)^2+6h((h-4)^2+26)+36.
\]
It follows that all leaf diagonals are positive for every \(m\le10\).

For \(m\ge11\), put \(t=m-11\ge0\). An exact evaluation gives
\[
F_m(m)=-\big(t^5+46t^4+800t^3+6274t^2+19315t+5640\big)<0.
\]
Yet \(F_m(3)>0\) and the leading coefficient of \(F_m\) is positive. Hence it has at least one root in \((3,m)\) and another in \((m,\infty)\). Its coefficients, read in descending order, have signs \(+,-,+,+,+\) when \(m\ge11\); Descartes' rule of signs allows at most two positive roots counting multiplicity. Thus there are exactly two distinct simple positive roots \(\gamma_m\in(3,m)\) and \(\delta_m\in(m,\infty)\), and \(F_m(h)<0\) exactly between them.

**5. Combination and endpoint behavior.** The two forbidden intervals are disjoint because \(\beta_m<2<3<\gamma_m\). Their signs and the strict positivity of every off-diagonal entry give the claimed three-component exact set, including all four nonnegative endpoints. As \(h\to\infty\), the two nonzero spectral multipliers tend to zero and \(T_m(h)\to\Pi_0\), explaining the eventual reappearance of positivity. Moreover, \(|R(-z)|<1\) for \(z>0\); hence \(\|T_m(h)\|_{2\to2}=1\) and \(T_m(h)\mathbf{1}=\mathbf{1}\) for every \(h\ge0\), even during the two sign-failure intervals. \(\square\)

## Verification

The standalone `verify.py` uses exact rational arithmetic to check the complete matrix identity \((6I+4hL_m+h^2L_m^2)T_m(h)=6I-2hL_m\), all four entry formulas, symmetry, row sums, and off-diagonal and diagonal sign identities for 176 star/step pairs across eleven star sizes. It also checks exact boundary and rational negative-witness evaluations, and reports numerical root approximations for five larger stars. Run with `python verify.py`; the original output is provided in `verification_output.txt`. The finite checks corroborate the identities; the universal result depends on the symbolic projector and polynomial arguments above.

## Relationship to prior work

Gottlieb, Shu and Tadmor analyze strong-stability preservation for Runge–Kutta schemes, including obstructions to unrestricted higher-order SSP behavior. Kovács, Li and Lubich establish maximal parabolic regularity for A-stable discretizations, including Radau IIA. Chertock and colleagues study a **different**, sign-preserving semi-implicit family for damped ODEs. None of these inspected analyses supplies the exact completed-step positivity set for unweighted stars.

Existing specialized numerical-diffusion results on balanced complete multipartite and rook graphs can have a *single* forbidden time-step interval for two-stage Radau IIA. On the present unequal-part star there are **two distinct forbidden intervals**, produced successively by two different diagonal classes. A previously established reversible-chain diagonal lower bound explains why stars on at most eleven vertices have positive diagonals, but does not establish the exact leaf-diagonal quartic or the three-band classification for larger stars.

## Limitations

The statement is confined to unweighted stars and the specified two-stage scheme. It does not establish positivity of internal Runge–Kutta stages or approximation quality at large time steps. The exact classification has been self-checked but not independently audited. An unlocated specialized treatment of this graph–method pair could still contain an equivalent classification; bibliographic search cannot establish uniqueness in the literature.

## References

1. S. Gottlieb, C.-W. Shu and E. Tadmor, “Strong Stability-Preserving High-Order Time Discretization Methods,” *SIAM Review* **43** (2001), 89–112. DOI: 10.1137/S003614450036757X. Electronically published 2001-02-02.
2. A. Chertock, S. Cui, A. Kurganov and T. Wu, “Steady State and Sign Preserving Semi-Implicit Runge–Kutta Methods for ODEs with Stiff Damping Term,” *SIAM Journal on Numerical Analysis* **53** (2015), 2008–2029. DOI: 10.1137/151005798.
3. B. Kovács, B. Li and C. Lubich, “A-stable time discretizations preserve maximal parabolic regularity,” arXiv:1511.07823, first posted 2015-11-24; journal version, *SIAM Journal on Numerical Analysis* **54** (2016), 3600–3624.
