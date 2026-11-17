# Six canonical attracting rhythms and a critical algebraic clock in a three-harmonic phase triad

## Finding
Consider the identical, all-to-all phase oscillator system on \((\mathbb R/2\pi\mathbb Z)^3\)
\[
\dot\theta_j=\Omega+g\sum_{k\ne j}H_{r,s}(\theta_k-\theta_j),\qquad
H_{r,s}(u)=\sin u+r\sin(2u)+s\sin(3u),
\]
where \(g>0\), \(r>0\), \(s>0\) and \(\Omega\in\mathbb R\). Stability throughout means orbital asymptotic stability modulo a common rotation. The six **canonical** relative equilibria are full synchrony, the two opposite equally spaced traveling-wave configurations, and the three assignments of a synchronized pair with the remaining oscillator opposite in phase (pacemakers).

**Theorem.** All six canonical rhythms are exponentially attracting if and only if
\[
 r>\frac32,\qquad \frac{1+2r}{6}<s<\frac{2r-1}{3}.
\]
All six are asymptotically attracting, allowing nonexponential attraction, if and only if
\[
 r>\frac32,\qquad \frac{1+2r}{6}<s\le\frac{2r-1}{3}.
\]
At the included upper boundary \(s=(2r-1)/3\), synchrony and both waves remain exponentially attracting; the three pacemakers are asymptotically but not exponentially attracting. In the invariant two-equal-phases manifold near any pacemaker, write \(u(t)\) for its signed antipodal phase defect. For every sufficiently close nonzero defect,
\[
 \lim_{t\to\infty}t\,u(t)^2=\frac{1}{2g(5r-4)}.
\]
The lower boundary is excluded: the splay configurations have a nonzero, sign-changing cubic term in their local gradient potential, so they are not attractors.

For every parameter in the strict interior, the six hyperbolic rhythms persist as six distinct attracting phase-locked solutions under all sufficiently small positive or negative phase delays \(\alpha\) in the shifted interaction model \(H_{r,s}(\theta_k-\theta_j-\alpha)\). Along each pacemaker continuation, the singled-out phase lag \(\delta(\alpha)\) satisfies \(\delta(0)=\pi\) and
\[
 \delta'(0)=\frac{A-B}{3B},\quad A=1+2r+3s,\quad B=-1+2r-3s.
\]
No assertion is made that these are the only attracting configurations of the phase quotient.

## Assumptions and scope
The model is a finite-dimensional phase-reduced ODE, not the unreduced delayed FitzHugh–Nagumo network. A normalized delay is represented only by a phase shift in the coupling function; the theorem is exact within this phase model. The harmonic interaction is prescribed analytically and is not claimed to be the phase-response convolution of any specific physiological oscillator. A common additive frequency \(\Omega\) does not affect phase differences.

Represent the quotient by \((\theta_2-\theta_1,\theta_3-\theta_1)\in\mathbb T^2\). The canonical relative phase configurations are \((0,0)\), \((2\pi/3,4\pi/3)\), \((4\pi/3,2\pi/3)\), and \((0,\pi)\), \((\pi,0)\), \((\pi,\pi)\). These six are distinct on the quotient. They are relative equilibria for any odd \(H\), including the stated three-harmonic family, because the pair contributions cancel or vanish. All quantitative statements below hold for every \(g>0\) and every \(\Omega\in\mathbb R\).

