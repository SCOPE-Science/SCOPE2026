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

The unit cuts generate input increments modulo constants with l1 coefficient norm equal to input variation. On a strict order chamber each cut gives entries in {−1,0,1} supported on at most three consecutive windows. For output lengths 1,2,3,4,≥5 this bounds variation by 0,2,4,5,6 respectively. Integrating the chamber bounds gives the global estimate; a common generic perturbation of the two endpoints handles a segment lying in a tie hyperplane by continuity without changing their difference. The displayed rank-preserving perturbations attain the bounds and extending the baseline from length eight adds no straddling windows. For one input the layer-cake integral over binary exact-two windows and the discrete coarea identity reduce the estimate to the 16-state binary potential, whose 32 transition inequalities telescope against the input jumps. The length-five replacement has slopes 0,−1,1,0 between the fixed samples and gives bound 1; length four gives zero. Binary step witnesses attain the reported nonzero constants. Independent exact replay /workspace/branches/963c0367-66b4-4b22-8f89-2bf105ae50bb/independent_replay.py (replay.log in the same directory) checked the potential and transitions, all strict rank orders and cuts for n=4,…,8, and the finite and extending witnesses; enumeration is supplementary to the all-length proof.

## originality

PASS

The supported distinct claim is the pair of sharp attained coefficient sequences for the open, unpadded four-site middle gap. The strongest available neighboring claims concern single-rank filters or different robust-scale maps. They do not state or imply this pair of sequences.

## value

PASS

A local robust spread statistic can have small ordinary output variation while substantially amplifying the variation of differences of nearby inputs. The exact separation 2 versus 6 and the first lengths at which amplification is possible and maximal are useful for stability and finite-window analyses; they cannot be read off from monotonicity of a single rank statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
