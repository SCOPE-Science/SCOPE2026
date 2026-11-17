# Scientific review

## Correctness — PASS
The operator is well-defined for all stated dimensions, including the repeated-neighbor convention at two sites. Its strict-order chamber matrices give all local linearizations and hence the global Lipschitz constant by translation equivariance and continuity. The universal \(\sqrt3\) bound follows from the fact that a coordinate can serve at most three windows. For dimensions four and five, the standalone standard-library verifier enumerates all 24 and 120 permutations respectively and uses exact rational Schur-complement tests for the inequality \(\|Q_nS Q_n\|_2^2\le2\). Witnesses attain the bound at four and five sites; an explicit pattern with two triply selected columns attains \(\sqrt3\) for all dimensions at least six. No unproved extrapolation from a finite computation is used.

## Originality — PASS, qualified
The closest published scientific record, *Arithmetic saturation of the Lipschitz amplification of cyclic running medians*, concerns ordinary uncentered \(\ell_p\) perturbation norm; the centered seminorm here is not a direct special case and has a strictly different five-site outcome (\(\sqrt2\) rather than \(\sqrt3\)). The published BV-threshold result studies adjacent-edge variation, not centered Euclidean geometry. Full primary material by Maragos and Schafer and by Little and Jones was inspected for the relevant median/filter and variation properties. Public record summaries for the two closest findings were available, but full documents were not; an unrecognized equivalent computation remains a significant historical-priority risk. No claim of independently established novelty or completeness of the literature is made.

## Mathematical value — PASS
The mean-centered distance is intrinsic to translation-equivariant filtering, since additive baseline shifts are immaterial. The result determines its sharp nonlinear stability in every dimension, identifies the first dimension where the local threefold replication ceiling is attainable, and isolates an exact centering-induced loss at five sites. This distinction is useful when stability is measured after removal of a global baseline, and cannot be inferred merely from one-input smoothing or uncentered norm bounds.

## Scientific boundaries
Only finite uniform cycles, the single three-point median, real signals, and unweighted centered Euclidean distance are proved. The finite small-size certificate and uniform construction have different evidentiary roles. Historical priority remains qualified; independent review was not performed.

Self-review: passed. Independent audit: not yet performed.
