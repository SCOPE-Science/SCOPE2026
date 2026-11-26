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

In characteristic zero or p != 2,7, the two affine singularity equations force t=xy nonzero, equal seventh powers of x and y, and both stated eliminants in t. I independently recomputed the competing quadratic/quartic resultant 392, so only G(t)=4t^2+3t+1 can vanish. The two diagonal roots r have distinct t=r^2=-(r+1)/2; at each t the fixed nonzero x^7 leaves at most seven x values. Direct diagonal substitutions and the order-seven symmetry give all fourteen. The two points at infinity have nonzero Z derivative. The two pure second derivatives vanish at each node and the mixed derivative is (49/4)(1-t) != 0, giving the split node and two distinct rational branches over its residue field, not just over the closure. The independently verified quartic Q has discriminant 2^12*7^2. Its quadratic extension is nontrivial and u=x^7 has pole order four on the sign choice v~-7t^2, so the degree-seven Kummer step is irreducible. Hence the torus model, and then its plane closure (no components supported on coordinate axes or infinity), are geometrically integral. The Gauss sum squares to -7 and transforms by the quadratic character; multiplication of j by q gives two regular sextic orbits on j != 0 and the quadratic sign orbit at j=0. The ratio x/y recovers a primitive seventh root for j != 0; even x separates the values since r^7=(7r+5)/64 recovers r from x^7. Recomputed the irreducible 2+6+6 projection factors, all four orbit partitions follow from the action, and normalization adds exactly one point per rational node over each extension. Reproduction: python /workspace/flex_and_octic_reproduction.py (SymPy 1.14.0); frozen verifier inspected only.

## originality

PASS

The equation, node count, absence of singularities at infinity, and smooth-model good reduction and arithmetic are prior. The explicit closed-node fields and simultaneous split-branch descent, with their complete singular-to-smooth zeta correction, survive the strongest inspected comparisons. This is a bounded originality finding, not a priority guarantee.

## value

PASS

The arithmetic of the node scheme is a natural missing exact invariant of a known rational singular presentation. In particular, the residue degrees alone would not give the correction without the separate branch descent. Together they supply all plane-model point counts from known smooth counts by an explicit finite zeta factor, with no new smooth zeta or exceptional-prime claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
