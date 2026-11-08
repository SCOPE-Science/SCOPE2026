# Exact classicality profiles and signed positive fragments in minimal evidence logic

## Finding

Work in the propositional minimal logic of evidence and truth \(LET_F^-\), with connectives \(\wedge,\vee,\neg,\circ\) and the standard non-deterministic bivaluation semantics. Fix a propositional letter \(p\), and put \(a_0=p\) and \(a_{i+1}=\circ a_i\). For each \(k\ge1\), consider the length-\(k\) signed classicality profile
\[
(t_0,f_0,\ldots,t_{k-1},f_{k-1})
=\bigl(v(a_0),v(\neg a_0),\ldots,v(a_{k-1}),v(\neg a_{k-1})\bigr).
\]

**Exact profile theorem.** A bit string is such a profile for a global \(LET_F^-\) bivaluation if and only if
\[
\forall i\in\{0,\ldots,k-2\},\qquad t_{i+1}=1\ \Longrightarrow\ t_i\ne f_i.
\]
Consequently exactly \(4\cdot3^{k-1}\) signed profiles occur, for every \(k\ge1\). Their unsigned projection onto \((t_0,\ldots,t_{k-1})\) is the entire Boolean cube \(\{0,1\}^k\).

**Exact positive-fragment theorem.** Let \(\mathcal L_k^+\) be the nonempty formulas built from the *fixed atoms* \(a_0,\ldots,a_{k-1}\) by \(\wedge\) and \(\vee\) only (no extra occurrence of \(\neg\) or \(\circ\) outside those atoms). Under mutual \(LET_F^-\) consequence, \(\mathcal L_k^+\) is the free distributive lattice **without specified bounds** on these \(k\) generators. It contains exactly \(D(k)-2\) distinct equivalence classes, where \(D(k)\) is the Dedekind number (all monotone Boolean functions of \(k\) variables). For \(k=1,2,3,4,5\) these counts are respectively \(1,4,18,166,7579\).

**Complete signed-positive fragment theorem.** Now allow **both** signed atoms \(a_i\) and \(\neg a_i\), \(0\le i<k\), as indivisible generators for positive combinations by \(\wedge,\vee\). Let \(S_k\subseteq\{0,1\}^{2k}\) be the signed profiles satisfying the constraint above, ordered coordinatewise, and let \(0\) denote its all-zero element. For every \(k\ge2\), the resulting quotient lattice under mutual consequence is **exactly the lattice of all upward-closed subsets of the poset \(S_k\setminus\{0\}\)**, under union and intersection. Its number of classes is therefore the number of antichains in this explicit poset; for \(k=2,3\) the exact class counts are **83** and **70,806** respectively. For \(k=1\) the signed-positive fragment has four classes, the free unbounded distributive lattice on two generators. The count of 70,806 was obtained by an exact finite recursion, not a probabilistic estimate.

The unsigned positive-fragment inclusions for increasing \(k\) form a free distributive lattice on countably many generators inside the one-letter consequence algebra. In particular that algebra is not locally finite. Nonexistence of a finite deterministic characteristic matrix for the minimal logic was already noted in earlier literature and is **not** claimed here as new.

## Assumptions and scope

The semantic object is the full set \(\mathcal F\) of formulas on any denumerable nonempty set of letters containing \(p\). A bivaluation is a function \(v:\mathcal F\to\{0,1\}\) satisfying, for arbitrary formulas \(A,B\),
\[
\begin{aligned}
v(A\wedge B)&=v(A)\wedge v(B),\\
v(A\vee B)&=v(A)\vee v(B),\\
v(\neg(A\wedge B))&=v(\neg A)\vee v(\neg B),\\
v(\neg(A\vee B))&=v(\neg A)\wedge v(\neg B),\\
v(\neg\neg A)&=v(A),\\
v(\circ A)=1&\Longrightarrow v(A)\ne v(\neg A).
\end{aligned}
\]
Equivalently the last line says: whenever \(v(\circ A)=1\), \(v(A)=1\) iff \(v(\neg A)=0\). There is **no** converse requirement. The consequence relation is preservation of value \(1\) across all these bivaluations, as in Grandinetti and Rodrigues, Definition 3.2 and Theorem 3.3. In particular this theorem does **not** concern the stronger propagation logic \(LET_F^+\).

Here \(D(k)\) counts all monotone maps \(\{0,1\}^k\to\{0,1\}\) including the two constant maps. All assertions quantify over every positive integer \(k\); the finite checker below is corroborative, not the proof of that universal quantification.

## Proof

**1. Necessity of the local constraint.** By definition \(a_{i+1}=\circ a_i\). If \(t_{i+1}=v(\circ a_i)=1\), the final semantic clause implies \(v(a_i)\ne v(\neg a_i)\), which is \(t_i\ne f_i\). No other condition on the displayed pairs follows from the six semantic clauses.

