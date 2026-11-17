# Sharp Fourier-order barrier for universal phase-grid multistability

## Finding

Fix integers \(N\ge2\) and \(q\ge2\). For the complete, identically driven phase network

\[
\dot\theta_i=\Omega+g\sum_{j\ne i}H(\theta_j-\theta_i),\qquad g>0,
\]

let \(H\) be a real odd trigonometric polynomial of degree \(d\), and remove simultaneous phase translation. For each \(\mathbf k\in\{0,\ldots,q-1\}^{N-1}\), write \(C_{\mathbf k}\) for the relative phase configuration \(\theta_1=0\), \(\theta_i=2\pi k_i/q\), \(2\le i\le N\). If **every** such configuration is an exponentially attracting equilibrium, then \(d\ge q\). This is sharp for every \(N,q\): the single harmonic \(H(s)=\sin(qs)\) makes all \(q^{N-1}\) configurations attracting, and these are its only asymptotically attracting relative equilibria. Their basins partition the phase quotient up to a null set and each has normalized Haar measure \(q^{1-N}\).

The new result is the universal *minimum Fourier degree*. The pure-harmonic lifting, its attraction patterns and basin rescaling follow established dynamical equivalence results, which are cited below and are **not** claimed as original.

## Assumptions and scope

All phases live in \(\mathbb R/(2\pi\mathbb Z)\). Network edges have identical positive strength \(g\); oscillators have the same intrinsic angular speed \(\Omega\). The interaction \(H\) is odd, real and \(2\pi\)-periodic, with finite Fourier representation \(H(s)=\sum_{r=1}^{d}a_r\sin(rs)\) and \(a_d\ne0\). Linear/exponential attraction is considered on the \((N-1)\)-dimensional phase-difference torus, not along the neutral common-phase direction. The lower bound concerns **all labelled phase-coloring states**, not merely the existence of some stable clusters or travelling waves.

## Proof

**1. Sharp Fourier obstruction.** Since \(H\) is odd, \(H(0)=0\) and \(H'(-s)=H'(s)\). Choose any \(k\in\{1,\ldots,q-1\}\) and restrict to the invariant two-cluster submanifold with \(N-1\) oscillators at phase \(A\) and one at \(B=A+\delta\). Its exact phase-gap equation is

\[
\dot\delta=-gN H(\delta).
\]

For the grid phase-gap \(\delta_k=2\pi k/q\) to be an exponentially attracting equilibrium in the full network, it must be an attracting fixed point within this invariant two-cluster submanifold. Consequently \(H'(\delta_k)>0\). The synchronized grid configuration likewise has transverse eigenvalue \(-gN H'(0)\), so \(H'(0)>0\). Thus all \(q\) sampled derivatives \(H'(2\pi k/q)\) must be strictly positive. On the other hand, if \(d<q\), root-of-unity orthogonality gives

\[
\sum_{k=0}^{q-1}H'(2\pi k/q)
=\sum_{r=1}^{d}r a_r\sum_{k=0}^{q-1}\cos(2\pi rk/q)=0,
\]

because \(q\nmid r\) for every \(1\le r\le d\). The contradiction proves \(d\ge q\).

**2. Attainment and full sink census.** Take \(H(s)=\sin(qs)\). For every grid state, all interactions vanish, while every off-diagonal Jacobian entry equals \(gq\), and diagonal entries equal \(-gq(N-1)\). The full Jacobian has exactly one common-phase zero eigenvalue and \(N-1\) eigenvalues \(-gqN\). Hence all \(q^{N-1}\) labelled relative grid states are hyperbolic sinks.

