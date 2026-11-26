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

Averaging over within-class permutations and exchange of the first two classes preserves constraints and cannot increase the spectral norm. The four nonstationary eigenvalues on within-class contrasts, the A−B contrast and the AB−C contrast are 1−X−Y, 1−κY, 1−2X−Y and 1−(1+κ)Y. For fixed Y, T=1−Y: if X<2T/3 then T−X>T/3; if X>2T/3 then 2X−T>T/3. The best possible value for these two X-dependent constraints is uniquely achieved at X=2T/3 with value T/3. The positive sign of the AB−C contrast is dominated by 1−κY. The remaining envelope is max{1−κY,(1+κ)Y−1,(1−Y)/3} on [0,min(1,1/κ)]. The decreasing and increasing bounds cross at Y=max{2/(1+2κ),4/(4+3κ)}, with the optimal Y clipped to the right endpoint if necessary. Strict decrease before the crossing and strict increase after it yield uniqueness in Y, the four branches, and transition points κ=1/2,2,4. For fixed optimal Y and μ, all feasible X lie in [max(0,1−Y−μ), min(1−Y,(1−Y+μ)/2)], giving exactly the stated face, including collapse at the two endpoints. At p=q (κ=2), the unique weights are equal across all three pairs, so the optimizer also respects the full automorphism group in that case. RESULT.md, VERIFICATION.md and verify.py were inspected; the reported finite rational LP and eigenvector checks were not rerun. No unrestricted optimizer classification beyond existence and value is inferred from averaging.

## originality

FAIL

The exact value and the complete invariant optimal face are already covered in the presently indexed Resultary literature by the stronger result with prescribed, possibly nonuniform, stationary masses on the same graphs. This is a current-coverage finding, not a claim that the differently dated record had earlier priority. The older published spectral reduction alone would not decide this verdict.

## value

FAIL

The three transitions and the nonunique optimal face would be useful in their own right for network allocation, but the entire stated invariant and face are mechanically recovered from a stronger available result by substituting the uniform class masses. No independent valuable remainder needing repair is present.

The dated certificate retains the supplied scientific assessment, sources and limitations.
