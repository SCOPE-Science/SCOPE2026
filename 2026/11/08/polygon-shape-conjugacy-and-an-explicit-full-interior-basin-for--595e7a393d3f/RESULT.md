# Polygon-shape conjugacy and an explicit full-interior basin for calibrated affine oscillators

## Finding

A single explicit calibration of the normal and tangential coefficients of the polygonal piecewise-affine oscillator makes its entire transient dynamics independent of the shape of the prescribed polygon. For every admissible star-shaped polygon with the same number of vertices, the calibrated systems are time-preservingly conjugate on a forward-invariant radial domain that contains the **entire punctured polygon interior** and an explicit exterior collar.

More precisely, let \(N\geq3\), \(a>0\), and ordered positive speeds \(\omega_i>a/2\) be fixed. Let \(C\) be a simple counterclockwise polygon with vertices \(p_0,\ldots,p_{N-1}\), strictly containing the origin and star-shaped with respect to it, with successive ray-angle gaps strictly between zero and \(\pi\). Indices are cyclic. Set

\[
 e_i=p_{i+1}-p_i,\quad \Delta_i=\det(p_i,p_{i+1})>0,\quad
 L_i^2=\|e_i\|^2,\quad n_i=((e_i)_2,-(e_i)_1),
\]
\[
 V_i(x)=n_i\cdot x-\Delta_i,\quad
 \lambda_i=\frac{a}{L_i^2},\quad
 \mu_i=\frac{a}{\Delta_i}\left(\frac{p_i\cdot e_i}{L_i^2}+\frac12\right).
\]

On the open sector between the rays through \(p_i\) and \(p_{i+1}\), consider the affine differential equation

\[
 \dot x=(\omega_i-\mu_i V_i(x))e_i-\lambda_i V_i(x)n_i.
\]

The solution is continued at a transverse ray crossing in the next sector, with no reset. Every nonzero point in a sector has unique coordinates

\[
 x=r\big((1-u)p_i+up_{i+1}\big),\qquad r>0,\quad 0\leq u\leq1.
\]

The radius \(r\) is the continuous polygonal radial gauge. In the calibrated system its exact equations are

\[
 \boxed{\dot r=-a(r-1),\qquad
 \dot u=\frac{\omega_i+a(u-1/2)(r-1)}{r}.}
\]

Write \(R=1+2\min_i\omega_i/a\). The set \(\mathcal A_C=\{x:0<r(x)<R\}\) is forward invariant. Every initial state there has a unique, globally defined forward hybrid trajectory crossing successive rays counterclockwise, and

\[
 \boxed{r(t)=1+(r(0)-1)e^{-at}.}
\]

Consequently every such trajectory tends to \(C\) exponentially in distance, and \(C\) is the **only periodic orbit** in \(\mathcal A_C\). The cycle has period \(T=\sum_i1/\omega_i\) and nontrivial transverse return multiplier \(\exp(-aT)\).

For two polygons \(C\) and \(\widetilde C\) satisfying the hypotheses with the same \(N,a\), and ordered \(\omega_i\), the sectorwise map

\[
 \boxed{\Phi\!\left(r((1-u)p_i+up_{i+1})\right)
 =r((1-u)\widetilde p_i+u\widetilde p_{i+1})}
\]

is a time-preserving topological conjugacy between the hybrid flows on their respective \(\mathcal A\)-domains. Thus not only the asymptotic period but also the complete sequence of switching times and radial transients is polygon-shape invariant.

## Assumptions and scope

The polygon is simple, radially star-shaped around the strict interior origin, has no coincident consecutive vertices, and its successive polar gaps belong to \((0,\pi)\). Accordingly every radial ray intersects its boundary once, and \(\Delta_i>0\). The scalar \(a\) is constant across modes; the ordered \(\omega_i\) are fixed and each strictly exceeds \(a/2\). The coefficients \(\lambda_i>0\) and \(\mu_i\in\mathbb R\) are prescribed exactly above. The system is interpreted as a switched Carathéodory/hybrid flow with the next-sector convention at rays; it is not asserted to be a continuous vector field at ray boundaries or at the origin.

