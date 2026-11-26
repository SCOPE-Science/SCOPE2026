# A lag-independent first integral and exact elliptic periods for a four-oscillator ring

## Finding
For four identical, nearest-neighbor sinusoidally coupled phase oscillators on a cycle, a nonconstant, explicitly defined ratio of sines is conserved for **every** real phase lag. At the critical quadrature lag, its regular levels give a complete family of genuinely periodic four-phase trajectories with a closed elliptic-integral period; the common phase undergoes **zero net drift**. The period is strictly decreasing in the absolute value of the invariant product and has an explicit logarithmic divergence at its separatrix.

For every choice of phase lifts for which the denominator does not vanish, the first integral is
\[
J=\frac{\sin((\theta_3-\theta_1)/2)\sin((\theta_4-\theta_2)/2)}{\sin((\theta_2+\theta_4-\theta_1-\theta_3)/2)}.
\]
At lag \(\alpha=\pi/2\), set \(\phi=(\theta_2+\theta_4-\theta_1-\theta_3)/2\) and \(p=\sin((\theta_3-\theta_1)/2)\sin((\theta_4-\theta_2)/2)\). If \(\sin\phi\ne0\) and \(0<|p|<1\), the original four-oscillator trajectory is periodic with **minimal** period
\[
T(p,\phi)=\frac{2}{|\sin\phi|}\,K\!\left(\sqrt{1-p^2}\right)
=\frac{\pi}{|\sin\phi|\operatorname{AGM}(1,|p|)}.
\]
Here \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2 s)^{-1/2}\,ds\). Its exact boundary laws are
\[
\lim_{|p|\uparrow1}T(p,\phi)=\frac{\pi}{|\sin\phi|},\qquad
T(p,\phi)=\frac{2}{|\sin\phi|}\log\frac4{|p|}+o(1)\quad(|p|\downarrow0),
\]
for fixed \(\sin\phi\ne0\). The limiting first expression is the small-amplitude period; the \(|p|=1\) configuration itself is fixed, not a nonconstant periodic solution.

## Assumptions and scope
The phase-space is the torus \((\mathbb R/2\pi\mathbb Z)^4\), and for each \(j\in\{1,2,3,4\}\), cyclic indices are used in
\[
\dot\theta_j=\sin(\theta_{j-1}-\theta_j+\alpha)+\sin(\theta_{j+1}-\theta_j+\alpha).
\]
The coupling amplitude is normalized to one; rescaling it by a positive constant divides the stated periods by that constant. The first-integral theorem holds for all real \(\alpha\), on the open invariant set where its denominator does not vanish. The exact-period theorem requires \(\alpha=\pi/2\), \(\sin\phi\ne0\) and \(0<|p|<1\), where the phase lifts are chosen continuously along the trajectory. Changing any lift by a multiple of \(2\pi\) leaves \(J\) unchanged, while \(|p|\) and \(|\sin\phi|\) are intrinsically defined. No assertion of globally defined \(J\) is made on its denominator-zero invariant set.

## Proof
**1. Exact coordinates.** For continuous real lifts put
\[
A=(\theta_1+\theta_3)/2,\quad B=(\theta_2+\theta_4)/2,\quad
u=(\theta_3-\theta_1)/2,\quad v=(\theta_4-\theta_2)/2,\quad\phi=B-A.
\]
Then \((\theta_1,\theta_3)=(A-u,A+u)\) and \((\theta_2,\theta_4)=(B-v,B+v)\), and direct trigonometric addition gives the **exact**, untruncated equations
\[
\begin{aligned}
\dot A&=2\cos u\cos v\sin(\phi+\alpha),&
\dot B&=2\cos u\cos v\sin(\alpha-\phi),\\
\dot u&=-2\cos v\cos(\phi+\alpha)\sin u,&
\dot v&=-2\cos u\cos(\alpha-\phi)\sin v,\\
\dot\phi&=-4\cos\alpha\cos u\cos v\sin\phi.
\end{aligned}
\]
The \(\sin\phi=0\) set is invariant. Any initial \(\sin\phi\ne0\) stays off it at each finite time, since \(\dot\phi\) is proportional to \(\sin\phi\) with bounded coefficient.

