# Cubic boundary tomography and logarithmic tangency marks for nonuniform random chords

## Finding

Let \(p:\mathbb R/(2\pi\mathbb Z)\to(0,\infty)\) be a \(C^1\), normalized angular density. Choose four independent circle points \(Z_j=e^{i\Theta_j}\) with \(\Theta_j\) having density \(p\). Intersect the complete lines \(Z_1Z_2\) and \(Z_3Z_4\), obtaining \(X\) almost surely, and let \(C=\{|X|<1\}\). Write \(q_p(x)\) for the **unconditional** planar probability density of \(X\) at interior points. Then, uniformly in \(t\in[0,2\pi)\),
\[
\boxed{\lim_{r\uparrow1}\frac{q_p(re^{it})}{\log(1/(1-r^2))}=16p(t)^3.}
\]
Here \(\Pr(C)=1/3\), for every such \(p\). Thus the near-boundary intersection direction \(T=\arg X\), conditioned on \(C\) and \(1-\varepsilon<|X|<1\), converges in total variation to the angular density
\[
\boxed{\frac{p(t)^3}{\int_0^{2\pi}p(s)^3\,ds}},
\qquad
\boxed{\Pr(1-\varepsilon<|X|<1\mid C)\sim48\varepsilon\log(1/\varepsilon)\int_0^{2\pi}p(s)^3\,ds}.
\]
In particular, this extreme-intersection direction law **uniquely reconstructs** the original sampling law: if the limiting density is \(b\), then \(p(t)=b(t)^{1/3}/\int_0^{2\pi}b(s)^{1/3}\,ds\).

There is also a *marked rare-configuration theorem*. Disintegrate at \(X=re^{it}\), \(0<r<1\). Among the four endpoint labels, let \(J_r\) be the label with largest circular angular distance to \(t\). Let \(S_r\) be that endpoint's angle. The sampled chord *not containing* \(J_r\) has its normal line angle \(M_r\in\mathbb R/(\pi\mathbb Z)\); put \(d_r=\operatorname{dist}_{\mathbb R/(\pi\mathbb Z)}(M_r,t)\in(0,\pi/2]\), \(L_r=\log(1/(1-r^2))\), and
\[
U_r=\frac{2\log(1/d_r)}{L_r}.
\]
For every fixed \(t\), as \(r\uparrow1\), the joint law of \((J_r,S_r,U_r)\) converges in total variation to independent variables: \(J\) uniform on four labels, \(S\) with density \(p\) on the circle, and \(U\sim\mathrm{Uniform}(0,1)\). Thus three endpoints cluster near the observed boundary intersection, while the fourth retains the original sampling distribution and the tangency approach spans a full logarithmic scale.

The formulas concern labelled *independent endpoint pairs* and interior line intersections. Uniform sampling is the special case \(p\equiv1/(2\pi)\), where the known radial dilogarithm formula is recovered; that formula is not asserted as new.

## Assumptions and scope

The unit circle is equipped with angle in radians modulo \(2\pi\); all four angles are independent with the same strictly positive normalized \(C^1\) density \(p\). Supporting lines coincide or are parallel with probability zero. Every supporting-line intersection with \(|X|<1\) is also an intersection of both finite chord segments. The planar density is with respect to Lebesgue area, not polar-radius measure. The conditional law at \(X=re^{it}\) is the regular conditional law defined by the explicit smooth positive interior density. A normal line angle is unoriented modulo \(\pi\), so its distance to \(t\) is well defined.

## Proof

**1. Exact line-coordinate density.** Represent an unoriented line by \((m,h)\in[0,\pi)\times(-1,1)\), meaning \(x\cdot(\cos m,\sin m)=h\). Writing \(v=\arccos h\), its circle endpoints are \(e^{i(m+v)}\) and \(e^{i(m-v)}\). The two ordered parametrizations and their Jacobians give
\[
F_p(m,h)=\frac{4p(m+v)p(m-v)}{\sqrt{1-h^2}}.
\]
For \(p\equiv1/(2\pi)\) this equals \(1/(\pi^2\sqrt{1-h^2})\). For two independent lines with normal angles \(m,n\), the map from intersection position \(x\) to offsets \((h,k)=(x\cdot n_m,x\cdot n_n)\) has absolute Jacobian \(|\sin(m-n)|\). Therefore, for \(|x|<1\),
\[
q_p(x)=16\int_0^\pi\!\int_0^\pi
\frac{|\sin(m-n)|\,p(m+v_m)p(m-v_m)p(n+v_n)p(n-v_n)}{\sqrt{1-(x\cdot n_m)^2}\sqrt{1-(x\cdot n_n)^2}}\,dm\,dn,
\quad v_m=\arccos(x\cdot n_m),\ v_n=\arccos(x\cdot n_n).
\]
This is a complete finite-radius formula and establishes absolute continuity inside the disk.

