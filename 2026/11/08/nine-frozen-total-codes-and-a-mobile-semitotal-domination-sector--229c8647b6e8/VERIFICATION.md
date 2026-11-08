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

# Verification of Pappus semitotal-domination reconfiguration

All three verifiers are standalone Python 3 programs that require only the standard library. From the extracted package directory, run:

```sh
python3 verify_lcf.py
python3 verify_incidence.py
python3 verify_symmetry.py
```

Every successful invocation terminates with `VERIFY_OK`. The `.out` files contain the actual recorded successful outputs, not substitutes for running the scripts. The two main programs reconstruct the graph from different data (LCF chords versus Pappus point-line triples) and check their equality through an explicit vertex isomorphism. Both independently enumerate all six-element candidates and legal exchanges, and compute every eccentricity in each \(288\)-vertex mobile component. The orbit program independently enumerates the entire automorphism group through \(9!\) point permutations and one explicit point-line duality.

## Mathematical checks

The lower bound for semitotal domination is \(\gamma_{t2}(G)\ge2|V(G)|/(2\Delta(G)+1)\). For \(18\) vertices and cubic degree, it gives \(\gamma_{t2}\ge6\). The finite scripts produce six-element witnesses, so the minimum is exactly six. There are \(\binom{18}{6}=18564\) candidate subsets; the scripts check all of them with no sampling. Exactly \(297\) qualify, including exactly nine efficient open dominating sets, which form the displayed \(3\times3\) family.

The jump graph has \(1026\) undirected edges, nine isolated states and one component of size \(288\), where every vertex has eccentricity six. The slide graph has \(432\) edges and the same component sizes. Its nontrivial component has eccentricities \(8\) for \(126\) states, \(9\) for \(54\) states and \(10\) for \(108\) states. Thus its radius is eight and its diameter is ten. Every isolated state in either graph is exactly an efficient total dominating set.

The automorphism enumeration verifies group order \(216\), the orbit sizes \(9,18,54,108,108\), and degree pairs \((0,0),(6,6),(8,8),(6,2),(8,1)\) for jump and slide, respectively.

## Boundaries

The programs certify complete finite calculations on the explicitly supplied Pappus graph only. They do not assert novelty, mathematical publication priority, infinite-family claims or any external independent audit. All inferred numeric edges and metric claims require executing the full delivered source files, not merely trusting the saved outputs.
