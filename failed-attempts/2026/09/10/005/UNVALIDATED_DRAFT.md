# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Phase-design obstructions for disjoint-arc two-weight CGOs on the unit disk

## 1. Setting (admitted cell, unchanged)
$D=\{|x|<1\}$, $\Gamma_D=\{| \theta|<\pi/4\}$, $\Gamma_N=\{|\theta-\pi|<\pi/4\}$.
Closures are positively separated (distance $\sqrt2$). Complements
$K_D=\partial D\setminus\Gamma_D$, $K_N=\partial D\setminus\Gamma_N$ are closed
$3\pi/2$ arcs; $K_D\cup K_N=\partial D$; $K_D\cap K_N$ is the two gap arcs of
total length $\pi$. Chords joining $\Gamma_D$ to $\Gamma_N$ have directions
within $\pi/4$ of horizontal (limited-angle cone). All verified numerically
(`emergent_verify.py`, V1).

## 2. What was attempted (target route)
Prove disjoint-map uniqueness via paired Morse holomorphic weights $\Phi_D$,
$\Phi_N$ with complementary reality/vanishing plus a disjoint Alessandrini
reduction to an attenuated chord transform over $\Gamma_D\to\Gamma_N$ chords.
We derived the disjoint orthogonality identity, built strict single-arc sign
patterns, and tried sum/difference Carleman weights and Morse-with-critical-point
solves. Every symmetric two-weight closure failed for a structural reason,
formalized below.

## 3. Results

### Theorem O2 (parity obstruction for rotation-symmetric real pairs; proved).
Let $\Phi_D$ be a polynomial with real coefficients and
$\Phi_N(z)=\Phi_D(-z)$ (rotation by $\pi$ exchanging the arcs).
Put $\psi_-=\mathrm{Re}(\Phi_D-\Phi_N)$, $\psi_+=\mathrm{Re}(\Phi_D+\Phi_N)$.
Then:
- (a) $\partial_n\psi_-(\pm i)=0$ exactly (gap midpoints are forced
  characteristic points of any such difference weight);
- (b) $\partial_n\psi_+$ takes equal values at antipodal boundary points,
  hence cannot satisfy the two-sided sign pattern (negative on both
  $\Gamma_D,\Gamma_N$, positive on both overlap gaps) required for simultaneous
  two-sided Carleman control.
*Proof.* Write $\Phi_D(z)=\sum c_n z^n$, $c_n\in\mathbb R$.
Then $\psi_-(z)=2\sum_{\mathrm{odd }n}c_n\mathrm{Re}(z^n)$ is odd,
$\psi_+(z)=2\sum_{\mathrm{even }n}c_n\mathrm{Re}(z^n)$ is even; differentiate
radially at $z=\pm i$ (resp. compare $w,-w$). The odd/even normal-derivative
identities give (a)/(b) algebraically. Numerically confirmed to $10^{-15}$ on
the logged degree-32 coefficient vector. ∎

### Lemma O1 (Fourier mechanism against exact polynomial reality; proved for polynomials).
No nonconstant polynomial is real-valued on a boundary arc of positive length:
$P(e^{it})=\sum_{n\ge0}c_n e^{int}$ has vanishing negative Fourier modes, so
reality $P=\bar P$ on an arc forces all $c_{n\ge1}=0$ by analytic continuation
(F. and M. Riesz / identity theorem). Hence the reality locus of a nonconstant
polynomial on $\partial D$ is isolated zeros ($\le 2N$; exactly 4 for $z^2/2$).
Verified by DFT (negative bins $\sim 10^{-17}$) and zero count.
*Status.* Proved for polynomials (the class used in every audited construction
above). For general holomorphic $\Phi$ continuous to the closed $3\pi/2$
complement the same coefficient mechanism applies under $H^p$/F. and M. Riesz
regularity; we state that extension as a conjecture, not a theorem.

### Proposition E (Cayley escape; explicit witness).
$\Phi(z)=i(1+z)/(1-z)$ is real-valued on $\partial D\setminus\{1\}$ and
$\Phi'\ne0$ in $D$ (min $|\Phi'|=0.51$ on the audit grid). Exact circle reality
is achievable only with a boundary pole — outside the holomorphic class
required by the GT-style construction. This locates the only escape route:
singular weights or non-polynomial asymmetric phases.

### Certified tables.
Strict single-arc sign pattern (margins $3.00/1.00$), geometry/chord cone,
harmonic max-principle check, and the failed sum/difference sign tables are
logged with replay scripts.

## 4. Consequence for the admitted claims
- The full TARGET (uniqueness via paired Morse weights + chord injectivity)
  is not proved; the symmetric two-weight closure is obstructed by O2.
- The PRESET_FALLBACK as literally qualified (holomorphic phases real on the
  full closed $3\pi/2$ complements + paired CGOs + reduction) is not completable
  as a positive construction: O1 blocks the polynomial route and O2 blocks the
  rotation-symmetric route; the only exact-reality witness (Cayley) violates
  the holomorphicity hypothesis. We therefore do not claim TARGET or
  PRESET_FALLBACK.
- The obstruction triple (O1 lemma + O2 theorem + Cayley escape + certified
  tables) is the consolidated EMERGENT_FINDING: it tells every future
  disjoint-disk attempt exactly which phase classes are dead and which
  (singular/asymmetric) must be tried, and supplies the fixed limited-angle
  chord-cone input for tomography.

## 5. Reproduction
Run `python3 output/artifacts/emergent_verify.py` → `EMERGENT_VERIFY_ALL_OK`
(V1 geometry, V2 parity, V3 Cayley, V4 sign pattern, V5 Fourier mechanism,
V6 chord threshold). Supporting logs: `geometry.json`, `phases3.json`,
`weight.json`, `symm_nogo.json`, `phases5.json`, `phases6.json`.

## 6. Limitations (explicit)
- O1 is proved for polynomials; the $H^p$ extension to all holomorphic phases
  is a conjecture with a named mechanism, not a theorem.
- O2 covers rotation-symmetric real-coefficient pairs, not all asymmetric pairs.
- No Carleman estimate, CGO existence, chord injectivity, or potential
  uniqueness is claimed. No single-measurement obstruction witness $f^*$ is
  claimed (FD-SVD deferred for lack of scipy).
- Originality: GT/IUY/Daude comparisons are admission-triage level; the O1/O2
  pair itself was found by direct computation in-session and is, to our
  knowledge, not recorded in the surveyed priors.
