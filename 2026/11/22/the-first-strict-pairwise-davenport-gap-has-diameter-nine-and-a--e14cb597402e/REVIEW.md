# Scientific review

## Correctness — PASS

The universal length bound follows from a greedy opposite-sign ordering of a minimal zero-sum multiset, with distinct partial sums in an interval containing precisely the diameter many integers. The support reduction is monotone for the pairwise lower invariant. The complete exact integer enumerator covers every sorted mixed-sign zero-sum multiset at each diameter from two through nine and tests proper-submultiset sums exactly. It finds no strict witnesses before diameter nine and exactly two sign-related witnesses there. Independent direct positive/negative subset sums establish that the witness is minimal. A second exhaustive multiplicity-vector census proves the exact five atom types on the support and the maximal length five. Adding zero contributes only its singleton. The verifier reports the full finite candidate counts. No finite experiment is substituted for an infinite assertion: the theorem is finite, and the universal reduction proves the finite search is exhaustive.

## Originality — PASS, with explicit priority risk

The invariant and both general inequalities are prior work of Plagne–Tringali (arXiv:1405.4363, *Acta Arith.* 171 (2015), Theorem 1). Their published text explicitly credits W. Schmid with an example of strict inequality; that existence claim is not novel. Inspected Theorems 1–3 and the relevant proof establish bounds and interval extremizers, not a sharp least-diameter or unique minimizing-support classification. Sissokho (arXiv:1401.0715) addresses estimates and derivation order for integer minimal zero-sum sequences, not this exact gap profile. Targeted published-source and mathematical-record searches disclosed no dominating first-gap result. The unspecified Schmid example and possible historical finite enumerations remain residual priority risks; no claim of global uniqueness beyond the precise diameter constraint is made.

## Mathematical value — PASS

The pairwise lower invariant is the most accessible computable lower bound on the Davenport constant. Determining the first precise failure and classifying every smallest support tests its sharpness and differentiates higher-support atoms from primitive two-point sequences. The single sharp diameter and inverse uniqueness are motivated finite invariants attached to an established bound, not an arbitrary slice or known-table recomputation.

## Reproducibility and scope

The attached pure-Python certificate enumerates every relevant multiset through the sharp diameter, verifies minimality, classifies atoms on the unique four-point support, and checks impossibility of enlarging that support without destroying the strict inequality. The result is conditional on the exact stated integer-set definitions, not on an unverified generalization to other groups. Historical-priority completeness is not guaranteed.

Self-review: passed. Independent audit: not yet performed.
