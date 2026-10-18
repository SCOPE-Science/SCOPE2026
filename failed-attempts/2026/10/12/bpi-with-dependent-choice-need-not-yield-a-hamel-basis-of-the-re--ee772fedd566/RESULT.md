# BPI with dependent choice need not yield a Hamel basis of the reals
## Finding

Assuming
\[
\operatorname{Con}(\mathrm{ZFC}),
\]
one has
\[
\operatorname{Con}\!\left(
\mathrm{ZF}+\mathrm{DC}+\mathrm{BPI}
+\text{“\(\mathbb R\) has no Hamel basis over \(\mathbb Q\)”}
\right).
\]

Thus the Boolean Prime Ideal Theorem does not imply the existence of a Hamel basis of \(\mathbb R\) over \(\mathbb Q\), even in the presence of Dependent Choice.

There is also an immediate Hahn--Banach consequence. Since BPI implies the Hahn--Banach theorem, the same model witnesses
\[
\operatorname{Con}\!\left(
\mathrm{ZF}+\mathrm{DC}+\mathrm{HB}
+\text{“\(\mathbb R\) has no Hamel basis over \(\mathbb Q\)”}
\right)
\]
relative to \(\operatorname{Con}(\mathrm{ZFC})\).

## Assumptions and scope

BPI denotes the Boolean Prime Ideal Theorem, equivalently the assertion that every Boolean algebra carries a prime ideal, or dually an ultrafilter.

DC denotes Dependent Choice.

For the source theorem, a Vitali set is a selector for the eventual-equality relation
\[
x\,E_0\,y
\quad\Longleftrightarrow\quad
(\exists n)(\forall m\ge n)\,x(m)=y(m)
\]
on \(2^\omega\): it meets every \(E_0\)-equivalence class in exactly one point.

A Hamel basis of \(\mathbb R\) over \(\mathbb Q\) is a subset \(B\subseteq\mathbb R\) such that every real has a unique finite \(\mathbb Q\)-linear combination representation using elements of \(B\).

The conclusion is a **relative consistency separation**. It does not assert that BPI proves the nonexistence of Hamel bases.

## Proof

Zapletal proves that if ZFC is consistent, then there is a model
\[
W\models
\mathrm{ZF}+\mathrm{DC}+\mathrm{BPI}
+\text{“there is no \(E_0\)-selector.”}
\]

The needed bridge from linear algebra to the selector statement is older. Larson and Zapletal prove, in \(\mathrm{ZF}+\mathrm{DC}\), that
\[
\text{“\(\mathbb R\) has a Hamel basis over \(\mathbb Q\)”}
\quad\Longrightarrow\quad
\text{“there is a total \(E_0\)-selector.”}
\]

Apply this implication inside \(W\). The hypothesis DC holds in \(W\), while the conclusion of the implication fails there. Hence \(W\) cannot contain a Hamel basis of \(\mathbb R\) over \(\mathbb Q\). Therefore
\[
W\models
\mathrm{ZF}+\mathrm{DC}+\mathrm{BPI}
+\text{“\(\mathbb R\) has no Hamel basis over \(\mathbb Q\).”}
\]

This proves the first consistency statement.

Finally, BPI implies the Hahn--Banach theorem. Therefore the same \(W\) also satisfies Hahn--Banach, giving the second displayed consistency statement.

## Verification

The source theorem was checked in the full text of Zapletal's preprint. The abstract and Theorem 1.1 state the relative consistency of
\[
\mathrm{ZF}+\mathrm{DC}+\mathrm{BPI}
+\text{“there is no Vitali set,”}
\]
and the paper explicitly defines a Vitali set as a selector for \(E_0\), the eventual-equality relation on \(2^\omega\). The construction of the model, the proof of DC, the proof of BPI, and the final no-selector argument were inspected.

The implication from a Hamel basis to an \(E_0\)-selector was checked in Larson and Zapletal's published work. Their Observation 3.13 states in \(\mathrm{ZF}+\mathrm{DC}\) that a Hamel basis for the reals, or a transcendence basis for the complexes, yields a total \(E_0\)-selector. The argument first extracts a selector for rational-difference classes and then uses the preceding transfer result for nonsmooth hyperfinite Borel equivalence relations.

No computation or finite experiment is involved. The proof is an implication comparison between two independently verified set-theoretic results.

## Relationship to prior work

Larson and Zapletal supplied the implication
\[
\text{Hamel basis}\Longrightarrow\text{\(E_0\)-selector}
\]
under \(\mathrm{ZF}+\mathrm{DC}\), but their result did not provide a model satisfying BPI with no \(E_0\)-selector.

Earlier work also produced models of \(\mathrm{ZF}+\mathrm{DC}\) without Vitali selectors and hence without Hamel bases, but this did not establish the additional Boolean Prime Ideal Theorem.

Zapletal's 2026 theorem supplies exactly the missing model: DC and BPI hold while the selector fails. The preprint does not state the Hamel-basis corollary. Combining it with the older implication therefore separates BPI from the existence of a Hamel basis over the reals.

A contemporary 2025 discussion of weak choice principles explicitly described it as unknown whether BPI, and therefore the standard ultrafilter route to Hahn--Banach, implies the existence of a Hamel basis of \(\mathbb R\). The present consequence resolves that implication negatively at the level of relative consistency.

## Limitations

The result is conditional on \(\operatorname{Con}(\mathrm{ZFC})\), exactly as in Zapletal's source theorem.

It is a nonimplication by relative consistency, not a theorem of ZF asserting that BPI is incompatible with Hamel bases. Other models can satisfy both.

The proof uses DC in the known bridge from a Hamel basis to a total \(E_0\)-selector. No claim is made here about the exact strength of the corresponding implication over bare ZF without DC.

The Hahn--Banach conclusion is only the consequence that one model has Hahn--Banach and no Hamel basis; it does not identify the weakest choice principle separating the two assertions.

## References

[1] Jindřich Zapletal, “The Boolean Prime Ideal Theorem and Vitali sets,” arXiv:2609.17087v1, first posted 15 September 2026.

[2] Paul B. Larson and Jindřich Zapletal, “Canonical Models for Fragments of the Axiom of Choice,” *Journal of Symbolic Logic* 82 (2017), no. 2, 489–509, DOI 10.1017/jsl.2017.29.

[3] Mariam Beriashvili and Ralf Schindler, “Some Pathological Sets of Reals and the Axiom of Choice,” *Fundamenta Mathematicae* 236 (2017), 163–179.
