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

The continuous Poissonized independent coordinate refresh semigroup gives A(t)=∏q_i(1-e^-t/m) from empty, B(t)=∏(q_i+p_i e^-t/m) from full; strong Markov renewal implies Laplace transform m!/Q(v), v=ms, with Q(v)=∑e_k∏_{l≠k}(v+l), e_k elementary symmetric of r_i=p_i/(1-p_i). At -j, Q(-j)=(-1)^j j!(m-j)! e_j. For exactly d>0 losses this establishes strict alternating signs and unique roots in (-(j),-(j-1)) for j<=d, and untouched -j roots for j>d, hence a genuine independent geometric factorization. Strict convex log[1+up/(1-p)] proves Schur PGF order; direct positive pair-balancing cost proves strict mean order; fixed-budget extremizers and P>=1 unbounded supremum follow. Independently for m=3 p=(1/10,1/5,3/10), Q=(250v³+1350v²+2055v+756)/126 has roots approximately -0.54073,-1.87225,-2.98702 and exact Markov-state PGF E[2^-T]=84/2869 agrees with m!/Q(3).

## originality

PASS

Attrill–Garoni and Long 2026 analyze common homogeneous erasure probabilities or stationary-entry asymptotics; those do not yield the arbitrary heterogeneous-profile geometric roots and majorization budget laws. Classical independent-geometric first-hit results for skip-free birth-death chains require one-dimensional skip-free dynamics; the heterogeneous number-present process is not Markov, so direct theorem implication fails. This proof provides a polynomial-root reduction for the heterogeneous model; full primary articles inaccessible, retained as priority risks.

## value

PASS

An exact full first-completion law and fixed total erasure-budget extremizers are natural quantitative invariants of the nonmonotone coupon system. The sharp threshold P=1 between attained finite worst profiles and infinite supremum, strict allocation ordering and exact geometric-factor interlacing are useful structural facts beyond a restatement of the classical coupon collector.

The dated certificate retains the supplied scientific assessment, sources and limitations.
