---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Reconstructed the unbounded step as well as the local one. For a cutoff 2^aK, at each odd divisor t of K, sum coefficients at 2^j d over d|t for each layer j. The transform is triangular with diagonal ones. The condition lcm(d,e)|t is equivalent to both d|t and e|t; two positive two-adic layers multiply to zero. Thus the cutoff ring is a product of F_2⊕F_2^a with square-zero second summand. Each local principal ideal is the ring, zero, or one radical line, so the stated case rule produces its meet. Enlarging to 2^bL pulls back the old t-coordinate along s↦gcd(s,K) and pads the radical vectors with zeros; the same case rule commutes with both operations. For w=xr=ys, include the finite supports of both witnesses in one larger cutoff, proving equality globally and yielding the claimed support bound; iteration gives the finite-intersection statement, with zero and all-odd cutoffs included. For (C_2,C_4), the homomorphism retaining the odd-divisor-1 coordinate and layers 0,1,2 is surjective, so the image of the actual source ideal is the two-dimensional radical; a principal source ideal would have principal image. This directly justifies the nonprincipality conclusion in place of relying on the wording about the inverse image. The frozen VERIFY.py and the recorded 139,536 finite pairs were inspected without running uploaded code; the finite checks are not the proof of compatibility at arbitrary cutoffs.

## originality

PASS

Gadouleau–Johnson already provide the multiplication and Boolean/square-zero structure. The general meet result with a stable finite-support construction is the distinct claim: their published discussion explicitly leaves arbitrary pairs open and establishes two restricted cases. The local radical-line argument is elementary, not claimed as a new abstract theorem.

## value

PASS

This closes an explicit general-case gap for a natural cycle ring, with an algorithm that stays within the inputs' divisor cutoff even though global multiples may use arbitrary cycles. The positive intersection theorem together with the nonprincipal two-generator sum identifies a meaningful boundary of the ring's ideal structure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
