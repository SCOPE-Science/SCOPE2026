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

# Verification of the dyadic norm-one additive diameter

The proof derives all exponents from an explicit square-root criterion, rather than from extrapolated finite data. For odd–odd integers \(u,v\), compute \(h=(u^2+v^2)/2\); the fact \(h\equiv1\pmod4\) implies that \(2h^{-1}-1\) is \(1\) modulo \(8\). Choose a modular square root to form the two displayed norm-one vectors. Their norms and exact sum are direct algebraic identities. The modulo-eight obstruction separately establishes sharpness.

## Reproducing finite checks

With Python 3, run `python3 verify.py`. No third-party packages, network services, tables, or other files are required. The script checks for every exponent \(1\le k\le7\) that all odd–odd pairs occur in the double sumset, the triple and quadruple sumsets are precisely the two parity cosets, and \((2,2)\) is absent from the double sumset when \(k\ge3\). It additionally constructs both modular norm-one summands explicitly for every odd–odd target for \(1\le k\le9\). On replay the output ends in `VERIFY_OK` with `constructive_oddodd_certificates=87381`.

## Proof obligations and unproved limits

The critical infinite step is the square-root lemma: units congruent to \(1\) modulo \(8\) have modular square roots at arbitrarily high powers of two, proved by a one-bit lifting argument. The finite checker does not establish this infinite statement; its proof does. The result does not enumerate all two-summand multiplicities or extend to arbitrary quadratic forms or odd prime-power coefficient rings. Independent mathematical validation has not been performed.
