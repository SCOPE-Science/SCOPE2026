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

For a J² target, reduction modulo J forces every root into J since the semisimple quotient is a product of fields. Multiplying the paths gives a_i a_{i+1}=u_i and a_i b_{i+1}+b_i a_{i+2}=v_i, with all length-three root coefficients free, even when n=3 and length-three paths return to their starting vertices. On the torus all a_i are units; closing a_i=s_i t^{(-1)^i} requires t²=s_n in odd length and s_n=1 in even length. Dividing b_i by a_i a_{i+1} leaves I+S on a cyclic sequence. Its kernel is controlled by h_{i+1}=-h_i: zero when n and q are odd, one-dimensional otherwise, with image given by the signed-sum condition (unsigned in characteristic two). In even length the normalization produces P/t-tQ=0, including in characteristic two. Counting t, then the normalized length-two solution and then the free length-three vector gives all three fiber laws. The image counts follow by counting admissible u, and in even length by the surjective map v↦(P,Q) with q^{n-2} points over each pair. Summing the fibers gives (q-1)^n q^{2n}; the claimed coincidences at q=2,3 also follow. These are statements about the principal torus, not all of J².

## originality

PASS

The shared degree-two cycle condition is not new. The checked contribution is the precise J⁴ lift with prescribed length-three target coefficients: compatibility, square-class strata, fiber sizes, and the resulting torus density. Neither of the unusually close Resultary records gives or implies the lift, and the inspected external sources give structural context only. This judgment does not infer chronological priority from a shared date.

## value

PASS

The all-nonzero locus is a natural stratum of the square map, not an arbitrary slice. Counting its lifts reveals a second obstruction invisible after J³ reduction and a qualitative density difference: in odd characteristic the fraction of attainable targets stays one-half for odd cycles but is asymptotic to 1/(2q) for even cycles. The fiber laws additionally separate the even-cycle degeneracy P=Q=0 from square-class compatibility. These are usable exact data for this map, beyond the familiar multiplicative recursion alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