The invariant domain \(\mathcal A_C\) excludes the origin but contains all points of the polygonal interior other than the origin, the cycle itself, and an explicit homothetic exterior collar. No assertion about solutions outside this domain or about their global attractors is made.

## Proof

**Step 1: radial-coordinate reduction.** The vectors \(p_i,e_i\) are a basis because \(\Delta_i>0\). In its sector write \(x=rp_i+be_i\) with \(b=ru\). The normal vector satisfies

\[
 n_i\cdot p_i=\Delta_i,\qquad n_i\cdot e_i=0,
 \qquad \|n_i\|^2=L_i^2,
\]

and therefore \(V_i(x)=\Delta_i(r-1)\). As a vector identity,

\[
 n_i=\frac{L_i^2}{\Delta_i}p_i-
 \frac{p_i\cdot e_i}{\Delta_i}e_i.
\]

Substitute into the affine field, using the selected \(\lambda_i,\mu_i\). The coefficient of \(p_i\) is \(-a(r-1)\); the coefficient of \(e_i\) is \(\omega_i-a(r-1)/2\). Hence

\[
 \dot r=-a(r-1),\qquad
 \dot b=\omega_i-\frac a2(r-1).
\]

Differentiating \(b=ru\) gives the claimed \(\dot u\). This calculation is valid on each open sector and the radial gauge remains continuous at ray switches, so the same radial ODE persists across all switches.

**Step 2: positive switching and global solutions.** For \(0<r\leq1\) and \(0\leq u\leq1\),

\[
 \omega_i+a(u-1/2)(r-1)\geq\omega_i-a(1-r)/2>0.
\]

For \(1\leq r<R\), the corresponding lower bound is \(\omega_i-a(r-1)/2>0\). Thus \(\dot u>0\) throughout \(\mathcal A_C\). A hit at \(u=1\) is immediately continued as \(u=0\) in the next sector. Its two one-sided angular crossing speeds are positive, so the crossing is transversal. The radial solution is explicit and remains in a compact subinterval of \((0,R)\) depending on the initial radius. On each such radial compact set the angular speeds have positive lower and finite upper bounds. Consequently the trajectory cannot stall or undergo infinitely many switches in finite time: each full traversal requires positive elapsed time, and the solution exists uniquely for all positive times. The radial formula also proves forward invariance.

For an incoming ray state with \(u(0)=0\) and \(s=r(0)-1\), integration of \(\dot b\) shows that the sector exit time \(\tau>0\) is the unique solution of

\[
 \boxed{\omega_i\tau=1+\frac s2(1+e^{-a\tau}),\qquad
 s_{\mathrm{next}}=se^{-a\tau}.}
\]

Indeed the difference between left and right sides has derivative \(\omega_i+(as/2)e^{-a\tau}>0\) for \(-1<s<R-1\), starts negative and diverges to positive infinity. The event equation is shape-free.

**Step 3: limit set and multiplier.** Set \(M=\max_{y\in C}\|y\|\). For a point \(x(t)=r(t)y(t)\) with \(y(t)\in C\),

\[
 \operatorname{dist}(x(t),C)\leq\|x(t)-y(t)\|
 \leq M|r(0)-1|e^{-at}.
\]

A periodic orbit requires \(r(t)\) periodic; the scalar ODE forces \(r\equiv1\). On \(r=1\) the angular-coordinate speed in sector \(i\) is precisely \(\omega_i\), so the polygon itself is one periodic orbit with minimal period \(T=\sum_i1/\omega_i\), and there are no other periodic orbits in the domain. On the ray section \(u=0\), the first-return radial map has the form \(r\mapsto1+(r-1)e^{-aT(r)}\) with continuous \(T(r)\) and \(T(1)=T\). Its derivative at \(r=1\) is \(e^{-aT}\), giving the transverse multiplier.

**Step 4: shape conjugacy.** Each radial sector of either polygon is parametrized uniquely by the same pair \((r,u)\), with the vertex identification \((i,1)=(i+1,0)\). This yields a homeomorphism \(\Phi\), whose inverse swaps the polygons. The reduced differential equations, switching convention, and radial domain \(0<r<R\) depend only on \(a\) and the ordered speeds, not the vertices. Both sides therefore produce identical \((r(t),i(t),u(t))\) for every initial coordinate and every time. Hence \(\Phi\circ\varphi_t=\widetilde\varphi_t\circ\Phi\) for all \(t\geq0\). This establishes time-preserving conjugacy, not merely orbit equivalence.

