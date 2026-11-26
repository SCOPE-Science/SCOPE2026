# Independent mathematical audit

## correctness

PASS

The seen-factor mask and last min(3,|w|) bits describe exactly what new factor can appear on the next input bit, by induction on word length; the predicate tests only the fifteen required factors, allowing the optional factor arbitrarily often. Reachability is finite transition closure. Refinement starting with acceptance yields agreement on all suffixes of length at most d after d rounds. Stability of the nested partition certifies agreement for arbitrarily long words; a strict split in the last changing round certifies sharpness. Independent run `python3 /tmp/opencode/factor-review.py` used target-specific sets of missing factors and collapsed all fulfilled states at construction. For the first eight patterns in increasing binary order it obtained (8435,11121,9670,10152,9956,9537,8524,11746), and the reverse order for the complementary eight. Sharp depths were 17 for 0000/1111 and 18 elsewhere; the preceding round was strictly coarser in every case (e.g., 8431 vs 8435 for 0000 and 11113 vs 11121 for 0001). This quotient computation was exhaustive for all input lengths, not limited by a sample of words. The frozen Moore and Hopcroft implementations were inspected without executing them; their common seen-mask representation has a different raw state count from the target-specific independent check. Complement relabels letters; reversal sends 0001 to 1000 and the verified state counts differ by exactly 625. The classification is only for one specified optional factor of length four in the binary alphabet.

## originality

PASS

The contribution is the exact fifteen-required-factor spectrum and sharp suffix complexity. Neither full-factor universality nor the same-day constrained scattered-subsequence reversal result states it. The generic coverage construction and minimization are standard; the claimed new content is the exact pattern dependence and reversal counterexample in this contiguous-factor language. Same-day chronology is not used to resolve priority.

## value

PASS

Deleting a single requirement from the familiar binary full-factor monitor is a natural perturbation: it isolates how the geometry of one edge in the order-three de Bruijn graph affects exact right languages. The eight distinct answers, extremal patterns, sharp uniform suffix lengths, and concrete reversal gap establish that this perturbation is not captured by full-factor coverage or complement/reversal symmetry alone. Four is the first order allowing eight complement classes and these data give exact quantitative benchmarks for reductions and symmetry conjectures, not just code examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
