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

# Verification and limitations

The evidence consists of a rigorous primitive-root/rotation probabilistic proof in RESULT.md plus two exact-rational finite sanity checks. With Python 3 standard library, run `python3 verify_direct.py` and `python3 verify_fkm.py` from the package directory. The concatenated recorded stdout is `verification_output.txt`.

`verify_direct.py` reconstructs each inverse Lyndon word by comparing it with every proper nonempty suffix and independently enumerates repetitions of primitive anti-Lyndon roots. It verifies equality of exact probabilities for binary source masses \((1/2,1/2)\), \((2/3,1/3)\), \((9/10,1/10)\) through length 12 and ternary masses \((1/2,1/3,1/6)\) through length 8. `verify_fkm.py` generates prenecklaces by the reversed-order FKM extension algorithm and checks exact cardinalities against Möbius primitive-necklace formulas, the inverse-Lyndon suffix property and source-weight sums for alphabets of sizes two through four.

These programs test finitely many words and are not substitutes for the asymptotic proof. The infinite limit and summability of its error depend on the positive iid assumptions, the primitive-root orbit argument, a disjoint-block run bound, and the geometric remainder bound explicitly proved in RESULT.md. Independent mathematical audit has not been performed.
