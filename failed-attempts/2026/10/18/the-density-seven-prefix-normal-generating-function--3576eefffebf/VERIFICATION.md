---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed the shortest-span equivalence for fixed numbers of ones. For seven ones the length-one gap comparisons give five nonnegative excess gaps, the length-two and length-three comparisons give the four listed inequalities, and the other comparisons are redundant. The tail and the common gap increment have weights 1 and 6. For fixed A,B,C and s=D+E, there are s-max(0,A-C)+1 choices as soon as s>=max(A,A+B-C). Inverting the parameter substitutions confirms that the six regions are disjoint and cover the admissible triples, including all equality boundaries. Independently recomputed every region's geometric-series contribution: for exponent vector k, lower bounds l, and linear multiplicity 1+m·p, the unweighted sum is K=product z^(k_i l_i)/(1-z^k_i), and the weighted sum is K times [1+sum m_i(l_i+z^k_i/(1-z^k_i))]. Exact cancellation gives the stated numerator. Direct integer summation without region decomposition matches the rational coefficients through n=57 (p_7(57)=3531473); the symbolic argument, not the cutoff, establishes the claim at all lengths. Lengths below 7 have no terms and length 7 has coefficient 1. Replay: /tmp/opencode/frozen_density7_cubic.py, density7(). Inspected but did not run the frozen checker.

## originality

FAIL

The exact formula is covered by two distinct published catalogue findings: all 19 numerator coefficients and every denominator factor agree, and both matching records go beyond the exact formula. This is a finding of equivalent published coverage, not a conclusion that either later-dated catalogue record has priority or that this calculation is wrong. The cited 2014/2016 articles themselves do stop at density six.

## value

FAIL

The first omitted fixed-density series is a natural target and the exact formula would make a useful benchmark. As submitted, however, that benchmark is already available in two matching published findings. The frozen claim asserts no independently needed new invariant, more general cone method, or other substantive advance beyond those statements; a different calculation of the same function does not supply one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
