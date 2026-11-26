---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For the stated Zak convention, translations supply Fourier phases in omega, while splitting modulations into the two residue classes modulo 2 gives the two channels omega and omega+1/2 by Parseval (irrelevant unimodular phases and common normalization). A common zero of the continuous weight therefore rules out a uniform lower bound. At (a/2,1/2), terms k and -k-1 cancel; at (a/2,0) the transform is S(a)(U(a)-c). At (0,1/4) and (0,3/4) the odd samples cancel in pairs and the even samples give D(a)(V(a)-c), proving both exact energy identities. The Gaussian series are locally analytically convergent, with positive S and Jacobi product D. Poisson summation gives D(a)=(2a)^(-1)S(1/(2a)); differentiating its logarithm gives the duality with constant 1/(2*pi). For an independent monotonicity proof, write S_*(u)=sum_j (-1)^j exp(-u*j^2) and Phi(u)=u*S_*'(u)/S_*(u). Jacobi's product expresses Phi as a positive sum of terms m*u/(exp(m*u)-1) with weights 1 or 2; every term decreases strictly, with local uniform convergence of derivatives. Since V(a)=-Phi(4*pi*a^2)/pi, both curves increase strictly by duality. The a-to-infinity half-grid sum has U(a)=a^2/4+O(a^2*exp(-2*pi*a^2)); as a tends to zero its Poisson dual gives U(a) tending to 1/(2*pi) from above. These limits yield both open ranges and exactly one aspect for the indicated fiber, not a classification of all resonant lattices. The more precise endpoint terms in RESULT.md follow from the next half-grid pair or the leading exponential in the theta product. The derivative sign test also confirms the positive window is not a positive Gaussian-scale mixture. See RESULT.md lines 42–114; VERIFICATION.md and CHECK.py were inspected, not run, and finite sums do not establish global uniqueness.

## originality

FAIL

The motivating positive-window branch and its unique aspect are exactly covered by prior indexed record 8357d6e9b461, in a broader Gaussian-scale family, with the same theta equation and the same null character. The other branch is its standard Fourier transform at the reciprocal aspect. The shared scalar strict monotonicity was already stated independently in theta literature. The remaining off-resonance numbers are direct squares of a scalar residual already computed in the prior pre-Gramian proof; the repackaging is not a distinct surviving claim of mathematical acceptance value.

## value

FAIL

A unique nonframe aspect for each positive quadratic-Gaussian window is a meaningful obstruction, but it is not new here; its Fourier counterpart requires no new mechanism. The part not literally spelled out in the prior result is a pair of pointwise Zak energy squares of the known scalar row, not an analysis of the minimum, another distinct family of obstructions, or new control near the frame boundary. This is useful exposition of one obstruction, but no independently valuable surviving finding has been established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
