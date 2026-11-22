# Exact modal formula algebras and the last-leaf depth gap on reflexive stars

## Finding

Let \(F_k\) be the reflexive rooted star with a root \(r\) accessing itself and \(k\) leaves, each of which accesses only itself. Fix \(s\geq0\) ordinary Boolean propositional letters, put \(q=2^s\), and interpret formulas with Boolean connectives and the usual necessity operator \(\Box\), under **arbitrary** (not persistent) valuations on this fixed frame. Let \(A_d(s,k)\) count distinct truth-set operations induced by formulas of modal depth at most \(d\), where two formulas agree if their truth sets agree for every valuation on \(F_k\). Then, with \(k\geq0\),

\[
\begin{aligned}
A_0(s,k)&=2^q,\\
A_1(s,k)&=2^{\displaystyle q\sum_{j=0}^{\min(k,q-1)}\binom{q-1}{j}},\\
A_d(s,k)&=2^{\displaystyle q\sum_{j=1}^{\min(k,q)}\binom qj}\quad(d\geq2,\ k\geq1),\\
A_d(s,0)&=2^q\quad(d\geq0).
\end{aligned}
\]

Every formula on any such star is equivalent to a formula of depth at most two. The depth-two bound is **sharp if and only if** \(s\geq1\) and \(k\geq2\). With at least one letter, the full formula algebra and the \(s\)-letter frame-validity theory increase strictly when the leaf count passes through every \(k=0,1,\ldots,q\), and become unchanged for all \(k\geq q\). By contrast, depth-one expressivity stabilizes already at \(k=q-1\). In particular, with one letter the numbers of formula operations for \(k=0,1\), and \(k\geq2\) are respectively \(4,16,64\); the depth-one numbers are \(4,16,16\).

## Assumptions and scope

The world set is \(W=\{r,\ell_1,\ldots,\ell_k\}\), with \(rRr\), \(rR\ell_i\), and \(\ell_iR\ell_i\), and no other edges. This is a finite reflexive and transitive, but generally non-linear, \(\mathsf{S4}\) frame. A valuation assigns each letter an arbitrary subset of \(W\). An **atomic color** is one Boolean truth assignment to all \(s\) letters, so the set \(Q\) of colors has cardinality \(q\). Define \(\chi_c\) as the conjunction of all signed literals specifying color \(c\) (\(\top\) if \(s=0\)). Write \(\Diamond\varphi=\neg\Box\neg\varphi\).

For \(k\geq1\), record the root color \(a\in Q\) and the nonempty **set**, not multiset, \(S\subseteq Q\) of colors occurring among leaves, with \(1\leq|S|\leq\min(k,q)\). Formula operations are counted on the entire collection of valuations and points of the **fixed** frame; the claim is neither the number of full Boolean functions on the underlying powerset nor the cardinality of a free \(\mathsf{S4}\) algebra over arbitrary frames. Modal depth measures nested occurrences of \(\Box\) and \(\Diamond\).

## Proof

**1. Support invariance.** At a leaf \(\ell\), all modal operators act as identity: \(\Box\psi\) is equivalent there to \(\psi\). Thus truth at a leaf depends solely on its atomic color. By structural induction, truth of every formula at the root depends solely on \((a,S)\). For the modal step, the truth of \(\Box\psi\) at the root is the conjunction of \(\psi\)'s truth at the root, already determined by \((a,S)\), and its truth at one representative leaf of each color in \(S\). Repetitions of leaf colors cannot affect any formula.

**2. An exact depth-two observation of leaf support.** For every \(c\in Q\), define
\[
\theta_c=\Diamond(\chi_c\land\Box\chi_c).
\]
When \(S\neq\{a\}\), the root has some successor of color different from \(a\). Consequently the root itself cannot witness any \(\theta_c\), and \(r\models\theta_c\) if and only if \(c\in S\): a leaf of color \(c\) is precisely an accessible witness to \(\chi_c\land\Box\chi_c\). When \(S=\{a\}\), every world has color \(a\), and \(\theta_c\) holds precisely for \(c=a\).

