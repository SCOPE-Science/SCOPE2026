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

Write M=(a^2-c^2)(c^2-1)>0. The assumed bound b^2<=M implies (ac)^2-b^2>=a^2+c^2(c^2-1)>0. Multiplication by q and 1/q are bounded on H^2; evaluation of the first two coefficients and removing them give the bounded inverse displayed in the record, with x_1=g(0) and x_0=ag'(0). Direct substitution gives UT=zU and the transported space has kernel given by the three orthogonal summand evaluation vectors. With t=z conjugate(w) and W=q(z) conjugate(q(w)), Q=1-(1-t)K=tR/W. The determinant of the coefficient matrix of R is strictly positive throughout the region, including its endpoint, and the positive leading entry proves positivity. Q is positive by analytic conjugation and Schur product, with Q(z,z)=1-(1-|z|^2)K(z,z)<1; thus |Q(z,w)|<1 and K never vanishes. For H=c^2 R-(c^2-1)W, the positive leading entry and determinant c^4(M-b^2)>=0 give positivity even at b^2=M. The identity 1-1/K=c^2t/W+t^2H/[W^2(1-Q)] now gives positivity by the convergent Schur series for 1/(1-Q). Normalization at zero, nonvanishing and the classical criterion give CNP. On the finite summand D=T*T-I has positive leading entry and det D=(a^2-1)(c^2-1)-b^2>0; the defect is strictly positive on that summand and zero on H^2. On the same summand, the difference (T*T)^2-T*^2 T^2 is P=D+D^2-A*DA. Its leading entry is c^2(b^2+c^2-1)>0 and its determinant is a^2c^2(M-c^2b^2). Thus equality is allowed at M/c^2 for logarithmic concavity, which fails above it, and the endpoint b^2=M still satisfies CNP. A separately written symbolic script extracted the R/H coefficient matrices from rational expressions and P from a finite truncation of T, matching all determinants, including 20, -36 and 176 at (3,2,2). Replay: python3 /workspace/branches/independent-checks/record5.py (SymPy 1.14.0); record5.log in that directory. The frozen script was inspected, not executed.

## originality

PASS

Credit only the CNP certificate in the strict non-logarithmically-concave region beyond the known exact threshold. A distinct same-day result gives the same two-site model, the entire log-concave part of the parameter cone, its exact boundary and CNP there, after a direct change of symbols. The same-day radial result covers the uncoupled line. Neither supplies the nonzero-coupling continuation beyond log-concavity. The CNP upper sufficient cutoff is not credited as an exact classification.

## value

PASS

A coupled rank-two Hardy-block model gives a robust open separation: complete Pick can persist after exact operator log-concavity fails, with an analytic certificate rather than isolated numerical examples. The known boundary and classical criterion are context, not the scientific contribution. The location and positive size of the new interval can guide sharper boundary and finite-defect investigations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
