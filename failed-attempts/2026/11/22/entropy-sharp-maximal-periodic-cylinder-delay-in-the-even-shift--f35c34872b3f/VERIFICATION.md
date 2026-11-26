---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

A word with ones closes by appending zero or one zero as dictated by its exterior parity, while the all-zero cylinder contains a fixed point. For n even the single-one witness and for n odd the leading-two-ones witness are unbordered with odd exterior parity, ruling out periods below n by the border condition and period n by the wrap gap. The marker construction has length 2L+7 plus the total odd-part length, correct internal gaps and odd exterior parity. Borders of lengths 1–3 fail the explicit endpoints; lengths 4 through 2L+2 have prefix ending 00 and suffix ending 10; longer proper borders would recur the unique 110^(2L)1 marker. Gap parsing is injective. The odd-part composition generating function has a simple positive dominant pole and no other pole of the same modulus (part 1 enforces zero phase in equality in the triangle inequality). Fixing L gives the lower exponential bound at every sufficiently large n; the roots then tend to the golden-ratio root of the infinite odd-part sum. The two-state even-shift graph counts every word with a one exactly once, and counts the all-zero word twice, yielding F_(n+3)−1 for the matching upper bound. This proves a growth rate, not density by itself. Independent verification reconstructed indexed cylinders by closed labelled graph walks, treating the zero fixed point separately, and found Q_2 through Q_14 equal to 2,2,4,4,8,10,18,24,42,62,104,158,262; it also checked all 1,960 specified sampled marker words by direct border and parity tests.

## originality

FAIL

The distinct indexed modular-gap record fb6f7b997adb states its main theorem for m≥3, but its exact closing, shortest-border and density proofs (§§1–4) apply unchanged at m=2 and its verification explicitly includes m=2. This is demonstrable stronger coverage, not a title match or an inference of chronological priority. Its m=2 recurrence also reduces exactly to the enumerator in the distinct golden-mean record ce7ef1cd5963 after an index shift. The assigned record's explicit marker proof is a different proof of the weaker conclusion, not an additional new extremal law.

## value

FAIL

The worst-case closing statistic on this standard strictly sofic system is well motivated, and the explicit marker families give a valid alternate proof. As submitted, however, the exact maximum and the entropy exponent are weaker consequences of a checked covering argument that gives the full recurrence and positive density. The frozen finding does not establish a separate classification or substantively stronger conclusion specific to the marker method; the alternate proof alone is insufficient under the value criterion for a narrow covered invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
