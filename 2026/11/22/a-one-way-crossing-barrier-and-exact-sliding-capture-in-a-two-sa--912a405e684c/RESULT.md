# A one-way crossing barrier and exact sliding capture in a two-saddle affine switch

## Finding

Consider the planar piecewise-affine differential system, with its discontinuity on \(\Sigma=\{x=0\}\),
\[
(\dot x,\dot y)=
\begin{cases}
(2x-y+1,\;3x-2y+1),&x<0,\\
(\tfrac12x+y+a,\;x+\tfrac12y+d),&x>0,
\end{cases}
\qquad a,d\in\mathbb R.
\]
Use the Filippov convention on \(\Sigma\). A *crossing periodic orbit* is a nonconstant periodic Filippov trajectory whose intersections with \(\Sigma\) are isolated transverse crossings, with no sliding segment. Then **for every real \(a,d\), there is no crossing periodic orbit**. In fact, any strict transverse passage across \(\Sigma\) has a single parameter-dependent direction: for \(a>-1\), all such passages are from \(x<0\) to \(x>0\); for \(a<-1\), all are in the reverse direction; at \(a=-1\) no strict transverse crossing occurs.

At the natural published parameter point \(a=-5/4\), \(d=-7/4\), put \(\delta=2/\sqrt5\) and \(\varphi=(1+\sqrt5)/2\). The two half-plane level-set arcs joining \(P_+=(0,1+\delta)\) to \(P_-=(0,1-\delta)\) are **both traversed from \(P_+\) to \(P_-\) in positive physical time**. The exact left and right flight times are, respectively,
\[
T_L=6\log\varphi,\qquad T_R=4\log\varphi.
\]
The upper contact is in a repelling Filippov sliding region, while the lower contact is in an attracting sliding region. On its entire attracting sliding component \(\{(0,y):y<1\}\), the Filippov motion has a unique globally attracting pseudoequilibrium
\[
(0,y_*),\qquad y_*=(5-\sqrt{73})/12.
\]
Thus the closed algebraic loop obtained by joining the two arcs is **not a periodic trajectory** under the stated Filippov convention.

## Assumptions and scope

All parameters \(a,d\) are arbitrary real numbers in the general crossing obstruction. Off the switching line each vector field is classical, affine and smooth. The Filippov convexified vector field determines sliding where the one-sided normal components have opposite signs. The exact flight-clock and sliding-equilibrium assertions use only \(a=-5/4\), \(d=-7/4\). Crossing means a strict passage, where both one-sided normal components are nonzero and have the same sign. The theorem does **not** classify periodic motions with sliding segments, nonunique Filippov trajectories at tangencies, or asymptotic dynamics in the entire plane.

## Proof

**1. One-way barrier for the entire two-parameter family.** At \((0,y)\in\Sigma\), the left and right normal speeds are
\[
\nu_L(y)=1-y,\qquad \nu_R(y)=a+y.
\]
For strict left-to-right crossing both must be positive, which is equivalent to \(-a<y<1\), possible only if \(a>-1\). For strict right-to-left crossing both must be negative, equivalent to \(1<y<-a\), possible only if \(a<-1\). These parameter conditions are mutually exclusive. At \(a=-1\), the normal speeds are opposite for all \(y\ne1\), and both vanish at \(y=1\). A periodic trajectory that intersects \(\Sigma\) only in isolated transverse crossings would have to make strict crossings in both directions, which is impossible. A nonconstant periodic orbit contained in either open half-plane is also impossible: the left linearization has eigenvalues \(-1,1\), while the right has eigenvalues \(-1/2,3/2\), so their affine flows are saddle flows without nonconstant periodic trajectories. This proves the crossing-orbit assertion independently of matching level-set equations or of \(d\).

**2. The two oriented algebraic arcs.** At the stated parameter values, the first integrals are
\[
H_L=3x^2+y^2-4xy+2x-2y,\qquad
H_R=(x+y-2)(y-x+1)^3.
\]
Both take equal values at \(P_+\) and \(P_-\). The left flow is diagonalized by \(u=y-x\), \(v=y-3x-2\), with \(\dot u=-u\), \(\dot v=v\). Starting at \(P_+\) gives
\[
 x_L(t)=\tfrac12\big[(1+\delta)e^{-t}+(1-\delta)e^t-2\big].
\]
It first returns to the switching line at \(T_L=\log((1+\delta)/(1-\delta))=6\log\varphi\), reaching \(P_-\). Strict convexity of the bracket, with equal endpoint values, gives \(x_L(t)<0\) throughout \(0<t<T_L\).

