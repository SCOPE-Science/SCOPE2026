# Sharp transverse profile in a cubic two-cycle bifurcation

## Finding
For the cubic vector field
\[
\dot x=ax+y-(ax^2+xy+ay^2)(x+y),\qquad
\dot y=ay-(ax^2+xy+ay^2)(y-x),
\]
there is a sharp local separation law for the second periodic orbit that meets the invariant circle at \(a_0=-1/4\). Put \(\delta=a+1/4\) and orient the polar angle clockwise, \(\phi=-\arg(x+iy)\). For each sufficiently small nonzero \(\delta\), exactly one additional periodic orbit occurs in a common annulus about the unit circle, and its radial graph obeys, uniformly over one turn,
\[
r_a(\phi)=1-\frac{16\pi}{C}\delta E(\phi)+O(\delta^2).
\]
Here the strictly positive, nonconstant periodic function \(E\) and its normalization constant \(C\) are defined by
\[
\Psi_0(\phi)=-\tfrac14-\sin\phi\cos\phi,\quad
G_0(\phi)=\Psi_0(\phi)-\sin^2\phi,\quad
E(\phi)=\exp\!\left(\int_0^\phi\frac{2\Psi_0(s)}{G_0(s)}\,ds\right),
\]
\[
C=\int_0^{2\pi}2\left(\frac{\Psi_0(\phi)}{G_0(\phi)}\right)^2E(\phi)\,d\phi>0,
\qquad E(0)=E(2\pi)=1.
\]
In particular, at the positive horizontal section the exact first-order inverse-square-radius coefficient is
\[
\lim_{a\to-1/4}\frac{r_a(0)^{-2}-1}{a+1/4}=
\frac{32\pi}{C}=3.750745269\ldots.
\]
The circle and companion have transverse multipliers, respectively,
\[
\rho_{\mathrm{circle}}(a)=1-32\pi\delta+O(\delta^2),\qquad
\rho_{\mathrm{comp}}(a)=1+32\pi\delta+O(\delta^2).
\]
Thus the companion is **outside and attracting** for \(\delta<0\), and **inside and repelling** for \(\delta>0\); the invariant circle exchanges stability with it. At \(\delta=0\) the invariant circle has multiplicity exactly two and attracts locally from outside but repels from inside.

## Assumptions and scope
All parameters and coordinates are real. The conclusion applies in some unspecified but fixed open neighborhood of \(a_0=-1/4\), with \(\delta\ne0\) for the companion orbit. Uniqueness refers only to periodic orbits wholly contained in a sufficiently small common tubular annulus about \(x^2+y^2=1\). A local return map is taken on \(\phi=0\), whose positive direction corresponds to forward physical time. Uniform \(O(\delta^2)\) is in the \(C^0\)-norm on \(0\le\phi\le2\pi\); analytic dependence actually gives uniform derivatives of any fixed finite order. No conclusion about global cycle counts outside that annulus is needed.

## Proof
**1. Exact radial and angular reduction.** Write \(x=r\cos\theta\), \(y=r\sin\theta\), \(r>0\). Direct differentiation gives
\[
\dot r=r(1-r^2)(a+\sin\theta\cos\theta),\qquad
\dot\theta=r^2(a+\sin\theta\cos\theta)-\sin^2\theta.
\]
Consequently the unit circle is invariant. Set \(\phi=-\theta\), \(w=r^{-2}-1\), and
\[
\Psi_a(\phi)=a-\sin\phi\cos\phi,\qquad
G_a(\phi)=\Psi_a(\phi)-\sin^2\phi
=a-\tfrac12+\tfrac12(\cos2\phi-\sin2\phi).
\]
Then exactly
\[
\dot w=-2\Psi_a(\phi)w,\qquad
\dot\phi=-\frac{G_a(\phi)-w\sin^2\phi}{1+w},
\]
and therefore
\[
\frac{dw}{d\phi}=
\frac{2\Psi_a(\phi)w(1+w)}{G_a(\phi)-w\sin^2\phi}.
\tag{1}
\]
At \(a_0=-1/4\), \(G_{a_0}\le-3/4+1/\sqrt2<0\). Thus, in a product neighborhood of \((a_0,w=0)\), \(\phi\) is a valid increasing physical-time coordinate. The right side of (1) is real analytic there, periodic in \(\phi\), and its time-\(2\pi\) return map \(P_a(w)\) is analytic in \((a,w)\). It fixes \(w=0\) for every \(a\).

