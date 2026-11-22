# A minimal thermal-robust cubic handedness witness for triangular run-and-tumble confinement

## Finding
For a planar particle confined by an isotropic harmonic force and driven by three equilateral headings, the **stationary spatial law is reflection symmetric if and only if the clockwise and anticlockwise heading-switch rates agree**. A single, explicitly computable third complex spatial moment detects every nonzero rate bias. First and second *pure complex* moments vanish by threefold rotation symmetry, and any independent isotropic translational Brownian diffusion leaves the complex cubic moment exactly unchanged. Two or fewer heading directions cannot encode a reflection-asymmetric stationary spatial law under the same isotropic confinement and noise assumptions.

Write \(Z=X+iY\), \(\omega=e^{2\pi i/3}\), \(U_t=\omega^{J_t}\), and let \(J_t\in\{0,1,2\}\) jump \(j\mapsto j+1\pmod3\) at rate \(u\) and \(j\mapsto j-1\pmod3\) at rate \(d\). Define \(s=u+d>0\), \(\delta=u-d\), \(\kappa>0\), \(v>0\), and \(D\ge0\), with the dynamics
\[
\mathrm{d}Z_t=(-\kappa Z_t+vU_t)\,\mathrm{d}t+\sqrt{2D}\,(\mathrm{d}B^x_t+i\mathrm{d}B^y_t).
\]
Here the two Brownian coordinates are independent and independent of \(J\). In the unique stationary distribution, put
\[
A=(\kappa+3s/2)(2\kappa+3s/2)+3\delta^2/4,\qquad B=\sqrt3\kappa\delta/2.
\]
Then
\[
\boxed{\mathbb EZ=\mathbb EZ^2=0,\qquad
\mathbb EZ^3=\frac{2v^3}{\kappa(A+iB)},\qquad
\operatorname{sgn}\operatorname{Im}\mathbb EZ^3=-\operatorname{sgn}(u-d).}
\]
In particular, the complex cubic moment is never real if \(u\ne d\), and its imaginary part vanishes precisely at zero heading-current bias. The result applies at every finite temperature \(D\ge0\), not merely in the noiseless model.

## Assumptions and scope
The heading triangle is fixed in the laboratory frame, with one vertex at the positive real axis; clockwise and anticlockwise labels are defined relative to the orientation \(0,2\pi/3,4\pi/3\). The noise is circular Gaussian in the plane and does not alter the angular chain. The switching rates may be zero individually, but their sum is positive; the directed three-cycle remains irreducible. The statement concerns the full stationary spatial probability measure, not whether a chosen trajectory is dynamically reversible. The base system is unidirectional or bidirectional cyclic heading switching, **not** independent redrawing of headings at each event.

For \(D=0\), the support is the equilateral triangle with vertices \(v\omega^j/\kappa\); this is a standard accessible-set consequence of finite-state piecewise deterministic switching and is used only as a symmetry tool. For \(D>0\), convolution with a circular nondegenerate Gaussian gives full planar support, but preserves the presence or absence of reflection symmetry.

## Proof
**Existence and rotational symmetry.** Since \(s>0\), the three-state heading chain is irreducible with unique uniform stationary distribution. The stable linear filter has the unique stationary realization
\[
Z^{(0)}_t=v\int_{-\infty}^t e^{-\kappa(t-r)}U_r\,\mathrm{d}r.
\]
Its thermal counterpart is \(Z_t=Z^{(0)}_t+G_t\), where \(G_t\) is an independent stationary isotropic Gaussian Ornstein–Uhlenbeck process. Rotation \((Z,U)\mapsto(\omega Z,\omega U)\) commutes with every transition, so uniqueness yields threefold invariance; therefore \(\mathbb EZ=\mathbb EZ^2=0\).

**Exact moment recursion.** Set \(W_n=\mathbb E[(Z^{(0)})^n U^{-n}]\), with \(W_0=1\). Apply the stationary Markov generator to the function \(z^n U^{-n}\): on a clockwise switch the angular factor is multiplied by \(\omega^{-n}\), and on an anticlockwise switch by \(\omega^n\). Thus, for each integer \(n\ge1\),
\[
W_n=\frac{nv W_{n-1}}{n\kappa+u(1-\omega^{-n})+d(1-\omega^n)}.
\]
For \(n=1,2,3\), the denominators are respectively
\[
\kappa+3s/2+i\sqrt3\delta/2,\quad
2\kappa+3s/2-i\sqrt3\delta/2,\quad 3\kappa.
\]
Because \(U^3=1\), \(\mathbb E(Z^{(0)})^3=W_3\). Multiplication of the first two denominators yields \(A+iB\), giving the claimed formula, with \(A>0\). Consequently
\[
\operatorname{Im}\mathbb EZ^3
=-\frac{2v^3 B}{\kappa(A^2+B^2)},
\]
which is zero exactly when \(\delta=0\).

