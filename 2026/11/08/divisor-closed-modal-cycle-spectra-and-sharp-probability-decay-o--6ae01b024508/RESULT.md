# Divisor-closed modal cycle spectra and sharp probability decay on permutation frames

## Finding

Consider the basic unimodal propositional language with Boolean connectives, one modal operator \(\Box\), and arbitrarily many propositional letters. Let \(C_m\) be the directed cyclic Kripke frame on \(\mathbb Z/m\mathbb Z\) whose unique successor of \(i\) is \(i+1\pmod m\), where \(m\ge1\). A formula is **frame-valid** if it holds at every world under every Boolean valuation. Write \(\operatorname{Spec}(\varphi)=\{m\ge1:C_m\models\varphi\}\), and let \(d\) be the modal depth of \(\varphi\).

**Complete spectrum and depth theorem.** Exactly one of the following holds:

1. \(\operatorname{Spec}(\varphi)=\mathbb Z_{>0}\), i.e. \(\varphi\) is valid on every finite permutation frame;
2. \(\operatorname{Spec}(\varphi)=A\subseteq\{1,\dots,d\}\), where \(A\) is finite and **divisor-closed**: if \(m\in A\) and \(k\mid m\), then \(k\in A\).

Conversely every finite divisor-closed \(A\subseteq\mathbb Z_{>0}\), including the empty set, is the spectrum of a basic modal formula. Every nonempty such \(A\) has **minimum defining modal depth** \(\max A\) for its associated class of all finite permutation frames. The empty set is defined by falsum at depth zero; the all-positive-integers spectrum by truth at depth zero.

**Probability and rate theorem.** Draw \(\sigma_n\) uniformly from the \(n!\) permutations of \([n]\), and give it the Kripke relation \(iRj\iff j=\sigma_n(i)\). If \(A=\operatorname{Spec}(\varphi)\) is finite, put \(c_n=\Pr(( [n],R)\models\varphi)\). Then for all \(n\ge1\)
\[
 c_n=[z^n]\exp\!\left(\sum_{a\in A}\frac{z^a}{a}\right),\qquad
 c_0=1,\qquad n c_n=\sum_{a\in A,\ a\le n}c_{n-a}.
\]
For \(A=\varnothing\), \(c_n=0\) for \(n\ge1\). For nonempty \(A\), let \(L=\max A\); then \(1\in A\), \(c_n>0\), and
\[
 \log c_n=-\frac nL\log n+\frac nL+O_A\bigl(n^{(L-1)/L}+\log(n+1)\bigr).
\]
For the all-positive-integers spectrum, \(c_n=1\). Hence **every** basic modal formula obeys a frame-validity zero-one law on uniform permutation frames. Among nontrivial formulas of modal depth at most \(d\ge1\) with positive (but vanishing) validity probabilities, the exact possible exponents in
\(\lim_{n\to\infty}-\log c_n/(n\log n)\) are precisely \(1,1/2,\ldots,1/d\).

## Assumptions and scope

The frame has one **total bijective** successor map; fixed points and loops are allowed. Boolean valuations are unrestricted and vary independently for distinct propositional letters. The probability is uniform on **labelled permutations**, not uniform on conjugacy classes, not on all directed graphs, and not an average over valuations. The maximum \(d\) is the usual syntactic nesting depth of modal operators. The theorem quantifies over every basic modal formula with finitely many propositional letters, every integer \(n\ge1\), and every finite divisor-closed spectrum. No claim is made about full PDL with tests, converse, star, or loop connectives.

## Proof

**1. Deterministic unrolling and the long-cycle dichotomy.** At a world of a functional frame, \(\Box\theta\) evaluates \(\theta\) at its unique successor, so a modal formula \(\varphi\) of depth \(d\) at a root depends only on the Boolean values of its finitely many letters at successor positions \(0,1,\dots,d\). In a simple cycle \(C_m\) with \(m>d\), these positions are distinct. Therefore the Boolean truth-function of the unrolled formula, and in particular its universal validity, is independent of \(m\) for all \(m>d\).