**2. Global extension lemma (sufficiency).** We explicitly explain why every locally admissible finite profile extends to a bivaluation on *all* formulas, rather than just to a partial truth table. Give every formula a pair \((T(A),F(A))\), intended to mean \((v(A),v(\neg A))\). For each propositional letter freely choose its two bits; for \(p\), choose \((t_0,f_0)\). Extend by structural recursion:
\[
\begin{aligned}
(T(A\wedge B),F(A\wedge B))&=(T(A)\wedge T(B),F(A)\vee F(B)),\\
(T(A\vee B),F(A\vee B))&=(T(A)\vee T(B),F(A)\wedge F(B)),\\
(T(\neg A),F(\neg A))&=(F(A),T(A)).
\end{aligned}
\]
For the head \(\circ A\), freely choose a bit \(u_A\) if \(T(A)\ne F(A)\), and set \(u_A=0\) otherwise; independently choose a bit \(w_A\) for its negation. Set \((T(\circ A),F(\circ A))=(u_A,w_A)\). This recursive choice is possible at every finite syntactic depth. For the special heads \(\circ a_i=a_{i+1}\), prescribe \(u_{a_i}=t_{i+1}\) and \(w_{a_i}=f_{i+1}\) up to \(i=k-2\); admissibility makes every such choice legal. Elsewhere take, for example, zero for both discretionary bits. Then define \(v(A)=T(A)\). Structural recursion and the identity \(F(A)=T(\neg A)\), checked simultaneously by induction, establish all six bivaluation clauses. The prescribed profile is realized.

**3. Exact counting.** There are two choices for \(t_0\). Given \(t_i\), the pair \((f_i,t_{i+1})\) has exactly three choices: \(t_{i+1}=0\) permits both values of \(f_i\), and \(t_{i+1}=1\) permits only \(f_i=1-t_i\). There are \(k-1\) independent steps and two remaining choices of \(f_{k-1}\). Thus the total is \(2\cdot3^{k-1}\cdot2=4\cdot3^{k-1}\). Choosing \(f_i=1-t_i\) for every index allows *every* assignment of the positive bits, proving surjectivity onto \(\{0,1\}^k\).

**4. Exact lattice and entailment.** Each formula \(F\) in \(\mathcal L_k^+\) evaluates as a monotone Boolean function \(\widehat F(t_0,\ldots,t_{k-1})\) because \(\wedge\) and \(\vee\) obey their usual truth tables. If \(F,G\in\mathcal L_k^+\), then
\[
F\models_{LET_F^-}G\quad\Longleftrightarrow\quad
\forall z\in\{0,1\}^k,\ \widehat F(z)\le \widehat G(z).
\]
The forward implication uses the surjective unsigned projection of Step 3; the reverse uses truth-functionality of the two positive connectives. Hence mutual consequence is exactly equality of the monotone functions, and meets/joins are their pointwise Boolean meets/joins.

Every \(F\in\mathcal L_k^+\) gives a monotone Boolean function with \(\widehat F(0,\ldots,0)=0\) and \(\widehat F(1,\ldots,1)=1\), so neither constant function is present. Conversely any nonconstant monotone Boolean function is representable by the positive disjunctive normal form taking the disjunction over its inclusion-minimal true supports, with each support represented by a nonempty conjunction of distinct atoms. Thus *every* nonconstant monotone function occurs. The fragment is precisely the standard free (unbounded) distributive lattice on \(k\) generators, with size \(D(k)-2\).

**5. Signed-positive quotient and its exact order-ideal model.** Fix \(k\ge2\), let \(S_k\) be as stated, and name the \(2k\) signed atoms \(L_{2i}=a_i\), \(L_{2i+1}=\neg a_i\). The global extension lemma shows that **every** \(x\in S_k\) is realized by a full bivaluation. A positive formula in these signed atoms is monotone in the \(2k\) displayed bits and vanishes at the all-zero profile. Its truth set on \(S_k\) is therefore an upward-closed subset of \(X_k=S_k\setminus\{0\}\). Conversely let \(U\subseteq X_k\) be any upward-closed set. If \(U\ne\varnothing\), list its finitely many minimal profiles \(u\). For each such \(u\), form the nonempty conjunction of those \(L_j\) for which \(u_j=1\). Their disjunction is true at exactly the profiles \(x\in U\), because \(U\) is the union of the principal upsets generated by its minimal points. If \(U=\varnothing\), use the term \(a_0\wedge\neg a_0\wedge a_1\): a profile satisfying it would have \(t_1=t_0=f_0=1\), contradicting the local profile constraint. Thus **every** upset is definable, and semantic consequence between positive formulas is exactly inclusion between their truth sets, by global realizability. Meets and joins are intersections and unions. The correspondence is bijective and order-preserving. For \(k=1\), no nonempty positive formula realizes the empty truth set, while the other four upsets of the three-element punctured two-cube are realized, giving four equivalence classes.

