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

Target squaring translates supports by one because each square is one distinct basis vector and a field has no nonzero element of square zero. Orthogonality is exactly support disjointness. A nonzero first image has support S stable under addition by n and therefore by g=gcd(m,n). If g<n its g-shift coincides with it, contradicting orthogonality. When n divides m it consists of just one residue class since the n consecutive shifts are disjoint. Coefficient recurrence around this class raises c by 2^m and so closes exactly for c^(2^m−1)=1; conversely the displayed supports and coefficients satisfy all relations and give independent image vectors. This holds in characteristic two and does not need Frobenius surjectivity. Distinct embeddings with the same image differ by exactly one source automorphism, giving the quotient; equivalently for a fixed residue the first support line agrees exactly when c'/c is fixed by the 2^n power (strict case, compare the first two coordinates in that support). Rotations move among residues and the diagonal automorphisms scale the distinguished coefficient by d^(2^r); this power is a permutation on the odd-order roots, proving transitivity. The cyclic multiplicative group gives the finite-field gcds (e.g. 30 embeddings and five images for n=2, m=4, q=16). Cases n=1, n=m, and n∤m are included without a unit condition. No flaw in the mathematical statement was found. The supplied finite checks were inspected but not executed and do not prove the arbitrary-field classification. The cited Cadavid et al. theorem number in the retrieved v1 is 2.3, not 2.4; this does not affect correctness.

## originality

FAIL

The principal claimed strict-divisor classification and full map parameterization are already covered by the single-target-cycle statement of a distinct indexed result for permutation evolution algebras. That theorem is stated over finite fields, but its support and coefficient-closure argument is literally field-independent until the final gcd conversion. The arbitrary-field formula is therefore a direct consequence of the same statement-level proof, not a separate new classification. Image counting and transitivity are not printed in the inspected competing finding; they follow by taking the standard quotient by source automorphisms and acting on its single-residue parameters by the known rotations and diagonal roots. No relative priority is inferred from the equal dates. This is rejection for demonstrated coverage and immediate implications, not for access limits or a false theorem.

## value

FAIL

Cycle algebras and the distinction between maps and image copies are naturally motivated, but the actual claimed contribution is a singleton specialization of an exact classification, with the arbitrary-field count already encoded by the root constraint. The remaining image quotient and transitivity use only the classified residue and the standard diagonal action; they provide a useful explanatory corollary, not a separate non-routine exact invariant under the review standard. No scientifically distinct repaired claim is delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
