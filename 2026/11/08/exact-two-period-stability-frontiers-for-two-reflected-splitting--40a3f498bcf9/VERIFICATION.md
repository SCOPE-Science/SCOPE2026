---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

From the inspected actual RESULT.md and original verify.py, the resolvent of LJ gives T_c(t)=[[ (1-2it)/(1+it), it/(1+it) ],[1,0]] and T_h(t,u)=[[ (1-i(t+u))/(1+it), iu/(1+it) ],[1,0]]. Rebuilt the two monodromies independently in symbolic algebra; both determinants equal -ab/[(1+ia)(1+ib)], of modulus strictly less than 1. Direct Schur–Cohn evaluation factors the respective strict-stability gaps as 8ab(1-4ab)(1+2(a+b)^2)/[(1+a²)²(1+b²)²] and 4(1-(a+b)²)((a+b)^4+a²+b²)/[(1+a²)²(1+b²)²]. Reconstructed det(I+M)=2(1-4ab)/D or 2(1-(a+b)²)/D; the threshold root is -1 and other root strictly inside disk. Beyond the boundary there is exactly one expanding multiplier. Equal-history data yield z_1/z_0=(1-ia)/(1+ia) of modulus 1 and cannot lie in the decaying one-dimensional monodromy eigenspace. Independent spectral samples confirm the factors, without replacing proof. Quantifiers limited to positive a,b, L>0 and exactly two-period prescribed steps on A=B=LJ.

## originality

PASS

The matched-skew constant-step t=1/2 threshold was proved by Shehu and is credited; it supplies only the diagonal a=b, where both new boundaries agree. The variable-step FRB linesearch work uses previous-step weighting, but adaptive step restrictions do not imply the exact stability regions for arbitrary prescribed two-cycles or their contrast. A new comparison of the two updates on exactly the same skew inclusion and sharp off-diagonal Floquet diagram survives. Best-of-knowledge, with specialist-periodic-splitting priority risk.

## value

PASS

The coefficient on the reused gradient is a motivated choice in variable-step reflected splitting. On a canonical sharp fixed-step counterexample, the exact boundaries differ drastically: 4ab<1 allows an arbitrarily large individual step, whereas a+b<1 does not. This is a useful sharp algorithmic stability stress test, not claimed as a general nonlinear or adaptive convergence result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
