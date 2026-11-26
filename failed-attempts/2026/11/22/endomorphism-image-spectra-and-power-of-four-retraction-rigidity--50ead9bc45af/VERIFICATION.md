---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For coordinates (p,u) representing p+2u modulo four, the output parity is p and the upper bits are u+p+q under the quandle product. Any preserving map has parity output constant in u, since p+q ranges over all translations. The upper output satisfies h(p,u+t)+h(p,u)=a(p)+a(p+t). At p=0 its increments are additive in t, forcing a(p)=Lp+c, and the equation at every p then forces h(p,u)=Lu+b_p; direct substitution proves sufficiency and uniqueness. With rank k let B=2^k, C=2^(r-k). The B output parity fibers are disjoint. In each, C input parities choose from C quotient cosets of im L, so occupancy t has (C)_t S(C,t) assignments, with B^C lifts and Bt image points. Multiplying fibers, rank-L counts and 2^r translations yields E_r. Rank-L counts come from choosing a k-space and a surjection onto it. Composition gives L^2=L, Lc=0 and b_(Lp+c)=(I+L)b_p. In each of the B fibers the fixed parity label x+c has b in ker L, with 2^(r-k) choices, and each other label must share that kernel component and has B choices of image component. The number of complementary kernels to a given image is 2^(k(r-k)), since each is the graph of a linear map from a fixed complement to the image. Multiplication by the choices of c gives I_r, including the constant maps (k=0) and identity (k=r). Each image has B fibers of size B, exactly one full coset of im L over each output parity; subtract its fiber offset and reindex by x in im L. The operation adds x+y to the second coordinate, giving Q_k, not merely the cardinality 4^k. All counts are of functions. For r=2 the independent counts match every coefficient, and substitution at r=3 gives I_3=64z+114688z^4+229376z^16+z^64 and E_3(1)=2^36.

## originality

FAIL

Two distinct indexed findings already give the exact all-endomorphism and idempotent counts in broader rank-one square-zero unipotent Alexander families, including the same quandle in characteristic two. Their specializations reproduce all coefficients and the retract rigidity; the retraction record also classifies prescribed embedded images and multiplicities. This is demonstrated equivalent/broader coverage, not a conclusion about which same-day record came first.

## value

FAIL

The objects and the distinction between images of arbitrary and idempotent maps are natural. But the exact invariants and retract isomorphism types are already determined by the broader checked results under a coordinate swap and prime specialization, including the printed small-case values. No distinct non-mechanical Takasaki consequence beyond that transport is established here. The failure is about the submitted specialization, not the utility of an exact quandle census in general.

The dated certificate retains the supplied scientific assessment, sources and limitations.
