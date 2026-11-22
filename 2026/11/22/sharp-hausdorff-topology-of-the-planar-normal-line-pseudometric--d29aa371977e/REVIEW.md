# Scientific review

## Correctness — PASS

The claim is a two-sided metric comparison on all equal-perimeter planar convex bodies, with two distinct optimality statements. Normal-line offset equals the derivative of the support function because the supporting point is \(h u+h' u'\), so the pseudometric is half the \(L^1\) derivative difference. The key lemma is reconstructed for a periodic Lipschitz function with measure-valued second derivative: a forward difference plus a triangular integral remainder yields \(\|f'\|_1\le4\pi\|f\|_\infty/a+a\|f''\|_{\mathrm{TV}}/2\), with optimum \(a=\sqrt{8\pi\|f\|_\infty/\|f''\|_{\mathrm{TV}}}\). Convex support curvature positivity gives \(\|f''\|_{\mathrm{TV}}\le P(K)+P(L)+2\pi d_H\). The equal-perimeter support difference has zero integral; periodic total variation then proves the strict inverse bound. The smooth bump witness makes the inverse constant tend to one, and the explicit high-frequency support family has curvature radius at least \(3/8\), constant perimeter \(3\pi/2\), and exact distances \(e_n\) and \(2ne_n\), proving the upper exponent sharp. All assumptions and boundaries were checked. A standalone script was run successfully and re-executed from the actual decoded package; its finite tests are supplementary, not substitutes for the proof.

## Originality — PASS, with residual priority risk

The primary 2023 source [1] introduces and studies the normal-line pseudometric but proves no Hausdorff comparison, fixed-perimeter metric theorem, inverse sharp constant, or sharp high-frequency counterexample. Hug–Schneider [2] prove a half-Hölder bound for support measures in the bounded-Lipschitz **measure metric**, not this \(L^1\) normal-line pseudometric; their implication does not directly contain the new assertion. Allemann–Hungerbühler–Wasem [3] and Ftouhi–Zuazua [4] give classical support identities underlying the proof, not the combined result. Indexed geometric records and the accessible geometry ledger were checked by source, formulas and aliases. In particular, a previously derived coaxial-ellipse distance evaluation is strictly a restricted four-parameter distance computation and cannot imply a uniform theorem for all convex bodies or high-frequency sharpness. A classical interpolation formulation with different terminology could have appeared elsewhere; the searches do not prove uniqueness.

## Mathematical value — PASS

The original normal-line distance is a pseudometric because outer parallel bodies are not separated. The theorem identifies a natural geometric normalization (fixed perimeter) that restores definiteness, proves that the resulting metric has precisely the Hausdorff topology, and quantifies the optimal uniform Hölder order. The strict inverse inequality, optimal inverse constant and smooth fixed-perimeter exponent obstruction are independent boundary phenomena; they clarify what approximation in normal-line distance does and does not control. This is a motivated metric-structure result, not an arbitrary finite table or a routine extension of the earlier ellipse calculation. The proof uses familiar analytic tools but their synthesis establishes a globally quantified shape-theoretic statement not found in the inspected primary sources.

## Closest literature and limitations

[1] Akopyan–Glazyrin, *On the total perimeter of disjoint convex bodies*, arXiv:2308.16340v1, §§2–3, defines \(d_N\) and derives elementary pseudometric properties.

[2] Hug–Schneider, *Hölder continuity for support measures of convex bodies*, arXiv:1501.06214, §§1, 3–4, concerns bounded-Lipschitz support-measure distances, with a sharp half-Hölder exponent for that different problem.

[3] Allemann–Hungerbühler–Wasem, *Equilibria of Plane Convex Bodies*, 2021, §2, supplies support parametrization and curvature identities.

[4] Ftouhi–Zuazua, *Optimal Design of Sensors via Geometric Criteria*, 2023, §2, states the Hausdorff support formula and positive-curvature support characterization.

The numerical constant in the forward estimate is not claimed sharp. No higher-dimensional statement and no reverse Hausdorff bound without fixed perimeter are claimed. Abstract interpolation precedents may yield alternative proofs. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
