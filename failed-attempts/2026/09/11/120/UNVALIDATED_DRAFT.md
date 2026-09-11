# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Triviality of the 2×2 interchanger holonomy loop in Gray-categories

## Theorem (target claim, proved)

Let `G_free` be the free Gray-category on the compatible 2×2 grid computad:
objects `P, Q, R`; 1-generators `f, f', f'' : P → Q`, `g, g', g'' : Q → R`;
2-generators `a : f ⇒ f'`, `c : f' ⇒ f''`, `b : g ⇒ g'`, `d : g' ⇒ g''`.
Let `χ_{b,a}`, `χ_{d,c}` be the Gray interchanger 3-cells (with fixed orientations)
and `L` the cyclic four-step whiskered loop

> `L = B₀⁻¹ ∘ A₁⁻¹ ∘ B₁ ∘ A₀ : S₀ ⇛ S₀`

defined in §2. Then `L` equals the identity 3-cell `id_{S₀}` on the common
composite 2-cell `S₀ : g∘f ⇒ g''∘f''`. In fact the equation holds in **every**
Gray-category, hence in particular in the free one. No hidden holonomy exists
around this minimal loop.

## 1. Preliminaries (only Gray-constitutive laws used)

We use only the following definitional Gray-category laws:

1. **Strict hom 2-categories.** Each hom `G(X,Y)` is a strict 2-category:
   objects = 1-cells, 1-morphisms = 2-cells with strictly associative/unital
   vertical composition `∘`, 2-morphisms = 3-cells with strictly
   associative/unital vertical composition, strictly functorial horizontal
   composition `*` satisfying strict middle-four interchange
   `(q' ∘ q) * (p' ∘ p) = (q' * p') ∘ (q * p)`.
2. **Strict 1-cell composition and strict whiskering functors.**
   1-cell composition is strictly associative/unital; whiskering a 2-cell or
   3-cell by a fixed 1-cell is a strict 2-functor, hence preserves `∘` strictly.
3. **Invertible interchangers.** For horizontally composable 2-cells
   `α : f ⇒ f'`, `β : g ⇒ g'` there is an invertible 3-cell
   `χ_{β,α} : (β*f') ∘ (g*α) ⇒ (g'*α) ∘ (β*f)`
   (either orientation convention; we fix this one and use `χ⁻¹` for the reverse).
   Invertibility `χ⁻¹ ∘ χ = id`, `χ ∘ χ⁻¹ = id` holds strictly at the 3-cell level.

No further coherence axioms, strictification theorems, or surface-diagram
isotopy slogans are invoked.

## 2. The grid, the corners, and the loop

Write whiskered atoms `g*a`, `b*f'`, `g'*c`, `d*f''`, etc. for horizontal
composites of a 1-cell with a generating 2-cell. Each atom is a 2-cell between
1-cells `P → R` (e.g. `g*a : g∘f ⇒ g∘f'`). The four corner 2-cells are the
vertical composites (all parallel, `g∘f ⇒ g''∘f''`):

- `S₀ = (d*f'') ∘ (g'*c) ∘ (b*f') ∘ (g*a)`
- `S₁ = (d*f'') ∘ (g'*c) ∘ (g'*a) ∘ (b*f)` (apply `χ_{b,a}` at positions 0–1)
- `S₂ = (g''*c) ∘ (d*f') ∘ (g'*a) ∘ (b*f)` (apply `χ_{d,c}` at positions 2–3)
- `S₃ = (g''*c) ∘ (d*f') ∘ (b*f') ∘ (g*a)` (apply `χ_{b,a}⁻¹` at positions 0–1)

and back to `S₀` by `χ_{d,c}⁻¹` at positions 2–3. The four steps are:

- `A₀ = id ∘ χ_{b,a} : S₀ ⇒ S₁` (top pair forwards),
- `B₁ = χ_{d,c} ∘ id : S₁ ⇒ S₂` (bottom pair forwards),
- `A₁⁻¹ = id ∘ χ_{b,a}⁻¹ : S₂ ⇒ S₃` (top pair backwards),
- `B₀⁻¹ = χ_{d,c}⁻¹ ∘ id : S₃ ⇒ S₀` (bottom pair backwards),

where `∘_H` denotes horizontal composition of 3-cells (along the middle
object, i.e. the 1-cell `m = g'∘f'`, inside the strict 2-category `G(P,R)`),
`∘_V` denotes vertical composition of 3-cells (along 2-cells), and `id`
denotes the identity 3-cell on the untouched vertical segment. The loop is
`L = B₀⁻¹ ∘_V A₁⁻¹ ∘_V B₁ ∘_V A₀ : S₀ ⇛ S₀`, compared against `id_{S₀}`.

