---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the repaired RESULT.md. Absorption requires each signed field to be strictly positive because ties may change spins. At an aligned site, the cutoff above d−2 forces all d neighbors to agree in each layer; identical adjacency and connectedness propagate the same aligned pair globally. Those two configurations are stable since d−a>0. In the remaining sector B=−A, the two signed fields coincide and equal d−2r_i+a, positive exactly if the number r_i of unlike neighbors is less than d. Both implications hold uniformly in the strict window; the repair makes explicit that (1,3) is the cubic case only. On a prism each rung with different spins requires a horizontal match in each row; a monochromatic rung supplies both matches vertically. The overlap matrix therefore counts labeled cyclic rung words by rooted closed walks without a division by n, also for n=3. Independent exact replay: python3 /workspace/branches/b5974770-8b31-4e59-b98c-19cdbacf146e/reproduce_transfer.py 12. Using integer trace identities it yields coefficients [1,−4,5,−10,7,−6,4,−4,4,0,0,0,0,0,0,0,0], verifying the factorization; totals n=3..12 are 36,120,366,1166,3828,12464,40392,131188,426498,1386006; direct cyclic-word enumeration agrees for n=3..6. On |z|=2, |z³(z−3)|≥8 and |z²−2|≤6, so the quartic has exactly one exterior root, simple and real in (3,4); every other root is smaller than 2 in modulus. Power trace counts algebraic multiplicities without assuming diagonalizability, so the leading coefficient is one and the entropy normalization is by 2n in one layer. The frozen verifier was inspected, not run; numerical and finite checks do not replace the graph-general proof.

## originality

PASS

The repaired scope credits prior enumeration of the degree-two coloring slice and compares the cubic result with a directly inspected one-layer circular-ladder census. The distinct claims are the exact absorbing-state reduction for intermediate inhibition and its evaluated cubic-prism transfer; neither the local neighbor predicate by itself nor the binary cycle census is counted as new.

## value

PASS

The local-field theorem resolves which mixed states can genuinely remain frozen, rather than merely linger in metastability, in an entire natural coupling interval. Exact counts on the natural cubic family quantify the size of that sector, with a growth rate measurably distinct from one-layer majority. It shows extensive possible heterogeneity without overclaiming its dynamical likelihood or attraction basins.

The dated certificate retains the supplied scientific assessment, sources and limitations.
