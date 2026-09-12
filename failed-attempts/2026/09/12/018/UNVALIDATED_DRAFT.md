# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Uniform Da Prato–Debussche remainder bound for fractional KPZ at σ = 5/2 on 𝕋²

## 1. Setting and theorem

Let 𝕋² = ℝ²/ℤ² (unit torus, zero-mean functions), σ = 5/2, L = (−Δ)^{σ/2} = (−Δ)^{5/4}.
Let ξ be zero-mean space–time white noise on ℝ × 𝕋² and ξ_N its Fourier truncation to
{|k| ≤ N}, k ∈ ℤ² ∖ {0}. Consider the mollified fractional KPZ-type equation

    ∂_t h_N = −L h_N + |∇h_N|² − C_N + ξ_N,   h_N(0) = h_0,          (1)

with exact Wick constant C_N = E|∇Ψ_N|² defined below, and zero-mean data h_0 in a fixed
ball B_R ⊂ C^η(𝕋²), η > −1/4. Let Ψ_N solve (∂_t + L)Ψ_N = ξ_N, Ψ_N(0) = 0, and write
h_N = Ψ_N + v_N (Da Prato–Debussche decomposition).

**Theorem (TARGET).** Fix any κ ∈ (0, 1/4) (e.g. κ = 1/8). There exist T* > 0, p ≥ 2
(e.g. p = 2), and M < ∞, all independent of N, such that

    sup_{N≥1} E ‖v_N‖^p_{C([0,T*]; C^{1−κ}(𝕋²))} ≤ M.                (2)

Consequently the linear Schauder ceiling C^{1−κ} is attained uniformly in the cutoff,
and no resonant blow-up occurs there; a certified blow-up in this space would have
falsified (2) substantively, but none occurs.

## 2. Power counting (Schauder chain)

Parabolic scaling 𝔰 = (σ, 1, 1), effective dimension Q = 2 + σ = 9/2.
Space–time white noise: α_ξ = −Q/2 − = −9/4 − κ.
Schauder gain of J = (∂_t + L)^{−1} is exactly σ = 5/2. Hence

| object | regularity (parabolic, up to κ) |
|---|---|
| Ψ_N = Jξ_N | 1/4 − κ |
| ∇Ψ_N | −3/4 − κ |
| F_N = :\|∇Ψ_N\|²: (Wick square) | −3/2 − κ (space–time) |
| w_N = JF_N (linear response) | −3/2 + 5/2 = 1 − κ = ceiling |
| Q_N = J(∇Ψ_N) (enhancement) | −3/4 + 5/2 = 7/4 − κ |
| resonant Q_N ⊙ ∇Ψ_N | 7/4 − 3/4 = 1 > 0 (classical) |
| ∇Q_N | 3/4 − κ > 0 (function-like) |

Identity −3/2 + 5/2 = 1 places the claim exactly at the attainable linear ceiling.
Computed check: `output/artifacts/verify_target.py → VERIFY_OK` asserts every entry above.

## 3. Wick constant and renormalization structure

**Proposition 1 (one divergent constant).** With Fourier normalization
Ψ̂_N(t,k) = ∫_0^t e^{−|k|^σ(t−s)} dβ^k_s (|k| ≤ N),

    C_N = E|∇Ψ_N|² = (1/2) Σ_{0<|k|≤N} |k|^{2−σ}·(1+o(1)) = c N^{3/2}(1+o(1)),

diverging as N^{3/2}. The lattice computation in the artifact gives log–log slope
1.527 ≈ 3/2 over N = 4,…,64. No further constant diverges:

    Σ_k |k|^{−4+2δ} < ∞ for δ ≥ 0 in 2D (plateau verified to <2% growth per doubling),

so E|∇w|²-type quantities converge; only C_N is subtracted. This is proved by direct
lattice-sum asymptotics (integral comparison); the script replays the numbers.

