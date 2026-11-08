# Scientific review — exact minimal Roman cycle weight census

## Correctness: PASS

A pointwise-minimal Roman function is determined uniquely by its set of vertices labelled \(2\): all their other neighbors are \(0\) and remaining vertices are \(1\). Each labelled \(2\) must have a private adjacent \(0\), or its value can be reduced. Along a cycle this is equivalent to forbidding adjacent cyclic gaps of lengths zero or one. The block transfer-matrix trace logarithm counts all admissible circular gap words, and its multiplicity \(n/k\) is justified by counting distinguished defenders, even for periodic patterns. Independent binomial counts recover every coefficient. The lower weight bound and all-long-gap constructions prove the precise support. The all-one RDF and small-order/single-defender boundary cases are included. The extracted verifier independently checked exhaustive functions and defender sets plus rational arithmetic; no extrapolation from finite computation is used as proof.

## Originality: PASS, with residual publication-priority risk

Abu-Khzam–Fernau–Mann (2022, arXiv:2204.04765) already established the general definition and private-neighbor criterion, and counted 16 minimal Roman functions on the five-cycle. *Roman Census* (arXiv:2208.05261) enumerates minimal functions for paths; it does not state this complete cycle polynomial. Deepak–Alwardi–Indiramma (2021) enumerates **all**, not minimal-only, RDFs on cycles; minimum-weight coefficients coincide and are already known. Plouffe (1992), Appendix A.178, contains exactly the univariate total sequence and rational denominator after an index shift; these numerical results are explicitly treated as **covered**. The surviving claim is the **full bivariate weight distribution**, its labelled gap-word counting identity, coefficient formula and support. Relevant indexed-record searches and cross-checks found no equivalent bivariate claim, but an unindexed stronger theorem remains possible. The 2021 primary PDF's indexed text was read; page screenshots returned HTTP 403.

## Mathematical value: PASS

The general enumerability of minimal Roman functions and the previously developed all-RDF cycle polynomial motivate a complete minimal-only weight refinement for this canonical infinite family. The result describes every nonminimum minimal labeling weight, not just a known extremal coefficient, and supplies exact coefficients with structural private-neighbor explanations. The bivariate polynomial strictly refines the known numeric Fielder sequence. This is a motivated natural complete classification, although the scalar totals themselves are not new.

## Limitations and prior-coverage statement

Scope is labelled simple cycles \(C_n\) with \(n\ge3\), and pointwise rather than weight-minimal RDFs. The univariate total sequence, minimum Roman domination weight and the five-cycle total are known before this work. The evidence does not establish exhaustive publication priority or independent mathematical validation. See RESULT.md for proof and references; verify.py reproduces finite checks.

Self-review: passed. Independent audit: not yet performed.