**2. Exact circle multiplier.** Linearizing (1) at \(w=0\) gives \(w'=L_a(\phi)w\), where \(L_a=2\Psi_a/G_a\). The identity
\[
\Psi_a=\frac12G_a+\frac{2a+1}{4}+\frac14G_a'
\]
and the elementary trigonometric integral
\[
\int_0^{2\pi}\frac{d\phi}{G_a(\phi)}
=-\frac{2\pi}{\sqrt{a^2-a-1/4}}
\qquad\bigl(a<(1-\sqrt2)/2\bigr)
\]
prove the *exact* formula
\[
\log P_a'(0)=2\pi-
\frac{\pi(2a+1)}{\sqrt{a^2-a-1/4}}.
\tag{2}
\]
At \(a=a_0\) this is zero, and its derivative with respect to \(a\) is \(-32\pi\). Hence \(P_{a_0}'(0)=1\) and
\[
P_a'(0)=1-32\pi\delta+O(\delta^2).
\tag{3}
\]
The period on the invariant circle at \(a_0\), in original physical time, is \(8\pi\), since \(\int_0^{2\pi}(-G_{a_0})^{-1}d\phi=8\pi\).

**3. A strictly positive second return coefficient.** Expanding the exact rational equation (1) uniformly in \(w\) gives
\[
w'=L_a(\phi)w+B_a(\phi)w^2+O(w^3),\qquad
B_a(\phi)=2\left(\frac{\Psi_a(\phi)}{G_a(\phi)}\right)^2.
\tag{4}
\]
At \(a_0\), let \(E(\phi)=\exp(\int_0^\phi L_{a_0}(s)ds)\). Formula (2) gives \(E(2\pi)=1\). Solving the first- and second-order variational equations in the initial datum \(w(0)\) yields
\[
P_{a_0}(w)=w+Cw^2+O(w^3),\qquad
C=\int_0^{2\pi} B_{a_0}(s)E(s)ds.
\tag{5}
\]
Every factor in the integrand is nonnegative and \(\Psi_{a_0}\) is not identically zero, hence \(C>0\). Therefore the circle has *exactly* double fixed-point multiplicity and is semistable in the sense stated; this is an analytic conclusion, not a finite numerical observation.

**4. Companion branch and full shape.** Analyticity permits factoring \(P_a(w)-w=wH(a,w)\), with
\[
H(a_0,0)=0,\qquad
\partial_a H(a_0,0)=-32\pi,\qquad
\partial_wH(a_0,0)=C>0.
\]
The analytic implicit-function theorem gives a unique nonzero fixed point for every sufficiently small \(\delta\ne0\), with
\[
w_a(0)=\frac{32\pi}{C}\delta+O(\delta^2).
\tag{6}
\]
Smooth dependence of the flow of (1) on initial data and parameter gives, uniformly over \(0\le\phi\le2\pi\),
\[
w_a(\phi)=\frac{32\pi}{C}\delta E(\phi)+O(\delta^2),\qquad
r_a(\phi)=(1+w_a(\phi))^{-1/2}
=1-\frac{16\pi}{C}\delta E(\phi)+O(\delta^2).
\tag{7}
\]
Since \(E>0\), the companion is on the indicated side of the unit circle. Its return multiplier is obtained by differentiating the analytic expansion of \(P_a\) at the nonzero root:
\[
P_a'(w_a(0))=1+32\pi\delta+O(\delta^2).
\tag{8}
\]
Equations (3), (5), and (8) prove the stability and semistability assertions. The monotone angular coordinate ensures that the fixed points yield genuine simple periodic orbits, not spurious roots of a time reparametrization.

## Verification
The included standalone standard-library script `check_branch.py` numerically integrates the exact scalar equation (1) and its two variational equations by fourth-order Runge–Kutta. It reports \(C\approx26.802930538\), \(32\pi/C\approx3.750745269\), checks \(E(2\pi)=1\), and tests the predicted first-order companion sections at two nearby parameters. It reports `CHECK_OK` at the provided tolerances. Separately, straightforward polynomial algebra verifies the polar identities, and differentiating (2) gives exactly \(-32\pi\). These computations are diagnostic only: the existence, positivity, uniqueness and asymptotic orders are established analytically above.

## Relationship to prior work
Gasull and Giacomini (2022 preprint, 2023 journal version, Section 7.1) study this exact cubic system, crediting Gasull–Llibre–Sotomayor (1987) for the two-cycle count and the double invariant circle at \(a=-1/4\). Those qualitative counts and the existence of the unit-circle cycle are **not** claimed as contributions here. The statement established here is the explicit first-order **full radial graph** of the accompanying cycle, its positive integral normalization, the section slope \(32\pi/C\), and the paired sharp transverse-multiplier expansions. The inspected published treatment provides the model and qualitative cycle counts but not these quantitative formulas. General scalar-return-map techniques explain the analytic method but do not by themselves give the benchmark's coefficient or profile.

## Limitations
The result is local near \(a=-1/4\), and does not supply a global explicit expression for the companion orbit, its finite-distance period, or an exact elementary closed form for \(C\). Earlier detailed work from 1987 could not be inspected in full; it may contain related local calculations, leaving a publication-priority risk. Numerical agreement does not certify any theorem. No independent audit has been performed.

## References
1. A. Gasull and H. Giacomini, *Number of limit cycles for planar systems with invariant algebraic curves*, arXiv:2210.15803v1, first posted 2022-10-27, Section 7.1. https://arxiv.org/html/2210.15803v1
2. A. Gasull and H. Giacomini, *Number of Limit Cycles for Planar Systems with Invariant Algebraic Curves*, Qualitative Theory of Dynamical Systems 22, Article 44 (2023), DOI: 10.1007/s12346-023-00746-7. https://link.springer.com/article/10.1007/s12346-023-00746-7
3. A. Gasull, J. Llibre, and J. Sotomayor, *Limit cycles of vector fields of the form \(X(v)=Av+f(v)Bv\)*, Journal of Differential Equations 67 (1987), 90–110. DOI bibliographic index: https://portalrecerca.uab.cat/ca/publications/limit-cycles-of-vector-fields-of-the-form-x-v-av-fvbv/
4. A. Gasull, *From Abel’s differential equations to Hilbert’s 16th problem*, São Paulo Journal of Mathematical Sciences 18 (2024), 1342–1379, DOI: 10.1007/s40863-024-00471-2. https://link.springer.com/article/10.1007/s40863-024-00471-2