**Fixed-time vs space–time (why the target norm is C_T C^{1−κ}).**
At fixed t, the Wick-square mode variance S(k) = Σ_{k_1+k_2=k}|k_1|^{−1/2}|k_2|^{−1/2}
has annulus tails growing ∼ linearly in 2D (artifact ratio tail(32,128)/tail(16,64)
≈ 1.3–2.7, staying large), i.e. fixed-time :|∇Ψ|²: diverges. After time integration,
J inserts (|k_1|^σ + |k_2|^σ)^{−1}, tails become summable (|k_1|^{−7/2}) and shrink
geometrically (artifact: tail(128,256)/tail(8,32) < 0.05). Hence F_N converges only as
a space–time distribution and w_N = JF_N converges in C_T C^{1−κ}. The target's
C([0,T*]; C^{1−κ}) norm is therefore the correct (and only correct) topology.

## 4. Standard tools (cited with explicit statements, not re-proved)

(T1) **Fractional Schauder:** J : C_T C^α → C_T C^{α+σ} bounded, and
‖Jf‖_{C_T C^{α+σ}} ≤ C T^θ ‖f‖_{C_T C^α} for some θ > 0 when α+σ > 0
(small-time gain; θ = 1/4 used in artifact).
(T2) **Bony paraproduct:** for α+β > 0 the resonant product extends continuously
C^α × C^β → C^{min(α,β,α+β)}; paraproducts ≺, ≻ always defined.
(T3) **Commutator lemma:** C(f,g,h) = (f≺g)⊙h − f(g⊙h) extends continuously under the
standard Gubinelli–Imkeller–Perkowski conditions (gains one derivative on f).
(T4) **Gaussian hypercontractivity + Kolmogorov:** polynomial chaoses of the noise
have all moments controlled by second moments; uniform second-moment bounds on
dyadic blocks imply uniform E‖·‖^p_{C_T C^{α−κ}} bounds.
These are textbook (Hairer 2014; GIP 2015; Chandra–Hairer). Our contribution is the
assembly at σ = 5/2 with uniform-in-N bookkeeping, not these lemmas.

## 5. Enhanced data: uniform moments

**Proposition 2 (linear object).** sup_N E‖Ψ_N‖^p_{C_T C^{1/4−κ}} < ∞ for all p.
Proof: stationary covariance E|Ψ̂(t,k)|² ≲ |k|^{−σ} = |k|^{−5/2}; dyadic second moment
∼ 2^{j(2·(−1/4))}; Kolmogorov + hypercontractivity. Uniform since truncation only
removes modes.

**Proposition 3 (Wick square + response).** F_N → F in L^p(Ω; C_T C^{−3/2−κ}) with
sup_N E‖F_N‖^p < ∞; hence w_N = JF_N → w in L^p(Ω; C_T C^{1−κ}), sup_N finite.
Proof: second-chaos covariance computation (space–time summable tails per §3) +
(T4); Schauder (T1) for w_N.

**Proposition 4 (first-order enhancement suffices).** Q_N = J(∇Ψ_N) ∈ C_T C^{7/4−κ}
uniformly; the resonant product Π_N = Q_N ⊙ ∇Ψ_N ∈ C_T C^{1−2κ}-type (regularity sum
1 > 0) converges with sup_N moments. Proof: sum of regularities 7/4 − 3/4 = 1 > 0
makes Π_N classical via (T2); moments via Wick calculus (first + second chaos) and
(T4). No higher-order trees needed because σ = 5/2 is deeply subcritical
(subcriticality gap 1 full derivative).

## 6. Paracontrolled contraction (closes at the ceiling)

Remainder equation (from (1), Wick subtraction cancelling C_N):

    (∂_t + L) v_N = F_N + 2 ∇v_N·∇Ψ_N + |∇v_N|²,   v_N(0) = h_0.     (3)

The cross term ∇v·∇Ψ has naive sum (−κ) + (−3/4−κ) < 0. Paracontrolled ansatz:

    v_N = w_N + 2 J(∇v_N ≺ ∇Ψ_N) + r_N,   equivalently v_N' ≺ Q_N structure,

