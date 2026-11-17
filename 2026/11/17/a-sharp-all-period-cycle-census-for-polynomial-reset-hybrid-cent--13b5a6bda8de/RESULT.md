# A sharp all-period cycle census for polynomial-reset hybrid centers

## Finding

For every integer \(n\ge 2\), there is a nonempty open set of real polynomial resets of degree \(n\) in a planar two-zone hybrid oscillator for which the number of strictly alternating positive-section points fixed by the \(k\)-th two-half-turn return is **exactly** \(n^{2k}\) for every integer \(k\ge 1\). All these periodic points are simple and have nonneutral return multipliers. The number of distinct cycles with primitive two-half-turn return period \(k\) is
\[
C_{n,k}=\frac1k\sum_{d\mid k}\mu(k/d)n^{2d},
\]
where \(\mu\) is the number-theoretic Möbius function. Their physical flowing time per primitive cycle is \(2\pi k\). The corresponding Artin–Mazur periodic-point zeta function is \(1/(1-n^2z)\).

The count is sharp **simultaneously for every return iterate** within the symmetric centered subclass below: for an arbitrary degree-\(n\) reset, no strict alternating periodic itinerary of two half-turns per return can provide more than \(n^{2k}\) distinct positive-section fixed points of the \(k\)-th return.

An explicit center of the open set is obtained from the degree-\(n\) Chebyshev polynomial \(T_n\), defined by \(T_n(\cos\theta)=\cos(n\theta)\). For every \(\delta>0\), put
\[
f_{n,\delta}(u)=\frac12+\frac{1+\delta}{2}(-1)^{n+1}T_n(2u-1),
\qquad \varphi_{n,\delta}(s)=f_{n,\delta}(-s).
\]
The asserted counts and hyperbolicity hold for this reset and for every sufficiently small perturbation of its polynomial coefficients (with degree preserved).

## Assumptions and scope

The switching line is \(\Sigma=\{(x,y):x=0\}\). In \(x<0\), the vector field is \((\dot x,\dot y)=(-y,x)\), and in \(x>0\), it is \((\dot x,\dot y)=(y,-x)\). At each exit from one half-plane, a hit \((0,s)\) is reset instantaneously to \((0,\varphi(s))\) and the field on the opposite half-plane is attempted, as in the usual hybrid-center convention. Only trajectories with strictly positive heights after every reset are considered; each of their semicircular legs is transverse, lasts exactly \(\pi\) units of original flowing time, and alternates left and right. Switching-line orbits with zero-time retries, grazing, or other itineraries are excluded from the census.

A return section is the positive height \(u>0\) at \((0,u)\) immediately before a left-hand leg. A **full return** consists of a left semicircle, a reset, a right semicircle, and a reset, and has flowing time \(2\pi\). The return function on strict alternating itineraries is \(P(u)=f(f(u))\), where \(f(u)=\varphi(-u)\). A primitive return-\(k\) cycle means the least positive \(k\) satisfying \(P^k(u)=u\), together with the physical hybrid trajectory and its two modes. In particular, this is a count of a specified transverse sector, **not** a global count of all hybrid or Filippov orbits and not a count of regular cycles in the orientation-based terminology of the motivating article.

## Proof

**1. Exact half-flight reduction.** From \((0,u)\), \(u>0\), the left vector field gives \((x(t),y(t))=(-u\sin t,u\cos t)\) for \(0<t<\pi\), reaches \((0,-u)\), and resets to \((0,\varphi(-u))=(0,f(u))\). If \(f(u)>0\), the right vector field follows \((f(u)\sin t,f(u)\cos t)\) for another time \(\pi\), reaches \((0,-f(u))\), and resets to \((0,f(f(u)))\). Thus, on trajectories for which every intermediate height is positive, \(P=f^2\) and \(P^k=f^{2k}\). For any real polynomial reset of exact degree \(n\), \(f^{2k}(u)-u\) has degree \(n^{2k}\); hence it has at most this many distinct real roots and therefore at most this many points of the specified kind.

**2. Strict complete branches.** Write \(J=[0,1]\). The chosen Chebyshev polynomial satisfies \(f_{n,\delta}(0)=-\delta/2<0\), and its other endpoint \(f_{n,\delta}(1)\) is either \(-\delta/2\) or \(1+\delta/2\). Its \(n-1\) interior critical points are all simple, and their critical values alternate strictly between \(-\delta/2\) and \(1+\delta/2\). Therefore each of the \(n\) monotonicity laps crosses the full interval \(J\). More precisely, there are exactly \(n\) pairwise disjoint compact nondegenerate intervals \(I_1,\ldots,I_n\subset(0,1)\) on which \(f_{n,\delta}\) is a homeomorphism onto \(J\), and these intervals are separated by positive gaps. Let \(h_i:J\to I_i\) be its inverse branch.

