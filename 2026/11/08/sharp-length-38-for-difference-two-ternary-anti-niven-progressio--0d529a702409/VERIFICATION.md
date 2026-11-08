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

The accompanying `verify.py` checks all 27 possible starting residues modulo 27 by explicit triples, with each triple's three indices in one 27-block and their digit sums covering residues 0, 1, 2 modulo 3. An exhaustive independent-quotient test covers all 243 combinations of lower-block starting residue and the two arbitrary quotient digit-sum residues. This is the finite input to the general symbolic base-three decomposition proved in `RESULT.md`, which applies to all magnitudes.

The script also checks the 38 claimed anti-Niven terms using integer gcd and two separately coded base-three digit-sum functions. Its exact captured output is `verification_output.txt`. Five thousand small starting points were additionally checked; these finite samples are corroboration, not a replacement for the global proof.

The self-review found the block argument and witness sufficient for the stated maximum. Independent audit has not been performed. Mathematical scope is restricted to base three and difference two, and literature indexing is not guaranteed to be exhaustive.
