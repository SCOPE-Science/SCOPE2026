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

Partitioning by the actual set of changed sites proves the local formula: separate nonadjacent choices multiply, and on an adjacent edge exactly q-d_i same-letter pairs must be subtracted. For the minimum put b=q-3 and let E count the interior distance-two matches. The lower comparison loses at most the number A of adjacent pairs of matches and the two boundary matches; the endpoint terms of the nonadjacent-pair sum cancel the latter. If E>0, E-A is the positive number of runs of matches. If E=0, attaining the minimum forces every four-letter window to use three letters, so its end letters coincide and the word is period three with three distinct starting colors. For the maximum the cost of each interior defect exceeds the possible adjacent-edge gain for q>=4; for q=3 the only potentially uncompensated defects are at sites 2 and n-1, whose mutual nonadjacent pair strictly loses because n>=5. The reference volumes simplify to b^2 binom(n,2)+(4n-3)b+n+5 and (b+1)^2 binom(n,2)+3b+4, and the first letters give the stated labelled multiplicities. An independent exact Hamming-cost transfer recurrence, /workspace/reproductions/frozen_diagnostics.py 2, checked 11,962 centres, including q=2 for the local formula. The frozen enumerator was inspected, not executed; the all-length claim rests on the proof.

## originality

PASS

Best of current knowledge: no demonstrated coverage of the center-specific radius-two correction together with both rigid extremal profiles for labelled proper paths. The novelty is not proper-coloring codes or substitution-distance packing in general.

## value

PASS

Radius two is the first substitution radius where adjacent changes interact, and its smallest ball is a natural packing input for distance-five codes. The sharp ternary linear-versus-quadratic distinction and the two different rigid periodic extremizers explain a real feature of the constrained geometry; the local formula applies to nonextremal centers as well. This is not an optimal code-size or biochemical claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