**2. First-integral identity.** Direct differentiation, valid even at \(\sin u\sin v=0\), shows
\[
\frac{d}{dt}(\sin u\sin v)=-4\cos\alpha\cos u\cos v\cos\phi\,\sin u\sin v,
\]
while
\[
\frac{d}{dt}\sin\phi=-4\cos\alpha\cos u\cos v\cos\phi\,\sin\phi.
\]
Consequently their ratio \(J=(\sin u\sin v)/\sin\phi\) is constant wherever its denominator is nonzero. Under a lift shift of an individual phase by \(2\pi\), the numerator and denominator acquire the same sign, proving that \(J\) is a bona fide torus function on its indicated open domain.

**3. Critical complete reduction.** At \(\alpha=\pi/2\), \(\dot\phi=0\), and with \(s=\sin\phi\), \(c=\cos\phi\) the remaining equations become
\[
\dot u=2s\sin u\cos v,\qquad
\dot v=-2s\cos u\sin v,\qquad
\dot A=\dot B=2c\cos u\cos v.
\]
The product \(p=\sin u\sin v\) is constant. For \(0<|p|<1\), each connected component of the level \(\sin u\sin v=p\) is a smooth simple closed curve: the gradient \((\cos u\sin v,\sin u\cos v)\) cannot vanish there; moreover the component stays within one pair of open sine-sign semicircles and surrounds its single nondegenerate maximum or minimum. The vector field has no zero on this component: simultaneous vanishing of its first two entries would require \(\cos u=\cos v=0\), forcing \(|p|=1\). Thus each component is one periodic orbit, without a smaller return on the component.

**4. Exact quadrature and minimal period.** Let \(x=|\sin u|\). Along one quarter of a component, \(x\) runs monotonically from \(|p|\) to \(1\). Squaring the differential equation yields
\[
(\dot x)^2=4s^2(1-x^2)(x^2-p^2).
\]
The four symmetric quarters therefore give
\[
T=\frac2{|s|}\int_{|p|}^{1}\frac{dx}{\sqrt{(1-x^2)(x^2-p^2)}}.
\]
Set \(x^2=p^2+(1-p^2)\sin^2 t\); the integral is \(K(\sqrt{1-p^2})\), giving the formula. The arithmetic-geometric mean identity is \(K(\sqrt{1-p^2})=\pi/[2\operatorname{AGM}(1,|p|)]\) for \(0<|p|<1\). Since \(K\) increases strictly with its modulus, \(T\) decreases strictly with \(|p|\).

**5. Full-phase return, not just shape recurrence.** For nonzero \(p\), both \(\sin u\) and \(\sin v\) remain nonzero, and
\[
\dot A=\frac{\cos\phi}{\sin\phi}\frac{d}{dt}\log|\sin u|.
\]
Integration around the shape orbit gives \(A(T)-A(0)=0\). As \(\phi\) is constant, also \(B(T)-B(0)=0\). The original lifted phases \(A\pm u,B\pm v\) therefore return exactly. They cannot return earlier because \((u,v)\) traverses its level curve once in the computed time. This establishes minimality in the original four-phase system.

**6. Boundary analysis.** Standard complete elliptic-integral limits give \(K(k)\to\pi/2\) as \(k\downarrow0\) and \(K(k)=\log[4/\sqrt{1-k^2}]+o(1)\) as \(k\uparrow1\); inserting \(k=\sqrt{1-p^2}\) establishes both stated endpoints. At \(p=0\) the regular level consists of invariant sine-zero circles with equilibria and separatrix trajectories, so no nonconstant finite period follows from the regular formula. At \(|p|=1\) the shape and individual phases are fixed. At \(\sin\phi=0\), the denominator of \(J\) vanishes and the displayed theorem does not apply; indeed \(u,v,\phi\) are constant at the quadrature lag while the whole pattern can rigidly rotate. These boundary cases prevent overextension of the classification.

## Verification
Run \(`python3 verify.py`\) with Python 3 and its standard library. The verifier independently checks the conserved quantity's derivative identity on nonsingular random states, the trigonometric coordinate reduction, return of all four original phases after the predicted period for 24 cases by a fourth-order Runge–Kutta scheme, monotonicity on a sampled grid, and both limiting formulas. It reports 548 derivative checks, 400 reduction checks, 24 full-state return checks, maximum phase-return error below \(4\cdot10^{-11}\), and endpoint/monotonicity checks passed. These are finite diagnostics, not substitutes for the preceding global analytical proof.

