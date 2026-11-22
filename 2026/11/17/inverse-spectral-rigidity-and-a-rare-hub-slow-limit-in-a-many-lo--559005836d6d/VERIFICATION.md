---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For r>=2 with 0<epsilon<1 and 0<alpha_i<=1, c=(epsilon,(1-epsilon)/r,...), the Volterra quadratic update is exactly the reversible row-stochastic star chain P: x_{i,-}x_{j,+}-x_{i,+}x_{j,-}=c_ic_j(q_j-q_i). Positivity and irreducibility give a simple zero eigenvalue and r positive relaxation eigenvalues. Schur complement of epsilon*z I-L yields epsilon^r*z*[U(z)-(1-epsilon)z U'(z)/r]; the leading factor epsilon and coefficient multipliers 1-(1-epsilon)k/r>=epsilon prove unique recovery of the unordered alpha_i including repetitions. This identity was independently checked in exact SymPy arithmetic for alpha=(1/5,1/2,3/4), epsilon=2/7 and all four polynomial coefficients. For slow time, exact u_{n+1}=u_n+epsilon Q u_n+epsilon alpha e_n and |e_n|<=(1-A/2)^n+2epsilon/A make the forcing summable up to n<=T/epsilon. Markov-semigroup Euler convergence gives the stated uniform O(epsilon) bound and fast hub layer. Q has positive off-diagonals, zero row sums; the secular equation yields strict roots between pairwise distinct alpha_i, while trace gives the fast eigenvalue A+O(epsilon). Repeated couplings have no claimed strict interlacing.

## originality

PASS

Qualified best-of-knowledge originality after searches for identical and stronger implications, exact records, primary material, and same-object aliases; relevant previous methods are acknowledged. Neither theorem implies both the all-multiplicity weighted-star inverse coefficient formula and the O(epsilon) slow-limit Markov dynamics. The elementary-symmetric inverse idea has a strong antecedent; do not characterize it as wholly unprecedented.

## value

PASS

The physically natural observable, the entire noiseless fiber relaxation spectrum, determines the original interaction coefficients without labels or extra eigenvectors; the zero-hub regime reveals induced complete-graph communication and quantitative slow/fast spectral separation among originally uncoupled leaves. This is a nontrivial identifiability and dynamical singular-limit result, not just rewriting a stochastic matrix. The original star-mass symmetry must be preserved, and no stable inverse numerical estimation is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
