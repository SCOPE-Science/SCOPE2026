# Independent mathematical audit

## correctness

PASS

Each distinct run-letter c_i appears only in its own run, forcing at least one attractor position per run. Picking all run endpoints attains q. Each mixed adjacent bigram c_i c_{i+1} occurs once, forcing last(i) or first(i+1), which also suffices for any mixed factor; pure c_i^t has a sliding occurrence through any chosen position. Singleton runs split independent non-singleton blocks; a t-run block has t+1 all-endpoint configurations plus Σ(a_i−2) configurations with one interior choice, totaling 1+Σ(a_i−1). Block sequence GF yields xy/((1−x)(1−x−xy−x²y)), with [y^q] x^q(1+x)^{q−1}/(1−x)^{q+1}, hence binomial sum. Independent direct-occurrence enumeration covered 117 run vectors (lengths 1..3, 2..4 runs) and 30 coefficient comparisons; those are corroboration, not the proof.

## originality

PASS

A full primary general attractor combinatorics paper and close published Resultary repeated-word/binary-family results were compared by model and implication. None inspected implies the local iff minimizer classification for one-run-per-letter words or the bivariate composition census. Unindexed simple run-factor equivalences remain a residual risk; qualified best-of-knowledge originality PASS.

## value

PASS

The exact set of all minimum attractors of a natural language class, its block-factorized multiplicity and the complete two-parameter length/run census are independently useful structural/combinatorial facts, not mere minimum-size recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