## Proof
**1. Exact transverse eigenvalues.** Set
\[
 A=H'_{r,s}(0)=1+2r+3s,\qquad
 B=H'_{r,s}(\pi)=-1+2r-3s,\qquad
 C=H'_{r,s}(2\pi/3)=-\tfrac12-r+3s.
\]
At a relative equilibrium, the full phase Jacobian is the weighted graph Laplacian: \(J_{jk}=gH'(\theta_k-\theta_j)\) if \(j\ne k\), and \(J_{jj}=-\sum_{k\ne j}J_{jk}\). One zero eigenvalue is the common-phase direction. The remaining eigenvalues are, respectively,
\[
\begin{array}{ll}
\text{synchrony:}&-3gA,\ -3gA;\\
\text{each traveling wave:}&-3gC,\ -3gC;\\
\text{each pacemaker:}&-g(2A+B),\ -3gB.
\end{array}
\]
For the pacemaker with first two phases equal, the eigenvector separating the pair is \((1,-1,0)\), and the remaining transverse eigenvector is \((1,1,-2)\). The same result applies to both other assignments by permutation. Because \(r,s>0\), we have \(A>0\) and \(2A+B=1+6r+3s>0\). Thus strict attraction of all six is equivalent to \(B>0\) and \(C>0\). These are the two inequalities
\[
 s<\frac{2r-1}{3},\qquad s>\frac{1+2r}{6},
\]
whose simultaneous feasibility is exactly \(r>3/2\). This proves the exponential-attraction classification.

**2. Gradient structure and the upper boundary.** Define the phase-difference potential
\[
 W(\theta)=-\sum_{1\le i<j\le3}\left[\cos(\theta_i-\theta_j)+\frac r2\cos(2(\theta_i-\theta_j))+\frac s3\cos(3(\theta_i-\theta_j))\right].
\]
After removing the uniform rotation \(\Omega\), the vector field is \(-g\nabla W\), hence \(\dot W=-g\|\nabla W\|^2\le0\). Fix \(r>3/2\) and \(s=(2r-1)/3\). Then \(B=0\), \(A=4r\), and \(C=r-3/2>0\). Only the pacemaker's intercluster eigenvalue vanishes. Around \((0,0,\pi)\), write \((\theta_1,\theta_2,\theta_3)=(v/2,-v/2,\pi+u)\). Taylor expansion of the exact potential gives
\[
 W(v,u)-W(0,0)=2r\,v^2+\frac{5r-4}{6}u^4
 +O(|v|^2|u|+|v|^4+|u|^5).
\]
In this expansion the remainder is smaller than the two displayed positive terms in a sufficiently small neighborhood (the \(v^2|u|\) term is absorbed into \(v^2\), and the higher terms into \(u^4\)). The potential therefore has a strict isolated local minimum, despite a zero Hessian eigenvalue. Its gradient descent is locally asymptotically stable: a small sublevel set is forward invariant, and the only critical point in a sufficiently small neighborhood is the origin. The other two pacemakers follow by symmetry. Since the zero eigenvalue persists at the equilibrium, convergence cannot be uniformly exponential there.

On the invariant manifold where the first two phases agree, let \(\delta=\theta_3-\theta_1=\pi+u\). Because \(H\) is odd,
\[
 \dot\delta=2gH(-\delta)-gH(\delta)=-3gH(\delta).
\]
At the critical coefficient,
\[
 H'''(\pi)=10r-8,\qquad
 \dot u=-g(5r-4)u^3+O(u^5).
\]
The cubic coefficient is strictly negative since \(r>3/2\). Every sufficiently small nonzero \(u\) tends monotonically to zero, and differentiation of \(u^{-2}\) gives
\[
 \frac{d}{dt}u^{-2}=2g(5r-4)+O(u^2).
\]
Time averaging proves the exact stated limit. This establishes the algebraic endpoint law and the inclusion of the upper boundary in the asymptotic-attraction classification.

**3. Exclusion of the lower boundary and necessity.** At \(s=(1+2r)/6\), the traveling-wave transverse eigenvalues are both zero. Parametrize a neighborhood of \((0,2\pi/3,4\pi/3)\) by \((0,2\pi/3+u,4\pi/3+v)\). Direct Taylor expansion of the same potential, for \(r>3/2\), has the first nonzero homogeneous term
\[
 W(u,v)-W(0,0)=\frac{\sqrt3(4r-1)}4 uv(u-v)+O((|u|+|v|)^4).
\]
The cubic term changes sign arbitrarily close to the equilibrium. Thus it is not a local minimum of \(W\), and it cannot be an asymptotically stable equilibrium for a gradient descent (nearby points of lower potential cannot converge uphill to it).

If any of the canonical pacemakers is attracting, its transverse eigenvalue \(-3gB\) cannot be positive, so \(B\ge0\). If both traveling waves attract, likewise \(C\ge0\). Together they force \(r\ge3/2\). At \(r=3/2\), the only possible simultaneous nonpositive-eigenvalue parameters have \(s=2/3\), which is precisely the nonattracting splay boundary above. For \(r>3/2\), \(B<0\) or \(C<0\) gives a positive eigenvalue and instability, while \(B=0\) is attracting by part 2 and \(C=0\) is not by the cubic test. This proves the if-and-only-if statement for asymptotic attraction.

**4. Persistence under small nonzero phase shifts.** Inside the strict cone, all six relative equilibria are hyperbolic sinks. The implicit-function theorem continues them uniquely as locally attracting relative equilibria of the shifted phase interaction for sufficiently small \(|\alpha|\). Symmetry fixes the synchronous and the two splay relative configurations. It preserves each two-equal-phase manifold for the pacemakers. On such a manifold the phase lag satisfies
\[
 F(\delta,\alpha)=2H(-\delta-\alpha)-H(-\alpha)-H(\delta-\alpha)=0.
\]
At \((\delta,\alpha)=(\pi,0)\),
\[
 \partial_\delta F=-3B\ne0,\qquad \partial_\alpha F=A-B.
\]
Hence \(\delta'(0)=-(\partial_\alpha F)/(\partial_\delta F)=(A-B)/(3B)\). The continuation of the three pacemakers is distinct and remains attracting by continuity of eigenvalues. There is no corresponding assertion of persistence of the nonhyperbolic boundary states without further analysis.

## Verification
The standalone `verify_triad.py` checks symbolically the three characteristic polynomials, the exact derivative identities, the sign-changing cubic at the lower boundary, and the positive quadratic/quartic terms at the upper boundary. It also tests two rational strict-interior parameter pairs and one rational endpoint. These algebraic computations support but do not replace the analytic gradient argument, the infinite-time limit, or the implicit-function proof. Run with Python 3 and SymPy: `python verify_triad.py`.

## Relationship to prior work
Qie, Pedersen, Song, Liu and Shilnikov (2026) derive the general phase-reduced three-cell network and explore numerical coexistence of synchronous, pacemaker and traveling-wave rhythms. Their numerical phase portraits are not assertions of the present exact coefficient cone, its one-sided attracting boundary, or the sharp algebraic limit. Ashwin, Bick and Burylko (2016) give general symmetry and linear-stability theory for permutation-symmetric phase networks and a two-harmonic classification, including a degeneracy that motivates seeking a third harmonic. Those general tools underpin the elementary linear step here; the remaining claim is an exact three-harmonic six-rhythm coexistence classification including nonlinear boundary behavior and delay continuation. Earlier ring and cluster analyses provide important broad context but are not asserted to lack all possible equivalent formulations. The originality assessment remains provisional pending deeper independent historical review.

## Limitations
The six are the canonical equilibria only: the theorem neither classifies all possible relative equilibria nor excludes further attractors. The assertions apply to the specified positive sine-harmonic weights, identical all-to-all coupling and a phase-reduced ODE. They do not establish the same phenomena in the unreduced delay differential equations, for arbitrary PRCs, or for arbitrary delay. The sharp algebraic constant is proved on the exactly invariant two-equal-phase manifold; generic off-manifold asymptotic coefficients are not claimed. The proof is a self-review and not independent peer validation.

## References
1. X. Qie, M. G. Pedersen, J. Song, S. Liu, A. L. Shilnikov, *Delay-induced multirhythmicity in a 3-cell inhibitory network*, arXiv:2611.06836v1, publicly posted 2026-11-04, https://arxiv.org/html/2611.06836v1 (especially Section II.2, equation (6)).
2. P. Ashwin, C. Bick, O. Burylko, *Identical Phase Oscillator Networks: Bifurcations, Symmetry and Reversibility for Generalized Coupling*, Front. Appl. Math. Stat. **2** (2016), article 7, https://doi.org/10.3389/fams.2016.00007 (Sections 2–4).
3. W. Zou, M. Zhan, *Splay States in a Ring of Coupled Oscillators: From Local to Global Coupling*, SIAM J. Appl. Dyn. Syst. **8** (2009), 1324–1340, https://doi.org/10.1137/09075398X. Only the publicly accessible abstract was inspected; the full text was not available in this review.
4. C.-U. Choe, T. Dahms, P. Hövel, E. Schöll, *Controlling synchrony by delay coupling in networks: From in-phase to splay and cluster states*, Phys. Rev. E **81** (2010), 025205, https://doi.org/10.1103/PhysRevE.81.025205.
