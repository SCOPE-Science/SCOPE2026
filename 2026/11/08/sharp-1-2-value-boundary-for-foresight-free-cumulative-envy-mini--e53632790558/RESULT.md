# Sharp \(\{1,2\}\)-value boundary for foresight-free cumulative envy minimization

## Finding

**Theorem (sharp positive-integer alphabet boundary).** Consider two agents with a common, additive valuation and a fixed arrival order of \(m\ge 1\) indivisible goods. Each good must be permanently assigned when it arrives. Write \(L_{i,t}\) for the total value of goods given to agent \(i\) after \(t\) arrivals, and define the cumulative maximum envy
\[
C=\sum_{t=1}^{m}|L_{1,t}-L_{2,t}|.
\]
If every good has value in \(\{1,2\}\), allocating each arriving good to an agent with the smaller current bundle value minimizes \(C\) among **all**, even fully foresighted, assignments, for every \(m\) and every order. Thus, for each positive integer \(B\), this greedy rule is universally optimal for all such instances with values in \(\{1,\ldots,B\}\) if and only if \(B\le2\). This also holds after uniformly multiplying the two allowed values by a positive constant.

The boundary is sharp at four goods: with values \((1,1,3,1)\), greedy costs \(6\) whereas the optimum is \(4\). Strict positivity matters: allowing a zero value already destroys the assertion for \((1,1,2,0)\), where greedy costs \(5\) and the optimum is \(3\). For any three or fewer goods with arbitrary nonnegative values, greedy is optimal.

## Assumptions and scope

The two agents have **identical** additive, nonnegative values for all goods, with exactly one item arriving per round; both see the same fixed sequence. The allocation is complete, irrevocable, and evaluated by the sum of the maximum pairwise envies over all prefixes, not final envy, EF1, or weighted/discounted cumulative envy. In the main positive case the values are integers \(1\) and \(2\); no future information or tie-breaking restriction is needed. The rule is not asserted for heterogeneous valuations, three or more agents, arbitrary other bi-valued sets, or zero-valued arrivals.

Set signed discrepancy \(D_t=L_{1,t}-L_{2,t}\) and \(D_0=0\). Assigning a good of value \(w_t\) changes \(D_{t-1}\) to either \(D_{t-1}+w_t\) or \(D_{t-1}-w_t\). Its minimum possible new absolute discrepancy is \(\bigl||D_{t-1}|-w_t\bigr|\). Greedy chooses such a successor; the resulting absolute discrepancies obey \(d_0=0\) and \(d_t=|d_{t-1}-w_t|\).

## Proof

For a finite remaining word \(W=(w_1,\ldots,w_\ell)\) over \(\{1,2\}\) and an arbitrary **integer** starting absolute discrepancy \(z\ge0\), let \(F_W(z)\) be the least sum of absolute discrepancies including the current one and all later ones, over every sequence of choices on \(W\). Thus \(F_\varnothing(z)=z\), and if \(W=(w,V)\),
\[
 F_W(z)=z+\min\{F_V(|z-w|),F_V(z+w)\}.
\]
We prove simultaneously by backward induction on the word length that:

1. For all integers \(z\ge2\), \(F_W(z)\ge F_W(z-2)\) (nondecreasing on each parity class).
2. The special difference \(\Delta_W=F_W(2)-F_W(0)\) lies in \([0,2]\).
3. At every starting state the minimum is attained by choosing the smaller absolute successor \(|z-w|\).

For the empty word, the first two properties hold since \(F_\varnothing(z)=z\) and \(\Delta_\varnothing=2\). Given the first two properties for \(V\), observe that \(z+w\ge |z-w|\) and their difference is \(2\min(z,w)\), an even integer. By parity monotonicity, \(F_V(z+w)\ge F_V(|z-w|)\). Hence the third property holds and
\[
F_W(z)=z+F_V(|z-w|).
\]
If \(w=1\), then \(\Delta_W=2\), while for \(z\ge3\),
\[
F_W(z)-F_W(z-2)=2+F_V(z-1)-F_V(|z-3|)\ge2
\]
by parity monotonicity (including \(z=3\), with arguments \(2\) and \(0\)). If \(w=2\), then
\[
\Delta_W=2-\Delta_V\in[0,2],\qquad
F_W(3)-F_W(1)=2,
\]
and, for \(z\ge4\),
\[
F_W(z)-F_W(z-2)=2+F_V(z-2)-F_V(|z-4|)\ge2.
\]
Thus both invariants hold for \(W\), completing induction. Starting at \(0\), successive greedy choices therefore minimize the entire cumulative objective for all positive \(\{1,2\}\) words. Multiplying every item value by the same positive constant multiplies every discrepancy and objective by that constant, preserving decisions and optimality.

