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

The proof checks the three action levels via an exact equivariant decomposition of the dominance complex into a join of simplex boundaries and two full simplices. The crucial chamber identifications are \(S(V)/A_k\cong S^{k-2}\) and \(S(V)/S_k\cong D^{k-2}\), where \(V\) is the standard sum-zero reflection representation. The shore exchange on the doubled alternating quotient is the linear swap on \(V\oplus V\), whose eigen-representation decomposition gives the projective-space join. The ball-attaching maps are nullhomotopic by dimension/connectivity. These arguments cover every integer \(k\ge3\).

The reproducible checker `verify_quotients.py` uses only the Python standard library. Execute `python verify_quotients.py`. It independently enumerates 50 and 226 nonempty faces for \(k=3,4\), and checks Euler characteristics under each of the four indicated symmetry actions, with all expected comparisons passing. Euler calculations alone do not prove homotopy decompositions or exclude torsion; the geometric proof supplies those statements. No external independent mathematical audit has been performed.
