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

Adjacent inequality gives signs ±1 mod 3, and abab is exactly an alternating sign triple, so only boundary sign-runs may be singletons. An interior insertion replaces s by −s,−s, the unique possible replacement. A new alternating triple must use one member of the identical pair on its boundary, with two old signs on one side. Its forbidden positions are the second position of a noninitial run and the penultimate position of a nonterminal run; they coincide only for an internal run of length three. A singleton boundary run transfers its one obstruction from an internal replacement to an end insertion. A single run has none. Two deletions can yield the same source from a destination only if the intervening segment is constant, impossible here. Thus among m+4 candidates the loss for r≥2 is 2r−2−t_3, and the degree is m+6−2r+t_3. The boundary weights z^L u^(L−1) and internal weights z^L u^(L−2+[L=3]), plus the one-run term, yield the rational series with six labels per composition. For r≥2 the excess d−4 is at most m−2. The cases of excess zero or one use all minimal internal lengths and either both minimal endpoints or exactly one incremented endpoint; they give the stated parity and multiplicities. Keeping internal lengths two realizes the parity of m through m−2; one internal length three realizes the opposite parity from 2 (m odd) or 3 (m even) through m−3. This includes empty ranges at the smallest lengths. One run alone attains m+4. Independent enumeration of valid destinations and inverse deletion (python /workspace/reproductions/insertion.py) matched every coefficient for 3≤n≤15. The all-length result follows from the run proof, not the cutoff.

## originality

PASS

The source language and its counting recurrence are known. Its length-preserving substitution graph is also studied in a distinct same-day finding. Neither covers this length-changing graph or its complete one-insertion degree spectrum. Fully square-free insertion extremality concerns a strictly smaller language and a different invariant. The supported distinct claim is the exact bivariate spectrum and its resulting support/extremizers.

## value

PASS

The complete local neighborhood distribution resolves a natural structural question for a word language used in tandem-duplication coding. The parity-sensitive minima, missing runner-up and exact extremizers go beyond total language or suffix counts. They can inform constrained insertion counting without implying any packing, covering or general edit-channel theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
