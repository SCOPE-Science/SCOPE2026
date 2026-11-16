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

# Exact arithmetic verification

In the same directory, run `python3 verify.py` followed by `python3 crosscheck.py`. Both use Python's standard library and no network access. The supplied compressed binary certificate contains exact signed int16 entries of three matrices, in degree order 1, 2, 3, each \(288\times288\), little-endian, row-major, after zlib decompression. Their integer scales are 288, 2880, and 2880.

`verify.py` proves the real Gram ranks by checking the following exact identities: every scaled projector is symmetric; its square is its stated scale times itself; its product with the integer Gram matrix vanishes; its trace is the scale times the expected kernel dimension. Modular Gaussian elimination over \(\mathbb F_{1009}\) independently checks matching lower bounds on rational Gram rank. Degree four has full modular rank 288; degree zero has the constant rank one. The script separately checks direct monomial-column ranks over characteristic two, which differ by one at degree two and are not substituted for rational ranks.

`crosscheck.py` independently enumerates 12 normalized Shidoku boards and all 24 symbol relabelings, computes direct characteristic-two ranks via feature-column bitsets, and checks the known 25,728 unique four-clue patterns. No finite sample extrapolation or external formal proof certificate is involved.

The proof is finite and exhaustive only for the stated \(4\times4\) domain. A self-review passed; an independent audit has not been performed.
