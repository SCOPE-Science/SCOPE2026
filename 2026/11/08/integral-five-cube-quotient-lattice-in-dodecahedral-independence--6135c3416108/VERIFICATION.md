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

For GP(10,2), independent enumeration gives 5828 faces, including five maximum independent octets. I reconstructed the sequential vertex matching: 2912 pairs, four unpaired size-six faces; built the low-face directed gradient graph and verified its acyclicity, then lifted all four critical 5-cells to integral cycles of 223,251,189,96 facets. The 120 graph automorphisms form a group with 60-element derived subgroup, and independent signed face-Lefschetz computation agrees with the rational ε·(#fixed octets−1) trace for every element. On the four critical generators the central involution is exactly -I; the 5-octet orbit map has columns [[0,0,1,0,-1],[0,0,0,1,-1],[0,1,-1,0,0],[1,-1,0,0,0]], sum zero and a unit 4×4 minor. This identifies H_5 integrally with ε⊗(Z[Ω]/Z∑Ω), not merely its character. The modular-5 coinvariant distinction follows also directly from the transitive permutation exact sequence: quotient coinvariants Z/5 vs augmentation coinvariants zero under A5.

## originality

PASS

Earlier 2026-11-01 full result proves only the rational orientation-twisted five-set module and explicitly disclaims determining the integral Z[G]-lattice; 2026-10-18 earlier published record is likewise rational. The older nonequivariant dodecahedral wedge result proves abstract rank four but not its integral automorphism lattice. The new index-one 5-orbit map and mod-five quotient-versus-augmentation distinction are neither consequences of the rational character nor restatements of the known wedge.

## value

PASS

Five maximum independent octets are a canonical A5-set for the dodecahedral graph, so the integral homology lattice is naturally asked for. Quotient and augmentation lattices have identical Q characters but inequivalent mod-five coinvariants; distinguishing them is a genuine structural invariant relevant to modular equivariant topology, not a merely cosmetic presentation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
