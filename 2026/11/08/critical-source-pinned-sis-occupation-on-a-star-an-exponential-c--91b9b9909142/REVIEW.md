# Self-review

## Correctness — PASS

The actual generator on the \(2(n+1)\) count states is explicitly specified. The two integral potentials satisfy a limiting two-state Poisson equation; uniform in-state-space Taylor control follows because the necessary weighted first and second derivatives are bounded. A uniform extinction-block argument gives first and second extinction moments of order \((\log n)^j\). The stopped-generator identity therefore determines the unforced hub occupation time. Harris graphical duality converts occupation into stationary hub infection probability exactly, and stationary leaf-birth/death balance gives the second observable. The proof covers all fixed positive \(c\), exact normalization \(\lambda_n=c/\sqrt n\), and both extreme leaf-count boundaries. The verifier independently reconstructs the full labeled chain for small sizes and compares the dual formula.

## Originality — PASS on examined evidence

Cator and Van Mieghem (2013) treat different finite-graph regularizations, not one pinned peripheral leaf. Cai, Wu and Holme (2021) do use the same permanently infected leaf, but Appendix B reports distributions at a fixed finite size/rate and a mean-replacement approximation, rather than the exact critical-window stationary exponential prefactor. Huang and Durrett (2018) study unforced star survival, not a forced-source stationary law. The Schwartz–Stone (2013) abstract describes a star SIS analysis but does not establish this pinned-leaf statement; its inaccessible full text remains a residual risk, not proof of uniqueness. Exact-result and equivalent-form searches of the examined literature and mathematical record did not identify a direct or dominating theorem. The search cannot prove global originality.

## Mathematical value — PASS

The pinned leaf and critical adjacency scale \(n^{-1/2}\) are structural, not arbitrary parameter choices. The result sharply quantifies a surprising intermittent regime: the hub's stationary infection probability vanishes, yet ordinary-leaf infection burden has a nonzero limiting mean with an explicit nonlinear exponential dependence on the coupling. This is useful as a solvable test case for localized SIS epidemics and for comparing pinned-source models with quasi-stationary regularizations. It supplies a precise finite-size scaling law and a new analytic occupation-time method rather than a routine finite computation.

## Sources and limitations

Primary full texts examined: Cator–Van Mieghem (2013), Cai–Wu–Holme (2021), and Huang–Durrett (2018). Schwartz–Stone (2013) abstract inspected; the complete paper was unavailable and remains a historical-priority caveat. Numerical verification is not an infinite proof. No independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
