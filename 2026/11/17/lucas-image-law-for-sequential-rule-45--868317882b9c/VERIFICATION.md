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

For sequential one-pass left-to-right Rule45 on each labelled cyclic ring n>=3, checked the local Boolean identity f(a,b,c)=a xor (b or not c) and the asymmetric first/last boundary equations, which must use old x_{n-1} at i=0 and already-updated y0 at i=n-1. Interior equality marks encode exactly old 0->1 pairs, hence cannot be adjacent. Endpoint constraints recover y0 and q=y_{n-1} xor y_{n-2}. The constructive proof realizes every nonadjacent-mark word with prescribed single endpoint, giving the complete iff output language. Counting independent sets in a line gives F_n+2F_(n-1)=L_n; image entropy is log phi, not a recurrent entropy. Inspected repository check_constructive.py and separately enumerated every input and every candidate output for each n=3..13; exact reachable sets satisfy all three boundary tests and Lucas counts n=3..13 (4,7,11,18,29,47,76,123,199,322,521). Finite checks corroborate all-n constructive proof.

## originality

PASS

Best-of-knowledge the full single-sweep output language and Lucas image count for fixed sequential Rule45 differ from existing results on eventual convergence or asynchronous order-independent periodic states. The Rule45 convergence conjecture is not settled by this image result.

## value

PASS

An exact complete image-language characterization for a naturally studied fixed-order cellular automaton gives predecessor reachability, exact Garden-of-Eden population 2^n-L_n, and a nontrivial exponential information-loss rate. These are mathematically useful even without settling the separate convergence conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
