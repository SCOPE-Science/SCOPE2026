---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Each update reduces relevant prefix length by one until the first-letter subspace. The reduced loopless complete NOR map permutes the zero/one pair, fixes each singleton and sends every other nonuniform vector to zero. Periodicity forces membership in the image after d−1 steps; a specified two-one vector is attainable then by disjoint, individually surjective NOR trees (including height 0), hence realizes T=d. Initial leaves of distinct prefix evaluations have distinct suffixes, while leaves within a root are indexed by all admissible prepended strings, once each. Independence and equal bias therefore give the stated CDF as the disjoint probabilities of two uniform outcomes and q+1 single-block outcomes; at t=d−1 only one-hot outputs reach a fixed point. Exact integer counts use B_t and S_t as leaf counts. For the critical limit, differentiation of J(s) gives the sign of sum_{j=0}^{q−1} s^(−j)−q², strictly falling from +infinity to q−q². With endpoint limits 1 and 0 this establishes precisely one interior crossing of 1; monotone even iterates converge to opposite endpoints on either side, and p=p_* is stationary. The basin limit is (q+1)p_*² there, including the stated endpoint cases off criticality.

## originality

PASS

Credit the classical graph structure and strong same-day overlap in NOR prefix collapse, product bias recursion and exact shells on de Bruijn words. The Kautz fixed phases, extra block event and resulting exact nonzero critical basin are not obtained by substituting parameters in the two-uniform-state law. No inspected source provided a stronger theorem covering this additional phase and first-entry statement. This is a limited substantive distinction, not a priority determination for the method.

## value

PASS

Kautz is a standard directed network, and the effect of deleting same-letter transitions is qualitative: a uniform oscillator acquires q+1 coexisting fixed phases. The exact first-entry and individual-basin laws, and the isolated critical survival limit, measure the effect for all alphabets and depths and are useful beyond the elementary NOR-tree recursion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
