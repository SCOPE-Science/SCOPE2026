---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Squarefree derivative 2x^6+lambda gives discriminant condition lambda^7!=2. Riemann–Hurwitz for 8 fully ramified points yields g=6. The basis dx/y, x dx/y, dx/y²,...,x³ dx/y² is regular and length six. Cartier coefficient extraction of powers (1+lambda x+x^7)^3 and ^1 gives the listed 6x6 semilinear matrix; independent expansion for lambda=0,1,2 matched every entry, including zero entries. For lambda=0 one length-3 nilpotent chain and remaining killed directions yield first-rank 2, then 1, then 0; for lambda!=0 a length-5 chain and one killed direction yield ranks 4,3,2,1,0. The parameters excluded exactly remove singular branch polynomial. Finite F25 tests in bundled script corroborate only, not prove all algebraic closed parameters.

## originality

FAIL

DECISIVE PREPUBLICATION COVERAGE. The published 2026-11-02 result Arithmetic-rank strata and a genus-three nonordinary divisor for cyclic trigonal genus-six curves in characteristic five treats y^3=x^7+a x^3+b x+1. Specializing a=0, b=lambda gives the exact submitted curve and discriminant D(0,lambda)=lambda^7-2. Its theorem explicitly states p-rank zero along all smooth a=0 and a-number 4 only at (0,0), otherwise 2. Its full text also prints the complete coefficientwise semilinear Cartier blocks A and B, whose specialization reproduces the submitted complete iterate profiles by routine matrix-chain multiplication. The submitted finding is a special case of a strictly stronger established classification, despite its narrower wording.

## value

FAIL

The natural special-fiber a-number jump and p-rank-zero line are scientifically meaningful in the broader 2-parameter classification, but the submitted 1-parameter result recomputes a known subfamily; its extra iterate profile is a short direct consequence of the earlier explicit Cartier blocks, not a new motivated independent invariant. Relative to available prior work it adds no substantive gap. Correctness and exact finite verification do not restore value for this covered restricted statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
