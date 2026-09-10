# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Obstruction and exact-pin package for the Teng Stein-cork twist cell in the Dolgachev surface E(1)_{2,3}

## Claim (emergent — obstruction + exact pins, NOT an exotic-pair proof)

Let X = E(1)_{2,3} (Dolgachev surface, e = 12, σ = −8, b₂ = 10, (b₂⁺, b₂⁻) = (1, 9)),
with intersection pairing presented charitably as Q_X = (−E₈) ⊕ N,
N = [[0,1],[1,−1]] (fiber F² = 0, section S² = −1, F·S = 1).
Let W₁ := C(1,1;−1) be the first (Mazur-type) member of the Teng (2026)
infinite-order Stein cork family, with cork automorphism f (infinite-order
torus twist), and let ξ be the Stein-induced contact structure on Y = ∂W₁
from the fixed Legendrian diagram (Teng Fig.37/Fig.20240420-23: framing −2, tb −1).
Then:

1. **Canonical-class pin (exact, chamber-clean).** The class K_X = −F satisfies:
   K_X² = 0 = c₁²(X); K_X is characteristic (10/10 basis rows exact);
   formal SW dimension d(K_X) = (K_X² − 2e − 3σ)/4 = 0; and the b₂⁺ = 1 wall
   W_{K_X} is EMPTY (hence SW(−, K_X) is chamber-independent — the usual b₂⁺ = 1
   chamber worry is a non-issue for this class). Exact label: in the (−E₈, F, S)
   basis K_X = (0⁸, −1, 0); in the diagonalized block basis K_X = (0⁸, −1, +1).
2. **Twist-side inheritance (formal, exact).** For any contractible cork twist
   X_f with homology-sphere boundary, the Mayer–Vietoris + Van Kampen argument
   gives H₂(X − int W) ≅ H₂(X), Q_{X_f} = Q_X, π₁(X_f) = 0, hence a canonical
   isometry H²(X_f) ≅ H²(X) sending K_X to a well-defined K_f with K_f² = 0,
   K_f characteristic. Freedman (Q, KS) = (same, 0) then gives X_f homeomorphic X.
3. **Mechanism obstruction (proved).** Twist-knot Alexanders for k = 0..8 are
   pairwise distinct (exact), and only k = 0 has Alexander 1. Hence the quoted
   Fintushel–Stern knot-surgery mechanism — the mechanism of Teng's own torus-twist
   construction — preserves SW nonvanishing and can NEVER produce an SW = 0 twist
   side from an SW-nontrivial base. A Teng-W₁ vanishing twist would need a
   rational/PSC identification of X_f; none is sourced (the only sourced vanishing
   twist in E(1)_{2,3} is Akbulut's positron/W̄₁ cork with N ∪_f W = E(1), a
   different cork: honest-negative diagram comparison logged).
4. **Boundary d₃ baseline + contactomorphism dilemma (exact + logical).**
   d₃(ξ) = −1/2 exactly (e(W₁) = 1 − 1 + 1 = 1, σ = 0, H²(W₁) = 0 ⇒ c₁ = 0;
   (0 − 2 − 0)/4; rotation-independent). DISCLOSED LIMITATION: this number is
   a universal constant for EVERY contractible compact Stein 4-manifold
   (χ = 1 ⇒ e = 1; H₂ = 0 ⇒ σ = 0, c₁ = 0), verified in-work by direct
   computation — so its novelty is NOT cell-specific; its value here is as a
   fixed baseline plus the dilemma below. The fallback's hoped-for
   d₃(f_∗ξ) = +1/2 is unreachable from the fixed diagram: it would need a Stein
   filling with c₁² − 2e′ − 3σ′ = 2 (none sourced), and the only honest route —
   proving f a contactomorphism — would force d₃(f_∗ξ) = d₃(ξ) = −1/2,
   contradicting distinctness. (Teng's closing Question confirms f's
   contactomorphism status is open.)
5. **Clause repair + embedding gap (exact + sourced).** The literal target clause
   "Q_X = −E₈ ⊕ H ⊕ nucleus" is defective as written (parity: −E₈, H even vs
   Dolgachev odd; rank 8 + 2 + ≥1 ≥ 11 > b₂ = 10); the charitable −E₈ ⊕ N is odd,
   det −1, rank 10, σ −8, with exact N-diagonalization PᵀNP = diag(+1,−1),
   det P = +1. Separately, no source embeds Teng C(1,1;−1)/C_m into E(1)_{2,3}
   (Teng: E(n), n ≥ 2 via 6n vanishing cycles; Akbulut–Yasui: general method,
   no such cell).

## What is proved / quoted / open (strict separation)

- **Proved (machine-checked, replayable):** N1 (characteristic 10/10), N2 (d = 0),
  N3 diagonal wall-empty step, D1/D2/D3 (N-diagonalization, block congruence,
  K coords), F1 (K_f inheritance), F2 (sign-rule exponent (12−8)/4 = 1, odd),
  M1 (Mazur presentation [±1] unimodular), M2 (contractible ⇒ homology-sphere
  boundary via PL+LES), T1 (trefoil Δ = t − 1 + t⁻¹, coeffs ±1), I1/I2
  (twist-knot Alexanders k = 0..8 distinct; no Alexander-1 for k ≥ 1),
  P1/P2 (literal-Q parity defect + rank overflow), E2/E3 (E(1)→Dolgachev
  numerics), d₃(ξ) = −1/2, SW sign-robustness, KS = 0 = 0, Rochlin consistency.