For a finite poset, upsets are in bijection with antichains by taking minimal elements. This gives an exact cardinality specification for each \(k\). The checker implements the standard recurrence on an induced finite poset: for a selected element \(x\), an antichain either omits \(x\) or contains \(x\) and omits every element comparable with it. On the 11- and 35-element punctured profile posets this yields respectively \(83\) and \(70,806\) antichains. The recurrence is exhaustive and independent of any asymptotic extrapolation.

**6. Nested inclusions.** Under the natural inclusion of the first \(k\) terms into the first \(k+1\), equality and order are preserved by Step 4. Every finite positive expression in the countably many \(a_i\) belongs to some \(\mathcal L_k^+\), yielding their free distributive direct limit. Its cardinality is infinite because the generators are pairwise independent: for \(i\ne j\), a truth assignment making \(t_i=1,t_j=0\) separates them. This establishes the claimed local infinitude, but does not assert a finite *deterministic* matrix obstruction as a new result (that consequence was already stated by Coniglio and Rodrigues).

## Verification

The accompanying self-contained Python 3 checker, `checker.py`, enumerates all signed profiles of length \(k=1,\ldots,7\), verifies that each count is \(4\cdot3^{k-1}\), and verifies that every unsigned bit string is attained. It computes the exact antichain counts for signed-positive fragments at \(k=1,2,3\) using a finite-poset branching recurrence and cross-checks the count for \(k=2\) directly from all monotone four-variable Boolean functions. It enumerates all monotone Boolean functions for \(k\le4\), and computes \(D(5)=7581\) by comparable pairs of four-variable monotone functions, confirming fragment sizes \(1,4,18,166,7579\). Executing `python3 checker.py` returns the marker `LETF_LADDER_FINITE_CHECKS_OK`. The global extension lemma and the general count are mathematical proofs, not inferred from finite enumeration.

## Relationship to prior work

Grandinetti and Rodrigues (arXiv:2610.24203v1, 2026) define the exact minimal semantics used here and prove a cut-free sequent calculus and decision method. The inspected introduction, semantic clauses, and surrounding discussion concern proof theory rather than a complete finite-depth signed-ladder profile and positive-lattice count. Coniglio and Rodrigues (arXiv:2209.12337v1, 2022) already explain that earlier LET logics lack a single finite deterministic matrix, and construct a deterministic six-valued semantics only after adding propagation rules, yielding \(LET_F^+\). This established no-finite-matrix claim is not treated as a contribution. The classical Dedekind-number count of monotone Boolean functions is likewise known. The present specific content is the global extendibility of **every** local ladder profile, the exact factor \(4\cdot3^{k-1}\), and the complete signed-positive quotient as an explicit finite-poset upset lattice with nontrivial counts 83 and 70,806. The unsigned free-lattice count is a useful corollary, not the sole novelty.

## Limitations

Only finite prefixes of the iterated \(\circ\)-ladder and the fragments obtained by positive combinations of those signed or unsigned prefixes are classified. No classification of all one-letter formulas with arbitrary placements of \(\neg\) or \(\circ\) is claimed. The proof uses the nondeterministic semantics of \(LET_F^-\), not the propagation extension \(LET_F^+\). Priority for a formulation equivalent to these exact profile/lattice counts remains subject to specialist scrutiny; in particular the non-finite-matrix conclusion itself predates this result. No independent audit has been performed.

## References

1. N. Grandinetti and A. Rodrigues, *A Kleene-inspired sequent system for a minimal logic of evidence and truth*, arXiv:2610.24203v1 (first submitted 2026-10-16), Definition 3.2 and Theorem 3.3, https://arxiv.org/abs/2610.24203.
2. M. E. Coniglio and A. Rodrigues, *On six-valued logics of evidence and truth expanding Belnap-Dunn four-valued logic*, arXiv:2209.12337v1 (2022), Introduction and Section 2, https://arxiv.org/abs/2209.12337.
3. W. Carnielli, L. Frade, and A. Rodrigues, *Analytic proofs for logics of evidence and truth*, arXiv:2412.10588 (2024), https://arxiv.org/abs/2412.10588 (abstract consulted).
4. R. Dedekind, classical monotone-Boolean-function enumeration; modern sequence and values collected in *Dedekind Number*, MathWorld, https://mathworld.wolfram.com/DedekindNumber.html.