**3. Exact roots of every iterate.** For a word \(w=(w_1,\ldots,w_m)\) of length \(m\) over \(\{1,\ldots,n\}\), the map \(h_w=h_{w_1}\circ\cdots\circ h_{w_m}\) is a continuous map from \(J\) into a compact subinterval of \((0,1)\), and \(f_{n,\delta}^m\circ h_w\) is the identity on \(J\). Since \(h_w(0)>0\) and \(h_w(1)<1\), the intermediate value theorem supplies \(u_w\in(0,1)\) satisfying \(h_w(u_w)=u_w\), whence \(f_{n,\delta}^m(u_w)=u_w\). Distinct words have disjoint cylinder intervals: at their first differing branch, inverse images lie in distinct \(I_i\), and preceding inverse branches are injective. Hence the \(n^m\) points \(u_w\) are distinct. But the real polynomial \(f_{n,\delta}^m(u)-u\) has degree \(n^m\), so these are **all** its real or complex roots, all are simple, and all lie in \((0,1)\). Moreover, every intermediate iterate of each root lies in \((0,1)\), because the inverse-branch construction gives its full recurrent itinerary. Taking \(m=2k\) proves the sharp full-return count and the positivity and transversality of the underlying hybrid trajectories.

**4. Cycle counts and nonneutral multipliers.** Write \(N_k=n^{2k}\) for the number of points fixed by the \(k\)-th full return. If \(C_{n,d}\) denotes the number of primitive return-\(d\) cycles, then \(N_k=\sum_{d\mid k}d C_{n,d}\). Möbius inversion gives the displayed formula. The zeta identity follows from \(\exp(\sum_{k\ge1}N_kz^k/k)=\exp(-\log(1-n^2z))\). Every root of \(P^k(u)-u\) is simple, so \((P^k)'(u)\ne1\). If \((P^k)'(u)=-1\), then the same point would be a multiple root of \(P^{2k}(u)-u\), contradicting the simplicity proved for \(m=4k\). Thus every primitive cycle has \(|(P^k)'(u)|\ne1\); its itinerary is strictly inside the transverse branch domains, so this is the actual local return multiplier and establishes isolation and hyperbolicity.

**5. Openness in coefficients.** Each critical point of the explicit polynomial is nondegenerate, its endpoints stay strictly outside \(J\), and its critical values have uniform positive separation from both endpoints of \(J\). Under sufficiently small coefficient perturbations, there remain exactly \(n-1\) simple real critical points in \((0,1)\), in the same order, with the same strict alternating side inequalities. The two endpoint inequalities also persist. Consequently all \(n\) strict inverse branches persist, and Steps 3–4 apply to each nearby degree-\(n\) polynomial. Reflection of the argument, \(\varphi(s)=f(-s)\), gives a nonempty open set in the degree-\(n\) polynomial-reset coefficient space. The sharp count holds simultaneously for **all** integers \(k\ge1\), not just any finite list of periods.

## Verification

The analytic proof is complete without computations. The included script `checks/verify.py` uses SymPy exact polynomial arithmetic with rational \(\delta=1/2\) to count all roots in \((0,1)\), using Sturm sequences, for \((n,k)=(2,1),(2,2),(3,1)\): respectively \(4,16,9\). It checks simplicity by polynomial gcd, and tests the Chebyshev endpoint and critical-value margin for degrees two through eight. The script prints `CHEBYSHEV_HYBRID_SHARP_CYCLE_COUNT_CHECK_OK` on success. The symbolic count for finite degrees illustrates, but does **not** prove, the all-degree/all-period theorem. Reproduce with Python 3 and SymPy 1.14 (`python checks/verify.py`).

## Relationship to prior work

Llibre and Santana introduced the two-linear-center polynomial-reset hybrid family and explicitly constructed a quadratic reset with logistic half-return \(f(u)=4u(1-u)\), proving chaos. Their full paper contains the general piecewise-polynomial return representation and an orientation-based uniqueness theorem for degree-one regular cycles, but does not state an all-degree sharp cycle count or an open robust coefficient family saturating every iterate. The present use of Chebyshev polynomials and inverse-branch/word arguments relies on classical polynomial interval dynamics; those standard methods are not claimed as new. The distinct contribution is their exact all-period sharp and open realization in **the physical hybrid-center return**. The previously studied stationary spatial laws and correlations for the quadratic reset concern time statistics rather than this degree-uniform cycle census. Earlier impact-cycle studies with linear resets do not cover the nonlinear reset range here.

## Limitations

The theorem is for concentric unit-frequency linear centers of opposite orientations, one polynomial reset shared by both switching directions, and strict positive alternating two-half-turn itineraries. It neither bounds all nonalternating or grazing hybrid cycles nor establishes global chaotic dynamics for every perturbation outside the invariant symbolic survivor. Its zeta function counts the specified periodic-section points, not arbitrary trajectories. The possible existence of an equivalent construction in literature not indexed by the inspected searches remains a publication-priority risk. No independent external mathematical audit has been performed.

## References

1. J. Llibre and P. Santana, *Limit cycles and chaos in planar hybrid systems*, arXiv:2407.05151, first publicly posted 2024-07-06; see particularly Sections 2, 5–7 and equation (24). https://arxiv.org/abs/2407.05151 . Journal version: *Communications in Nonlinear Science and Numerical Simulation* 140 (2025), article 108382, doi:10.1016/j.cnsns.2024.108382.
2. Z. Li and X. Liu, *Impact limit cycles in the planar piecewise linear hybrid systems*, *Communications in Nonlinear Science and Numerical Simulation* (2023), doi:10.1016/j.cnsns.2022.107074 (linear piecewise reset; bibliographic and abstract comparison only).
3. Classical facts on Chebyshev polynomials, full-branch interval maps, Sturm root counting, and Möbius inversion; elementary ingredients reproved or stated explicitly above.
