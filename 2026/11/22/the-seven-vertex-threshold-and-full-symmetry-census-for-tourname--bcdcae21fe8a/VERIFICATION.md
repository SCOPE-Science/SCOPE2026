---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducibility

Compile `verify.cpp` using a C++17 compiler, for example `c++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify`, and execute `./verify`. The full enumeration prints `ALL_CHECKS_OK` only after assertions of \(1{,}503{,}216\) labelled rank-three seven-point tournaments, \(313\) corresponding isomorphism classes, \(456\) total classes, the automorphism-order histogram, and their exact orbit-size sums. The code enumerates exactly the integer mask interval from zero through \(2^{21}-1\), with every bit assignment representing one labelled tournament; it does not sample the claimed finite census.

`independent_check.py` implements the rank recursion over actual vertex subsets, and checks agreement with the optimized witness criterion exhaustively through order five and for 1,000 deterministic masks at each of orders six and seven. This separately cross-checks the semantic reduction, but is not an exhaustive independent orbit or labelled census. Published McKay catalogues supply a separate cross-check for the total of 456 unlabelled tournaments, not for the claimed rank-three tally.

Scope: finite tournaments and their ordinal-free, finite one-point-extension rank levels. The statement makes no inference about infinite hosts. Only the displayed orbit census relies on executable exhaustive finite computation; the lower threshold, rank criterion, and upper rank-four exclusion have mathematical proofs. Mathematical and historical-priority peer audits remain unperformed.
