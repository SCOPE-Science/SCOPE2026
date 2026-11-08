# Scientific review

## Correctness — PASS

Every positive odd state uniquely has \(y+3=2^j k\) with odd \(k\). The exact next odd state is \(ky\). If \(k=1\), the stated primitive \(j\)-cycle occurs. If \(k\ge3\), the odd state grows. A hypothetical transition \(k(2^j k-3)=2^m-3\) forces \(m>j\) and \(m-j\) even by the modulo-three condition. Writing \(m-j=2h\) makes its left-hand side at least \(4k-2\), strictly exceeding the required \(3(k-1)\). This excludes all nonterminal-to-terminal transitions without computational assumptions, and implies divergence of all iterates. The exact counting formula is a unique-odd-part census; its leading coefficient follows by comparing \(2^m-3\) with dyadic cutoffs.

The attached exact-integer test program corroborates transitions, cycles, finite orbit samples, and bounded-count values, but the infinite theorem is proved analytically.

## Originality — PASS (qualified)

The closest relevant primary paper (Ye, arXiv:2610.10660) gives complete orbit classifications for odd branches \(n(n-1)/2\), \(n(n+1)/2\), and \((n^2-1)/4\), not the plus-three branch. In particular, it has an exceptional preperiodic odd value \(5\) for the plus-one rule, whereas the plus-three rule has none. Sedaghat's arXiv:2004.07357 and arXiv:2005.10712 concern the minus-one and symmetric branches. The three mathematical statements are distinct; their theorems do not yield this plus-three classification merely by substituting a variable, and the new obstruction involves the factor \(3\) absent from their terminal equations. Targeted records searches for the exact branch, terminal numbers and Diophantine equation found no equivalent covering claim. Historical priority risk: equivalent unpublished or non-indexed derivations may exist. Absence from search results is not a proof of priority.

## Mathematical value — PASS

This solves a complete all-initial-state orbit dichotomy for the first positive odd-branch parameter beyond the plus-one map studied in 2026. The exact classification distinguishes a no-exception family from the plus-one map's genuine exceptional basin. It supplies a self-contained elementary obstruction to any extra eventual periodic basin and an exact initial-value census with quadratic logarithmic growth. The result concerns a natural adjacent member of a current published dynamical family, not a selected finite-range computation or a single ad hoc orbit.

## Remaining limitations

The proof does not cover other odd coefficients, escaping rates, or negative starting values. The independence of the mathematical result has not been assessed. Searches and inspected sources materially narrow but do not eliminate historical-priority uncertainty.

Self-review: passed. Independent audit: not yet performed.
