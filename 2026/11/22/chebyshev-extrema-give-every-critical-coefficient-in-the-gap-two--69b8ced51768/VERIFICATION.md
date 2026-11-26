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

The nonzero Jacobian-zero radius is R²=kc/(k+2); the extra singular point at zero for k>1 cannot be a root. Put n=k+2 and let G(θ)=exp(inθ)+(n/k)exp(−ikθ). The imaginary part satisfies k Im G=−2 sin³θ U'_k(cos θ), and the stationary-angle condition (k+1)sinθ cos((k+1)θ)=cosθ sin((k+1)θ) gives Re G=2U_k(cos θ)/k there. At the endpoints 0 and π the values are opposite, with only 0 giving a positive crossing; conjugation accounts for the lower half. The condition R^n G=1 gives exactly the displayed c_j. Rolle interlacing and oddness give (k−1)/2 positive interior heights, and the squared stationary condition gives |U_k(x)|⁻²=1−k(k+2)x²/(k+1)². It strictly separates them and bounds them by the endpoint height. The k=1 case has just the endpoint. The cited 2020 theorem applies since gcd(k,k+2)=1 and establishes the counts only between critical values. As a cross-check, G'(θ)=−2n sin((k+1)θ)exp(iθ); each positive stationary crossing is downward in imaginary part, and the positive cusp at zero crosses downward to third order. Thus as c increases and R^−n decreases, winding of G−R^−n drops by one at the first threshold and two at each later one, measuring the negative of the interior zero count. The signed total is n by the highest degree term, giving the claimed jumps. For odd k≥3 the nearest stationary point sits between the central zero and the adjacent zero at sin(π/(k+1)) in absolute value. The height identity bounds the smallest positive height by 1+O(k⁻²); the largest is k+1. Applying logarithms to the exact threshold formula and exponentiating gives both endpoint expansions and width as stated. The exact k=3 radical is correct; independent decimal evaluation in /workspace/independent_sanity.py gives 1.8946457081379976029… (the frozen display differs at its last shown digit). The supplied checker was inspected, not executed; finite diagnostics are not the proof.

## originality

PASS

The transition-count theorem, the Jacobian-circle crossing approach, and the first threshold are prior. The comparison supports the gap-two Chebyshev-extrema reduction, explicit and strictly ordered full list, and sharp aggregate width as the distinct contribution; neither an open-interval zero count nor a general geometric crossing criterion alone provides those conclusions.

## value

PASS

Gap two is the smallest gap allowing this nontrivial coprime odd-exponent sequence. The critical parameters locate genuine changes in the number of distinct roots; explicit locations, strict order, and a sharp overall width provide information not given by the number of transitions. The Chebyshev description is usable uniformly in the degree and improves the published worked example. The result does not claim to solve arbitrary gaps, or give the distinct root count at singular coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
