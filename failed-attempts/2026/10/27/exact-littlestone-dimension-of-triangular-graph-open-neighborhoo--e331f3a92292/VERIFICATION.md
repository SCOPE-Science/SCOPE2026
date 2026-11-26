---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

These are open neighborhoods: query and center are unordered edges and equality gives label zero. After any first query ab the positive version space consists of a-spokes and b-spokes outside ab. The next query ab makes no split; a query disjoint from ab has only four positives; and a query ai or bi produces two star-plus-one classes. In a star-plus-one class, a query in the two centers gives a constant answer; most queries through the two centers leave at most two on one side; and a query through neither has at most three positives. A child of at most three hypotheses cannot have depth two. Thus the star-plus-one bound is two, the first positive version space has dimension at most three, and depth five is impossible. At n=2,3,4 the function counts are 1,3,3 (opposite edges duplicate functions at n=4), with informative queries when n>=3. At n=5,6 there are fewer than 16 hypotheses. The supplied n=5 proof tree has nonempty children through depth three; it embeds for n>=5. For n>=7 the negative branch of ab contains that tree on five outside labels, while querying ai on the positive branch leaves at least four same-center spokes on each side; a query on two of the spokes' endpoints splits 2–2 and a spoke query distinguishes each pair. This yields depth four. Independent version-space replay gave 0,1,1,3,3,4 at n=2..7 and checked 8 and 16 paths in the two witnesses. Replay and log: /workspace/branches/1a8ff292-054c-4d26-a2bd-42356b76104b/triangular_open_replay.py and triangular_open_replay.txt in the same directory. The supplied script, JSON witnesses and recorded output were inspected, not executed as code; the all-n result uses the structural proof, not the replay.

## originality

FAIL

Distinct indexed record df7df7b63727 explicitly states the identical four-case open-neighborhood Littlestone formula for every n>=2 and supplies a proof. It also notes restriction to induced subgraphs. This is demonstrable equivalent coverage in the checked catalogue, not a claim that it predates the frozen work. Its visible entry date is later and the lineage and priority of the two records are not established. The earlier static literature alone would not cover the adaptive theorem.

## value

FAIL

The underlying question is substantive: a fixed deterministic mistake cap for a growing natural concept class, with an adaptive-versus-static separation at n=5. But the exact adaptive dimensions, including both sharp thresholds and an essentially matching fiber upper bound, are already explicitly available in the distinct catalogued result. The frozen record provides no separate invariant, improvement or new consequence beyond that coverage. The failure is not based on small size or on the earlier static result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
