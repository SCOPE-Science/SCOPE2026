# Sharp-degree simultaneous period and Floquet realization on prescribed concentric circles

## Finding
For every integer \(m\ge2\), every ordered list of radii \(0<r_1<\cdots<r_m\), every list of positive original-physical-time minimal periods \(T_1,\ldots,T_m\), and every list of positive, nonunit transverse Floquet multipliers \(\mu_1,\ldots,\mu_m\), a real polynomial planar vector field of total degree exactly \(2m\) has the circles \(x^2+y^2=r_i^2\) as hyperbolic limit cycles with precisely those periods and multipliers. **No alternating-stability restriction applies**: the multipliers may be independently prescribed on either side of one. Moreover, no lower-degree polynomial vector field can possess all these concentric circles as *limit cycles*, regardless of the desired periods or multipliers.

This is an existence-and-sharp-degree result for the prescribed circles. Additional periodic trajectories elsewhere are **not excluded**; the cycles need not be the system's only periodic orbits.

## Assumptions and scope
All fields are autonomous real polynomial vector fields on \(\mathbb R^2\). A transverse Floquet multiplier is the nontrivial positive eigenvalue of the linearized first-return map of a regular periodic orbit; nonunit implies hyperbolicity and isolation. Periods are measured in physical time, without orbital time-reparameterization. The datum \(T_i>0\) is the minimal period, and \(\mu_i\in(0,\infty)\setminus\{1\}\) has no sign restriction on \(\log\mu_i\). Other periodic orbits and equilibria are permitted. The degree counts maximum total Cartesian monomial degree across both vector-field components.

