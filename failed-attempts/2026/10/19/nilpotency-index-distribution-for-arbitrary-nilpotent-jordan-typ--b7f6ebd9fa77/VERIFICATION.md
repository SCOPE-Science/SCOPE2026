---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Square-zero expansion over the stated dual ring is valid in every characteristic and reduces powers at m>=k to the kernel of T_m. Conjugating A reduces to independent ordered rectangular blocks. For sizes a,b, identify matrix units with u^{a-i}v^{j-1} in K[u,v]/(u^a,v^b). The operator multiplies by h_{m-1}; for d>=m-1 both u h_d and v h_d equal h_{d+1}, since u^{d+1}=v^{d+1}=0. Its image has exactly one nonzero generator in each grade m-1 through a+b-2 (each a sum of distinct monomials with coefficient one), and no others. This yields max(0,a+b-m) in every field. Rank-nullity gives the cumulative formula, differences give the point law, and reduction precludes indices below k. At 2k all terms vanish; at 2k-1 precisely the s^2 ordered pairs of largest blocks contribute. This includes k=1, where only B=0 gives index one. Independent bounded replay: python3 /workspace/reproduction.py 3 exhausts six dual-ring lift cases over F_2, F_3 and F_4 (including (2,2) over F_2, with bins 256,3840,61440), and computes ranks by literal dual powers on matrix units for (3,2) and (4,2,1) over F_2 (respectively 8,4,1,0 and 10,5,2,1,0). Bounded tests corroborate the proof and do not address higher-order coefficient rings.

## originality

FAIL

The arbitrary-partition count is mathematically correct, but it is mechanically implied by the explicit rectangular operator evaluation in Prasad–Singla–Spallone, arXiv:1212.6157v2, §6.2, pp. 20–21. This is stronger evidence than prior knowledge of the linearized-power operator itself: the authors give its action on matrix units and the resulting coordinate vector on the first column for arbitrary rectangular sizes and exponent. In the claimed range, the first column determines the whole output. The closed count need not have been printed in that source to be covered. Earlier Resultary records also state the one-block distribution and the arbitrary-block top mass explicitly. The originality failure does not rest on inaccessible literature or on later overlapping records.

## value

FAIL

The fixed-residue distribution is a natural invariant, and the formula is convenient. But its exact value is already obtained by reading off the first-column image from the prior all-rectangular matrix-unit computation, followed by rank-nullity. The top probability is explicitly covered by an earlier record, and the alternative proof is a reformulation of the same computation with no independent further finding. No distinct valuable remainder of the stated theorem survives that coverage, so no repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
