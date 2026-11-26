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

In the stated left-to-right binary automaton, the preimage of a nonempty proper cyclic interval is another such interval, empty, or full. A b-preimage increases size precisely at start 0 and changes the start to n−1; losses and harmless b-steps cannot advance a successful path toward start 0. A reset to t with h losses and r harmless b-steps therefore uses at least L+t+(n+1)h+r letters, and any inter-gain a-run has length n−1 modulo n. At L this forces the unique word U_n. At L+1 no losses are possible, and the sole slack is an endpoint a or a harmless b. In the inverse gap after gain r, the sole loss is at phase r, and reversing the gap gives the forbidden forward position j=i. Adjacent doubled b's admit either order of identifying the extra copy; there are n−1 distinct such words including U_nb. The disjoint classification yields (n−2)^2+3. A fresh inverse-image bitset DP, n=3..30, checked the L and L+1 counts by targets 0, 1 and n−1 (the proof rules out all targets >1 at L+1). The DP is corroboration, not proof. Replay: python -B /workspace/branches/frozen_recheck.py 5.

## originality

FAIL

The earlier October 13 Resultary record states and proves the same exact coefficient and classifies exactly the same words for a domain that contains the frozen domain. It uses a different proof, via a mandatory subsequence and forward interval images; this does not make the frozen claim distinct.

## value

FAIL

The count is a useful local invariant of a natural reset language, and the inverse viewpoint is an elegant alternate derivation. But the submitted contribution is the exact invariant and full word list, both already available in the earlier record. The alternative proof does not establish a separately claimed extension or application; publication as a new exact invariant is not warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
