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
# Computational verification and limits

Execute `python affine_pebble.py` and `python check_affine_algebra.py` with Python 3, without dependencies. Both programs and their captured outputs accompany the theorem.

The first program independently constructs all affine tuple orbit types for each tested dimension and variable width, enumerates possible one-coordinate pebble moves and iteratively refines atomic-compatible classes until the finite partition stabilizes. It tests ten dimension/width pairs: in particular dimensions 4 and 5 are equivalent at widths five and six, but distinct at seven. This is a finite combinatorial corroboration of a permanent strategy, not a bound on the quantifier depth of the general theorem. The refinement state space reaches 5,585 affine-orbit states at width seven.

The separate program evaluates the recursive first-order even-parity formulas for 71,388 exhaustive/sampled assignments, and independently checks affine-independent canonical witnesses in dimensions 0 through 6. Its finite input range and seeded sampling are explicit in the code. Neither program certifies all dimensions or proves the absence of prior publications; the mathematical proof provides the universal quantifiers. Both outputs are to be replayed against the embedded text files.
