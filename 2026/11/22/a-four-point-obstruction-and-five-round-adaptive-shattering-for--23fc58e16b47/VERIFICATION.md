---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact verification of the finite classification

The delivered directory contains `certificate.json`, `verify_projective.py`, and `verify_cyclic.py`. Both programs run under Python 3.10+ with no external libraries. Run `python3 verify_projective.py` and `python3 verify_cyclic.py` in the extracted directory; assertion failure gives a nonzero exit status.

The projective-coordinate checker regenerates the thirteen normalized projective points, thirteen lines, and 78 distinct six-point pair-sum concepts. It verifies every one of the 8192 support traces, the face polynomial, purity, full projective-group size 5616, all orbit representatives and cardinalities, all 32 four-support witness traces, every tree path and leaf concept, and the 36/15 one-point/two-point concept multiplicities.

The second checker instead uses the cyclic order-thirteen difference set \(\{0,1,3,9\}\) to reconstruct an isomorphic plane without using `certificate.json`, enumerates all 8192 supports independently, and evaluates the adaptive shattering depth using a memoized recursive tree test. It verifies identical face counts, the 702 four-facets, and depths five possible / six impossible.

The two successful program terminators are `TERNARY_TWO_LINE_XOR_PROJECTIVE_PASS concepts=78 faces=1080 facets=702 orbits=2 VC=4 Ldim=5` and `TERNARY_TWO_LINE_XOR_CYCLIC_PASS concepts=78 VC=4 Ldim=5 facets=702`.

These are finite mathematical reproducibility checks, not an independent mathematical audit and not a proof of analogous claims for larger finite fields. The stated structural argument for the impossibility of a six-round tree does not depend on executing the recursive verifier.