**2. Divisor closure.** If \(k\mid m\), the map \(C_m\to C_k\) taking residues modulo \(k\) commutes with successors and is a surjective bounded morphism. Any valuation falsifying \(\varphi\) on \(C_k\) pulls back to a falsifying valuation on \(C_m\). Hence \(C_m\models\varphi\) implies \(C_k\models\varphi\). If \(\varphi\) validates one long cycle \(C_m\) with \(m>d\), it validates all long cycles by step 1; for any \(k\le d\), choose a multiple of \(k\) exceeding \(d\), and apply divisor closure. Thus the spectrum is all positive integers. Otherwise the spectrum is a divisor-closed subset of \(\{1,\dots,d\}\).

**3. Attainability and optimal depth.** For every finite divisor-closed nonempty set \(A\), choose pairwise distinct letters \(p_a\) and define
\[
 \varphi_A=\bigvee_{a\in A}\bigl(p_a\leftrightarrow\Box^a p_a\bigr).
\]
If \(k\mid a\), the corresponding disjunct is valid on \(C_k\). Conversely if \(k\nmid a\) for every \(a\in A\), fix a world \(w\) and for each independent letter \(p_a\) set \(p_a\) true at \(w\) and false at the distinct world reached after \(a\) steps. Then every disjunct is false at \(w\). Hence \(C_k\models\varphi_A\) exactly when \(k\mid a\) for some \(a\in A\), which equals \(k\in A\) by divisor closure. Its modal depth is \(\max A\). The dichotomy from step 2 forces the depth of **any** formula defining the same nonempty finite spectrum to be at least \(\max A\). Falsum and truth realize the two remaining cases.