**2. Singular-endpoint extraction.** By rotating angles, fix the observation direction \(t=0\) and replace \(p\) by \(p_t(s)=p(t+s)\); the bounds below are uniform in \(t\) by compactness. Let \(\delta=1-r^2\), \(L=\log(1/\delta)\), and
\[
G_r(m)=\frac{4p_t(m+\arccos(r\cos m))p_t(m-\arccos(r\cos m))}{\sqrt{1-r^2\cos^2m}}.
\]
Then \(q_p(re^{it})=\iint|\sin(m-n)|G_r(m)G_r(n)\,dm\,dn\). For each \(m\in(0,\pi)\),
\[
G_r(m)\longrightarrow \frac{4p(t)p(t+2m)}{\sin m},
\quad \sin m\,G_r(m)\longrightarrow 4p(t)p(t+2m).
\]
The last convergence is dominated in \(L^1(0,\pi)\), since \(\sin m/\sqrt{\delta+r^2\sin^2m}\le 1/r\). Moreover, on the angular circle \(\mathbb R/(\pi\mathbb Z)\),
\[
\frac{G_r(m)\,dm}{L}\ \Longrightarrow\ 4p(t)^2\delta_0(dm),
\qquad \int_0^\pi\sin m\,G_r(m)\,dm\to 2p(t).
\]
Indeed \(\int_0^\pi(\delta+r^2\sin^2m)^{-1/2}dm=L+O(1)\), and the numerator approaches \(4p(t)^2\) uniformly within a sufficiently small circular neighborhood of zero.

To use the logarithmically divergent weak limit without double-counting, split both integrations into a circular \(\eta\)-neighborhood \(A_\eta\) of zero and its complement. The complement-complement term is \(O_\eta(1)\). Both mixed terms give, after division by \(L\),
\[
2\cdot4p(t)^2\int_{A_\eta^c}\sin n\,\frac{4p(t)p(t+2n)}{\sin n}\,dn.
\]
The double-near term is \(O(\eta L)\): use \(|\sin(m-n)|\le\operatorname{dist}_\pi(m,0)+\operatorname{dist}_\pi(n,0)\), \(\int_{A_\eta}\operatorname{dist}_\pi(m,0)G_r(m)dm=O(\eta)\), and \(\int_{A_\eta}G_r=O(L)\). Letting first \(r\uparrow1\), then \(\eta\downarrow0\), and using \(\int_0^\pi p(t+2n)dn=1/2\), yields the coefficient \(2\cdot4p(t)^2\cdot2p(t)=16p(t)^3\). Uniformity in \(t\) follows from the common modulus of continuity and positive lower bound for \(p\).

**3. Boundary angle law and inverse reconstruction.** Conditional on the cyclic order of four independent continuously distributed endpoints, exactly one of the three possible pairings crosses, hence \(\Pr(C)=1/3\). Polar integration of the uniformly valid spatial asymptotic yields
\(\Pr(1-\varepsilon<|X|<1,\arg X\in dt)=16p(t)^3\varepsilon\log(1/\varepsilon)(1+o(1))dt\).
Division by \(1/3\) gives the probability and limiting density displayed above; uniformity implies total-variation convergence. The cube-root reconstruction follows by normalization.

