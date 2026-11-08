# The 4–12–60 unary algebra of bi-intuitionistic rooted stars

## Finding
For each integer \(m\geq 0\), let \(P_m\) be the finite poset with one least point \(r\) and \(m\) incomparable maximal points. Let \(b_m\) denote the number of equivalence classes of formulas in **one propositional letter** \(p\), with connectives \(\bot,\top,\wedge,\vee,\to,\prec\), where two formulas are identified precisely when they have the same truth set for **every upset valuation** on the fixed frame \(P_m\). Under the standard bi-intuitionistic interpretation of \(\prec\) as co-implication,
\[
\boxed{b_0=4,\qquad b_1=12,\qquad b_m=60\quad(m\geq2).}
\]
Thus two incomparable successors are both necessary and sufficient for the stabilization of the entire one-letter formula algebra. The proof supplies explicit uniform normal forms realizing all classes, not just an upper bound or a finite census.

## Assumptions and scope
Write \(L=\{\ell_1,\ldots,\ell_m\}\), \(W=L\cup\{r\}\), and \(r\leq\ell_i\) for all \(i\). The upsets are \(W\) and all subsets of \(L\), including \(\varnothing\); for \(m=0\), they are just \(\varnothing,W\). Each valuation maps \(p\) to an upset \(S\). Formulas are interpreted as upsets, with intersection and union for conjunction and disjunction and
\[
 A\to B=\{w:\forall v\geq w\;(v\in A\Rightarrow v\in B)\},
 \qquad A\prec B=\{w:\exists v\leq w\;(v\in A\wedge v\notin B)\}.
\]
The equivalence relation is *fixed-frame, all-valuation* equivalence, not derivability in unrestricted bi-intuitionistic logic. Leaves are labelled only to define the fixed frame; formulas do not name them. We use \(\neg\alpha=(\alpha\to\bot)\) and \(C(\alpha)=(\top\prec\alpha)\).

## Proof
**1. All possible outputs.** For \(S=\varnothing\) or \(S=W\), the input to every formula is a constant upset. The two-element subalgebra \(\{\varnothing,W\}\) is closed under all six operations, so a formula produces only \(\varnothing\) or \(W\) in each case. For \(S=L\), the subgroup of automorphisms permuting the leaves fixes the valuation, and every output upset is either \(\varnothing,L,W\). If \(m\geq2\) and \(S\) is a proper nonempty subset of \(L\), the automorphisms preserving \(S\) permute the two leaf types transitively. Therefore any formula's truth set belongs to \(\{\varnothing,S,L\setminus S,L,W\}\). These arguments apply to **all** formulas, not merely formulas of bounded depth. They give \(b_0\leq4\), \(b_1\leq 2\cdot 2\cdot 3=12\), and \(b_m\leq2\cdot2\cdot3\cdot5=60\) for \(m\geq2\).

**2. A global test from co-implication.** On any rooted star, if \(A\) is an upset then
\[
 C(A)=\uparrow(W\setminus A)=
 \begin{cases}\varnothing,&A=W,\\W,&A\neq W.\end{cases}
\]
Indeed, a proper upset omits the root, and the upward closure of the root is all of \(W\). Because \(C(A)\) takes only the two Boolean values, \(\neg C(A)=W\) if and only if \(A=W\).

**3. Four exclusive valuation selectors.** Define the formulas
\[
 e_0=\neg C(\neg p),\quad
 e_1=\neg C(p),\quad
 e_L=\neg C(\neg\neg p)\wedge C(p),\quad
 e_M=C(\neg\neg p)\wedge C(\neg p).
\]
For \(S=\varnothing\), the truth sets of \(\neg p\) and \(\neg\neg p\) are \(W\) and \(\varnothing\), respectively. For \(S=W\) they are \(\varnothing,W\). For \(S=L\) they are \(\varnothing,W\). For a nonempty proper \(S\subset L\), they are \(L\setminus S,S\). Thus exactly one selector is true everywhere, depending respectively on \(S=\varnothing\), \(S=W\), \(S=L\), or \(\varnothing\subsetneq S\subsetneq L\); the other three selectors are false everywhere. In the degenerate cases \(m=0,1\), nonexistent valuation categories simply have zero selectors.

