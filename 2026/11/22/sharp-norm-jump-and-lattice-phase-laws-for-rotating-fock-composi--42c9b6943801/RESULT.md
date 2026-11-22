# Sharp norm-jump and lattice-phase laws for rotating Fock composition semigroups

## Finding

Consider the standard complex Gaussian Fock Hilbert space \(\mathcal F^2(\mathbb C^d)\), and fix an integer \(d\ge1\), positive real numbers \(a_1,\ldots,a_d\), and arbitrary real numbers \(\omega_1,\ldots,\omega_d\). For \(t\ge0\) define
\[
 T_t f(z_1,\ldots,z_d)=f(e^{(-a_1+i\omega_1)t}z_1,\ldots,e^{(-a_d+i\omega_d)t}z_d),
 \qquad \rho=\max_{1\le j\le d}\frac{|\omega_j|}{a_j}.
\]
The operators form a strongly continuous contractive analytic semigroup, and every \(T_t\) with \(t>0\) is trace class. Its **sharp initial operator-norm jump** is
\[
 \lim_{t\downarrow0}\|I-T_t\|=J(\rho),\qquad
 J(0)=1,\quad
 J(\rho)=\max_{u\ge0}\left|1-e^{-u+i\rho u}\right|\quad(\rho>0).
\]
For \(\rho>0\) there is exactly one maximizing point \(u_\rho\), in \((\pi/(2\rho),\pi/\rho)\), characterized by
\[
 \cos(\rho u_\rho)+\rho\sin(\rho u_\rho)=e^{-u_\rho}.
\]
The function \(J\) is continuous and strictly increasing from \(1\) to \(2\), never attaining \(2\), with sharp endpoint laws
\[
 J(\rho)-1\sim\frac{\rho}{e}\exp\!\left(-\frac{\pi}{2\rho}\right)
 \quad(\rho\downarrow0),\qquad
 J(\rho)=2-\frac{\pi}{\rho}+O(\rho^{-2})\quad(\rho\to\infty).
\]
Moreover, for the one-dimensional case \(d=1\), \(a=a_1>0\), and \(\rho=|\omega_1|/a>0\), put
\[
 D_\rho=\frac{(1+\rho^2)e^{-u_\rho}[-\cos(\rho u_\rho)]}{J(\rho)}>0.
\]
Then the **sharp lattice-phase correction** is, as \(t\downarrow0\),
\[
 J(\rho)-\|I-T_t\|
 =\frac{D_\rho a^2t^2}{2}
 \operatorname{dist}\!\left(\frac{u_\rho}{at},\mathbb Z\right)^2+O_{a,\rho}(t^3),
\]
and the full set of limit points of the normalized deficit \(t^{-2}(J(\rho)-\|I-T_t\|)\) is exactly
\[
 \left[0,\frac{a^2D_\rho}{8}\right].
\]
In particular, the second-order coefficient does not converge along all positive real times, even though the semigroup is compact and trace class at every positive time.

## Assumptions and scope

The Fock norm is the standard Gaussian norm for which \(e_{\mathbf n}(z)=\prod_j z_j^{n_j}/\sqrt{n_j!}\), \(\mathbf n\in\mathbb N_0^d\), is an orthonormal basis. All \(a_j\) are **strictly** positive. No translation component or nonnormal linear symbol is included. Complex-time analyticity means bounded holomorphy on some open sector about the positive real axis, with \(T_0=I\) only in the strong topology. In the scalar correction, \(t\) ranges over all positive real values, not a fixed discrete subsequence. At \(\rho=0\) the exact identity \(\|I-T_t\|=1\), for every \(t>0\), replaces the lattice-phase statement.

## Proof

**1. Monomial diagonalization and compact analyticity.** On the above orthonormal basis,
\[
 T_t e_{\mathbf n}
 =\exp\!\left(t\sum_{j=1}^d(-a_j+i\omega_j)n_j\right)e_{\mathbf n}.
\]
Each multiplier has modulus at most one, and tends to zero as \(|\mathbf n|\to\infty\) for fixed \(t>0\). Consequently \(T_t\) is contractive, compact and trace class, since its trace norm is
\[
 \|T_t\|_{\mathcal S_1}=\prod_{j=1}^d(1-e^{-a_jt})^{-1}<\infty.
\]
Strong continuity follows on polynomials and then by contractivity on the whole space. If \(\rho<\infty\), the same diagonal multipliers are bounded holomorphic functions of complex \(t\) on \(|\arg t|<\arctan(1/\rho)\) (interpreted as \(\pi/2\) for \(\rho=0\)); this establishes analyticity on every smaller sector.

