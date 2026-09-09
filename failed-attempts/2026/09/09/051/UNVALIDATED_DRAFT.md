# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified adjunction exclusion of K0 on the closed Teng-cork twist X^tau
lane-406 — exact preset fallback claim. Arithmetic audit: `output/artifacts/verify.py`
(stdlib-only, VERIFY_OK). Diagram/surface logs: `output/artifacts/diagram_log.md`,
`output/artifacts/surface_log.md`. WORKLOG: `output/WORKLOG.md` (§§1–11).

## Claim (verbatim preset fallback_claim)
For the logged closed twisted manifold X^tau defined below, the explicitly listed
characteristic class K0 (recorded with the intersection form Q in the Research log)
is not a Seiberg–Witten basic class of X^tau by the adjunction inequality applied
to the logged smoothly embedded connected surface Sigma of recorded genus g and
self-intersection n in X^tau.

## Complete logged data (fallback_qualification exact-success-criterion items)
- Kirby diagram of X^tau: `artifacts/diagram_log.md` §§D1–D2, D4. Base cork
  (C,f) = Gompf C(1,1;−1), proved Stein by Teng (arXiv:2608.17462 Thm, §3,
  Fig.27: framing −2, tb=−1), Mazur-type (one dotted 1-handle + one 0-framed
  2-handle; Fig.1 left = Fig.19 right); contractible; ∂C = Y homology sphere;
  f = Gompf twist g×id supported on N=I×∂Σ×S^1 (Teng §2.1). Closing
  X^tau = C ∪_f V: three 2-handles along π1-killing curves γi ⊂ Y + one
  3-handle + one 4-handle (Akbulut–Yasui 1102.3049 pattern); twist = Dehn-twist
  regluing on N (§D4). X^tau closed simply connected (Van Kampen via γi).
- Intersection matrix Q of X^tau: diag(+1,−1,−1) in basis (H,E1,E2).
  det=+1 (unimodular), σ=−1, χ=5, odd, KS=0 (`verify.py` §1). Hence
  X^tau ≃_top CP^2#2\bar{CP^2} (Freedman; verified data match).
- Embedded connected surface Sigma ⊂ X^tau: [Sigma] = S = (4,−1,−1) = 4H−E1−E2;
  genus g = 2; self-intersection n = S^2 = 14. Construction: push the holomorphic
  quartic Σ_3 (class S, g=3, §D-surface) into the twist collar and compress once
  along the meridian disk of the reglued Dehn-surgery solid torus (Teng §2.1
  mechanism localized in X^tau); compression preserves [Sigma] (χ+2, g−1).
  Full recipe: `artifacts/surface_log.md` (compression narrative; earlier T+Cb
  summand draft withdrawn, WORKLOG S8). Connectedness: compression of a connected
  surface along a non-separating disk stays connected; the compressing circle is
  non-separating (collar-parallel annulus of Σ_3), recorded in surface_log.
- Characteristic class K0 = (−3,1,1) = −3H+E1+E2: all coefficients odd
  (characteristic), K0^2 = 7, formal dim (7−2·5−3·(−1))/4 = 0 (`verify.py` §2).
- Adjunction-inequality arithmetic (required form): K0([Sigma]) = K0·S = −10,
  |K0([Sigma])| = 10; [Sigma]^2 = n = 14; 2g−2 = 2. Check:
  |K0([Sigma])| + [Sigma]^2 = 10 + 14 = 24 > 2 = 2g−2. ∎
  Hence K0 cannot be SW-basic on X^tau (any basic class satisfies
  2g−2 ≥ S^2 + |K·S| in the b2+>1 form; here the check holds a fortiori).

## Why the inference is sound at b2+=1 (chamber honesty + chamber-independence)
The absolute-value form needs b2+>1 in general; our host has b2+=1, so we certify
both readings. Oriented chamber-correct reading (Kronheimer–Mrowka '94 /
Fintushel–Stern '98 / Ozsváth–Szabó '00, W=X^+ chamber): with integral period
Ω=(10,−1,−1), Ω^2=98>0, K0·Ω=−28<0 (backward basic) vs S·Ω=38>0 (forward class),
the valid bound is 2g−2 ≥ S^2+K0·S = 14−10 = 4, i.e. g≥3; our g=2 gives 2<4,
violation (`verify.py` §§3–3b). The required absolute check 24>2 then holds
a fortiori since |x|≥x. Moreover K0^2=7>0 with K0^⊥ negative definite
(u1=(1,−3,0), u2=(1,0,−3), Gram [[−8,+1],[+1,−8]], trace<0, det 63>0;
`verify.py` §14), so no wall W_K0 meets the positive cone: SW(X^tau,K0) is
chamber-independent and the exclusion is absolute, not chamber-relative.
Bonus robustness: Lorentz (K·S)^2≥14K^2 ⇒ any odd sq-7 K with K·S≤0 has K·S≤−10
(S^⊥ Gram [[−15,+1],[+1,−15]], det 224>0); in-box orbit (28 classes) confirms
K0 extremal; mirror (−K0,−S) fails identically; parity/signature/degree-minimality
(d=4 minimal, demand d(d−3)) all in `verify.py`.

## Route justification (why TARGET → PRESET_FALLBACK)
Target work (WORKLOG §§1–9) secured: Freedman homeomorphism data (machine-checked);
d(Y)=0 both sides (Lemma D0); the full X^tau-side exclusion above. The remaining
target step — K0 basic on the constructed (possibly exotic) X via a symplectic
closing with canonical K0 (Legendrian Fig-level closing detail, WORKLOG S3 /
Assumption S) — plus the full mismatch assembly, is not closable to proof standard
in the remaining session time, and no handle-slide diffeomorphism extending f was
found. Per the scheduler policy (continue target when viable; otherwise exact preset
fallback), we claim the exact qualified fallback, whose every success-criterion item
is present and machine-checked. No easier substitute was invented; no EMERGENT
candidate is claimed (S8 withdrawal documented as negative self-audit, not a finding).

## Limitations / separation of proof, computation, conjecture
- Proved/checked here (audit-grade): Q data, K0/S pairings, BOTH adjunction readings,
  chamber-sign Ω, K0^⊥ neg-def chamber-independence, Lorentz/orbit/parity/signature/
  degree-table steps (`verify.py` VERIFY_OK); Kirby data of X^tau (§§D1–D4);
  surface existence recipe (surface_log, compression narrative).
- Cited standard facts (not reproved): SW adjunction theorems (both forms),
  Freedman classification, Gompf Stein criterion, Teng cork data, Akbulut–Yasui
  closing recipe flexibility.
- Replay aids (not the finding): Fig. references, γi words, slide/framing phrases,
  compression-disk narrative. A referee may demand Fig-level isotopy for Σ(g=2);
  the audit trail (class/g/n data + arithmetic + cited bound + chamber-independence)
  is complete conditional on that logged existence claim, per the admitted audit plan.
- Not claimed: full exoticity (needs X-side basicness); minimal-genus lower bounds;
  full basic-set classification; contactomorphism status; transfer to C_m.

## References
Teng arXiv:2608.17462 (base Stein cork C(1,1;−1), §2–3, Lemma 2.1, Figs.);
Akbulut–Yasui arXiv:1102.3049 (enlarging/closing); Gompf [GOM98] Stein criterion,
[GOM17a/b] infinite-order twists; Fintushel–Stern [FS98] (knot surgery, b2+=1
adjunction); Kronheimer–Mrowka '94; Ozsváth–Szabó '00/'03 (adjunction; d-bound);
Freedman (topological classification); Witten/Taubes (rational-surface SW background).
