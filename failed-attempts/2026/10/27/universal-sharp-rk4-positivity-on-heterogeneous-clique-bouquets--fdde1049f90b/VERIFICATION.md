---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With m = n-1, the all-ones space, the direction (m,-1,...,-1), the zero-weighted-mean petal-constant subspace, and within-petal zero-sum spaces are orthogonal with eigenvalues 0, n, 1, and s_i+1. Their projectors give the stated entries. Write E=(1-r(nh))/n and B=(m+r(nh)-nr(h))/(mn). For h>0, strict convexity of r gives B>0. For distinct vertices in petal i, the entry is B+q_s with s=s_i and q_j=(r(h)-r((j+1)h))/j. Secant-slope monotonicity gives q_s>q_m when h>0 (since t>=2 implies s<m), and B+q_m=E. This directly verifies the strict distinct-leaf signs at the endpoint; independently the reflection identity follows by factoring its cubic difference at 0, rho/2 and rho and matching the cubic coefficient. Positivity of r for all real arguments gives positive diagonal entries via the spectral projectors. The increasing cubic factor of r(x)-1 shows r(x)<=1 exactly for 0<=x<=rho, so the hub-to-leaf entry alone rules out h<0 or h>rho/n. Convexity on [0,rho] and the attained eigenvalue n give the exact same interval for Euclidean norm <=1 (the last proof sentence in the source must retain the lower bound h>=0). At h=0 the map is I. The supplied verifier was inspected, not executed; the audit does not depend on its samples.

## originality

FAIL

A distinct indexed Resultary theorem demonstrably covers the entire frozen finding: it proves the same apex-positivity criterion on the same unweighted heterogeneous clique windmills for every nonnegative convex filter, explicitly includes order four, and its strict secant inequalities and eigenvalues imply the remaining endpoint and Euclidean-norm assertions. This is a finding about mathematical coverage of the standalone claim in the inspected corpus, not a determination of historical priority. The broader record has a later catalogue date; no claim is made that it predates the frozen result or that it was independently discovered.

## value

PASS

The phenomenon itself is worth identifying: a sharp safe timestep for positive diffusion on graphs with triangles and unequal cliques, with positivity and spectral stability coinciding and the first failure localized at a single entry class. It addresses a real distinction between norm stability and positivity. This scientific value does not make an already covered specialization a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
