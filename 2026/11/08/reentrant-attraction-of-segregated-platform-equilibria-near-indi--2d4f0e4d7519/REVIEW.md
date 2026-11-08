# Self-review

**Final claim assessed:** Reentrant local exponential stability of the two segregated equilibria in the two-dimensional counterfactual-learning platform-choice model, with a single critical exploration strength \(\beta_*\) and exactly two transverse stability crossings when \(\beta>\beta_*\).

## Correctness — PASS

The equilibrium parameterization follows from the original model's softmax and platform reward equations. The monotone function \(\operatorname{artanh}b/b\) proves branch existence and uniqueness; the unrestricted two-dimensional Jacobian has one strictly negative longitudinal eigenvalue and the transverse eigenvalue \(\alpha[\beta\mu b(1-b^2)-1]\). The sign of the latter is controlled by the function \(B(b)\), whose derivative has a numerator with a strictly positive derivative and opposite endpoint signs. These analytic steps prove the number and order of stability transitions; the formulae do not extrapolate numerical results into infinite proofs. The separately reconstructed original vector field and finite-difference Jacobian agree with the analytic eigenvalues, including the renewed stability at \(\mu=0.8745\). Numerical thresholds are approximate evaluations of exact implicit definitions.

## Originality — PASS, with identified residual risk

The motivating article [1] provides the governing model and reports the first segregation stability loss near \(\mu=0.79\) at \(\beta=8\), followed by a region supposedly dominated only by integrated mega-platforms through \(\mu=0.875\). Direct full-text comparison of Eqs. (9)–(14), the Figure 9 discussion and the described coarse sampling reveals no claim of a second stable segregation window or a sharp exploration-parameter classification. The present statement is incompatible with the source's all-interval 'only stable' assertion for that reduced equation, rather than a restatement of it. Banisch and Olbrich's earlier social-feedback theory [2] addresses opinion polarization on fixed interpersonal networks and does not imply these two-platform transverse eigenvalues. The closest identified published research-record results address different nonlinear games or dynamics; they have no reduction yielding the claimed parameter curve. The source-linked supplemental PDF could not be read; it is a specific unresolved originality risk. A literature search cannot establish absolute uniqueness.

## Mathematical value — PASS

The result repairs a qualitative stability map in a directly studied social-feedback model by proving that segregation **returns** immediately before the uniform indifference threshold, rather than disappearing permanently when the mega-platform regime begins. The return window is only approximately \(0.0009012575\) wide at the source's \(\beta=8\), explaining why a grid with \(0.005\) increments would miss it. More generally, the unique critical \(\beta_*\) proves precisely when reentrant behavior can arise. This is a structural, parameter-wide phenomenon of the model, not a change of notation or an arbitrary numerical slice.

## Closest source and limits

[1] Banisch, Jacob, Willaert and Olbrich, *The social dilemma of online segregation: A dynamical model of platform choice*, first published March 24, 2026, https://doi.org/10.1177/10434631261428850, Eqs. (9)–(14) and Figure 9 discussion.

[2] Banisch and Olbrich, *Opinion polarization by learning from social feedback*, first published October 10, 2018, https://doi.org/10.1080/0022250X.2018.1517761.

The conclusion is local to the two-dimensional counterfactual ODE. The frequency-weighted four-dimensional original model and agent-based version remain outside the proved scope. At the transverse eigenvalue-zero points no nonlinear stability determination is made. The source's online supplemental PDF was not accessible; an independent audit has not been done.

Self-review: passed. Independent audit: not yet performed.
