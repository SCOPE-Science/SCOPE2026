# Four-step majority dynamics and exact oscillation basins on triangular clique windmills

## Finding
For each integer \(r\geq1\), let \(G_r=K_1\vee (rK_3)\): one central hub adjacent to every vertex of \(r\) pairwise disjoint labelled triangles. Apply synchronous binary **open-neighbor majority**: a vertex changes to the strict majority among its neighbors, and retains its previous state at a tie. Let \(F_r\) be this map on \(2^{3r+1}\) labelled binary states. Every orbit enters either a fixed point or a primitive two-cycle by its fourth update. The sharp worst-case first periodic-entry time is \(1\) for \(r=1\), \(3\) for \(r=2\), and \(4\) for every \(r\geq3\). In particular, \(F_r^6=F_r^4\) for every \(r\geq1\).

The exact number of fixed states is
\[
 f_r=2\sum_{b=0}^{\lfloor r/2\rfloor}\binom rb.
\]
Write \(T=3r/2\), and let the following sums run over nonnegative integers \(o,q\) with \(o+q\leq r\) and strict inequalities \(3o+q<T<3o+2q\). Then the exact number of **primitive temporal two-cycle orbits** and the total number of initial states eventually entering a two-cycle are respectively
\[
 c_r=\sum_{\substack{o,q\geq0,\ o+q\leq r\\3o+q<T<3o+2q}}
 \frac{r!\,3^q}{o!\,q!\,(r-o-q)!},\qquad
 b_r=2\sum_{\substack{o,q\geq0,\ o+q\leq r\\3o+q<T<3o+2q}}
 \frac{r!\,3^q4^{r-o-q}}{o!\,q!\,(r-o-q)!}.
\]
Thus precisely \(f_r+2c_r\) states are initially periodic, and the two-cycle basin has cardinality \(b_r\).

More strongly, the complete **first-entry-time and eventual-period census** is given by the finite, explicit category table in the Proof. In particular, every two-cycle-basin state enters its cycle at time \(0\) or \(1\), although the fixed-point basin can require four updates.

As \(r\to\infty\), \(c_r/5^r\to1\), with the explicit bound \(1-2e^{-r/50}\leq c_r/5^r\leq1\). Hence a uniform random initial state is already periodic with probability
\[
 \frac{f_r+2c_r}{2\cdot8^r}\sim\left(\frac58\right)^r.
\]

## Assumptions and scope
The graph is simple and undirected. The hub is the unique shared vertex of \(r\) copies of \(K_4\); equivalently, the \(3r\) outer vertices form \(r\) disjoint triangles, and each outer vertex has degree \(3\). The hub degree is \(3r\). All vertices update simultaneously using **neighbors only**, not a closed neighborhood. At ties (possible at the hub when \(r\) is even) the hub keeps its current bit. Initial states are labelled; two temporal states belonging to the same primitive two-cycle constitute one orbit. The first entry time is the smallest nonnegative update count at which the state is periodic.

For a state with hub \(0\), let \((z,o,p,q)\) count triangles with, respectively, zero, three, one and two occupied outer vertices. Here \(z+o+p+q=r\). A triangle with one occupied vertex has three choices, as does one with two occupied vertices. Consequently its labelled multiplicity is
\[
 w_r(z,o,p,q)=\frac{r!}{z!o!p!q!}\,3^{p+q}.
\]
Hub \(1\) states are counted symmetrically by global bit complement.

## Proof
**1. Exact local transition table.** With hub \(0\), a triangle with outer occupation number \(0,1,2,3\) moves respectively to occupation number \(0,0,1,3\). With hub \(1\), it moves respectively to \(0,2,3,3\). The locations of the unique occupied (respectively unoccupied) vertex in the mixed types determine the next positions uniquely: a two-occupied triangle under hub \(0\) becomes a singleton at its previously unoccupied vertex; that singleton under hub \(1\) returns to the original two-occupied pattern. This exact spatial return is essential, and is not inferred only from occupation counts.

