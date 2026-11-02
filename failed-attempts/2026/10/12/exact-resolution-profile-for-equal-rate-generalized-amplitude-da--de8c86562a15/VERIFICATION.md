---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The equal-rate generator sends I->0, X->-mu X, Y->-mu Y, Z->-2mu Z. Thus N_s=e^{sL_mu} is the exact Pauli channel with p_I=(1+a)^2/4, p_X=p_Y=(1-a^2)/4 and p_Z=(1-a)^2/4, a=e^{-mu s}. The weights are nonnegative, sum to one, and yield channel eigenvalues a,a,a^2. Since N_s-p_I id is CP, for arbitrary ancilla and finite D(rho||sigma), N_s⊗id(sigma)>=p_I sigma, and operator-monotonicity of log gives D(rho||N_s(sigma))-D(rho||sigma)<=-log_2 p_I. The Bell input rho=sigma=Phi saturates the bound, since N_s(Phi) is Bell diagonal with eigenvalue p_I on Phi. Consequently D^A(id||N_s)=-log_2 p_I. Anchor Theorem A1 directly identifies the minimum-resolution asymptotic exponent with sup_{s>=smin}D^A/s. g(x)=-ln((1+e^{-x})/2)=x/2-ln cosh(x/2) obeys g(0)=0 and g''(x)=-1/(4cosh^2(x/2))<0, hence g(x)/x strictly decreases for x>0; the supremum is at smin for mu>0. The limit is mu log_2 e and the series is mu log_2 e-(mu^2 smin/4)log_2 e + (mu^4 smin^3/96)log_2 e+O(smin^5). For mu=0 both exponents vanish for every smin and no strictness is claimed. This is the full quantifier and normalization range. Independently executed SymPy matrix-generator, Pauli-weight, spectrum and Taylor checks reproduce the algebra; they corroborate, rather than replace, the infinite analytic proof.

## originality

FAIL

The exact profile is a routine corollary of two published stronger results: Salzmann et al. (2026) Theorem A1 gives every fixed-resolution Lindbladian Stein exponent as a duration supremum of amortized channel relative entropy; Wilde et al. (2020) Theorem 37 reduces all jointly covariant fixed-channel pairs, hence the identity versus any Pauli channel, to relative entropy of their Choi states. The equal-rate generator has the elementary Pauli/Bell weight p_I=((1+e^{-mu s})/2)^2. Substituting -log_2 p_I into Theorem A1 and differentiating the elementary function g(x) evaluates the supremum and yields every asserted boundary, limit and Taylor coefficient. The absence of an identical formula in the 2026 paper is not independent originality when its own general theorem and the earlier broad fixed-channel theorem mathematically imply it.

## value

FAIL

The requested temporal-resolution profile is physically interpretable and concerns a natural qubit noise model, but all its mathematical content is a standard Pauli-channel Choi-overlap substitution into the general Stein/variational theorems, followed by strict concavity of a one-variable logarithm and its Taylor expansion. The source already identifies the equal-rate finite regime. No independently unknown obstruction, new structural lemma, boundary classification beyond the covered general theorem, or nonroutine parameter phenomenon is established. This can be useful as an illustrative computation but does not survive the stated independent mathematical-value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
