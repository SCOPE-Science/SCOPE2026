# Optimal placement of two cross-links between parallel paths: a modulo-five law

## Finding

Take two disjoint copies of the unit-resistance path \(P_m\), with vertices \((s,t)\), \(s\in\{0,1\}\), \(1\le t\le m\), and \(m\ge2\). Add precisely two unit-resistance rungs between corresponding vertices at indices \(1\le i<j\le m\). Among all choices of the two indices, the minimum Kirchhoff index \(K(G)=\sum_{\{u,v\}\subset V(G)}R_{\mathrm{eff}}(u,v)\) is attained exactly as follows:

- If \(m=5k\) (necessarily \(k\ge1\)), the two and only two minimizing pairs are \((i,j)=(k,4k)\) and \((i,j)=(k+1,4k+1)\).
- If \(m=5k+s\) with \(s\in\{1,2,3,4\}\), the unique minimizing pair is \((i,j)=(k+1,m-k)\).

In particular the optimal rung locations approach one-fifth and four-fifths of each rail, not the endpoints. The minimum satisfies \(K_{\min}(m)=\frac{8}{15}m^3+O(m^2)\).

## Assumptions and scope

Both rails are paths with \(m\) vertices; all original edges and both added rungs have unit resistance. The two added rungs use distinct corresponding indices. The minimization is discrete over all \(\binom{m}{2}\) possible positions, not over nonuniform edge weights, arbitrary cross-links, or additional rungs. The graph is connected and unicyclic. The Kirchhoff index is the unscaled sum over unordered pairs, not the pair-average or normalized Laplacian index.

Define \(l=i-1\), \(r=m-j\), and \(q=j-i+1\). Thus \(l+r+q=m\), \(q\ge2\), and the unique cycle has length \(2q\). The exact index at every legal placement is

\[
K(G_{m;i,j})=
\frac{m}{6q}\left(5m^2q-6mq^2+12mq-3m+5q^3-12q^2+2q\right)
+\frac m2(l-r)^2.
\]

## Proof

**Exact resistance formula.** The two rails between the rungs and the rungs themselves form a simple cycle \(C_{2q}\). Four unit paths (possibly of length zero) attach at the four cycle corners: two lengths equal \(l\), and two equal \(r\). The unique path from any pendant vertex to its attachment corner is in series with the remaining graph. For a cycle of length \(L\), effective resistance between corners at cyclic distance \(d\) equals \(d(L-d)/L\); the cycle's Kirchhoff index is \((L^3-L)/12\), and the sum of resistances from any corner to the entire cycle is \((L^2-1)/6\).

For one pendant path of length \(t\), the contribution from its \(t\) non-corner vertices to old cycle vertices is \(Lt(t+1)/2+t(L^2-1)/6\); among its non-corner vertices the contribution is \(t(t^2-1)/6\). For two different pendant paths of lengths \(t\) and \(u\) at corners \(v,w\), the contribution between their non-corner vertices is \(tu(t+u+2)/2+tuR_{C_L}(v,w)\). In the present cycle, the corner resistance across either rung is \((2q-1)/(2q)\), and the sum of the four left-right corner resistances is \((2q^2-1)/q\). Summing the cycle, four individual paths and all six cross-path contributions, and simplifying with \(m=l+r+q\), gives the displayed exact formula. This derivation is valid also for zero-length tails.

**Balancing.** Holding \(q\) fixed, the only part depending on \(l,r\) is \(m(l-r)^2/2\); hence the best lengths differ by at most one, with both orientations allowed if \(m-q\) is odd. Write \(\epsilon_q\in\{0,1\}\) for the parity of \(m-q\), and \(a=(3m+6)/5\). Removing a term independent of \(q\) and multiplying by \(6/m\), the balanced objective is
\[
F_m(q)=5(q-a)^2-\frac{3m}{q}+3\epsilon_q,
\quad 2\le q\le m.
\]

**Unique cycle length.** Write \(m=5k+s\), \(s\in\{0,1,2,3,4\}\), and set
\[
q_* =\begin{cases}3k+1,&s=0,1,\\3k+2,&s=2,\\3k+3,&s=3,\\3k+4,&s=4.\end{cases}
\]
For all \(m\ge2\), \(2\le q_*\le m\), \(m/q_*\le5/3\), and \(\delta=q_*-a\) is respectively \(-1/5,-4/5,-2/5,0,2/5\). Put \(H(q)=5(q-a)^2+3\epsilon_q\).

