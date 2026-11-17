---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Direct arrowhead matrix multiplication gives (T_h)_{0i}=hw_iQ_{w_i}(h) and (T_h)_{ij}=h² w_iw_j[12-4h(S+w_i+w_j)+h²(S²+V+S(w_i+w_j)+w_i²+w_iw_j+w_j²)]/24. The leaf-leaf quadratic has negative discriminant, and the RK4 scalar polynomial is strictly positive on nonnegative arguments, guaranteeing diagonal positivity by symmetry. The expanded 9A_xC_x-4B_x² certificate is strictly positive using V-x²<= (S-x)², so each edge cubic decreases strictly and crosses zero once. Q_x-Q_y is a negative multiple of the always-positive leaf quadratic for x>y, making the largest spoke first. A stochastic irreducibility/Perron-Frobenius argument forces H<β/λmax for unequal weights, while equal weights yield equality. Independently checked exact rational star matrices and symbolic difference/discriminant identities.

## originality

FAIL

The October 25 bidirected-star theorem treats arbitrary positive inward rates a_i and outward rates b_i. Its specialization a_i=b_i=w_i has precisely the symmetric weighted star Laplacian and exactly the same coefficients: B=S, S1=V, S2=W, and g_i(h)=Q_{w_i}(h). Its unique first hub-edge zero theorem covers the principal iff positivity result. Ordering by largest w_i and strict spectral separation follow by elementary subtraction and Perron–Frobenius from that earlier exact formula; they do not leave a substantial new result.

## value

FAIL

The weighted-star exact positivity formula and loss of positivity before spectral stability on reversible nonuniform examples already follow from the broader bidirected-star theorem. Selecting the largest spoke and showing equality only at uniform weights require brief positive-polynomial and Perron–Frobenius arguments from that explicit known formula, without an independently substantial new invariant or classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
