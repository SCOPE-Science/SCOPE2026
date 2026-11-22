# Review: gcd-sensitive modular-marker determinization

## Correctness — PASS

The language is recognized by an explicitly defined epsilon-free \(r+s\)-state NFA with a unique branching transition. Every reachable subset has one first-cycle state and an arbitrary second-cycle subset in one gcd residue class. Generalized Chinese remaindering realizes all these subsets. An explicit Myhill--Nerode argument distinguishes different second-cycle subsets and all unsaturated first-cycle phases; only full-residue-class subsets merge. Therefore the minimal count is \(r(2^{s/\gcd(r,s)}-1)+\gcd(r,s)\). Two independent checkers passed for small parameters; their finite tests are not substituted for the proof. Remaining scientific risk: no independent human or formal audit.

## Originality — PASS against inspected evidence

Baburin–Cotterell (arXiv:2611.10911v1) studies general determinization hardness and subset complexity, but its inspected theorems do not yield the exact two-modulus quotient. Their older arXiv:2407.09891v1 supplies classical Moore/Meyer–Fischer exponential examples; the unconstrained-prefix special case is acknowledged rather than claimed anew. Jirásek–Jirásková (arXiv:2511.03814v1) gives other concatenation witnesses, not the current language's exact gcd-dependent state formula. Hospodár–Mlynárčik (2020) treats concatenation of permutation languages; here the left marked factor is not a permutation language, and only its summary was accessible. Relevant published small-state censuses and other modular word statistics have different hypotheses and do not imply the all-positive-parameter result. Exact-claim and alternative-description searches revealed no direct coverage. Residual priority risk: an unindexed equivalent specialized treatment could exist, and source searches cannot establish uniqueness.

## Value — PASS

A single branch can yield exponential determinization, but congruences between the cycle lengths impose systematic identifications. The formula supplies an exact arithmetic classification and complete quotient structure for an infinite natural family, explaining a transition from \(r2^s-r+1\) in coprime cases to \(2r\) on the diagonal. This is substantially more informative than small-case enumeration or a generic upper bound, and gives a reusable exact benchmark for determinization and minimization.

## Evidence and limitations

Reproduce with `python3 verify_subset.py` and `python3 verify_quotient.py`; exact recorded outputs are `verify_subset.txt` and `verify_quotient.txt`. The formal proof, rather than the parameter-range checks, supports unrestricted integer parameters. No assertion is made of minimum NFA size, broad general NFA behavior, or exhaustive priority coverage.

Self-review: passed. Independent audit: not yet performed.
