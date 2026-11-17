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
The symbolic proof uses the exact finite-rank cubic derived in Oliveira [1], together with an elementary, exhaustive split into the three terminal-switch types. The proof itself establishes the theorem for all integer branch counts and orientation words.

`verify.py` is a standalone checker using Python 3 and NumPy. It constructs every \(n\)-bit orientation word for \(3\le n\le12\), checks the matrix's square is strictly positive, checks Perron and nonleading eigenvalue bounds numerically, checks each eigenvalue against the specified cubic and checks the sharp-example asymptotic expression. The finite checks are regression evidence, not an infinite certificate; residual floating-point tolerance is explicit in code.

No external independent audit has been performed. Published premises are attributed rather than re-certified; indexed literature searches do not prove priority against every historical paper.
