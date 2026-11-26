---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Direct coordinate sets give degree six and two common neighbors for every pair of distinct vertices (hence the same strongly regular spectrum). After the first accepted vertex there are nine free vertices, and after any nonadjacent second vertex four. Sorting their induced degrees gives nine cycles on the rook graph and on Shrikhande three cycles (the three specified second choices) and six diamonds. Only the latter can stop at three, and do so half the time. Each permissible ordered triple of early acceptances has probability 1/(16·9·4); a terminal triple has six orders and a terminal quadruple 24, because in the latter case the fourth vertex is the sole free vertex after the third. This gives the claimed labeled probabilities, counts and means. Independently of the packaged subset DP, exponential memorylessness gives independent stages with rates 16, 9 and 4 up to the third acceptance, and with rate 1 when a fourth is possible. Each free vertex is unattempted, and the waiting time for its minimum clock is independent of which free vertex is selected. Thus the mean gap is one third the CDF of the sum of independent exponentials of rates 16,9,4,1. With q=exp(−t), partial fractions give (1−8q/5+4q⁴/5−8q⁹/35+q¹⁶/35)/3. Expanding q^j using (p+q)^(16−j)=1 exactly reconstructed all 17 coefficients and both boundaries, including zero at t=0, the first term 8p⁴ and limiting gap 1/3. The replay command is python /workspace/branches/rook_shrikhande_clock_check.py /workspace/source/2026/11/08/strict-kinetic-separation-of-two-cospectral-graphs-under-hard-co--0f9e5993c6ec/KINETICS_COEFFICIENTS.csv; the separately written checker also confirms the residual classifications. Packaged scripts were inspected, not executed.

## originality

PASS

Both the static graph distinction and the random-order greedy algorithm are established. The supported distinct claims are the evaluated labeled terminal law and strict positive-time expected coverage gap for this particular strongly regular pair. No earlier evaluated equivalent appeared in the compared material; the inaccessible foundational paper remains a priority caveat.

## value

PASS

The rook and Shrikhande graphs are a canonical, not arbitrary, equal-parameter nonisomorphic pair. Their full labeled terminal laws and strict positive-time mean separation provide a concrete test of what a natural exclusion process detects beyond spectral parameters. The fourth-order onset specifies exactly when low-attempt expansions first distinguish the graphs; the result is more than a comparison of maximum independent-set counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
