# Sharp global angular positivity and punctured-plane attraction in polygonal affine oscillators

## Finding

For the three-parameter polygonal piecewise-affine oscillator family of Kai (2026), there is a **sharp, directly checkable sign criterion** that ensures the prescribed polygon is the globally attracting periodic orbit for **every nonzero initial point of the plane**, not only for a local annulus or a prescribed finite exterior collar. The criterion makes the extra tangential-shear parameters essential rather than cosmetic.

Let \(C\) be a simple counterclockwise polygon with vertices \(p_i\), \(i=1,\ldots,N\), \(N\ge3\), surrounding the origin and star-shaped with respect to it. Successive angular gaps are in \((0,\pi)\). Set

\[
 e_i=p_{i+1}-p_i,\quad \Delta_i=\det(p_i,p_{i+1})>0,\quad n_i=((e_i)_2,-(e_i)_1),\quad V_i(x)=n_i\cdot x-\Delta_i,
\]

with cyclic indices, and consider the sectorwise affine field

\[
 \dot x=(\omega_i-\mu_iV_i(x))e_i-\lambda_iV_i(x)n_i, \qquad
 \lambda_i>0,\ \mu_i\in\mathbb R,\ \omega_i>0.
\]

Define the two endpoint coefficients

\[
 B_i^0=\lambda_i(p_i\cdot e_i)-\mu_i\Delta_i,
 \qquad B_i^1=B_i^0+\lambda_i\|e_i\|^2.
\]

**Theorem.** The angular sector-coordinate derivative is strictly positive at **every** nonzero point in every open sector if and only if, for every \(i\),

\[
 \boxed{ B_i^0\ge0,\qquad \omega_i\ge B_i^1. }
\]

Under this condition, the standard next-sector, no-reset crossing convention defines a unique forward-complete hybrid trajectory from every \(x_0\ne0\), including every point outside \(C\). Every such trajectory has \(C\) as its omega-limit set and converges to it exponentially. In particular, the only periodic orbit in \(\mathbb R^2\setminus\{0\}\) is \(C\); there are no other periodic attractors. Its minimal period and transverse return multiplier are exactly

\[
 \boxed{ T=\sum_{i=1}^N\frac1{\omega_i},\qquad
 \Lambda_C=\exp\!\left(-\sum_{i=1}^N\frac{\lambda_i\|e_i\|^2}{\omega_i}\right). }
\]

For a concrete all-plane example, take the diamond with consecutive vertices \((1,0),(0,1),(-1,0),(0,-1)\), and set \(\lambda_i=1\), \(\mu_i=-2\), \(\omega_i=4\) for every sector. Then \(B_i^0=1\), \(B_i^1=3\); every nonzero state converges to \(\{|x_1|+|x_2|=1\}\), with \(T=1\) and \(\Lambda_C=e^{-2}\).

## Assumptions and scope

The polygon must be radially star-shaped about a **strict interior** origin, with simple nonintersecting edges, positive successive determinants, and consecutive polar gaps less than \(\pi\). The region of mode \(i\) is the open infinite cone spanned by \(p_i,p_{i+1}\). At a radial sector boundary, a path that crosses transversely enters the next sector continuously, without resetting the state. This is the crossing convention used by Kai (2026), not a Filippov sliding definition. Our inequalities ensure such crossing is well-defined everywhere on the punctured plane and eliminate sliding ambiguity there. Initial condition \(x_0=0\) is explicitly excluded.

The **if and only if** concerns the sharp *pointwise property of counterclockwise sector progression throughout the whole punctured plane*, not necessity of those inequalities for asymptotic attraction under arbitrary different switching dynamics. No assertion about globally defined trajectories with other parameters is made.

## Proof

**1. Global radial coordinate and the exact reduced equations.** Inside sector \(i\), uniquely write

\[
 x=r((1-u)p_i+up_{i+1})=rp_i+ru e_i,\qquad r>0,\quad 0<u<1.
\]

