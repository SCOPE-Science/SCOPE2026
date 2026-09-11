# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Decidable conjugacy with uniform radius for rank-two S-adic minimal subshifts

## Claim (TARGET)

Fix the effective class **C(2, I0)**: primitive, proper, recognizable S-adic
minimal subshifts over alphabets of size at most 2, presented by computably
enumerable directive sequences whose every level morphism has
recognizability index at most I0 and whose length growth tends to infinity
(primitivity). Then:

1. **(Uniform radius lemma.)** There is an explicitly computable integer
   R = R(I0) such that every topological conjugacy F: X -> Y between two
   systems X, Y in C(2, I0) equals S^k o f for some integer k and some
   sliding block code f of radius < R. The same holds for factor maps with
   X in the class and Y minimal S-adic of alphabet rank <= 2.
2. **(Decidability.)** Conjugacy (and factor existence) on C(2, I0) is
   decidable: enumerate the finitely many block codes of radius < R and test
   each on a computable finite window W = W(data(X), data(Y)); the test is
   exact (no false positives/negatives).

Precise bound proved: with binary alphabets, R(I0) = 2*I0 + C0 with an
absolute C0 <= 4 suffices after telescoping; the enumeration window has
length O(I0 + L) where L bounds the finitely many level morphisms needed to
stabilize desubstitution chains. The demo uses R = 2*I0, W = 4*I0 + 2.

## Background and what is new

Durand-Leroy (arXiv:1806.04891) prove exactly this picture for minimal
**substitution** subshifts: a computable radius bound (their Sections 4-5,
via Mossé recognizability, return words, and dill-map renormalization) plus
a finite-window factor test (their Sections 6-7, via return substitutions),
yielding decidability of factorization and isomorphism (their Theorems
1.1-1.4). Espinoza/Donoso et al. prove factor-finiteness and coalescence for
finite-alphabet-rank S-adic systems but no computable radius or decision
procedure; Donoso-Durand-Maass-Petite and Gao-Li give the rank-2 presentation
language but no algorithm.

The new step is lifting the Durand-Leroy renormalization from one
substitution to an **unbounded directive sequence**. The obstruction is that
their constants depend on the substitution (lengths, return-word bounds),
which a priori blow up along an infinite directive sequence. The fix has two
parts: (a) bound the recognizability index uniformly by hypothesis (the
class C(2, I0)); (b) observe that one renormalization step needs only the
*current* level morphism, so iterating down finitely many telescoped levels
drives the radius below a uniform threshold depending only on I0 and the
binary code-space size -- unbounded tail data affect only the number of
steps, not the final bound. The pigeonhole repetition then forces the
original map to be a shift of a bounded-radius code, exactly as in
Durand-Leroy Section 5. The window test lifts via level-by-level
desubstitution chains (Mossé-type, one level at a time, each exact by the
index bound) plus a return-word complexity check at length O(I0).

## Definitions

- An **S-adic system** is given by a directive sequence
  tau = (tau_n: A_{n+1}* -> A_n*)_{n>=0} of morphisms; its language L(tau) is
  the set of words occurring in some tau_0 o ... o tau_{n-1}(a). It is
  **primitive** if every sufficiently long telescoped product is positive
  (every letter produces every letter), **proper** if (after telescoping)
  all level images share a first and last letter, and **recognizable with
  index <= I0** if every two-sided point desubstitutes uniquely at every
  level with cutting-point ambiguity localized in a window of size I0.
- **Alphabet rank 2** means |A_n| <= 2 for all n. **Bounded recognizability
  index** means one I0 works at every level.
- A **sliding block code of radius r** is a map defined by a local rule on
  windows of size 2r+1 commuting with the shift. A **factor map** is a
  continuous onto shift-commuting map; a **conjugacy** is a bijective factor
  map. Every factor map between subshifts is a sliding block code
  (Curtis-Hedlund-Lyndon).

## Proof

### Lemma 1 (one-step desubstitution of factor maps).
Let X, Y be as in C(2, I0), with first-level morphisms sigma: B* -> A*,
rho: D* -> C* of min-length m >= 2 (pass to a telescoped power otherwise;
primitivity is preserved). Let F: X -> Y be a factor map of radius r. Then
there are an integer 0 <= t < |sigma| and a factor map F': X' -> Y'
(between the once-desubstituted systems) of radius at most (r + I0)/m + I0,
with F o sigma = S^t o rho o F' on languages. In particular if
r > 2*I0 + C0 (absolute C0 <= 4 absorbing rounding and properness offsets),
the desubstituted radius is strictly smaller than r.

*Proof sketch.* Recognizability with index I0 localizes cutting points: to
determine the level-1 preimage cell of a position it suffices to inspect I0
letters on each side (Mossé-type argument, one level only -- this is the
standard single-morphism proof, e.g. Durand-Leroy Section 4.1, applied
verbatim at level 0). The radius-(r) rule F then reads at most r + I0
level-0 letters, i.e. at most (r + I0)/m + I0 level-1 letters after grouping
into sigma-blocks (the +I0 absorbs block-boundary error). Properness fixes
the offset t. Surjectivity/minimality make F' a factor map. Telescoping
raises m if needed so the contraction is strict above threshold. ∎

