# Self-review

## Correctness (C): PASS

For any reference trajectory satisfying the stated amplitude and order assumptions, the delayed-argument root is bracketed strictly between the current time and two mean delays into the past. The strictly increasing map \(H\) supplies existence, uniqueness and continuity of the implicit delay, and its inverse gives strict temporal order. The sign identity follows directly from comparing \(H(s)\) with \(H(d)=s\), including the zero case; it does not use a contraction. A finite-step comparison using both positive continuous delays establishes uniqueness of the whole state-and-delay solution. For the explicit eight-periodic witness, every join, the slope interval, the reference forcing, the rational iterates and the nonzero-measure nested-sign discrepancy are checked analytically. The standalone exact-rational checker independently verifies the indicated identities and local sign tests, but is not substituted for the general proof.

## Originality (O): PASS within inspected evidence

The closest primary work is Bolduc-St-Aubin, Subramanian and Krauskopf (2026), arXiv:2610.39281v1, Theorem 1.1 and Sections 3–6. It requires a two-sided Lipschitz contraction and gives all-nesting as well as implicit coincidence. Its Section 6 identifies the noncontracting regime as an open direction; the current result replaces that contraction with monotonicity of \(H\), for the implicit branch only. This is a strict extension: the explicit reference has \(\operatorname{Lip}(g)=2\), whereas the response is \(\Psi(u)=u\); the published two-sided hypothesis fails.

The published result *Sharp history-slope threshold for invisible and oscillating nested delays* supplies a prior local example of nested cycling despite a unique implicit delay. It does not contain a general global order criterion. The related *Sharp universal temporal-order boundary for finite nested state-dependent delays* concerns finite nesting within the contraction regime, not implicit invisibility beyond it. Walther's 2009 paper studies algebraic delay equations and increasing delayed arguments in a differentiable white-blood-cell model; those known monotonicity ideas are not claimed as new here. The model-specific sign-preservation implication, its global uniqueness and the noncontractive periodic separation are the contribution. The smooth ENSO and smooth feedback papers address other dynamical settings. Risk remains from specialized prior algebraic-delay work using equivalent language; the searches cannot certify worldwide novelty.

## Mathematical value (V): PASS

The precise gap is whether an implicit delayed relay can remain dynamically invisible when a nested-delay contraction fails. A complete global sufficient criterion provides the answer for a large class: negative slopes need a bound, while large positive forcing slopes are permitted. Exact separation from a nonconvergent nested solver matters because the latter can sample a different relay sign even though the implicit feedback is uniquely and globally meaningful. The theorem is a structural characterization for the implicit branch, not a routine isolated parameter substitution. It does not claim the corresponding result for a smooth switch, every nonmonotone delay, or a physical sinusoidal forcing.

## Sources and remaining limitations

Full relevant text or sections inspected: arXiv:2610.39281v1 (theorem, delay-iteration lemma, proof and outlook), two relevant published mathematical result statements, and Walther (2009, introduction and temporal-order sections). Keane et al. (2019) was inspected for its model and analysis context; Humphries et al. (2021) and Walther (2023) were assessed using available abstracts. An older undiscovered equivalent remains possible, as does a broader theorem in uninspected material. Only the general implicit-branch theorem and its explicit separation example are asserted.

Self-review: passed. Independent audit: not yet performed.
