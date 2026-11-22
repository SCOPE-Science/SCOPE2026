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

# Verification and limits

Run `python3 verify.py` with Python 3.8 or later and no third-party dependencies. It constructs every Boolean matrix partner in dimensions one, two and three and checks every nonzero rank-one rectangle against direct matrix products. At dimension four, the script chooses one representative of each feasible triple of support sizes and intersection sizes and enumerates all `65536` Boolean matrix partners for each representative. It compares observed centralizer counts with the proposed closed formula, checks the combinatorial support multiplicities, and checks the first five row-and-column-covering counts.

Expected final line: `VERIFY_OK`. The checker replayed successfully in the present package. These tests have finite extent. The general statement is justified by the two-case Boolean-product identity and the disjoint block enumeration in RESULT.md, not extrapolation from experiments. The row-and-column-cover asymptotic uses a union probability with pairwise-intersection control. This does not constitute an independent audit or mathematical certification.