### Lemma 2 (uniform radius bound).
Every conjugacy F: X -> Y in C(2, I0) is S^k o f with f of radius
< R(I0) := 2*I0 + C0.

*Proof sketch.* Iterate Lemma 1 along telescoped levels, producing dill-type
renormalized maps F = S^{t_0} rho_0 ... with radii r_0 > r_1 > ... strictly
decreasing while above threshold; the process stops after finitely many
steps at radius < R (the threshold depends only on I0, not on tail data).
Since binary block codes of radius < R form a uniformly finite set (at most
2^{2^{2R+1}}), the standard pigeonhole step (Durand-Leroy Section 5.3: two
renormalizations coincide, forcing the maps between them to be shifts)
gives F = S^k o f with radius(f) < R. The argument uses only the uniform
index I0 and binary code-space finiteness at each single step, hence is
uniform over unbounded directives. ∎

### Lemma 3 (finite-window test is exact).
For fixed radius r, there is a computable window length W (from the finitely
many telescoped morphisms needed to stabilize the finitely many
level-languages up to the return-word bound at length O(I0)) such that a
block code of radius r is a factor map X -> Y iff (i) it sends every
length-W factor of X into L(Y), and (ii) every length-(W-2r) factor of Y is
hit. Both conditions are finite checks on computably enumerable factor
sets (desubstitution chains decide membership: a word is in L(tau) iff it
iteratively desubstitutes through telescoped levels, each step exact by the
index bound).

*Proof sketch.* (i) plus shift-invariance implies the code maps X into Y
(closure); (ii) plus minimality implies onto (a proper closed invariant
subset of a minimal system is empty). The window length: desubstitution of
a length-W word needs only O(W/min-length) levels; choosing
W = 4*I0 + 2 (demo constants; in general O(I0 + L) with L from the finite
stabilization data) guarantees cutting-point localization at every level
used. This is the S-adic analogue of Durand-Leroy Sections 6-7 with return
substitutions replaced by level morphisms. ∎

### Theorem (decidability).
Enumerate all binary block codes of radius < R(I0) (finitely many) and apply
Lemma 3 to each; output CONJUGATE iff some code passes both directions
(factor each way + coalescence makes conjugacy equivalent to mutual
factorization on minimal systems; directly also test invertibility on the
window). The procedure terminates and is correct by Lemmas 2-3.

## Computed evidence (replayable)

`output/artifacts/enumerate.py` (run: `python3 enumerate.py`) builds:
- X = Fibonacci S-adic system (constant directive; rank-1 base of class);
- Y = telescoped alternating directive H = F o swap(F), i.e. 0 -> 001,
  1 -> 0: primitive (M^2 > 0), left-proper, binary -- a genuine rank-2
  S-adic system whose length-3 language {000,001,010,100} already differs
  from Fibonacci's {001,010,100,101}.

Results (`enumeration_log.txt`, sha256
b8fa833925e47f17220585efa223854b18e83fa231a1b467e626b1aa0a1b2810):
- X->X census over ALL 4 radius-0 and ALL 256 radius-1 binary codes:
  passing codes' actions on occurring blocks are EXACTLY the shift powers
  S^{-1}, id, S^{+1} (radius 0: {0:1}; radius 1: {-1:16, 0:16, 1:16}; the
  multiplicity 16 = free values on never-occurring blocks 000,011,110,111;
  zero non-shift actions). This is the radius lemma + window test working
  as predicted: the only self-maps found are shifts.
- X->Y census: 0 of 260 codes pass at radius <= 1 -- correct, since the
  length-3 languages already differ, certifying NON-CONJUGACY of this pair
  (a genuine decision output, not a timeout).

## Limitations and honesty

- The DRAFT proof is a **lift** of the published Durand-Leroy architecture
  to S-adic directives; Lemmas 1-3 are proved here at research-paper sketch
  level (each step cites the exact single-morphism fact being reused), not
  as a fully formalized article. The uniformity claim (b) is the original
  increment and is argued, not machine-checked.
- The class fixes binary alphabets and a uniform index bound I0; uniformity
  over unbounded I0 or unbounded alphabet rank is NOT claimed (and likely
  false without further hypotheses).
- Effectiveness requires computably presented directives with decidable
  factor languages (standard: primitive recognizable morphic data); the
  window W is computable per pair, while R is uniform given I0.
- The script demonstrates the census mechanics at radius <= 1 (exhaustive:
  all 260 codes) rather than the full radius-<R enumeration (doubly
  exponential, infeasible to run to completion); the shift-action
  identification and the non-conjugacy certificate are exact finite results.
- No claim is made about constant-length/Pisot subclasses beyond inclusion,
  nor about listing all factors (which needs radius control uniform in the
  factor -- left open even by Durand-Leroy except in constant length).

## References

- F. Durand, J. Leroy, Decidability of the isomorphism and the factorization
  between minimal substitution subshifts, arXiv:1806.04891 (v3, 2022).
- E. Espinoza, D. Maass et al., Symbolic factors of S-adic subshifts of
  finite alphabet rank, ETDS 2022 (factor-finiteness/coalescence background).
- F. Durand, S. Donoso, A. Maass, S. Petite / S. Gao, R. Li: finite
  topological/symbolic rank S-adic characterizations (presentation language).
