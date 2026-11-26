---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The classification into zero, two, and four transitions is exhaustive. The three two-transition families contain the complete middle run; only the two families beginning in zero can overlap, precisely at equal b,d and radii at most min(a,c,e). The four-transition family exists exactly when b=d and adds min(a,e) strings. Pairing the larger external zero run with c through max+min gives the displayed formula, with duplicate subtraction and the new four-transition family canceling the residual loss at b=d. If defect is k>0, both outer runs have length at least c+k and the unequal positive one-run lengths sum to at least three. Thus n>=2k+6. The tuple (k+1,1,1,2,n-k-5) attains each positive admissible k, and equal one-run lengths attain zero for every n>=5. The length-eight word 00101100 has defect one. The checker and verification note were read, not executed; a separate replay /workspace/branches/replay_frozen.py computed defects through longest palindromic suffixes for all 42504 positive five-part compositions at n=5–24 and confirmed the formula and the lengthwise spectra. The proof, not the finite replay, covers the unbounded claim.

## originality

FAIL

The separate indexed six-run record states exactly the whole five-run numerical law. The fixed-length spectrum and length-eight onset follow from it by a sharp elementary bound and assigning surplus length to one outer run. The same date does not imply a priority order; it does not erase the demonstrated coverage. An earlier three-one record already gives a subfamily attaining the full positive range, and the first example is known up to complementation.

## value

FAIL

The invariant is natural, but the nontrivial five-run calculation duplicates the exact indexed law. The remaining interval is obtained by the elementary size bound and putting all length slack in one terminal run; even its positive attaining family is covered by the indexed weight-three law. No independently useful nonmechanical remainder survives in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
