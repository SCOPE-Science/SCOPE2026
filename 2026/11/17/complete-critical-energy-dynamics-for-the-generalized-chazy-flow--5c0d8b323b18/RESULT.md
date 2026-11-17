# Complete critical-energy dynamics for the generalized Chazy flow

## Finding
Consider the generalized Chazy system, with an arbitrary fixed integer \(q\geq2\),
\[
\dot x=y,\qquad \dot y=z,\qquad
\dot z=-|x|^q z-(q+1)\operatorname{sgn}(x)|x|^{q-1}y^2,
\]
where the last coefficient is defined to be zero at \(x=0\). Its first integral is
\[
H(x,y,z)=xz-\frac{y^2}{2}+x|x|^q y.
\]
Every initial condition on the entire critical surface \(H=0\) is an equilibrium or lies on a trajectory explicitly represented by a scalar autonomous equation. For every non-equilibrium critical trajectory: (i) physical-time evolution exists for all positive time and tends to one equilibrium \((x_\infty,0,0)\), retaining the sign of \(x\) except at a possible single tangential zero; (ii) its maximal backward lifespan is finite, and its position diverges at the universal rate
\[
 x(t)\sim\sigma\left(\frac{2q+1}{2q}\right)^{1/q}
(t-t_-)^{-1/q}\quad(t\downarrow t_-),\qquad \sigma\in\{-1,1\};
\]
(iii) convergence to a nonzero terminal equilibrium is exponential with exact rate \(|x_\infty|^q\), whereas convergence to the origin is algebraic with exact law
\[
|x(t)|^{-q}=|x(t_0)|^{-q}+\frac{2q}{2q+1}(t-t_0)
\]
for any nonstationary origin-bound trajectory, evaluated at an instant \(t_0\) with \(x(t_0)\ne0\). In particular \(H=0\) has no nonconstant complete or periodic trajectory.

## Assumptions and scope
Time \(t\) is the original physical time, not a rescaled time. The integer \(q\ge2\) is fixed. The function \(\operatorname{sgn}(x)|x|^{q-1}\) extends locally Lipschitz-continuously to zero for the stated integers, so the three-dimensional initial-value problem is unique. The invariant \(H\), the sign \(\sigma\), and the term 'critical surface' refer exactly to the definitions above; no assertion is made for nonzero values of \(H\) or for the discontinuous case \(q=1\). We use forward time \(t\to+\infty\), and \(t_-\) is the maximal past endpoint of the trajectory.

## Proof
**1. The complete scalar parametrization.** Fix a sign \(\sigma\in\{-1,1\}\), a constant \(c\in\mathbb R\), and a scalar solution \(r(t)\) of
\[
\dot r=u(r),\qquad u(r)=c-\frac{r^{2q+1}}{2q+1}.
\]
The polynomial map
\[
\Phi_\sigma(r,c)=
\left(\sigma r^2,\ 2\sigma r u(r),\
2\sigma\bigl(u(r)^2-r^{2q+1}u(r)\bigr)\right)
\]
sends that scalar solution into \(H=0\). Direct differentiation gives \(\dot x=y\), \(\dot y=z\) and
\[
\dot z=2\sigma\left[-(2q+3)r^{2q}u^2+r^{4q+1}u\right]
=-|x|^qz-(q+1)\operatorname{sgn}(x)|x|^{q-1}y^2.
\]
It also gives \(xz-y^2/2+x|x|^qy=0\) identically, even at \(r=0\).

Conversely let \((x,y,z)\in H^{-1}(0)\). If \(x\ne0\), take \(\sigma=\operatorname{sgn}(x)\), \(r=\sqrt{|x|}\), \(u=y/(2\sigma r)\), and \(c=u+r^{2q+1}/(2q+1)\). The equation \(H=0\) forces exactly the third component of \(\Phi_\sigma(r,c)\). If \(x=0\), then \(H=0\) forces \(y=0\). For \(z\ne0\), choose \(\sigma=\operatorname{sgn}(z)\), \(r=0\), \(c=\sqrt{|z|/2}\); this represents \((0,0,z)\). The remaining point is the origin, an equilibrium. Uniqueness of the original three-dimensional initial-value problem proves that these scalar representatives exhaust every critical trajectory. The two signs of \(c\) at \(r=0\) can represent the same original trajectory and do not create additional solutions.

