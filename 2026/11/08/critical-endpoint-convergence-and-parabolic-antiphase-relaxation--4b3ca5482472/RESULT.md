# Critical-endpoint convergence and parabolic antiphase relaxation on Huygens cycles

## Finding

Let \(n\geq3\) be an integer not divisible by four. For the unweighted repulsive discrete Huygens phase map on the cycle \(C_n\), the endpoint \(h_*=2/\Lambda_n\) of the usual strict Lyapunov interval **is itself a strictly Lyapunov, globally point-convergent step**. Every edge-phase orbit converges to one of finitely many fixed configurations, no orbit has prime period greater than one, and Lebesgue-almost every orbit converges to a uniform twist with \(\cos(2\pi q/n)<0\).

For \(n\equiv2\pmod4\) (hence \(n\geq6\)), \(h_*=1/2\). The all-antiphase configuration \(p=(\pi,\ldots,\pi)\) remains locally asymptotically attracting at that exact endpoint, despite a simple multiplier \(-1\). Its other \(n-2\) edge-quotient multipliers have modulus strictly less than one. For every orbit approaching \(p\) that does not eventually lie on the local strong-stable leaf, take the local lift \(z^{(k)}-p\) and define the alternating amplitude
\[
a_k=\frac1n\sum_{j=0}^{n-1}(-1)^j(z^{(k)}_j-\pi).
\]
Then
\[
\lim_{k\to\infty}k a_k^2=\frac32.
\]
On the exceptional strong-stable leaf and its finite preimages, the convergence after entering a sufficiently small neighbourhood is exponential. At parameters \(h>1/2\), the all-antiphase configuration is linearly unstable; thus \(h=1/2\) is a genuinely attracting nonhyperbolic boundary for this even-cycle family.

## Assumptions and scope

Write \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) and let the phase-difference quotient be
\[
\mathcal Z_n=\{z\in\mathbb T^n:\;\sum_{j=0}^{n-1}z_j\equiv0\pmod{2\pi}\}.
\]
On its tangent space \(E=\{v\in\mathbb R^n:\sum_jv_j=0\}\), let \(K\) be the cycle Laplacian \((Kv)_j=2v_j-v_{j-1}-v_{j+1}\) with cyclic indices. The reduced map and potential are
\[
F_h(z)=z+hK\sin z\pmod{2\pi},\qquad V(z)=\sum_j\cos z_j.
\]
Here \(\sin\) acts coordinatewise. The positive eigenvalues of \(K|_E\) are \(\lambda_j=2-2\cos(2\pi j/n)\), \(1\leq j<n\); the largest is \(\Lambda_n=4\) for even \(n\), and \(\Lambda_n=2+2\cos(\pi/n)\) for odd \(n\). All measure statements concern Haar probability on \(\mathcal Z_n\). The scalar time index \(k\) counts full discrete iterations. The assertion about \(a_k\) is for trajectories approaching the all-antiphase point, not for the other attracting twists.

## Proof

**1. Strict descent survives the spectral endpoint.** Let \(s=\sin z\), \(h=2/\Lambda_n\), and choose a real lift for the increment \(d=hKs\). Taylor's formula with integral remainder and \(\cos t\geq-1\) gives
\[
V(z+d)-V(z)\leq -s^{\mathsf T}d+\frac12\lVert d\rVert^2
=-h s^{\mathsf T}Ks+\frac{h^2}{2}s^{\mathsf T}K^2s\leq0.
\]
The last inequality follows from \(K^2\preceq\Lambda_n K\). The first inequality is **strict if \(d\ne0\)**: in every coordinate with \(d_j\ne0\), the integrand \(-\cos(z_j+t d_j)\) is strictly smaller than one on a set of \(t\in(0,1)\) of positive measure. Thus \(V(F_h(z))<V(z)\) whenever \(Ks\ne0\); equality occurs exactly at the fixed points \(Ks=0\). In particular, there are no nonconstant periodic orbits at the endpoint. This strictness is not supplied by the usual non-strict Lipschitz-gradient bound, whose quadratic coefficient vanishes at \(h=h_*\).

**2. The critical set is finite and nondegenerate.** Since \(\ker K=\operatorname{span}(\mathbf1)\), the critical equation means that all \(\sin z_j\) agree. Each coordinate is consequently \(\alpha\) or \(\pi-\alpha\) modulo \(2\pi\). If \(k\) coordinates take the minority value and \(m=n-k\) the majority, then \(m>k\) when \(4\nmid n\); closure imposes \((m-k)\alpha+k\pi\equiv0\pmod{2\pi}\), which has finitely many solutions. Equal multiplicities would require \(4\mid n\), while \(\cos\alpha=0\) would also require \(4\mid n\). On \(E\), the Hessian of \(V\) is the restriction of the diagonal form \(-\sum_j\cos(z_j)v_j^2\). Its decomposition into the two within-group zero-sum spaces and the one mixed direction has nonzero signs \(\pm\cos\alpha\) and \(\operatorname{sgn}[(m-k)\cos\alpha]\). Therefore every critical point is nondegenerate. Exactly the uniform twists with negative cosine are local minima. This agrees with the explicit classification in Buescu--Oliveira (2026), Theorems 3.1 and 4.2, but the endpoint descent is established independently above.

**3. Every orbit converges, and nonminimal basins are null.** Along an orbit \(z^{(k)}\), the nonnegative continuous drop \(\Delta(z)=V(z)-V(F_hz)\) tends to zero because its sum telescopes against the bounded potential. Its zero set is the finite critical set. Compactness therefore implies \(\operatorname{dist}(z^{(k)},\operatorname{Crit}V)\to0\), and the step increment tends to zero. Choose disjoint small balls around the finitely many critical points; for sufficiently large \(k\), the orbit is inside their union and each step is shorter than their separation. It eventually stays in one ball, and its distance to that ball's critical point tends to zero. Thus every orbit converges to a single fixed point.