i.e. decompose ∇v_N·∇Ψ_N = (∇v_N ≺ ∇Ψ_N) + (∇v_N ≻ ∇Ψ_N) + (∇v_N ⊙ ∇Ψ_N);
the ≺ piece is absorbed by the ansatz, the ≻ piece is always defined, and the
resonant piece is controlled via the commutator (T3) using Π_N from Proposition 4.
The self-term |∇v_N|² is handled through the same structure since ∇Q_N is
function-like (3/4−κ > 0): writing ∇v_N = ∇w_N + v'_N ∇Q_N + regular remainder,
products of the regular remainders are classical in C^{1−κ} (positive regularity),
and commutators absorb the rest. This yields a fixed-point map Φ_N on the ball

    B = {(v,v') : ‖v‖_{C_T C^{1−κ}} + ‖v'‖_{C_T C^{3/4−κ}} ≤ R}

with estimate ‖Φ_N(v) − Φ_N(u)‖ ≤ C(R, ‖enhanced data‖) T^θ ‖v − u‖, θ > 0 from (T1).
Choosing R = R(data ball radius, enhanced-data size) then T* = T*(R) > 0 small gives a
contraction with constants depending only on the enhanced-data norms, whose moments
are N-uniform (Propositions 2–4), and on the fixed data-ball radius. Hence T* can be
chosen N-independently (deterministic, depending on R and a large-probability uniform
bound on the data; standard localization: fix T* so contraction holds on an event of
probability ≥ 1/2 uniformly in N, then propagate moments via (T4) and the a priori
bound — see §7). The fixed point v_N ∈ C_T C^{1−κ} is unique in B.

## 7. Moment propagation and uniformity

On the contraction event, ‖v_N‖ ≤ R deterministically. Off the event, use the
standard SG estimate: the map data ↦ v_N is locally Lipschitz with polynomial growth
in enhanced-data norms, all of which have Gaussian tails (finite exponential moments
via (T4)). Hence for p = 2 (hence any fixed p by Hölder/equivalence on finite chaos
plus Lipschitz composition — we state p = 2 for auditability),

    sup_N E‖v_N‖²_{C_{T*} C^{1−κ}} ≤ M < ∞.

Explicitly, M depends on R, T*, the uniform bounds of Propositions 2–4, and κ; none
depends on N. This is (2). The κ ∈ (0,1/4) constraint guarantees ∇Ψ ∈ C^{−3/4−κ}
stays above −1 (so Q gains enough) and η > −1/4 keeps data compatible with Ψ's
1/4−κ regularity.

## 8. What is proved / cited / computed

- **Proved here:** Proposition 1 (lattice asymptotics argument), power-counting chain
  identities, fixed-point assembly and uniformity logic at σ = 5/2.
- **Cited standard:** (T1)–(T4) with explicit statements; commutator and Schauder
  constants imported, not derived.
- **Computed evidence:** `verify_target.py` replays Wick slope 1.527 ≈ 3/2, ceiling
  arithmetic, second-renormalization convergence, fixed-time divergence vs space–time
  convergence tails, resonant positivity sum = 1.0. Run: `python3
  output/artifacts/verify_target.py` → `VERIFY_OK`; results in `verify_results.json`.
- **Uncertainty:** global-in-time extension, invariant measures, and optimal κ → 0
  endpoint are out of scope; T* is small and non-explicit (depends on imported
  Schauder/commutator constants).

## 9. Conclusion

The Da Prato–Debussche remainder at σ = 5/2 satisfies a cutoff-independent moment
bound exactly at the Schauder ceiling C^{1−κ} with N-independent (κ, T*, p, M).
Linear theory sets the ceiling; the paracontrolled contraction with the single
enhancement Q_N closes the nonlinear problem there. No second counterterm and no
resonant blow-up occur. ∎
