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

# Verification and reproducibility

Run from the directory containing the three bundled Python 3 files:

```sh
python3 verify_monophonic_triangular.py
python3 verify_homology.py
python3 verify_equivariance.py
```

The first verifier enumerates all graph-theoretic induced paths and all \(2^{\binom n2}\) vertex subsets at \(3\le n\le6\), then compares the face and facet polynomials and Euler characteristics. It prints `VERIFY_OK`. The second independently builds the faces and exact mod-two boundary matrices for \(4\le n\le7\), with positive Betti pairs \((3,1),(15,4),(45,10),(105,20)\); it prints `HOMOLOGY_OK`.

The third verifier represents permutations by their exact signed action on disjoint-edge pairs. It checks all 24 permutations of \(\mathfrak S_4\), verifying that the signed matching-pair character is \(\#\operatorname{Fix}(\sigma)-1\), the irreducible \((3,1)\) character. It checks the basis count, representative traces and the hook-length dimensions of every Pieri constituent for \(4\le n\le9\), printing `EQUIVARIANCE_OK`.

These programs use only standard Python libraries and exact arithmetic. They are finite checks of a theorem proved for every \(n\ge4\) by a natural equivariant relative-homology isomorphism, induction in stages, and Pieri's rule. Mod-two tests do not prove integral torsion-freeness, and no independent publication-priority certification is claimed.
