# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Integral secondary-stability gap in H3 for Conf_5 → Conf_6 of Theta_(2,3,4): Disproof

## Claim (negation of the target)

Let `Theta_(2,3,4)` be the theta graph (two branch vertices joined by three
internally-disjoint arcs with 2, 3, 4 edges respectively) and let
`B_n = UConf_n` denote unordered configuration space, per the audit plan.
Then for every `n`:

```
H_3(B_n(Theta_(2,3,4)); Z) = 0.
```

In particular `H_3(B_5;Z) = H_3(B_6;Z) = 0`, the edge-stabilization map

```
s_*: H_3(B_5;Z) → H_3(B_6;Z)
```

is the zero map `0 → 0` (for **any** choice of stabilizing edge), its cokernel
is `0` (hence does **not** contain `Z/2`), and `s_* ⊗ Q` is surjective
vacuously. No nonzero Morse 3-cycle witness exists. The target conjunction is
**false**.

## 1. Setup

Write `Γ_sub` for the subdivided model: vertices
`a, b` (branch points) plus `1 + 2 + 3 = 6` bivalent subdivision vertices,
`8` vertices and `9` edges total, `χ = 8 − 9 = −1`, valences `(3,3,2⁶)`.
Write `Γ_min` for the smoothed (minimal) theta: `2` trivalent vertices joined
by `3` parallel edges, `χ = 2 − 3 = −1`.

Subdivision/smoothing is a homeomorphism of underlying spaces. Since
unordered configuration spaces are homeomorphism-functorial, there is a
homeomorphism `B_n(Γ_sub) ≅ B_n(Γ_min)` for every `n`, hence identical
integral homology. (In the language of An–Drummond-Cole–Knudsen,
arXiv:1806.05585 §2.1, smoothing is a graph morphism and a homeomorphism;
Theorem 2.10 gives the same identification via the Świątkowski complex.)

## 2. Reduced Świątkowski complex degree bound

We use the reduced Świątkowski complex (ADK Definition 2.11):

```
~S(Γ;R) = R[E] ⊗_Z ⊗_{v ∈ V} ~S(v),
```

where `~S(v) = span{∅} ⊕ span{h_i − h_j}` with `|∅| = (0,0)` and
`|h_i − h_j| = (1,1)` (degree, weight). The inclusion
`~S(Γ;R) ⊆ S(Γ;R)` is an `R[E]`-linear quasi-isomorphism (ADK §2.3;
`R = Z` is [ADK2, Prop 4.9]), and
`H_*(B(Γ);R) ≅ H_*(~S(Γ;R))` as bigraded modules (ADK Theorem 2.10).

Lemma. For any graph, the homological degree-`d` piece of `~S(Γ)` is spanned
by choices of `d` **distinct** vertices at which a difference-generator
`h − h'` is taken (degree 1 each), `∅` elsewhere, times a monomial in `Z[E]`
(degree 0). Hence `C_d = 0` for `d > #{v : val(v) ≥ 2}`.

Proof. Each `~S(v)` is concentrated in degrees 0 (`∅`) and 1 (differences;
empty if `v` is univalent/isolated). The tensor product over `v` adds degrees,
so degree equals the number of vertices contributing a degree-1 factor. ∎

## 3. Vanishing

Apply the Lemma to `Γ_min`: it has exactly 2 vertices, both of valence 3.
Each contributes at most degree 1. Hence:

```
C_d(~S(Γ_min)) = 0 for all d ≥ 3, in every weight w.
```

Enumerated explicitly: a degree-3 generator would need 3 distinct vertices;
`C(2,3) = 0` choices; times any edge-monomial count gives `0`. The replay
script certifies `dim C_3 = 0` at weights 5 and 6 (indeed all weights).

Since `H_3 = ker(∂_3)/im(∂_4) = 0/0 = 0`:

```
H_3(B_n(Γ_min); Z) = 0 ∀n ⇒ H_3(B_n(Theta_(2,3,4)); Z) = 0 ∀n.
```

The same holds with any coefficients (universal coefficients), in particular
over `Q`.

## 4. Stabilization cokernel

Both domain and codomain of `s_*` are `0`, so `s_*` is `0 → 0`:

- `coker(s_*) = 0`, which contains no `Z/2` subgroup;
- `s_* ⊗ Q : 0 → 0` is surjective (vacuously);
- the chain group of 3-cycles is `ker(∂_3 : 0 → ·) = 0`, so no nonzero
  (Morse or singular) 3-cycle witness exists; the "explicit witness" clause
  is unsatisfiable.

Therefore the claimed "integral secondary-stability failure" (torsion cokernel
plus witness, contrasted with rational surjectivity) is impossible at this
graph in degree 3: the rational surjectivity holds only vacuously and there is
no integral gap. The literal target is **false**. ∎

## 5. Reproducibility

`output/artifacts/verify_theta_H3_vanishing.py` (stdlib only, `VERIFY_OK`):
§1 inventories the subdivided graph (8 vertices, 9 edges, `χ = −1`,
essential vertices `{a,b}`); §2 checks smoothing preserves `χ` and the
essential count; §3 enumerates the reduced degree-3 basis at weights 5, 6
(`hcombos = C(2,3)·2³ = 0`, so `dim C_3 = 0`); §4 records the cokernel logic.

## 6. Scope and limits

- "Conf" is read as unordered `B_n = UConf_n`, per the audit plan and
  fingerprint ("unordered configuration spaces"). No claim is made about
  ordered configurations.
- The proof cites (not re-proves) the ADK quasi-isomorphism
  `H_*(B) ≅ H_*(~S)` and homeomorphism-invariance of `B_n`; the new content is
  the degree-count applied to the theta graph and its consequence for `s_*`.
- Which edge carries the stabilization is irrelevant: any homomorphism
  `0 → 0` has trivial cokernel.
