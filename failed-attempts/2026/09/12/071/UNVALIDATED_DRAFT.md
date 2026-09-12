# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — No cyclic-prime two-J-class small monoid has complexity 2

## Claim (target alternative (ii), proved in strengthened form)

Let S be any finite monoid with at most one regular J-class containing a
nontrivial maximal subgroup (no bound on |S|, arbitrary groups). Then the
Krohn–Rhodes complexity satisfies c(S) ≤ 1. In particular, no monoid in the
admitted scope — |S| ≤ 24, exactly two nonzero regular J-classes, at most one
regular J-class with nontrivial maximal subgroups, every maximal subgroup
cyclic of prime order — has complexity 2. The bound 1 is best possible: the
full transformation monoid T₂ (order 4) lies in the scope and has c(T₂) = 1.

## Definitions used

- Green's J-order; regular J-class (contains an idempotent / regular element).
- Maximal subgroup = H-class H_e of an idempotent e (a group).
- Aperiodic = H-trivial (all subgroups trivial); c(S) = 0 iff S is aperiodic
  (standard: groups are exactly the complexity-1 building blocks beyond
  aperiodics).
- Depth d(S) = maximum n for which there is a strict chain
  J₁ <_J J₂ < … <_J Jₙ of regular J-classes each containing a nontrivial
  subgroup (d(S) = 0 if none does).

## Established theorems invoked (standard references)

1. **Rhodes Depth Theorem** (Rhodes 1968; see Eilenberg, *Automata, Languages
   and Machines*, Vol. B, Ch. VII; Rhodes–Steinberg, *The q-theory of Finite
   Semigroups*, Ch. 4): for every finite semigroup S, c(S) ≤ d(S).
2. **Holonomy / Prime Decomposition Theorem** (Tilson, Ch. XI of Eilenberg
   Vol. B; Rhodes–Steinberg Ch. 4): S divides an iterated wreath product whose
   group levels are indexed by regular J-classes, with the level of a regular
   J derived from its Schützenberger groups; J-classes with trivial
   Schützenberger data are absorbed into adjacent aperiodic factors. Hence
   irregular J-classes never contribute a group level.
3. **Regular-J facts** (standard; e.g. Rhodes–Steinberg Ch. 2; Howie,
   *Fundamentals of Semigroup Theory*): every subgroup of a finite semigroup
   lies in the H-class of its (idempotent) identity, hence in a regular
   J-class; within a regular J-class of a finite semigroup all Schützenberger
   groups are mutually isomorphic and coincide with the maximal subgroup. So a
   regular J-class has trivial maximal subgroups iff its holonomy group level
   is trivial.

## Proof

Let S be a finite monoid with at most one regular J-class with nontrivial
maximal subgroups.

- If no regular J-class has a nontrivial subgroup, then S is aperiodic: any
  subgroup G ≤ S has idempotent identity e, G ≤ H_e, and J_e is regular, so
  H_e is trivial and G is trivial. Hence c(S) = 0.
- Otherwise exactly one regular J-class J* has nontrivial subgroups. Any
  strict chain of regular J-classes each containing a nontrivial subgroup can
  contain at most the single class J*, so d(S) ≤ 1. By the Depth Theorem,
  c(S) ≤ d(S) ≤ 1.

Remarks. (a) Irregular J-classes contribute no group level by (2); they are
absorbed in aperiodic coordinates. (b) The hypotheses "|S| ≤ 24", "exactly two
nonzero regular J-classes", and "cyclic of prime order" are not needed for the
upper bound — the argument works for every finite monoid (indeed semigroup)
with ≤ 1 group-carrying regular J-class and arbitrary groups. (c) The zero
J-class {0}, when present, has trivial group and never affects the count.

Consequently no S in the admitted scope has c(S) = 2: alternative (ii) of the
target holds.

## Sharpness: T₂ witnesses c = 1 inside the scope

Let T₂ be the full transformation monoid on 2 points, |T₂| = 4 ≤ 24, with
elements {id, swap, c₀, c₁}. Computed Green's structure (artifact
`output/artifacts/verify_T2_scope.py`, output reproduced below):

- J-classes: J_top = {id, swap} (group of units ≅ C₂, cyclic of prime order),
  J_low = {c₀, c₁} (regular — both elements idempotent — with singleton
  H-classes, hence trivial maximal subgroups). No zero. So T₂ has exactly two
  nonzero regular J-classes, at most one with nontrivial groups, all maximal
  subgroups trivial or C₂: T₂ is in scope.
- H(id) = {id, swap} has size 2, so T₂ is not aperiodic, hence c(T₂) ≥ 1
  (c = 0 iff aperiodic). The theorem above gives c(T₂) ≤ 1. Hence c(T₂) = 1.

So complexity 1 does occur in the scope while complexity 2 never does; the
one-group-J bound is sharp.

## Computed evidence (run: `python3 output/artifacts/verify_T2_scope.py`)

- Multiplication table of T₂ verified; principal two-sided ideals:
  I(id) = I(swap) = whole monoid, I(c₀) = I(c₁) = {c₀, c₁} → two J-classes.
- Regularity: every element regular (each satisfies f·x·f = f for some x).
- H-classes of idempotents: H(c₀) = {c₀}, H(c₁) = {c₁}, H(id) = {id, swap}.
- Scope checks pass: |S| = 4 ≤ 24; two nonzero regular J-classes; one with
  nontrivial (C₂) group.
- Rees-size enumeration: 90 triples (|A|, |G|, |B|) with |G| ∈ {1} ∪ primes
  and |A|·|G|·|B| ≤ 23, consistent with the scope arithmetic; T₂ corresponds
  to (1,2,1) + (2,1,1), total 4.

## What is proved vs cited vs computed

- Proved here: the deduction d(S) ≤ 1 ⇒ c(S) ≤ 1 for the in-scope class, the
  aperiodic case, the sharpness computation c(T₂) = 1 given the upper bound.
- Cited (not re-proved): Depth Theorem c ≤ d; holonomy indexing of group
  levels by regular J-classes; regular-J Schützenberger facts. These are
  textbook-level results with precise pointers above.
- Computed: full J-structure/regularity/maximal-subgroup verification for T₂
  and the Rees-size enumeration.

## References

- S. Eilenberg, *Automata, Languages and Machines*, Vol. B, Chs. VII (depth),
  XI (Tilson holonomy / prime decomposition).
- J. Rhodes & B. Steinberg, *The q-theory of Finite Semigroups*, Chs. 2–4.
- J. Rhodes, "Characters and complexity of finite semigroups" (1968).
- J. M. Howie, *Fundamentals of Semigroup Theory* (Green's relations, regular
  J-classes, Rees matrix form).
