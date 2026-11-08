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

# Verification information

The analytical proof gives a parameter-uniform conclusion for every stated pair of distinct primes and every stated exponent. The main nonstandard steps—cyclotomic reduction modulo \((1-\zeta_{q^k})\) and irreducibility of \(\Phi_p\) over \(\mathbb Q(\zeta_{q^k})\)—are justified explicitly in `RESULT.md`; the finite checks below do not replace those steps.

Run `python CHECK.py` using the Python standard library. The script constructs cyclotomic polynomials exactly and tests zero remainders, not floating-point approximations. For \((p,q,k)=(2,3,1),(3,2,1),(3,2,2),(2,3,2)\), it checks every \(p\)-point time set and every \(p\)-point frequency set, including nonspectral candidates. It additionally checks every pair of transversals for \((2,5,1),(3,2,3),(5,2,2)\). Cases with \(p=2\) or \(k=1\) are boundary controls, outside the stated domain. The successful final marker is `ALL_EXACT_CHECKS_PASSED`.

The checker does not exhaust infinitely many parameters, and no independent audit or external certificate is claimed. Priority over inaccessible older literature is not established.