For a feasible \(q=q_*+d\), \(d\ge1\), one has \(H(q)-H(q_*)=5d^2+10\delta d+3(\epsilon_q-\epsilon_{q_*})\). When \(d=1\), these differences for residues \(s=0,1,2,3,4\) are respectively \(0,0,4,8,12\); for \(d\ge2\) they are at least \(5d^2-8d-3>0\). Since \(-3m/q\) is strictly increasing, every \(q>q_*\) has larger objective.

For a feasible \(q=q_*-d\), \(d\ge1\), one has \(H(q)-H(q_*)=5d^2-10\delta d+3(\epsilon_q-\epsilon_{q_*})\). At \(d=1\), the five residues yield \(4,16,12,8,4\). At \(d\ge2\), the difference is at least \(5d^2-4d-3\). Meanwhile the adverse fractional term has magnitude
\[
3m\left(\frac1q-\frac1{q_*}\right)=\frac{3md}{qq_*}\le\frac52d
\]
using \(q\ge2\) and \(m/q_*\le5/3\). For \(d=1\), \(4>5/2\); for \(d\ge2\), \(5d^2-4d-3>(5/2)d\). Hence every \(q<q_*\) is worse. The optimal cycle length is unique.

For \(s=0\) the two balanced arms have lengths \((k-1,k)\) and \((k,k-1)\); these produce exactly the two index pairs in the finding. For \(s\ne0\), both arms have length \(k\), producing the unique stated pair. Substitution of \(q_*/m\to3/5\) and bounded arm imbalance into the exact formula yields \(K_{\min}/m^3\to(5-6(3/5)+5(3/5)^2)/6=8/15\), with an \(O(m^2)\) remainder.

## Verification

The included `verify_two_rungs.py` computes the exact Kirchhoff index independently from the rational inverse of \(L+J/(2m)\), where \(L\) is the combinatorial Laplacian and \(J\) is the all-ones matrix, via \(K=2m\operatorname{tr}((L+J/(2m))^{-1})-2m\). It compares every placement for \(2\le m\le7\) to the closed formula, and exhaustively checks the claimed optimum for \(2\le m\le100\). Execute with Python 3 and SymPy: `python verify_two_rungs.py`. Finite checks are supplementary to the proof for arbitrary \(m\).

## Relationship to prior work

Carmona, Encinas and Mitjana (2014) developed effective-resistance and Kirchhoff-index expressions for ladder-like chains formed by adding consecutive cross-edges to a path. The present problem selects exactly two potentially widely separated cross-links between independent parallel paths and optimizes their placement over all integer positions; general index formulas do not themselves state this modulo-five optimizer classification. Chen and Yan (2021) derived a general matching-theoretic formula for the Kirchhoff index of every unicyclic graph; it gives a method to calculate an instance but not a placement minimizer without additional optimization. Neither prior formula is claimed as new here.

## Limitations

The theorem is for two identical unit-resistance rails and exactly two identical corresponding rungs. It does not optimize variable conductances, more cross-links, independent rail lengths, or other network objectives. The closest ladder-chain paper's full text was unavailable in the material inspected; although its published model uses consecutive rungs and the precise extremal classification was not visible in its abstract, that access limitation leaves a residual prior-art risk. An independent review has not been performed.

## References

- A. Carmona, A. M. Encinas and M. Mitjana, “Effective resistances for ladder-like chains,” *International Journal of Quantum Chemistry* **114** (2014), 1670–1677. First published 24 July 2014. https://doi.org/10.1002/qua.24740
- Y. Chen and W. Yan, “On the Kirchhoff index of a unicyclic graph and the matchings of the subdivision,” *Discrete Applied Mathematics* **300** (2021), 19–24. https://doi.org/10.1016/j.dam.2021.05.007
- D. J. Klein and M. Randić, “Resistance distance,” *Journal of Mathematical Chemistry* **12** (1993), 81–95. https://doi.org/10.1007/BF01164627
