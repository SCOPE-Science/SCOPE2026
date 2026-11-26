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

Reflection about −1/2 turns the second cubic sum into δU, where δ=χ(−1). Substitution −x/(x+1) on the field minus −1 turns the quartic sum into δU−1, with the missing cubic summand δ at −1 accounting for the constant. In the sign-indicator expansion the two separable monic quadratic sums are −1. The zero terms at 0 and −1 are (1+b)(1+c) and (1+aδ)(1+c); at each cyclotomic root ρ the first two characters are 1 and δ because ρ=(ρ²)² and ρ+1=−ρ². Subtracting these terms gives the piecewise formulas with the stated singleton sign pair for each δ. The curve has q+1+U points and is smooth in the intended odd characteristics other than 3. Hasse yields simultaneous positivity by q≥71 (even the weakest lower bound q−19−6√q is positive and increasing there). Below 71 the 17 eligible primes and 25,49 exhaust the admissible orders. A fresh field enumeration verified all counts there and the exact exception list. In particular the bins at 49 in lexicographic order with + before − are (9,0,4,8,4,8,4,8); 41,43,47 and 53 have no missing bin. The stated cutoffs are the least eligible field orders after the last failure in their respective classes. Characteristic 3 is separate: the quadratic becomes (x−1)² and has no negative sign.

## originality

PASS

The distinct result is the exact one-trace histogram for this nonlinear tuple, with its sharp extension-field exceptions. Related exact sign-pattern results use different functions, and the strongest inspected generic shattering theorem concerns translates of the square set and gives asymptotic existence, not these counts. Credit Hasse, character orthogonality and indicator expansion as standard tools.

## value

PASS

This natural cyclotomic tuple has symmetries that turn several apparent trace inputs into one and give two orbit types of counts without enumerating each field. The order-49 obstruction proves that the extension-field cutoff differs from the prime-field cutoff. This is a precise, motivated boundary phenomenon, not just a numerical table or a generic large-field positivity argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
