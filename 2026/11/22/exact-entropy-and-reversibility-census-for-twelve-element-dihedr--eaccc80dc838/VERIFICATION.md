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

The exact group-enumeration test is `python3 verify.py`. It constructs the order-twelve group from three generators and verifies all endomorphism tables against multiplication. It checks all commuting-image two-site local rules, their local-image sizes and the proposed global structural classification, as well as the first seven entropy-multiplicity polynomials. Expected results: 64 one-site endomorphisms, 12 onto one-site group automorphisms, 144 globally surjective two-site group cellular automata, 96 reversible two-site rules, and 168 locally surjective two-site homomorphisms.

The finite checks corroborate the structural classification; the general infinite-shift assertions use the proof in RESULT.md, the domain property of the Laurent-polynomial ring, the compact-group entropy addition theorem and the one-dimensional linear-entropy formula. No independently conducted mathematical audit is claimed.
