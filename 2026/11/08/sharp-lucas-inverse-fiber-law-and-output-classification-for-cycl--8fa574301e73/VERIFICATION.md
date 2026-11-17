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

The Wolfram Rule 28 local outputs 1 exactly on 010,011,100; de Bruijn Z/O matrices enumerate closed indexed cyclic paths, including n=1 and n=2. Z³=Z² and tr Z=tr Z²=2 give zero-output fiber count. Restricting OZ^r to the nonzero two-state block gives E (zero gap) and F (positive gap), so every output fiber has the displayed trace product. With all positive gaps, trace(F^k)=Lucas L_k and k≤floor(n/2). Zero gaps either create E²=0 or permit pairing EF=diag(1,0)≤F entrywise; nonnegative trace-product monotonicity yields strict suboptimality, including the lone odd-ring boundary via Fibonacci F_m<L_m. Hence exactly the two alternating even winners or n rotations of the unique length-two zero-gap odd winner, with short n≤3 direct cases. Independent exhaustive direct-map counts through n=12 corroborated every output fiber; the matrix proof handles all n.

## originality

PASS

Classical de Bruijn predecessor enumeration, Jen 1989 and fixed-block t-step preimage literature precede this work. The inspected Jen treatment describes finite-linear preimage patterns and notes alternating extremizers for Rule 76, but does not give the all-length indexed *cyclic* Rule 28 Lucas maximum, exact every-fiber gap product and complete winner classification. Published-record searches closest to Rule 18, Rule 22, Rule 126 and Rule 184 concern different local rules and not implication-equivalent truth tables. Originality is best-of-knowledge subject to older per-rule tables.

## value

PASS

A natural exact all-length inverse-fiber invariant for a standard elementary cellular automaton, including every fiber and a complete optimizer/equality set, quantifies the worst one-step information loss under periodic boundary conditions. The two-matrix reduction and even/odd optimizer split are substantive structural properties rather than a sample of finite automata.

The dated certificate retains the supplied scientific assessment, sources and limitations.
