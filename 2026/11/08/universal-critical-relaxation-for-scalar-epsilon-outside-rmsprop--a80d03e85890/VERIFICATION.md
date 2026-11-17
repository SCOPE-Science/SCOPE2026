---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The exact update multiplier is (sqrt(v_{n+1})-epsilon)/(sqrt(v_{n+1})+epsilon). Its strict magnitude below one when x!=0 forces |x_n| decreasing; geometric averaging forces v_n to the squared limiting gradient; a positive limit contradicts strict contraction. Thus x_n,v_n->0; either finite hit or eventual negative multiplier. The nontrivial memory tracking lemma follows by unrolling v_{n+1}, bounding old history with rho in (sqrt(beta),1), and dominated convergence so v_{n+1}/(a^2x_n^2)->1. Reciprocal increment of |x| tends to 2a/epsilon. Cesaro implies amplitude and memory constants. Independent numerical iteration at a=2,epsilon=3,beta=.6,n=80000 gives n|x_n|=0.74869, n^2v_n=2.24229 versus limits .75,2.25. Boundary initial x=0 and finite-hit handled.

## originality

PASS

Loh et al. establish subcritical stability and supercritical trapping, instability and cycles, while the source explicitly distinguishes the equality case. The submitted exact equality global convergence and universal polynomial rates with memory tracking are not directly implied by the reported strict results. Earlier different memoryless Riemannian example is not the same recurrence. Best-of-knowledge given full recent primary could not be obtained with accessible tools.

## value

PASS

The critical learning-rate boundary is a natural omitted case of nonlinear optimization stability; algebraic convergence where linearization has multiplier -1 and a universal memory-independent decay constant is useful for sharp step-size theory. Not merely a numerical threshold reproduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
