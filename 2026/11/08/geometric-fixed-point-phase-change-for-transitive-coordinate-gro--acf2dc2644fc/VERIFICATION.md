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

# Reproduction and evidentiary limits

Run `python3 verify.py` using Python 3.8 or newer, from the directory containing the verifier. No external packages, datasets, websites, or author credentials are required. The program constructs coordinate-permutation orbits of all binary words in the indicated small dimensions, enumerates those having pairwise Hamming diameter at most two, enumerates every compatible union of such orbits as a face, computes mod-two homology by exact bit-level row reduction, and checks orbit-size and face-count predictions.

The script checks 32 generated coordinate-transitive groups in dimensions one through eight (cyclic, dihedral, symmetric, alternating, imprimitive, and a Klein-four action where applicable). The expected ordinary mod-two Betti vectors are \((1)\) for dimensions one and two, \((1,1)\) for dimension three, and \((2)\) for every checked dimension at least four. Every test passed. The attached output ends with the exact line `ALL_VERIFY_OK cases=32`.

The general proof is **not** inferred from these finite tests. Its critical infinite steps are: barycentric orbit-face identification; the star/top dichotomy for cliques of the Johnson graph; exclusion of all intermediate-weight orbits using transitivity; and explicit compatibility of the four remaining orbits. This establishes the PL classification for all permitted groups, including those not computationally enumerated.

Limits: the script does not enumerate every transitive subgroup up to isomorphism, does not test scales other than two, and does not establish independence from possible unindexed prior statements. Independent audit remains unperformed.
