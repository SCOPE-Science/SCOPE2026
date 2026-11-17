---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For the unit one-impulse cyclic window g=(1+z delta_0)/sqrt(N+|z|^2+2 Re z), full Gabor intensity-lifting singular values are sqrt(N) times Weyl self-ambiguity magnitudes. The mixed nonzero translation/modulation labels sample every product residue mod composite N (zero using nonzero zero divisors), so their minimum is 2|z| min_j|cos(arg z-pi j/N)| over B. Arithmetic-geometric mean forces |z|=sqrt N; the optimal phase is pi for odd composite N>=9 and pi±pi/(2N) for even N>=6. At these phases both unmixed-axis magnitudes exceed the mixed minimum; this yields exactly the two claimed sharp condition numbers and optimizer equality sets. Direct independently recomputed ambiguity values at N=6,8,9,10,15 confirm the formulas. The full mathematical proof is correct but neither parity branch is new.

## originality

FAIL

Two already published complete theorems cover the whole composite domain, with the identical window, measurement, norm, exact condition numbers, and all optimizer phases. The odd-composite theorem proves the z=-sqrt N branch for every odd composite N>=9; the even-order theorem proves z=-sqrt N exp(±pi i/(2N)) for every even N>=6. Their union implies the submitted theorem immediately, without a new invariant, structural lemma, boundary case, or stronger scope. All were dated November 8, 2026; no intra-day temporal ordering is claimed, only demonstrable published statement coverage.

## value

FAIL

The exact sharp conditioning of the one-impulse Gabor frame is a legitimate mathematical problem, but both parity components and the proof mechanism are already established independently in full. Merely combining the odd and even published formulas into one parity slogan is a routine collation with no additional mathematical obstacle, classification, or independent value; code reproducibility does not rescue the duplicate contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
