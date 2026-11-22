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

# Reproduction and limits

Run `python3 verify_rule94.py` from the directory containing the provided files. It constructs all adjacency edges for the 4-state and 64-state temporal transfer graphs, computes traces through their complete dimensions, and reconstructs every integer coefficient of the characteristic determinant using Newton identities. It checks the exact stated determinants (including all zero coefficients) and 100 return-count terms. The recorded output gives 5 and 65 edges respectively, and nonzero determinant coefficients at degrees 0, 1, 2 and 4 for the first graph, and at 0, 1, 2, 4, 7 and 8 for the third-return graph. The period-three counts begin with 7 at ring length 7, 0 at length 8, 9 at length 9.

Run `python3 direct_check.py`. It independently simulates the literal 8-entry local transition table and checks every binary configuration on indexed rings of lengths 3 through 16. For each circumference, direct fixed and third-return counts equal the transfer determinant predictions. The length-16 check covers 65,536 initial configurations; the full run covers 131,064 configurations across lengths 3–16. For length 16 there are 91 fixed states and 475 third-return states, hence 128 temporal three-cycle orbits.

`transfer_certificate.json` records the exact graph edges and polynomial coefficients. The all-size theorem is justified by the graph–spacetime bijection, full exact determinant evaluation, formal series support argument, and pole analysis. Exhaustive finite examples are not an infinite proof by themselves. Independent external validation and definitive historical priority review have not been performed.
