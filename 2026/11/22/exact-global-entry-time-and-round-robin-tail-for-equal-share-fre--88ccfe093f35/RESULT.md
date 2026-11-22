# Exact global entry time and round-robin tail for equal-share Frege dynamics

## Finding
Fix an integer \(m\ge 2\), the equal-share vector \(p_i=1/m\), and an arbitrary real initial score vector \(u\in\mathbb R^m\). In the modified Frege map, update
\[
T(x)=x+(1/m,\ldots,1/m)-e_{i(x)},
\]
where \(i(x)\) maximizes \(x_i+1/m\), using a fixed deterministic priority among tied indices. Write \(\delta=\min_i u_i\), \(\{s\}=s-\lfloor s\rfloor\), and
\[
\tau(u)=\sum_{i=1}^{m}\lfloor u_i-\delta\rfloor.
\]
The **first time** at which the range of the relative scores \(u_i-N_i(t)\), with \(N_i(t)\) the number of wins by index \(i\) in the first \(t\) steps, becomes strictly less than one is **exactly** \(\tau(u)\). At that time,
\[
N_i(\tau)=\lfloor u_i-\delta\rfloor,\qquad
T^{\tau}(u)_i=\delta+\{u_i-\delta\}+\tau/m.
\]
These values and the entry time are independent of tie resolution. From time \(\tau\) onward, every block of \(m\) consecutive winners contains every index exactly once, in the order determined by descending fractional parts \(\{u_i-\delta\}\) and the fixed tie priority, and the state is periodic with **least period exactly \(m\)**. In particular \(T^{t+m}(u)=T^t(u)\) for all \(t\ge\tau(u)\).

## Assumptions and scope
The map is the *modified*, not historical, Frege rule. The vote shares remain identically \(1/m\) and \(u\) is any real vector; one may additionally restrict to the zero-sum hyperplane without changing the result. A deterministic, state-independent index-priority rule is imposed at ties to define a single-valued map. Statements about the exact entry state and \(m\)-block counts remain valid even when ties are chosen differently on successive visits. No assertion is made for unequal vote shares, and the first width-one entry need not equal the shortest possible preperiod of the eventual cycle.

## Proof
Let \(N_i(t)\) count allocations to index \(i\) before time \(t\). By induction,
\[
T^t(u)_i=u_i+t/m-N_i(t).
\]
Thus its winning index is any maximizer of the **head** \(h_i(t)=u_i-N_i(t)\); a winning head decreases by exactly one. Each index supplies an ordered stack of priorities \(u_i,u_i-1,u_i-2,\ldots\). At every update the maximum currently exposed priority is removed.

Set \(\delta=\min_i u_i\). The stack for index \(i\) has exactly \(k_i=\lfloor u_i-\delta\rfloor\) priorities at least \(\delta+1\), namely \(u_i,u_i-1,\ldots,u_i-k_i+1\), with the list empty if \(k_i=0\). Their total number is \(\tau=\sum_i k_i\). Until all these priorities have been removed, an exposed one remains at least \(\delta+1\); hence the greedy rule cannot select a priority below \(\delta+1\). It therefore removes *all and only* these priorities in the first \(\tau\) updates, independent of ties. An index initially at \(\delta\) has not been selected. Consequently the minimum head is exactly \(\delta\) for every \(t\le \tau\), while the maximum head is at least \(\delta+1\) for every \(t<\tau\). The head range is therefore at least one before \(\tau\). At \(\tau\), each head equals
\[
h_i(\tau)=u_i-\lfloor u_i-\delta\rfloor=\delta+\{u_i-\delta\}\in[\delta,\delta+1),
\]
so the head range is strictly less than one, and the claimed initial entry and state formula follow.

