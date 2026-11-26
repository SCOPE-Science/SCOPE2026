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

For markers i<j, their left and right admissible incidences give X,Y and the pair spacing bit h; subtract the possible 11 pair once from each of the mixed counts, giving (T−X−Y+h,X−h,Y−h,h). This is invertible to the signature (X+Y−2t,h,X), where t=n−2s+1. In the middle zone, exact separation e gives coordinate sums e,e+2,…,2t−e. For s≥3 these yield 2t−1 short-pair sums (from e=1,2) and 2t−2s+1 long-pair sums (from e=s,s+1, or just e=s if t=s). At fixed positive excess δ≤s−1, the left–middle, left–right and middle–right ranges are disjoint and fill [0,2t+δ]. The spacing bit may vary within a range, but each X specifies one primary pair; the same-side repetitions at the extremes agree in h=0 because at the extremes the primary pair's gap is δ<s. For δ≥s, left–right contributes s(s−1)/2 profiles in all and the two same-side extremes add 2(s−2); the latter are possible precisely for s≤δ≤2s−3 (choose one excess s−1 and the other δ−s+1). This gives (2s+2)t+s²−5. At t=s−1 the positive excess arguments still apply and the zero-excess slice has no long pairs, replacing the formal count −1 by zero. For s=2, t≥2, the zero slice has t odd short sums plus 2t−3 long sums; the positive slices give 2t+2 and 1. At t=1 there is one short and no long zero-excess profile and the positive slices are unchanged, giving six. A maximum code has one representative per deck. A separate literal four-count enumeration for 2≤s≤10 and s≤n≤3s+4 covered 153 parameter pairs and 21,549 marker pairs. It agreed where the theorem or boundary asserts a value, e.g. C₃(8)=28 and C₃(7)=21. Replay: python3 /workspace/branches/e7113c82-bf6e-498f-ba38-8e41a101654e/direct_pair_check.py 10 4; direct_pair_check_extended.log in the same directory. This check is finite, and the frozen verifier was inspected, not executed.

## originality

FAIL

A distinct indexed record proves the identical all-spacing capacity and the identical sharp one-unit boundary excess, by a layer count for the same deck. It additionally observes singleton counts but these are fixed by (n,weight two) and create no splits. Its catalog date is later; the finding is of exact existing content coverage, not earlier priority or provenance. Primary references on collision thresholds, binomial equivalences and ungapped deck enumeration are related but are not the reason for the failure.

## value

FAIL

The exact linear capacity and its sharp onset are meaningful for deterministic sparse-word coding; a slope alone would miss an observable boundary effect. But both exact statements and a corresponding profile count are already available for this same fixed-weight channel. Dropping redundant singleton fields or rearranging the slice count supplies no independently needed exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
