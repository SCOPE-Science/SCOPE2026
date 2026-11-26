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

The trace pairing is nondegenerate over the complex matrix space. The Weyl operators form an orthogonal basis, and their distinct conjugation characters are orthogonal, so the rank is the support size of the ambiguity coefficients (a sign convention can permute their indices). Global sign leaves every projector unchanged. Zero displacement leaves only zero modulation; at nonzero displacement nine signs cannot sum to zero. Reduction at a primitive cube root gives equality of the three column sums; for order nine, divisibility of a degree-at-most-eight polynomial by 1+z^3+z^6 forces three-periodic coefficient signs. For h_a(j)=g_j g_{j+a}, this forces u(j)=g_{j+3}/g_j invariant under +a. For a unit it is constant everywhere and for a=3,6 constant on each 3-orbit; either way the telescoping product of the three signs on each orbit gives u=1. The converse holds. Opposite shifts have the same cubic test. For a unit shift the normalized g corresponds bijectively to h_a of product one, with the event forcing 0 or 2 negatives per column. In the nonconstant case, the 27 choices of one positive edge per column split into three size-nine translation orbits: a nonidentity stabilizer would include shift by 3, which cannot preserve one positive edge per column. The representatives give exactly E1 with E3, E4, or E2, respectively. The unit action (in particular multiplication by 2 up to sign) propagates this to all six distinct pairs, each on nine windows. E3 holds on 108 nonperiodic windows by counting three nonconstant columns, 27 already in pairs, leaving 81 singles; the 117 remaining nonperiodic windows have no event. The four periodic windows have ranks 21 for the three nonconstant ones and 9 for the constant one. Independently evaluated every coefficient for all 256 windows by formal remainder arithmetic modulo 1+z^3+z^6, confirming rank totals 9:1, 21:3, 65:54, 69:81, 73:117 and all nonperiodic event profiles. The separately supplied norm argument is valid: reduction at an order-nine element kills a prime ideal over 531613, whereas every nonzero norm of the tested sums has modulus at most 9^6=531441. No conclusion here about synthesis rank, conditioning or nonlinear phase retrieval.

## originality

PASS

The general projector-span/ambiguity-support relation and cyclotomic arithmetic are prior. The supported distinct finding is the exact normalized sign-window histogram with its sharp maximum and structural four-event intersection classification. A pointwise test that permits a new enumeration is not an evaluated joint census or an orbit classification.

## value

PASS

Nine is the first odd prime-square cycle, and the smallest sign-only alphabet already exhibits both primitive and cubic cancellations. Assigning every possible rank and identifying all optimal sign designs via local events is a usable exact observability benchmark for the linear matrix measurement problem. The structural rank gaps, the loss from constant modulus, and the exceptional periodic classes make this more informative than measuring a particular window or quoting the general support identity; no phase-retrieval design guarantee is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
