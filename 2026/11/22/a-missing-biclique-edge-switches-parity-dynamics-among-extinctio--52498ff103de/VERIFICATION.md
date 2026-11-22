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

# Scientific verification

The exact proof in `RESULT.md` gives a four-cell invariant-image reduction and derives all finite-field conclusions from the three possible characteristic-two matrix types. The crucial ranks are \((N,4,4,\ldots)\) for even-even, \((N,4,3,2,2,\ldots)\) for mixed parity, and \((N,4,2,0,\ldots)\) for odd-odd, where the rank sequence begins at the identity iterate.

From the same directory run `python3 verify_ranks.py` and `python3 verify_orbits.py`. No external Python packages are required. The first program checks the exact binary rank sequences, unmodified-graph comparison and global power identities for all 225 ordered size pairs \(2\le m,n\le16\). The second program builds independent neighbor-list updates and checks every initial state for nine binary and six four-element-field cases, comparing first-entry times, primitive temporal orbit counts and every individual basin with symbolic predictions (15,376 states altogether). Exact finite-field addition for four elements is two-bit XOR because only the field coefficients zero and one occur. The observed success markers are saved in `verification_output.txt`.

Finite testing corroborates but cannot establish all-size correctness. The proof requires nonempty residual shores and characteristic two; no claim of independent external auditing or additional formal verification is made.
