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

For a distinguished chord, isolation requires even open-arc sizes 2r and 2s, s=n-1-r, and separate uniform matchings. Its event has probability w and reduces the crossing mean by (n-1+rs)/3. Summing the indicators by rotational symmetry (two endpoints per chord) contributes a factor n. The terms r=0,n-1 are precisely simple chords and removing them gives Z, including the empty sum at n=2. The two r=1 or s=1 terms for n>=4 have total covariance -2n/[3(2n-1)]; the ratio (2r+1)/(2s-1) gives geometric decay from r=2 to floor((n-1)/4) and a negligible middle after polynomial weighting. Hence the asserted sparse-isolate mean, limiting covariance contribution, and total constant follow. Independent bitmask enumeration reproduced the exact Z mean and three covariances on all 146598 matchings at n=2..7 (python3 /workspace/branches/reproduce_reviews.py 4). This is bounded, not the proof of the general law.

## originality

FAIL

An earlier distinct Resultary statement on the same random matching model explicitly contains the exact total- and simple-isolate covariances, the signs, and both constant-order asymptotics. The exact nonsimple covariance and mean differ only by removing the two simple-chord terms; no distinct remainder was identified.

## value

PASS

The covariance of a vanishingly rare part of a statistic need not vanish. The exact split and the nonzero correction quantify this for a natural random diagram model; this is mathematical value of the law, not value as a new contribution in the present record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
