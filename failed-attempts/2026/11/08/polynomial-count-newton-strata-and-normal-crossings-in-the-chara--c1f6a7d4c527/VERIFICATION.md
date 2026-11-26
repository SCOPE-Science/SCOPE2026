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

Checked the theorem on the smooth marked coefficient open, not on isomorphism classes. The gradient equations reduce to the principal minors and determinant of the displayed matrix on squared coordinates; Euler's identity gives F=0 at a gradient zero. Frobenius on the three negative-monomial Čech classes has diagonal 2(b+ac), 2(c+ab), 2(a+bc), with all cross entries killed by parity. Stable rank gives 3-rank and the first kernel gives the a-number by Cartier duality. The three tame sign quotients have genus one and give the three distinct character summands, hence an elliptic product up to isogeny. Completing the square gives the X-quotient coefficients a^2-1, 2ac-b, c^2-1; the middle coefficient detects the elliptic Hasse invariant, and ordinary and supersingular elliptic slopes give the stated total polygon. The graphs meet on the axes because 1-a^2 and its cyclic variants are units; the two-by-two gradient determinants are those units and the triple gradients are independent. On the origin a=3 implies superspeciality. The discriminant in c is (a^2-1)(b^2-1); summing its quadratic character gives (q-2)^2+1 raw triples with a,b not ±1, and the two boundary slices c=±1 remove 2(q-2). Each nonordinary graph has q^2-6q+10 points, each axis q-2 and the triple intersection one, giving the four exact strata by subtraction. q=3 leaves only the origin.

## originality

FAIL

Two earlier dated distinct Resultary records already state the same divisors and all-extension counts; one also gives exactly the Newton and a-number strata. The frozen record supplies no separate theorem outside their combined coverage. This is demonstrated indexed coverage, not an inference from unavailable literature.

## value

FAIL

The marked-space SNC theorem and complete count are useful in their own right, for example to calibrate coefficient-space sampling, but these exact outputs and their geometric interpretation are already available together across the two indexed records. No distinct invariant, new hypothesis, or sharper useful consequence is added by the frozen package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
