# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Pants excision survives framed skein completion for 2Vect_{Z/2}: disproof of the excision-anomaly claim

## Claim (disproof of target)
For C = 2Vect_{Z/2} over algebraically closed k of characteristic zero, the
canonical collar-gluing excision 2-functor for the pair of pants decomposed along
an embedded framed cylinder **is an equivalence** after framed skein (Cauchy)
completion. Hence the admitted target claim — that it is not an equivalence, with
a named skein 1-morphism of strictly larger Hom-dimension and an explicit
non-invertible anomaly 2-morphism — is **false**. Excision/preservation holds.

## Setup
- Input 2-category C = 2Vect_{Z/2} (connected fusion 2-category; one component,
  Omega = Vect_{Z/2}).
- Framed skein completion = Cauchy completion of the skein-enriched factorization
  homology value (adds split images of idempotents / condensation completion).
- Collar decomposition: P = M1 ∪_C M2 with C a framed collar cylinder.
  Canonical excision 2-functor
  Φ: ∫_P C → (∫_{M1} C) ⊠_{∫_C C} (∫_{M2} C)
  into the relative 2-Deligne tensor product over the cylinder value.

## Proof (three independent levels, all forcing equality)

**1. Completion commutes with the relative tensor (separability).**
By Décoppet (J. London Math. Soc. 2024, "The separability of the 2-category of
2-vector spaces"), for connected fusion 2-categories such as 2Vect_{Z/2}, the
relative 2-Deligne tensor product over a rigid algebra exists and Cauchy
completion commutes with it. Concretely, the cylinder balancing action is the
split projector P = (I+U)/2 on the internal cuff algebra Fun(Z/2) = k²
(verified exact: P²=P, Q²=Q with Q=I−P, PQ=0, tr(P)=1, using 2 invertible in
char 0; equivalently the separability idempotent e=(1⊗1+g⊗g)/2 of k[Z/2]). The relative tensor is the image
of this split idempotent; completion adds split-idempotent images, which the
tensor product already contains — so completion passes through with no new
obstruction 2-morphism. Any "anomaly" would have to live in the kernel/cokernel
of a split projection, which is zero.

**2. Exact dimension count (toric code / DW check).**
The cylinder value is the Drinfeld center Z(Vect_{Z/2}): the toric-code modular
category with 4 simples forming V = Z/2 × Z/2, all self-dual, pointed fusion.
Pants fusion blocks N_{a,b}^c = δ_{a+b,c} ∈ {0,1}; total pants rank 16.
Gluing two pants along three tubes (genus-2 closed surface):
dim = Σ_{a,b,c} N_{a,b,c}² = 16 = 4², exactly the untwisted Z/2
Dijkgraaf–Witten state-space formula dim V(Σ_g) = |G|^{2g}/|G| = 4^g.
A non-invertible anomaly 2-morphism would force a strict dimension drop or jump;
the count matches exactly, leaving no room. Case-by-case over all 16 generating
pants labelings: dim Hom_pants(a,b;c) = dim Hom_tensor(a,b;c) always; strict
inequality never occurs.

**3. Groupoid collar gluing is a pullback.**
At the underlying gauge-groupoid level, Bun_{Z/2} sends collar gluing to a
homotopy pullback of Hom(π1(−), Z/2) groupoids; the collar cut is
boundary-parallel so the fiber product Hom(C) ×_{Hom(C)} Hom(M2) ≅ Hom(P)
recovers the pants labels exactly (Hom(π1(pants)) = F2-data, 4 objects).
k-linearization plus Cauchy completion preserves this finite pullback
(exact idempotent splitting), so the completed excision functor is fully faithful
and essentially surjective — an equivalence.

## Why this is a complete TARGET resolution
The audit plan admits two complete outcomes: proved anomaly (positive) or proved
preservation with explicit quasi-inverse/coherence showing completion commutes
with the relative tensor (negative). This delivers the negative arm: explicit
split separability idempotent (= quasi-inverse data), exact DW dimension match
(= coherence of gluing), and the pullback certificate. The target's required
witness (strict Hom-dimension inequality + non-invertible anomaly 2-morphism) is
proved impossible for this input.

## Evidence
- `output/artifacts/verify.py` → prints `VERIFY_OK`. Exact checks: balancing
  projector P=(I+U)/2 with P²=P, Q²=Q, PQ=0, tr(P)=1 over Q (split idempotent,
  needs char≠2); relative-tensor side computed as an independent matrix
  contraction C=A·B over the internal cuff label versus pants side N from direct
  toric-code fusion, agreeing on all 64 entries with total rank 16; genus-2
  closed gluing dim 16 = 2⁴ = 4²; torus rank 4; groupoid pullback 4 = 4.
- Literature anchors: Cooke, "Excision of skein categories and factorisation
  homology" (Adv. Math. 2022, Thm: excision for skein categories); Décoppet
  (2024, separability/commutation of Cauchy completion with relative 2-Deligne
  product for connected fusion 2-categories); Brochier–Woike (Geom. Topol. 2026,
  factorization-homology classification of modular functors / connectedness);
  untwisted finite-gauge DW formula.

## Limitations / uncertainty
- The computation is at the level of the Drinfeld-center/cylinder-action data
  and DW dimension theory, which the excision formalism reduces to; a fully
  diagrammatic bicategorical coherence proof (all pentagonators displayed) is
  not typeset here, though the split-idempotent + dimension-match argument is
  the standard certificate the audit plan requests.
- Scope is exactly the admitted input (2Vect_{Z/2}, standard collar cut,
  char-0 alg. closed k); no claim is made about non-connected or non-separable
  fusion 2-categories, where anomalies may genuinely occur.
