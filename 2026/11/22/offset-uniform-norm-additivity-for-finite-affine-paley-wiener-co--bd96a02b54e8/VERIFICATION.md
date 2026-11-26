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

The Fourier image of c_j f(a_j x+b_j) is (c_j/a_j)e^{ib_jη/a_j} f̂(η/a_j), supported within the target bandwidth. Real offsets leave the individual norm |c_j|/√a_j unchanged. Log frequencies give a shifted argument and coefficient d_j e^{ib_j e^x/a_j}. Independently, on the common intersection of the shifted length-R packet supports, of length R−(max ℓ_j−min ℓ_j), the offset-free output is e^{itx}m(t)/√R. For fixed R and t the offset error in norm tends to zero as the support moves to −∞ (uniform phase convergence and the individual norm bounds); unit packets there are weakly null, so any compact perturbation vanishes in norm on them. Sending R to infinity gives the required essential-norm lower bound for each t and all fixed real offset vectors. The full-line convolution upper bound at zero offsets holds on both frequency signs, so the exact unshifted norm is sup|m|. Maximizing over the compact relative-phase orbit closure gives L iff all summands align there; its annihilator is exactly the integer relations of the log ratios. This also verifies genericity and the squeeze for every approximation number. In the 1,2,4 example |m|²=11/4+x/√2−2x², x=cos θ, attaining 45/16 at x=1/(4√2). No attainment at a finite phase parameter is needed in the general theorem.

## originality

PASS

Best-knowledge pass for the exact offset-uniform phase criterion. The translation-invariant multiplier formula is classical and not itself the contribution. The available individual-operator, two-term and other-space sum theorems do not supply the offset-family equivalence. Particular prior limit-operator or crossed-product coverage remains a realistic residual risk, as does the relative priority of conceptually related same-day work.

## value

PASS

The phase criterion is a complete answer to when the norm triangle bound persists simultaneously under arbitrary real translations. It ties exact essential norms and approximation numbers to integer relations among dilation parameters, contrasting universal-phase genericity with an explicit sharp resonant deficit. This separates a structural obstruction from the problem of optimizing each finite sum numerically.

The dated certificate retains the supplied scientific assessment, sources and limitations.
