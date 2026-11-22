# Review of the length-nine run-ceiling-two deletion-code finding

## Correctness — PASS
The source is the precisely defined set avoiding both `000` and `111`; one arbitrary deletion is permitted and output words need not obey the source constraint. The exact clique formulation is equivalent to disjoint deletion shadows. The standalone standard-library branch-and-color checker enumerates all 110 nine-bit permitted words, proves no clique larger than thirteen can exist, and exhibits a thirteen-word clique. It repeats the exact computation for lengths one through eight and independently recomputes all VT-syndrome intersections. A differently formulated SciPy integer packing optimization corroborates the larger results but is not the logical basis of proof. The correctness claim is finite; no extrapolation is used.

## Originality — PASS, qualified
Kulkarni and Kiyavash (2012, arXiv:1211.3128) treat arbitrary deletions and a different guarded \((d,k)\) constraint, proving general bounds, not this exact two-sided homopolymer restriction. Schoeny et al. (2017, DOI 10.1109/TIT.2017.2661747) define maximum-run-limited VT subsets and derive burst-code constructions, without stating the first loss of optimality for run ceiling two. Takemoto and Nozaki (2020, arXiv:2012.13536) provide efficient RLL insertion/deletion coding and redundancy comparisons, not the exact 110-input-word, length-nine packing problem. Related published finite deletion-code records concern minimum-zero-run constraints, balanced sources or different error channels, and therefore do not imply the stated length-nine value. Historical priority is qualified because the literature search cannot exclude an unindexed short-block table.

## Value — PASS
Two simultaneous constant-run constraints are natural for timing, molecular storage and synchronization, and exact finite capacity governs short-block message budgets. The result identifies the first length at which restricting the classical VT partition loses an entire codeword, despite standard VT classes being optimal at every shorter length. This is a motivated structural boundary and an exact benchmark for constructions; no claim of a general asymptotic improvement is made.

## Scientific limitations
An independent mathematical audit and exhaustive bibliographic priority verification have not been performed. All upper bounds in the claim are finite, computation-assisted exact results with publicly inspectable code; the additional MILP solver is corroborative only.

Self-review: passed. Independent audit: not yet performed.
