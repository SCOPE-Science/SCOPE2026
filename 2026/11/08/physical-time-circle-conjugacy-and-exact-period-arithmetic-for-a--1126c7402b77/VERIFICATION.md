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

# Verification of the physical-time conjugacy

The proof independently derives both reset branches from the stated planar map: one step for \(x>1/(1+r)\), two for \(\mu<x\le1/(1+r)\). The second tentative risk state is \(-(1+r)(\beta+1)x<-1\) because \(r(\beta+1)>1\). On the four right-closed arcs, the same formulas show \(F\circ H=H\circ R\) **pointwise**, including switching endpoints. The rotation of circumference \(2(1+a)\) then determines all prime periods and the irrational Haar spectrum. A direct roof coboundary gives the exact physical reset count.

Run `python checker.py` in this package (Python standard library only). The checker explicitly updates the original two-dimensional map with exact `Fraction` arithmetic for rational resonances \(a=1/q\), \(3\le q\le12\), and checks prime-period nonreturn before the asserted first return. It also verifies exact two-step reset branches and samples additional admissible real parameters with a deterministic pseudorandom seed. Its output includes 4,750 exact prime-period assertions, 11,940 exact branch/tower assertions, 170 exact original-step phase-circle assertions, and 10,000 floating-point section assertions; finite checks cannot prove universal real-parameter, irrational, uniqueness or spectral assertions. Those follow from the fully written proof, not the checker. No independent external audit or computer proof certification was performed.
