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

# Verification record

Run `python3 verify.py` in this directory. The script uses only Python 3 standard-library integer arithmetic and deterministic pseudorandom samples. It builds cyclic subset-sum profiles by repeated integer convolution; computes every cyclic autocorrelation entry directly; and checks equivalence with sign-identified doubling invariance of generator multiplicities.

Exact exhaustive binary-multiplicity runs: moduli \(3,5,7,9,11,13,15,21\), with respectively \(4,16,64,64,1024,4096,256,4096\) multisets. Deterministic 100-case tests: moduli \(25,27,33,35,45,65,91,105\), using small nonnegative integer multiplicities. The composite modulus-65 example with generators \(\{1,2,4,8,16,32\}\) has subset-sum counts \(1\) at residues \(0\) through \(63\), zero at residue \(64\), and autocorrelation \(64\) at zero, \(63\) elsewhere. The modulus-nine example produces counts \((7,7,7,7,7,7,7,8,7)\) and autocorrelation \((456,455,455,455,455,455,455,455,455)\).

These checks are exact but finite. The infinite classification depends on the character-theoretic proof in `RESULT.md`, including the classical nonvanishing of primitive even Dirichlet \(L\)-functions at \(1\). No claim of exhaustive computation over arbitrary moduli or independent review is made.