**Thermal invariance.** The stationary thermal component \(G\) is centered circular Gaussian with \(\mathbb EG=\mathbb EG^2=\mathbb EG^3=0\), independent of \(Z^{(0)}\). The binomial identity yields \(\mathbb E(Z^{(0)}+G)^3=\mathbb E(Z^{(0)})^3\) for every \(D\ge0\). Its ordinary second radial moment, given for cross-checking, is
\[
\mathbb E|Z|^2=\frac{v^2}{\kappa}\,
\frac{\kappa+3s/2}{(\kappa+3s/2)^2+3\delta^2/4}
+\frac{2D}{\kappa}.
\]

**If-and-only-if reflection statement.** If \(u=d\), the generator is invariant under \((Z,J)\mapsto(\overline{Z},-J\pmod3)\), hence the stationary law is invariant under reflection in the real axis (and the other two triangle symmetry axes). If \(u\ne d\), the imaginary cubic moment excludes all three reflections preserving the heading triangle. Indeed, the noiseless stationary support is exactly the triangle: the filter is a convex exponentially weighted average of its three vertices, and positive-probability arbitrarily rapid switching followed by arbitrary dwell times makes every convex combination approximately attainable. Therefore any reflection preserving its positional distribution must preserve the triangle and be one of its three geometric reflections. With \(D>0\), a reflection of the Gaussian-convolved measure would imply the same reflection of the noiseless measure, by division of characteristic functions by the everywhere nonzero isotropic Gaussian Fourier factor. No reflection is possible for \(u\ne d\).

**Minimality.** With at most two admissible headings, the noiseless stationary stable-filter output is confined to the line segment joining their equilibrium velocity positions. Reflection across that (possibly affine) line fixes the positional measure, and isotropic Gaussian convolution preserves the reflection. Hence three is the smallest number of headings for stationary spatial handedness in this model class.

## Verification
The accompanying `checker.py` derives the first three stationary moments from a separate three-state Markov-generator linear solve, tests four symbolic rational parameter configurations and 80 independent numerical rate configurations, then samples 180,000 stationary trajectories by backward exponential-renewal decomposition. It also checks independence of the cubic signal under an added isotropic Gaussian displacement. These computations corroborate the exact proof; they do not substitute for its infinite-parameter argument. Run `python checker.py` with NumPy and SymPy.

## Relationship to prior work
Guéneau, Majumdar and Schehr (2026, arXiv:2602.08436) provide exact trapped RTP stationary laws for **independently redrawn** headings, including discrete velocity laws (Section VI); their angular process lacks the history-dependent cyclic bias considered here. Smith, Le Doussal, Majumdar and Schehr (2022, arXiv:2207.10445) solve the **symmetric** quarter-turn trapped RTP, whose fourfold structure differs from the three-heading biased cycle. Britton and collaborators (2026, arXiv:2608.23519) treat preferred angular turns in unconfined RTP transport. Established piecewise deterministic support theorems characterize accessible invariant supports in far greater generality and are not claimed as new. The contribution assessed here is the **exact minimal third-order static handedness obstruction and its all-temperature robustness**, not the general polynomial-moment method, support theorem, or known symmetric trapped laws.

## Limitations
The observable distinguishes the sign of the net clockwise/anticlockwise rate bias relative to the laboratory heading triangle; it does not by itself identify both switching rates. Thermal Gaussian convolution reduces signal-to-noise ratios although it leaves the unnormalized complex cubic moment unchanged. No claim is made for anisotropic noise, arbitrary non-equilateral heading triangles, interacting particles, or time-dependent traps. The literature comparison supports best-knowledge novelty, not a claim of exhaustive publication priority; inaccessible or unindexed treatments of three-state cyclic planar traps may already contain equivalent moment identities. Independent review remains outstanding.

## References
1. M. Guéneau, S. N. Majumdar, G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (first submitted 2026-02-09), https://arxiv.org/abs/2602.08436 .
2. N. R. Smith, P. Le Doussal, S. N. Majumdar, G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions*, arXiv:2207.10445 (2022), https://arxiv.org/abs/2207.10445 .
3. *Run-and-tumble particles with preferred reorientation*, arXiv:2608.23519 (2026), https://arxiv.org/abs/2608.23519 .
4. M. Benaïm, S. Le Borgne, F. Malrieu, P.-A. Zitt, *Qualitative properties of certain piecewise deterministic Markov processes*, arXiv:1204.4143 (2012), https://arxiv.org/abs/1204.4143 .
5. M. Benaïm, F. Colonius, R. Lettau, *Supports of Invariant Measures for Piecewise Deterministic Markov Processes*, arXiv:1604.06219 (2016), https://arxiv.org/abs/1604.06219 .