For the right flow define \(p=x+y-2\) and \(q=y-x+1\). Then \(\dot p=3p/2\), \(\dot q=-q/2\), and starting at \(P_+\) gives
\[
 x_R(t)=\tfrac12\big[(\delta-1)e^{3t/2}-(2+\delta)e^{-t/2}+3\big].
\]
The first return to \(\Sigma\) occurs at \(T_R=2\log((2+\delta)/(2-\delta))=4\log\varphi\), again at \(P_-\). Indeed \(x_R'(t)\) has exactly one zero before return and starts positive, so \(x_R(t)>0\) on \(0<t<T_R\). Both invariant arcs therefore run from the same upper endpoint toward the same lower endpoint; they cannot be concatenated into a forward-time cycle.

**3. Sliding classification and capture at the benchmark.** On \(\Sigma\), the normal components are \(\nu_L=1-y\), \(\nu_R=y-5/4\). Hence \(y<1\) is attracting sliding, \(1<y<5/4\) is strict right-to-left crossing, and \(y>5/4\) is repelling sliding, aside from the fold endpoints. At \(P_-\), the normals are \(\delta>0\) and \(-1/4-\delta<0\); at \(P_+\) they are \(-\delta<0\) and \(\delta-1/4>0\). This independently excludes a forward-time periodic crossing.

Writing \(q_L(y)=1-2y\) and \(q_R(y)=y/2-7/4\) for the tangential velocities, the standard sliding combination gives
\[
\dot y_s=\frac{-\nu_Rq_L+\nu_Lq_R}{\nu_L-\nu_R}
=\frac{6y^2-5y-2}{9-8y}.
\]
For \(y<1\) the denominator is positive. The numerator has a single root on this half-line, \(y_*=(5-\sqrt{73})/12\), with positive sign for \(y<y_*\) and negative sign for \(y_*<y<1\). Solutions on the attracting sliding component remain there, exist for all forward time, and approach \(y_*\) monotonically. Its tangential linearization is strictly contracting:
\[
\left.\frac{d\dot y_s}{dy}\right|_{y_*}
=-\frac{3\sqrt{73}}{17+2\sqrt{73}}<0.
\]
This establishes the claimed unique, globally attracting sliding pseudoequilibrium *within that component*.

## Verification

The standalone \(\texttt{CHECK.py}\) reconstructs both first integrals and their Lie derivatives symbolically, verifies the saddle eigenvalues, the source parameter transformation, the normal signs, the exact linear-flow formulae, the two golden-ratio flight clocks, the sliding field and its equilibrium/exponent. It also runs finite interior-point diagnostics that both arcs lie in their advertised half-planes. Run using Python 3 with SymPy installed:

```bash
python CHECK.py
```

Expected success marker: \(\texttt{ONE\_WAY\_FILIPPOV\_VERIFY\_OK}\). The universal absence of crossing cycles and the sliding global-attraction statement follow from the preceding exact sign proofs, **not** from finite sampling.

## Relationship to prior work

The model and its polynomial first integrals occur in García, Llibre, Pérez del Río and Pérez-González (2023), Section 4, equations (36)–(38). Their algebraic matching identifies the two displayed contact heights and presents the resulting closed level-set configuration as a limit cycle. Matching first-integral values is a *necessary geometric condition*, but it does not impose the normal-velocity orientations required by a Filippov crossing trajectory. The one-way barrier proves that the configuration is not such a trajectory; this does **not** challenge the separate general upper-bound assertion of at most one cycle.

Llibre and Valls (2021) exclude crossing limit cycles for two *Hamiltonian* affine saddles. That theorem does not apply here because the right vector field has divergence \(1\). Phatangare, Masalkar and Kendre (2024) study *nilpotent centers coupled to linear saddles*, not this pair of noncenter affine saddles. The present conclusion concerns the explicit two-parameter family and its stated Filippov interface, not all discontinuous two-saddle systems.

## Limitations

Only the no-**crossing** conclusion is global in \((a,d)\). The finding does not classify periodic trajectories with sliding or tangencies and does not prove nonexistence of limit cycles throughout the wider classes investigated in the cited papers. The two flight times and the attracting pseudoequilibrium require the specified parameter point. The geometric discrepancy follows from the published equations; priority remains qualified by the possibility of earlier discussions or corrections.

## References

1. B. García, J. Llibre, J. S. Pérez del Río, S. Pérez-González, *Limit Cycles of Polynomially Integrable Piecewise Differential Systems*, **Axioms** 12 (2023), 342. First public publication 2023-03-31. https://doi.org/10.3390/axioms12040342
2. J. Llibre and C. Valls, *Limit Cycles of Planar Piecewise Differential Systems with Linear Hamiltonian Saddles*, **Symmetry** 13 (2021), 1128. https://doi.org/10.3390/sym13071128
3. N. Phatangare, K. Masalkar, S. Kendre, *Limit Cycles of Piecewise Smooth Differential Systems with Nilpotent Center and Linear Saddle*, arXiv:2407.15163 (2024). https://arxiv.org/abs/2407.15163
4. A. F. Filippov, *Differential Equations with Discontinuous Righthand Sides*, Kluwer, 1988.
