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

Every absent root edge uv has d(u)+d(v) distinct active neighbours, giving the synchronous update and the four-seed lower bound. A moving four-seed set must be covered by two nonadjacent root vertices. The degree pairs (4,0), (3,1) and (2,2) exhaust this case. The full star, the full star with one leaf-edge, and K4 plus isolates are closed upper envelopes for the losing types. In the (2,2) case zero, one and two common neighbours give two P3s, P5 and C4, respectively. The explicit trajectories of the two winners give 4,5,7,2n,C(n,2) and 4,5,9,2n+3,C(n,2), with exactly the claimed early coincidences. Reversal of a labeled path, and block exchange plus independent center choices for two P3s, give the two counts. For P5, removing a terminal or interior edge gives respectively one or three alternatives inside its five labels, and for each extra label gives respectively two P5 or two paired-P3 alternatives per removed edge. For two P3s the remainder is P3+P2, permitting four path joins, one alternative using the old detached vertex, and two joins per fresh vertex per removed edge. This proves both degrees and double-counting gives the exchange edge count. Prefix reversals connect paths on a support, replacing a terminal label connects the supports, and joining P3 to P2 connects every paired type to a path. Independently, `python3 /workspace/reviews/check_4.py 5 6` exhausts seeds through size four on the explicit host, identifying root components and checking exchange connectivity. It reproduced 60 paths at n=5 (time 3, degree 8), and 360 paths plus 90 pairs at n=6 (times 4 and 3, degrees 16 and 20). The two frozen programs were inspected, not executed; the bounded replay supplements the all-n argument.

## originality

PASS

The numerical minimum four is expressly credited rather than original. The supported increment is the complete starter classification, labeled counts, parallel-time profile and the exchange graph of these starters. Same-host comparisons with different dynamics do not supply these results. The strongest same-rule journal source remains a specific full-text access risk; no inference of noncoverage is made from the missing text.

## value

PASS

A minimum size alone neither characterizes viable four-seed configurations nor distinguishes their parallel dynamics or whether all optimal choices can be traversed by replacements. The two forest types and their exact times and different exchange degrees resolve those questions for every host order by a uniform structural argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
