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

Cauchy–Binet gives the sum of three squared minors including a zero minor for coincident times, so independent replicates yield equal objective values at the endpoints. The reduced objective has derivative with the sign pattern of an affine sinusoid of period π: its amplitude strictly exceeds the offset by the squared-amplitude test, since sinh(ηΦ)>η|sin Φ|. The endpoint derivative signs force only a minimum in the short interval; at Φ=θ the terminal zero crosses downward, so it is positive immediately to the left and there is still no interior maximum. For θ<Φ<π the negative terminal derivative beats both equal endpoints; there is at most one interior downward crossing. For Φ≥π the multiplicative decay per π excludes every later period from positive global optimality, and the test x=θ strictly beats the endpoints of [0,π], including resonances. For Φ=π (and all integral multiples) factoring the sin² gives x=θ directly. Uniform convergence to the limiting objective and F₀′(θ)=−2 then give an O(q) root displacement; Taylor expansion and the uniformly bounded phase derivative of the perturbation give the stated first-order term and O(q²) remainder. Fixing small positive and negative residual phases makes that leading sign alternate on unbounded sequences. An independent direct Gram-matrix calculation spot-checked the reported two interior examples and a multiple-period resonance.

## originality

PASS

Qualified pass for the exact horizon partition and unique all-horizon interior optimizer with signed oscillatory drift under the stated three-event design. The closest prior conclusions either constrain the times to a different design or use different mode families or objectives. The determinant reduction and perturbation methods alone are standard.

## value

PASS

The exact threshold resolves whether to spend a third real measurement on replication or on a new sample, and the first-period conclusion avoids a global search over an arbitrary number of periods. The sign of the long-horizon bias is a substantive distinction from monotonically approaching an optimal placement. These conclusions are naturally tied to the information design and not fine-tuned examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
