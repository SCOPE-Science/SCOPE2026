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

For a vanishing sum of at most p roots, split off a prime s>p from the squarefree conductor. At most p fibers are occupied, while the minimal polynomial over the remaining cyclotomic field is 1+X+…+X^(s-1); its degree s-1 follows from the coprime cyclotomic degree ratio. A missing fiber forces all coefficients to vanish, and induction on the number of primes forces exactly one occupied fiber and one p-cycle. The one-prime case follows from the same minimal polynomial over Q, and conductor 1 cannot vanish. Applying the result to exponent products a(b-b') gives a full residue set mod p and constant coordinates at r>p where the difference is nonzero. Since B has p entries, all differences nonzero mod p is equivalent to its being a transversal. The converse gives each required Fourier zero. Labeling the selected elements by their p-coordinate counts literal sets exactly once: B has r^p choices for a constant coordinate of A and r choices elsewhere; A has r choices per constant coordinate and r^p-r per nonconstant coordinate. This gives the stated multiplicities, their distinctness by unique factorization, and Q times the product of (2r^p-r). For N=30, the positive strata total 225 supported two-sets, out of 435; the weighted multiplicity total is 10125. The analytic proof, not tests, establishes all t≥1.

## originality

FAIL

The classification and its multiplicity products are mechanically implied by Lam–Leung’s prior classification of minimum-weight vanishing sums, followed by column orthogonality and independent-coordinate counting. The exact products were not located as earlier explicit statements, but that does not protect this direct corollary. The later-dated exact content match is recorded separately and is not the basis for the failure.

## value

FAIL

Literal multiplicity is a legitimate invariant, but in this scope the proposed contribution is an immediate coordinate count after applying a known minimum-weight theorem to the orthogonality equations. Neither the histogram nor the ordered count introduces a separately motivated unknown invariant requiring nonroutine work. The N=30 example illustrates the same formula, rather than exposing a new obstruction or structural phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
