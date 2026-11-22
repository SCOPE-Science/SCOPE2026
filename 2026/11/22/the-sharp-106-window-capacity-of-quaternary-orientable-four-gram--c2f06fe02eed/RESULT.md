# The sharp 106-window capacity of quaternary orientable four-grams

## Finding
The maximum possible period of a four-symbol orientable sequence of window order four is
\[
M_4(4)=106.
\]
An orientable sequence is a circular word \(s\) over \(\{0,1,2,3\}\) in which no length-four cyclic window is palindromic and no two distinct windows agree up to reversal. The optimum is attained by the following 106-symbol word (read cyclically):

`0003101021023001030021210312110122020012322031311120331033230113032113202132212331321333030201312223023231`

## Assumptions and scope
The alphabet consists of exactly four labeled symbols, the window length is four, the word is circular, and a window is forbidden to reappear either as itself or reversed. A cyclic window whose reverse is itself is forbidden. No constraint on symbol multiplicity is imposed. This is not a result about finite non-circular paths, negative-orientable sequences, or alphabet sizes other than four.

## Proof
There are \(4^4=256\) four-grams, of which \(4^2=16\) are palindromes. The remaining \(240\) form \(120\) reversal pairs. Regard a four-gram \(a b c d\) as the directed edge from its length-three prefix \(a b c\) to suffix \(b c d\) in the order-three de Bruijn digraph. Any cyclic orientable word selects at most one directed edge from each reversal pair and has equal indegree and outdegree at all \(64\) vertices.

For a smaller *necessary* relaxation, introduce \(z_e\in\{0,1\}\) for each of the \(120\) reversal-pair orbits. There are \(40\) reversal classes of three-grams, of which \(24\) are nonpalindromic. For a canonical representative \(a b c d\) of orbit \(e\), let \(u=a b c\), \(v=b c d\), and write \(\bar u\) for reversal. For each nonpalindromic three-gram class representative \(p\), define
\[
B_{p,e}=[u=p]-[v=p]-[u=\bar p]+[v=\bar p].
\]
The balance-difference equations are \(Bz=0\). They are independent of which orientation of the reversal pair was selected: reversing the four-gram swaps its source and target while reversing both three-gram labels, leaving the displayed expression unchanged.

For each of the \(40\) reversal classes \(c\) of three-grams, define \(P_{c,e}\) as the number of endpoints \(u,v\) belonging to \(c\), counting a loop twice. In a closed directed Eulerian traversal, the sum of indegrees and outdegrees in any class must be even, hence
\[
Pz=2t,\qquad t\in\{0,1,\ldots,10\}^{40}.
\]
The upper bound ten is safe: an original three-gram has at most four incoming and four outgoing directed edges, and each reversal class has at most two vertices, so any selected balanced realization has \(t_c\le8\). In particular these equations constrain every admissible circular word, but may allow edge sets that do not form a single circuit; such a relaxation can only increase the maximum.

A fully specified finite integer optimization, reproduced verbatim by `checker.py`, maximizes \(\sum_e z_e\) subject to \(Bz=0\), \(Pz=2t\), and the indicated domains. The SciPy/HiGHS mixed-integer solver terminates with a global optimality gap of zero and objective \(106\). A second formulation with \(240\) binary orientation variables, \(64\) original-vertex conservation rows, and \(120\) reversal-pair packing rows independently gives the same objective. The checker constructs these matrices from alphabet Cartesian products, rather than using cached constraints or output logs, and checks all resulting integral primal conditions.

For attainment, the displayed word has exactly \(106\) circular windows. The checker independently enumerates all its windows and establishes that the \(106\) canonical representatives \(\min(w,\operatorname{reverse}(w))\) are distinct and none is palindromic. Therefore \(M_4(4)\ge106\). Combining the two bounds gives equality.

## Verification
Run `python checker.py` with Python 3, NumPy and SciPy (including HiGHS). It prints `DIRECT_OPTIMUM 106 RELAXATION_OPTIMUM 106 ... VERIFY_OK`. It rebuilds both optimization models from definitions, requires solver success with zero reported global relative MIP gap, verifies the integer primal, generates an Euler circuit, and directly checks every cyclic four-gram. Both formulations have all-integer model data and are small enough to reproduce interactively. This is computational exhaustive optimization with solver-assisted global optimality, not an independent formal proof certificate.

## Relationship to prior work
The 1992 published *Position-sensing apparatus* disclosure defines orientable sequences and their de Bruijn graph representation. Its public publication date, 15 October 1992, is day-verified; an earlier HP technical report carries only the month January 1992, not a verified exact day. Mitchell and Wild, *New orientable sequences* (arXiv:2507.02526, 3 July 2025), provide the bound of \(112\) at this parameter; their 2026 full text discusses the still-open four-symbol order-four case. A separate published construction supplies a \(106\)-symbol example but does not show its optimality. This result adds the matching upper bound. The original construction is not claimed as new.

## Limitations
The global upper bound relies on the stated reproducible integer-programming solver's optimization guarantee; no third-party validation or solver-independent cutting-plane certificate is claimed. The smaller necessary relaxation is not claimed to characterize all realizable cycles. Exact-day source dating predates neither a month-only 1992 technical report nor an earlier year-only account; 15 October 1992 is the earliest *day-verified* public antecedent used here, not a claim that the concept originated that day. Unindexed earlier results or a stronger equivalent upper bound remain a residual originality risk.

## References
- *Position-sensing apparatus*, WIPO publication WO1992017859A1, published 1992-10-15, https://patents.google.com/patent/WO1992017859A1/en.
- J. Burns and C. J. Mitchell, *Coding schemes for two-dimensional position sensing*, HPL-92-19, January 1992 (month only), https://www.chrismitchell.net/HPL-92-19.pdf.
- Z. D. Dai, K. M. Martin, M. J. B. Robshaw, P. R. Wild, *Orientable Sequences*, 1993, pp. 97–115.
- C. J. Mitchell and P. R. Wild, *New orientable sequences*, arXiv:2507.02526 (first posted 2025-07-03), https://arxiv.org/abs/2507.02526; full text https://link.springer.com/article/10.1007/s00236-026-00528-z.
- *A 106-symbol quaternary orientable cycle of order four*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-a-106-symbol-quaternary-orientable-cycle-of-order-four--341177c7af0a.
