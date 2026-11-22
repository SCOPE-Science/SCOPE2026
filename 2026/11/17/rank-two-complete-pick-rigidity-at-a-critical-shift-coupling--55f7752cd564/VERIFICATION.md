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

PASS: q_b=a²+bz has bounded multiplier inverse because a>1 and |b|<a²-1. U_b(f,x,y)=[z²f+azx+q_b y]/q_b maps H²⊕C² bijectively with equivalent H² norms and transports M_z to [S, v_b;0,A], with v_b(x,y)=e0(ax+by), A(x,y)=(ay,0). Since S*e0=0, defect D_b=[[a²-1,ab],[ab,a²+b²-1]], det=(a²-1)²-b²>0: expansion rank exactly 2. Log-concavity slack E=D+D²-A*DA has det=-a^6 b² and at b=0 is positive diagonal, giving iff b=0. CNP normalized kernel 1+R/(q q*) has F=1-1/K, and congruent Q=q q* F has coefficient block degrees (2,3) [[0,b/a²],[b/a²,1-a^-2-b²/a^4]] of determinant -b²/a^4; negative determinant for b≠0 contradicts positive analytically coefficient kernel. For b=0, 1-1/K=sum_{n>=1} f_n (z wbar)^n has f1=a^-2>0,f2=0,f_n=alpha f_{n-1}+beta f_{n-2}>=0, with alpha=1-a^-2, beta=(a²-1)/a^4, so the standard normalized CNP criterion applies. The b=0 ordinary concavity slack is indefinite. The rank-one operator difference is exactly |b|. Independently confirmed symbolic determinant identities for D and E and inspected exact formal-bivariate verifier. No all-rank-two-shift or nonreal b generalization is claimed.

## originality

PASS

PASS best-of-knowledge: Luo–Rydhe 2026 prove concave-shift CNP and give a logarithmically concave/non-CNP *rank-three* example on H²⊕C³ with a different defect block. Their general CNP criterion and model techniques are inputs; the submitted rank-two a,b critical family has CNP iff b=0 and logarithmic concavity iff b=0 (so is NOT a rank-two log-concave/non-CNP counterexample), together with two exact obstruction determinants and rank-one perturbation instability. None of those specific identities was found stated in inspected primary work or earlier Resultary output.

## value

PASS

PASS: Finite-rank shift perturbations are a canonical test setting for stability of complete Nevanlinna–Pick and logarithmic concavity, and rank two is a natural low-defect boundary compared with prior rank-three counterexamples. The exact condition that both properties hold only on b=0 while expansivity and defect rank persist under arbitrarily small rank-one changes provides a motivated obstruction/rigidity phenomenon rather than a formal parameter rename. Both exact determinants and the nonconcave CNP base point matter for CNP operator geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
