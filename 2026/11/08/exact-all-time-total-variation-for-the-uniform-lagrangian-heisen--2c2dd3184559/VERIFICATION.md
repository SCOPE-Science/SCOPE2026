---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Uniform symplectic-Lagrangian incidence gives Pr(v nonzero in L)=1/(Q+1), and the step law mu=delta_e/(Q+1)+Q nu/(Q+1), nu uniform on zero-central slice, q odd. For each nontrivial additive central character, the Schrödinger Weyl-slice sum is Q times parity R, so Fourier(mu)=(I+R)/(Q+1), with +1 eigenspace size (Q+1)/2 and -1 size (Q-1)/2. The Q^2 abelian characters give eigenvalues 1 and 1/(Q+1). Counting each dimension-Q irrep Q times gives the stated complete convolution spectrum; finite Fourier inversion yields exactly the point-mass expression. For t>=1 the signed mass excess is on z=0 and deficiency on z!=0 (checked from a_t and b_t); summation gives TV=(q-1)/q*(2/(Q+1))^(t-1). Initial t=0 is expressly excluded from chi-square formula. Independently carried out exact group convolution on every state for q=3,5,m=1 and t=1..4, matching all point masses and TV values; finite tests supplement the Fourier proof for odd prime powers.

## originality

PASS

Gross (2006) establishes the standard odd-dimensional Wigner/parity identity used here, and finite Heisenberg Fourier representation is classical. Bump et al. (2015/17) treat sparse few-generator Heisenberg steps. A similarly named November 8 finding averages only TWO fixed complementary coordinate Lagrangian subgroups and has different Fourier spectrum and mixing law t/2^(t-1), not the UNIFORM mixture over all Lagrangians. The complete dense-measure all-time exact total variation and complete PMF do not follow from those prior theorems without a new measure-specific transform and sign calculation. Priority remains bounded.

## value

PASS

Uniform selection from all symplectic Lagrangians is a natural high-symmetry finite Heisenberg walk. An exact full-time point mass and total-variation identity reveals a sharp one-step-to-two-step asymptotic mixing transition, dramatically different from sparse generators and from mixing only two fixed coordinate subgroups; the exact spectrum is reusable for analysis of this walk. This is a motivated structural calculation, not just general Fourier theory restated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
