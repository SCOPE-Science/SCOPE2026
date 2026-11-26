---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Write the monic polynomial with the five distinct column roots; at a root, z^5 equals (sum of the roots) times z^4 plus a combination of powers 0 through 3. Thus the determinant is Vandermonde times that sum and the first four rows give rank at least four. The frozen conductor reduction is sound: for a prime-power part p^a of the normalized ratio conductor, the p^a cyclotomic polynomial stays irreducible over the prime-to-p field by the product degree. Its coefficient constraints make each residue block modulo p^(a-1) a zero subsum. Only one such block can occur by minimality, so all ratios have p-part at most p. At a=1, all p residues must appear: if any residue is absent all block coefficients vanish, minimality forces a single occupied residue, and p would then be absent from the ratio conductor. Hence p<=5 and the conductor divides 30. An independent tensor-basis check of all size-2 through size-5 subsets of the 30th roots found 15, 10, 0 and 6 minimal sets, respectively, with the six minimal five-sets exactly the pentagons. Alternatively, in the conductor argument a minimal five-set with factor 5 must have one term in each residue, with equal prime-to-5 factors by coefficient equality; without factor 5 its conductor divides 6, where an opposite-free set has size at most three. The only nonminimal five-term partition has component sizes 2 and 3. For each antipodal pair the two endpoints lie in distinct cosets of the subgroup of size three, leaving N/3-2 available triples; the opposite pair in the union is unique since an endpoint's antipode is already in the pair and a triangle has no antipodes. This proves the all-N count and the full-spark boundary including N=6. Scope: N>=6, unordered distinct columns and precisely the specified five rows; no general pattern or smaller-minor theorem follows from the finite replay alone.

## originality

FAIL

Lam–Leung's older Lower Bound Theorem 4.8 and their definition of symmetric minimal elements imply precisely the vanishing configurations needed at weight five, for all orders. This is not a comparison only to their Main Theorem about attainable weights. Combined with the standard alternant identity, the full frozen rank classification and census are a direct corollary by counting disjoint cosets. The exact N=12 instance is also explicitly recorded earlier. No separate distinct mathematical claim survives within the frozen result; an independent certificate of the known short-sum step does not change that conclusion.

## value

FAIL

This is a natural Fourier sampling pattern and its failure fraction is a useful explicit expression. But the exact invariant and boundary here are mechanically implied by the older minimal-sum theorem, a standard Vandermonde identity, and immediate subgroup-coset counting. The exact replay and short alternative proof add reproducibility and exposition, not a distinct unknown invariant, nonroutine structural result, or surviving valuable claim under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
