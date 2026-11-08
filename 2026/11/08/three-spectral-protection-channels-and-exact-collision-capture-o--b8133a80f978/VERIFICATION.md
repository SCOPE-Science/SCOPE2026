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

# Verification record

The classification for all integer \(q\ge3\) and \(m\ge2\) follows from the algebraic proof in RESULT.md. The following are reproducible finite corroborations, not an exhaustive parameter census or independent external certification.

`python3 verify_exact.py` uses standard-library integer arithmetic modulo \(1000003\) on collision-constrained energy-sector matrices. It passed at \((q,m)=(3,2),(4,2),(3,3),(4,3),(5,2)\), with six-sector nullity vectors respectively \((3,3,0,0,0,0)\), \((6,8,2,0,0,0)\), \((12,6,0,0,0,0)\), \((24,16,2,0,0,0)\), and \((10,15,5,0,0,0)\). The vector order is \(0,-Jm,-2Jm,Jm(q-1),Jm(q-2),2Jm(q-1)\).

`OPENBLAS_NUM_THREADS=1 python3 verify_numeric.py` (Python with NumPy) builds the independently normalized symmetric hopping matrix and collision projector. It passed at \((q,m)=(3,2),(4,2),(3,3),(4,3),(5,2),(3,4),(4,4)\), checking all stated sector dimensions, Hermiticity, projector idempotence, dark-space invariance, collision annihilation, and both localized capture formulas within \(10^{-8}\). The resulting total dark dimensions were \(6,16,18,42,30,42,88\), in that order.

The modular checks do not by themselves certify rational-rank upper bounds without the analytic construction; the independent floating-point checks do not constitute infinite proofs. The general proof also supplies these limits exactly, including degeneracy at the boundary values \(q=3\) and \(m=2\).
