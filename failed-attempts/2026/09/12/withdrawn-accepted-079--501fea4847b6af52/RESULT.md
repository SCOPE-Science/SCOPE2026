# Mixed-branching rooted-tree conjugacy: wreath structure, profinite smoothness, Z-orbit vanishing, and a conditional smoothness dichotomy

## Context

The admitted target asks whether conjugacy in `G = Aut(T)` is smooth (Borel
reducible to equality on `2^N`), where `T` is the rooted tree whose root has
countably infinitely many children and every other vertex has exactly two
children, with vertex set `N`, and `G` carries the pointwise-convergence Polish
topology acting on itself by conjugation. A complete target resolution would
either exhibit an explicit Borel complete invariant or prove non-smoothness via
an invariant dense `G_delta` with generic `E_0`-ergodicity plus an explicit
`E_0`-hardness witness. This record reports the proved structural core as an
emergent finding and names the single remaining gap honestly.

## Definitions

- `T`: rooted tree; root `r` has children indexed by `N`; each non-root vertex
  has exactly two children.
- `B`: rooted full binary tree; `H = Aut(B)` with the pointwise-convergence
  topology (compact profinite, `H = projlim H_n`, `H_n = Aut(B_n)` finite,
  `H_{n+1} = (H_n x H_n) rtimes S_2`, `|H_0| = 1`, `|H_{n+1}| = 2|H_n|^2`).
- `G = Aut(T)` with the pointwise-convergence topology; `X = G` with the
  conjugation action.
- Write elements of the wreath product as `(h, sigma)` with
  `h in H^N`, `sigma in S_infinity = Sym(N)`, group law
  `(l,tau)(h,sigma) = (l . (tau . h), tau sigma)`,
  `(tau . h)_i = h_{tau^{-1}(i)}`.
- `=^+`: equality of countable sets of reals (Friedman-Stanley jump of `=`).

## Result

Let `T`, `G`, `H` be as above.

1. (Wreath structure.) `G` is Polish-isomorphic to `H^N rtimes S_infinity`,
   where `S_infinity` permutes the top binary subtrees. Conjugation is
   `(l,tau)(h,sigma)(l,tau)^{-1} = (h', tau sigma tau^{-1})` with
   `h'_i = l_i h_{tau^{-1}(i)} l_{sigma'^{-1}(i)}^{-1}`,
   `sigma' = tau sigma tau^{-1}`.
2. (`H`-smoothness.) `H`-conjugacy is smooth via the explicit profinite
   invariant `I_H(x) = ([pi_n(x)])_n`, where `pi_n : H -> H_n` is restriction
   and `C_n = H_n/conj` is finite discrete. The finite-level class counts
   satisfy `c_0 = 1`, `c_{n+1} = c_n(c_n+1)/2 + c_n`
   (`1, 2, 5, 20, 230, ...`; orders `1, 2, 8, 128, 32768, ...`).
3. (Z-orbit vanishing.) Over any bi-infinite (`Z`-type) `sigma`-orbit, any two
   `H`-labels are cohomologous via the explicit two-sided recursion
   `l_{j_m} = h'_{j_m} l_{j_{m-1}} h_{j_m}^{-1}` (forward) and
   `l_{j_{m-1}} = (h'_{j_m})^{-1} l_{j_m} h_{j_m}` (backward) from an arbitrary
   seed. Hence bi-infinite orbits carry no conjugacy invariant.
4. (Finite-cycle classification.) For a `k`-cycle `O` of `sigma`, the
   `H`-conjugacy class of the cyclic product `P_O(h)` is a complete invariant
   (telescoping plus cyclic-closure converse); the centralizer permutes
   equal-length cycles, so for each `k` the multiset of these classes over the
   `k`-cycles is complete. On the identity-permutation fiber,
   `(h,id)` is `G`-conjugate to `(h',id)` iff the `H`-class sequences agree as
   multisets; this Borel-reduces multiset equivalence of `H`-sequences to
   `G`-conjugacy.
5. (Conditional dichotomy.) If `H` has only countably many conjugacy classes,
   `G`-conjugacy is smooth with an explicit countable invariant (finitary cycle
   type plus per-length multiplicity functions). If `H` has continuum many
   classes, `=^+` Borel-reduces to `G`-conjugacy via infinite-repetition coding,
   so `G`-conjugacy is not smooth.

