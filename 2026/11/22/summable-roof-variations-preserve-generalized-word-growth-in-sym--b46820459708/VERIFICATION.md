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

Summable centered variations imply continuity, so positivity on the compact subshift gives 0<m<=r<=M. For a match on [-K,N+K], shift j has centered agreement radius at least K+min(j,N-j); each radius appears at most twice. Thus every partial return sum differs by at most twice the variation tail, independently of N. Quantizing starting height and choosing one sequence per padded word gives a fixed number of points per word. To check seam times, at a common physical time express both trajectories as short flows from their respective jth section points, taking j from the first trajectory; the second flow time may cross its seam and differs from the first by at most the initial height error plus the uniform drift. Both lie in a fixed bounded flow-time range. The matching symbolic neighborhoods and uniform continuity then give the Bowen spanning bound. Conversely a uniform section box separates symbol cylinders. Continuous-time closeness pairs crossings in either direction uniquely within a fixed distance less than m/8; the pairs are ordered and none can be skipped before the end margin. Since each interval lasts at most M, section points representing distinct words of length floor(c n) cannot stay close. Uniform continuity on one sampling interval transfers this to discrete separation. For negative t, f^(n-1) is an isometry from the forward n-Bowen metric for f to the inverse n-Bowen metric for f^(-1), so exact separated and spanning numbers agree. Fixed padding costs at most a constant |A|^B; monotonicity and iterated doubling compare both linear rescalings to p(n). These are analytic checks, with no finite experiment required. The equality is not inferred for arbitrary continuous roofs or without bounded doubling.

## originality

PASS

Credit the constant-roof formula, the materially overlapping same-day finite-window result, ordinary flow-box geometry, and bounded-doubling rescaling. The supported distinction is the uniform spanning comparison under summable centered variations, allowing infinite memory and giving the complete growth order under bounded doubling. Available statement evidence does not establish wider prior coverage. This is not a priority verdict for the related finite-window result or a resolution for arbitrary continuous roofs.

## value

PASS

The proof supplies a length-independent drift bound on orbit segments, where uniformly approximating an infinite-memory roof by a finite-window roof alone would not suffice. It resolves the growth-class question on a natural regularity family while also giving quantitative word bounds without doubling, not merely the usual exponential entropy comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
