# Exact global entry time and round-robin tail for equal-share Frege dynamics

## Finding
Fix an integer \(m\ge 2\) and an arbitrary real initial score vector \(u\in\mathbb R^m\). In the equal-share modified Frege map, update
\[
T(x)=x+(1/m,\ldots,1/m)-e_{i(x)},
\]
where \(i(x)\) maximizes \(x_i+1/m\), using a fixed priority order among tied indices. Write \(\delta=\min_i u_i\), \(\{s\}=s-\lfloor s\rfloor\), and \(N_i(t)\) for the number of wins of index \(i\) in the first \(t\) steps. The first time at which the range of the relative scores \(u_i-N_i(t)\) is strictly less than one is exactly
\[
\tau(u)=\sum_{i=1}^m\lfloor u_i-\delta\rfloor.
\]
At that time,
\[
N_i(\tau)=\lfloor u_i-\delta\rfloor,\qquad
T^{\tau}(u)_i=\delta+\{u_i-\delta\}+\tau/m.
\]
With fixed tie priority, the winners from time \(\tau\) onward repeat the permutation sorted by descending fractional parts \(\{u_i-\delta\}\), with ties in priority order. Consequently every block of \(m\) consecutive winners after entry contains all indices once, and the states from entry have least period exactly \(m\).

## Assumptions and scope
The vote shares stay identically \(1/m\). One may restrict \(u\) to the zero-sum hyperplane without changing the conclusions. If tie choices are allowed to vary with time, the exact entry time and state still hold and the successive length-\(m\) blocks **starting at** times \(\tau+jm\), \(j\ge0\), still contain each index once. Arbitrary sliding length-\(m\) blocks need not then have this property. The first strict range-one entry is not claimed to equal the shortest preperiod of the eventual cycle.

## Proof
Induction on the update gives \(T^t(u)_i=u_i+t/m-N_i(t)\), so a winner maximizes the head \(h_i(t)=u_i-N_i(t)\). Equivalently each index supplies an ordered stack \(u_i,u_i-1,u_i-2,\ldots\), and each step removes the largest exposed priority.

For index \(i\) there are exactly \(k_i=\lfloor u_i-\delta\rfloor\) priorities at least \(\delta+1\). They form the initial segment of its stack. As long as any remain, at least one is exposed; hence the greedy rule removes all and only these priorities in the first \(\sum_i k_i\) steps, regardless of ties. An index originally at \(\delta\) remains unselected throughout these steps, and the smallest head equals \(\delta\) for every \(t\le\tau\). The largest head is at least \(\delta+1\) for \(t<\tau\), whereas at \(t=\tau\) all heads equal \(\delta+\{u_i-\delta\}\) and lie in \([\delta,\delta+1)\). This proves first entry and the exact score vector.

From heads of range strictly less than one, the decrement of any selected head places it strictly below every not-yet-selected head in that round. Thus the next \(m\) winners are a permutation of the indices, and after these steps each head is the corresponding initial head minus one. This proves the aligned block assertion even with variable ties. With fixed tie priority, subtracting a common constant preserves the full ranking including ties; the very same permutation repeats. Therefore the sliding block assertion holds in this case. After a round, the common gain \(m/m\) offsets the one win per index, so \(T^{\tau+m}(u)=T^\tau(u)\). If any state recurs after \(d>0\) further steps, the coordinate difference formula forces \(d/m=N_i(t+d)-N_i(t)\) to be an integer. Thus \(m\mid d\), proving the least period.

Entry time is unbounded even at fixed \(m\): take \(u=(N,0,\dots,0)\) for a positive integer \(N\). Subtracting the mean gives the same entry time on the zero-sum hyperplane.

## Verification
The companion `checker.py` implements exact rational score updates under lowest-index priority. It checks the entry formula, strict nonentry before that time, the exact entry state and aligned \(m\)-step recurrence in 3,403 finite tests. It is a diagnostic, not the proof for arbitrary reals. To check the distinction for varying ties, start at \(m=2\), \(u=(0,0)\). Resolve the first tie in favor of index 1 and the next tie in favor of index 2. The winner sequence begins \(1,2,2,1\). The two aligned blocks are permutations, but the middle sliding block repeats index 2.

## Relationship to prior work
Conze, Janson and Öberg study the fixed rational-share Frege map: Theorem 6.1 gives exact period \(Q\) from a specified cube and for projected orbits, Theorem 6.4 gives global eventual periods that are multiples of \(Q\), and Problem 6.3 asks for a global exact-period result for unprojected orbits. Here \(Q=m\). Their §2.4 also identifies the Frege update with a previously studied greedy chairman-assignment algorithm. The threshold formula quantifies the time and state of first strict-range entry from arbitrary real initial score vectors in the uniform case only. General convex-dynamics boundedness is distinct from this exact first-hitting statement. The proof does not settle the global question for unequal rational shares.

## Limitations
The strict range-one condition may fail at an intermediate step in a round when initial fractional heads tie. Entry time can also exceed the preperiod: for \(m=2\), priority 1 before 2, and \(u=(0,1)\), the states cycle through \((0,1)\) and \((1/2,1/2)\) from the start, but \(\tau=1\). The result is specific to equal shares. Historical priority beyond inspected sources is not established.

## References
1. J.-P. Conze, S. Janson, J. Öberg, *Frege's election method: discrepancy, invariant polygons and Farey geometry*, arXiv:2611.13996v1, Sections 2, 5, 6. https://arxiv.org/html/2611.13996v1
2. R. L. Adler, B. Kitchens, M. Martens, C. Pugh, M. Shub, C. Tresser, *Convex Dynamics and Applications*, arXiv:math/0402115. https://arxiv.org/abs/math/0402115
3. R. L. Adler, T. Nowicki, G. Świrszcz, C. Tresser, *Convex dynamics with constant input*, *Ergodic Theory and Dynamical Systems* 30 (2010), 957–972. https://doi.org/10.1017/S0143385709000595
