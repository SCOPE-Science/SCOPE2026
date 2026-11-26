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

Independent replay /tmp/opencode/check_majority_independent.py built all transitions by bitboard swaps along the four XOR dimensions and strict majority of the five bitboards (self plus four neighbors); then tested the first t with X_(t+2)=X_t separately for each word, and distinguished p=1 by X_(t+1)=X_t. Exhaustion found every pinned word in the eleven cells (t=0..6, counts by p=1:425,5490,12713,5171,1224,198,24; by p=2:602,3187,3562,172,0,0,0). There are 425 fixed points and 602/2=301 two-cycle orbits, with no others. All 24 words first entering at t=6 land at word 1: the wording 'attainable at time six' is read in its first-entry census context, not as a claim about the image of P^6. The witness 35537->35025->32977->209->81->17->1 certifies P^7 != P^5 and exhaustion gives P^8=P^6. All-one and word-1 basins have sizes 9383 and 3696. Unpinned replay gave max t=4 both for all 65536 starts and for the same 32768 odd starts, which have all-one basin 8229. The matched sets have difference 1154 and reverse difference zero. The order-preservation proof compares both iterates starting at the same x, because clamping dominates an ordinary update and the ordinary map is increasing. No inference about eventual fixedness of two-cycle starts or time to consensus.

## originality

PASS

The credited unpinned four-cube census and general majority theory cover the baseline, not the specific pinned transient, two basin sizes, or exact matched gain. Different pin graphs and stochastic stubborn-agent models are meaningful context but do not specify the pinned Q4 map used here. The evidence supports the distinct paired gain-and-delay result without a global priority claim.

## value

PASS

Single-vertex permanent forcing and the canonical even-degree cube make a specific natural intervention/relaxation test. On the same starts this intervention increases the all-one basin by exactly 1154 without loss yet lengthens the worst first-periodic-entry time from four to six, while a highly polarized equilibrium still attracts 3696. It is a sharp finite witness that monotone improvement of consensus attraction does not imply faster worst relaxation, with a full reusable entry-period census; not an empirical social claim or an all-dimensional result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
