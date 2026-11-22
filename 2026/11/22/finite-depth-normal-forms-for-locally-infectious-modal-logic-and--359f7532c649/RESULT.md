# Finite-depth normal forms for locally infectious modal logic and exact directed-cycle spectra

## Finding

Consider Bochvar's three-valued external modal language with \(k\geq0\) propositional letters, the ordinary weak-Kleene connectives \(\neg,\lor\), the external truth test \(J_2\), constants \(0,1\), and the locally infectious necessity operator \(\Box\). On any **nonempty finite** Kripke frame \(F\), let \(\mathcal T_d(F,k)\) be the set of realized pointed depth-\(d\) three-color modal signatures across **all** assignments of the three values to the letters. For each \(S\subseteq[k]\), put \(\mathcal T_d(F,k;S)=\{t\in\mathcal T_d(F,k):\text{all letters indexed by }S\text{ are classical at the root}\}\).

The exact number of distinct depth-at-most-\(d\) **three-valued formula functions**, with equivalence taken over all worlds and all valuations on \(F\), is

\[
\boxed{A_d(F,k)=\sum_{S\subseteq[k]}2^{|\mathcal T_d(F,k;S)|}.}
\]

More precisely, every formula has a unique *semantic undefinedness support* \(S\subseteq[k]\): it takes the indeterminate value at a world exactly when some root letter indexed by \(S\) does. Conditional on those letters being classical at the root, the formula can have **any** Boolean output function of the depth-\(d\) signature; every such function has a formula of modal depth at most \(d\).

For the directed cycle \(C_n^{\to}\) with \(n\geq1\) and exactly one outgoing successor per world, put \(L=\min\{d+1,n\}\). Then every three-color word of length \(L\) occurs and

\[
\boxed{A_d(C_n^{\to},k)=\sum_{s=0}^{k}\binom{k}{s}\,2^{\,2^s3^{kL-s}}.}
\]

For every \(k\geq1\), the depth hierarchy on \(C_n^{\to}\) is strictly increasing through depth \(n-1\) and constant thereafter; this bound is sharp for each \(n\). With one letter the exact sequence, up to stabilization, is

\[
A_d(C_n^{\to},1)=2^{3^L}+2^{2\cdot3^{L-1}}.
\]

For example, the first three distinct levels (on cycles long enough to exhibit them) are \(12\), \(576\), and \(134479872\) formula functions. For two letters, depth zero already has exactly \(656\) functions.

## Assumptions and scope

A model is a finite nonempty set of worlds \(W\), a binary accessibility relation \(R\), and an arbitrary letter valuation \(v:W\times[k]\to\{0,1,u\}\), where \(u\) is the undefined value. Weak-Kleene negation fixes \(u\) and interchanges \(0,1\); weak-Kleene disjunction is infectious (if either input is \(u\), the result is \(u\); otherwise it is ordinary Boolean disjunction). \(J_2(a)\) is \(1\) exactly when \(a=1\), and \(0\) otherwise. Conjunction is defined by De Morgan duality. The Bochvar modal clause is

\[
v(w,\Box\varphi)=\begin{cases}
u,&v(w,\varphi)=u,\\1,&v(w,\varphi)\ne u\ \text{and all }wRz\text{ have }v(z,\varphi)=1,\\0,&\text{otherwise},\end{cases}
\]

In particular \(\Box\varphi\) remains undefined exactly when \(\varphi\) is undefined **at the current world**, not when it is undefined at a successor. The empty-successor universal condition is true. Modal depth assigns depth zero to propositional letters, constants and Boolean or truth-test operations; \(\Box\) increases depth by one.

Define the signatures recursively: \(t_0(w)\) is the vector of the \(k\) root letter values, and

\[
t_{d+1}(w)=\bigl(t_0(w),\{t_d(z):wRz\}\bigr).
\]

These signatures are considered across all valuations of the **fixed** frame and all roots. No assumption of transitivity, seriality, symmetry or reflexivity is made for the first theorem. The cycle corollary uses a deterministic total directed cycle, not an undirected cycle.

## Proof

**1. Undefinedness invariant.** To a formula associate its set of unguarded letters recursively: a letter has its own singleton set; constants have the empty set; negation and the modal operator preserve the set; disjunction takes the union; applying \(J_2\) erases the set. Induction on syntax using the infectious truth table and the local modal clause shows that the formula evaluates to \(u\) exactly when at least one of those unguarded letters has value \(u\) at the root. This is independent of all successors.

**2. Upper bound from signatures.** Induction on modal depth shows that every formula of depth at most \(d\) has a value determined by \(t_d(w)\). For the modal step, the signature determines the previous-depth signature at the root and the set of previous-depth signatures of successors. Together these determine the current operand's undefinedness and all successor operand values, hence its boxed value. Thus, after fixing the undefinedness-support set \(S\), each formula is specified by a binary function on \(\mathcal T_d(F,k;S)\). There are at most \(2^{|\mathcal T_d(F,k;S)|}\) such functions.

