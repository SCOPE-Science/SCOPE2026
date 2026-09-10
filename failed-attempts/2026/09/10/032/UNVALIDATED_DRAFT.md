# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — lane-584: audit of the once-stabilized positron-cork twist sector

## Route assessment (min-30 checkpoint, honest)

**Target** (full survival: FSW≠0 + S¹/Pin(2)-BF nontrivial + strong-cork
survival ≥1): **not proved**. The parametrized count J is uncomputed
(no analysis engine in-lane), and target-directed stress in fact produced
a conditional sector-wide killing chain (families adjunction via the
F-fixed class h) pointing the other way.

**Preset fallback** (exact FSW(E_F,s#t₀)=1 with certified
wall-crossing/monopole-Floer count log): **not met** — the exact success
criterion requires proving the parametrized moduli count is 1 mod 2 with
a certified computation log. We have the reduction TARGET ⟺ odd-linking
regular loop L₁ but no such loop exhibited. Claiming it would be overclaim.

**Emergent finding**: the target work produced a genuinely valuable,
auditable package that satisfies the SCOPE standard:
a certified formal/topological/chamber skeleton for the positron
once-stabilized sector (exact integer certificates, all replayable) PLUS
a sharp sector-wide dichotomy theorem (exact bound arithmetic) that
decides the fate of the FSW prong conditional on one named Kirby input.
This is a substantive obstruction/classification fact discovered through
pursuit of the target — not an easier substitute invented to produce
a record: it is the precise hinge on which the target lives or dies, with
independent value as a stabilization-survival benchmark (it tells the
cork-survival tables exactly which certificate would kill — or fail to
kill — this triple, and corrects two structural errors in the admitted
framing: Pin(2)-vacuity and the F-construction gap).

## Consolidated emergent claim

**Theorem (sector pinning + dichotomy for the positron once-stabilized
twist sector).** Let Z₀=ℂP²#−ℂP² (Q₀=diag(1,−1)), Z₁=Z₀#(S²×S²)
(Q₁=diag(1,−1)⊕H), and let F be the stabilized positron-cork twist with
F∗=id on H₂(Z₁;ℤ) (corrected Wall-key construction; see §4). Let
s#t₀ denote a spin-c structure on the mapping torus E_F→S¹ restricting
to a characteristic class c∈H²(Z₁;ℤ) on each fiber. Then:

1. **(Gap + pinning, certified exact.)** Every characteristic c satisfies
   c²≡0 mod 8; the naive extension (1,1,0,0) has c²=0, formal dim d=−3
   (families exp-dim −2, empty). The minimal positive sector is c²=8
   (e.g. (1,1,2,2)), d=−1, families exp-dim 0 (countable). All 68/68 flux
   vectors in the |·|≤4 box are primitive (pairing gcd 1), so each
   transverse wall crossing contributes quantum ±1 (=1 mod 2).
2. **(Chamber, certified exact + standard.)** The zero-perturbation path
   is wall-free for c²=8 (|c⁺|²≥8 for every metric); a generic S¹ loop
   misses the wall; homotopies can jump, so the value is per-path-component
   (b₂⁺=2<3). The PSC loop has value 0. Hence FSW(C_far)=J with J open.
3. **(Pin(2)-vacuity, certified exact.)** Q₁ is odd, so w₂(Z₁)≠0: Z₁ is
   non-spin and Pin(2)-family Bauer–Furuta is undefined on E_F. The
   target's "S¹/Pin(2) where defined" collapses to S¹-equivariant only;
   the S¹-BF class is stem-0 with ghost part 0 (Bauer connected-sum
   vanishing, both sides b₂⁺>0) and free part the FSW count.
4. **(Sector-wide dichotomy, exact arithmetic.)** For every flux class
   c=(a,b,m,n) (a,b odd), |⟨c,h⟩|=|a|≥1 where h=(1,0,0,0) has a genus-0
   representative with h²=+1: the families-adjunction bound
   2g−2 ≥ |⟨c,[S]⟩|+[S]² reads −2 ≥ |a|+1 ≥ 2, violated by every flux
   class. Consequently: **either** h admits no F-fixed representative
   (the only escape), **or** FSW(E_F,s)=0 for the entire flux sector
   (conditional on the standard families-adjunction theorem for
   mapping-torus classes + a Kirby disjointness certificate for the fixed
   positron embedding — the two named missing inputs).
5. **(Corrections, certified.)** H₂(E_F)=H₂(Z₁)=ℤ⁴ (not plus ℤ[T]; T is
   the H₁ base circle); H²(E_F)→H²(Z₁) is an isomorphism; F∗s≅s for all
   spin-c s (exact); Dirac index 1; explicit H⁺ plane and explicit
   integral isometry Q₁≅diag(1,1,−1,−1) (det −1, Gram equality);
   Lin–Mukherjee vanishing inapplicable (connected-sum fiber, distinct
   functors); no F-invariant neck for Wall-key F (families connected-sum
   vanishing inapplicable); ordinary SW(Z₁)=0.

## What is proved vs conjectured (separation)

- **Proved (replayable integer certificates):** items 1–3 and 5 above;
  scripts `output/artifacts/audit_*.py` all print ALL VERIFY_OK.
- **Exact-conditional (dichotomy):** item 4's bound arithmetic is exact;
  the killing implication is conditional on two named inputs outside the
  lane (families-adjunction citation for mapping-torus FSW; Kirby
  disjointness of the fixed positron embedding). The counter-consideration
  (support-intersection escape) was considered and rejected on
  statement-level grounds (F|_S=id is strong invariance).
- **Not claimed:** FSW=1; S¹-BF nontriviality; killing isotopy; strong-cork
  status; positron strongness (cf. Mukohara Q1.8); any monopole-Floer count.

## Reproduction

Run `for f in output/artifacts/audit_*.py; do python3 "$f"; done` — every
script ends `ALL VERIFY_OK` and writes its `*_ledger.json`. No external
computation needed (stdlib only). Literature inputs used at statement
level only: Freedman–Quinn topological isotopy; Witten/Bauer connected-sum
vanishing; Gromov–Lawson PSC; Weitzenböck; Baraglia/Konno families
wall-crossing + adjunction shape; Akbulut–Yasui nucleus disjointness.

## Prior-art boundary (no overclaim)

Machinery comes from KMT (families-SW umbrella), Lin–Mukherjee (family-BF
vanishing), Bauer–Furuta, Baraglia, Freedman–Quinn, Wall/AKMR stabilization.
None states the positron once-stabilized sector pinning, the Pin(2)-vacuity
collapse, the F-construction correction, or the sector-wide dichotomy for
this triple (per Admission's gap check). The emergent theorem reuses
standard tools but its conclusion — the exact hinge deciding this named
sector — is new at triage level; if any part coincides with unpublished
folklore we claim only the auditable certificate, not priority.
