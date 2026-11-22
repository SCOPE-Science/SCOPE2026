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

The analytic proof establishes (i) arbitrarily many disjoint small inverse branches, (ii) a uniform contraction on infinite orbit sequences, (iii) a compact onto full-shift factor, and (iv) periodic-point lifting by interval continuity. The inequalities are uniform for all selected branch indices and hold for each fixed positive \(a,b\) after taking the rectangle scale sufficiently small.

The standalone `check.py` runs high-precision finite diagnostics with `mpmath`. Two parameter pairs were tested: \((a,b)=(1,2)\), \(v=10^{-6}\), and \((a,b)=(30,20)\), \(v=10^{-8}\). In both, five branch representatives passed derivative, range, separation and inverse tests; finite Picard iterates satisfied both map coordinates. This does not verify the mathematical theorem for every \(a,b,N\), nor is finite iteration a replacement for Banach's theorem.

No independent audit has been performed. The compact-subsystem interpretation is essential: the formula is undefined at \(x=0\), and the proof does not establish continuity on the entire closed square.
