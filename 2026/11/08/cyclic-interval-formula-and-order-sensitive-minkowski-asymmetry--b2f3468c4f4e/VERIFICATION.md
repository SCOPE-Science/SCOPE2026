---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The full-dimensional chainlink polytope is defined by coordinate and cyclic-difference halfspaces with 2ell<=min a_i and s>=3. Explicit feasible witnesses show coordinate support extrema 0,a_i and difference extremes -a_(i+1),a_i-ell. Reflection containment reduces exactly to 0<=u_i<=(lambda-1)a_i and u_i-u_(i+1)<=(lambda-1)a_i-lambda ell. The difference-constraint digraph has only cycles through a proper contiguous directed ring run and the full directed ring (plus nonnegative two-arcs), giving lambda=max(A/(A-s ell), A_(i,m)/(A_(i,m)-m ell)). All denominators are positive. Shortest-path potentials attain the sharp bound and describe all centers. Homogeneous specialization yields a genuine center segment. For ell=2 the (4,4,20,20) and (4,20,4,20) ratios are 4/3 and 6/5. Independent rational barrier LP and support inequalities were checked for 3/4 dimensions; finite checks are corroboration, not the all-parameter proof.

## originality

PASS

The first chainlink paper develops Ehrhart equivalence and sections, not the affine reflection asymmetry of its full polytope. Classical difference-constraint theory is used as an explicit proof tool. No equivalent all-center cyclic-interval theorem was found among the directly compared published results, while general Minkowski-center results apply to different polytope families; best-knowledge priority remains provisional.

## value

PASS

An exact Minkowski-asymmetry value and the entire optimizing center locus are natural affine invariants of chainlink polytopes; the order-sensitive contrast exhibits behavior not controlled by composition multiset. The cyclic-potential derivation and existence of nonunique center strata give a motivated, reusable geometric classification, rather than a renamed parameter formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
