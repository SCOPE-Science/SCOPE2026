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

The augmented-ancestor expectation and residue are correct. Interpret the shorthand 'reachable downwards from the root' in the proof using the cited two-seed block definition: the root is included, and recurse from each included tree vertex to each child iff the child's edge to its grandparent is open (the formal parent serves as the grandparent of the children of the root). Traversing only long edges from the root itself would omit the odd parity class. The prefix has thinned offspring of mean mp and separates into two long-edge classes, based at the root and the formal parent. A short edge inside the prefix plus formal parent joins them; there are exactly N independent opportunities when the prefix has size N. A boundary child's closed long edge leaves only connections through its parent, so the attached subproblems are independent new augmented blocks when their parent is reached. With x=1-p, the size law tilted by x^N has normalizer a=x*phi(1-p+p*a). For that tilted tree the offspring pgf is x*phi(1-p+p*a*u)/a, obtained by weighting each open child's independent subtree by its factor a. Its mean is x*p*v, so its expected even population is 1/(1-(x*p*v)^2). It follows that the unnormalized even-size correction is a/Delta, as in U. The known boundary expectation is V and summing block generations gives U/(1-V), including the continuous values U(0)=V(0)=0 by finite mean. At the critical point p_c<m^-2 both denominators are positive and f<=1-p^2<1. Differentiating the fixed point gives f'<0 and v'<=0; at fixed v the derivative of H=x^2*v/Delta is -2*x*v*(1-p*x^3*v^2)/Delta^2<0 because p*m^2<=1, whereas its v derivative is positive. Thus V'>0 is finite without a second-moment assumption. U>=p from the root short edge, and an ordinary first-order expansion gives the displayed positive finite residue. This does not establish an original-root or quenched formula.

## originality

FAIL

The prior primary paper does not print this susceptibility or its amplitude. Nevertheless, in the identical finite-mean model and identical augmented cluster it already gives the independent marked blocks, the parity gate, the explicit offspring mean V and the differentiable transverse critical equation. Applying the ordinary progeny sum and reweighting its given thinned tree by the already used total-size factor (1-p)^N gives the exact numerator by a geometric sum over even generations. This is mechanical implication of the exact claim, not merely a shared method, inaccessible possible overlap, or overlap on the deterministic exponent alone.

## value

FAIL

The mean cluster size and its amplitude are natural and potentially useful quantities, but this submission as a distinct finding adds only the routine total-progeny and weighted even-generation evaluations to an existing exact block law and transverse critical equation. The finite-mean scope comes from the same prior block law and its interior pgf fixed point. No independent nonmechanical invariant, broader coverage, or new estimate is demonstrated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
