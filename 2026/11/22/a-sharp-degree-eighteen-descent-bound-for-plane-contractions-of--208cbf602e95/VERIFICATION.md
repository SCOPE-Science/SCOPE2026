---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The standard geometric blow-up gives the 56 exceptional classes in the four displayed families; for distinct curves zero numerical intersection is equivalent to disjointness. A Galois-stable disjoint seven-curve collection has a unique contraction up to isomorphism of the target, so it descends to a form of P^2; over a finite field the Brauer group is trivial. Conversely the exceptional collection of a plane contraction is stable. The least extension degree is the least Frobenius cycle length on unordered collections, not the order of Frobenius or the least degree splitting every curve. The seven reflections generate W(E7) and act faithfully because the exceptional classes span the Picard lattice. A separately written exhaustive Python/NumPy calculation rebuilt the lattice, enumerated 576 seven-cliques, closed the group and conjugacy classes under the generators, and computed cycle profiles of each representative. The 60 classes exhaust 2,903,040 elements and the exact length:count pairs were 1:694477, 2:1012627, 3:99008, 4:30240, 6:139328, 8:362880, 9:161280, 12:241920, 18:161280. The 161,280-element witness class has curve, set and quotient profiles 2^1 18^3, 18^32 and 9^32, respectively. Geiser D -> -K-D pairs distinct partners with intersection 2, so it cannot fix a disjoint collection as a set. The new calculation verifies the finite action, not the geometric classification or arithmetic realization. The latter was checked in Loughran–Trepalin Theorem 1.2 (p. 3), with no excluded fields q>=9. Replay from the workspace: python3 checks/record-2/e7_independent_check.py (NumPy); exact output alongside in e7_independent_check.log. Read the frozen census and supporting code statically, not by execution.

## originality

PASS

The 56-curve lattice, the classical 288-heptad geometry, and Frobenius-class realization are prior. In fact the old group order classes plus the S_7 stabilizer give a short route to the extreme number 18 alone. The material surviving contribution is the evaluated all-class census for the actual 576-set action, with an explicitly verified descent comparison on its two-sheeted quotient. The strongest distinct same-day matches tabulate the 288-heptad action or a different, aggregated and restricted action on chambers, not the evaluated full lift.

## value

PASS

The census evaluates a specific arithmetic descent invariant for every Weyl type, giving the exact possible extension degrees and their distribution on the natural geometric configuration. This lets future users distinguish shortening after quotient by Geiser from actual plane descent; on the witness every degree-nine heptad still leaves the two possible contractions exchanged. The value is the complete distribution and the practical lift distinction, not recomputation of the classical number of markings or simply quoting an element of order 18.

The dated certificate retains the supplied scientific assessment, sources and limitations.
