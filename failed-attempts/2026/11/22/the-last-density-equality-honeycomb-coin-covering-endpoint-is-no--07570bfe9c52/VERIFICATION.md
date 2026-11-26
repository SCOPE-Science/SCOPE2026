---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

I independently enumerated circle intersections in Cartesian coordinates with an anisotropic integer metric, using rational intervals for the squared-distance comparisons and handling radical equalities exactly. I obtained 54 sites, 2,352 intersection events, maximum occupancy 26, 180 maximizing events and 30 distinct midpoint centers in the finite enumeration; these give exactly the six stated cosets and both norm-39 unit classes occur in the diameter pairs. Every center can be translated to the closed fundamental parallelogram, whose norm bound confines its entire disk's sites to the finite list. For any chosen 26 of these sites, their admissible-center intersection is compact and has a point on two of the defining circles: if no point had two active constraints, its connected boundary in the interior-nonempty case would be a single whole circle, impossible for two distinct equal disks; in the empty-interior case a lone active constraint would give interior points nearby. At the resulting candidate the chosen 26 sites exhaust the finite-list hits, so they include a diameter pair; the only center containing this pair is its midpoint. This proves exhaustiveness even when the auxiliary candidate is outside the fundamental parallelogram, and rules out 27 hits. Kittipassorn–Phetmak–Sriamorn Lemma 3.14 applies under the contrary covering hypothesis because the scaled density is 13/√3 and the exact occupancy maximum is 26. It supplies the existence of a triangular-lattice covering of minimum scaled center distance 2, not a statement that every hypothetical covering is hexagonal. In unscaled coordinates the shortest vector u has norm 39; 2u is Eisenstein and its norm 156 is even, forcing both its integer coordinates even. Norm divisibility by 3 then gives u∈Λ, so uZ[ω] has index 13 in Λ. Every maximal disk repeats a class among the 26 honeycomb residues modulo uZ[ω] by the diameter pair associated to u; translations do not recover the missing residue. Thus the noncoverability and the sharper center classification both hold as stated for closed disks.

## originality

FAIL

A distinct published Resultary record, 6b97e17b63e3, demonstrably covers the entire main result and the sharper classification, using the same rigidity reduction and repeated-residue obstruction. It states the same noncoverability at 2/√39 for the same closed-disk honeycomb, the same six cosets and an antipodal pair from each of the same two norm-39 associate classes. Its statement that there are exactly two pairs is even more precise. Both records are listed on the same UTC date; this comparison establishes equivalent substantive coverage, not precedence or provenance. The cited primary v1 article actually leaves this endpoint open and is not itself the source of the duplication.

## value

PASS

As a mathematical result the endpoint is a natural critical-density exception explicitly isolated in the precursor; the sharp finite geometry and congruence obstruction settle a genuine packing/covering boundary that ordinary density alone does not decide. This intrinsic value does not add a distinct contribution beyond the matched published record and cannot overcome the originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
