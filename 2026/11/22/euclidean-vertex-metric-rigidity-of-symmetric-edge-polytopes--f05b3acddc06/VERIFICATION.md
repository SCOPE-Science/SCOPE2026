---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reassessed the narrowed decoder in repairs/2/RESULT.md. The original Finding incorrectly assigns 2 and 3 to the raw squared-distance submatrix ranks. Since the six roots have center zero and norm squared 2, D = 4*11^T - 2G with G1=0. The raw ranks are 3 and 4, while the centered ranks are 2 and 3, also confirmed by independent exact matrix arithmetic. The corrected statement and proof distinguish both. The common sphere exposes every signed root; squared distances 8 pair antipodes uniquely, and cross-shells {2,6} versus {4} reconstruct incidence of distinct edges. Apply Whitney componentwise, resolving its sole connected ambiguity by Gram rank: incidence span has dimension v-1 in a connected component. A single edge presents no ambiguity. The decoder is invariant under point permutation, and nearest-even rounding is exact under the strict bound; it cannot detect isolates.

## originality

PASS

PASS is for the repaired distance-table decoder with exception handling and deterministic rounding guarantee, not for the original framing of the Euclidean classification. Cuchilla et al. Theorem 3.8 directly covers the connected classification. After splitting the intrinsic metric into components, its result also yields the disconnected uniqueness consequence; that consequence is no longer presented as original. The distinct output is a direct reconstruction procedure in the squared-distance table through line-graph inversion and a six-point test, without constructing root coordinates or a lattice.

## value

PASS

The repair gives a usable exact decoder for unlabeled SEP distances, not just a test of isometry or an injectivity theorem. It avoids fitting an ambient realization or enumerating graph candidates: the pairwise shells supply a standard line-graph inversion instance, with a local fixed-size exception test and an immediately usable deterministic input tolerance. This is a natural reconstruction task even when connected uniqueness is already known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
