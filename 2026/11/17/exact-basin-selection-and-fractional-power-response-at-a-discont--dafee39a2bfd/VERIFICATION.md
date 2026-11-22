---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

On (0,1/2), H(x)=a x(1−x), a=2(1−ε)∈(1,2) is increasing and maps lower half into itself; f(x)−x=a x(L−x) forces monotone convergence to L=(1−2ε)/(2(1−ε)). On upper half H(x)=b x(1−x), b=2(1+ε)∈(2,3), decreases and crosses the switch 1/2 once at c=(1+√(ε/(1+ε)))/2. For 1/2<x<c the image lies in (1/2,c), and c<x<1 maps lower immediately. Upper branch has U=(1+2ε)/(2(1+ε)). Factorization g(g(x))−x=−x(bx−b+1)[b²x²−b(b+1)x+b+1] has quadratic discriminant b²(b+1)(b−3)<0, excluding nonfixed period two; increasing g² iterates converge to U. Exceptional points 0,1 go to 0; 1/2 fixed by sign convention; c maps to 1/2, no nonfixed cycles. Uniform basin mass p=c−1/2; U−L=ε/(1−ε²); elementary two-atom moments yield claimed exact formula and Puiseux exponents. Independent symbolic and rational iteration tests corroborate boundaries/coefficients, not proof of all initial conditions.

## originality

PASS

Full original Morozov–Almutairi–Petrovskii–Lai 2023 open access publication defines exactly the density-change sign dispersal and studies long transients, especially μ near 3.7–4, including Appendix A trapping inequalities; it does not state the μ=2 all-state basin partition or fractional equilibrium selection moments. Tan–Chia 1993 original studied a sectional discontinuous logistic map but only its original abstract could be read, and equivalence of piecewise coefficients remains a concrete risk. Jiang et al 2024 studied a distinct fixed-threshold impulsive logistic model (figures show h=0.2 rather than the endogenous switch x=F(x)); its full paper was paywalled. Both full-text attempts via authorized Oxford access returned vpn_disconnected, so no false whole-document negative inference. Best-of-knowledge PASS, not historical proof of uniqueness.

## value

PASS

At a natural border-critical parameter where the logistic maximum coincides with the switching point, the basin develops an exactly computable square-root opening and a nonanalytic ε^(3/2) selected mean despite O(ε) equilibrium separation. This connects meaningful global attractor selection and nonsmooth critical scaling rather than merely solving a textbook fixed-point equation; it gives a complete phase portrait and exact uniform-selection law for the source population model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
