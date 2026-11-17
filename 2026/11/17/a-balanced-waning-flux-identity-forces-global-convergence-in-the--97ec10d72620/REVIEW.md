# Self-review

**Claim assessed:** exact global convergence of the prevalence-driven SIRCm model on the balanced immune-escape surface, with the stated extinction threshold and sharp closure property. This is one combined structural dynamical theorem; equilibrium uniqueness is a supporting ingredient already available in prior work.

## Correctness — PASS

Equation (1) is obtained by adding the recovered equation to \((1-\sigma)\) times the cross-immune equation and substituting the population identity. In the balanced case, the residual term \((1-\sigma)(\sigma\delta-\gamma)(1+\varepsilon I)C\) vanishes exactly. Equation (2) follows by replacing \(R=U-(1-\sigma)C\). The one-dimensional equilibrium equation has a strictly increasing and a strictly decreasing side, which proves existence and uniqueness for \(\beta>\mu+\alpha\). Equation (6) follows by cancelling the mixed terms in the translated planar equations, with \(q=aU_*/I_*>0\). Properness at the extinction face and strictly negative Lyapunov derivative establish attraction without relying on numerical experiments. The stable scalar fiber transfers convergence to all four compartments. At and below threshold, direct differential inequalities imply extinction. The attached checker executed successfully on 2,400 consistency cases. Risk: proof applies only to the stated unforced, balanced, equal-feedback setting.

## Originality — PASS within inspected evidence

The full relevant arXiv HTML of [1] was inspected at model (1), the equilibrium/stability analysis (Sections 3–4), and the prevalence-driven appendix. It does not identify the balance factor, the mixed-entropy Lyapunov identity, or global attraction at all feedback strengths. The highly relevant full RESULT.md of [2] was read; it proves all-feedback equilibrium uniqueness but expressly excludes any local/global stability claim. The 2006 SIRC model [3] has fixed rather than infection-responsive rates, and the delay SIRS model [4] has a different phase space; neither is a statement covering the new theorem in the inspected records. Searches also covered alternative aggregate variables and global stability aliases. Residual risk: an unindexed or differently formulated global-Lyapunov theorem could imply this restricted case; complete historical priority is not certified.

## Mathematical value — PASS

The rate balance \(\gamma=\sigma\delta\) is exactly the cancellation locus of the aggregate immunity feedback and therefore is not a chosen numerical slice. The theorem converts a three-dimensional epidemiological flow into a globally controlled planar factor and gives a strict identity that excludes all intrinsic periodic endemic dynamics for every feedback gain, whereas the source had only numerically observed stability along an equal-feedback diagonal and could exhibit Hopf instabilities with another feedback mechanism. This is a meaningful structural limit on mutation-driven oscillations. Neither a general theorem off the balance surface nor an inference about observations is claimed.

## Closeness, scope, and residual priority risks

Closest records: [1], which develops the SIRCm models and numerical Hopf regions; [2], which already resolves equilibrium uniqueness, not global stability; [3] classical no-feedback SIRC; [4] delayed SIRS stability switches. The proof uses only smooth positive ODE dynamics on the biological simplex and is limited as specified in RESULT.md. Searches do not logically establish uniqueness of publication.

Self-review: passed. Independent audit: not yet performed.
