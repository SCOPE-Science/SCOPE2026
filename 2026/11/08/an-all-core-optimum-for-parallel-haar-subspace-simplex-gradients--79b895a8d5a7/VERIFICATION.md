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

The exact source score is positive constant C_d times Gamma ratio B(p) divided by two evaluation rounds when 2<=p<=c or ceil(p/c)+1 beyond, with a special 2/3 factor for p=1. The integral L(s)=d(log B)/ds=int_0^∞ e^(-su)/(1+e^-u)du is positive and strictly <1/[2(s−1)] for s>1. Hence H_c(s)=B(s)/(s+c) strictly decreases for s>=c+2, while Gamma recurrence gives exact equality H_c(c+2)=H_c(c). Since B(p) strictly increases, each partially filled batch is strictly dominated by its full batch; for k>=2, H_c(kc)<=H_c(c+2)=H_c(c), equality at k=2,c=2 only. p=1 and c=1 bounds compare elementary B(1),B(2),B(3) with 3<π<4, all d cases included. Independent exhaustive bounded score comparison d<=150,c<=64 matched all classifications, not used as all-integer proof.

## originality

PASS

Hare–Roberts–Royer arxiv:2308.04734 Theorem 4.2/section 4.2 already gives B(p), the parallel cost model, empirical p=c rule over finite c and p multiples, and the c=2,p=2,4 tie. This review credits all those findings. Inspected 2023 full preprint section explicitly gives finite numerical exploration, not complete all-integer proof or nonmultiple exclusion; new proof closes their stated unbounded optimality gap. Later journal 2025 full text remains a risk, as different generic subspace descent papers optimize different objectives.

## value

PASS

A sharp all-integer optimizer of an explicit, practically motivated idealized parallel evaluation model closes a published finite numerical conjecture and determines the only nonunique case, including sparse partial batches. This is a mathematically useful rigorous frontier even without a new optimization algorithm or hardware runtime assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
