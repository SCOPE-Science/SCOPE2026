---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

PASS. Reconstructed the Pell strong-divisibility gcds gcd(P_n,P_(n+3))=P_gcd(n,3), gcd(P_n,P_(n+4))=P_gcd(n,4), gcd(P_(n+3),P_(n+4))=1, and exact recurrence identity 5P_(n+4)=P_n+12P_(n+3). For 3|n these give d=5 and remaining generator c=a/5+12b/5, the positive gluing condition. Small symmetric exceptions n=1,2,4 are one-/two-generated. For n≥5 with 3∤n, a=P_n≥29, c<3b and gcd(a,b)=1 exclude c in <a,b>, hence three minimal generators; odd n is pairwise-coprime and for even n the possible a,c gcd d=2 or 12 cannot represent b in <a/d,c/d> (the relation b=5(c/12)-(a/12) in the 4|n case gives a/12>5). The three-generator symmetric-semigroup criterion yields only the claimed indices. Independent exact Pell/gcd and Apéry genus/Frobenius symmetry checks n=1..9 reproduced the rule, but the universal result relies on the arithmetic proof.

## originality

PASS

PASS, bounded prior-art assessment. Komatsu–Mu's complete Pell p-Frobenius/p-genus study applies to triples (P_i(u),P_(i+2)(u),P_(i+k)(u)), so its first index gap is 2 and cannot be specialized to (i,i+3,i+4). Fel's full 2008 Fibonacci/Lucas source, including Theorem 5 and the foundational three-generator criterion, was checked; it treats recurrence coefficient 1, not the ordinary Pell sequence coefficient 2. A nearby published Pell result treats offsets (3,5), not (3,4), and its exception list differs. Generic gluing conditions provide a tool, not the explicit congruence/exception classification. No directly covering exact index theorem located; a more general recurrence classification unindexed remains possible.

## value

PASS

PASS. Symmetry/Gorenstein/complete-intersection are standard intrinsic semigroup properties, so giving an all-index if-and-only-if classification for a natural Pell-number triple family answers a substantive arithmetic-semigroup question. The sharp 3-divisibility mechanism and the isolated small exceptions require ruling out alternative pairwise-gcd gluings for an infinite family, beyond mechanical substitution or a short finite table. The result is distinct from the adjacent studied gap-two Pell family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