For the sharp positive-alphabet converse, take \((1,1,3,1)\). Greedy has absolute discrepancies \((1,0,3,2)\), of sum \(6\). Assigning the first two unit goods to one agent, the value-\(3\) good to the other, and the final unit good to the first gives absolute discrepancies \((1,2,1,0)\), of sum \(4\). The only two absolute discrepancies after two goods are \(0\) and \(2\); conditioned on these, optimal last-two contributions are respectively \(3+2=5\) and \(1+0=1\), giving global optimum \(4\). Every alphabet \(\{1,\ldots,B\}\) with \(B\ge3\) contains this counterexample.

For the zero-valued boundary, \((1,1,2,0)\) gives greedy discrepancies \((1,0,2,2)\) of cost \(5\), while the assignments with absolute discrepancies \((1,2,0,0)\) cost \(3\). The same two-state argument shows optimum \(3\).

Finally, with any three nonnegative values \(a,b,c\), after the first good the discrepancy is \(a\). At the second good the two possible absolute discrepancies are \(u=|a-b|\) and \(v=a+b\). Greedy's best total for the final two rounds is \(u+|u-c|\), compared with \(v+|v-c|\) for the only other second-round choice. The reverse triangle inequality gives \(|u-c|-|v-c|\le v-u\), so the greedy choice is optimal; the final step is always best handled greedily. The cases of one or two goods are immediate. Hence four is the shortest possible counterexample length, even allowing zeros.

## Verification

The standalone Python 3 program `check.py` computes the greedy cost and independently computes the exact optimum by dynamic programming on **all attainable absolute discrepancies**. It additionally compares the dynamic program to direct enumeration of allocation signs to validate the computational oracle. Run `python3 check.py` with a standard Python 3 interpreter. Recorded results: 9,841 dynamic-program-versus-direct-enumeration tests of all words over \(\{1,2,3\}\) through eight goods; 65,535 exhaustive words over \(\{1,2\}\) through fifteen goods; 960 seeded longer words of lengths \(20,40,80,150\); 156 nonnegative words through three goods over \(\{0,\ldots,4\}\); and the two exact four-good counterexamples. These finite tests supplement but do not replace the unbounded induction proof.

## Relationship to prior work

Goldberg, Robinson, and Teh (2026) define and analyze cumulative maximum envy for a fixed item order, prove general hardness, give a pseudopolynomial algorithm for fixed numbers of agents, and prove greedy exactness for **identical binary \(\{0,1\}\) valuations**. Their Proposition 1 and its proof attain a pointwise parity/lower-bound optimum when there is only one positive item size. The present positive \(\{1,2\}\) theorem is a different and strictly more demanding length-unbounded exactness statement: individual prefixes can be suboptimal under the greedy path, yet the sum is minimized; adding zero goods invalidates it. Neither their general dynamic program nor the binary proposition implies this stronger online-optimality claim.

Elkind et al. (2024/2025) study **temporal EF1**, a feasibility property at every prefix, including structured valuations; the present objective is an exact numerical sum and is not implied by TEF1 existence. Amanatidis et al. (2025) study personalized two-value online allocation using MMS and EF1/EF2 guarantees rather than exact cumulative maximum-envy optimization. These distinctions concern mathematical implications, not merely different titles or nomenclature.

## Limitations

Universal exactness is proved only for two agents with identical valuations and positive goods from the common set \(\{1,2\}\) (or a common positive scaling). The threshold does not classify all arbitrary two-value sets; it does not assert greedy optimality for every \(\{a,b\}\), real-valued domains, zero-valued goods, or other envy objectives. The four-good examples disprove greediness but do not prove computational hardness in broader alphabets. No independent audit or publication-priority certification has occurred.

## References

1. P. W. Goldberg, I. Robinson, and N. Teh, *Minimizing Cumulative Envy in Allocating a Sequence of Items*, arXiv:2610.09843v1, October 7, 2026, https://arxiv.org/abs/2610.09843 (especially Section 4, Proposition 1, and Appendix 0.B.1).
2. E. Elkind, A. Lam, M. Latifian, T. Y. Neoh, and N. Teh, *Temporal Fair Division of Indivisible Items*, arXiv:2410.14593v1, October 18, 2024; AAMAS 2025, https://arxiv.org/abs/2410.14593.
3. G. Amanatidis, A. Lolos, E. Markakis, and V. Turmel, *Online Fair Division for Personalized 2-Value Instances*, arXiv:2505.22174v1, May 28, 2025, https://arxiv.org/abs/2505.22174.