A nonuniform root of color \(a\) is characterized by \(\chi_a\land\neg\Box\chi_a\), which is false at every leaf. Hence for every pair \((a,S)\) with \(S\neq\{a\}\) the depth-two formula
\[
\rho_{a,S}=\chi_a\land\neg\Box\chi_a\land
\bigwedge_{c\in S}\theta_c\land
\bigwedge_{c\in Q\setminus S}\neg\theta_c
\]
characterizes exactly the root points with that profile, across all valuations. The depth-one formula \(\lambda_a=\chi_a\land\Box\chi_a\) characterizes all leaves of color \(a\), along with roots whose entire valuation is uniformly color \(a\). Such a uniform root is bisimilar to a leaf of color \(a\); no modal formula can separate them. Conversely, the formulas \(\lambda_a\) and \(\rho_{a,S}\) distinguish every other pair of profiles. Thus the complete modal equivalence classes are exactly one leaf/uniform-root class per \(a\), and one class for each \((a,S)\) with \(S\neq\{a\}\).

**3. Counting and completeness at depth two.** For \(k\geq1\), every nonempty color support with size at most \(k\) can occur by putting one representative of each chosen color on distinct leaves and duplicating an arbitrary chosen color on remaining leaves. There are \(q\sum_{j=1}^{\min(k,q)}\binom qj\) formal pairs \((a,S)\). The \(q\) pairs with \(S=\{a\}\) become the \(q\) leaf/uniform-root classes, not an additional family, so the total number of pointed modal types is exactly the displayed sum. The characteristic formulas above have depth at most two. Because the set of classes is finite and Boolean negation and disjunction are available, every subset of these types is definable by a depth-two formula. Thus the entire formula algebra has \(2^{q\sum_{j=1}^{\min(k,q)}\binom qj}\) elements, and greater depths introduce none. If \(k=0\), the frame is a single reflexive point and all modalities collapse to identity, giving exactly \(q\) pointed colors and \(2^q\) formula operations.

**4. Exact depth-one quotient and its sharp failure.** A formula of depth at most one at the root depends only on root color \(a\) and the accessible color palette \(T=\{a\}\cup S\). The depth-one tests \(\chi_a\) and \(\Diamond\chi_c\), for every \(c\in Q\), distinguish these profiles. The accessible palette contains \(a\) and has at most \(k\) other colors; every such palette is realizable when \(k\geq1\), while \(k=0\) has only \(T=\{a\}\). At any leaf of color \(a\), the depth-one profile coincides with \((a,\{a\})\). Hence there are exactly \(q\sum_{j=0}^{\min(k,q-1)}\binom{q-1}{j}\) depth-one types, and hence the stated number of depth-one formula operations.

For \(s\geq1\) and \(k\geq2\), choose distinct colors \(a,b\). Compare two valuations whose root color is \(a\), with leaf supports respectively \(\{b\}\) and \(\{a,b\}\). Both roots have the same accessible palette \(\{a,b\}\), so every depth-one formula agrees. Yet \(\theta_a\) is false at the first root and true at the second. Conversely, when \(s=0\) or \(k\leq1\), the depth-one and full type counts coincide; all formulas then collapse to depth one or less. This proves the exact sharpness conditions.

**5. A sharp last-leaf branching distinction.** For \(q\geq2\), the full type count increases at each \(k=1,\ldots,q\) by the positive summand \(q\binom qk\), and becomes constant thereafter; from \(k=0\) to \(k=1\) it increases from \(q\) to \(q^2\). Choose, for each \(0\leq k<q\), a root color \(a\) and a leaf support \(S\) of cardinality \(k+1\) with \(S\neq\{a\}\). The formula \(\neg\rho_{a,S}\) is valid on \(F_k\), because no valuation there has that support, but is refuted on \(F_{k+1}\). Monotonicity in the reverse direction follows from duplicating leaf colors to simulate any valuation on the smaller star. Thus the fixed-letter frame-validity theories strictly decrease at every leaf count below \(q\), then coincide for all \(k\geq q\). The depth-one type count stops growing already at \(q-1\), so the last strict step is visible only at depth two.

