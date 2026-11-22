# A golden-ratio Cantor transition in the switching positions of a harmonically trapped renewal swimmer

## Finding

A one-dimensional, athermal, harmonically trapped swimmer reverses propulsion sign at independent renewal times. If each run lasts either \(\tau\) or \(2\tau\), each with probability \(1/2\), then the locations recorded **at successive starts of positive runs** undergo a sharp geometric transition. Write \(q=e^{-\kappa\tau}\), \(\varphi=(1+\sqrt5)/2\), and normalize position by \(z=\kappa x/v\). The unique invariant switching-position support \(K_q\) is a separated Cantor set exactly when \(0<q<\varphi^{-1}\), equivalently \(\kappa\tau>\log\varphi\). At and above \(q=\varphi^{-1}\), its support instead fills one explicit interval. In particular,
\[
\dim_{\mathrm H}K_q=\begin{cases}
\log\varphi/\log(1/q),&0<q<\varphi^{-1},\\
1,&\varphi^{-1}\le q<1.
\end{cases}
\]
In the Cantor regime the unique invariant **probability measure** \(\mu_q\) on \(K_q\) is singular and exact dimensional, with
\[
\dim_{\mathrm H}\mu_q=\frac{\log4}{3\log(1/q)}.
\]
Yet at **every** \(0<q<1\), the stationary law of position observed at a uniformly sampled physical time is absolutely continuous with an essentially bounded density. This event-time/physical-time regularity contrast is not an identification of their different probability laws.

For the example \(q=1/2\), the switching support is contained in \([-5/7,-1/7]\), with four first-generation intervals \([-5/7,-9/14]\), \([-17/28,-4/7]\), \([-3/7,-2/7]\), and \([-3/14,-1/7]\). Thus \(\dim_{\mathrm H}K_{1/2}=\log\varphi/\log2\), whereas \(\dim_{\mathrm H}\mu_{1/2}=2/3\).

## Assumptions and scope

Fix \(v,\kappa,\tau>0\). Between instantaneous orientation reversals, the particle evolves by the deterministic equation \(\dot X_t=-\kappa X_t+v\sigma_t\), where \(\sigma_t\in\{-1,+1\}\). At every reversal, the sign flips; it is not independently redrawn. Successive runs have independent durations with law \(\Pr(T=\tau)=\Pr(T=2\tau)=1/2\), independent of all prior positions. No translational Brownian noise, inertia, or resting stage is present. The mean run duration is \(3\tau/2\). The two-run return section is observed just after the negative run ends and the next positive run starts. The stationary physical-time law uses the standard equilibrium renewal-phase construction, rather than an arbitrary synchronized time origin. The dimension of a probability measure refers to its almost-sure local/Hausdorff measure dimension, not to the dimension of its support.

Define the positive and negative endpoints
\[
\ell_q=\frac{q^2-q-1}{q^2+q+1},\qquad
h_q=\frac{q^2+q-1}{q^2+q+1},\qquad I_q=[\ell_q,h_q].
\]
For \(m,n\in\{1,2\}\), define the four increasing affine contractions
\[
F_{mn}(z)=q^{m+n}z-1+2q^n-q^{m+n}.
\]
Their probabilities are all \(1/4\). The support \(K_q\) means the unique nonempty compact attractor satisfying \(K_q=\bigcup_{m,n}F_{mn}(K_q)\). The probability \(\mu_q\) is the unique probability fixed by the corresponding equally weighted push-forward equation.

## Proof

**1. Derivation and uniqueness of the embedded recursion.** A positive run of duration \(m\tau\) maps normalized position \(z\) to \(1+(z-1)q^m\). A subsequent negative run of duration \(n\tau\) maps that position \(u\) to \(-1+(u+1)q^n\). Their composition is exactly \(F_{mn}\). Because each slope is \(q^{m+n}\in(0,1)\), independent successive pairs give an iterated-function system with a unique invariant probability and compact attractor, by the contraction theorem. Its stationary position is a convergent random affine series. For all \(q\in(0,1)\), the four maps send \(I_q\) into itself; the leftmost fixed point is that of \(F_{12}\), namely \(\ell_q\), and the rightmost fixed point is that of \(F_{21}\), namely \(h_q\). Indeed, direct substitution shows \(F_{mn}(\ell_q)\ge\ell_q\) and \(F_{mn}(h_q)\le h_q\), with equality on the left for \((m,n)=(1,2)\), on the right for \((2,1)\). Both endpoints belong to the attractor, so \(I_q\) is exactly its convex hull.

**2. Exact gap factorization and the threshold.** Consider the first-level images in the fixed order \((1,2),(2,2),(1,1),(2,1)\). Direct substitution into the affine maps gives the three consecutive *signed* gaps, defined as the next image's left endpoint minus the previous image's right endpoint:
\[
\begin{aligned}
G_1&=\frac{2q^3(1-q-q^2)}{1+q+q^2},\\
G_2&=\frac{2q(1-q-q^2)}{1+q+q^2},\\
G_3&=\frac{2q^2(1-q-q^2)}{1+q+q^2}.
\end{aligned}
\]
Every first-level image has positive length; the leftmost image begins at \(\ell_q\) and the rightmost ends at \(h_q\). Since \(1-q-q^2\) changes sign exactly at \(q=1/\varphi\), the images are pairwise disjoint with positive gaps below this threshold, touch without gaps at equality, and overlap in a connected chain above it. In the latter two cases their union equals \(I_q\), so uniqueness of the compact invariant set gives \(K_q=I_q\). Below threshold, the positive gaps persist at every level, making \(K_q\) a perfect nowhere-dense self-similar Cantor set with the strong separation condition.

