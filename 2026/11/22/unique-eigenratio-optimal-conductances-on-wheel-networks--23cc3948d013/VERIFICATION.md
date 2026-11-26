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

On the complement of constants, the hub-versus-rim vector gives Rayleigh value (m+1) mean(a). Averaging the first real Fourier pair gives mean(a)+s_m mean(b), an upper bound on the gap; averaging the highest pair gives mean(a)+S_m mean(b), a lower bound on the maximum. In the even case the last pair is replaced by the alternating mode of norm squared m, giving the same comparison. Thus for all connected allocations the eigenratio is bounded below by the displayed max/min function of r=mean(b)/mean(a), with finite r because the hub is connected. The function strictly decreases up to m/S_m and then strictly increases: the middle rational branch has derivative (S_m-s_m)/(1+s_m r)^2 and this middle interval collapses at m=3. Constant within-class weights realize the Fourier spectrum and bound, including K4. At equality the mean ratio is forced and both first real Fourier vectors individually attain the minimum Rayleigh value, so the first complex mode is a gap eigenvector. At each rim vertex its eigen-equation has imaginary part (b_(j-1)-b_j)sin(2pi/m)=0 and then forces a_j constant via its real part. This rules out all asymmetric optima, not merely those found by averaging. For m>=7, s_m<1 makes the uniform-star gap bound sharp and strict unless the rim budget is zero, with spoke equality again forced. Dividing the two gap formulas yields the stated comparison, and s_m=4pi²/m²+O(m^-4), S_m=4+O(m^-2) give the asymptotics. Independently assembled incidence-based Laplacians agree for eight sizes and 48 sampled nonsymmetric budgets; for B=1, m=6 gives ratio 2.8, and m=7 gives ratio 3.35227951010077 and gap fraction 0.839949343506056. Replay: python /workspace/branches/reproduce_frozen.py (wheels section). Frozen checker and verification notes inspected, not executed. The all-conductance theorem is analytic; the comparison refers to the combinatorial Laplacian, not normalized or stochastic weights.

## originality

PASS

The established optimization problem and wheel Fourier formulas are not claimed as new. The supported distinction is the exact all-size wheel eigenratio optimum, uniqueness against asymmetric allocations at fixed total budget, and its quantitative separation from absolute gap optimization. The earlier gap formula is credited, and the generic eigenratio literature genuinely overlaps in feasible shapes.

## value

PASS

The wheel is a standard test graph with a universal hub and local cycle constraints. The result separates two natural spectral meanings of fast convergence on exactly the same feasible graph, showing a constant-order eigenratio benefit at an order-m cost in absolute decay rate in the regime studied. The exact allocation and equality rigidity make the tradeoff interpretable and usable, rather than reporting an isolated numerical improvement or a symmetric-candidate computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
