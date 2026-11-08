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

# Verification details

The independent-audit channel has not been performed.

Execute `python3 check.py` from the directory containing this file. The dependency-free checker generates labeled Prüfer trees of size two through five, verifies 1,356 exact-rational pair checks for two rounds at probability \(p=1/2\), and independently propagates integer-coefficient polynomials through the finite graph transition kernel. The symbolic checks verify \(w_2(p)=2p-p^2\), \(w_3(p)=2p^2-p^3\), \(w_4(p)=p^3\), and the exact third-round branch defect \(p^4(2-p)(1-p)^4\). It also checks that an extra leaf at the terminal endpoint of the five-vertex path does not affect the path-pair law through round three, and checks total state probability one.

The universal finite-tree theorem is proved by geodesic enumeration and conditional independence in `RESULT.md`; checking small trees does not prove the unrestricted claim. The sparse random-graph limit uses the known local limit of \(G(n,c/n)\), Talukdar's fixed-repetition local convergence theorem, a finite-depth degree-moment bound, and uniform integrability. The checker is not a test of these infinite limit theorems.