Take any vector of heads with range strictly less than one. When its largest exposed head is selected and decremented by one, it becomes strictly *smaller* than every head not yet selected within the current block, since every original pair differs by less than one. Thus before an index can be selected again, every previously unselected index must be selected. The next \(m\) selections are a permutation of all indices, sorted by their initial heads (with the prescribed tie rule). After this block every head has decreased by one. Therefore the same ordering repeats in each subsequent block and
\[
T^{\tau+m}(u)_i=u_i+(\tau+m)/m-(N_i(\tau)+1)=T^{\tau}(u)_i.
\]
The identical reasoning applies after each block. For the least period, if \(T^{t+k}(u)=T^t(u)\) for a positive integer \(k\), then from every coordinate's difference formula, \(k/m=N_i(t+k)-N_i(t)\) is an integer. Hence \(m\) divides \(k\). The exhibited period \(m\) is therefore the least possible.

The entry time can be arbitrarily large even with fixed \(m\): take \(u=(N,0,\ldots,0)\) for any positive integer \(N\), yielding \(\tau=N\). A common additive shift gives the same example on the zero-sum hyperplane. The argument establishes all quantified assertions for all real starting vectors, not merely rational test points.

## Verification
The accompanying `checker.py` independently computes the exact rational greedy updates under lowest-index priority; it checks \(\tau\), non-entry at every earlier step, the explicit state and repeated \(m\)-step return, and unbounded-sharp examples. Running `python3 checker.py` gives `PASS 3403 finite tests: exact entry, strict pre-entry, m-step periodicity, and sharp examples`. Tests are finite consistency checks, not the proof for arbitrary real data. The proof is the exact threshold-stack counting and whole-block argument above.

## Relationship to prior work
Conze, Janson and Öberg (arXiv:2611.13996v1, first posted 10 November 2026) establish exact period \(Q\) for their rational Frege map on a specified initial cube (Theorem 6.1), eventual period a multiple of \(Q\) for arbitrary real initial vectors (Theorem 6.4), and explicitly leave global exact period \(Q\) open (Problem 6.3). Here \(Q=m\), and the equal-share case is fully settled for *every* real initial vector with an additional exact hitting-time and entry-state formula. The present result does not solve their problem for unequal rational shares. Adler et al. (2005) treat general convex dynamics and orbit boundedness; Adler et al. (2009/2010) treat eventual entry into invariant fundamental domains in restricted dimensions. Neither of the inspected accessible statements gives the all-dimensional exact equal-share entry-time formula. Known connections with greedy chairman assignment and priority-stack merging are acknowledged; previously implicit equivalence or priority of an exact formula remains a historical risk.

## Limitations
The exact first hitting time concerns the strict range-one head condition, **not** the shortest possible preperiod: a trajectory can already be on an \(m\)-cycle while its head range is at least one. The strict range-one condition need not persist at each *intermediate* step of an \(m\)-block when initial fractional heads tie; the period conclusion applies to the full \(m\)-step block. The method uses equal shares essentially. The prior-literature comparison is not an independent exhaustive historical audit; the complete 2009 constant-input paper could not be substantively inspected beyond the publisher abstract.

## References
1. J.-P. Conze, S. Janson, A. Öberg, *Frege's election method: discrepancy, invariant polygons and Farey geometry*, arXiv:2611.13996v1, 10 November 2026, https://arxiv.org/html/2611.13996v1, especially Sections 2, 5, 6, Theorems 6.1, 6.4, and Problem 6.3.
2. R. L. Adler, B. Kitchens, M. Martens, C. Pugh, M. Shub, C. Tresser, *Convex Dynamics and Applications*, arXiv:math/0402115, https://arxiv.org/abs/math/0402115, especially Theorem 1.1 and its scheduling interpretation.
3. R. L. Adler, T. Nowicki, G. Świrszcz, C. Tresser, *Convex dynamics with constant input*, *Ergodic Theory and Dynamical Systems* 30 (2010), 957–972, first published online 30 September 2009, https://doi.org/10.1017/S0143385709000595 (publisher abstract accessible).
