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

The valuation of j+1 counts the trailing base-b digits equal to b−1, even when b is composite. This proves Delta_j=1−(b−1)nu_b(j+1) modulo m; in any two consecutive increments at least one is +1. For any triple with a reverse occurrence, the two increments therefore include both +1 and −1, distinct for m≥3, so the endpoints agree. Applying this to all internal triples of a reversible word forces period two. An even-length nonpalindromic such word has, in one of its two orientations, the consecutive increments (−1,+1,−1); impossible because any −1 transition has endpoint divisible by b if b≥3 and by 4 if b=2. Thus every class at n≥3 is singleton, not necessarily absent of palindromes. The permitted pair differences are the coset 1 modulo g; for each permitted d solve (b−1)h=1−d modulo m and choose digits of L with sum a−h(b−1) modulo m. At N=b^h(bL+1)−1 the two digit sums differ by 1−h(b−1) and the first has residue a. This realizes all pairs even for g=m. Negation preserves the coset exactly when g divides two. Counting fixed pairs (m for g=1, none for g=2) proves the three formulas. The classical binary prefix already contains 011 and 110. The frozen finite-prefix verifier was inspected without execution and is not needed for the universal proof.

## originality

FAIL

The earlier Resultary record f12270a0ea48 directly states the entire reflection profile in the frozen setting, including the same gcd correction, and proves strictly stronger reversible-factor cutoffs. The frozen note correctly distinguishes dihedral symmetry from ordinary reversal, but that distinction does not remove the explicit earlier plain-reversal coverage. The failure is demonstrated statement-level overlap, not uncertainty about historical authorship.

## value

FAIL

A uniform ordinary-reflection profile would answer a natural question, but it is already recorded in stronger form for exactly this family. The short-pair witness and elementary orbit count recertify the existing language data and do not isolate a new independently useful mathematical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
