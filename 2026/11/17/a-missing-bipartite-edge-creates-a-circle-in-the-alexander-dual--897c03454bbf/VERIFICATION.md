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

# Reproducibility and mathematical verification

Run `python verify.py` with Python 3.9 or later. The program uses the standard library only. Expected exact stdout is recorded as `verification_output.txt` and ends in `COMPLETE_BIPARTITE_EDGE_DEFECT_THREE_CUT_PASS`.

The program constructs edges of the graph directly, enumerates disconnected induced triples, creates the ordinary cut complex as the downward closure of their complements, and builds the combinatorial Alexander dual by avoiding disconnected triples. It checks that the dual is precisely \(\{\sigma\in E_a*E_b:\{u,v\}\not\subseteq\sigma\}\cup\{uv\}\). Signed chain boundary operators are reduced independently modulo primes 1009 and 10007; for shore sizes \((3,3),(3,4),(4,4),(4,5),(5,5),(5,6)\), both prime fields return first and third dual Betti ranks \(1\) and \(R(a,b)\), with no others. The original cut-complex ranks are checked separately when its ground set contains at most ten vertices. Enumeration also checks the exact number of disconnected triples.

These finite modular checks are diagnostic evidence, **not an integral or universal proof**. The actual integral proof appears in `RESULT.md`: the Mayer--Vietoris map is injective over the integers, and Whitehead's theorem supplies a wedge decomposition. No infinite-range algorithmic certification and no independent mathematical audit are asserted.
