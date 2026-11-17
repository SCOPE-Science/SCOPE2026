# Equilibrium flux locking and three-way anticorrelation in a vertical-Hopf chemical oscillator

## Finding
Consider the three-species bimolecular mass-action flow of Banaji, Boros and Hofbauer [1], with positive rate constants and concentrations:
\[
\begin{aligned}
\dot x&=x(\kappa_1z-\kappa_2y),\\
\dot y&=y(\kappa_2x-\kappa_3z),\\
\dot z&=2\kappa_4-z(\kappa_3y+\kappa_1x).
\end{aligned}
\]
Write \((x_*,y_*,z_*)\) for its unique positive equilibrium, namely
\[
z_* =\sqrt{\frac{\kappa_2\kappa_4}{\kappa_1\kappa_3}},\qquad
x_* =\frac{\kappa_3}{\kappa_2}z_*,\qquad
y_* =\frac{\kappa_1}{\kappa_2}z_*.
\]
Let \(\nu\) be **any invariant Borel probability measure with compact support contained in the strictly positive octant**. Write \(\langle f\rangle=\int f\,d\nu\) and
\(r=\langle z\rangle/z_*\). The following assertions hold for all positive rate constants, without assuming the Hopf parameter relation:
\[
\boxed{\langle x\rangle=r x_*,\quad
\langle y\rangle=r y_*,\quad
\langle z\rangle=r z_*,\quad
r\ge1.}
\]
There is an exact nonnegative defect formula
\[
\boxed{\langle z\rangle-z_*=\tfrac12\left\langle\frac{(z-z_*)^2}{z}\right\rangle.}
\]
All three reaction-pair flux averages are **exactly fixed at equilibrium**:
\[
\boxed{\kappa_2\langle xy\rangle=\kappa_1\langle xz\rangle
=\kappa_3\langle yz\rangle=\kappa_4.}
\]
The complete off-diagonal covariance matrix has a single scalar defect:
\[
\boxed{\operatorname{Cov}_\nu(u_i,u_j)
=-(r^2-1)u_{i,*}u_{j,*}\quad (1\le i<j\le3),}
\]
where \((u_1,u_2,u_3)=(x,y,z)\). Equality \(r=1\) holds **if and only if** \(\nu\) is the point mass at the positive equilibrium. Thus each non-equilibrium invariant probability has all three mean concentrations strictly above equilibrium and all three pairwise covariances strictly negative.

In particular, [1, Theorem 1] constructs a family of nonconstant positive periodic orbits when \(\kappa_1=\kappa_2+\kappa_3\). Their uniform **original-physical-time** orbital measures satisfy all strict conclusions, irrespective of orbit amplitude.

## Assumptions and scope
Rates \(\kappa_i>0\), \(i=1,2,3,4\); state space \((0,\infty)^3\); autonomous physical-time flow. The hypothesis is a stationary probability measure whose support is compact *within* that open octant; it can be a periodic-orbit measure, an equilibrium mass, a finite or continuous stationary mixture, or any other compact stationary measure. Compact positive support ensures all test functions below, including coordinate logarithms and reciprocal concentration, are smooth and bounded on a flow neighborhood of the support. No global boundedness assertion is made for arbitrary nonstationary initial conditions, and no claim is made about invariant measures supported on the boundary.

## Proof
**1. Stationary linear-concentration identities.** For a smooth observable \(f\), invariance and compact support imply \(\langle Lf\rangle=0\), where \(L\) is the vector-field derivative. With the two positive-coordinate logarithms,
\[
L\log x=\kappa_1z-\kappa_2y,
\qquad L\log y=\kappa_2x-\kappa_3z.
\]
Consequently \(\langle y\rangle=(\kappa_1/\kappa_2)\langle z\rangle\) and \(\langle x\rangle=(\kappa_3/\kappa_2)\langle z\rangle\), proving the common scale \(r\).

**2. Reciprocal balance and strict mean enhancement.** The third logarithm gives
\[
L\log z=\frac{2\kappa_4}{z}-\kappa_3y-\kappa_1x,
\qquad
\left\langle\frac1z\right\rangle
=\frac{\kappa_1\kappa_3}{\kappa_2\kappa_4}\langle z\rangle
=\frac{\langle z\rangle}{z_*^2}.
\]
Expanding \((z-z_*)^2/z\) and integrating gives
\[
\left\langle\frac{(z-z_*)^2}{z}\right\rangle
=\langle z\rangle-2z_*+z_*^2\left\langle\frac1z\right\rangle
=2(\langle z\rangle-z_*).
\]
Its nonnegative integrand proves \(r\ge1\), with equality precisely when \(z=z_*\) almost surely.

