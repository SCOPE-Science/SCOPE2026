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

PASS: In the unnormalized graph indicator on G=F_q^2, q=2^m, K=2^gcd(m,r), a nonzero horizontal translation a has Gold derivative D_a(x)=a^(2^r+1)+a^(2^r)x+a x^(2^r). Its linear part has kernel aF_K, so each nonempty overlap fiber has K points and each ambiguity coefficient is either 0 or K, with (q-1)q^3/K^2 nonzero such coefficients. For zero translation, quadratic Walsh sums of Q_d(x)=Tr(d x^(2^r+1)) have radical K when m/h odd, and when even have radical K^2 for exactly (q-1)/(K+1) choices d and radical 1 otherwise; Walsh-square orthogonality yields all stated levels/multiplicities. Weyl orthonormality gives singular values q|A_g| (sqrt(|G|)=q) and positive condition number q/K, including u=2 value coincidences. Independently constructed binary-extension-field/Walsh counts q=4,8,16 across r=1,2 agreed with every amplitude multiplicity (e.g. q=16,r=1: amplitudes 0:49995,2:15360,4:160,8:20,16:1; r=2:0:61500,4:4032,16:4). Finite checks corroborate, not substitute for universal radical arguments.

## originality

PASS

PASS (best knowledge): Bojarovska–Flinth full primary establishes general Gabor phase-lift and ambiguity diagonalization but not vector-valued Gold-graph subfield-specific amplitude counts. The fully read published scalar Boolean quadratic graph study uses a 1-dimensional binary OUTPUT; Gold maps F_2^m to F_2^m, so its 3-level law does not encompass this graph. Existing Gold-graph sharp fourth moment addresses different Fourier-extension operator. The distinct parity-branch singular multipliers/rank law are not implied by these results; implicit Gold ambiguity tables remain a residual risk.

## value

PASS

PASS: Gives the full singular-value and nullity spectrum of a natural phase-lift measurement operator, explicitly quantifies the subfield-parity transition and exact condition number, and identifies all Weyl kernel directions. Operator-recovery stability/rank invariants are meaningful beyond the classical Gold derivative and quadratic Walsh facts, although nonlinear phase retrieval is not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
