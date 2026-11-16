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

The included `verify.py` is a complete, standard-library-only integer proof by exhaustive finite enumeration. Reproduce with `python3 verify.py --csv`; the generated `spectrum.csv` must agree byte-for-byte with the supplied table.

The script reconstructs all rank-at-most-four simply-laced positive root posets (types \(A_1,A_2,A_3,A_4,D_4\)); checks the corresponding root coordinates and order relations; enumerates antichains recursively and all masks independently; obtains ideals by down-closure and by all-mask verification; evaluates every character sum both directly and by Walsh–Hadamard butterflies; checks Parseval identities; and verifies the Fourier-support projection norms as exact fractions. For type \(D_4\), it additionally checks the complete six-element diagram-symmetry action on all frequencies and counts each zero orbit.

Finite domain sizes are at most \(2^{12}=4096\) frequencies, with 50 signed support terms in type \(D_4\). A log or hash by itself is not an infinite mathematical proof; here the claim is explicitly confined to the completely enumerated finite types. The unrestricted projection-optimality step is a direct translation-averaging argument given in `RESULT.md` and is not merely a numerical assertion.

Independent external validation and exhaustive worldwide historical-priority checking have not been performed.
