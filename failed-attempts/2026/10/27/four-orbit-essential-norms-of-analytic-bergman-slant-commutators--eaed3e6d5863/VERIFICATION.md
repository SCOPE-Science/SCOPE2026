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

In the specified normalized Bergman basis W has even-entry weights approaching √2 and annihilates the odd entries. The multiplier intertwining M_f W=W M_{f(z²)} gives the stated sign and commutator W²M_P. For a polynomial P the weight along the t-th permitted partial shift is 2√((n+1)/(n+t+4)), so subtracting twice the unweighted model is compact. The four residue blocks give the stated Q_r with exponent (t+r)/4. A Hardy row multiplier has the stated norm upper bound, and its adjoint on a normalized weakly-null reproducing kernel has squared norm ∑|Q_r|², which proves the boundary lower bound against every compact perturbation. Four-point Parseval then absorbs the squared Bergman factor 4. Disk-algebra approximation works in operator and boundary sup norm; the zero-symbol cases are immediate, and otherwise the invariant ratio f/g has zero Laurent order at the origin and no first nonconstant Taylor term. I inspected the supplementary finite matrix checker without executing it; its floating-point comparisons are not the proof of the infinite-dimensional formula.

## originality

FAIL

No identical all-pair wording was located, but this is a direct consequence of the earlier same-normalization Calkin model and the known slant product identity. The earlier scalar two-point maximum alone would not determine a product norm; its actual proof supplies the necessary compact operator identifications. More explicitly, write J for even-index decimation and T_a^H for the Hardy Laurent Toeplitz matrix. The earlier proof gives W≡√2 J and T_a^B≡T_a^H modulo compacts in matching coefficient bases for continuous boundary symbols. Hence [B_f,B_g]≡2J²T_P^H. Standard continuous Toeplitz multiplication gives the Calkin square 4J²T_{|P|²}^H(J*)². Selecting rows and columns numbered 4m and 4n takes Fourier coefficient 4(m−n), exactly T^H_{A_4(|P|²)} with A_4 a the mean of a over the fourth roots. The square of the essential norm is therefore 4||A_4(|P|²)||∞. This derives the exact entire formula, not just its monomial values, without needing a new row-norm result. The archived earlier statement itself disclaiming higher orders does not change this proof-level implication.

## value

FAIL

The essential norm is well motivated, but the precise four-point result is a routine iteration of the earlier quantitative same-space Calkin calculation once the known commutator identity is applied. The example with mixed residues illustrates the formula without adding an independent invariant; phase interaction was already present in the prior general continuous-symbol model. No distinct nonmechanical result remains in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