**3. Every upper-bound function is expressible.** The externally classical formulas \(J_2p_i\), \(J_2\neg p_i\), and \(\neg(J_2p_i\lor J_2\neg p_i)\) distinguish the three atomic values of each letter. Since an external formula is always Boolean-valued and \(\Box\) acts on it like classical necessity, standard finite-depth characteristic formulas can be constructed recursively: for a realized successor-type set \(U\), require an accessible witness of each type in \(U\), and require every successor to have one of those types. The empty-set conventions are \(\bigvee\varnothing=0\) and \(\bigwedge\varnothing=1\). Consequently any Boolean function \(b\) on the finite set of realized depth-\(d\) signatures has an external formula \(\chi_b\) of depth at most \(d\).

For \(S\ne\varnothing\), define the internal meaningfulness factor

\[
\tau_S=\bigwedge_{i\in S}(p_i\lor\neg p_i),\qquad \tau_{\varnothing}=1.
\]

It equals \(u\) precisely when a root letter indexed by \(S\) equals \(u\), and equals \(1\) otherwise. The formula \(\tau_S\land\chi_b\) therefore outputs \(u\) on the required undefinedness set and agrees with \(b\) at every other pointed valuation. Every permitted function is thus achieved. Distinct support sets yield distinct functions because each letter can independently be assigned \(u\) at a chosen world and the frame is nonempty. This proves the general census and uniqueness of the semantic support.

**4. Cycle count and sharp depth.** On a directed cycle, the rooted depth-\(d\) signature reads exactly the first \(L=\min(d+1,n)\) successive vectors of \(k\) values. All such words are realizable by extending an arbitrary prefix to an \(n\)-cycle valuation. When exactly \(s\) root letters are required to be classical, the number of available signature words is \(2^s3^{kL-s}\). There are \(\binom{k}{s}\) choices of the support. Substitution in the general formula proves the displayed cycle expression. When \(k\ge1\), increasing \(L\) strictly increases every summand's exponent; hence every depth from zero through \(n-1\) adds genuinely new formula functions. At depth \(n-1\) the complete cyclic word is visible, so deeper formulas cannot distinguish additional pointed valuations. The depth cutoff is therefore both sufficient and sharp.

## Verification

The accompanying `verify.py` independently saturates the actual three-valued term functions under negation, disjunction and \(J_2\), adding modal images only when the depth budget permits. It compares all generated functions against the closed formula and checks their root-undefinedness supports and bounded-prefix invariance. The completed checks were: one-vertex one-letter depth zero (\(12\)), one-vertex two-letter depth zero (\(656\)), two-vertex one-letter depths zero and one (\(12,576\)), and three-vertex one-letter depths zero and one (\(12,576\)). Output: `VERIFY_OK`. This finite testing is corroboration, not a replacement for the all-parameter proof.

## Relationship to prior work

Bonzio, Vergottini and Zamperlin (2026) define the relevant Bochvar-Kripke semantics and prove algebraic representation and term-equivalence results for the Bochvar and Halldén settings; the current result uses their Bochvar clause and **does not assert the same primitive-language depth census for Halldén**. Bonzio and Zamperlin (2024) supply completeness and decidability of modal external weak Kleene systems. Bonzio and Pra Baldi (2024) provide the non-modal Płonka-style structure of Bochvar algebras. The classical finite-depth modal signature construction is standard. The present contribution is the explicit all-frame support-indexed function normal form and exact graded directed-cycle census with sharp saturation depth, not the underlying truth tables, representation theorems or standard bisimulation principle.

## Limitations

The count concerns equivalence of **three-valued outputs**, at each pointed valuation on one fixed finite frame, under all assignments. It does not count provability-equivalence classes over all frames, formula strings, independent truth assignments to modal subformulas, or finite-frame validity classes. The length or formula-size complexity of the characteristic formulas is not bounded here. The displayed cycle cutoff concerns the Bochvar modality in the given signature, and it does not automatically transport to Halldén syntax without analyzing translation depth. Exact historical priority of the census outside the inspected material requires independent review.

## References

1. S. Bonzio, G. Vergottini and N. Zamperlin, *Modal weak Kleene logics: algebraic semantics and Jónsson–Tarski representation*, arXiv:2611.09566 (public version November 6, 2026). https://arxiv.org/abs/2611.09566
2. S. Bonzio and N. Zamperlin, *Modal weak Kleene logics: axiomatizations and relational semantics*, Journal of Logic and Computation, DOI:10.1093/logcom/exae046. https://doi.org/10.1093/logcom/exae046
3. S. Bonzio and M. Pra Baldi, *On the structure of Bochvar algebras*, Review of Symbolic Logic, DOI:10.1017/S175502032400008X. https://doi.org/10.1017/S175502032400008X
4. Standard finite-depth characteristic formulas for classical modal \(\mathsf K\) are used in the proof; they are reconstructed above rather than invoked as an unproved nonstandard theorem.
