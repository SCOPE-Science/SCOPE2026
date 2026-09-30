# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof separates two sources of relative generators.

First, projection to the right factor forces at least \(\operatorname{rank}(R:G)\) generators whose right components are nonunits. Second, any word ending with unit right component uses only unit right components, because in a finite monoid a product is a unit only if every factor is a unit. Base generation therefore has to be supplied independently by relative generators with unit right component.

For those base generators, singular support is monotone under multiplication:
\[
\sigma((a,g)(b,h))=\sigma(a)\cup\sigma(b)g^{-1}.
\]
Thus a generator with support in one \(G\)-orbit cannot create a singleton singularity in another orbit, and support of size greater than one cannot be cancelled down to one. Each \(G\)-orbit therefore needs a full relative generating set for \(S\) modulo \(H\), giving the lower bound \(o_G(X)\operatorname{rank}(S:H)\). The matching construction supplies exactly that many coordinate-local generators, plus a relative generating set for \(R\).

The argument was stress-tested against the edge cases \(S=H\), \(R=G\), and transitive \(G\), and against the distinction between transitivity of \(R\) and transitivity of \(G\). The explicit 48-element counterexample was also exhaustively enumerated by the published verification script; its relative rank is \(3\), while the transitivity-only bound is \(2\).

The iterated formula follows from the one-step theorem and the elementary orbit identity
\[
o_{W_i}(\Omega_i)=\prod_{j=1}^i o_{G_j}(X_j).
\]
No step uses transitivity of the whole monoids.

## Originality

**PASS, to the best of our knowledge.**

The full HTML of arXiv:2609.20521v1 was inspected at its relevant statements and proofs. Its Lemma 3.2 uses transitivity of \(R\) to move a single base generator between coordinates, although only the unit group can be used in a word whose right component returns to the identity. The paper then propagates that upper bound through Lemma 3.4 and combines it with a lower bound in Lemma 3.8. The exact unit-orbit formula above is not stated there.

Targeted searches for relative rank, wreath products, transformation monoids, groups of units, and orbit decompositions located Araújo–Schneider (2009), which treats the special full-transformation wreath-product setting where the relevant symmetric unit group is transitive, and Castillo-Ramirez–Ruiz-Medina (2023), which studies relative rank for finite \(G\)-set endomorphism monoids. No located source states
\[
\operatorname{rank}(S\wr_XR:H\wr_XG)
=
\operatorname{rank}(R:G)+o_G(X)\operatorname{rank}(S:H)
\]
or the resulting iterated weighted sum.

Lu's 2026 thesis is closely related and its repository metadata and relevant transformation-semigroup chapter material were consulted, but it was not exhaustively checked line-by-line for every possible equivalent formulation. Meldrum's 1995 monograph *Wreath Products of Groups and Semigroups*, a broad foundational source cited by Lu, was not exhaustively inspected. These are the principal residual originality risks. Because the support argument is elementary once the unit-orbit obstruction is noticed, equivalent folklore or an implicit older statement cannot be ruled out.

The originality claim does not include the definition of transformation wreath products, their unit groups, the finite-monoid unit-factor fact, or known rank calculations for full transformation monoids.

## Value

**PASS.**

The result gives an exact formula in the general finite setting, identifies the precise missing hypothesis behind a recent upper-bound argument, provides small explicit counterexamples under both the one-step and iterated stated hypotheses, and simultaneously explains why the recent paper's principal full-transformation/symmetric specialization survives. The iterated weighted formula replaces a false unweighted expression by a computable invariant determined by unit-group orbit counts.

## Limitations

The theorem is finite. Infinite monoids can have one-sided invertibility phenomena that invalidate the support argument, so no infinite analogue is asserted.

The explicit computation is verification evidence for the small counterexample only; the general theorem rests on the proof above.

No independent validation or independent audit is claimed.
