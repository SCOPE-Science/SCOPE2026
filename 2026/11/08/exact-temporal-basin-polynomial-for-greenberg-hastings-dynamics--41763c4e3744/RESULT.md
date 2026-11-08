# Exact temporal-basin polynomial for Greenberg–Hastings dynamics on complete bipartite graphs

## Finding

For every pair of positive integers \(m,n\), consider the labelled complete bipartite graph \(K_{m,n}\) and the synchronous three-state Greenberg–Hastings rule. Define \(T(x)\) to be the least nonnegative number of updates needed for an initial configuration \(x\) to lie on a periodic orbit, and \(p(x)\) to be the least period of that orbit. The **joint first-entry-time and eventual-period distribution** is determined, with no simulation of large graphs, by the following ten potentially nonzero entries. Every unlisted entry is zero; some displayed entries vanish for small shore sizes.

Put
\[
 u=2^m-2,\quad U=2^n-2,\qquad
 v=3^m-3\cdot2^m+3,\quad V=3^n-3\cdot2^n+3.
\]
Let \(N_{t,p}(m,n)=\#\{x:T(x)=t,\ p(x)=p\}\). Then

| \((t,p)\) | \(N_{t,p}(m,n)\) |
|---|---|
| \((0,1)\) | \(1\) |
| \((0,3)\) | \(vV\) |
| \((0,4)\) | \(2uU\) |
| \((1,1)\) | \(3+2u+2U+uU\) |
| \((1,4)\) | \(2uU+uV+vU\) |
| \((2,1)\) | \(3+3u+3U+uU+v+V\) |
| \((2,4)\) | \(2uU+uV+vU\) |
| \((3,1)\) | \(2+2u+2U+uU+v+V\) |
| \((3,4)\) | \(uV+vU\) |
| \((4,1)\) | \(2u+2U+v+V\) |

Thus the two-variable finite-time generating polynomial is
\[
\begin{aligned}
\mathcal E_{m,n}(z,w)= {}&1+vVw^3+2uUw^4\\
&+z\bigl(3+2u+2U+uU+(2uU+uV+vU)w^4\bigr)\\
&+z^2\bigl(3+3u+3U+uU+v+V+(2uU+uV+vU)w^4\bigr)\\
&+z^3\bigl(2+2u+2U+uU+v+V+(uV+vU)w^4\bigr)\\
&+z^4(2u+2U+v+V).
\end{aligned}
\]
Here a monomial \(z^tw^p\) records a configuration's first-entry time and eventual least period; \(w^0\) does not occur. In particular the maximum first-entry time is four whenever \(\max\{m,n\}\ge2\), and is three for \(m=n=1\). The last-time population is exactly \(2u+2U+v+V\), and **every last-time configuration becomes extinct**. For a uniform random initial assignment, divide each displayed count by \(3^{m+n}\).

The eventual period-four basin has \(6uU+3uV+3vU\) initial states, whereas the period-three basin consists exactly of its \(vV\) initially periodic states. These aggregate counts are consequences of, rather than replacements for, the time-resolved theorem; the already known enumeration of recurrent configurations is not claimed as new.

## Assumptions and scope

The graph has two disjoint labelled shores, of respective sizes \(m,n\ge1\), with every edge between distinct shores and none within a shore. Vertices take values \(0\) (quiescent), \(1\) (excited), \(2\) (refractory). At one simultaneous update, \(1\mapsto2\), \(2\mapsto0\); a \(0\) becomes \(1\) exactly if some vertex in the opposite shore is presently \(1\), and otherwise remains \(0\). No random update, probabilistic transition, threshold above one, or asynchronous convention is included. Every initial configuration is counted once, with vertex labels distinguished.

For \(t\ge0\), the first-entry time means the smallest \(t\) such that the complete configuration at that time belongs to a genuine periodic orbit, not the time when a support pattern first repeats with a possible internal transient. The proof below establishes that these two times coincide for this graph family.

## Proof

**1. Closed support dynamics.** Let \(A(x)\) and \(B(x)\) be the *sets* (not multisets) of colors present on the left and right shores. Each is a nonempty subset of \(\{0,1,2\}\). Since every vertex in one shore receives the same excitation indicator from the other, the support pair evolves autonomously. Define
\[
 f_e(0)=e,\qquad f_e(1)=2,\qquad f_e(2)=0,
 \qquad e\in\{0,1\}.
\]
The induced support map is
\[
 \Phi(A,B)=\bigl(f_{\mathbf1_{1\in B}}(A),
                     f_{\mathbf1_{1\in A}}(B)\bigr),
\]
where a function acts on a set elementwise. This identity is exact for every choice of shore sizes; multiplicities do not affect it.

**2. A finite, complete support transition analysis.** Write \(01=\{0,1\}\), \(02=\{0,2\}\), \(12=\{1,2\}\), and \(012=\{0,1,2\}\). There are exactly seven possible nonempty supports per shore and hence 49 support pairs. Direct substitution into the two functions \(f_0,f_1\) proves that the only recurrent support components are
\[
 (0,0)\longrightarrow(0,0),\qquad
 (012,012)\longrightarrow(012,012),
\]
and
\[
 (01,02)\longleftrightarrow(02,01).
\]
For complete reproducibility, the finite support-distance table follows. The entry \(t/p\) indicates that this starting support pair first reaches one of those three recurrent support components after \(t\) support updates, and its underlying full-state eventual least period is \(p\).

| Left / right | 0 | 1 | 2 | 01 | 02 | 12 | 012 |
|---|---|---|---|---|---|---|---|
| 0 | 0/1 | 3/1 | 1/1 | 4/1 | 1/1 | 4/1 | 4/1 |
| 1 | 3/1 | 2/1 | 2/1 | 3/1 | 3/1 | 2/1 | 3/1 |
| 2 | 1/1 | 2/1 | 1/1 | 2/1 | 1/1 | 2/1 | 2/1 |
| 01 | 4/1 | 3/1 | 2/1 | 3/1 | 0/4 | 2/4 | 3/4 |
| 02 | 1/1 | 3/1 | 1/1 | 0/4 | 1/1 | 1/4 | 1/4 |
| 12 | 4/1 | 2/1 | 2/1 | 2/4 | 1/4 | 2/1 | 2/4 |
| 012 | 4/1 | 3/1 | 2/1 | 3/4 | 1/4 | 2/4 | 0/3 |

The table can also be checked without orbit assumptions: determine the four displayed recurrent support states from the elementwise formula, and apply \(\Phi\) repeatedly to each of the other 45 pairs. Every row entry is reached in at most four substitutions. The standalone support checker performs this exact finite enumeration and records the coefficient multiplicities independently.

**3. Support recurrence is full-state recurrence.** A configuration with support pair \((0,0)\) is all quiescent and fixed. In a configuration with supports \((012,012)\), both shores contain an excited vertex, so *every* vertex advances under the bijection \(0\mapsto1\mapsto2\mapsto0\) on every step; its least period is three. When the supports are \((01,02)\) or \((02,01)\), they swap at the next support update, and two updates exchange the two colors within each shore. Thus four updates restore every vertex, while two updates do not, proving least period four. Outside these support classes, the support has not yet entered a support cycle, so the full configuration is not periodic. Consequently its full-state first-entry time is **exactly** the support-table time \(t\), for all configurations.

**4. Enumeration.** For each fixed nonempty subset \(S\subseteq\{0,1,2\}\) of size \(k\), the number of length-\(r\) labelled shore assignments with *exact* support \(S\) is
\[
 a_k(r)=\sum_{j=0}^k(-1)^j\binom kj(k-j)^r.
\]
For positive \(r\), this yields \(a_1(r)=1\), \(a_2(r)=2^r-2\), and \(a_3(r)=3^r-3\cdot2^r+3\). Group the 49 support-table entries by their values \((t,p,|A|,|B|)\). Each such entry contributes \(a_{|A|}(m)a_{|B|}(n)\) configurations. For example, for \((t,p)=(2,4)\), there are two support pairs of sizes \((2,2)\), one of sizes \((2,3)\), and one of sizes \((3,2)\), giving \(2uU+uV+vU\). The other nine lines follow in the same way and are itemized independently by the support checker. The sum over all ten classes is \(3^{m+n}\), because the 49 nonempty support pairs partition all initial configurations. This proves the displayed joint law without a parameter cutoff.

**5. Sharp boundary.** The table's maximal entry is four; entries of first-entry time four appear, for instance, at initial support pairs \((0,01)\) and \((01,0)\). They are realizable exactly when at least one shore has size two or greater. If both shores have one vertex, neither support can contain two colors, and the largest of the singleton/singleton entries is three. This proves the sharp bounds including both smallest-shore edge cases.

## Verification

Run the two bundled Python 3 scripts with no third-party dependencies:

```
python3 verify_support.py
python3 verify_direct.py
```

`verify_support.py` rebuilds all 49 support transitions from the elementary rule, independently classifies their \((t,p)\) and support cardinalities, checks the aggregate basins, and verifies the resulting identities for 900 pairs of positive integers. `verify_direct.py` instead enumerates and iterates **every labelled full configuration** for all 28 parameter pairs \((m,n)\) with \(m,n\ge1\), \(m+n\le8\): a total of 63,972 configurations. It compares first-entry times and genuine eventual least periods to the closed formulas, without relying on support histories. Both scripts must terminate with `SUPPORT_OK` and `DIRECT_OK`, respectively. Captured outputs are included. The uniform formulas are mathematical consequences of the exact support map and onto-counting proof, not extrapolations from tested parameters.

As an example, for \(m=n=3\) the classes in ascending \((t,p)\) order have counts \(1,36,72,63,144,87,144,74,72,36\), totalling \(3^6=729\).

## Relationship to prior work

Greenberg and Hastings introduced the excitable update mechanism in 1978. Durrett and Griffeath's dated 1993 preprint studies asymptotic excitable cellular automata in lattice settings. Gravner, Lyu and Sivakoff (arXiv:1610.07320, publicly posted 24 October 2016) prove general finite-graph criteria for fixation versus oscillation and characterize eventual activity; these results do not state a complete finite-time, period-resolved basin polynomial for \(K_{m,n}\). Doba (2018) also gives the general cycle-density criterion and excitation-rate law rather than this ten-class time-of-entry enumeration. The recurrence types and counts on complete bipartite graphs have already been classified more generally for arbitrary numbers of Greenberg–Hastings colors; they are used here only as consistency checks. The present claim is specifically the **complete and sharp joint first-entry-time distribution** for the three-state model; period-only classifications are not presented as new.

## Limitations

This theorem is specific to three states, synchronous updates, threshold-one triggering and intact complete bipartite graphs. It does not count basins for unequal thresholds, arbitrary multipartite graphs, a deleted edge, stochastic updates, or higher-color variants. No assertion is made about the uniqueness of the result across all unindexed historical literature. All conclusions have an elementary all-parameter proof; computational output is corroborative only. The model has no external experimental validation in this result.

## References

1. J. M. Greenberg and S. P. Hastings (1978), “Spatial Patterns for Discrete Models of Diffusion in Excitable Media,” *SIAM J. Appl. Math.* 34(3), 515–523, DOI 10.1137/0134040.
2. R. Durrett and D. Griffeath (1993), “Asymptotic Behavior of Excitable Cellular Automata,” arXiv:patt-sol/9303002, publicly posted 22 March 1993.
3. J. Gravner, H. Lyu and D. Sivakoff (2016), “Limiting behavior of 3-color excitable media on arbitrary graphs,” arXiv:1610.07320, first posted 24 October 2016.
4. N. Doba (2018), “The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph,” *Complex Systems* 27(2), 101–126, DOI 10.25088/ComplexSystems.27.2.101.
