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

The first coordinate of a fixed pair forces b=0, which suffices. In a finite functional graph, the eventual cycle is constant along edges hence throughout a weak component; conversely every vertex connects to its eventual cycle. Thus the component criterion is exactly absence of additional cycles. T²(1,x)=(1,x+x²); a nonzero least-period orbit of g(x)=x+x² gives a T-cycle of twice that period because all its intermediate first coordinates 1+x differ from 1 and are distinct. For an odd divisor s>1, trace(1)=1, trace(x²)=trace(x), and ker(g)={0,1}, so g permutes the trace-zero subspace of dimension s-1. Its nonzero elements are periodic but not fixed. For multiples of four use the F16 subfield. The modulus u^4+u+1 has no binary root and is nonzero modulo u²+u+1 (remainder 1), hence is irreducible. Independent product convolution and reduction gave the eight products 8,14,10,13,15,9,12,11 in the listed order; XOR gave the corresponding first coordinates 5,13,3,9,4,11,2,14, with distinct pairs. For replay multiply the four-bit polynomials by convolution mod 2, then for each nonzero degree k>=4 subtract u^(k-4)(u^4+u+1) in descending degree. Every m>=3 is divisible by four or has an odd divisor s>1. For F4, a zero product reaches a fixed point in one step, a=b in two, and distinct nonzero pairs reach (1,1) in one step for {omega,omega²} and two for {1,omega} or {1,omega²}; (1,1) then reaches (1,0) in two steps. Independently iterated all starts until b=0 using moduli u+1 and u²+u+1: numbers at successive hitting times from zero were (2,1,1) over F2 and (4,3,3,2,4) over F4. I inspected, but did not run, the frozen script.

## originality

PASS

The distinct supported contribution is the all-degree characteristic-two conclusion, via the permutation on the odd-degree trace-zero subspace. The graph, cycle lift, extension reduction and some finite witnesses or existence results were already available. Neither that bounded coverage nor the companion short-period classification settles the unrestricted criterion.

## value

PASS

This answers the characteristic-two part of an explicit published hypothesis by replacing an unbounded family of prime-degree computations with a uniform invariant-subspace argument and one small field witness. It gives a clean boundary between the two fixed-point-only fields and all larger extensions. This value does not rest on refinding an eight-cycle already known to exist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