**3. Exact flux locking.** Direct differentiation of the linear observable \(p=x-y+z\) gives the polynomial identity
\[
Lp=2\kappa_4-2\kappa_2xy.
\]
Integration yields \(\kappa_2\langle xy\rangle=\kappa_4\). Stationarity of the first two coordinate functions yields
\[
0=\kappa_1\langle xz\rangle-\kappa_2\langle xy\rangle,
\qquad
0=\kappa_2\langle xy\rangle-\kappa_3\langle yz\rangle,
\]
which proves all three locked fluxes. At equilibrium each pair product is similarly \(x_*y_*=\kappa_4/\kappa_2\), \(x_*z_*=\kappa_4/\kappa_1\), \(y_*z_*=\kappa_4/\kappa_3\). Subtracting the products of means proves the three covariance identities.

**4. Rigidity at zero defect.** Suppose \(r=1\). Then \(z=z_*\) almost surely. By invariance and continuity, for almost every initial point the entire trajectory has \(z(t)=z_*\) for all real \(t\) for which the solution exists (apply invariance first at every rational time, then continuity). Thus \(\dot z=0\) and
\[
\kappa_1x+\kappa_3y=\frac{2\kappa_4}{z_*}\qquad\nu\text{-a.s.}
\]
The flux and mean identities at \(r=1\) give \(\operatorname{Cov}(x,y)=0\). Since \(y\) is an affine decreasing function of \(x\) on the displayed line,
\[
0=\operatorname{Cov}(x,y)=-\frac{\kappa_1}{\kappa_3}\operatorname{Var}(x).
\]
Therefore \(x=x_*\), \(y=y_*\), and \(z=z_*\), almost surely, establishing the equality case. Conversely the equilibrium point mass trivially has \(r=1\). The positive periodic orbits at the critical rates exist by [1, Theorem 1] and are nonconstant compact invariant curves, so their time-average measures have \(r>1\).

## Verification
The standalone `tools/check_identities.py` runs SymPy exact simplification for the equilibrium, the linear flux identity, logarithmic generator identities, and the three equilibrium reaction fluxes. Run from a materialized package with `python tools/check_identities.py` (SymPy dependency). Its successful output is `VERTICAL_HOPF_FLUX_COVARIANCE_SYMBOLIC_OK`. The infinite-measure argument is proved in Sections 1–4 and is not inferred from finite numerical experiments or symbolic algebra alone.

## Relationship to prior work
Banaji, Boros and Hofbauer [1] introduce the exact vector field, establish its unique positive equilibrium, and prove the analytic center surface and periodic orbits at the vertical Hopf condition. Their transformed Hamiltonian and periodicity results are prior work and are not claimed here. The earlier classification [2] establishes the reaction-network and bifurcation context. The contribution here is the **all-positive-rate** invariant-measure fluctuation/flux theorem: universal strict increases of all three physical-time means, fixed mean pair reaction fluxes, and common strictly negative pairwise covariance defect. These statements are not supplied by periodic-orbit existence or equilibrium flux balance alone. Related stationary covariance and flux identities for other oscillator models do not imply identities for this three-species vector field.

## Limitations
The claim covers only compactly supported strictly positive invariant measures. It does not guarantee existence of nonconstant recurrent sets away from the critical Hopf surface, nor global nonstationary boundedness, nor a numerical value for \(r\) on a given orbit. The comparisons with indexed and inspected literature are evidence of possible originality, not a proof of worldwide publication priority. Independent audit has not been performed.

## References
[1] M. Banaji, B. Boros, J. Hofbauer, *The smallest bimolecular mass-action system with a vertical Andronov–Hopf bifurcation*, arXiv:2210.06119v1 (first public 2022-10-12), Theorem 1 and Section 3. https://arxiv.org/abs/2210.06119 . Published in *Applied Mathematics Letters* 143 (2023), article 108671.

[2] M. Banaji, B. Boros, *The smallest bimolecular mass action reaction networks admitting Andronov–Hopf bifurcation*, arXiv:2207.04971 (first public 2022-07-11), Section 8 (exceptional network), https://arxiv.org/abs/2207.04971 .
