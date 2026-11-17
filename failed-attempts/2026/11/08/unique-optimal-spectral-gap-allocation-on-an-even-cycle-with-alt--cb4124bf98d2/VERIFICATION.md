---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The full RESULT.md proof is reconstructible: lambda_2 is concave in edge weights, so rotation-by-two averaging produces a symmetric optimum but does not by itself prove all-weights uniqueness. Bloch diagonalization gives the lower spectral band a+b-sqrt((a+b)^2-4ab sin^2(pi/m)). The substitution U,V>=0 with UV=cos^2(pi/m) and weighted AM-GM gives the two-rate optimum. A fixed two-dimensional complex eigenvector with squared edge chord lengths proportional to prices gives a sharp Rayleigh upper bound for any independent feasible vector; equality enforces both real and imaginary parts as eigenvectors, and the two noncollinear circle chords at each vertex determine both incident weights uniquely. The m=2 eigenspace is handled separately. Independent exact rational substitution for C6 with price (4,1), B=1 gives w_even=5/84,w_odd=2/21,lambda_2=1/14. The actual source verifier performs 48 rational case tests and principal minor PSD checks, only finite corroboration.

## originality

FAIL

Two earlier published results state and prove exactly this complete theorem. The Oct 13 and Oct 18 full RESULT.md findings have the same graph, all m>=2, independent nonnegative edge weights, strictly positive alternating price pair, same conductance allocation, same unnormalized Laplacian gap, global uniqueness, four-cycle exception and large-ring limit. B<= budget vs equality is immaterial because a connected positive maximizer spends the full budget. There is no surviving separately claimed new invariant.

## value

FAIL

The underlying spectral optimization is useful, but its exact complete answer and boundary cases were already independently published twice. The reviewed unchanged package offers no distinct motivated mathematical lemma or invariant not logically determined by those results; a different derivation or rational example is not new scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
