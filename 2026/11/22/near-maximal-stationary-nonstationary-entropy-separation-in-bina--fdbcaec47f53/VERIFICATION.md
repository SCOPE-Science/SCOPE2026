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

Disintegrating the one-step output over its tail gives conditional first-symbol probabilities J(0x), J(1x), with the input as the tail law. Thus its entropy equals H(p)+(log 2−H(p))μ(W_q). The equal mixture of 01^∞ and 10^∞ is fair and supported on W_q. A second marker at a positive distance less than q would have its initial symbol and first tail symbol inside the constant tail of the first, impossible. At distance q its initial symbol is the final symbol of the first marker, forcing opposite type. Every length-q starting window therefore contains at most one marker, yielding mass at most 1/q by invariance. Equality makes all translated windows contain exactly one start in the two-sided stationary extension, almost surely (countably many windows); hence starts are one residue class mod q and marker types alternate. The windows determined by these markers cover the line, so the only allowed orbit is the alternating runs of length q. Uniform measure there is fair and uniquely invariant on that orbit. Since 0<p<1/2 the objective is strictly increasing in marker mass, proving uniqueness as stated. For every positive continuous normalized J, compactness bounds both branch probabilities below by a common positive δ, so the stationary fair supremum is at least H(δ)>0 (fair invariant inputs exist) and no gap can equal log 2. For p=e^{−(q+1)}, H(p)=O(qe^{−q}), proving the stated asymptotic and sharpness. The bounded independent replay `python3 -B /workspace/review-evidence/marker_overlap.py` checks every two-marker overlap length for 2≤q≤100, finding only the opposite-type one-symbol overlap; this is corroborative, not the proof over all stationary inputs.

## originality

PASS

The conditional entropy identity and broad optimization distinction are prior. The inspected statements do not establish this exact fair-input family or the unique alternating-run optimizer and sharp nonattained output-entropy gap. The closest overlapping occupancy theorem excludes the one-symbol overlaps essential to the equality case.

## value

PASS

The exact example separates two natural optimization domains while imposing the same fair input marginal. The stationary optimum can vanish asymptotically although the unrestricted optimum is the full bit, and strictly positive continuous channels cannot attain the limiting gap. Identifying a unique stationary process at every finite q gives an exact witness rather than just a numerical separation or a restatement of the entropy identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
