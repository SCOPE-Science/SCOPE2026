---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the stated graph and three labeled colors, fixing the apex to 0 costs a factor of exactly three. The Mycielski recoloring argument gives chromatic number 3 for even rims and 4 for odd rims; an alternately 0/1 colored odd rim, all clones 2 and apex 0 attains exactly one monochromatic edge. In the transfer trace a step from (a,b) to (b,c) counts edge b–c and the three edges at the clone of the middle vertex. This counts each edge and assignment exactly once with a fixed indexing origin, including at n=4. Reconstructed the integer transfer certificates in /workspace/evidence/5_transfer_reconstruction.py; replay with python3 yields det(lambda I-A)=lambda^9-5lambda^7+6lambda^5-lambda^3 and tr(B A^(2k))=4,12,44,152,508 for k=0..4. Cayley–Hamilton gives A^3(A^6-5A^4+6A^2-I)=0, so these traces establish the two low-index instances and the rest follow algebraically; first-order insertions at n positions have equal trace by cyclicity. The even formula follows from the paired nonzero eigenvalues. The cubic has sign changes isolating three positive roots in (0,1/2), (1,2), (3,4); the odd generating-function numerator 4-8y+8y^2 is strictly positive on the real axis so the dominant pole is not canceled, and its coefficient is positive since the other denominators at y=1/rho_max are positive. Dividing k log(rho_max)+O(log k) by 2n+1 gives the claimed limit and the factor n gives the odd logarithmic correction. Frozen enumeration is corroboration, not an all-length proof.

## originality

PASS

Credit the known chromatic obstruction and general Potts/Tutte representation, and exclude the matched finite Grötzsch case from the novelty judgment. Distinct evidence for the surviving finding is the all-length evaluation of both parity branches, the one-defect recurrence, and the common entropy. The inspected statements do not supply that evaluation; the conclusion is best-of-knowledge, not historical priority certification.

## value

PASS

The natural sparse Mycielskian family has exactly one unavoidable odd-rim defect. Determining the number of states accommodating it, rather than rediscovering the frustration from chromaticity, gives an exact zero-temperature benchmark: the two parities have the same exponential growth but only the odd branch carries a linear count prefactor. The family formulas, not an isolated table entry or generic transfer identity, supply that comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
