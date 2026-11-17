---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For every uniform mapping, removing a prescribed set of r zero-indegree vertices leaves an independent uniform mapping on the other n-r vertices; cyclic points cannot belong to the deleted set. Combining this deletion identity with the exact rooted-forest k n^(n-k-1) count gives E[binom(Z,r)|C=k]=binom(n-k,r)(1-r/n)^(n-k-1), exact conditional empty-box occupancy, and strict descending conditional mean. For k=O(sqrt n), coupling conditional occupancy with n throws in n boxes controls the L2 difference as O(sqrt n) versus scale n. The classical occupancy CLT plus Rayleigh cyclic-core distribution yields asymptotic independence. Independent literal enumeration of all maps n<=6 matches the conditional moments. Boundary k=n gives Z=0. Thus the mathematical statement is correct, but C does not establish novelty.

## originality

FAIL

Fails for the submitted final theorem in its original scope. The 2 November published theorem on the same uniform mapping and identical observables explicitly proves the same complete conditional distribution, the same factorial moments and strictly negative regression, plus a sharper exact covariance/correlation result. The joint independence limit is not stated verbatim there, but follows from that already known occupancy representation together with a standard occupancy CLT and an O(sqrt n)-window coupling; it is not a separate completed, clearly delineated final scientific claim/package here. A narrowed, distinctly motivated joint-limit theorem would require a complete scientific repair and fresh three-axis assessment; no such repair was staged.

## value

FAIL

Fails for the complete submitted claim because its central exact conditional law and negative regression are already published in a same-object theorem, and the unseparated remaining asymptotic limit is obtained by standard empty-box CLT and conditional coupling. It is mathematically sound, but correctness and reproducibility are not sufficient to assign an independent new value to the already known main finite census; a substantial carefully scoped repair was not supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