**2. Forward and backward completeness.** The scalar right-hand side is strictly decreasing, with the unique real root
\[
\rho=\operatorname{sgn}(c)\bigl((2q+1)|c|\bigr)^{1/(2q+1)}.
\]
Every nonstationary \(r\) moves monotonically toward \(\rho\), remains in a bounded interval for forward time, and hence exists for all \(t\ge t_0\). Its image approaches the stationary state \((\sigma\rho^2,0,0)\). For backward time, a solution initially above \(\rho\) increases without bound, while one below decreases without bound. For example above the root, its remaining backward lifespan is the strictly finite integral
\[
t_0-t_-=\int_{r(t_0)}^\infty
\frac{ds}{s^{2q+1}/(2q+1)-c}.
\]
The lower branch has the analogous integral from negative infinity to \(r(t_0)\). Since \(\dot r\sim-r^{2q+1}/(2q+1)\), asymptotic integration gives
\[
|r(t)|^{2q}\sim\frac{2q+1}{2q}\frac1{t-t_-};
\]
squaring and restoring \(x=\sigma r^2\) proves the stated sharp blow-up coefficient. This divergence rules out backward continuation for every nonstationary state.

**3. Two asymptotic forward regimes.** When \(c\ne0\), write \(\lambda=\rho^{2q}>0\). Near \(\rho\), \(\dot r=-\lambda(r-\rho)+O((r-\rho)^2)\), and separation of variables or integration of the logarithmic derivative gives a finite nonzero constant \(K\) with
\[
r(t)-\rho=K e^{-\lambda t}(1+o(1)).
\]
Hence \(x(t)-\sigma\rho^2=2\sigma\rho K e^{-\lambda t}(1+o(1))\), and \(\lambda=|\sigma\rho^2|^q=|x_\infty|^q\) is the sharp position-relaxation exponent. When \(c=0\), solving \(\dot r=-r^{2q+1}/(2q+1)\) gives the exact formula in the Finding section; for any nonstationary origin-bound orbit, \(t^{1/q}|x(t)|\to((2q+1)/(2q))^{1/q}\). A scalar solution can cross \(r=0\) no more than once; at such a crossing \(c\ne0\), the original coordinate \(x=\sigma r^2\) has a strict quadratic tangency with the plane \(x=0\), at \(z=2\sigma c^2\ne0\). Thus the sign \(\sigma\) of every nonstationary orbit is invariant except at its possible one instantaneous touch.

**4. Exhaustion.** If \(r(t_0)=\rho\), the scalar solution is constant and maps to an equilibrium; conversely every equilibrium is of this type. All other critical trajectories have one finite backward endpoint and an equilibrium forward limit, so none is periodic or complete on both temporal directions.

## Verification
A standalone standard-library script `verify_chazy_zero.py` checks the polynomial semiconjugacy identity and the first integral for multiple integers and signs, including exact rational arithmetic at representative points; it also checks the algebraic origin-relaxation formula. Its observed result is `CHAZY_ZERO_ENERGY_ALGEBRAIC_CHECK_OK`. A separate symbolic expansion using exact computer algebra confirmed the full vector-field identities at \(q=2,3,4\). These finite checks support but do not replace the parameter-uniform proof, which is the displayed symbolic differentiation and scalar comparison argument.

## Relationship to prior work
Llibre, Novaes and Valls (2023, arXiv:2307.00087) introduced the exact conserved quantity and proved periodic-cylinder existence for **negative** energy. Their Section 2 and main theorems work on levels \(H=-\omega^2\) with \(\omega>0\); those results are not being claimed anew. Zhuang, Liu and Luo (2024) proved a broader classification of **periodic solutions** for the generalized Chazy family; an abstract was accessible but its full text was not. Earlier Géronimi–Leach–Feix (2001) developed parametric integral methods for symmetry-reduced third-order equations. The present claim is the specific global classification of **every** point of \(H=0\), including singular-plane tangencies, original-time completeness and the two exact relaxation laws; neither the general quadrature method nor the negative-energy periodic-cylinder theorem states this conclusion. Published database searches for the equivalent scalar equation and critical-energy behavior found no direct matching claim, though absence from an index does not prove priority.

## Limitations
This is a self-review, not an independent audit. The claim concerns only the critical first-integral level \(H=0\) for integer \(q\ge2\), not the other energy levels, arbitrary real exponents, or the discontinuous \(q=1\) extension. Some older singularity-analysis papers and the full text of Zhuang–Liu–Luo (2024) could not be compared exhaustively; a not-yet-indexed equivalent critical-level result remains a publication-priority risk. The parametric map is not asserted to be one-to-one.

## References
1. J. Llibre, D. D. Novaes and C. Valls, *Existence of a cylinder foliated by periodic orbits in the generalized Chazy differential equation*, arXiv:2307.00087 (first publicly posted 2023-06-30), https://arxiv.org/abs/2307.00087 .
2. Z. Zhuang, C. Liu and J. Luo, *On the periodic behavior of the generalized Chazy differential equation*, Chaos 34 (2024), 113106, DOI:10.1063/5.0209050 .
3. C. Géronimi, P. G. L. Leach and M. R. Feix, *First integrals and parametric solutions for equations integrable through Lie symmetries*, J. Nonlinear Math. Phys. 8 (2001), 211–216, arXiv:nlin/0104074 .
