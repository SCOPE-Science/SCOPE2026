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

The proof establishes a componentwise identity for the central-squarefree algebra of \(D_8\) and \(Q_8\) direct products, and proves the general formula without depending on enumeration. A separate exact checker in `CHECK.py` verifies multiplication tables and binary ranks for \(r=1,2\), including mixtures of dihedral and quaternion factors, and checks the central-polynomial recurrence through \(r=3\). The computed vectors are \((8,3,0)\), \((64,39,15,0)\), and \((512,387,243,63,0)\). To reproduce, run `python CHECK.py` with Python 3; no third-party dependencies are needed. These finite checks do not certify the infinite statement or establish independent scientific validation.
