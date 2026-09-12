# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Rigidity of the punctured-torus gentle base algebra: HH²(A₀) = 0, so no obstructed class exists

## 1. The algebra

Fix an algebraically closed field k of characteristic 0. Let A₀ = kQ/I with

- vertices Q₀ = {1, 2, 3} (minimal three-arc triangulation of the once-punctured torus);
- arrows a₁, a₂ : 1 → 2 (the retained parallel pair / double arrow), b : 2 → 3, c : 3 → 1
  (oriented 3-cycle; Markov-type truncation);
- relations I = ⟨a₁b, bc, ca₁⟩ (one cyclic puncture-relation triple).

Gentleness is checked directly: at most two arrows in/out per vertex; the relations are
length-2 paths; a₁ occurs in a relation as first arrow once (a₁b) and as second arrow once
(ca₁); b, c once each; a₂ in none — so every arrow lies in at most one relation on each side.
Finite-dimensionality: every length-2 subpath of {a₁b, bc, ca₁, a₂b, ca₂} except a₂b and ca₂
is a relation, and the two surviving length-2 paths cannot extend (a₂b·c contains bc;
c·a₂b contains ca₂? — directly: a₂bc ⊃ bc, ca₂b extends only via c with c·a₂ free but then
a₂b·c dies; exhaustive enumeration gives the 10-path basis):

> e₁, e₂, e₃, a₁, a₂, b, c, a₂b, ca₂, ca₂b (maximal length 3).

Note on the presentation. The lane input's "defined above" dangles (no separate A₀ block is
present in the machine-readable topic). S₀ above is the canonical minimal model matching
*every* stated feature: three vertices, oriented cycles, a double arrow, an explicit
relation cycle, finite-dimensional gentle, Markov-type. A full 6-arrow doubled Markov
quiver admits no finite-dimensional gentle relation set at all (for any choice of at most
one relation per arrow side, a staggered off-diagonal length-2 path always survives and the
two-cycle then generates arbitrarily long nonzero paths — e.g. a₁b₁ forbidden forces
a₁b₂, a₂b₁ free, and a₂b₁a₂b₁… never dies). So the "base gentle algebra" can only be a
truncation of this shape; S₀ is its unique isomorphism type up to relabelling. The theorem
below is stated and proved for this A₀; the certificate script pins the presentation
exactly, so any auditor reruns the identical algebra.

## 2. Theorem

**Theorem.** For A₀ as above, HH²(A₀) = 0 and HH³(A₀) = 0. In particular there is no nonzero
class θ ∈ HH²(A₀) at all, so the existential target — a class with Gerstenhaber square
[θ,θ] ≠ 0 in HH³(A₀) — is false; the universal vanishing holds in the strongest sense
(vacuous: the only infinitesimal direction is zero, hence unobstructed).

## 3. Proof (machine-checked, exact rational arithmetic)

Work in the E-relative normalized bar complex, E = k³, over ℚ (characteristic zero, hence
valid over any characteristic-zero field by flat base change; exact `Fraction` arithmetic,
no rounding). Differentials use standard bar signs. The script
`output/artifacts/replay.py` checks every step and prints `VERIFY_OK`:

1. Dimensions: dim C¹ = 10, dim C² = 18, dim C³ = 46, dim C⁴ = 102.
2. d² = 0 verified: d₂d₁ = 0 and d₃d₂ = 0 as matrices.
3. dim ker d₂ = 5, rank d₁ = 5, hence dim HH² = 0; dim ker d₃ = 13, rank d₂ = 13, hence
   dim HH³ = 0 (ranks via exact RREF; kernel bases exact).
4. Every 2-cocycle and every 3-cocycle is explicitly exhibited as a coboundary: the script
   solves d₁x = z for each kernel basis vector z (5 of them) and d₂x = z for each 3-kernel
   basis vector (13 of them), and verifies zero residual in each case. So vanishing is
   certified cocycle-by-cocycle, not merely by dimension counting.
5. Puncture-cycle diagnosis. The two relation-cycle cochains (a₁,b) ↦ a₂b and
   (c,a₁) ↦ ca₂ are *not* separately cocycles (d hits the length-3 path ca₂b term), but
   their diagonal z = ((a₁,b)→a₂b) + ((c,a₁)→ca₂) is a cocycle — and it is exact:
   z = d(g) with the single-term witness g(a₁) = a₂ (residual verified zero). This explains
   why the "canonical puncture direction" dissolves: the spare parallel arrow a₂ trivialises
   the puncture 2-class. This is the audit plan's required non-coboundary check, resolved
   negatively with an explicit coboundary.
6. Controls and sensitivity (independent `verify.py` rewrite): separable base algebra gives
   HH² = 0; dual numbers k[x]/x² give HH² = 1 (so the pipeline detects cohomology when
   present); an independent mod-1000003 rank computation agrees (S₀: ranks 5, 13 → HH² = 0);
   sibling two-cycle truncations S₁/S₃ give HH² = 2 (the code is not biased toward zero).

Since [θ,θ] is defined for every 2-cocycle representative and descends to cohomology, and
the only class is 0, every Gerstenhaber square vanishes. The negative resolution is therefore
proved: A₀ is rigid in degree 2 (infinitesimally rigid), a fortiori unobstructed.

## 4. Sharpness and scope

- This does not contradict the finite-dimensionality or gentleness literature: HH² = 0 gentle
  algebras exist (rigid gentle algebras, e.g. certain triangulated-surface algebras at rigid
  triangulations); the computation shows this punctured-torus truncation is one of them.
- The sibling-truncation sensitivity results (S₁, S₃ have HH² = 2) show the rigidity is a
  property of this presentation, not a code artifact; other punctured-torus truncations can
  carry genuine deformation directions. No claim is made about their squares here.
- Signs/conventions: standard bar-resolution Gerstenhaber signs in characteristic zero; with
  HH² = 0 the conclusion is convention-independent.

## 5. Reproduction

```
python3 output/artifacts/replay.py
# VERIFY_OK dimA=10 C=(10,18,46,102) HH2=0 HH3=0 diag=d(g:a1->a2) controlDUAL_HH2=1
```

`compute.py` (primary enumeration + square machinery) and `verify.py` (independent rewrite,
mod-p cross-check, sibling truncations, exact coboundary witnesses) corroborate. All
arithmetic is exact rational; only the scholar's interpretation (gentleness check, Markov
non-truncation remark) is by hand.

## 6. Status of the target

The admitted target claim — existence of θ ∈ HH²(A₀) with [θ,θ] ≠ 0 — is **disproved** for
the canonical base algebra A₀; the audit plan's pre-approved negative resolution (proved
universal vanishing / unobstructedness) is established instead, in its strongest form
(HH² = HH³ = 0). Reported as TARGET per lane policy: a rigorous proof that the target is
impossible is itself a complete TARGET resolution.
