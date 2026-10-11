---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

If a finite certificate exists, take the minimum of the finitely many positive expansivity constants. Orbitwise closeness below it forces equality of every observable value and joint injectivity gives equality of points, so f is expansive. Conversely, when f is expansive the source theorem gives Exp(f)=C(X) with a common constant; coordinates of any topological embedding X->R^m are therefore expansive. Any certificate map is continuous and injective from compact X to Hausdorff R^m and hence itself an embedding, proving equality with e_R(X). Menger--Nobeling gives the finite-dimensional 2d+1 bound. The singleton m=0 case is handled separately and consistently.

## originality

FAIL

Bautista--Jung--Morales already prove that an expansive homeomorphism has every continuous observable expansive with one common constant, and their Example 2 states that a single injective expansive observable forces expansivity. The submitted finite-family condition is the same argument after taking the minimum of finitely many constants. Once expansivity is known, identifying the least number of jointly injective real observables with the Euclidean embedding dimension is exactly the definition of a Euclidean embedding applied to coordinate functions. Menger--Nobeling then supplies the standard 2d+1 bound. The result is mathematically correct but mechanically assembled from the primary theorem and classical embedding theory.

## value

FAIL

The certificate invariant is tailored so that the cited expansive-observable theorem reduces it immediately to the classical Euclidean embedding dimension. The proof consists of taking a finite minimum, reading embedding coordinates, and invoking compact-to-Hausdorff injectivity. Under the required bar against renaming/substitution and textbook deductions, this has insufficient independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
