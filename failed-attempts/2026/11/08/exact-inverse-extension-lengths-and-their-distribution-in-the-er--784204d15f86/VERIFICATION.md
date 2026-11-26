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

An inverse b copies bit 0 into bit n-1 and grows the set exactly when the least run start is 0. Before reaching 0 an inverse b is neutral or deletes n-1 while 0 is absent, so cannot create an earlier run start (and deletion to the empty set cannot lead to growth). An inverse a reduces a positive least run start by one. The first growing step therefore requires at least r prior rotations, and equality uses exactly those rotations and one merge, giving the unique forward word b a^r. For r=0, the fixed endpoint bits leave 2^(n-2) choices. For 1<=r<=n-2 the prefix through r-1 must be 1^j 0^(r-j), j<r, with bit r present; nonzero j forces bit n-1 present. The total is (r+1)2^(n-r-2). At r=n-1 the last bit is already forced, leaving exactly the displayed n-1 prefixes. An independent layered inverse-transition count confirms minimal lengths, multiplicity one, witnesses, histograms and stuck sets for all 8,164 nonempty proper subsets across n=3,...,12.

## originality

FAIL

Two distinct pre-existing catalogue results explicitly contain the unique shortest word, pointwise length law, full histogram and exceptional subsets. A shift of state labels by +1 mod n conjugates the frozen transition maps to theirs, identifies their ordered boundary index with the frozen r, and preserves every word and preimage count. This is verified coverage, not a priority inference from similar titles or unsuccessful literature search.

## value

FAIL

The statistic itself is well motivated by the known short-extension obstruction. But the exact law, shortest word, exceptional sets and the entire histogram are already available, including stronger refinements. Relabeling states and independently checking examples does not supply an additional scientifically useful unknown classification or lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
