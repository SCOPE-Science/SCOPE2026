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

# Reproducibility and mathematical verification

The exact determinant-free permanent recurrence uses Eisenstein coordinates \((u,v)\) meaning \(u+v\omega\), multiplication \((u,v)(s,t)=(us-vt,ut+vs-vt)\), and squared modulus \(u^2-uv+v^2\). Integer-only evaluation has no rounding thresholds. The supplied C++17 and Python programs separately enumerate all 6,561 cyclic exponent words and both assert the least squared modulus 1296, minimum multiplicity 48 and exactly 59 squared-level values.

The Python checker independently verifies that the explicit unrestricted character has permanent \(9\) using a subset recurrence and separately by enumerating all \(8!=40,320\) permutation products; residue counts are \((13446,13437,13437)\). The C++ checker directly checks cyclic attaining word \((1,1,0,1,1,0,0,0)\) has permanent \(36\omega\).

**Proof rather than experiment:** For each size-\(k\) partial-matching correction, the minimal \((1-\omega)\)-valuation is \((5,6,5,6,7,6,7,8)\) for \(k=1,\ldots,8\); the base permanent \(8!\) has valuation four. Thus every unrestricted coefficient has valuation four and modulus at least nine. This step covers every one of the \(3^{64}\) characters without brute-force enumeration. Computational exhaustion is used only for the 6,561 cyclic frequencies and the two explicit witnesses.

**Known limits:** No all-order stability theorem, unrestricted full spectrum, classification of cyclic equivalence classes or independent mathematical review is asserted. The 2015 closely titled literature could not be inspected in full; historical originality remains a bounded comparison.
