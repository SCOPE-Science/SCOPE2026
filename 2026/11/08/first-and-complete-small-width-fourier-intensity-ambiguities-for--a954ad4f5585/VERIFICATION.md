---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The full torus intensity is a finite Laurent polynomial with the aperiodic autocorrelations as coefficients; orthogonality gives the converse from equality everywhere. Central reversal inverts both lags, and global sign cancels in every product. The action on arrays is the four-element action used in the census, allowing stabilizers. Burnside independently gives (4^n+2*2^n)/4 orbits: reversal and sign-times-reversal each pair the 2n cells into n pairs and global sign fixes none. A separate exact enumeration grouped full correlation vectors from one representative per orbit. For widths 1 through 8 the singleton counts were 2, 6, 20, 72, 272, 1048, 4160, 16488; the only double counts were 4 at width 6 and 12 at width 8, with no larger fibers. At width 6 all eight ambiguous representatives have neither identical nor opposite rows. Expanding F H and -F* H, with F=z^4+z^2-1 and H=(1+z)+w(z-1), gives the displayed pair; the reversal of F preserves its circle modulus. The two orbit representatives differ. This is exhaustive only through width 8. The frozen documentation's Python 3.8 minimum is inaccurate (int.bit_count needs 3.10), not a mathematical defect.

## originality

PASS

The supported distinct claim is the sharp two-row binary threshold and exact small-width fibers under the stated quotient. Neither the generic ambiguity mechanism nor one-dimensional uniqueness is new here. The identical indexed record is not a distinct antecedent; the distinct square-mask record agrees numerically at sixteen cells but classifies a different support. No transfer of its classifications to the two-row rectangle is established.

## value

PASS

The two-row sign model is a minimal genuinely multidimensional full-support phase-retrieval setting. The sharp first nonseparable ambiguity supplies benchmark witnesses, while the return to uniqueness at width seven gives an exact obstruction to treating ambiguity as monotonic in width under this support constraint. Counting all fibers distinguishes rare genuine failures from generic ambiguity constructions and is useful for checking proposed uniqueness criteria. No scaling inference beyond width eight is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