## Proof / evidence

- Root-fixing: the root is the unique infinite-degree vertex, hence fixed by
  every automorphism; each top subtree is a rooted binary tree isomorphic to
  `B`. The product topology on `H^N` times the pointwise topology on
  `S_infinity` coincides with pointwise convergence on `T`.
- Wreath class lemma: for finite `F` with `c` classes,
  `(F x F) rtimes S_2` has `c(c+1)/2 + c` classes (`binom(c+1,2)` unordered
  `(-,0)` pairs; `c` swap classes classified by the cyclic product, every class
  attained with `b = 1`). Verified by brute force for `n <= 3`: see artifact.
- `I_H` completeness: the fibers
  `F_n = {g in H_n : g pi_n(x) g^{-1} = pi_n(y)}` are nonempty finite with
  compatible restrictions, so compactness gives a thread conjugating `x` to
  `y`. Continuity implies Borel.
- Vanishing and cyclic products: direct verification of the recursions and the
  telescoping identity `P_O(h') = l P_O(h) l^{-1}`; centralizer analysis as in
  the finite wreath-cycle theory extended to the infinite-index setting.
- Countable side: the invariant lands in a countable product of countable sets
  (standard Borel) and is complete by the classification.
- Continuum side: smooth `H`-conjugacy with continuum many classes
  Borel-embeds `=_{2^N}` (standard: uncountable analytic image contains a Cantor
  set); infinite-repetition coding turns set equality into multiset equality
  with multiplicities `0` or `infinity`, reducing `=^+` to the identity fiber.
  `=^+` is strictly above `=` (Friedman-Stanley), hence non-smoothness.
- Computation: `verify_wreath.py` realizes `H_n` as permutations of `2^n`
  leaves generated by block swaps and enumerates classes for `n <= 3`,
  confirming `(|H_n|, c_n) = (1,1), (2,2), (8,5), (128,20)` with recursion and
  order identities matching at every step.

## Limitations

- Which side of the dichotomy holds (whether `H = Aut(B)` has countably or
  perfectly many conjugacy classes, i.e. whether the thread space
  `projlim C_n` with `|C_n| = 1, 2, 5, 20, 230, ...` is countable or contains a
  perfect set) is left open; unbounded finite-level growth does not imply a
  perfect thread set.
- The continuum side proves `=^+`-hardness (hence non-smoothness) but not the
  target's generic-`E_0`-ergodicity plus explicit `E_0`-witness certificate.
- Level-4 brute-force class enumeration (`|H_4| = 32768`) was not completed.
- The continuum-side `=_{2^N}` embedding and Friedman-Stanley `= <_B =^+`
  facts are quoted classical background.

## Reproducibility

- Rerun the artifact: `python3 output/artifacts/verify_wreath.py`; expected
  output lines `n=0..3` with `|H_n| = 1, 2, 8, 128`, classes `1, 2, 5, 20`,
  all recursion and order checks `True`/matching.
- All proofs are self-contained in this file's Result/Proof sections given the
  quoted classical facts above.

## References

- K. Beserra, S. Coskey, On the classification of automorphisms of trees,
  arXiv:1709.02467 (2017-2018): finitely-branching rooted smoothness,
  fully-branching Borel completeness, bounded-height jump hierarchy.
- P. W. Gawron, V. V. Nekrashevych, V. I. Sushchansky, Conjugation in tree
  automorphism groups, IJAC 11(5):529-547 (2001): types for locally finite and
  level-homogeneous trees.
- D. Bernhardt, A. C. Niemeyer, F. Rober, L. Wollenhaupt, Conjugacy classes
  and centralisers in wreath products, arXiv:2107.04645 (2021): finite-index
  wreath-cycle/territory theory.
- H. Friedman, L. Stanley, A Borel reducibility theory for classes of countable
  structures, JSL 54(3):894-914 (1989): `= <_B =^+` jump hierarchy.
- A. S. Kechris, Dynamics of non-archimedean Polish groups (survey): background
  on non-archimedean Polish groups.
