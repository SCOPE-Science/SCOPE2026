---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

From the actual 18-vertex LCF construction, independent check enumerated 27 edges and cardinality-4/5/6 face counts (801,756,348). A fresh sparse F3 chain elimination (not merely acceptance of recorded stdout) gave rank(d4)=472, rank(d5)=274, dim H4=10. The signed rotation on oriented five-vertex simplices yields induced ten-dimensional R with ranks R-I=6 and (R-I)^2=2 and (R-I)^3=0, hence two J3 blocks, two J2 blocks and no J1. The attached integral Morse checker source supplies an explicit acyclic 1292-pair matching, critical cells 1,11,1 in dimensions 0,4,5 and primitive d5 vector, consistent with H4(Z)=Z^10; original script was inspected but integral matching was not rerun independently. All claims concern the fixed finite graph, not a general Pappus-family theorem.

## originality

PASS

An earlier full-text exact Pappus computation gives the rational order-three character, but rationalization does not determine Jordan blocks after reducing an integral C3 lattice modulo3. The constructed comparator lattices Z²⊕Z[ζ3]^4 and Z[C3]^2⊕Z[ζ3]^2 have the same Q character yet different mod3 Jordan types. Fresh exact chain ranks identify the graph’s actual class. No prior same modular decomposition was located in targeted searches.

## value

PASS

The Pappus graph is a canonical symmetric incidence graph, and the characteristic dividing the symmetry order is an inherently natural boundary between semisimple and nonsemisimple representations. An exact Jordan decomposition, not implied by the known rational character or nonequivariant homotopy type, is a motivated, reusable invariant of a natural complex.

The dated certificate retains the supplied scientific assessment, sources and limitations.