Let \(T=3r/2\), \(K=3o+p+2q\), \(L=3o+q\), and \(U=3o+2q\) for an initial hub-zero state. The hub flips from \(0\) to \(1\) precisely when its occupied-neighbor count exceeds \(T\), and from \(1\) to \(0\) precisely when that count is below \(T\).

**2. Complete temporal classification.** If \(K\leq T\), the hub stays zero; after one update the outer triangles have \(z+p\) zeros, \(o\) full ones, and \(q\) singletons. Since \(L=3o+q\leq K\leq T\), the hub remains zero, the remaining singletons disappear on the next update, and the state is fixed by time two.

If \(K>T\), the hub is one at time one, with the same outer-triangle distribution \((z+p,o,q,0)\). When \(L\geq T\), the hub stays one at time two and the \(q\) singleton triangles become two-occupied; the next update sends them to full ones. The hub cannot thereafter flip because the occupied-neighbor count is nondecreasing throughout these steps. The state is fixed by time three.

It remains to consider \(K>T\) and \(L<T\), so the hub becomes zero at time two, with \(q\) two-occupied triangles. If \(U>T\), the next hub state is one, and every two-occupied triangle becomes a singleton; the following update restores the previous spatial two-occupied pattern while the hub flips back. Hence the states at times one and two form a primitive two-cycle. This cycle is already present at time zero precisely when \(p=0\). If \(U\leq T\), the hub stays zero, the triangles become singletons at time three and all those singletons disappear by time four; the final hub has at most \(T\) occupied neighbors and stays zero. Thus no other recurrent behavior is possible.

The classification also yields a completely explicit census. For \(t\geq0\) and \(\ell\in\{1,2\}\), the number \(N_{t,\ell}(r)\) of labelled initial states with first periodic-entry time \(t\) and eventual least period \(\ell\) is
\[
 N_{t,\ell}(r)=2\sum_{\substack{z,o,p,q\geq0\\z+o+p+q=r\\\mathcal C(z,o,p,q)=(t,\ell)}}w_r(z,o,p,q),
\]
where \(\mathcal C\) is defined by this exhaustive ordered decision table (the first applicable branch is used):

| Conditions | \(\mathcal C=(t,\ell)\) |
|---|---|
| \(K\leq T,\ q=0,\ p=0\) | \((0,1)\) |
| \(K\leq T,\ q=0,\ p>0\) | \((1,1)\) |
| \(K\leq T,\ q>0\) | \((2,1)\) |
| \(K>T,\ L\geq T,\ q=0\) | \((1,1)\) |
| \(K>T,\ L\geq T,\ q>0\) | \((3,1)\) |
| \(K>T,\ L<T,\ U>T,\ p=0\) | \((0,2)\) |
| \(K>T,\ L<T,\ U>T,\ p>0\) | \((1,2)\) |
| \(K>T,\ L<T,\ U\leq T,\ q=0\) | \((2,1)\) |
| \(K>T,\ L<T,\ U\leq T,\ q>0\) | \((4,1)\) |

All omitted entry/period categories have population zero. The factor of two uses global bit-complement symmetry; there is no overlap because the two hub values are different. This proves the global four-step claim and exact first-entry table.

**3. Recurrent populations and basin counts.** A fixed state has all triangles monochromatic. With hub zero, it has \(o\) all-one triangles and \(r-o\) all-zero triangles, subject to \(3o\leq T\). Counting positions and complementing gives the stated \(f_r\). In a primitive two-cycle, take its unique hub-zero phase. Then necessarily \(p=0\), \(q\geq1\), and \(L<T<U\). Choose \(o\) full-one triangles, \(q\) two-occupied triangles with three orientations each, and set the rest to zeros. This gives \(c_r\). For the entire two-cycle basin, the same strict condition \(L<T<U\) applies, but the remaining \(r-o-q\) triangles can be zero (one choice) or singleton (three choices), yielding the factor \(4^{r-o-q}\). Accounting for both hub values yields \(b_r\).

