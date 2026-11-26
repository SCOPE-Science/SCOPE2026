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

A BV and L² input has zero trace at −∞ and equals the superposition of steps against Df. The step itself need not be in L²: apply the local moment equations on each cell, where it is bounded. Fubini on compact test supports and the uniform single-step variation bound give TV(Pi_2 f) ≤ sup F · |Df|(R), including grid-node steps of gain one. Local projection preserves constants, and the shifted Legendre step integrals give the stated p_s. The affine reference-cell variation is |p_s(0)| + integral |p_s'| + |1−p_s(1)|, independent of cell length. On 0<s<2/5 the concave quadratic has an interior turning point; the signed trace terms switch at alpha=(4−√6)/10 and beta=(6−√6)/10. On [2/5,1/2] it is nondecreasing. These facts give exactly the four stated branches. For branch 1 and 3, writing z=1−2s gives F=1+(3/20)(1−z²)(5z−1)²/z and F=−1+(3/20)(1−z²)(5z+1)²/z, respectively; differentiation gives the increasing branches on their specified s-intervals. They and the last branch do not exceed 2. The central derivative has the sign of 500[s(1−s)]²−216s(1−s)+23, and only its smaller root in s(1−s), (54−√41)/250, is attained on that branch. The derivative changes from positive to negative; F(1/4)=331/160>2 and reflection give exactly the two optimal single-jump fractions. Independent symbolic checking gives K_2=2.0698386217193242… . A compact interval with matched jumps in two nonadjacent cells attains twice this gain for input TV=2. Even matched adjacent endpoints at s_* work: p_s(0)<0 and 1−p_s(1)>0, so their two signed interface contributions add rather than cancel. Arbitrary mixed matched/reflected fractions need not attain if their cells are adjacent; that is not a frozen claim about all extremizers.

## originality

PASS

The supported distinct claim is the exact sharp seminorm and its two single-jump maximizing locations for a broken quadratic L² projection with all interface jumps. Indexed global quadratic norms and the broken affine norm overlap substantially in local projection or proof method, but do not compute this extremum. Classical BV stability of projection is an important prior question, not itself the claimed novelty. The best-of-knowledge comparison is limited by lack of Cockburn full text.

## value

PASS

The seminorm is a natural worst-case stability measure for a standard discontinuous reconstruction, and ignoring interelement jumps would underestimate it. The exact grid-independent bound is attained even on arbitrarily graded grids, and the worst single-step location is not the grid midpoint. A sharp estimate and explicit interval attainers give meaningful information beyond generic BV boundedness or finite numerical observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
