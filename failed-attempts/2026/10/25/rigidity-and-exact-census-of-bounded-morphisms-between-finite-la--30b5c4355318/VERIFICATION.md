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

For any surjective monotone map and any target antichain level of size at least two, choose preimages of two distinct images there. They must lie in the same source level, since otherwise they are comparable. Every other preimage is in that level by comparing it to a preimage of a different image. Thus the preimage of each target level is confined to one source level. Two distinct target levels cannot have preimages confined to the same source level: from a preimage of a lower target point one must lift a higher target point, but all its preimages are in that same antichain and distinct from the starting point. The resulting assignment of levels is increasing by monotonicity and onto by nonemptiness of source levels, hence an increasing bijection. Levelwise surjections satisfy back, using the starting point for an equal target and any preimage in a higher level otherwise. For distinguished sets the level choices multiply and each surjection count is q! S(p,q), zero for p<q. Duplicating a singleton target level into two consecutive singleton source levels really is an onto bounded morphism: all distinct higher targets can be lifted in a higher level, and an equal target at the source point itself.

## originality

FAIL

The earlier October 18 prefix/tail normal form already gives the exact nonzero regime, rigidity and census. Its formal assumption that the source has no singleton level leaves out only an immediate zero case: if a point in a singleton source level maps into a target level of size at least two, a distinct point in that target level cannot have a preimage, since all other source points are comparable to the singleton-level point. Therefore the full principal claim is mechanically implied by the prior result plus this direct order obstruction; the Stirling notation is the same levelwise surjection count. The singleton-target sharpness illustration does not rescue the census claim.

## value

FAIL

The census is natural and the short argument is clear, but the exact invariant is already mechanically implied in all parameter cases. The only added source sizes yield no possible quotients by one monotonicity comparison. The singleton-target example is an elementary duplication, not a systematic description of the exceptional cases. No independently useful new exact invariant, witness at a substantive boundary, or broader classification remains in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
