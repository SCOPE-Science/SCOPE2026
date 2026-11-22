---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Read frozen RESULT.md, derivation and check.py. Positivity and P=S+I bound follow from S<=max(A,S0) and P'<=K(A+delta)-delta P. In any low-S episode (S_n<delta e^{-AT}/(2beta)), I_{n+1}<=e^{-delta T/2}I_n and S_{n+1}/S_n>=e^{delta T/(2beta)}e^{-beta TI_n}; geometric summation plus one-step entry bound yields a strictly positive susceptible floor for each positive solution. Exactly log L derivative = -beta^2 I for L=q^{beta tau/T} S^beta I; at a pulse q^beta is offset by phase reset. L decreases to zero (a positive limit would force I bounded below), so I->0 by S floor. Logistic pulse comparison gives S->s uniformly in phase. Integrating (1/L)'=beta^2 q^{-beta tau/T}S^{-beta} across periods and Cesaro yields nL->1/C and the explicit I profile. Stable linear equation for z=log(S/s), with forcing -beta I and coefficient tending to s>0, gives uniform n z->-k/C and hence n(S-s)->-sk/C. Boundary: positive initial S,I, delta<beta A, fixed T>0, q in (0,1); no finite-time or seasonal assertion. The three trajectory RK4/script checks are finite corroboration, not the infinite argument.

## originality

PASS

No searched prior theorem states the global neutral-threshold Lyapunov identity plus both universal phase-resolved 1/n coefficients in the exact unseasonal two-state pulse system. The originating paper determines the disease-free orbit and threshold, but its Theorem A analyzes p strictly above/below p2 and only identifies a Floquet crossing at p=p2. Other Resultary critical disease models change equations and cannot supply the explicit pulse profile. Best-of-knowledge PASS, not historical certification.

## value

PASS

The exact invasion-eigenvalue-one boundary is a mathematically and epidemiologically natural missing case of the originating bifurcation theorem. A global exclusion of positive recurrent infection plus universal phase-profile and susceptible correction gives nontrivial information beyond the familiar local transcritical sign and is independently reusable to benchmark critical pulse dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
