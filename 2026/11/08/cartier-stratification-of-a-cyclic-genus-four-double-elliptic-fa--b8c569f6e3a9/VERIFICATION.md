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

# Verification of the cyclic double-elliptic stratification

## Executed checks

From the package directory the following two standalone Python standard-library programs were run successfully:

`python3 verify_multinomial.py`

The multinomial computation returned the complete characteristic-five Hasse–Witt matrix with its only nonzero polynomial entry \(t^2-2\) in the fourth diagonal position, and the complete characteristic-seven diagonal entries \(3\), \(3t^3-2t\), \(0\), \(t^3-2t\). Terminal marker: `VERIFY_MULTINOMIAL_PASS`.

`python3 verify_expansion.py`

A distinct modular sparse-polynomial multiplication implementation computed \(225\) terms at characteristic five and \(784\) at characteristic seven for \((PQ)^{p-1}\), then matched all sixteen Hasse–Witt target monomials and the same coefficients. Terminal marker: `VERIFY_EXPANSION_PASS`.

## Mathematically verified limits

Both scripts certify finite exact coefficient identities over \(\mathbf F_p[t]\), not all possible geometric branch divisors or arbitrary-characteristic curves. The full assertions for every \(t\in\overline{\mathbf F}_p\) follow from polynomial identities plus the transversality, Frobenius-semilinearity, and prime-to-\(p\) Prym-isogeny arguments in `RESULT.md`. No finite parameter enumeration is passed off as an infinite proof. No independent mathematical audit is asserted, and the priority search is incomplete by its nature.
