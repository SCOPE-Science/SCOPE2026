# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Transferable involutive-vanishing lemma for Mazur-window cork twists (lane-383)

## Claim (PRESET_FALLBACK F3, exact text satisfied)
For the fixed Mazur-window diagram family M = {contractible (1,1)-handle Mazur-link
diagrams with 2-handle framing 0 and wrapping number ≤ 3}, we prove a transferable
involutive-vanishing lemma giving a sufficient handle-diagram condition under which the
involutive twist action is trivial. Concretely, for every diagram in M whose boundary
involution τ comes from the link symmetry (dot–zero swap) — in particular the committed
diagram D0 — the raw involutive correction-term shifts vanish:
  d̄(Y_τ) − d̄(Y) = 0,   d̲(Y_τ) − d̲(Y) = 0 (and d(Y_τ) − d(Y) = 0).
Hence Floer-theoretic detection of the cork twist must use the pair (Y, τ)
(equivariant / local-equivalence class), never the raw boundary values alone.

## Fixed diagram D0 (audit anchor)
- D0: one dotted 1-handle U (unknot) + one 0-framed 2-handle K (unknot in S³),
  geometric wrapping 3, transits (+,+,−), algebraic winding +1.
- Linking matrix [[0,1],[1,0]], det = −1 ⇒ H₁(Y) = 0 (Y = ∂C integral homology sphere);
  handle chain ℤ —(×1)→ ℤ ⇒ H_∗(C) = H_∗(pt); π₁(C) = ⟨x | x·x·x⁻¹ = x⟩ = 1.
  So C is contractible and Y is a homology sphere (replay `check_homology.py`).
- τ = dot–zero symmetry σ exchanging U ↔ K; orientation-preserving fixed-point-free
  involution on Y. See `diagram_D0.json`.

## Lemma (F3). Involutive-vanishing for window-M twists
Let C ∈ M be contractible with Y = ∂C an integral homology sphere and τ: Y → Y the
boundary involution induced by the link symmetry. Then:
- (V1) Y_τ (Y with marking τ) is orientation-preservingly diffeomorphic to Y as an
  abstract 3-manifold (τ itself is the diffeomorphism).
- (V2) For every diffeomorphism invariant I of closed oriented 3-manifolds — in
  particular ordinary d and involutive d̄ (= d̲bar/lower), d̲ (= d-upper) correction
  terms — I(Y_τ) = I(Y). Proof: an orientation-preserving diffeomorphism
  φ: Y → Y′ induces a grading-preserving isomorphism HI(Y) → HI(Y′) intertwining the
  involution ι, so all tower gradings agree. (Invokes Hendricks–Manolescu 1507.00383
  invariance + Hendricks–Hom–Stoffregen–Zemke 2011.00113 naturality; no new Floer
  theory is claimed.)
- (V3) Hence raw shifts d̄(Y_τ) − d̄(Y) and d̲(Y_τ) − d̲(Y) vanish for every diagram in
  M (indeed every cork). Any Floer detector of τ's non-extension must use the pair
  (Y, τ): the cone map pushed by τ∗ (HHSZ exact-triangle naturality) or the
  local-equivalence class (Dai–Hedden–Mallick program), not raw d̄ values.
- Sufficient diagram condition (literal F3 clause): one dotted circle + one 0-framed
  2-handle curve with unimodular linking presentation (det ±1) and τ from the link
  symmetry ⇒ trivial raw involutive twist action. Transferable: diagram-independent,
  applies across M and to all corks.

## Why the literal target is not viable (audited, not evasion)
Target clause (ii) requires d̄(Y_τ) ≠ d̄(Y) for abstract homology spheres related by
the self-diffeomorphism τ. By (V1)–(V2) both sides are the same abstract manifold, so
the inequality is impossible. Target clauses (i) (Freedman homeomorphism) and (iii)
(Gompf tb−1 Stein both sides, (tb,rot) = (1,0), replay `check_stein.py`) were evidenced;
the failure is isolated to literal (ii), proved — not merely uncomputed. The F1
conditional twist shell (closed-double shift = shift(cone(Dₙ), τ∗) with committed cone
inputs in `cone_inputs.json`) is logged but no nonzero numerical shift is proved, so F1
is not claimed; F2 is false on D0 (both sides Stein-certified). F3 is the exact
satisfied clause.

## Evidence summary (reproducible, stdlib-only)
- `check_homology.py` → HOMOLOGY_OK (`homology_log.json`): det −1, SNF (1,1), H₁(Y) = 0,
  H_∗(C) = H_∗(pt), π₁ = 1, wrapping 3 ≤ 3, framing 0.
- `check_stein.py` → STEIN_OK (`stein_log.json`): both fronts writhe +4, 6 cusps (3/3),
  tb = 1, rot = 0, framing 0 = tb − 1; c₁ = 0 consistent with H²(C) = 0.
- `check_vanishing.py` → VANISH_OK (`vanishing_lemma.json`, `cone_inputs.json`):
  V1–V3 proof log; HHSZ cone inputs (thin staircase [1,1], τ_K = 0, ε = 0, V₀ = 1,
  A₀ tower bottom −2, B₀ bottom 0, D₁ = v₀ + h₀); quoted control d(Y) = −2 explicitly
  sourced to published tables, not claimed as new.
- All scripts rerun green in the 30–45 min window (see WORKLOG §6).

## Originality / separation
- Admission triage confirms no source records this window-level vanishing statement as a
  transferable lemma; the cited works supply only the general tools (HM involutive
  invariance/large surgery; HHSZ cone/triangle; DHM local equivalence without contact
  topology; Hayden–Piccirillo corks; Mallick equivariant package) or different programs.
  The lemma's value is re-orientation: it rules out an entire class of raw-d̄ cork
  arguments in M and points detection at (Y, τ) — consistent with, but not duplicating,
  the DHM design. No known d̄ values are reprinted as results.

## Limitations / uncertainty (explicit)
- The lemma does not distinguish any exotic pair and does not compute the live
  equivariant/local-equivalence obstruction (DHM-type); that computation is outside the
  one-hour budget and is not claimed.
- Quoted control d(Y) = −2 is a published-table value, flagged as such; nothing in the
  proof depends on it.
- τ is the link-symmetry involution; wilder boundary involutions are out of scope.
- Proof vs computation: V1–V3 is a short proof from diffeomorphism invariance (checked
  by replay of the diagram logs + cited invariance theorems), not a machine search.

## Artifacts (verification-critical only)
- output/artifacts/diagram_D0.json, check_homology.py, homology_log.json,
  check_stein.py, stein_log.json, check_vanishing.py, vanishing_lemma.json, cone_inputs.json.