**3. Dimensions.** Under strong separation the classical self-similar-set dimension formula applies. Its dimension \(s\) is the unique positive solution of
\[
\sum_{m,n=1}^2q^{(m+n)s}=(q^s+q^{2s})^2=1.
\]
Consequently \(q^s=1/\varphi\) and \(s=\log\varphi/\log(1/q)\). At and above threshold, \(K_q\) is a nondegenerate interval, hence has Hausdorff dimension one. Under the same strong separation condition, the standard exact-dimensional self-similar-measure theorem applies: a typical length-\(N\) code cylinder has probability \(4^{-N}\), and its diameter is a fixed constant times \(q^{\sum_{j=1}^N(m_j+n_j)}\). The strong law for independent fair pairs gives \(N^{-1}\sum(m_j+n_j)\to3\); separation permits translation from cylinder exponents to local ball exponents. Thus the invariant measure has almost-sure local dimension \(\log4/[3\log(1/q)]\). Since the set dimension is strictly below one in this regime, the measure is singular relative to Lebesgue measure. No assertion about the local dimension of \(\mu_q\) is made at or above the overlap threshold.

**4. Smoothness at physical time.** Start a stationary pair at a switching point \(Z\sim\mu_q\), take independent durations \(m\tau,n\tau\) with \(m,n\in\{1,2\}\), and follow the two deterministic runs. The renewal-reward formula for the physical-time stationary distribution \(\nu_q\) is
\[
\nu_q(B)=\frac{1}{3\tau}\mathbb E\left[\int_0^{(m+n)\tau}\mathbf1_{\{X_t\in B\}}\,dt\right]
\]
for Borel sets \(B\), with the pair started in its stationary embedded law. The random cycle length need not be independent of the starting position to apply the stationary-reward identity; in this model the future durations are independent anyway. On a positive run, normalized position increases and remains at most \(1-(1-h_q)q^2\). On a negative run it decreases, remaining at least \(\ell_q\). Hence the absolute normalized speed throughout all runs is bounded below by
\[
\delta_q=\kappa\min\{(1-h_q)q^2,1+\ell_q\}>0.
\]
Since each run is monotone, its occupation time in any normalized-position Borel set \(B\) is at most \(|B|/\delta_q\), where \(|B|\) denotes Lebesgue measure. There are two runs per cycle. Consequently \(\nu_q(B)\le2|B|/(3\tau\delta_q)\) for all Borel sets, proving a bounded density. A change of spatial scale from normalized to physical position preserves absolute continuity. This demonstrates the regularity contrast without presuming any independence between phase and embedded position.

## Verification

Execute `python3 verify.py` in this extracted directory (Python standard library only). It checks exact-rational endpoint and image identities, all three factored gap formulas at multiple rational parameters on both sides of the critical point, the complete four-image coverage/gap regimes, the canonical \(q=1/2\) intervals, and finite prefix contraction and cylinder mass normalization. The symbolic algebra in the Proof can be rechecked independently by expanding the four affine expressions; the code and finite-prefix tests do not prove the all-parameter or infinite-dimensional statements. The proofs use exact affine identities, contraction, renewal reward, and standard self-similar-set and measure dimension theorems.

## Relationship to prior work

Farago and Smith, *Confined run-and-tumble particles with non-Markovian tumbling statistics* (first public January 3, 2024, arXiv:2401.01576), establish the alternating-renewal confined particle framework and develop a steady-density numerical method. Their worked waiting laws are exponential, semi-Gaussian, and heavy-tailed half-t. The primary full text's discussion identifies discrete waiting times as an unresolved test case for that numerical approach; it does not give the four-map switching section or the golden-ratio support/dimension transition. The present theorem does not claim that the general model, harmonic trajectories, or standard IFS dimension formulas are new.

Related results *Sharp variance envelope for harmonically trapped alternating-renewal swimmers* (2026) and *Sharp dwell-time noise bounds and trap-spectroscopic recovery for alternating-renewal propulsion* (2026) give stationary spatial variance envelopes and waiting-law spectroscopy for arbitrary run distributions. Their inspected complete result statements and proofs address moments/temporal correlations, not discrete switching-event support topology, its Hausdorff dimension, or the contrasting bounded physical-time density. Other iterated-function-system Cantor-to-interval results use different dynamical maps and are cited only as general methodological context, not as this specific theorem.

## Limitations

The binary equally weighted clock, exact duration ratio two, strictly alternating headings and harmonic restoring force are essential for the stated sharp formula. The theorem does not characterize all unequal probabilities or other duration ratios, nor does it claim the invariant event-time measure is absolutely continuous in the overlap regime. The physical-time density bound is not a formula for its full density. The dimensional results use classical self-similar-set theory in the strong separation regime; arbitrary sampling noise could change the event-time singularity. Publication priority is qualified because unindexed equivalent event-section results cannot be excluded by finite searches, and not every related paper's full text is accessible. No independent scientific audit is claimed.

## References

1. O. Farago and N. R. Smith, *Confined run and tumble particles with non-Markovian tumbling statistics*, arXiv:2401.01576 (first publicly posted 2024-01-03), *Physical Review E* **109**, 044121 (2024), https://arxiv.org/abs/2401.01576; https://doi.org/10.1103/PhysRevE.109.044121.
2. *Sharp variance envelope for harmonically trapped alternating-renewal swimmers*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-variance-envelope-for-harmonically-trapped-alternating-ren--3590eb1cf344.
3. *Sharp dwell-time noise bounds and trap-spectroscopic recovery for alternating-renewal propulsion*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-dwell-time-noise-bounds-and-trap-spectroscopic-recovery-fo--3baa3630f98c.
4. J. E. Hutchinson, *Fractals and self-similarity*, Indiana University Mathematics Journal **30** (1981), 713–747, https://doi.org/10.1512/iumj.1981.30.30055 (standard contraction and self-similar dimension background).
