---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For rank one, both K and J resolvents are inverse-positive irreducible M-matrices, and the S-step denominator 1+h(delta_x,+delta_y-alpha)>0. This proves all h>0 and graph sizes, not merely tested ones. Rank-two input F G^T has rank 2 and nonnegative entries. I independently assembled three rational Galerkin systems in SymPy (6x6,6x6,4x4) from the displayed Lx,Ly,F,G,h=20; the exact (3,3) output equals -594033061301428469823221753304439853683600602652582704940168750296800744522344351667480732497359830640303101165879631698969889519347925460619/6743357461779123941078498750026274375875445328946828328427350132661856787252531551389817715438793173726702157409367346355113640112458374247401, approximately -0.0880915871164129, verifying the claimed strict rational interval. Basis covariance of the Galerkin equations justifies unnormalized exact bases. Connected diffusion makes full backward Euler positivity improving.

## originality

PASS

Best-of-knowledge: the motivating BUG-MLFEM article addresses well-posedness, Sylvester solvers and L2 stability, whereas componentwise rank-one positivity and an untruncated rank-two sign-loss witness are different properties. Other indexed low-rank positivity results concern different numerical schemes/truncated PSD or Vlasov corrections. No implication-equivalent rank-specific positivity result located; full primary manuscript not inspected due access outage.

## value

PASS

The matrix heat equation preserves nonnegative concentrations; practitioners need to know whether a fixed-rank implicit subspace integrator preserves the invariant cone. The exact all-step rank-one guarantee and smallest demonstrated rank-two failure reveal a substantial method- and rank-specific structural boundary, not a generic negative matrix entry or textbook positivity exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