- **Quoted (standard, cited not re-derived):** Freedman (Q, KS); Serre odd
  indefinite classification; O(1,9) null-cone transitivity; Taubes
  symplectic nonvanishing; FS98 knot-surgery formula + distinction (b₂⁺ > 1
  sharp; b₂⁺ = 1 chamber version flagged); log-transform e/σ invariance;
  Donaldson/Morgan–Mrowka homeomorphism type; Gompf tb−1 Stein criterion and
  d₃ formula; Teng Aux lemma (winding-1, P(U) = U ⇒ contractible); Mazur-type
  acyclic + simply-connected ⇒ contractible; UCT; Rochlin spin-only;
  E(1)_{2,3} = E(1)_trefoil identification (Akbulut 0805.1524 p.118);
  Akbulut positron theorem E(1)_{2,3} = N ∪ W, N ∪_f W = E(1) (0805.1524).
- **Open (explicitly NOT claimed):** SW(X_f, K_f) = 0 for Teng W₁; any
  Teng-W₁ embedding into E(1)_{2,3}; any X_f identification; d₃(f_∗ξ);
  whether f is a contactomorphism; any closed exotic pair. The target's full
  SW twist-or-trivial certificate is NOT established here.

## Evidence summary (artifacts; replay)

All verifiers replay with `python3 output/artifacts/<name>` (stdlib + sympy):

| artifact | content | status |
|---|---|---|
| verify_target.py → target_audit.json | Dolgachev numerics; Q grams (−E₈/H/N/block); Stein pins; SW quote table; gap list | PASS (target_closed: false) |
| verify_target2.py → target_audit2.json | L1 K_X = −F exact solve; L2 MV+VK invariance; L3 gap | PASS |
| verify_target3.py → target_audit3.json | P1/P2 literal-Q defect; P3 charitable repair; P4 N≄H; P5 chambers | PASS |
| verify_target4.py → target_audit4.json | twist-knot Alex k = 0..8; I2 no-Alex-1; blockers B1–B6 | PASS |
| verify_target5.py → target_audit5.json | T1 trefoil; T2 quote chain; T3 formal iso; T4 K² = c₁² | PASS |
| verify_target6.py → target_audit6.json | M1 unimodular; M2 PL/LES; M3 wiring | PASS |
| verify_target7.py → target_audit7.json | N1 characteristic; N2 d = 0; N3 wall-empty; N4 blockers | PASS |
| verify_target8.py → target_audit8.json | E(1)→Dolgachev numerics from scratch | PASS |
| verify_target9.py → target_audit9.json | F1 K_f inheritance; F2 sign rule; F3 cork-identity test; F4 ledger | PASS |
| verify_target10.py → target_audit10.json | S1 KS; S2 Freedman; S3 Rochlin; S4 binary ledger | PASS |
| verify_target11.py → target_audit11.json | D1/D2/D3 exact diagonalization | PASS |
| verify_fallback.py → fallback_audit.json | d₃(ξ) = −1/2 exact; f-side FAIL (honest) | PASS (pair criterion NOT met) |
| verify_emergent.py → emergent_assess.json | V1–V5 route-decision assessment | PASS |

Fixed diagrams: Teng Fig.20240604-1-left (Mazur-type, 0-framed) + Fig.37/
Fig.20240420-23 (Legendrian −2/−1) + Aux lemma; Akbulut 0805.1524 Figs.40–44
(positron/W̄₁, N ∪_f W = E(1)).

## Independent value (retrieval use)

A future researcher on (i) Teng-family cork twists, (ii) Dolgachev SW chambers,
(iii) cork-boundary contact invariants, or (iv) knot-surgery vanishing attempts
retrieves: the exact chamber-clean label K_X = −F (removes a real b₂⁺ = 1 worry);
a proved no-go for the knot-surgery vanishing route (I2/B5); the fixed
d₃(ξ) = −1/2 baseline (universal contractible-Stein constant, disclosed as such)
with the contactomorphism dilemma constraining any f_∗ξ computation;
the charitable Q_X repair (blocks citation of a defective form); and the sourced
embedding gap (blocks assuming Teng-in-E(1)_{2,3}). Each is reusable obstruction/pin
input independent of any closed exotic result.

## Originality note

No validated prior covers this package: Teng (2026) logs no SW/d₃ values and leaves
the contactomorphism Question open; Akbulut–Yasui give a general machine with no
Teng-W₁-in-E(1)_{2,3} cell; Akbulut 0805.1524's vanishing twist uses a different
cork; Karakurt–Oba–Ukida treat older Mazur corks; SCOPE095 (different cork, SW = 0
both sides) and SCOPE072 (different domain) do not imply it. Classical ingredients
(trefoil Alexander, Gompf d₃ formula, E(1) numerics, standard classifications) are
quoted, not claimed as new; novelty is the cell-specific composition plus exact
machine-checked labels and the proved negative results.

## Limitations

Conditional on quoted standard theorems and on Teng's diagram/Aux-lemma pins as
cited; the (−1)-section geometric representative is needed for the −F label
(robustness test logged: a (−2)-section variant collapses the label to 0, K² = 0
stable); no claim is made on SW(X_f, K_f), the Teng embedding, X_f, d₃(f_∗ξ),
contactomorphism status, or any exotic diffeomorphism distinction.
