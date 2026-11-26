---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Unique representations follow digitwise without carry; converting the finite radix words gives a bijection to the atoms of S_k and 2S_k. At n=4^k there is exactly one extra A element. The truncated Cantor CDF errors are bounded by one atom because tail length is less than atom spacing; an interval of grid-cell length encounters at most two prefix hulls for each measure. For the ceiling coupling x=ceil(4^k U)/4^k, the product error is O(2^−k)/x and the denominator error at fixed product is H(x−U)/x. Direct expectation gives the harmonic sum and its multiple 1/(2·4^k), respectively. The uniform limiting bound follows from unique addition for the lower product and v²≤3a_v for the upper: at either family of numerator jumps in a block the ratio is 2^k(2^k+v+1)/(4^k+a_v)≤3/2+2^−k, and between jumps it decreases. Passage to fixed u>0 via the finite CDF approximations is valid. C∪2C is null and each open complementary interval has positive constant FG, giving the density by monotone change of variables there. The two displayed geometric gap families map bijectively onto (1,3/2) and their coefficient sum is 2, hence mass 2/3 and full support. Depth-L hull endpoints are Cantor points, so every exposed open gap has exact product found by prefix counting; the effect of omitted intervals on the CDF is bounded by their combined length ≤2^−L. Independent exact scaled-cell enumeration through depth eight reproduced the three stated CDF enclosures and checked gap images and both gap families: python3 /workspace/branches/independent_reproduction.py additive. The frozen script was inspected, not run; the finite calculation corroborates but does not prove the convergence and exhaustion arguments.

## originality

FAIL

The assigned distribution theorem has demonstrable equivalent or stronger coverage in the distinct indexed Resultary record 4d1044ecba2d. Its displayed full density contains the very same inverse-square component of mass 2/3 and the whole residual law. Its different sampling window gives the same continuum profile after rescaling; its Lipschitz bound also gives a stronger Wasserstein rate for the assigned window by geometric block mixing. Integrating and truncating its explicit rational gap series already yields a certified CDF with a smaller error at depth L. The particular cylinder-cover implementation is a useful alternate expression, not a distinct surviving theorem. The overlapping record is dated later than the frozen record; this is a finding of mathematical coverage in the reviewed corpus, not an assertion of earlier priority, copying, or incorrectness.

## value

PASS

The distributional question for a sharp additive-complement example is meaningful: an extremal limsup does not indicate how frequently any interval of ratios occurs. An exact positive density component, description of the entire law, and rigorous numerical enclosures answer that question. This judgment of the theorem's mathematical usefulness is separate from the duplication of scientific content in the inspected corpus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
