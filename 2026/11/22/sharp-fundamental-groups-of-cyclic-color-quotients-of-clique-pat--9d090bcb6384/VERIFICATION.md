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

The included `strip_quotient_check.py` constructs exact **geometric** simplicial-orbit boundaries with orientation signs. Each nonempty face has a free \(C_q\)-orbit; the checker uses one oriented representative per orbit, verifies \(\partial^2=0\), chooses a spanning tree of the quotient one-skeleton, and computes integral first-homology invariants using Smith normal form over \(\mathbb Z\).

Verified parameter pairs (\(q,m\)): \((3,2),(3,3),(3,4),(3,5),(4,2),(4,3),(4,4),(5,2),(5,3),(5,4)\). The resulting first-homology groups are, respectively, \(\mathbb Z,\mathbb Z,\mathbb Z/3,\mathbb Z/3,\mathbb Z^2,\mathbb Z/4,\mathbb Z/4,\mathbb Z^3,\mathbb Z/5,\mathbb Z/5\). Run `python strip_quotient_check.py` with Python 3 and SymPy.

The finite checks do not prove the infinite family. That proof is the closed-star cover and van Kampen argument in `RESULT.md`; the proof also treats each excluded boundary regime and the action's freeness. No external independent audit has been performed.
