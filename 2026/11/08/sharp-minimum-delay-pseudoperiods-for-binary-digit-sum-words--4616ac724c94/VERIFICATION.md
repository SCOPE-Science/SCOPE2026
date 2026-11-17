---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: RESULT.md defines positive fixed offsets independent of n and a lexicographic two-stage optimum for t_m(n)=s_2(n) mod m, all integers m>=2. At n=0, the unique admissible d<=2^m-1 is B=2^m-1, so the least horizon is B. Binary-carry case separation proves the explicit 2m-1 offsets all work for every n: if no low power-of-two works, the low bits have 0^a1^(m-a) with upper trailing-one run T; choosing the complementary offset 2^m-2^(a-r), r=T mod m in {1,...,a}, changes popcount by a-(a-r)-T= r-T divisible by m. The proof provides exact disjoint admissible shift sets E(0)={B}, E(N_j)={2^j} for j<m, and m-2 upper-half weight classes, forcing 2m-1 distinct offsets. Checked the carry/weight algebra, boundaries m=2, low-zeros case, and that necessary class membership is not claimed sufficient. Independently enumerated E(n) and all offsets for m=2..8, tested n<3000; this finite check corroborates, but does not establish the infinite claims.

## originality

PASS

PASS, qualified: the sharp minimum horizon follows trivially from n=0 and resembles the known dense coverage window, but the nontrivial uniformly sparse fixed-offset upper bound and matching 2m-1 lower bound for all moduli are not implied by the inspected interval-distribution or classical two-symbol pseudoperiodicity theorems. The exact lexicographic support optimum, not generic digit-sum recurrences, is credited. Search coverage is not historical-priority certification.

## value

PASS

PASS: minimizing a position-independent set of probes under the earliest possible return horizon is an intrinsically motivated sparse recurrence/automatic-word invariant, useful for periodicity tests and combinatorics on words. The exact linear-in-m cardinality despite exponential horizon and the disjoint Hamming-witness lower bound are a nonmechanical complete infinite-family tradeoff. The unrestricted minimum cardinality when the horizon grows remains unsolved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
