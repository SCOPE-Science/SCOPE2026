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

The normalized conductor description is reconstructed in `RESULT.md`. The unit quotient has \(m(m-2)\) branch-jet parameters, and its ring-image subgroup has \(\sum_{d=1}^{m-2}(d+1)\). This proves the connected Picard dimension \((m-1)(m-2)/2\). For \(s=p^r\), the \(s\)-power image has \(m\lfloor(m-2)/s\rfloor\) parameters; the intersection with the ring-image subgroup has \(\sum_{j=1}^{\lfloor(m-2)/s\rfloor}(sj+1)\) parameters. This gives the formula in the result.

`verify.py` is self-contained Python code using modular field arithmetic. Run `python3 verify.py` from the folder containing the files and compare to `verify_output.txt`. It checks ranks over \(\mathbb F_{16}\), \(\mathbb F_9\), \(\mathbb F_{25}\), and \(\mathbb F_7\), tests every \(m\) in the stated ranges, and directly enumerates the ring-unit subgroup and square-image intersection in the four-line characteristic-two case (quotient image cardinality four over \(\mathbb F_4\)), and demonstrates a nonzero doubled class and zero fourth power. The recorded run ends with `ALL_CHECKS_PASSED`.

Finite-field tests do not prove the infinite-family theorem: the general argument depends on the fact that a nonzero binary homogeneous polynomial of degree less than \(m\) cannot vanish at \(m\) distinct projective directions. The computations do not certify historical novelty or independent mathematical verification.
