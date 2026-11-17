---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

An equality graph connects each initial index i<k to all translated positions i+n_j; independent q-letter assignments constant on each of c components give probability q^{c−V}=q^{-tk+β}. Two translates give forests, hence pairwise independence. For three shifts, subtract n1, write gaps a,b and project overlap edges onto initial indices, lengths a,b; contracting a-residue chains and selecting b-edges yields c=max(gcd(a,b), a+b−k) for k>max(a,b), and β=0 below the sharp threshold. Thus β=max(0,k−a−b+g) and the centered third moment is q^{-3k}(q^β−1). Independent union-find checker covered 2704 gap/length triple cases and corresponding pair cases; finite tests do not prove all k/gaps, which rest on the explicit component proof.

## originality

PASS

Fine–Wilf word periodicity and Guibas–Odlyzko overlap graphs are known foundations. The exact simultaneous product-Bernoulli self-prefix three-time probability, pairwise-but-not-triple independence, and explicit third cumulant were not established by inspected period graph/recurrence texts. Guibas–Odlyzko 1981 original full text unavailable, leaving a concrete equivalence risk. Best-of-knowledge O, not a claim that gcd-threshold itself is novel.

## value

PASS

The first precise failure of joint independence among uniform symbolic self-returns is a natural finite-time correlation invariant and quantitatively determines an exact enhanced third cumulant, useful for recurrence statistics beyond pairwise mixing approximations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
