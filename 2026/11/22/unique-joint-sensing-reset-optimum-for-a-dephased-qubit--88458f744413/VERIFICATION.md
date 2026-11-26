---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

A stationary exponential preparation age, integrated against the decaying rotating coherence, gives c=r/(r+gamma+i omega). The resulting equatorial Bloch radius m=r/sqrt(h), h=(r+gamma)^2+omega^2, is strictly between zero and one for all admissible parameters. Pulling back the polar SLD metric diag((1-m^2)^-1,m^2) uses the Jacobian -r/h^(3/2), giving r^4/[(h-r^2)h^3]. The derivative has the sign of the frozen cubic: expand 4(h-r^2)h-2 gamma r h-6r(r+gamma)(h-r^2)=2P(r). The one coefficient sign change, P(0)>0 and P(infinity)<0 prove strict rise and fall and the two substitutions prove the uniform bracket. In normalized coordinates y=r/sqrt(A), u=gamma/sqrt(A), the root is above 2/sqrt(3) since the cubic takes value 2/3 there. Both F_y and F_u are negative at the root, so dy/du<0; u decreases with |omega|/gamma. Factoring at u=1 gives (1+sqrt(7))/3; at u->0 compactness of the positive root bracket gives sqrt(2). The scaled determinant A^2 det Q=y^4/[(1+2uy)(1+2uy+y^2)^3] proves the claimed 4/27 limit even when the ratio tends to infinity along varying gamma and omega. The SLD-vector map on the equatorial plane is invertible, so the nonzero parameter Jacobian implies a nonzero commutator parallel to sigma_z, whose expectation vanishes. In the usual local independent-copy collective setting, Q^-1 times the SLD vector is a feasible tuple in the Holevo optimization with real covariance Q^-1; hence weak commutativity makes the SLD benchmark asymptotically compatible, not a single-copy POVM guarantee. Independent normalized bisection gives y about 1.2152504370, 1.2929767057 and 1.4132181347 at u=1,0.25,0.001. Replay: /workspace/reproductions/frozen-review-checks.js, record 5, Node.js; the frozen symbolic and finite-difference script was inspected, not executed.

## originality

PASS

The distinct contribution supported is the stationary joint frequency–dephasing D-optimal design theorem, including the unique cubic and sharp normalization. The same-day scalar Resultary finding uses the same stationary state and changes the objective; the two optima provably differ even at resonance. The state, equatorial QFIM geometry and asymptotic compatibility test are not credited as new. This is a bounded comparison, not historical priority certification.

## value

PASS

A known reset rate is a natural experimental control, and a jointly unknown damping process makes a scalar-frequency optimum insufficient even on resonance. The exact all-parameter optimizer, sharp interval and detuning law give a usable stationary local precision benchmark under a fixed type of preparation. The result makes no claim about rate-normalized information, universal single-copy attainability or advantage over time-optimized unreset protocols.

The dated certificate retains the supplied scientific assessment, sources and limitations.
