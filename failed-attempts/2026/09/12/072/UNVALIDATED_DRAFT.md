# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Existence of a degree-7 transformation monoid with holonomy height 3 and group complexity 1

## Answer
Yes. The following faithful transformation monoid on Q = {0,1,2,3,4,5,6}
has holonomy height 3 and Krohn–Rhodes complexity exactly 1.

Generators (right actions, listed as images of 0..6):

- a = (1,0,2,3,5,4,6) — swap 0↔1 and 4↔5, fix 2,3,6. Note a² = id.
- b = (3,3,5,5,3,3,5) — rank 2: {0,1,4,5} ↦ 3/5 pattern (0↦3,1↦3,2↦5,3↦5,4↦3,5↦3,6↦5).
- c = (2,3,1,1,6,6,3) — rank 4.

Let S = ⟨a,b,c⟩ (closure under composition). Then |S| = 53, computed by
closure from the identity (51 non-identity elements plus identity; all
53 elements are tabulated in `output/artifacts/certificate.json`).

## 1. The monoid and faithfulness
S is given as maps on Q closed under composition by construction. The three
generators are pairwise distinct and all lie in S; the action is faithful by
definition (S is a concrete transformation monoid). The unique involution in
S is a itself (exhaustive check over all 53 elements: exactly one element
s ≠ id satisfies s² = id).

## 2. Holonomy skeleton (computed)
Im(S) has 21 image sets falling into 7 mutual-subduction classes:

| rep | class members | stabilizer size | bricks | holonomy group |
|---|---|---|---|---|
| {0} | all 7 singletons | 53 | 1 | trivial |
| {0,2} | {02,03,12,13} | 5 | {0},{2} | C2 = {id,(01)} |
| {0,6} | {06,16,34,35} | 3 | {0},{6} | C2 = {id,(01)} |
| {2,3} | {23} alone | — | 2 singletons | trivial |
| {0,2,3} | {023,123} | — | 3 singletons | trivial |
| {0,2,3,6} | {0236,1236} | — | 4 singletons | trivial |
| {0,…,6} | {Q} alone | 2 | 7 singletons | C2 = {id,(1 0 2 3 5 4 6)} |

Conventions: subduction A ≤ B iff A ⊆ B·s for some s ∈ S (Eilenberg);
rep = lexicographically least set of least size in its class; bricks are the
atoms of the Boolean algebra cut out by {I ∈ Im(S) : I ⊆ rep} (for the top
rep every image contained in Q meeting each point cuts a singleton, so the
bricks are the 7 singletons). Exactly 3 levels carry a nontrivial
permutation group (each C2), so the holonomy height is 3.

The nontrivial stabilizer actions were verified generator-by-generator:
each stabilizer element permutes bricks (no brick is split) and the induced
brick-permutations close to C2. Singleton reps have holonomy group S₁
(trivial) by definition.

## 3. Complexity is exactly 1
Lower bound: a ∈ S satisfies a² = id ≠ a, so S is not aperiodic; any divisor
of a finite aperiodic monoid is aperiodic, hence S divides no finite
aperiodic monoid and c(S) ≥ 1.

Upper bound: S divides W = U₂ ≀ C₂ ≀ U₂, where U₂ = {id,(0,0),(1,1)} is the
2-state reset (aperiodic) monoid and C₂ the 2-state flip group. W acts on
{0,1}³ ∋ (x,y,z), index x·4+y·2+z, by the cascade rule
(x,y,z)·(a,α,β) = (a(x), y⊕α(x), β(x,y)(z)) with 3·4·81 = 972 elements.
The divisor certificate is a Tilson relational morphism with singleton
fibres: injective φ : Q → X, φ(q) = q+1 (image {1,…,7}), and for each
generator g ∈ {a,b,c} and each q ∈ Q a wreath element w(g,q) ∈ W with
w(g,q)(φ(q)) = φ(g(q)). All 21 triples are tabulated with full labels
(a, α, β) and 8-state actions in `certificate.json`. Because each step lands
exactly on the required singleton, stepwise lifting is consistent for every
word; this was verified for all 53 elements of S (word-lift check in
`verify.py`). Hence S is a (relational) divisor of W, so
c(S) ≤ c(U₂)+c(C₂)+c(U₂) = 0+1+0 = 1.

Therefore c(S) = 1 while the holonomy height is 3.

## 4. Verification
- `output/artifacts/certificate.json`: all 53 elements, skeleton classes,
  brick partitions, holonomy groups, φ, and all 21 wreath covers with labels.
- `output/artifacts/verify.py`: recomputes closure (53), height (3, groups
  C2/C2/C2), involution, every cover equation w(φ(q)) = φ(g(q)), label/action
  consistency, and whole-monoid word-lift consistency. Prints ALL CHECKS PASSED.
- An independent second implementation of the skeleton/holonomy code
  (separate code path, run during research) confirms 7 classes / 21 images /
  height 3.

## 5. Separation of proof, computation, and conjecture
Proved: |S| = 53 by finite closure; a² = id; the three holonomy groups are
C2 (finite check); the 21 wreath-cover equations (finite check); the
complexity bounds via the cited standard theorems (division lowers
complexity; wreath/aperiodic facts). Computed evidence: the certificate
tables. No conjecture is used. The only external theorems invoked are the
Krohn–Rhodes wreath upper bound c(X ≀ Y) ≤ c(X)+c(Y), that divisors do not
raise complexity, and that U₂ is aperiodic / C₂ is a group (all standard;
the latter two also checked computationally).
