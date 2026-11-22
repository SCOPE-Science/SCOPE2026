---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS. Read RESULT.md proof and check_catalan_distance.py. The exposed face C_n is product of n-1 binary pair segments with endpoints fixed; distance squared to it is the stated separable quadratic. At a balanced binary vertex the pair counts force the bound floor((n+3)/2) and restricted equality patterns. An inversion of middle pair residuals admits a Dyck path with positive normal displacement, so only sorted 00 / optional mixed / 11 patterns project to P. Discrete summation by parts against all ballot-prefix slacks proves the normal-cone condition for the one odd-n vertex or two even-n vertices. The even-n edge shares a constant residual, so entire edge, and only it, attains gap. Independent constrained quadratic optimizations checked all 6,20,70 hypersimplex vertices for n=2,3,4 and exactly 2,1,2 deepest vertices; no extrapolation from finite n.

## originality

PASS

Dyck-base polytope outer Hausdorff and parity farthest locus are independent of earlier intrinsic inball work.

## value

PASS

PASS. The Catalan matroid is a canonical lattice-path matroid; measuring its maximal Euclidean deviation from the enclosing hypersimplex is a natural robust-projection invariant. The exact squared gap and odd-versus-even entire farthest locus (one point or a nontrivial edge), together with explicit nearest points, are a complete nontrivial classification that future metric-matroid work could use. The standard exposed-face and convexity tools alone do not make the result a textbook exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
