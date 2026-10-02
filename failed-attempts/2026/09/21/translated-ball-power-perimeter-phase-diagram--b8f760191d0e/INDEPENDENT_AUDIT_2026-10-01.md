# Independent audit — 2026-10-01

## Final claim

The radial-power weighted perimeter of a translated Euclidean ball has the stated complete monotonicity and touching-sphere phase diagram in \(p\), including the flat Newton-shell family at \(p=2-n\) and the sharp finite/infinite threshold at \(p=1-n\).

## Correctness — PASS

The spherical-mean ODE gives the interior derivative sign from \(p(p+n-2)\), direct differentiation gives the exterior sign from \(p\), and the critical case is the Newton-shell identity. The touching-sphere beta integral has the claimed integrability threshold and gamma value. Independent numerical checks reproduce representative decreasing, hill-shaped, and critical profiles. The finite checks are corroborative only; the analytic ODE and integral argument prove the full parameter statement.

Checked sources:
- Chafaï, Matzke, Saff, Vu and Womersley, Potential Analysis 63 (2025), open full text; Proposition C.1 and Lemma C.3 give the exact radial Riesz potential of uniform sphere measure.
- Csató, Communications on Pure and Applied Analysis 17 (2018); local translated-ball variation threshold for perimeter density \(|x|^p\).
- Csató, Giovagnoli and Roy, arXiv:2608.19851 (2026); weighted perimeter translation context.
- Classical Newton-shell/mean-value theorem for the fundamental solution.

Residual risks:
- None.

## Originality — FAIL

Originality fails under the required implication standard. Chafaï--Matzke--Saff--Vu--Womersley already give the exact uniform-sphere Riesz potential as a piecewise hypergeometric function of the radius ratio for \(s<d-1\). Under the substitution \(p=-s\) and spherical symmetry, this is exactly the translated-sphere power average in the full finite-touching range \(p>1-n\), including the weighted-perimeter regime emphasized here. The current monotonicity phases are routine sign consequences of that exact profile together with the standard radial Laplacian identity; the critical flat case is explicitly classical Newton-shell potential theory. The remaining more singular \(p\le1-n\) endpoint divergence is a local integrability check, not a new theorem that rescues the final claim.

### Equivalent formulations

Searches:
- Chafaï et al. 2025, Lemma C.3 equations (2.10)--(2.11)
- Searches under Riesz spherical mean / translated sphere power average terminology

Evidence:
- Lemma C.3 writes the same radial sphere integral in closed hypergeometric form, piecewise for radius ratio below and above one.
- Replacing Riesz exponent \(s\) by \(-p\) gives the audited \(\Phi_{n,p}\) up to the source normalization.

Reasoning: The weighted-perimeter translation profile is an equivalent formulation of a classical uniform-sphere Riesz potential, so title/field differences do not create originality.

### Broader coverage

Searches:
- Chafaï et al. 2025 exact Riesz-potential formula
- Classical Newton shell theorem
- Csató 2018 local perimeter variation

Evidence:
- The Riesz formula covers the entire finite-touching power range \(p>1-n\).
- Newton shell supplies the critical flat family \(p=2-n\).
- Csató already identifies the local translation threshold in weighted-perimeter language.

Reasoning: Together these are broader or equivalent coverage of the scientifically distinctive parts of the phase diagram.

### Exact database or table

Searches:
- Chafaï et al. hypergeometric formula and Gauss/Funk--Hecke appendices
- Touching-sphere beta integral in the audited proof

Evidence:
- The prior exact formula determines the radial profile, and its boundary value is obtained by the same standard hypergeometric/beta machinery.

Reasoning: The current boundary gamma expression is an evaluation of the already-known exact integral, not an independent unknown invariant.

### Claim versus prior implication

Searches:
- Exact Riesz profile versus current derivative-sign phase diagram

Evidence:
- Once the exact same radial potential is known, the current ODE identity gives its sign phases mechanically; for the critical exponent the result is the classical harmonic mean-value law.
- The singular threshold \(p=1-n\) follows from the local sphere-density exponent at the touching point.

Reasoning: The final theorem is therefore a repackaging/corollary of prior exact potential theory plus elementary differentiation and integrability, even though the combined weighted-perimeter wording is convenient.

### Source inspections

- **Riesz Energy with a Radial External Field: When is the Equilibrium Support a Sphere?** (https://doi.org/10.1007/s11118-024-10186-w): trigger — Exact uniform-sphere Riesz potential, mathematically identical after \(p=-s\); material read — Open full-text Appendix C, especially Proposition C.1, Lemma C.3 and equations (2.10)--(2.11); method — Primary full-text inspection; assessment — Decisive implication-level coverage of the translated-sphere power profile in the finite-touching range.; evidence — Lemma C.3 gives the piecewise radial hypergeometric formula for the uniform-sphere Riesz potential for \(s<d-1\).

Checked sources:
- Chafaï, Matzke, Saff, Vu and Womersley, Potential Analysis 63 (2025), open full text; Proposition C.1 and Lemma C.3 give the exact radial Riesz potential of uniform sphere measure.
- Csató, Communications on Pure and Applied Analysis 17 (2018); local translated-ball variation threshold for perimeter density \(|x|^p\).
- Csató, Giovagnoli and Roy, arXiv:2608.19851 (2026); weighted perimeter translation context.
- Classical Newton-shell/mean-value theorem for the fundamental solution.

Residual risks:
- No correctness defect was found; rejection is due to implication-level prior coverage and lack of an independent remaining mathematical gap.

## Scientific value — FAIL

The weighted-perimeter interpretation is clear, but after the exact Riesz spherical profile, the local Csató threshold, and the classical Newton-shell identity are accounted for, the advertised phase diagram is a routine sign/integrability extraction rather than a remaining independently motivated mathematical gap. Correctness and useful exposition do not by themselves establish scientific value under the audit standard.

Checked sources:
- Chafaï, Matzke, Saff, Vu and Womersley, Potential Analysis 63 (2025), open full text; Proposition C.1 and Lemma C.3 give the exact radial Riesz potential of uniform sphere measure.
- Csató, Communications on Pure and Applied Analysis 17 (2018); local translated-ball variation threshold for perimeter density \(|x|^p\).
- Csató, Giovagnoli and Roy, arXiv:2608.19851 (2026); weighted perimeter translation context.
- Classical Newton-shell/mean-value theorem for the fundamental solution.

Residual risks:
- No correctness defect was found; rejection is due to implication-level prior coverage and lack of an independent remaining mathematical gap.

## Conclusion

The finding is scientifically rejected because all three axes must pass. Correctness evidence is preserved, but originality and scientific value fail under the implication-based comparison.
