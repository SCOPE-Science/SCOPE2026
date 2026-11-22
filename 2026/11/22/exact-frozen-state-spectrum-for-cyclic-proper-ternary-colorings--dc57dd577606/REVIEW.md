# Review

## Correctness — PASS

The bijection between proper cyclic ternary colorings and mod-three-closed binary increment words has a three-to-one multiplicity. A legal swap is equivalent to three consecutive equal increments, established by inspecting the two outer neighbors of the swapped pair; the cyclic triangle boundary is included. The full four-state transfer and cubic roots-of-unity filter are expanded explicitly, with independently verified characteristic determinants. The exact arithmetic recurrence and existence witnesses prove the all-length conclusions. The bundled `verify.py` independently enumerates colorings through length 13 and closed sign words through 20; these checks are supporting evidence, not infinite certification.

## Originality — PASS, with residual historical-priority risk

The closest adjacent-swap paper derives algorithms and rigid structures for proper three-colorings of paths, without enumerating cyclic frozen states [2]. The 1988 majority-rule paper counts cyclic binary no-triple words without the mod-three closure condition [3]. Restricted order swaps [1] and single-vertex recoloring [4] do not imply the stated count. The particular roots-of-unity weighted refinement might appear in unindexed symbolic-dynamics work; neither keyword search nor semantic database ranking establishes absolute originality.

## Value — PASS

For cyclic proper ternary colorings, a fundamental reconfiguration obstruction is the exact number of states that admit no first move. The theorem gives all lengths, a sharp three-length nonexistence list, a rational generating function, and a quantitative exponentially decaying frozen fraction. These are intrinsic mobility statistics for a natural constrained swap system; they are not an arbitrary parameter slice or merely a finite census.

## Limits and closest literature

Only degree-zero states are enumerated, not components or reachability of moving states. Closest works are [2] (same swap rule on a path), [3] (binary no-triple cyclic words without ternary closure), [1] (constrained order swaps), and [4] (recoloring instead of swaps). Priority against unindexed earlier work remains open; no independent mathematical audit has occurred.

[1] https://doi.org/10.4230/LIPIcs.MFCS.2021.8

[2] https://arxiv.org/abs/2511.06473

[3] https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf

[4] https://arxiv.org/abs/2206.09268

Self-review: passed. Independent audit: not yet performed.
