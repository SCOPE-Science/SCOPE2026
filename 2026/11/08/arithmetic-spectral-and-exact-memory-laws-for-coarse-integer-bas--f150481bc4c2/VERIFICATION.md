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

Under Lebesgue-uniform X0, each b-fold map T_b(x)={b x} has b full subbranches per equal q-cell interval, giving conditional-uniformity on every observed cell after any finite observed history. Direct counting yields Q_b(j,k)=#(0<=r<b:bj+r≡k mod q)/b; composition T_c T_b=T_bc gives Q_b Q_c=Q_bc and commuting kernels. For B=aq+r, each row has r counts a+1 and q-r counts a, so TV=r(q-r)/(q B) and exact independence iff q|B. Nonconstant Fourier modes g_k(j)=(1-ζ^k)ζ^{kj} map to b^-1 g_{bk mod q}; the modular functional graph yields characteristic polynomial (z-1) z^(q-1-M) prod_C(z^|C|-b^-|C|), including transient zeros. Independently checked exact q=6,b=2 characteristic polynomial (z-1)z^3(z²-1/4), Q2 Q3=Q6 uniform and several TV distances. These finite checks are corroborative; algebra proves all q,b.

## originality

PASS

Previous integer-beta literature proves general transfer operator mixing, CLTs and invariant densities, but the relevant inspected primary paper does not give the exact q-cell commuting finite Markov factors, arithmetic no-memory criterion q|product, or complete noncoprime modular Fourier spectrum. No earlier Resultary equivalent surfaced in the actual meaning search. The new finite-factor classification is supported as best-of-knowledge original, with an explicit risk from older symbolic-dynamics/Markov-partition literature.

## value

PASS

The complete stochastic spectra for arbitrary q including composite noncoprime pairs, combined with exact finite-time erasure under changing integer slopes, are natural exact invariants of coarse observations. Distinguishes true finite-time independence from merely exponential mixing, and gives a reusable arithmetic method to select observation resolution and slope schedules.

The dated certificate retains the supplied scientific assessment, sources and limitations.