Boundary and non-degeneracy facts (machine-checked): each consecutive atom
pair is vertically composable; all four corners are parallel with total
`g∘f ⇒ g''∘f''`; the four corners are pairwise distinct as factor lists;
each step acts on a disjoint adjacent factor pair from its neighbours
(positions 0 vs 2 alternately), so no adjacent pair cancels definitionally.

## 3. Disjoint-peak lemma and contraction

Split each corner as `V ∘ U` (lower segment `U`, upper segment `V`) at the
middle 1-cell `m = g'∘f'`:

- `U₀ = (b*f') ∘ (g*a)`, `U₁ = (g'*a) ∘ (b*f)`, with `α := χ_{b,a} : U₀ ⇒ U₁`;
- `V₀ = (d*f'') ∘ (g'*c)`, `V₁ = (g''*c) ∘ (d*f')`, with `β := χ_{d,c} : V₀ ⇒ V₁`.

Then `A₀ = id_{V₀} ∘_H α`, `B₁ = β ∘_H id_{U₁}`, `A₁ = id_{V₁} ∘_H α`,
`B₀ = β ∘_H id_{U₀}`, where `∘_H` is horizontal 3-cell composition in `G(P,R)`.

**Lemma (disjoint peaks commute strictly).**
`B₁ ∘_V A₀ = A₁ ∘_V B₀` as 3-cells `S₀ ⇛ S₂`. Both equal `β ∘_H α`.

*Proof.* By strict middle-four in the strict 2-category `G(P,R)`, vertical
then horizontal composition of 3-cells along disjoint segments commutes with
horizontal packaging: `(β ∘_H id_{U₁}) ∘_V (id_{V₀} ∘_H α)`
`= (β ∘_V id_{V₀}) ∘_H (id_{U₁} ∘_V α) = β ∘_H α`,
and likewise `(id_{V₁} ∘_H α) ∘_V (β ∘_H id_{U₀}) = β ∘_H α`, using strict
vertical unit laws. ∎

Write `D := B₁ ∘_V A₀ = A₁ ∘_V B₀`. Then, by strict associativity of vertical
3-cell composition and invertibility of `A₁, B₀`:

```
L = B₀⁻¹ ∘_V A₁⁻¹ ∘_V (B₁ ∘_V A₀)
  = B₀⁻¹ ∘_V A₁⁻¹ ∘_V (A₁ ∘_V B₀)   (Lemma)
  = B₀⁻¹ ∘_V (A₁⁻¹ ∘_V A₁) ∘_V B₀   (strict associativity)
  = B₀⁻¹ ∘_V id ∘_V B₀              (invertibility of A₁)
  = B₀⁻¹ ∘_V B₀ = id_{S₀}.          (invertibility of B₀)
```

Each step is a Gray-constitutive identity, so `L = id_{S₀}` holds in every
Gray-category and therefore in `G_free`. The cyclic critical peak is joinable
with diagonal `D`; the loop carries no holonomy. ∎

## 4. Machine-checked ledger

`output/artifacts/verify_loop.py` replays the entire argument on factor-list
terms: presentation (distinct generators, column composability), parallelism of
both interchangers, corner chains and total boundary `g∘f ⇒ g''∘f''`,
closedness `S₄ == S₀`, four distinct corners, no-adjacent-cancellation at every
step (disjoint positions 0 vs 2), the commutation square
(`B₀;A₁` and `A₀;B₁` reach the same `S₂`), and per-segment word reduction
(`[alpha, alpha-inv] → []`, `[beta, beta-inv] → []`) giving `L = id`.
Run `python3 output/artifacts/verify_loop.py`; it prints `VERIFY_OK`
(23 checks, exit 0).

## 5. Scope and limitations

Proved: the canonical minimal 2×2 commutator loop (alternating a top-pair and
a bottom-pair interchanger with inverses, acting on disjoint segments) is the
identity in every Gray-category. Not claimed: statements about larger grids,
overlapping (non-disjoint) interchanger peaks, other whiskering/chirality
conventions beyond the fixed orientation (the same proof adapts mutatis
mutandis), or weak tricategories prior to Gray strictification. The negative
resolution (nontrivial holonomy witness) is ruled out for this loop by the
positive proof. Computation is a term-level replay of the equational proof,
not an independent search of the free model.
