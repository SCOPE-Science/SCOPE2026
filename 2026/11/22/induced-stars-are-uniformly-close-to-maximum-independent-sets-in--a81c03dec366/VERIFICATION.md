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

For a common atomless law the probability integral transform gives distinct iid uniforms and preserves their ranks almost surely even if the CDF has flat intervals. For 1≤k≤n the two ends of [t,1−t], t=√(k/(8n)), define disjoint endpoint-tail regions. A hub spans the central segment with probability 2t²=k/(4n), so the no-hub probability is at most e^(−k/4). An interval not meeting any chosen hub must be counted among the Y intervals wholly in one tail, with Y binomial of mean k/4. From a maximum independent family remove those members and the hub itself if present, since its neighborhood is open. Thus D_n≤Y+1 on the hub event. The event D_n>k+1 there is contained in Y≥k, whose probability is at most (e/4)^k by selecting k sampled intervals; independence of Y and the hub event is not used. The k>n case is trivial, and the geometric tail sums give the claimed exponential moments for 0<λ<1/4. For every fixed r, each of r disjoint equal-length bins contains a whole sampled interval except on an event of probability at most r(1−r^(−2))^n; endpoint ties have probability zero. Hence α_n diverges in probability and tight D_n gives the ratio limit. The supplied verify.py and its 146598-pairing evidence were inspected, not rerun. The analytic proof, not that bounded diagnostic, establishes the result for all n and k.

## originality

PASS

The supported new comparison is the uniform exponential additive gap between the independent kissing number and independence number in the iid-endpoint model. The invariant itself, the universal-vertex event, and results about the global independence number are prior. No inspected statement supplies the uniform additive control; historical coverage is qualified below.

## value

PASS

Local independent packing around one sampled interval captures global packing up to an exponentially tight additive loss. This is stronger than relative convergence and rules out the arbitrarily large gaps possible even for deterministic interval graphs. It quantifies the quality of a single sampled hub outside the classical universal-vertex event and for every graph size. The constants are not claimed optimal, and no limiting gap distribution is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
