# Scientific review of the Dyck 3-Abelian profile classification

## Correctness — PASS

The full observation recovers the number of peaks, singleton up- and down-runs, and two endpoint singleton indicators by five explicit linear formulas. Necessity of the parameter bounds follows from positive compositions and the Dyck boundary `10` condition. Sufficiency is constructive: after stripping forced boundary peaks, decreasing up-runs paired with increasing down-runs guarantee every prefix is nonnegative. Squaring the counts of admissible singleton choices for both run families and summing proves the cubic formula. Complete independent enumeration through semilength 11 and constructive exhaustive tuple witnesses through semilength 22 passed. Finite tests are not the all-length proof.

## Originality — PASS, qualified

The primary 2013 introduction to 3-Abelian equivalence, the 2016 unrestricted class-cardinality investigation, and the 2015 full paper on fixed-pattern position equivalence of Dyck paths were inspected. The closest published linear three-gram enumerations treat arbitrary binary words, while the Dyck paper equates positions of one fixed factor rather than all simultaneous multiplicities. No inspected text establishes the five-parameter Dyck feasibility classification. Importantly, OEIS A116731 gives **exactly the same cubic polynomial** for permutation avoidance, so neither the sequence nor its rational generating function is claimed as numerically new. The plausible original content is the explicit new Dyck interpretation and constructive support theorem. An unindexed equivalent treatment or deeper connection to the known permutation class is a residual priority risk.

## Value — PASS

Dyck words are a fundamental globally constrained binary language, while complete short-factor observations are a natural lossy sequence-reading model. The theorem characterizes all possible observations, proves explicit representatives for each, and gives the exact optimal zero-error reconstruction-code size for every semilength. The five-parameter support criterion is a nontrivial structural assertion, independent of whether its numerical count was already tabulated in another combinatorial model. No fiber-size, noisy-channel or longer-window results are claimed.

Self-review: passed. Independent audit: not yet performed.
