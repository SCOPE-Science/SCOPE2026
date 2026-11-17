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

# Verification details

Run `python3 verify.py` with Python 3.9 or later, without additional packages. The expected exact output is embedded in `verify_output.txt`. The checker directly reduces the ordinary augmented simplicial boundary matrices over the field with two elements for each nondecreasing integer weight vector of lengths 2 to 6 and entries 1 to 4. It separately forms the full *integral* oriented boundaries \(\partial[1,S]\), checks \(\partial^2=0\), checks exact leading coefficient one, and verifies that every term is within the asserted birth filtration. For unique minimum weights of lengths at most five, it checks the actual signed action of every weight-preserving permutation against the proposed normalizer-basis transformation.

The checker records 205 weight profiles, 3,964 integral basis-cycle tests, and 289 permutation-action tests. These are independent finite consistency checks, not a proof for unbounded orbit lengths, large weights, or every finite group. The mathematical proof for all cases is the explicit unitriangular filtered chain isomorphism in `RESULT.md`.

Boundary cases: an empty fixed-point realization is allowed below the minimum orbit size; the formal augmented degree-minus-one interval is not included in nonnegative reduced persistence. When there is just one orbit, the nonnegative barcode is empty. This proof does not imply a statement about quotient spaces or modified weighted boundary operators.
