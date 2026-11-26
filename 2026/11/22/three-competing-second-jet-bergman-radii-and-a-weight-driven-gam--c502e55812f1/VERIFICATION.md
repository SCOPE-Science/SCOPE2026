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

The disk involution and its reproducing-kernel cocycle give the weighted unitary; the order-three vanishing ideal at r is mapped to the one at zero, so the entire jet span maps to the first three orthogonal Taylor modes. Expanding (r−z)^n(1−rz)^{−(n+β)} gives exactly Q_j/j! times r^{n−j}; the monomial norms j!/(β)_j yield the displayed capture. A fresh symbolic calculation checks the full polynomial derivative identity for symbolic n and β, not just substituted integers. The Jacobi weights for Q_3 and Q_2 are v=x^{n−3}(1−x)^{β−1} and xv respectively. If S_2,S_3 are monic for v, then x times the monic quadratic for xv is S_3−[S_3(0)/S_2(0)]S_2. Evaluated at the three roots of S_3, its signs alternate by ordinary interlacing, so the two intervening roots are strict. The derivative is positive near zero and changes sign at each zero, giving exactly three interior peaks and two interior minima. The x=0 endpoint has capture zero (an endpoint minimum); the excluded x=1 endpoint has limit zero. Coefficient convergence under x=1−t/n and the gamma-ratio normalization give the locally uniform boundary limit; all possible global maximizers lie among the three Q_3 roots, which individually rescale to the three distinct Laguerre roots. A fresh exact rational certificate bisected the three β=2 root brackets and bounded exp(t) by a positive series and geometric remainder, reproducing the three stated disjoint height intervals. The replay /workspace/branches/replay_5.py checks these and both polynomial scalings. At large β the cubic in (t−β)/sqrt(β), after division by β^(3/2), tends to 3y−y³, and Stirling gives the stated Gaussian-polynomial heights. The central height wins strictly since e^(3/2)>4. Three continuous peak-value branches must share a global maximum somewhere when the unique winning index changes; the same strict endpoint rankings hold for all large n, giving the claimed finite-degree tie too. No uniqueness of the switch is proved or assumed.

## originality

PASS

The distinct claim is the second-jet weighted disk radial classification and, especially, the weight-driven change in the global winning Gamma peak, not the general use of repeated kernels or of classical polynomial scaling. The close first-jet result and the earlier Fock three-peak analogue are credited explicitly. Inaccessible primary text is a bounded residual risk, not an affirmative priority claim.

## value

PASS

For the natural one-site second-order measurement, the result reduces an unrestricted radial optimization to exactly three computable candidates for all n≥3 and all standard positive Bergman weights. The change of the maximizing asymptotic root, and its finite-degree consequence, explain why a single persistent choice of sampling shell cannot solve this problem. That structural switch is stronger than adding one Taylor coefficient or improving a single numerical example. The claim is restricted to the monomial and the same-site jet.

The dated certificate retains the supplied scientific assessment, sources and limitations.