The radial gauge \(r\) is continuous through ray crossings: the two adjacent sector formulas both give \(r\) on their common ray. Since \(n_i\cdot p_i=\Delta_i\) and \(n_i\cdot e_i=0\), we have \(V_i(x)=\Delta_i(r-1)\). The elementary decomposition

\[
 n_i=\frac{\|e_i\|^2}{\Delta_i}p_i-
      \frac{p_i\cdot e_i}{\Delta_i}e_i
\]

then yields, exactly and without approximation,

\[
 \boxed{\dot r=-c_i(r-1),\qquad
 r\dot u=\omega_i+(B_i^0+c_i u)(r-1),\qquad
 c_i=\lambda_i\|e_i\|^2>0.}
\]

These equations hold independently of any special coefficient calibration. At a ray crossing the continuous gauge has the same value on both sides.

**2. Sharp global angular-velocity criterion.** Let \(Q_i(r,u)=\omega_i+(B_i^0+c_i u)(r-1)\). Because \(c_i>0\), for \(r\ge1\), \(Q_i\) is minimized over \(0\le u\le1\) at \(u=0\); for \(0<r\le1\), it is minimized at \(u=1\). If \(B_i^0\ge0\) and \(\omega_i\ge B_i^1=B_i^0+c_i\), then

\[
 Q_i(r,u)\ge\begin{cases}
 \omega_i+B_i^1(r-1)\ge B_i^1r>0,&0<r\le1,\\
 \omega_i+B_i^0(r-1)\ge\omega_i>0,&r\ge1.
 \end{cases}
\]

Thus \(\dot u>0\) at every nonzero point, including both one-sided limits at radial boundaries. Conversely, if \(B_i^0<0\), then \(Q_i(r,u)<0\) for all sufficiently large \(r\) at \(u\) sufficiently close to zero. If \(\omega_i<B_i^1\), then \(Q_i(r,u)<0\) for sufficiently small positive \(r\) at \(u\) close to one. Hence both inequalities are necessary; equality cases are included and still strictly positive at each \(r>0\).

**3. Complete crossing flow.** The radial equation never leaves the closed interval between \(r(0)>0\) and \(1\), as follows by integrating each active-sector equation. On that compact positive interval, the angular velocity \(Q_i(r,u)/r\) has uniform strictly positive lower and finite upper bounds over all sectors and \(u\in[0,1]\). Therefore every trajectory exits each visited sector through its forward ray, crosses it transversely, and continues in the next sector; finite-time accumulation of switches is impossible because each full circuit has duration bounded away from zero. Repeated affine solutions give a unique forward solution for all \(t\ge0\).

Writing \(i(t)\) for the sector occupied at time \(t\), the radial equation integrates through every crossing to

\[
 \boxed{r(t)-1=(r(0)-1)
 \exp\left(-\int_0^t c_{i(s)}\,ds\right).}
\]

Let \(c_*:=\min_i c_i>0\) and \(M=\max_{y\in C}\|y\|\). With \(y(t)=x(t)/r(t)\in C\),

\[
 \operatorname{dist}(x(t),C)
 \le M|r(t)-1|
 \le M|r(0)-1|e^{-c_*t}.
\]

Since the angular speed remains bounded above and below by positive constants on the invariant radial interval, the orbit crosses every polygon edge infinitely often. Its omega-limit set is therefore **exactly** \(C\), not just a subset of it.

**4. Unique cycle and Floquet coefficient.** Every periodic crossing orbit must have periodic \(r(t)\). The strictly contracting radial law forces \(r(t)\equiv1\); thus it lies on \(C\). There, \(V_i=0\) and \(\dot x=\omega_i e_i\), so the orbit traverses edge \(i\) in time \(1/\omega_i\). It traverses the whole polygon in the stated period \(T\), showing uniqueness. For the transversal section at any polygon vertex ray, small radial displacements return after a time \(T(r)\to T\) as \(r\to1\). Their linearized return factor is exactly the exponential of minus the sum of \(c_i\) multiplied by the edge residence times \(1/\omega_i\), giving \(\Lambda_C\).

**5. Why genuine tangential shear is essential for this whole-plane criterion.** If every \(\mu_i=0\), then \(B_i^0=\lambda_i p_i\cdot e_i\). However,

