# Rado's Conjecture forces \(\mathfrak a\le\mathfrak d\)
## Finding

Let \(\mathfrak a\) be the least size of an infinite maximal almost disjoint family on \(\omega\), let \(\mathfrak d\) be the dominating number, and let \(\mathfrak c=2^{\aleph_0}\).

Then Rado's Conjecture implies
\[
\boxed{\mathfrak a\le\mathfrak d.}
\]

Consequently Rado's Conjecture rules out
\[
\mathfrak d<\mathfrak a.
\]

There is also a concrete consistency consequence. Relative to a strongly compact cardinal, there is a model of Rado's Conjecture satisfying
\[
\boxed{
\mathfrak a=\mathfrak d=\operatorname{non}(\mathcal N)=\omega_1
<
\operatorname{cov}(\mathcal N)=\mathfrak c=\omega_2.
}
\]

Thus the random-algebra cardinal-invariant pattern recently obtained under Rado's Conjecture automatically has the smallest possible value of the almost-disjointness number.

## Assumptions and scope

Rado's Conjecture is the compactness principle for specialness of trees of height \(\omega_1\) used in the cited set-theoretic literature.

The cardinal invariants are standard:
\[
\mathfrak a
=
\min\{|A|:A\subseteq[\omega]^\omega
\text{ is an infinite maximal almost disjoint family}\},
\]
and
\[
\mathfrak d
=
\min\{|D|:D\subseteq\omega^\omega
\text{ eventually dominates every member of }\omega^\omega\}.
\]

The symbols
\[
\operatorname{cov}(\mathcal N)
\quad\text{and}\quad
\operatorname{non}(\mathcal N)
\]
are the usual covering and uniformity numbers for the null ideal.

The implication
\[
\mathrm{RC}\Longrightarrow\mathfrak a\le\mathfrak d
\]
requires no large-cardinal hypothesis once Rado's Conjecture is assumed. The strongly compact cardinal is needed only for the relative consistency construction realizing the displayed pattern.

## Proof

Honzik proves that Rado's Conjecture implies
\[
2^\omega\le\omega_2,
\]
that is,
\[
\mathfrak c\le\omega_2.
\]

Pelayo-Gómez proves in ZFC that
\[
\mathfrak d=\omega_1
\Longrightarrow
\mathfrak a=\omega_1.
\]

He then records the immediate consequence
\[
\mathfrak c\le\omega_2
\Longrightarrow
\mathfrak a\le\mathfrak d.
\]

For completeness, the last step can be reconstructed directly from his theorem. Under
\[
\mathfrak c\le\omega_2,
\]
there are only two possibilities for \(\mathfrak d\).

If
\[
\mathfrak d=\omega_1,
\]
Pelayo-Gómez's theorem gives
\[
\mathfrak a=\omega_1=\mathfrak d.
\]

If
\[
\mathfrak d=\omega_2,
\]
then
\[
\mathfrak a\le\mathfrak c\le\omega_2=\mathfrak d.
\]

Therefore
\[
\mathfrak c\le\omega_2
\Longrightarrow
\mathfrak a\le\mathfrak d.
\]

Combining this with Honzik's consequence of Rado's Conjecture yields
\[
\mathrm{RC}\Longrightarrow\mathfrak a\le\mathfrak d.
\]

Hence
\[
\mathrm{RC}+\mathfrak d<\mathfrak a
\]
is inconsistent.

For the consistency statement, Honzik constructs, relative to a strongly compact cardinal, a model of Rado's Conjecture satisfying
\[
\mathfrak c=\omega_2,
\qquad
\mathfrak d=\omega_1,
\qquad
\operatorname{cov}(\mathcal N)=\omega_2,
\qquad
\operatorname{non}(\mathcal N)=\omega_1.
\]

Applying Pelayo-Gómez's theorem inside this model gives
\[
\mathfrak a=\omega_1.
\]

Substitution gives
\[
\mathfrak a=\mathfrak d=\operatorname{non}(\mathcal N)=\omega_1
<
\operatorname{cov}(\mathcal N)=\mathfrak c=\omega_2.
\]

## Verification

The two load-bearing source statements were independently checked.

Honzik's arXiv record, first posted on 28 June 2026, states both that Rado's Conjecture implies
\[
2^\omega\le\omega_2
\]
and that, relative to a strongly compact cardinal, Rado's Conjecture is consistent with
\[
2^\omega=\omega_2,\quad
\mathfrak d=\omega_1,\quad
\operatorname{cov}(\mathcal N)=\omega_2,\quad
\operatorname{non}(\mathcal N)=\omega_1.
\]

Pelayo-Gómez's arXiv record and primary text, first posted on 30 September 2026, prove
\[
\mathfrak d=\omega_1\Longrightarrow\mathfrak a=\omega_1
\]
and explicitly record the corollary
\[
\mathfrak c\le\omega_2\Longrightarrow\mathfrak a\le\mathfrak d.
\]

The deduction joining the two papers is purely logical; no finite experiment or computational evidence is used.

## Relationship to prior work

Honzik's work is explicitly motivated by determining cardinal-invariant patterns compatible with Rado's Conjecture. Its stated random-algebra pattern specifies
\[
\mathfrak d,\quad
\operatorname{cov}(\mathcal N),\quad
\operatorname{non}(\mathcal N),\quad
\mathfrak c,
\]
but its public abstract does not state a value of \(\mathfrak a\).

Pelayo-Gómez settles the long-standing question whether
\[
\mathfrak d=\omega_1
\]
can coexist with
\[
\mathfrak a>\omega_1,
\]
and derives the continuum-\(\omega_2\) inequality
\[
\mathfrak a\le\mathfrak d.
\]
His primary text contains no occurrence of Rado's Conjecture in the checked theorem and corollary discussion.

The present observation connects these two 2026 results. It converts Rado's continuum bound into a new global restriction on the pair
\[
(\mathfrak a,\mathfrak d),
\]
and completes Honzik's displayed random-algebra pattern by determining the missing invariant \(\mathfrak a\).

Targeted searches for Rado's Conjecture together with the almost-disjointness number, maximal almost disjoint families, and the inequality
\[
\mathfrak a\le\mathfrak d
\]
did not locate an equivalent published statement.

## Limitations

The relative consistency statement does not reduce the large-cardinal strength of Honzik's construction.

No claim is made that Rado's Conjecture determines \(\mathfrak a\) or \(\mathfrak d\) individually; it only forces their inequality.

Honzik's full paper text was not retrievable through the available primary-source route during this check. The exact forcing-pattern premises used here are stated in the arXiv abstract, but an uninspected passage in the body could conceivably mention \(\mathfrak a\). This leaves a residual literature risk for the model-specific completion, not for the correctness of the deduction.

## References

[1] Radek Honzik, “Rado's Conjecture and the random algebra,” arXiv:2606.29500v1, first posted 28 June 2026.

[2] José de Jesús Pelayo Gómez, “\(\mathfrak d=\omega_1\) implies \(\mathfrak a=\omega_1\),” arXiv:2610.00639v1, first posted 30 September 2026.
