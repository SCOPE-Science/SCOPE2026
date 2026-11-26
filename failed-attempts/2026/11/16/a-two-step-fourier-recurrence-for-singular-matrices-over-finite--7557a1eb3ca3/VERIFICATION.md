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

Unit-pivot elimination factors exactly the primitive determinant-zero matrices as uv^T, with one unit-scaling orbit per factorization. Subtracting the sum over nonprimitive v requires T^Tu in the socle because the character generates the additive dual. For kernel-size exponents x,y in the two coordinates, the primitive count is q^(x+y)-q^(min(x,m-1)+min(y,m-1)); use (x,y)=(a,b) or (min(a+1,m),min(b+1,m)). In the nonprimitive part, A=pi B is parametrized by B modulo pi^(m-1). Its fibers over length m-2 have size q^4 and their Fourier sum vanishes unless T is divisible by pi. For T=pi S the induced quotient character is psi(pi^2 times a lift), which is generating; the length-zero case works with the trivial sum. Rank-one factorization over the residue field gives the base. Counting lifts with a unit pivot whose Schur complement is prescribed, or factoring out the common power of pi, gives the four negative multiplicities, and convolution gives both sharp norms by a delta input and a phase-matching input respectively. Independent exact replay, evidence/1/reproduce.py and evidence/1/replay.txt, evaluated 46 diagonal Smith sums over Z/8, Z/16, F2[t]/(t^4), and F4[t]/(t^2), including 750 negative frequencies and mass 407/32 at Z/8. The all-length result rests on the argument, not these examples.

## originality

FAIL

The earlier Resultary determinant-zero cone record gives a stronger closed all-length coefficient formula and all spectral multiplicities for exactly the same chain rings. Its valuation parameters are a change of coordinates, and its negative histogram directly supplies the endpoint norms. The two-step identity is a correct alternate evaluation, but no distinct substantive spectral or norm claim survives.

## value

FAIL

The Fourier spectrum of the determinant-zero cone is a natural invariant. But its coefficient distribution is already known in a strictly more directly usable closed form, and the length-three sign tally and norm are mechanical evaluations of that spectrum. The alternate two-step proof, while sound, does not furnish an additional motivated unknown mathematical fact; the earlier proof is also elementary and already valid in both characteristics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
