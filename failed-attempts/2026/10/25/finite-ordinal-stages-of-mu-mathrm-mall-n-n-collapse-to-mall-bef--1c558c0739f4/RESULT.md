# Finite ordinal stages of \(\mu\mathrm{MALL}_{n,n}\) collapse to MALL before the first infinite branching level

## Finding

For every finite ordinal \(n<\omega\), the ordinal-indexed fixed-point proof system \(\mu\mathrm{MALL}_{n,n}\) has an effective finite translation to ordinary MALL preserving provability, uniformly in \(n\); hence the combined finite-stage theoremhood problem is decidable. At the first infinite stage \(\alpha=\omega\), theoremhood is \(\Sigma^0_{\omega^{\omega^\omega}}\)-complete under Turing reductions.

The finite-stage assertion follows from a uniform elimination of the ordinal-indexed fixed-point rules. It identifies the first infinite ordinal as the point where the finite elimination procedure no longer applies.

## Assumptions and scope

Work in the multiplicative-additive fragment of linear logic with least and greatest fixed points, using the ordinal-indexed proof systems \(\mu\mathrm{MALL}_{\alpha,\alpha}\) defined by Das and Pshenitsyn. For each fixed-point occurrence, its annotation is a finite ordinal \(\beta\le n\) when the ambient stage is \(n<\omega\). Fixed-point variables occur positively, as in the source system. Provability means derivability in the stated sequent calculus; no complexity bound on the finite-stage decision procedure is claimed.

## Proof

For a fixed-point body \(A(x)\), first translate its proper fixed-point subformulas recursively, leaving the free variable \(x\) unchanged; call the resulting MALL body \(\widehat A(x)\). Set \(L_0(A)=0\) and \(G_0(A)=\top\). For \(0<\beta<\omega\), put

\[
L_\beta(A)=\bigoplus_{\gamma<\beta} \widehat A[L_\gamma(A)/x],
\qquad
G_\beta(A)=\mathbin{\&}_{\gamma<\beta} \widehat A[G_\gamma(A)/x].
\]

The finite indexed connectives are parenthesized in a fixed order, and substitutions are capture-avoiding. Because \(\beta\) is finite and every recursive reference on the same binder uses \(\gamma<\beta\), this translation terminates and produces an ordinary MALL formula.

The rule for \(\mu^\beta x.A\) has one premise \(\Gamma,A(\mu^\gamma x.A)\) for a chosen \(\gamma<\beta\). This matches the finite additive-disjunction rule for \(L_\beta(A)\): a proof selects one summand. The rule for \(\nu^\beta x.A\) has a premise for every \(\gamma<\beta\), matching additive conjunction over the finite family in \(G_\beta(A)\). At stage zero the translations are exactly the MALL units. The translation also respects duality, since \(\oplus\) and \(\mathbin{\&}\) are dual and \(\mu\) and \(\nu\) are dual. Induction over the finite annotations and formula structure therefore translates derivations in either direction, preserving provability.

The construction is uniform in the input numeral \(n\): all finite indexed connectives and recursive substitutions can be generated effectively. Cut-free MALL proof search terminates, since each rule reduces the principal formula to proper subformulas, the branching at every node is finite, and the search depth is bounded by formula complexity. Decide the original sequent by translating it and running this MALL decision procedure. Hence the combined problem over all finite \(n\) is decidable.

For the contrast at the boundary, Das and Pshenitsyn prove that for computable \(\alpha\ge\omega\), theoremhood in \(\mu\mathrm{MALL}_{\alpha,\alpha}\) is \(\Sigma^0_{\omega^{\alpha^\omega}}\)-complete under Turing reductions (Theorem 2.8). Substituting \(\alpha=\omega\) gives the stated level \(\Sigma^0_{\omega^{\omega^\omega}}\). At this stage the greatest-fixed-point rule has infinitely many premises, so this finite-family translation no longer applies.

## Verification

The proof was checked against the exact rule shapes for the ordinal-indexed system: a single chosen lower approximant for each least-fixed-point rule, and all lower approximants for each greatest-fixed-point rule. The translation is finite precisely when every annotation is finite. The MALL decision step uses ordinary cut-free proof search, not an infinite proof enumeration. The complexity statement at \(\alpha=\omega\) is a specialization of the cited theorem, not a newly proved lower bound.

## Relationship to prior work

Das and Pshenitsyn's 2026 paper introduces the ordinal-indexed systems, explains their approximant reading, and establishes the hyperarithmetical-completeness result for \(\alpha\ge\omega\). The finite-stage collapse is isolated here as the complementary boundary statement. Das, De, and Saurin's 2023 paper studies the comparison of non-wellfounded and \(\omega\)-branching systems, including \(\mu\mathrm{MALL}_{\omega,\omega}\); its scope is different from the finite-ordinal elimination proved here. Targeted literature searches found no exact statement of this uniform finite-stage collapse.

## Limitations

No optimal time or space complexity is established for the finite-stage algorithm, and no claim is made about the complexity of a combined encoding that permits genuinely infinite ordinal annotations. The finite-stage result is an elementary proof-theoretic boundary consequence; its status as a separately publishable novelty is not established. Independent audit has not been performed.

## References

1. A. Das and T. Pshenitsyn, “Wider systems for linear logic with fixed points: proof theory and complexity,” arXiv:2602.10280, first submitted 10 February 2026; see the ordinal-indexed rules and approximant reading in Section 2 and Theorem 2.8. https://arxiv.org/abs/2602.10280
2. A. Das, A. De, and A. Saurin, “Comparing Infinitary Systems for Linear Logic with Fixed Points,” LIPIcs FSTTCS 2023, Article 40, DOI: 10.4230/LIPIcs.FSTTCS.2023.40. https://doi.org/10.4230/LIPIcs.FSTTCS.2023.40
