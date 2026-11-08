# The exact rational first-order limit spectrum of layered permutations

## Finding

Let \(\mathcal L_n=\mathrm{Av}_n(231,312)\) be the set of all size-\(n\) *layered permutations*, viewed as structures in the first-order theory of two orders (TOTO): \(<_1\) orders positions and \(<_2\) orders their values. Sample \(\pi_n\) uniformly from \(\mathcal L_n\). The *limit spectrum* is
\[
\operatorname{Lim}(\mathcal L)=\left\{\lim_{n\to\infty}\Pr(\pi_n\models\varphi):\varphi\text{ a first-order TOTO sentence}\right\}.
\]
Then
\[
\boxed{\operatorname{Lim}(\mathcal L)=\mathbb Q\cap[0,1].}
\]
In particular the spectrum is countable and dense, contains every rational including non-dyadic fractions such as \(1/3\), and contains no irrational number. For each pair of integers \(q\ge1\) and \(0\le p\le q\), an explicit sentence attaining \(p/q\) is given below. The novelty claimed is the **exact range and first-eligible-marker realization**, not the previously known first-order convergence law or regular-language rationality.

## Assumptions and scope

The universe consists of the \(n\) points of the permutation, not random unlabelled partitions or arbitrary permutations; the probability measure is uniform on the \(2^{n-1}\) distinct layered permutations. The language has equality and the two strict total orders \(<_1\) and \(<_2\); the formulas use ordinary first-order quantification, no arithmetic, counting or random external predicates. A layered permutation is a direct sum of decreasing nonempty blocks. All limits are taken as the integer size \(n\to\infty\). The value \(p/q\) is permitted at either endpoint. Fixing \(p,q\) permits a formula whose finite size may depend on them; the theorem is not a uniform bounded-rank assertion.

Encode a layered permutation by the \(n-1\) gap bits \(b_i\), with \(b_i=1\) when the consecutive positions \(i\) and \(i+1\) lie in different decreasing blocks, and \(b_i=0\) otherwise. Each gap word occurs exactly once and has probability \(2^{-(n-1)}\). The value of \(b_i\) is first-order definable on the left endpoint \(x\) of a successor pair by \(b_i=1\) precisely when \(x<_2y\) and \(y\) is the immediate \(<_1\)-successor of \(x\).

## Proof

**1. Rational upper bound.** A first-order TOTO sentence on layered permutations can be interpreted as a first-order sentence on the \(n\) ordered positions with a unary predicate indicating boundaries, with the last position separately marked as the maximum. For \(x<_1y\), they belong to distinct blocks if and only if a boundary bit lies at some position \(z\) with \(x\le_1z<_1y\). Distinct blocks preserve the order \(<_1\) in \(<_2\), and the order is reversed inside a single block. Thus for distinct \(x,y\), \(x<_2y\) is equivalent to
\[
(x<_1y\wedge\exists z\,[x\le_1z<_1y\wedge B(z)])\;\lor\;(y<_1x\wedge\neg\exists z\,[y\le_1z<_1x\wedge B(z)]).
\]
Every such formula translates to first-order logic on finite binary words; the word has \(n-1\) variable bits plus a definable terminal vertex. By the standard first-order-to-regular-language theorem, the accepted gap words form a regular language, recognized by a deterministic finite automaton. If \(M_0,M_1\) are its zero-one transition matrices, \(u\) its initial-state row and \(v\) its accepting-state column, then
\[
\Pr(\pi_n\models\varphi)=u\bigl((M_0+M_1)/2\bigr)^{n-1}v.
\]
This is the evolution of a finite-state Markov chain with rational transitions. Its Cesàro limiting distribution has rational entries: hitting probabilities of recurrent classes and stationary measures solve finite rational linear systems. The ordinary limit on the left exists by the established first-order convergence theorem for layered permutations [1]. Consequently the ordinary limit equals the rational Cesàro limit. This proves \(\operatorname{Lim}(\mathcal L)\subseteq\mathbb Q\cap[0,1]\). Note that the existence of the ordinary limit and the transfer between layered permutations and convex orders are **not claimed as new**.

**2. A first-order construction of every rational limit.** Fix integers \(q\ge1\) and \(0\le p\le q\). Set \(k=\max\{1,\lceil\log_2q\rceil\}\), \(L=k+2\), and let \(m=0^L1\) be the binary marker of length \(L+1\). It is unbordered: no nonempty proper prefix is a suffix. Hence two occurrences of \(m\) cannot overlap, and their ending positions are separated by at least \(L+1>k\).

For each marker occurrence that has at least \(k\) subsequent bits, read those bits as a binary integer \(J\in\{0,\ldots,2^k-1\}\). Call the marker *eligible* if \(J<q\) and *winning* if \(J<p\). Define \(\Phi_{p,q}\) to say that some eligible marker is winning and that no strictly earlier marker is eligible. For fixed \(k,L,p,q\), this is a first-order sentence on the ordered gap positions: a fixed word factor is definable by a fixed chain of immediate-successor formulas, \(J<q\) and \(J<p\) are finite disjunctions of the corresponding length-\(k\) bit patterns, and the first-eligible condition is a first-order universal statement over possible earlier starting positions. Replacing each gap predicate by its TOTO definition above yields the required formula on layered permutations.