**4. Every allowed output is definable independently.** Select independently
\[
 a,b\in\{\bot,\top\},\quad
 c\in\{\bot,p,\top\},\quad
 d\in\{\bot,p,\neg p,p\vee\neg p,\top\}
\]
and form
\[
 \Psi_{a,b,c,d}=(e_0\wedge a)\vee(e_1\wedge b)
 \vee(e_L\wedge c)\vee(e_M\wedge d).
\]
The preceding selector calculation shows that at the four respective valuation types, the output choices are exactly \(2,2,3,5\), independently. In the mixed case, \(p,\neg p,p\vee\neg p\) denote \(S,L\setminus S,L\); the other two choices are \(\varnothing,W\). Since all four types exist when \(m\geq2\), the \(60\) tuples of choices give pairwise inequivalent formulas. When \(m=1\), the mixed type is absent, giving exactly \(12\) classes; when \(m=0\), only \(S=\varnothing\) and \(S=W\) exist, giving exactly \(4\). This meets the upper bounds and proves the theorem.

## Verification
The standalone Python file `checker.py` implements the interpretation in two separate ways: bitset upset operations and direct quantification over predecessor/successor worlds. It constructs all \(60\) normal forms, verifies their semantic equivalence computations for every upset valuation on \(P_m\) for \(0\leq m\leq5\), checks each selector against the proposed four-way valuation split, and independently closes the generated one-letter term algebra under its four binary operations for \(m=0,1,2\), obtaining \(4,12,60\). Run `python3 checker.py`. Its final output is `BIINT_ROOTED_STAR_UNARY_4_12_60_OK`. These finite checks confirm implementations and small cases; the proof above establishes every \(m\).

## Relationship to prior work
Tasiou's *Profinite bi-Heyting algebras* (2025) develops the representation of profinite bi-Heyting algebras by upsets of finite connected posets and in Example 4.4 explicitly studies the same rooted-star posets as an inverse system of bi-Esakia spaces. It neither counts the one-letter formula equivalence classes nor derives the four valuation selectors or the sharp stabilization at two leaves. Badia, Kowalski and Olkhovikov's work on definable classes in bi-intuitionistic logic (journal version 2025, arXiv version 2026) develops the model/frame-level definability theory; its results do not give this fixed-frame, one-letter term-function census. Martins and Moraschini (2024) consider local tabularity of bi-intermediate logics over trees and co-trees, not this particular finite quotient. All underlying Kripke semantics, double-Heyting algebra definitions, and general duality facts are prior mathematics.

## Limitations
The result concerns one propositional variable and a fixed rooted-star frame with arbitrary upset valuations. It does not count formulas with two or more variables, nor establish an unrestricted free-algebra cardinality or a classification for all finite posets. The exact numerical classification is proved, but the historical-priority comparison is limited to the accessible sources described above; equivalent older formulas or specialist algebraic tables cannot be ruled out by search alone. Independent external validation has not been carried out.

## References
1. L. Tasiou, *Profinite bi-Heyting algebras*, Algebra Universalis 86, article 16 (2025), published 2025-05-09, https://doi.org/10.1007/s00012-025-00892-w, especially Sections 2–4 and Example 4.4.
2. G. Badia, T. Kowalski, G. Olkhovikov, *Definable Classes of Models and Frames in Bi-intuitionistic Logic*, Journal of Applied Logics 12(5), 1125–1151 (2025), full preprint https://arxiv.org/abs/2607.18956, Sections 2, 4, 5.
3. M. Martins, T. Moraschini, *Local Tabularity Is Decidable for Bi-Intermediate Logics of Trees and of Co-Trees*, https://arxiv.org/abs/2409.14998, first posted 2024-09-23.
