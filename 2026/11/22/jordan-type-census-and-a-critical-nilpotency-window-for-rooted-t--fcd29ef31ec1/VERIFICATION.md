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

In the canonical incidence representation, a cover-supported power has the product along a unique path at each possible entry, with no cancellation. For fixed k, rows from one depth have disjoint descendant supports; rows from different depths end at different depths. Thus rank X^k counts vertices whose longest open descent is at least k, and second rank differences give the exact Jordan multiplicities through size h+1. In the polynomial recursion, at cutoff j each child independently contributes its unrestricted assignment with a closed edge, or its root-length-at-most-j-1 assignments with one of q-1 nonzero connecting weights. The difference of consecutive cumulative polynomials therefore counts the exact root length with nonnegative coefficients, including j=0; marking the root and starting with the single leaf proves the full census and coefficient sum q^E. For the maximal index, root survival is the stated branching recurrence; strict concavity and bt>1 give the unique positive fixed point and iteration from 1, with the binary formula by solving the quadratic. At (2,2) the reciprocal increments tend to 1/4, proving p_a~4/a. The global deficit is h-max_v L(v): for a descent of length h-k only depths through k are possible, giving the union bound, while the b^k disjoint depth-k subtrees give independent opportunities. At k=floor(log_2 h)-L and +L these bounds give opposite tail estimates of order 2^(-L) and exp(-c 2^L) for sufficiently large h at fixed L; a positive survival lower bound yields uncentered tightness in the other fixed regimes. This is tightness, not convergence to a critical lattice law. In the whole radical a strict chain of h steps must increase depth by one at each step from the root, so all noncover coefficients are free for the top-power count only; R=sum d b^d counts strict ancestors. Inspected frozen programs and recorded outputs; the separate bounded `python3 -B /workspace/review_evidence/small_field_checks.py` computed actual matrix powers and ranks for all 4096 F4 binary-height-two edge assignments and matched the five exact rank pairs. This does not stand in for the all-parameter proof.

## originality

PASS

The supported distinction is the full finite-field Jordan census of the cover-supported tree operators and its link to the deficit from the longest open descent starting anywhere. Classical root survival and the branching threshold are prior, as are Jordan enumeration in other incidence or triangular families. The inspected broader statements neither specialize to the given support restriction nor identify the all-starting-vertices deficit.

## value

PASS

All-power Jordan type is a natural invariant of this canonical family of sparse radical elements; the exact positive recursion avoids rank enumeration over field labels and provides the joint profile law rather than just top connectivity. The logarithmic critical deficit versus bounded supercritical deficit locates a difference in typical largest blocks not captured by the root percolation threshold alone. The whole-radical lifting is useful within its explicitly limited maximal-index scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
