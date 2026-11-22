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

# Verification of the nonbinary one-deletion profile theorem

The Python program constructs the explicit Euler-trail extremizer for every tested alphabet \(3\le q\le8\), checks the full set of local change signatures using direct deletion profiles, confirms the two required distinct unequal boundary pairs and compares the cardinality to \(q(q-1)^2+q+2\). It additionally enumerates every ternary word of lengths 2 through 9.

Run `python3 verify_profile_euler.py` and compare with `verify_profile_euler.out`.

The separate C++ program constructs every literal deletion descendant from scratch, forms its ordered adjacent-pair count vector, validates the ternary length-20 and quaternary length-46 witnesses, and enumerates all binary words through length 10, ternary words through length 11, and four-letter words through length 7. The q=2 check also reproduces the known first-six-profile length nine, which is outside the nonbinary first-length theorem.

Run `g++ -O2 -std=c++17 verify_profile_literal.cpp -o verify_literal && ./verify_literal` and compare with `verify_profile_literal.out`. The disposable executable is not a package dependency.

Both runs completed successfully from the packaged source files, and saved outputs matched the actual console results. All unbounded conclusions follow from the mathematical local-change classification, equal-vertex traversal bound, directed Euler-trail theorem, and independent-triple probability estimate, not from finite enumerations. Priority assessment remains limited by inaccessible recent-paper full text and unindexed equivalent literature.