**A boundary qualification.** The bound \(R\) is the supremum of radii for which angular-coordinate velocity is strictly positive for every phase and mode: at any \(r>R\), choose a mode achieving \(\min\omega_i\) and \(u=0\); the numerator of \(\dot u\) is negative. This is a sharp **uniform positive-traversal** cutoff, not a claim that every trajectory outside \(\mathcal A_C\) fails to approach the polygon.

## Verification

The standalone program `verify.py` executes exact symbolic identities via SymPy and integrates the original two-dimensional affine vector fields for two geometrically distinct five-vertex polygons. It compares sector trajectories against the independent radial/axial formulas, checks ray-exit times, and verifies one full return at several interior and exterior radii. A successful execution with the documented dependencies reports:

`VERIFY_OK symbolic_vector_identity=True local_ode_checks=1280 full_cycle_step_checks=50 polygon_shapes=2 forward_radius=3.25 shape_invariant_event_times=True`

The finite numerical tests are corroboration only; Steps 1–4 are the proof for all admissible polygons and parameters.

## Relationship to prior work

Kai (2026) introduces the three-parameter polygonal affine family, proves existence and local attraction of its prescribed cycle, and obtains within-sector normal contraction. That paper supplies the **model**, not the radial calibration or the asserted full punctured-interior basin and shape-independent time-preserving conjugacy. Its proof explicitly limits the general stability theorem to a small invariant annulus and does not claim global uniqueness. Earlier Kai/Masuda work, including Kai (2013) and Kai/Chiku/Maehara (2019), establishes synthesis and uniqueness for earlier coefficient families. Accordingly, generic polygonal cycle synthesis and generic uniqueness are **not** claimed as contributions here. The new statement is the specific simultaneous coefficient tuning giving an exact, globally shared radial-and-angular law, a provable large basin, and an explicit switching map. A related published result for smooth contracting star-node cycles gives exact radial returns and Floquet exponents for a different homogeneous planar flow; it does not cover this piecewise-affine polygon class.

## Limitations

The conclusion is confined to simple origin-star-shaped planar polygons with strictly positive consecutive determinants, the specific calibrated coefficients, and \(\omega_i>a/2\). It does not prove basin maximality beyond \(r=R\), existence of a classical smooth flow at vertices or the origin, extension to non-star-shaped curves, or phase-conjugacy when the ordered modal speeds differ. The accessible 2026 source and earlier 2013 primary text were inspected. Full texts of the closely related 2012 synthesis paper and 2019 conference paper were not accessible through the available open/institutional routes; this leaves a historical-priority risk, although their documented earlier coefficient families predate the additional tangential parameter introduced in 2026. Independent mathematical assessment has not been performed.

## References

1. T. Kai, *Piecewise affine oscillators with polygonal limit cycles*, International Journal of Dynamics and Control **14**, article 392 (first public 2026-10-08). DOI: 10.1007/s40435-026-02340-6. Full open-access text: https://link.springer.com/article/10.1007/s40435-026-02340-6
2. T. Kai, *Limit Cycle Generation for Multi-Modal and 2-Dimensional Piecewise Affine Control Systems*, International Journal of Advanced Computer Science and Applications **4**(9), 200–206 (2013). Full issue: https://thesai.org/Downloads/IJACSA_Volume4No9.pdf
3. T. Kai and R. Masuda, *Limit cycle synthesis of multi-modal and 2-dimensional piecewise affine systems*, Mathematical and Computer Modelling **55** (2012), 505–516. DOI: 10.1016/j.mcm.2011.08.028.
4. T. Kai, S. Chiku, and K. Maehara, *Derivation and mathematical analysis of piecewise affine oscillators with desired polygonal limit cycles*, European Control Conference (2019), 2632–2637. DOI: 10.23919/ECC.2019.8795666.