## Verification

`verify.py` is a standalone Python 3 program requiring only the standard library. Running `python verify.py` compares the claimed modal-depth profile against direct successor-set color refinement across **all valuations and all pointed worlds**, for \(q\in\{2,4,8\}\) and the indicated \(k\leq4\); it also evaluates \(\theta_c\) directly on every tested valuation. Independent of this partition calculation, it enumerates the actual Boolean modal term-operation closure for the one-letter stars with \(0\leq k\leq3\), obtaining \(4,16,64,64\) operations. The recorded output ends in `VERIFY_OK 24686 pointed valuation cases`. These are finite computational checks and do not certify the universally quantified proof; the preceding arguments establish the formulas for all integers \(s,k\geq0\).

## Relationship to prior work

Agnew (2026), especially Theorem 3.16, characterizes when the complex algebra of a transitive frame is locally finite, via well-foundedness and avoidance of an infinite disjoint-order obstruction. It neither provides nor implies the numerical fixed-frame generated-operation census for an individual finite reflexive star. The general bisimulation and local-tabularity connections are standard and are not claimed as new.

Ten Cate and Koudijs (2022/2023) study finite characterizations of modal formulas and prove general connections to local tabularity, not this complete variable-by-variable star census. Related published classifications include a formula-operation census for **reflexive linear-preorder cluster chains** (not rooted incomparable leaves), a rooted-**intuitionistic** fork census under persistent valuations (not Boolean modal evaluations), and a stronger **topological derivative/path reachability** language on Alexandrov stars. The latter uses a different observable signature; its partition refines but does not state this \(\Box\)-reduct's exact identification of a homogeneous root with leaves, its two different depth exponents, or the strict one-extra-leaf gap. Their full inspected claims do not directly subsume the present count. Finite-model bisimulation invariance and Boolean normal forms, and the basic binomial identities, are prior mathematics.

## Limitations

The classification concerns a **fixed finite reflexive star**, ordinary Boolean valuations and the standard ungraded unary modal operator. It does not count term operations over arbitrary \(\mathsf{S4}\) frames, nonreflexive stars, persistent intuitionistic valuations, graded or global modalities, or formulas with additional fixed-point operators. The exact formula-algebra count is proved, but independently prior equivalent specializations in older modal-algebra tables cannot be excluded solely through search. No independent mathematical or historical-priority audit has been performed.

## References

1. Gabriel Agnew, *On Local Finiteness of Modal K4 Algebras*, arXiv:2606.02941, first posted 2026-06-01, https://arxiv.org/abs/2606.02941 .
2. Balder ten Cate and Raoul Koudijs, *Characterising Modal Formulas with Examples*, arXiv:2206.06049 (first posted 2022-06-13; later version arXiv:2304.06646), https://arxiv.org/abs/2304.06646 .
3. *Canonical palette-word census of modal term operations on finite S4.3 cluster chains*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-canonical-palette-word-census-of-modal-term-operations-on-finite--241545926600 .
4. *Sharp variable visibility and exact rooted type counts on intuitionistic forks*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-variable-visibility-and-exact-rooted-type-counts-on-intuit--b556d9d8fa10 .
5. *Exact formula algebra and sharp depth two for reachability on Alexandrov stars*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-formula-algebra-and-sharp-depth-two-for-reachability-on-al--1151377036d3 .
6. *The 4–12–60 unary algebra of bi-intuitionistic rooted stars*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-4-12-60-unary-algebra-of-bi-intuitionistic-rooted-stars--d9e2de8c6c99 .
