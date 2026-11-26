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

The source counts distinct outputs for distinct length-n linear words, not deletion locations. Type A requires opposite alternating phases on the differing interval; length ≥3 forces 010 in one endpoint. The two triples crossing either side of the surviving swap give the stated context tests. The oriented 01 endpoint determines the edge uniquely; each context has OGF U=(1−z)/(1−2z+z²−z³), from 1+z+z² A(z), where A counts 010-avoiders. Padding makes every permitted context two adjacent ones before and after the pair, and a matched pair must lie inside the original word. Beyond inspecting the eleven-state polynomial certificate, I independently checked the all-length isolate series via runs. In the padded word containing a zero, the 1-runs all have length ≥2; a singleton zero is allowed only between two runs of length exactly 2. Classify 1-runs as length 2 or length ≥3, set b=z/(1−z), a=z²/(1−z), v=(1,b)^T, D=z² diag(v), and R=[[b,a],[a,a]]. With boundary pads subtracted the series is (1−z)^−1 + v^T R(I−DR)^−1 v, which reduces to the claimed numerator and denominator. A swap changes the inversion parity; the matching consequence follows from König's theorem. Independent distinct-output enumeration at n=0–12 matched the neighbors and both reported sequences; replay /workspace/branches/06ec2142-f343-4801-bdd5-192a9e7ae3f2/reproduce_counts.py. That run corroborates finite values only.

## originality

PASS

The Type-A test and its adjacent-swap restriction here are prior structure and an immediate specialization, respectively. The supported distinct contribution is the exact induced-graph edge and isolate census, especially the padded local isolation criterion and its complete rational series. No inspected separate result covers those counts.

## value

PASS

For a natural memory-two constrained source, edges measure precisely which source pairs are ambiguous from two distinct reads, and isolates can be included in every maximum independent code without consuming a conflict. A complete boundary-aware isolate criterion and exact isolate and edge series answer those motivated questions uniformly in length. The result does not claim the optimal code-size formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