**4. Marked tangency.** The mixed terms in Step 2 have an explicit asymptotic interpretation. In one of the two interchangeable chords, its normal approaches \(t\) modulo \(\pi\), with transverse angular offset \(z\) carrying asymptotic density proportional to \(dz/|z|\) over \(\sqrt\delta\ll |z|\ll1\). The other chord has one endpoint tending to \(t\) and the other endpoint tending to angle \(s\) with weight \(p(s)ds\); its normal contributes a factor \(|\sin(m-n)|\) which cancels the reciprocal sine in the line density. Each choice of the near-tangent chord and of the isolated label within the other chord has the same leading weight, yielding four equally likely isolated labels. Setting \(u=2\log(1/|z|)/L\) gives \(dz/|z|=(L/2)du\) on either side of the angular singularity. Thus for any fixed isolated label, any \(s\) away from \(t\), and \(0<u<1\), the normalized joint density converges pointwise to \(\tfrac14p(s)\), with independent Lebesgue-uniform \(u\). All mass lies in these four sectors because the double-near contribution is \(o(L)\), the complement-complement term is \(O(1)\), and the \(u\)-ranges outside \((0,1)\) carry \(o(L)\). Density normalization plus Scheffé's lemma establishes total variation for \((J_r,S_r,U_r)\). This also proves that the three nonisolated endpoints approach \(t\) in probability.

## Verification

The accompanying `CHECK.py` evaluates the exact two-angle integral by periodic FFT convolution. For constant \(p\), it checks the independent published identity \(q_p(re^{it})=-2\log(1-r^2)/(\pi^3r^2)\) across five radii. For positive anisotropic \(p(t)=(1+0.5\cos t)/(2\pi)\), it computes the ratio to the derived cubic boundary leading term at three angular directions and three radii, confirming convergence in the expected direction. The checker also confirms the exact \(1/3\) crossing combinatorics by counting the three pairings of each cyclically sorted quadruple. Numerical quadrature is an illustration and not a replacement for the limiting argument above.

## Relationship to prior work

Poonen–Rubinstein (first public preprint August 2, 1995; primary MSC 51M04) classify interior diagonal incidences for regular polygons rather than sampling from nonuniform circle densities. Karamata (1962) and the later Bortolotto–Souza 2025/2026 work determine the circularly symmetric dilogarithmic *radial* intersection law. The latter source's full arXiv paper was checked, including its Theorem 1 and the proof of the radial formula; it does not provide the density-dependent local cubic angular law, cube-root sampling reconstruction, or the four-label logarithmic tangency mark. Bortolotto–Ramos (2025) consider optimization over arbitrary circle sampling measures and give nonsharp global boundary estimates; their stated theorems do not determine a local \(16p(t)^3\) coefficient for fixed smooth densities. The 2019 Barahona Torres–Manrique-Mirón–Treviño-Aguilar angle result concerns a chord from two *disk-interior* points and a separate randomly positioned horizontal chord, not the present endpoint sampling or boundary marks. A 1964 David–Fix paper is close historically but full material could not be inspected; the nonuniform marked claim therefore retains historical priority risk.

## Limitations

The theorem assumes a shared strictly positive \(C^1\) angular density and independent endpoints; it does not cover singular measures, densities vanishing at observation directions, noncircular boundaries, or dependent chord endpoints. The marked total-variation limit is a regular conditional limit at a fixed interior point approaching the boundary; it is not a finite-radius exact factorization. Only this theorem and its corollaries are asserted, not the previously known uniform radial law or polygon incidence formula. Independent validation and definitive priority assessment are not claimed.

## References

- Bjorn Poonen and Michael Rubinstein, *The Number of Intersection Points Made by the Diagonals of a Regular Polygon*, arXiv:math/9508209v1 (first public August 2, 1995), SIAM J. Discrete Math. 11 (1998), 135–156. Primary MSC 51M04.
- Cynthia Bortolotto and Victor Souza, *Intersections of random chords of a circle*, arXiv:2504.12866v1 (April 17, 2025); American Mathematical Monthly 133 (2026), 661–680.
- Cynthia Bortolotto and João P. G. Ramos, *On extremal problems associated with random chords on a circle*, Mathematika 71 (2025), e70024, doi:10.1112/mtk.70024.
- J. I. H. Barahona Torres, P. C. Manrique-Mirón and E. Treviño-Aguilar, *Angle distribution of two random chords in the disc: A sine law*, arXiv:1911.05576 (November 13, 2019).
- F. N. David and Evelyn Fix, *Intersections of random chords of a circle*, Biometrika 51 (1964), 373–379, doi:10.1093/biomet/51.3-4.373 (full text unavailable in this review).
