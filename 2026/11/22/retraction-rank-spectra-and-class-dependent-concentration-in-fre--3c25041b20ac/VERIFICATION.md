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

The theorem is proved by a free-generator automorphism normal form, an exact stabilizer calculation, and a uniform saddle-point estimate for Witt dimensions. The standalone `verify.py` executes exhaustive independent finite computations for the free rank-two Lie algebras of classes three and four, including the induced structure-constant maps rather than merely substituting a formula.

Run `python3 verify.py` using Python 3 with only its standard library. Expected counts by abelianization rank \(0,1,2\) are \((1,48,1)\) for class three over \(\mathbb F_2\), \((1,324,1)\) for class three over \(\mathbb F_3\), and \((1,384,1)\) for class four over \(\mathbb F_2\). These finite cases test the proof but cannot verify the unbounded theorem. The external independent audit has not been performed.
