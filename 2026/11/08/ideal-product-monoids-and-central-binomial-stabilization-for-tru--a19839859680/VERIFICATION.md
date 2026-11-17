---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Right projective e_iA is uniserial, giving unique thresholds 0≤t_i≤ell. Left-arrow closure iff t_{i−1}≤t_i+1. For products, u_{j+1}≥u_j−1 ensures a+u_{i+a} nondecreasing in a, hence (t⋆u)_i=min(ell,t_i+u_{i+t_i}). Trace of weighted transition matrix sums all labeled cyclic profiles by dimension. Shifting positive thresholds reduces N_{n,ell+1}−N_{n,ell} to minimum-zero profiles; their Catalan zero-to-zero gaps give 1/2*C(2n,n)=C(2n−1,n−1) for ell≥max(2,n−2). Frobenius path complement pairing proves dimension reciprocity. Independent exact profile enumeration n=2..7, multiple ell, confirmed palindromicity and stabilization; direct ordered product law inspected algebraically. Infinite n,ell results rely on combinatorial proof.

## originality

PASS

PASS qualified: classical Nakayama uniserial structure and radical-square-zero special cases are prior; Eisenbud–Griffith 1971 serial-ring results and Han 2010 truncated-cycle homology do not state this full ordered ideal multiplication monoid, dimension transfer trace, or sharp central binomial Loewy increment. Relevant Resultary cyclic Nakayama results concern Jordan types/Cartan invariants, not these ideal products. The novel natural invariant is not just substituting a standard one-sided module classification.

## value

PASS

PASS: the full multiplicative monoid of *two-sided* ideals, including noncommuting products, and their dimension distribution are natural representation-theoretic invariants of cyclic Nakayama algebras. Sharp eventual linear growth with an explicit Catalan central-binomial slope is a motivated structural cutoff and offers a uniform calculation for all fields, not an arbitrary small computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
