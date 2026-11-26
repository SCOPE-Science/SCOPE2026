---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Let s=x+y. On the (f,g) step, (s',x')=(2+f-g-s,2s-x-f); the four lower and four upper x-bounds follow from y∈[0,1/2], x'∈[1/2,1], y'∈[0,1], and x∈[0,1]. Pulling the intervals back for all 16 pairs and integrating their linear envelopes gives precisely AB, BA, AD, CA, each of area 1/48. The two recurrent words are repetitions of AB or BA; their two-step translation is -4δ about s=3/4 or 5/4. Intersecting translates of the respective two-letter interval takes the extreme shift in each bound and gives width 1/4-(4m-1)|δ| on |δ|≤1/[4(4m-1)]. The terminal AD constraint at ε=3/4-s intersects the initial AB interval with the last AD interval shifted by -4(m-1)ε. The initial CA constraint, in the ensuing A coordinates with Jacobian one, intersects the interval of the first CA step with the terminal A upper bound shifted by -4(m-1)ε. Both yield width min(2ε,1/4-(4m-3)ε) on 0≤ε≤1/[4(4m-3)]. These give recurrent areas 1/[16(4m-1)] and transient areas 1/[16(4m-1)(4m-3)] each. Summation and nested-set squeezing prove the frozen even formula and all-time normalizing constant. The frozen verification notes overstate the supplied main program: it checks 240 named word areas, including the four positive pairs at m=1, but does not enumerate all 16 pairs. That supplementary evidence error does not affect the independent full transition check or the symbolic proof.

## originality

FAIL

The exact even law and tail are covered by the distinct indexed result fa18f62401f4, which also gives the odd law and first-exit consequences. Its named branch and the frozen branch are area-preservingly conjugate by a symmetry of this same map, so the overlap is exact, not just equality of exponents. The later catalogue date does not establish publication priority. The 2023 paper is independently close because it analyzes escape-cell geometry, but its base-return and correlation estimates are not themselves the frozen observable. No separate distinct surviving contribution is shown.

## value

FAIL

The precise residence tail of a neutral branch is a motivated statistic that would be useful independently of a correlation theorem. Here it is already available with stronger temporal information for the symmetry-related branch. Repeating its even tail for P by a map symmetry changes no invariant and leaves no independently useful exact fact or new mechanism in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