## Relationship to prior work
Yan, Ozawa, Kori and Sato (arXiv:2603.02135, first submitted 2 March 2026) analyze common-lag nearest-neighbor rings, twisted-state basins and the Hamiltonian/volume-preserving endpoint. Their inspected analysis does not provide a lag-independent first integral specific to four oscillators, an exact elliptic period for each nonsingular critical trajectory, or a proof of zero common-phase drift. Ahnert and Pikovsky (arXiv:0806.1833) investigate lattice waves and an associated Hamiltonian structure rather than this finite four-ring period. Ashwin, Burylko and Maistrenko (2008) analyze three and four globally coupled higher-harmonic oscillators, not this nearest-neighbor sine ring. Gong and collaborators (arXiv:1812.05883) invoke Watanabe–Strogatz theory for common-forcing/global oscillators; that does not itself supply the closed period and no-drift law of the present special network. Ashwin, Bick and Burylko (arXiv:1603.07937) discuss integrability and time-reversal symmetries for **fully permutation-symmetric, globally coupled** identical oscillators; their full-text discussion concerns a different adjacency and does not supply the four-site nearest-neighbor lag-independent ratio or minimal elliptic period. Burylko, Mielke, Wolfrum and Yanchuk (SIAM J. Appl. Dyn. Syst. 2018) consider **skew-symmetric anisotropic couplings** and low-dimensional Hamiltonian-like/heteroclinic regions; only their abstract was available in this comparison, so no whole-text noncoverage is asserted. A 2009 study by Canale and Monzón analyzes ring global properties but its full text was unavailable; equivalent four-ring results elsewhere remain possible.

## Limitations
The exact periodic foliation is proved for exactly four identical oscillators, equal nearest-neighbor sinusoidal couplings, and critical phase lag \(\alpha=\pi/2\). The first integral is conserved for arbitrary lag but only on \(\sin\phi\ne0\). No claim is made about generic larger rings, variable frequencies, basin fractality, heteroclinic time scales beyond the displayed period limit, or stochastic perturbations. The four-ring condition does not prove universal integrability across ring sizes. The exact minimal period concerns fully specified regular level components, not boundary equilibria or the invariant denominator-zero set. Bibliographic novelty remains subject to later independent checking, particularly unpublished or inaccessible finite-ring studies.

## References
1. Jin Yan, Ayumi Ozawa, Hiroshi Kori, Yuzuru Sato, *Basin Metamorphosis in Coupled Phase Oscillators*, arXiv:2603.02135 (first version 2026-03-02), https://arxiv.org/abs/2603.02135.
2. Karsten Ahnert and Arkady Pikovsky, *Traveling waves and Compactons in Phase Oscillator Lattices*, arXiv:0806.1833, https://arxiv.org/abs/0806.1833.
3. Peter Ashwin, Oleksandr Burylko, Yuri Maistrenko, *Bifurcation to heteroclinic cycles and sensitivity in three and four coupled phase oscillators*, Physica D **237** (2008), 454–466.
4. Chen Gong, Chunming Zheng, Ralf Toenjes, Arkady Pikovsky, *Repulsively Coupled Kuramoto-Sakaguchi Phase Oscillators Ensemble Subject to Common Noise*, arXiv:1812.05883, https://arxiv.org/abs/1812.05883.
5. Eduardo Canale and Pablo Monzón, *Global properties of Kuramoto bidirectionally coupled oscillators in a ring structure* (2009), publicly available repository abstract; full text not accessible in this inspection.
6. Peter Ashwin, Christian Bick, Oleksandr Burylko, *Identical phase oscillator networks: bifurcations, symmetry and reversibility for generalized coupling*, arXiv:1603.07937, https://arxiv.org/abs/1603.07937.
7. Oleksandr Burylko, Alexander Mielke, Matthias Wolfrum, Serhiy Yanchuk, *Coexistence of Hamiltonian-Like and Dissipative Dynamics in Rings of Coupled Phase Oscillators with Skew-Symmetric Coupling*, SIAM J. Appl. Dyn. Syst. **17** (2018), 2076–2105, DOI:10.1137/17M1155685 (abstract inspected).