\[
 \sum_{i=1}^{N}p_i\cdot e_i
 =-\frac12\sum_{i=1}^{N}\|e_i\|^2<0.
\]

At least one \(p_i\cdot e_i\) is negative, contradicting \(B_i^0\ge0\) for every sector. Therefore this sharp *global positive-traversal* regime is unavailable in the earlier zero-shear subfamily or the calibrated finite-collar construction; some nonzero (indeed negative) tangential-shear coefficient is necessary. For the stated diamond example \(B_i^0=1\), \(B_i^1=3\), and \(c_i=2\) in all four sectors, so its radial law reduces exactly to \(r(t)=1+(r(0)-1)e^{-2t}\).

## Verification

Run `python3 verify.py` (Python standard library only) from a directory containing this package. It performs exact-rational coordinate and vector-field identities in four nonuniform sectors at 80 rational states; checks four distinct sector contraction coefficients, the cyclic polygon dot-product identity, and two exact sign-boundary violations. It also verifies the whole-plane diamond example. The expected successful output is:

`VERIFY_OK exact_sector_states=80 nonuniform_rates=4 square_full_plane=1 sign_boundary_counterexamples=2`

The computation is a finite algebraic consistency test. The all-parameter and all-initial-condition assertions are proved above, not inferred from numerical sampling.

## Relationship to prior work

Kai (2026) introduces the full three-coefficient affine polygon oscillator, proves an attracting polygon in a sufficiently small invariant annulus, and gives the within-sector contraction of the edge function. Its full text explicitly **does not claim global uniqueness**. The present theorem resolves the **entire punctured-plane crossing regime** for a sharp, explicit, nonempty range of shear coefficients, and determines its geometric necessity and dynamics.

Kai (2013, Sec. II) proves uniqueness of a polygonal cycle for the earlier no-shear coefficient family, with all of its coefficients built from a scalar normal feedback and an edge drift. The current all-plane positive-traversal regime requires tangential shear, as Step 5 proves, so it does not follow from this theorem by a parameter substitution. Kai and Masuda (2012) proved synthesis and uniqueness for their earlier family, but the available abstract does not cover the later 2026 shear model. A separate calibrated polygon result establishes full attraction on an explicit interior-and-exterior collar **after a special coefficient calibration**; that calibration has \(B_i^0<0\) on every sector and hence cannot yield the present unbounded global basin. Related exact radial-return results for homogeneous smooth star-node oscillators concern another vector-field class.

## Limitations

The theorem is about the particular piecewise-affine vector fields above, with strictly transverse sector crossing and no state resets. It does not address the origin, Filippov sliding trajectories under other conventions, stochastic perturbations, or whether global attraction remains true when the sharp **everywhere-positive angular velocity** inequalities fail. The 2012 article was accessible only through its abstract; an institutional full-text request could not proceed because the required connection was unavailable. This leaves a residual priority risk, though the 2013 full text and the 2026 full text delineate the earlier zero-shear and later sheared coefficient families. Independent scientific validation has not been performed.

## References

1. T. Kai, *Piecewise affine oscillators with polygonal limit cycles*, International Journal of Dynamics and Control **14**, article 392 (first public 2026-10-08). DOI: 10.1007/s40435-026-02340-6. Full open-access article: https://link.springer.com/article/10.1007/s40435-026-02340-6
2. T. Kai, *Limit Cycle Generation for Multi-Modal and 2-Dimensional Piecewise Affine Control Systems*, International Journal of Advanced Computer Science and Applications **4**(9), 200–206 (2013). DOI: 10.14569/IJACSA.2013.040931. Open-access PDF: https://thesai.org/Downloads/Volume4No9/Paper_31-Limit_Cycle_Generation_for_Multi-Modal.pdf
3. T. Kai and R. Masuda, *Limit cycle synthesis of multi-modal and 2-dimensional piecewise affine systems*, Mathematical and Computer Modelling **55** (2012), 505–516. DOI: 10.1016/j.mcm.2011.08.028.
