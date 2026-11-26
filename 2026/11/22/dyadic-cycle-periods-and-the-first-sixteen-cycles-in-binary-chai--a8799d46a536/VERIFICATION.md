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

Mod t only (0,0) and (1,0) can be periodic. In the first class, multiplying b by a∈tR_m strictly raises its valuation until b=0, so only (a,0) cycles there. In the second, the output equations give b=v+u and u²+(1+v)u+v+w=0; the unknown coefficient at each positive degree has coefficient 1 and all other summands at that degree are determined from lower ones. Thus this core is permuted. Under one-level reduction, new coefficients transform affinely with linear part (x,y)↦(x+y,y). A power returning the lower level acts by a translation or by a shear plus translation on a fiber, with order dividing four. The singleton unit core at m=1 begins the induction, so all periods are powers of two. For the formal polynomial iterates the second-coordinate degree is strictly larger than the first, and the degree recurrence is (d,e)↦(e,d+e); no positive iterate is the identity. For each power 2^k a nonzero coordinate difference cannot vanish on the product of the infinite subset tF₂[[t]] of F₂((t)) with itself. A nonzero evaluation survives in a finite quotient, giving periods exceeding 2^k. The degree-eight jet argument is consistent: both homogeneous parts have both variables as factors and vanish on u=b, so they contain ub(u+b); on the binary core this product is in t⁴, giving order at least nine after the degree-five factor, while discarded degree ≥9 terms already vanish through m=9. The entire finite cutoff and census were also independently reproduced, using a distinct multiplication-table recurrence P(a,2c+e)=tP(a,c)+ea and full path visitation of all 2^(2m) vertices for 1≤m≤10. No period 16 occurred at m≤9. At m=10 the exact cycle counts at 1,2,4,8,16 were 1024,1280,5888,17152,6144 and no others; core fixed counts were 512,3072,26624,163840,262144. The witness in bit encoding went (3,4)→(515,4) after eight and returned after sixteen, so its least period is sixteen. In a finite functional graph each weak component has exactly one directed cycle; the counts sum to 31488. Replay: python3 /workspace/branches/5d54ab14-9345-42dc-b9bd-eb18147d673b/independent_census.py 10; full_run.txt in the same directory records the UTC run and all counts. Uploaded verify.py and reference log were inspected, not executed. The finite run supports the finite cutoff and census, not the all-m assertions.

## originality

PASS

The structure graph and the possibility of two-cycles in nonreduced rings are established prior work. The available comparisons do not give the periodic core, the unbounded dyadic-order statement, or the exact first period-sixteen threshold and census for this truncated-polynomial tower. A focused lookup and inspected passages support this bounded verdict, not a comprehensive priority claim.

## value

PASS

Long cycles of this natural structure map are a posed mathematical direction. The binary nilpotent tower isolates the effect of thickening; the periodic core and unbounded dyadic orders are structural answers. The cutoff at an intrinsically defined first occurrence of period sixteen is not an arbitrary finite slice, and the complete counts at that threshold give the component structure and a baseline for studying later lifts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
