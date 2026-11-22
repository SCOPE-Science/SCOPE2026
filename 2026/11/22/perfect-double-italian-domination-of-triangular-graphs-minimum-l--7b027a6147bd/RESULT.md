# Perfect double Italian domination of triangular graphs: minimum-label rigidity and cycle enumeration

## Finding

For every integer \(n\ge5\), let \(T_n=L(K_n)\), with each vertex of \(T_n\) representing an unordered pair from \([n]\). A perfect double Italian dominating function is a map \(f:V(T_n)\to\{0,1,2,3\}\) such that whenever \(f(e)\in\{0,1\}\), the sum over the closed neighborhood of \(e\) lies in \(\{3,4\}\). Its weight is \(w(f)=\sum_{e\in E(K_n)}f(e)\).

**Theorem.** For all \(n\ge5\), \(\gamma_{dI}^{p}(T_n)=n\). Moreover a feasible function has weight \(n\) if and only if its root weighted degrees
\[
 d_f(v):=\sum_{e\ni v}f(e)
\]
are all exactly \(2\). Thus every minimum labeling is uniquely a vertex-disjoint union of ordinary simple cycles of length at least three (their edges have label \(1\)) and doubled edges (their single underlying edge has label \(2\)); all remaining edges have label \(0\). No label \(3\) occurs in an optimum.

Let \(a_n\) be the number of minimum functions on the fixed labeled root graph \(K_n\) for \(n\ge5\), and let \(b_n\) be the number of these cycle/double-edge decompositions for every \(n\ge0\). The complete exponential generating function of the decompositions is
\[
 \sum_{n\ge0}b_n\frac{x^n}{n!}
 =\exp\!\left(\frac{x^2}{2}+\sum_{j\ge3}\frac{x^j}{2j}\right)
 =\frac{\exp(-x/2+x^2/4)}{\sqrt{1-x}},
 \qquad a_n=b_n\quad(n\ge5).
\]
With \(u\) recording the number of doubled edges, the refined generating function is
\[
 \sum_{n,t\ge0}b_{n,t}\frac{x^n}{n!}u^t
 =\frac{\exp(-x/2+(2u-1)x^2/4)}{\sqrt{1-x}}.
\]
The first optimum counts are \(a_5=22\), \(a_6=130\), \(a_7=822\), \(a_8=6202\), \(a_9=52552\), and \(a_{10}=499194\). In particular,
\[
 a_n\sim\frac{e^{-1/4}n!}{\sqrt{\pi n}}
 \quad(n\to\infty).
\]

## Assumptions and scope

The complete graph \(K_n\) is simple, its ground vertices are distinguished, and \(T_n\) is its line graph. The closed neighborhood of root edge \(uv\) in \(T_n\) consists of all root edges incident to \(u\) or \(v\), counted once. The label convention is precisely that of Hao, Jalilolghadr and Mojdeh (2023): labels \(0,1,2,3\); a restriction to closed-neighborhood total between \(3\) and \(4\) only at vertices labeled \(0\) or \(1\). The proof applies to every integer \(n\ge5\) and does not extend the optimizer characterization to smaller orders.

## Proof

**Neighborhood identity.** For any labeling \(f\) on root edges, and any root edge \(uv\), the closed-neighborhood sum in \(T_n\) is
\[
 s_f(uv)=d_f(u)+d_f(v)-f(uv).
\]
The subtraction accounts for the root edge counted at both ends.

**Small-degree obstruction.** There cannot be two distinct root vertices \(u,v\) with \(d_f(u),d_f(v)\le1\). Indeed \(f(uv)\le1\), and so \(s_f(uv)\le2\), violating the required lower bound \(3\) for a label at most \(1\).

**Weight bound.** Since \(\sum_v d_f(v)=2w(f)\), if \(w(f)\le n-1\), some root degree is at most \(1\). By the preceding obstruction this is the only one. Every other degree is at least \(2\), hence \(2w(f)\ge2(n-1)+d_f(u)\). The assumed bound forces \(d_f(u)=0\), all others equal \(2\), and \(w(f)=n-1\). But each \(uv\) incident to \(u\) then has label \(0\) and \(s_f(uv)=2\), contradiction. Thus \(w(f)\ge n\).

**Rigidity at equality.** Suppose \(w(f)=n\). If every root degree is at least \(2\), their sum \(2n\) makes every degree exactly \(2\). Otherwise there is exactly one degree-at-most-one vertex \(u\).

If \(d_f(u)=0\), then for every \(v\ne u\), the edge \(uv\) has label \(0\), so \(d_f(v)\ge3\). This forces \(\sum_vd_f(v)\ge3(n-1)>2n\) for \(n\ge5\), impossible.

