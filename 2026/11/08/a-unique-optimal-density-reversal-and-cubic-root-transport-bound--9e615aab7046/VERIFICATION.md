---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The source Gibbs stationary-current parameter s maps (0,infty) bijectively to densities (0,1). Its derivative factors with exactly one positive-root quintic P(s,q) by one Descartes sign change and endpoints; the global maximizer is unique. Differentiating rho(s_*(q),q) and eliminating s gives the exact polynomial resultant 16q^6(q-1)^12(7q^4+12q^3+94q^2+20q-53), independently reconstructed symbolically. Direct evaluation at q=1 yields rho_*′(1)=1/81>0, excluding the spurious q=1 factor. The quartic increases strictly for positive q, crosses once. Weak-q analytic expansion gives derivative -1/4; large-q scaling gives positive derivative (1/3)2^(-2/3)q^(-4/3). This proves the unique reversal. Using the source eigenvalue ratio (q-1)s/((1+s)(1+qs)) on s_*=2^(1/3)q^(-1/3)+O(q^(-2/3)) yields xi_*(q)~2^(-1/3)q^(1/3). The exact original Gibbs/current input is a prior premise, not independently proved by finite experiments.

## originality

PASS

Strong pre-coverage must be credited: the 2026-10-13 full published exact-optimal-density theorem already proves uniqueness of the global density optimizer and its q^(-1/3) vacancy/current boundary scalings by the same quintic. Those are not novel components. However it does not derive the sign of rho_*′(q), an exact unique minimizer at q_c determined by the new quartic, or the Gibbs correlation length *along the optimizing path*; the original June 2026 primary TEP paper supplies only the stationary current, pair correlations and fixed-density xi~sqrt(q). No checked broader theorem implies the optimizer reversal or optimized exponent 1/3. Thus an original and motivated nontrivial final theorem remains, with the already known ingredients explicitly segregated.

## value

PASS

A unique parameter-induced reversal in the density that globally maximizes throughput, with a closed algebraic transition q_c and a nontrivial q^(1/3) optimized correlation length versus fixed-density q^(1/2), describes a real global transport-regime change. These facts are motivated directly by the natural stationary-current optimizer and Gibbs correlation length, and neither fact is just a renamed earlier uniqueness/cube-root-current theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
