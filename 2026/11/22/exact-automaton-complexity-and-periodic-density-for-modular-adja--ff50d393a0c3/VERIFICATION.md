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

The theorem is proved for all integers \(q,m\ge2\) by an integer-flow Euler-lift lemma, an explicit modular-incidence state count, a Myhill–Nerode suffix-separation argument, and finite-state periodic Markov-chain convergence. Neither a finite word cutoff nor a numerical approximation is used to infer the universal theorem.

Two structurally distinct finite checks were run against the source files in this package:

* `python3 verify_bfs.py` enumerated reachable states by breadth-first search, minimized by iterative quotient refinement, compared acceptance against direct factor counting on all short words, and computed exact rational acceptance probabilities for several lengths.
* `g++ -O2 -std=c++17 verify_residue.cpp -o verify_residue && ./verify_residue` enumerated incident-compatible residues directly (not by reachability), then independently minimized the resulting complete DFA.

The checked pairs \((q,m)=(2,2),(2,3),(2,4),(3,2)\) all give the theorem's sizes \(18,56,130,386\). Output files `verify_bfs.out` and `verify_residue.out` record the observed values. Direct word checking is bounded (up to length eight for the binary cases and six for the ternary case). The recorded density examples are illustrative only; the limiting statement relies on the graph's proven irreducibility, regular in/out degree, and period exactly \(m\). The public source files are standalone, need no external data, and require Python 3 and an ordinary C++17 compiler.
