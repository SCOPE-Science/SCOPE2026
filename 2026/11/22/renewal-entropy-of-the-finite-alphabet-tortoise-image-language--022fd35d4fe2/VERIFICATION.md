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

The Defant–Kravitz maximum-letter recursion proves both language inclusions, since each lower-alphabet output block can be lifted independently. To check the ambiguous initial concatenation, let B(z) count distinct words in I_{q-1}I_{q-1}. Splitting at successive maximum letters then gives the exact unambiguous block-level series A_q=A_{q-1}+z B/(1-z A_{q-1}), with A_{q-1} coefficientwise <= B <= A_{q-1}^2. The smaller-alphabet growth induction makes A_{q-1} diverge at its radius and z A_{q-1}(z) strictly increase through 1 at an interior first root. On the root circle there are no other zeros of the renewal denominator: the z and z^2 coefficients are positive, so equality in the triangle inequality requires the positive real point. The positive numerator and simple pole give the claimed two-sided exponential bounds (indeed a positive leading constant), and the interior root gives strict monotonicity. In the binary case every word ending in 1 and only those and all-zero words are possible. For larger q the specified four-letter factor would force a descending length-two image between consecutive maxima; a direct length-two check excludes it. Independent aligned windows give the stated exponential bound. For the sextic, splitting every binary prefix after its last 1 gives I_2 I_2 all binary words, which yields the stated rational A_3 and the sextic as its denominator minus z times its numerator. Decimal bisection (`python /workspace/branches/frozen_replay.py 5`) gives lambda_4=3.5503790656826695146745…. The frozen enumeration was read as bounded corroboration, not a proof for arbitrary lengths.

## originality

PASS

Pass for the supported uniform sharp growth characterization and fixed-alphabet density dichotomy, with the quaternary constant as a consequence. The word recursion is prior and the binary/ternary specializations are covered; neither gets originality credit. No established broader source supplies the stated all-alphabet renewal root or its sparsity consequence.

## value

PASS

For a natural word stack map, the supported result determines the exponential size of the reachable set at every fixed alphabet size, not merely whether sorting succeeds on special words. The universal recurrence turns that rate into an exact algebraic quantity, and the binary positive-density versus larger-alphabet exponential-decay transition is a meaningful qualitative separation. This concerns image cardinality, not Shannon entropy or fiber sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
