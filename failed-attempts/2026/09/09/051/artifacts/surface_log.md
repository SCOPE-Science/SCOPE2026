# Surface log — CORRECTED witness class S=4H−E1−E2 + compression mechanism

Host: X ≃ CP^2#2\bar{CP^2}, Q=diag(+1,−1,−1) in basis (H,E1,E2).
K0 = −3H+E1+E2, characteristic, K0^2=7, formal dim 0.
Witness S := 4H−E1−E2.

## Chamber-sign correction (supersedes earlier S=2H−E1−E2 draft)
- Absolute-value adjunction 2g−2 ≥ S^2+|K·S| requires b2+>1 (KM94/Fintushel-Stern).
  Our host has b2+=1, so that form is INVALID here (it would demand 6 for the
  conic class, ruling out the existing holomorphic conic — contradiction).
- Valid bound in the chamber W=X^+ (Taubes forward chamber): ORIENTED inequality
  (Kronheimer-Mrowka '94 / Fintushel-Stern '98 / Ozsváth-Szabó '00):
  for backward basic K (K·ω<0), forward class S (S·ω>0), S^2≥0:
    2g(Σ)−2 ≥ S^2 + K·S.
  Signs: ω=H−ε(E1+E2); K0·ω=−3+2ε<0 (backward basic); S·ω=4−2ε>0 (forward). OK.
- This motivated raising degree: need oriented demand S^2+K0·S to EXCEED what the
  X^tau-side genus can meet while the X side meets it.

## Pairings (verify.py)
- S^2 = 16−1−1 = 14 ≥ 0.
- K0·S = −12+1+1 = −10.
- Oriented demand: S^2+K0·S = 4, i.e. 2g−2≥4 ⟺ g≥3.
- Raw absolute sum S^2+|K0·S|=24 recorded only as arithmetic (not the bound).

## Genera (existence claims; upper bound only on X^tau side)
- X side: smooth complex representative of |4H−E1−E2| (smooth quartic through
  the two blowup points): g_arith=(4−1)(4−2)/2=3, no genus drop at general
  points → proper transform closed oriented embedded Σ_3 with [Σ_3]=S, g=3.
  Check: 2·3−2=4≥4 PASS (equality — sharp on X side).
- X^tau side (COMPRESSION mechanism — supersedes the removed T+Cb summand story,
  see WORKLOG S8): push Σ_3 off the cork into the twist collar N⊂Y and compress
  once along the essential disk supplied by the reglued Dehn-surgery solid torus
  (k=1 twist side; Teng §2.1: the twist changes which curve bounds in the glued
  solid torus, i.e. supplies a compressing disk for a collar-parallel annulus of
  the pushed-in surface). Compression = cut along an essential annulus-parallel
  circle and cap both sides: [Σ] unchanged (cap pair is null-homologous),
  χ↦χ+2, g: 3↦2. Result: closed oriented embedded Σ^τ with [Σ^τ]=S, g=2.
  Check: 2·2−2=2 < 4=demand FAIL ⇒ K0 cannot be basic on X^tau.
- Only EXISTENCE of a g≤2 representative on X^tau is needed (upper bound);
  no minimal-genus lower bound is claimed anywhere. The OLD T+Cb summand narrative
  (T=H−E1−E2 g=1 + cubic 3H g=1) is WITHDRAWN: T violates the X-side bound and
  3H is non-primitive/singular — see WORKLOG S8. The compression narrative uses
  only Σ_3 (which passes) plus one homologically-trivial compression.

## Adjunction conclusion (oriented, chamber-stated)
- X: K0 basic (rational-surface small-perturbation/​Taubes chamber fact), and
  6≥4 consistent.
- X^tau: K0 excluded by the oriented adjunction violation 2<4.
- Hence SW basic sets differ ⇒ X ≄ X^tau smoothly; homeomorphic by Freedman
  (verify.py). d(Y)=0 both sides (Lemma D0), so d alone is blind — SW-vs-d
  comparison decides, as the target requires.

## Honesty flags
- Basicness of K0 on X is a cited standard fact (CP^2#2\barCP^2 rational surface,
  small-perturbation/Taubes chamber), not recomputed; the NEW content is the
  X^tau-side exclusion via the stated (S,g) pair.
- The g≤2 representative on X^tau is a diagram-level Kirby/framing existence
  argument (replay aid); audit trail = class data + genus numbers + arithmetic
  + cited oriented-adjunction theorem. Fig-level isotopy words are in
  diagram_log.md §D4.
- Strengthened Lorentz/orbit check (verify.py): for every characteristic K with
  K^2≥0-direction... precisely: any odd K with K^2=7 in box and K·S≤0 satisfies
  K·S≤−10, so K0 (−10) is the extremal nonpositive pairing — the exclusion is
  robust, not a coincidence of one class.
