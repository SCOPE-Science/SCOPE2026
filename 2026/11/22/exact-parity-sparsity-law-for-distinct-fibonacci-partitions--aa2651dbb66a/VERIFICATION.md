---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Execute `python3 verify.py` with the Python 3 standard library. It regenerates the finite-state machine directly from stated transition rules, verifies that it has exactly 84 reachable states, and checks the exact integral identities

\[
w=(T^5-2T^4+T^3-2T+2I)u,\qquad T^2w=w,\qquad e^Tw=e^TTw=0.
\]

The identities yield an infinite recurrence by elementary matrix algebra. The script additionally compares 17,711 directly generated partition parities with the automaton and an independently generated binary-polynomial product, checking the first Fibonacci-window counts. Neither numerical fitting nor finite enumeration is used to infer the infinite statement. No formal proof assistant or independent outside review was used.

The principal mathematical dependency is the established Zeckendorf-gap partition recursion in Chow–Slattery, *On Fibonacci partitions*, arXiv:2009.08222. The leading-term estimate follows from the exact rational generating function and an isolated positive dominant pole.