At a critical point with a negative Hessian direction, \(DF_h=I-hK_EH\), where \(H\) denotes the intrinsic Euclidean Hessian on \(E\). Because \(K_E\) is positive definite and \(K_EH\) is similar to the symmetric \(K_E^{1/2}HK_E^{1/2}\), that negative direction gives a real multiplier strictly greater than one. A local centre-stable trapping theorem for smooth maps places all nearby forward-trapped points on a Lipschitz graph of codimension at least one, even when other multipliers have modulus one. Finally, the determinant of \(DF_h\) is a nonzero real-analytic function: at \(z=0\) it equals \(\det(I+hK_E)>0\). Hence its zero set is null and inverse images of null sets remain null, by local inverse-function charts. The finite union of global basins of all non-minimal critical points is null. Every other orbit converges to one of the listed uniform twisted minima.

**4. The parabolic antiphase mode.** For \(n\equiv2\pmod4\), \(p\in\mathcal Z_n\), \(h_*=1/2\), and \(K|_E\) has one simple eigenvalue \(4\), with alternating eigenvector \(e_j=(-1)^j\). Its remaining eigenvalues are strictly between zero and four. Since \(\cos p_j=-1\), the quotient Jacobian \(I-K_E/2\) has exactly one multiplier \(-1\) and all others strictly within the unit disk. The strict local minimum \(V(p)=-n\), together with strict global descent and finiteness of the critical set, proves local Lyapunov asymptotic stability by invariant sufficiently small sublevel neighbourhoods.

The exact alternating invariant line \(z_j=\pi+(-1)^j u\) lies in \(\mathcal Z_n\) and obeys
\[
u_{k+1}=u_k-2\sin u_k=-u_k+\frac13u_k^3+O(u_k^5).
\]
For its small nonzero orbits, \(\lvert u_{k+1}\rvert<\lvert u_k\rvert\) and
\[
\frac1{u_{k+1}^2}-\frac1{u_k^2}=\frac23+O(u_k^2),
\]
so Stolz--Cesàro, or summation followed by division by \(k\), yields \(k u_k^2\to3/2\). The invariant line is a local centre manifold. The spectral gap gives a local strong-stable foliation whose leaves shadow unique centre-line orbits at an exponential rate; the leaf of the fixed point itself is codimension one. Thus every attracted orbit outside its eventual preimages has alternating amplitude \(a_k=u_k+O(\rho^k)\) for some \(0<\rho<1\) and obeys the same limit. On the exceptional leaf, all components decay exponentially. When \(h>1/2\), the alternating multiplier \(1-4h<-1\), establishing the stated sharp local instability beyond the endpoint.

## Verification

The accompanying `verify.py` checks the exact scalar Taylor coefficients and reciprocal-square leading increment, the cycle spectral endpoints, pointwise strict potential descent on 1,500 sampled nonstationary quotient configurations, the exact alternating invariant-line update and its long-time coefficient on three even ring sizes, and the stability spectrum for six finite ring sizes. It was executed successfully with output:

`VERIFY_OK exact_scalar_cubic=1 exact_reciprocal_coefficient=1 strict_descent_samples=1500 alternating_invariant_lines=3 critical_amplitude_limits=3 sink_spectra=6`

The universal statement follows from the preceding proof, not from finite sampling. The local foliation and centre-stable trapping arguments invoke standard finite-dimensional invariant-manifold theorems; they are not computer certified.

## Relationship to prior work

Buescu and Oliveira, arXiv:2610.19953v1 (2026), establish the critical-set and sink classification and prove almost-global convergence only for \(0<h<2/\Lambda_n\), not at equality. The underlying network construction in Buescu--D'Aniello--Oliveira, arXiv:2610.10993v1 (2026), likewise uses a strict Lyapunov step interval. The strict-saddle avoidance framework of Schaeffer and McCalla, arXiv:1908.01753v1 (2019), treats measure-zero saddle basins at large admissible steps but does not itself prove endpoint point convergence, classify Huygens-ring basins, or evaluate the parabolic antiphase coefficient. The known cosine-potential geometry and general centre-manifold theory are used as established ingredients, not claimed as discoveries.

## Limitations

The argument excludes \(4\mid n\), where the critical set contains intersecting circles and the finite-critical-set proof is unavailable. The parabolic limit applies only to even cycles congruent to two modulo four and to orbits converging to the all-antiphase point outside the exceptional strong-stable set; it is not a uniform convergence rate for all initial conditions. The result concerns the identical-oscillator, unweighted, noiseless sinusoidal map and the phase quotient, not heterogeneous interactions or robustness under perturbation. The checked novelty is relative to inspected literature; definitive historical priority and independent scientific validation are not established.

## References

1. J. Buescu and H. M. Oliveira, *Almost-global convergence to twisted states in discrete Huygens rings*, arXiv:2610.19953v1, first posted 2026-10-14, https://arxiv.org/abs/2610.19953.
2. J. Buescu, E. D'Aniello, and H. M. Oliveira, *Morse--Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, first posted 2026-10-07, https://arxiv.org/abs/2610.10993.
3. H. Schaeffer and S. G. McCalla, *Extending the step-size restriction for gradient descent to avoid strict saddle points*, arXiv:1908.01753v1, 2019, https://arxiv.org/abs/1908.01753.