**4. Arbitrary finite permutation frames and exact counting.** Every permutation frame is a disjoint union of directed cycles. Frame validity is componentwise, so \(\varphi\) holds on it exactly when every component length belongs to \(A\); for the all-positive spectrum this is automatic. For a finite \(A\), the exponential formula for labelled permutations gives
\[
 \sum_{n\ge0}\frac{\#\{\sigma\in S_n:\text{all cycle lengths in }A\}}{n!}z^n
 =\exp\!\left(\sum_{a\in A}\frac{z^a}{a}\right).
\]
This is exactly the ordinary generating function of the uniform validity probabilities \(c_n\). Differentiating yields \(n c_n=\sum_{a\in A,\ a\le n}c_{n-a}\), proving the stated exact formula and recurrence.

**5. Sharp logarithmic asymptotics.** Suppose \(A\) is nonempty and \(L=\max A\). Divisor closure forces \(1\in A\), hence \(c_n>0\). Since the coefficients are nonnegative, at the positive real \(t=n^{1/L}\),
\[
 c_n t^n\le\exp\!\left(\sum_{a\in A}\frac{t^a}{a}\right)
 \le\exp\!\left(\frac nL+O_A(n^{(L-1)/L})\right).
\]
Taking logarithms gives the desired upper bound. Conversely write \(n=kL+r\) with \(0\le r<L\). The permutations with exactly \(k\) cycles of length \(L\) and \(r\) fixed points contribute at least
\[
 c_n\ge \frac{1}{L^k k!\,r!}.
\]
Here \(k=n/L+O_L(1)\) and \(r\) is bounded. Stirling's formula therefore gives
\[
 \log c_n\ge-\frac nL\log n+\frac nL-O_A(\log(n+1)).
\]
The two bounds prove the asymptotic with its stated error. It tends to zero super-exponentially for every finite nonempty spectrum. When the spectrum is empty the probability is identically zero, and when all positive integers occur it is identically one. The depth hierarchy follows because \(L\le d\), while \(p\leftrightarrow\Box^L p\) has depth \(L\) and spectrum exactly the positive divisors of \(L\), attaining exponent \(1/L\).

## Verification

The accompanying `checker.py` performs finite truth-table checks on cyclic frames, validates \(\operatorname{Spec}(p\leftrightarrow\Box^a p)=\{k:k\mid a\}\), and exhaustively compares coefficient probabilities with the counts of all labelled permutations of sizes one through eight for eight allowed length sets. It separately tests the two-leading-term bound on representative finite spectra. Run `python checker.py` in the same directory; expected marker: `PERMUTATION_MODAL_CYCLE_SPECTRA_OK`. The code illustrates the finite calculations and is **not** relied on to prove the statements for unbounded \(n\).

## Relationship to prior work

Bednarczyk and Swoboda (2026) analyse finite satisfiability in an extension of PDL with an explicit loop operator and converses; their results motivate the distinction between cycle-sensitive logics and the weaker basic modal language. The present theorem concerns **frame validity**, not satisfiability, and quantifies over a much smaller, fixed family of bijective one-successor frames.

Benaych-Georges (2007), along with earlier permutation enumeration, supplies substantial **pre-existing** general results on cycle-length-restricted permutations; the exponential formula and the finite-length enumeration are classical, and we do not present them as independently new. The claimed combination is the complete attainable **basic-modal** cycle spectrum with a sharp modal-depth restriction and its induced exact probability/decay hierarchy. Goranko's work on asymptotic modal frame validity samples all relations rather than bijections; this distinction is essential, as a general modal frame-validity zero-one law fails. Goldblatt's results on transitive frames of bounded circumference have a different frame class. Müller, Skerman and Verstraaten (2023) revisit the theory of one bijection and cite Compton's classical result: the uniform permutation ensemble has a first-order convergence law but not a first-order zero-one law. This does not conflict with the theorem here: a **basic-modal frame-validity** assertion quantifies over all valuations and is not an arbitrary first-order sentence about a permutation. Koponen (2026) discusses convergence laws for random finite structures, which is part of the broader motivation but does not provide the cycle-spectrum theorem.

## Limitations

The logical spectrum classification uses the ordinary basic modal language with arbitrary propositional letters. It does not cover enhanced temporal languages with backward modalities or loop testers. The main probability conclusion is for **uniform labelled permutations** only. The count of restricted permutations and its asymptotic are supported by classical combinatorics and are not claimed to be novel in isolation. An equivalent modal cycle-spectrum statement could occur in older specialist literature, so a residual historical-priority risk remains. The complete statements and proofs concern the specified classical Boolean modal semantics only.

## References

- B. J. Bednarczyk and M. Swoboda, *Towards Finite Satisfiability of PDL with Loops*, arXiv:2610.15632v1 (first public October 11, 2026), introduction, preliminaries, main theorem, conclusions.
- F. Benaych-Georges, *Cycles of random permutations with restricted cycle lengths*, arXiv:0712.1903 (2007), Sections 1–2, particularly Section 2.2 and Lemma 2.6.
- V. Goranko and B. Kapron, *The modal logic of the countable random frame*, Archive for Mathematical Logic 42 (2003), 221–243, DOI:10.1007/s001530100135.
- V. Goranko, *The modal logic of almost sure frame validities in the finite*, text available at https://titan.dcs.bbk.ac.uk/volumes/volume13/Goranko.pdf, introduction on sampling all finite frames.
- R. Goldblatt, *Modal Logics that Bound the Circumference of Transitive Frames*, arXiv:1905.11617 (2019).
- T. Müller, F. Skerman and T. W. Verstraaten, *Logical limit laws for Mallows random permutations*, arXiv:2302.10148v3 (originally submitted February 20, 2023), Sections 1.1–2 and the one-bijection literature reviewed there.
- V. Koponen, *A characterization of the finite model property for ω-categorical theories*, arXiv:2610.16163v1 (first public October 12, 2026).
