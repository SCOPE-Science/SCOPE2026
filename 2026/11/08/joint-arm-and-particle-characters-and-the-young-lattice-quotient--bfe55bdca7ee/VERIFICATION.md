---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Radial-order graph model Γ_{m,k} has A-vertices equal to m ordered arm words, B-vertices equal to one center label plus words, and m edges from each B. Counts k! binom(k+m-1,m-1), k! binom(k+m-2,m-1), and m times the latter give known Betti rank E-V+1. Simultaneous symmetry fixes an A-word iff every d-cycle of particle labels is placed, with one of d phases, on an arm d-cycle, yielding F(α,β)=∏ d^{c_d}c_d! binom(c_d+a_d-1,a_d-1). Fixed B-vertices require a fixed center particle, count B; fixed edges are a_1 B. Lefschetz then yields 1-F+(a_1-1)B. Taking orbit arm occupancies gives A-partitions of k, B-partitions of k-1, and distinct Young-cover edge orbits, producing rank r_m(k). A six-vertex cycle exists for k≥5, with m≥3; direct partition enumeration gives tree for k≤4 and r_m(5)=1. Independently reconstructed 360 A, 240 B and 720 edges at (m,k)=(3,4), checked all 144 S_3×S_4 character values by actual fixed-word enumeration, and checked quotient partition ranks for k=2..8. The equivariant collar/graph-model equivalence uses the stated convex radial-order strata and central transfers; the finite check corroborates but does not replace that topology.

## originality

PASS

Lütgehetmann 2014 Proposition 3.5 supplies the complete S_k-only rational module and old Betti rank, not mixed S_m×S_k character; previously published full arm module for unordered particles and two/three-particle cases imply some specializations but not the all-k simultaneous character. The two-rank Young-lattice quotient adds an explicit topological orbit classification.

## value

PASS

Simultaneous arm and particle relabeling are natural physical and combinatorial symmetries. The full character and first cyclic quotient at five particles expose topology hidden in the previously known one-factor representation and rank formula; this is a structural all-parameter theorem, not a repackaged small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
