---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Independent exact replay fixed each horizontal mask first and counted its completions by an unsigned integer height recurrence, then summed each Walsh character directly (no submitted code or fast transform). Replay path: /tmp/opencode/frozen_riordan_replay.py; the recurrence starts with d(0)=1 and uses only h→h at positive height on marked slots, and h→h±1 subject to admissibility on all other slots. Take d_final(0), weight it by 1−2 parity(S∩mask), and sum over masks. The first/last bits are never marked, so each of the 44 internal zeros gives four full zeros. For n=2,…,13 the zero counts are 0,0,0,16,0,8,0,64,0,0,0,176, with minimum weights 1,2,2,5 at the four singular orders (n=1 has no paths; the empty path at n=0 would give no zero). At n=13 the full weight census is 22,66,66,22 at weights 5–8, and bitmask 110 is a zero. There are 4008 eigenvalues of each sign; the least positive and least absolute nonzero values are both 2, and the largest absolute value is 11298. This verifies rank 8016, condition number 5649 on the nonzero singular spectrum and pseudoinverse norm 1/2. Computing k(x)=8192·1{x=0}−Σ_{W(S)=0}χ_S(x) directly reproduces the submitted absolute histogram and total 35360. The projection operator has endpoint norm equal to its kernel's ℓ¹ norm (use a delta at ℓ¹ and the sign of a row at ℓ∞). Averaging any projection over the translations preserves its range and acts identically there, so gives a projection; Fourier diagonalization makes it the unique period-translation invariant projection with that range. This proves the unrestricted endpoint minima 1105/256 over both real and complex scalars. Static verifier inspection found a documentation-only issue: int.bit_count requires Python 3.10, not the advertised 3.9; use 3.10+ for the frozen verifier. The independent exact certificate confirms the mathematical claim.

## originality

PASS

Qualified for the positional Walsh zero census, first low-weight-surviving length, and its exact projection norm. The unsigned counts, height transfer and averaging principle are not originality claims.

## value

PASS

The family and the low-order visibility criterion are natural before enumeration: one asks for the first order where genuine convolution nonidentifiability exists but every parity up to fourth order survives. The census locates the boundary at weight five and the optimum projection norm quantifies the endpoint cost for projecting onto recoverable modes. The precise finite answer, unlike the ordinary path count, is not supplied by the standard univariate formulas. No extrapolation to longer paths is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