If \(d_f(u)=1\), exactly one other vertex \(v\) has root degree \(3\) and all remaining degrees equal \(2\). The unique label-\(1\) edge incident to \(u\) must be \(uv\): choosing a degree-\(2\) endpoint would give closed-neighborhood sum \(1+2-1=2\). For each of the \(n-2\) other vertices \(z\), the edge \(vz\) must have a positive label, since a zero label would have neighborhood total \(3+2=5\). But \(v\) has weighted degree \(3\), with one unit already on \(uv\), leaving only two units; this would require \(n-2\le2\), impossible for \(n\ge5\). Thus all degrees equal \(2\).

**Converse and classification.** Whenever all degrees equal \(2\), no edge label exceeds \(2\). A zero edge has neighborhood sum \(4\), and a one edge has neighborhood sum \(3\); two edges are unrestricted. Thus every such labeling is feasible and has weight \(n\). Interpreting label \(2\) as two parallel copies of a root edge produces a loopless degree-two multigraph. Its components are precisely doubled pairs and ordinary cycles of length at least three. Conversely those components uniquely specify \(f\), proving the structural statement.

**Counting.** A doubled pair on \(2\) chosen root vertices has one realization, hence component EGF \(x^2/2\). On \(j\ge3\) fixed vertices there are \((j-1)!/2\) undirected Hamiltonian cycles, hence component EGF \(x^j/(2j)\). The labeled exponential formula gives the stated product and its refinement by \(u\). Algebraically \(\sum_{j\ge3}x^j/(2j)=(-\log(1-x)-x-x^2/2)/2\). The recurrence
\[
 b_0=1,\quad b_1=0,\quad b_2=1,\qquad
 b_{n+1}=n b_n+n b_{n-1}-\frac{n(n-1)}2 b_{n-2}\quad(n\ge2)
\]
follows by logarithmic differentiation. Finally the analytic factor at \(x=1\) is \(e^{-1/4}\), giving the stated asymptotic by the standard coefficient estimate for \((1-x)^{-1/2}\).

## Verification

Run `python3 verify_direct.py` to enumerate every ternary/quad-label assignment with total weight at most \(n\) directly on the closed neighborhoods for \(n=5,6,7\). It reports respectively \(22,130,822\) feasible labelings, all of weight \(n\), after testing \(2893\), \(52224\), and \(1141536\) labelings. This finite exhaustion checks the indicated small orders; it is not used as the proof for all orders.

Run `python3 verify_cycles.py` to independently construct every cycle/doubled-edge support on labeled root sets for \(5\le n\le9\), check its neighborhood conditions, and compare the resulting counts and doubled-edge histograms with an independently implemented exponential-formula recurrence through \(n=12\). Both programs use only the standard Python library. The mathematical proof above establishes the infinite assertion.

## Relationship to prior work

Hao, Jalilolghadr and Mojdeh (2023) define perfect double Italian domination and establish results for paths, cycles, complete multipartite graphs and other graph classes, but no corresponding exact optimal-label classification for \(L(K_n)\) was identified in the inspected text. A public result on **square rook graphs** also links minimum perfect double Italian functions to weighted degree conditions, but concerns \(K_n\square K_n\), not triangular graphs. A public result on the ordinary **Roman domination polynomial** of triangular graphs concerns a different labeling rule, and its weight formula does not imply the present theorem. The standard enumeration of undirected cycles is not itself claimed as a new combinatorial counting principle; its identification as exactly the optimum-label space is the contribution.

## Limitations

The result covers \(n\ge5\) only and the perfect double Italian convention with a closed-neighborhood interval constraint on labels \(0,1\). It is not a result about perfect Roman domination, perfect double Roman domination, or arbitrary line graphs. The formulas enumerate minimum-weight functions, not the full weight polynomial. Full historical publication priority and independent mathematical validation have not been established.

## References

1. G. Hao, P. Jalilolghadr, D. A. Mojdeh, “Perfect double Italian domination of a graph,” *AKCE International Journal of Graphs and Combinatorics* 20 (2023), 247–257. https://doi.org/10.1080/09728600.2023.2218457. Published online 2023-06-21.
2. M. Chellali, N. Jafari Rad, S. M. Sheikholeslami, L. Volkmann, “Varieties of Roman domination II,” *AKCE International Journal of Graphs and Combinatorics* 17 (2020), 966–984. https://doi.org/10.1016/j.akcej.2019.12.001. Defines the earlier nonperfect Roman \(\{{3\}}\) variant, not the same exact constraint.
3. “Perfect double Italian domination of square rook graphs,” public mathematical result record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-perfect-double-italian-domination-of-square-rook-graphs--4f59f40e97e0 (public summary inspected).
4. “Roman-domination polynomial of triangular graphs, with minimum-function census,” public mathematical result record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-roman-domination-polynomial-of-triangular-graphs-with-minimum-fu--66092f59608f (public summary inspected).