**2. The maximum-ratio principle.** Put \(r_j=\omega_j/a_j\). For any monomial index and \(t>0\), set
\[
 U=t\sum_j a_jn_j\ge0,\qquad V=t\sum_j\omega_jn_j,
 \qquad |V|\le\rho U.
\]
For \(\rho>0\), compare \(|1-e^{-U+iV}|\) with the one-coordinate spiral using \(U'=|V|/\rho\le U\). If the first modulus is at most one, it is automatically at most \(J(\rho)>1\). Otherwise, writing \(s=e^{-U}\), its square being larger than one gives \(\cos V<s/2\). Since the derivative of \(|1-r e^{iV}|^2\) with respect to \(r\) is \(2(r-\cos V)>0\) throughout \([s,e^{-U'}]\), replacing \(s\) by \(e^{-U'}\) cannot decrease the modulus. The resulting modulus is \(|1-e^{-U'+i\rho U'}|\), up to complex conjugation, and hence at most \(J(\rho)\). If \(\rho=0\), all multipliers are real in \([0,1]\), giving the bound one.

Conversely, choose a coordinate attaining \(|r_j|=\rho\) and restrict to monomials supported in that coordinate. As \(t\downarrow0\), the points \(a_jtn\), \(n\in\mathbb N_0\), become dense in each compact subinterval of \([0,\infty)\). Their norms converge from below to the continuous spiral maximum. This proves the asserted full operator-norm limit, and also its dependence only on the maximal rotation-to-damping ratio.

**3. Unique spiral maximizer and strict variation.** Define
\[
 F_\rho(u)=|1-e^{-u+i\rho u}|^2
 =1+e^{-2u}-2e^{-u}\cos(\rho u).
\]
Its derivative is
\[
 F_\rho'(u)=2e^{-2u}h_\rho(u),\quad
 h_\rho(u)=e^u[\cos(\rho u)+\rho\sin(\rho u)]-1,
 \quad h_\rho'(u)=(1+\rho^2)e^u\cos(\rho u).
\]
On \((0,\pi/\rho)\), \(h_\rho\) strictly increases up to \(\pi/(2\rho)\), strictly decreases thereafter, and has values \(h_\rho(0)=0\) and \(h_\rho(\pi/\rho)=-e^{\pi/\rho}-1<0\). There is therefore precisely one interior positive root \(u_\rho\), lying in the claimed interval; it is a strict local maximum. For \(u\ge\pi/\rho\),
\[
 |1-e^{-u+i\rho u}|\le1+e^{-u}\le1+e^{-\pi/\rho}
 =|1-e^{-\pi/\rho+i\pi}|<\sqrt{F_\rho(u_\rho)},
\]
so it is the unique global maximum. In particular \(J(\rho)>1\).

For \(0<\rho_1<\rho_2\), preserve the maximizing phase \(\theta=\rho_1u_{\rho_1}\in(\pi/2,\pi)\) while reducing the decay parameter from \(u_{\rho_1}\) to \(\theta/\rho_2\). Because \(\cos\theta<0\), increasing the radius \(e^{-u}\) strictly increases the modulus. Thus \(J(\rho_2)>J(\rho_1)\). Continuity at every positive \(\rho\) follows from the unique root and the implicit function theorem; continuity at zero follows from the endpoint asymptotic below.

**4. Sharp small- and large-angle laws.** Set \(\theta_\rho=\rho u_\rho\). Its defining equation has a zero of the trigonometric part at
\[
 \theta_0=\frac\pi2+\arctan\rho.
\]
As \(\rho\downarrow0\), the exponentially small right side shifts this zero by \(O(e^{-\pi/(2\rho)})\), hence
\[
 u_\rho=\frac{\pi}{2\rho}+\frac{\arctan\rho}{\rho}
 +O\!\left(\frac{e^{-\pi/(2\rho)}}{\rho}\right).
\]
Substitute into \(F_\rho(u_\rho)-1=e^{-2u_\rho}-2e^{-u_\rho}\cos\theta_\rho\). Since \(-\cos\theta_0=\rho/\sqrt{1+\rho^2}\) and \(e^{-u_\rho}\sim e^{-1}e^{-\pi/(2\rho)}\), the result is
\[
 J(\rho)-1=\frac{\rho}{e}e^{-\pi/(2\rho)}(1+O(\rho^2)).
\]
For \(\rho\to\infty\), the same root equation, expanded at \(\theta=\pi\), gives \(\theta_\rho=\pi-2/\rho+O(\rho^{-2})\). Therefore \(u_\rho=\pi/\rho+O(\rho^{-2})\), and substitution yields \(J(\rho)=2-\pi/\rho+O(\rho^{-2})\). This also establishes the limiting range \((1,2)\).

**5. Quadratic lattice correction and all its limit points.** Differentiating the above identity at \(u_\rho\), where \(F_\rho'=0\), gives
\[
 -\left.\frac{d^2}{du^2}\sqrt{F_\rho(u)}\right|_{u=u_\rho}
 =\frac{(1+\rho^2)e^{-u_\rho}[-\cos(\rho u_\rho)]}{J(\rho)}=D_\rho>0.
\]
A fixed neighborhood of the strict global maximizer has a uniform third-order Taylor remainder. Outside it there is a strict positive gap below \(J(\rho)\); on the tail the same gap follows from the estimate in Step 3. For sufficiently small \(t\), an optimal integer index therefore lies among the lattice points within \(O(t)\) of \(u_\rho\). Taking the best such point, the Taylor formula yields
\[
 J(\rho)-\max_{n\ge0}|1-e^{(-a+i\omega)nt}|
 =\frac{D_\rho}{2}(at)^2
 \operatorname{dist}\!\left(\frac{u_\rho}{at},\mathbb Z\right)^2+O_{a,\rho}(t^3).
\]
The tail of the diagonal spectrum gives the competing value \(1\), but the lattice maximum is strictly above one once \(t\) is sufficiently small, so this equals \(J(\rho)-\|I-T_t\|\). Division by \(t^2\) confines every limit point to \([0,a^2D_\rho/8]\). Conversely, for each \(\eta\in[0,1/2]\), choose \(t_m=u_\rho/[a(m+\eta)]\). Then \(t_m\downarrow0\), the fractional lattice distance is \(\eta\), and the normalized deficit tends to \(a^2D_\rho\eta^2/2\). Every value of the stated interval occurs.

## Verification

A standalone Python checker in `check.py` numerically evaluates the unique spiral critical point by bisection, compares it with dense finite samples, tests the curvature identity, checks small-angle and large-angle asymptotic scales, probes the lattice-phase correction at prescribed fractional phases, and tests the multivariate maximum-ratio upper bound. The checker emits `PASS 12241 finite diagnostics` in the supplied environment. These are **finite diagnostics**, not a substitute for the analytic proof, and no finite sample is represented as exhaustive evidence about the infinite monomial index set.

## Relationship to prior work

Bayart, Wang and Yao (2026) characterize the relevant strongly continuous Fock composition semigroups in several variables and their generators; their normal-generator case includes the diagonal symbols above. Chalendar and Partington (2021/2023) give a one-variable semigroup classification and strong-continuity framework. Neither paper's inspected semigroup statements yields the explicit initial norm-jump envelope, its beyond-all-orders small-rotation law, or the sharp quadratic correction with its full lattice-phase cluster interval. The monomial diagonalization itself is standard and is not claimed as novel. Published studies of general diagonal-semigroup norm jumps and of zero–two saturation concern different spectral scaling regimes, as detailed in the accompanying review.

## Limitations

The result applies only to diagonal normal linear Fock symbols with strictly positive decay; translations, nondiagonal dissipative generators, coordinates with zero damping, and general weighted composition operators are not covered. The quantitative correction is proved only in one complex coordinate, not for arbitrary competing multidimensional rotation ratios. The claim has not undergone independent mathematical review, and an older equivalent treatment of spiral norm maxima or lattice-phase discretization could affect priority. No claim about general norm-jump envelopes of all analytic semigroups is made.

## References

1. F. Bayart, M. Wang and X. Yao, *Semigroup of composition operators on the Fock space of several complex variables*, arXiv:2610.26349, first version 19 October 2026. https://arxiv.org/abs/2610.26349
2. I. Chalendar and J. R. Partington, *Weighted composition operators on the Fock space: iteration and semigroups*, arXiv:2106.00427, first version 1 June 2021; Acta Sci. Math. 89 (2023), 93–108. https://arxiv.org/abs/2106.00427
3. C. C. Cowen and B. D. MacCluer, *Composition Operators on Spaces of Analytic Functions*, CRC Press, 1995. Background on composition operator theory; not cited for the new quantitative estimates.