**4. Sharpness.** For \(r\geq3\), take the hub zero, no full-one or empty triangles, \(q=\lfloor3r/4\rfloor\) doubletons and \(p=r-q\) singletons. Then \(r/2<q\leq3r/4\), so \(K=r+q>T\), \(L=q<T\), and \(U=2q\leq T\). Because \(q>0\), the table gives first-entry time exactly four. For \(r=2\), a hub-zero state with one full-one triangle and one doubleton has first entry time three; a time-four state is impossible because the time-four branch requires simultaneously \(K>T\), \(L<T\), and \(U\leq T\) with \(q>0\), which has no integer solution for two triangles. For \(r=1\), the graph is \(K_4\), whose sixteen labelled states comprise two fixed states, six periodic states in three two-cycles, and eight states of first-entry time one. Therefore the claimed sharp cutoff holds for every \(r\).

**5. Oscillation asymptotics.** Count five symbols per triangle for a hub-zero periodic two-cycle: empty, full, and three oriented doubletons. Under a uniform five-symbol choice, the random contributions to \(L\) are \(0,3,1\) with respective probabilities \(1/5,1/5,3/5\); the contributions to \(U\) are \(0,3,2\) with the same probabilities. Their expectations are \(6/5\) and \(9/5\), respectively, both separated from \(3/2\) by \(3/10\). Hoeffding's inequality for independent variables in \([0,3]\) bounds the probabilities of \(L\geq T\) and \(U\leq T\) by \(e^{-r/50}\) each. The union bound gives \(1-2e^{-r/50}\leq c_r/5^r\leq1\). Since \(f_r\leq2^{r+1}\), the displayed periodic-density asymptotic follows.

## Verification
The standalone program `check_states.cpp` constructs all graph neighborhoods directly and independently iterates every labelled binary state for each \(r\in\{1,\ldots,7\}\), a total of \(4{,}793{,}488\) state trajectories. It detects the least eventual period and first entry time from actual states, without using the count-category table. The program `check_macro.py` independently constructs the four-type triangle transition, tests the decision table for every integer macrostate with \(1\leq r\leq60\), and evaluates all counting formulas by exact integer arithmetic. Its results were compared with the direct enumerator for all seven shared sizes. Execution outputs are included as `states_output.txt`, `macro_output.txt` and `crosscheck_output.txt`.

For \(r=1,2,3,4,5,6,7\), the pairs \((f_r,c_r)\) are respectively \((2,3),(6,9),(8,45),(22,189),(32,1683),(84,6885),(128,45699)\). The corresponding two-cycle basin populations are \(6,18,198,1026,11736,61398,712452\). All numerical verifications are finite; the all-size theorem is established by the local transition proof and exact multinomial counting, not by extrapolating experiments.

## Relationship to prior work
The theorem of Goles and Olivos (1980) already establishes that symmetric finite threshold networks have eventual periods at most two. Kuhlman, Mortveit, Murrugarra and Kumar (2011, arXiv:1108.2974, Sections 3 and 4) extend that observation to bi-threshold systems and study other graph constructions. Neither generic period restriction determines a uniform sharp four-step cutoff, the first-entry census or the windmill orbit and basin formulas. Turau (2022, arXiv:2202.01580, Sections 3–5) gives a combinatorial characterization of synchronous majority fixed states and two-cycles on **trees**; the present windmill has many triangles and the tree characterization does not specialize to it. Earlier exact majority results on a wheel rim and a pineapple clique-plus-leaves concern different graph families; prior three-state excitation results on the same friendship-graph family concern a different state set and update rule. The present contribution is the specific triangular-clique-windmill recurrence and transient classification, not the general period-two theorem.

## Limitations
The classification uses a clique blade of exactly three outer vertices, strict **open-neighbor** majority and tie retention. It does not automatically extend to other blade sizes, asynchronous updates, stochastic updates, or closed-neighborhood majority. The source searches do not establish historical uniqueness: equivalent formulas could appear in older, unindexed graph-dynamics literature. No independent external mathematical audit is claimed.

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
2. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra and V. S. A. Kumar, *Bifurcations in Boolean Networks*, initial public arXiv version dated 2011-08-15, https://arxiv.org/abs/1108.2974.
3. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, initial public arXiv version dated 2022-02-03, https://arxiv.org/abs/2202.01580.
