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

On n+1 circular spots the unique empty spot rotates equivariantly when all n preferences are shifted. In each diagonal coset exactly one tuple leaves spot n empty and is a classical parking function. Summing a nontrivial character trivial on the diagonal over this transversal is the zero quotient character sum. There are (n+1)^(n-1)-1 such frequencies. Coordinate permutations preserve the indicator, and Fourier diagonalization over C counts the nonzero multipliers as the rank. Independently generated the parking set by sequential simulation at every size 1 through 5 and tested every frequency orbit. For an exact vanishing test, evaluate the residue polynomial at all primitive m-th roots modulo 65521. They give precisely the distinct roots of the reduced cyclotomic polynomial. The integer remainder coefficients have absolute value at most the support size, at most 1296, since each of the first m monomials reduces with coefficients in {-1,0,1} for these m. Thus vanishing modulo 65521 at all primitive roots is equivalent to an integer zero remainder. Results: forced zeros 0,2,15,124,1295, no others before n=5, and at n=5 exactly the stated five orbits of sizes 60,60,120,60,60. This gives ranks 2,7,49,501,6121 and five-car nullity 1655. Replay: python3 /workspace/reproduce_reviews.py 2.

## originality

FAIL

Shown already covered in a distinct Resultary record, b9abcc7e4a5d: its Finding explicitly states the same cutoff, all five exceptional multisets with identical multiplicities, and the exact rank. This is statement-level equivalent coverage, not a plausible title or a conclusion about who discovered it first. The universal forced part is classical from Pollak. No distinct scientific remainder survives in the frozen claim.

## value

FAIL

The first strict loss of rank is a natural scientific question and would be useful as a new classification. This submission instead reproduces the same complete known table and adds only immediate rank-nullity arithmetic; a rerun of the same bounded invariant is not a distinct valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
