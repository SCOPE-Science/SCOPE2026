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

# Verification

Reproduce by running `python3 verify_modal_tree.py` with Python 3 and no third-party packages. The script separately enumerates unordered coloured rooted tree shapes by vertex order through six vertices, computes direct modal signatures and minimum orders, tests literal depth-bounded forth/back bisimulation on all small pairs, and compares against the exact polynomial recurrence. It also checks full finite histograms, extremal coefficients, consecutive support, palindrome symmetry, exact mean and variance, and a Berry--Esseen bound against directly accumulated normal-CDF discrepancies in tractable instances.

The script concludes with `VERIFY_OK`. The finite cases include zero or one propositional letter and depths through four (according to tractability). The exact all-depth claims rest on the recursive proof and the explicitly stated Berry--Esseen and Hoeffding inequalities; the finite checker does not certify unbounded induction, unique scientific priority, or independent review. The result is specifically **tree-relative** and assumes one non-counting child modality.