Define the radial polynomial \(F(s)=\prod_{j=1}^m(s-r_j^2)\), where \(s=x^2+y^2\). Fix any
\[
K>\max_{1\le i\le m}\frac{|\log\mu_i|}{2|F'(r_i^2)|r_iT_i}.
\]
For each \(i\), put
\[
 z_i=-\frac{\log\mu_i}{2KF'(r_i^2)r_iT_i},\qquad
 \omega_i=\frac{2\pi}{T_i},\qquad |z_i|<1,
\]
and
\[
 a_i=\omega_i\frac{1+z_i^2}{1-z_i^2},\qquad
 b_i=\frac{2\omega_i z_i}{r_i(1-z_i^2)}.
\]
Let \(A(s)\) and \(B(s)\) be the unique real Lagrange interpolants of degree at most \(m-1\) satisfying \(A(r_i^2)=a_i\), \(B(r_i^2)=b_i\). The claimed field is explicitly
\[
\boxed{\begin{aligned}
\dot x&=KF(x^2+y^2)+y\bigl(A(x^2+y^2)+xB(x^2+y^2)\bigr),\\
\dot y&=-x\bigl(A(x^2+y^2)+xB(x^2+y^2)\bigr).
\end{aligned}}
\tag{1}
\]

## Proof
**1. Invariant circles and physical angular speeds.** For the field (1), the radial identity is exact:
\[
\dot s=2x\dot x+2y\dot y=2KxF(s).
\]
Therefore every \(s=r_i^2\) is invariant. On this circle write \(x=r_i\cos\theta\), \(y=r_i\sin\theta\). Direct differentiation gives
\[
\dot\theta=-\bigl(a_i+r_ib_i\cos\theta\bigr).
\]
The interpolated constants obey
\[
 a_i^2-r_i^2b_i^2=\omega_i^2,
 \qquad a_i>|r_ib_i|.
\]
Thus angular speed is strictly negative everywhere on the full circle; the orbit traverses it exactly once per minimal period. Standard tangent-half-angle integration, or a residue calculation, yields
\[
 T(\Gamma_i)=\int_0^{2\pi}\frac{d\theta}{a_i+r_ib_i\cos\theta}
 =\frac{2\pi}{\sqrt{a_i^2-r_i^2b_i^2}}=T_i.
\]

**2. Exact transverse Floquet multiplier.** Because \(s-r_i^2\) is a regular normal coordinate around \(\Gamma_i\), linearizing the full radial equation (without assuming rotational symmetry) gives
\[
 \dot{\delta s}=2K F'(r_i^2) r_i\cos\theta(t)\,\delta s.
\]
Consequently, the logarithm of its one-period multiplier is
\[
 \Lambda_i=2KF'(r_i^2)r_i
 \int_0^{2\pi}\frac{\cos\theta\,d\theta}{a_i+r_ib_i\cos\theta}.
\]
For \(a>|c|\), use the exact integral identities
\[
 \int_0^{2\pi}\frac{d\theta}{a+c\cos\theta}
 =\frac{2\pi}{\sqrt{a^2-c^2}},\qquad
 \int_0^{2\pi}\frac{\cos\theta\,d\theta}{a+c\cos\theta}
 =\frac{2\pi}{c}\left(1-\frac{a}{\sqrt{a^2-c^2}}\right),
\]
with the second understood by continuity when \(c=0\). With \(a=a_i\) and \(c=r_ib_i\), the chosen parametrization makes the cosine integral exactly \(-T_i z_i\). Hence
\[
 \Lambda_i=-2KF'(r_i^2)r_iT_i z_i=\log\mu_i.
\]
So the actual multiplier is precisely \(\mu_i\). As \(\mu_i\ne1\), each circle is a hyperbolic periodic orbit and therefore an isolated limit cycle. There is no coupling condition between the target data at distinct radii: the interpolation assigns their angular coefficients independently.

**3. Sharp lower bound without a symmetry hypothesis.** Let \((P,Q)\) be any nonzero polynomial planar field of degree \(d\) possessing these \(m\) circles as limit cycles. Its radial polynomial \(R(x,y)=xP(x,y)+yQ(x,y)\) vanishes identically on each circle, so, by divisibility of real polynomials vanishing on a full real circle, \(F(x^2+y^2)\) divides \(R\). This follows iteratively from Euclidean division by the monic polynomial \(y^2+x^2-r_i^2\): the linear remainder in \(y\) vanishes at both branches for every interior \(x\), hence vanishes identically; the distinct factors are coprime.

If \(R\equiv0\), radius is a first integral. Since the required circles are regular periodic orbits, nearby concentric circles also carry nonzero angular speed and are periodic, contradicting their isolation. Hence \(R\not\equiv0\). Write \(R=F(s)L(x,y)\). At \((0,0)\), \(R=0\) but \(F(0)=\prod_j(-r_j^2)\ne0\), so \(L(0,0)=0\). Since \(L\) is nonzero, \(\deg L\ge1\), and
\[
 \deg R\ge2m+1,\qquad \deg R\le d+1,
 \qquad \boxed{d\ge2m}.
\]
For the constructed field (1), \(\deg_sA,\deg_sB\le m-1\), so both Cartesian components have degree at most \(2m\). The \(K F(x^2+y^2)\) term contributes the uncancelled monomial \(Kx^{2m}\) to the first component, while every other term there carries a factor \(y\). Hence the degree is exactly \(2m\), attaining the absolute lower bound.

## Verification
Run `python3 verify.py` with Python, NumPy, SciPy and SymPy. It checks polynomial radial and angular identities exactly using symbolic algebra. It then constructs one-, two-, three-, and four-circle numerical instances (ten specified circles total), independently integrates physical periods and the normal logarithmic multipliers by both quadrature and an ODE, and checks arbitrary, including same-sign, multiplier data. All checks passed for the supplied implementation. Finite tests are supplementary; the proof above establishes the infinite family and the sharp degree bound.

## Relationship to prior work
Jana and Sarkar (2026, Theorem 2.5) give a general form for planar polynomial fields preserving concentric circles, and discuss degree constraints. Their source motivates the question but does not supply the simultaneous arbitrary **numerical Floquet multipliers**, independent periods and sharp-degree construction above. The lower bound \(2m\) for concentric circular limit cycles is classical and is credited to earlier work; the new contribution is realizing all these independent dynamical data at that bound.

Margalef-Bentabol and Peralta-Salas (2015, Theorems 1.2 and 2.1) prove a much broader configuration-realization theorem prescribing periods, multiplicities and qualitative attracting/repelling stability. This does not directly yield independently specified numerical Floquet multipliers at sharp degree \(2m\) for the original circles. The full open preprint was inspected. Giné, Llibre and Valls (2018) prove that two concentric invariant circles cannot both be limit cycles of a cubic polynomial field; this is compatible with the sharp quartic case here.

The published result *An exact orthogonality wall for minimal-degree concentric cycles* studies a degree-\(2m\) field with a **single common affine** angular twist; its Floquet signs alternate (or simultaneously vanish). It does not cover the present radius-dependent interpolated shear with independently chosen multipliers, including the same-sign two-circle case. The published *Sharp polynomial-degree trichotomy for two prescribed circular limit cycles* imposes rotational equivariance, global positive angular speed and exactly two periodic orbits; the present construction does not impose those restrictions, so its higher restricted degree bounds do not dominate this claim.

## Limitations
This theorem does not claim that the prescribed circles are the only periodic trajectories, that any trajectory beyond them is bounded, that the angular speed remains nonzero away from those circles, or that the system has a global attractor. Hyperbolicity excludes unit target multipliers. The theorem concerns finitely many strictly concentric circles; it makes no assertion for nonconcentric configurations or countably many circles. Historical priority is assessed against the inspected literature and published mathematical records, not independently certified. Some specialized older circular-cycle classification sources were only partially accessible, leaving a residual historical-priority risk. The independent mathematical audit remains unperformed.

## References
1. S. Jana and S. Sarkar, *Some remarks on polynomial vector fields in \(\mathbb R^2\)*, arXiv:2610.33226v1, first publicly posted 23 October 2026, https://arxiv.org/abs/2610.33226.
2. J. Margalef-Bentabol and D. Peralta-Salas, *Realization problems for limit cycles of planar polynomial vector fields*, arXiv:1507.00698v1 (2 July 2015), https://arxiv.org/abs/1507.00698, DOI:10.1016/j.jde.2015.10.044.
3. M. V. Dolov and Yu. V. Pavlyuk, *Invariant Algebraic Curves of Polynomial Dynamical Systems*, *Differential Equations* 39 (2003), 1091–1097, DOI:10.1023/B:DIEQ.0000011281.74525.3b.
4. J. Giné, J. Llibre and C. Valls, *The Cubic Polynomial Differential Systems with two Circles as Algebraic Limit Cycles*, *Advanced Nonlinear Studies* 18 (2018), 183–193, DOI:10.1515/ans-2017-6033.
5. J. Llibre, R. Ramírez, V. Ramírez and N. Sadovskaia, *The 16th Hilbert problem restricted to circular algebraic limit cycles*, *Journal of Differential Equations* 260 (2016), 5726–5760, DOI:10.1016/j.jde.2015.12.019 (priority-risk reference; full text not inspected).
