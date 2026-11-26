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

For a connected admissible symmetric chain, L=I-P is positive definite on constants' orthogonal complement. The objective is the trace of the inverse there. For a nonzero symmetric direction D, writing B=A^(-1/2) D A^(-1/2) gives second derivative 2 tr(B A^(-1) B)>0. The compressed Laplacian identifies the full zero-row-sum matrix and hence every edge weight. A connected feasible walk exists, and along any approach to a disconnected walk the smallest nonconstant eigenvalue goes to zero and its reciprocal diverges. Thus compactness gives a connected optimum and strict convexity gives uniqueness before using symmetry. Conjugation by base automorphisms and the apex swap forces precisely one apex weight a and one base weight b, subject to 0<a≤1/n and 2a+db≤1. Laplacian modes are the apex difference (na), the constant-on-base contrast ((n+2)a), and the mean-zero base modes (2a+bη_i). Since η_i>0 for each such base mode, b must be maximal at each a. Then the base denominators are s_i+2a(1-s_i), 0<s_i≤2 by the regular undirected base spectrum. Terms with s_i≤1 contribute nonpositively to F'; for s_i>1 the denominator is at least one and the positive contribution is at most 2. The two apex terms dominate: F'≤-(1/n+1/(n+2))n²+2(n-1)=-4/(n+2). Both row classes are therefore saturated at the claimed weights; this is full uniqueness among symmetric kernels, not merely among orbit weights. For cycles the two spectra reduce to 1-(1-2/n)cosθ and (4-2cosθ)/n on the nonconstant base modes. Summing the Poisson expansion over roots of unity retains exactly indices divisible by n. The omitted k=0 term is n/2 in both evaluations; the apex contributions are 1+n/(n+2). For the optimum the geometric ratio simplifies to q_n=(√(n-1)-1)/(√(n-1)+1), giving exponentially small q_n^n in √n and leading term n^(3/2)/2. For maximum-degree weights the ratio is the fixed 2-√3 and the leading term is n²/(2√3). These give the displayed exact values and ratio, with equality at n=4, strict inequality for n≥5 by uniqueness, and no maximum-degree formula claimed at n=3. The inspected verify.py, with NumPy/SciPy requirements, was not executed; the recorded finite spectral and optimization diagnostics cannot prove unrestricted uniqueness or the asymptotics.

## originality

PASS

Qualified pass for the uniform saturation theorem across connected vertex- and edge-transitive bases with two nonadjacent apexes, and the exact cyclic comparison. Credit the existing constrained convex Kemeny framework and effective-resistance connection, the earlier demonstration of unbounded improvements over uniform conductances with another budget and family, and the SLEM theorem's shared spectral reduction on exactly these double cones. The same-day single-hub Kemeny wheel result is especially close in both proof and conclusions: saturation, Poisson resolvent and the square-root loss pattern are already there for that model. The double-cone theorem still needs the distinct two-apex modes, derivative bound for an arbitrary permitted base spectrum, and different constants. No same-day priority is inferred.

## value

PASS

The result gives the actual unique policy over all individual symmetric edge weights on a broad family, and shows that the saturation decision is independent of the base spectrum despite the spectral objective and the different fastest-mixing policies. For cycles it quantifies the growth of the performance penalty for a natural feasible maximum-degree policy with an explicit ratio, not merely a slight local improvement. The qualitative gap and argument have close precedents; the useful distinct output is the universal two-apex saturation and its quantified consequence under vertex row constraints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
