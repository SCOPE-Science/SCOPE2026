# Independent mathematical audit

## correctness

PASS

For exact Pareto tail P(T>u)=u^(-α), α>2, and independent restarted Brownian excursions, Brownian scaling yields R=2DT²J with J=∫_0^1 W_s²ds independent of T. Wick gives E J=1/2 and E J²=7/12, E R=D E T², E R²=(7/3)D² E T⁴, E RT=D E T³, so centered Y=R-μT has mean zero, μ=D(α-1)/(α-2). Renewal age A_t is tight (nonlattice finite-mean Pareto); U_t|A_t has law 2D A_t²J and is also tight. The exact decomposition t(Q_t-μ)=Σ_{i≤N(t)}Y_i+U_t-μA_t and renewal strong law prove Q_t→μ a.s.; the last full-cycle reward is o(t) a.s. by integrability and Borel-Cantelli. For α>4, Var(Y)/E T gives σ²=D²/m[(7/3)a4-2qa3+q²a2]>0, confirmed α=5→172/27, α=6→695/192, α=8→2597/1080 for D=1. For 2<α<4, β=α/2∈(1,2), Breiman lemma and all positive Gaussian-area moments give P(Y>x)~cα x^-β, cα=E(2DJ)^β. The negative tail is O(x^-α) because Y≥-μT; centering/negative-tail upper bound and the positive-tail sandwich justify spectrally positive β-stable DOA with exponent β cα Γ(-β)(-iu)^β/m after random time change. At α=4, c4=(7/3)D² and truncated second moment ~2c4 log z, so normalized variance c4/m=7D²/4 after sqrt(t/log t). Independent sympy arithmetic verified formulas and independent 160000-draw Brownian KL experiment yielded E(2J)≈0.99972, E(2J)²≈2.32069 (exact 7/3), E(2J)^1.5≈1.40182. This only corroborates moment identities; infinite distributional limits depend on analytic DOA, renewal and random-time-change theorems. D>0 essential; no α≤2, non-Pareto, path-level theorem, finite-time variance convergence or formal Lean attestation asserted.

## originality

PASS

Best-of-knowledge novelty is restricted to the exactly normalized Pareto-reset quadratic Brownian occupation stable/log-critical fluctuation trichotomy, not classical stable-limit methods or the finite-variance CLT. Zamparo 2022 explicitly covers the finite-moment Gaussian branch; Méndez/Flaquer-Galmés 2025 derive general transform/moment formulas and an explicit half-occupation distribution, but not the present centered quadratic stable weak limit. Related published Brownian signed-area and thermal-work trichotomies involve different rewards and are not implication theorems for squared occupation. A Resultary record with the identical identifier/title is a public mirror of THIS claim, not an independent prior discovery; it is disclosed as pre-existing publicity, not counted as disjoint priority evidence.

## value

PASS

Mean-squared displacement exposure is a natural quadratic path functional of renewal-reset Brownian motion; the finite-mean threshold α>2 and finite-Gaussian-fluctuation threshold α>4 are distinct, making exact critical √(t/log t) and spectrally positive α/2-stable limits relevant to sampling uncertainty. The sharp fourth-moment transition and evaluated physical-time amplitudes are nontrivial natural invariants that are not simply a table lookup. The model-specific R=2DT²J calculation contributes concrete constants beyond the classical renewal reward template. Value does not rely on a new general stable theorem or downstream application; the Gaussian α>4 part is already known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