Now couple all finite words with an infinite sequence of independent fair bits, and let \(T_1<T_2<\cdots\) be the ending times of successive marker occurrences. Each \(T_i\) is a stopping time and, because the marker is unbordered, \(T_{i+1}-T_i\ge L+1>k\). The length-\(k\) blocks immediately following \(T_i\) are therefore **independent and uniformly distributed** on \(\{0,1\}^k\). Indeed, the block after \(T_i\) is independent of the sigma-field up to \(T_i\), and is measurable with respect to the sigma-field at \(T_{i+1}\); induction using the stopping-time property proves independence across all marker samples. Each marker is eligible with probability \(q/2^k>0\), independently of other markers, and conditioned on eligibility it wins with probability exactly \(p/q\).

The marker occurs infinitely often almost surely: for example, look at independent aligned disjoint blocks of \(L+1\) bits, each equal to \(m\) with probability \(2^{-(L+1)}>0\). Hence an eligible marker almost surely exists, and its label is uniformly distributed on \(\{0,\ldots,q-1\}\). Thus \(\Pr(\Phi_{p,q})\to p/q\).

For precision, write \(A_N\) for the event that an eligible marker with its entire \(k\)-bit following sample appears within the first \(N\) gap bits. The same stopping-time argument yields the **exact finite identity**
\[
\Pr(\Phi_{p,q}\text{ holds on the first }N\text{ bits})=(p/q)\Pr(A_N).
\]
As \(\Pr(A_N)\to1\), the asserted limit follows. The arguments include \(p=0\) (always false) and \(p=q\) (eligible eventuality with probability tending to one), as well as \(q=1\).

Combining both inclusions proves the theorem.

## Verification

The standalone `checker.py` reproduces the bijection between binary gaps and layered permutations for sizes \(1\le n\le9\). It independently compares the first-eligible-marker word definition against an exact finite-state dynamic program for each \(1\le N\le15\), for \((p,q)=(1,3),(2,5),(3,7)\), and confirms the exact finite calibration \(q\Pr(\Phi_{p,q})=p\Pr(A_N)\) for \(N=32,64,128,192\). Running `python checker.py` yields `ALL_CHECKS_OK`. These finite checks are consistency tests; the infinite theorem follows from the mathematical arguments above, the standard regular-language correspondence, and the existing convergence theorem.

## Relationship to prior work

Braunfeld and Kukla [1, Sections 2–3] prove first-order convergence for layered permutations and use an Ehrenfeucht–Fraïssé/finite-Markov-chain method; that theorem supplies the existence of ordinary limits and strongly covers the present rational upper bound. Markström and Räty [2] generalize regular-language encodings and logical convergence to small permutation classes. Falgas-Ravry, Markström, Räty and Skerman [3, Theorem 1.4] prove density of first-order limiting probabilities in the exponential-growth regime, which includes layered permutations, but do not assert the exact rational spectrum or the construction above. Berthé, Goulet-Ouellet and Perrin [4, Section 3.2 and Theorem 3.6] treat densities for aperiodic/regular languages under invariant measures, including Bernoulli rationality, which also covers part of the upper-bound mechanism. The distinction here is the **exact endpoint-inclusive set and FO realization of each prescribed rational**, not merely density, existence or generic rationality.

## Limitations

This theorem concerns only the specific uniform layered-permutation class and ordinary first-order TOTO; it does not determine exact spectra for all exponentially growing permutation classes, random unrestricted permutations, monadic second-order logic, or biased encodings. Formula complexity grows with the denominator, and no uniform effective quantifier-rank bound is claimed. The construction proves asymptotic attainment, not equality to \(p/q\) at finite \(n\). Earlier general results about star-free-language densities or prefix codes could imply the same rational-realization mechanism; historical priority beyond the inspected literature remains a residual uncertainty.

## References

[1] S. Braunfeld and M. Kukla, *Logical Limit Laws for Layered Permutations and Related Structures*, Enumerative Combinatorics and Applications 2:4 (2022), S4PP2; arXiv:2111.06307; DOI 10.54550/ECA2022V2S4PP2.

[2] K. Markström and E. Räty, *Logical isomorphism and logical limit laws for small permutation classes and regular languages*, first posted October 15, 2026, arXiv:2610.22218.

[3] V. Falgas-Ravry, K. Markström, E. Räty and F. Skerman, *On first-order limiting probabilities for small permutation classes*, first posted October 25, 2026, arXiv:2610.34328.

[4] V. Berthé, H. Goulet-Ouellet and D. Perrin, *Density of Rational Languages Under Shift Invariant Measures*, ICALP 2025, Article 143; DOI 10.4230/LIPIcs.ICALP.2025.143.