To exclude any other attracting equilibrium, apply the covering transformation \(\phi_i=q\theta_i\pmod{2\pi}\), yielding the attractive first-harmonic Kuramoto flow (with rescaled gain). Let \(Z=N^{-1}\sum_j e^{i\phi_j}\). Its exact potential \(V=\tfrac12|Z|^2\) is nondecreasing, strictly except at equilibria. At an equilibrium with \(Z\ne0\), every \(\phi_i\) equals the argument of \(Z\) or its antipode. If both clusters occur, the inter-cluster splitting mode is unstable: its eigenvalue is positive. States with \(Z=0\) are global minima of \(V\), and no neighborhood of such a state is attracted to it under the gradient ascent of \(V\). Therefore the only asymptotically attracting relative equilibria downstairs are fully synchronized, and their lifts are precisely the \(q^{N-1}\) grid states. This pure-harmonic covering argument is a known result (Delabays, 2019).

**3. Equal basin law.** The analytic gradient flow on the compact phase quotient converges to an equilibrium by the standard analytic gradient convergence theorem. Almost every initial condition has \(Z\ne0\), so the monotonicity of \(|Z|\) precludes convergence to the \(Z=0\) locus. Every nonuniform antipodal equilibrium with nonzero \(Z\) has a positive transverse eigenvalue, hence its stable manifold has measure zero. There are only finitely many such equilibria modulo phase translation. Thus almost every first-harmonic initial state converges to synchrony. Its \(q^{N-1}\) lifted basins are permuted transitively by the \((\mathbb Z/q\mathbb Z)^{N-1}\) deck group, preserving Haar measure, and consequently each basin has probability exactly \(q^{1-N}\).

## Verification

The included standalone \(\texttt{verify.py}\) uses only the Python 3 standard library. It checked all \(34{,}631\) grid configurations for \(2\le N\le6\), \(2\le q\le7\), verifying the vector field and complete Jacobian entrywise, and also checked all finite root-of-unity sums in those ranges. The finite tests corroborate the exact arguments; they are not used to infer the universal quantifiers. Invoke \(\texttt{python3 verify.py}\).

## Relationship to prior work

The new obstruction answers a Fourier-design question prompted by the coexistence of synchronous, pacemaker and travelling-wave rhythms in the November 2026 three-cell phase-model study of Qie and coauthors. Delabays (2019, Section II and Section III) **already established** the dynamical covering equivalence between pure higher-harmonic and first-harmonic Kuramoto systems, explicitly including the multi-cluster fixed points and basin scaling. Jain and Jalan (2025) analyze related higher-harmonic cluster basins. The present finding is restricted to the distinct *necessity* statement: no odd Fourier interaction of degree smaller than the number of desired grid colors can stabilize the entire grid of phase configurations, for any network size at least two. Neither inspected text provides that lower-bound sampling argument. This is a literature-based priority assessment, not a proof of historical uniqueness.

## Limitations

The necessity statement depends on oddness, all-to-all equal coupling and the demand that **every** grid coloring be exponentially attracting. It is not a lower bound for stabilizing one special cluster state, for arbitrary directed networks, or for interactions lacking odd symmetry. Pure-harmonic basin assertions concern identical autonomous oscillators with Haar-distributed phases; frequency disorder and noise are not included. Existing higher-harmonic equivalence results cover the sufficiency and basin descriptions. The possibility of an unindexed prior statement of the sharp sampling obstruction remains.

## References

- X. Qie, M. G. Pedersen, J. Song, S. Liu and A. L. Shilnikov, *Delay-induced multirhythmicity in a 3-cell inhibitory network*, arXiv:2611.06836v1 (first posted 2026-11-04), https://arxiv.org/html/2611.06836v1.
- R. Delabays, *Dynamical equivalence between Kuramoto models with first- and higher-order coupling*, Chaos 29, 113129 (2019), https://doi.org/10.1063/1.5118941; author open-access copy https://delabays.xyz/docs/articles/Delabays19a.pdf.
- J. C. Jain and S. Jalan, *Low dimensional Watanabe–Strogatz approach for Kuramoto oscillators with higher-order interactions*, arXiv:2508.13707v1 (2025), https://arxiv.org/html/2508.13707v1.
