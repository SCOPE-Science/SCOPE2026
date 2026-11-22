# Two field thresholds and exact critical occupation polynomials in a tripartite Potts antiferromagnet

## Finding
Let \(a>b>c\ge1\) be integers and let \(G=K_{a,b,c}\) have vertex shores \(A,B,C\) of these sizes. Define \(n_0(\sigma)\) to be the number of vertices with preferred spin color \(0\). The exact dimensionless ground energy is
\[
e(h)=\min\{-ah,\;ab-(a+b)h,\;ab+ac+bc-(a+b+c)h\}.
\]
Exactly two strictly positive field values are crossings: \(h=a\) and \(h=a+b\). The complete preferred-color occupancy polynomial \(P_h(x)=\sum_{\sigma\text{ ground}}x^{n_0(\sigma)}\), with each labeled configuration counted once, is
\[
P_h(x)=\begin{cases}
2(x^a+x^b+x^c),&h=0,\\
2x^a,&0<h<a,\\
P_a(x),&h=a,\\
2^c x^{a+b},&a<h<a+b,\\
x^{a+b}(2+x)^c,&h=a+b,\\
x^{a+b+c},&h>a+b,
\end{cases}
\]
where
\[
P_a(x)=x^a\left[2+2\sum_{k=1}^{b-1}\binom bk x^k+2\sum_{k=1}^{c-1}\binom ck x^k+2^c x^b+2^b x^c\right].
\]
Consequently the two positive-field crossing degeneracies are \(3(2^b+2^c)-6\) and \(3^c\). The strict intermediate-field region has \(2^c\) ground configurations, although the other strict regions have at most two.

## Assumptions and scope
Every vertex has spin in \(\{0,1,2\}\), every edge pays \(J>0\) when its two endpoint colors agree, and every color-\(0\) vertex gains magnetic energy \(H\ge0\). There are no within-shore edges. The Hamiltonian and normalization are
\[
\mathcal H(\sigma)=J\sum_{uv\in E(G)}\mathbf1_{\{\sigma_u=\sigma_v\}}-Hn_0(\sigma),\quad h=H/J,\quad e(h)=\min_\sigma\mathcal H(\sigma)/J.
\]
All formulas use integer shore sizes satisfying the strict inequalities. Labeling means that exchanging two physical sites inside the same shore produces different configurations if their assigned colors differ. The result includes every nonnegative real \(h\), including all boundary equalities. There is no claim for negative fields, unequal bonds, or unequal part sizes.

## Proof
Write \(s=n_0(\sigma)\), and denote the numbers of preferred spins in the shores by \((u,v,w)\), with \(0\le u\le a\), \(0\le v\le b\), \(0\le w\le c\) and \(u+v+w=s\). The number of monochromatic color-\(0\) edges is \(uv+uw+vw=(s^2-u^2-v^2-w^2)/2\); all monochromatic edges of colors \(1\) and \(2\) add a nonnegative amount.

The exact minimum number \(f(s)\) of edges induced by any \(s\)-vertex subset of \(K_{a,b,c}\) is
\[
f(s)=\begin{cases}
0,&0\le s\le a,\\
a(s-a),&a\le s\le a+b,\\
ab+(a+b)(s-a-b),&a+b\le s\le a+b+c.
\end{cases}
\]
To prove this, maximize \(u^2+v^2+w^2\) under the shore capacities. If \(s\le a\), the vector \((s,0,0)\) majorizes every feasible occupancy vector after sorting. If \(a\le s\le a+b\), \((a,s-a,0)\) does so: its largest coordinate is the universal upper bound \(a\), and its first two coordinates already sum to \(s\). If \(a+b\le s\le a+b+c\), \((a,b,s-a-b)\) majorizes all feasible vectors because their largest coordinate is at most \(a\), and their largest two have sum at most \(a+b\). Strict convexity of the sum of squares proves the formula and gives all equality cases, up to exchanging the two smaller occupied shores when only two shores are used.

For every spin configuration, \(\mathcal H/J\ge f(s)-hs\). Conversely, for each of the three special values \(s=a,a+b,a+b+c\), fill the first one, first two, or all three shores with color \(0\), and color any remaining shore using nonpreferred colors so that no extra monochromatic edge is introduced. Thus the lower bound is attained at all three vertices of the piecewise-linear graph of \(f\). Minimizing \(f(s)-hs\) proves the displayed energy envelope. Its slopes select exactly \(s=a\) for \(0<h<a\), exactly \(s=a+b\) for \(a<h<a+b\), and exactly \(s=a+b+c\) for \(h>a+b\). Only at the two stated positive fields is an entire segment of \(f\) minimizing.

We now count equality configurations. At \(h=0\), zero monochromatic edges require assigning the three different colors one per shore, yielding six states and polynomial \(2(x^a+x^b+x^c)\). At \(0<h<a\), the preferred set is all of \(A\); the remaining shores must be monochromatic in different nonpreferred colors, giving \(2x^a\).

At \(h=a\), equality in the induced-edge bound requires all of \(A\) to be preferred, plus a subset of either \(B\) or \(C\), never positive subsets of both. If a subset of size \(1\le k<b\) is selected from \(B\), the remaining sites of \(B\) and all of \(C\) must use opposite nonpreferred colors; this contributes \(2\binom bk x^{a+k}\). The analogous \(1\le k<c\) subsets of \(C\) contribute \(2\binom ck x^{a+k}\). With no extra preferred vertices there are precisely two states. If all of \(B\) is preferred, each of the \(c\) vertices of \(C\) may independently use either nonpreferred color, giving \(2^c x^{a+b}\). If all of \(C\) is preferred, the \(b\) vertices of \(B\) each choose independently between the two nonpreferred colors, giving \(2^b x^{a+c}\). These disjoint cases prove \(P_a(x)\) and, by setting \(x=1\), its stated degeneracy.

At \(a<h<a+b\), the preferred set is exactly \(A\cup B\); all \(c\) vertices of the remaining shore choose independently between colors \(1\) and \(2\), giving \(2^cx^{a+b}\). At \(h=a+b\), each vertex of \(C\) is independently free to choose any of the three colors, because its cost for color \(0\) exactly cancels its magnetic reward; hence \(P_{a+b}(x)=x^{a+b}(2+x)^c\). Above \(a+b\), the fully preferred configuration is the unique ground state. There are no other equality cases, by strict majorization unless the sorted favored occupancy equals the listed extremizer and by the forced proper coloring of its nonpreferred complement.

For any increasing sequence of strictly ordered shores with \((a,b,c)/(a+b+c)\to(\alpha,\beta,\gamma)\) and \(\gamma>0\), the first crossing count is bounded between \(3\cdot2^b-6\) and \(6\cdot2^b\), while the second is exactly \(3^c\). These bounds require no strict separation of limiting proportions. Taking the logarithm divided by total vertex number proves the two critical residual entropy densities \(\beta\log2\) and \(\gamma\log3\). Between the crossings the exact count \(2^c\) gives \(\gamma\log2\). The larger of the two critical entropy densities changes at \(\beta/\gamma=\log3/\log2\).

## Verification
The accompanying standalone Python file `verify_tripartite_potts.py` enumerates the integer triples of per-shore color counts, weights them by exact multinomial coefficients, and computes their edge penalties and preferred-spin counts independently of the proof. It checks the stated energy and complete occupancy polynomial at eight nonnegative rational magnetic fields for each of six strict shore-size triples: \((3,2,1)\), \((4,3,2)\), \((5,4,2)\), \((6,4,3)\), \((7,5,2)\), and \((8,6,4)\). It reports `EXACT_TRIPARTITE_CENSUS_PASSED 48`. This finite test checks 48 sample cases, not infinitely many triples or fields. The all-size guarantee is supplied by the preceding proof.

## Relationship to prior work
Chang and Shrock's general magnetic-field Potts partition-function treatment [1] includes an all-graph spanning-subgraph identity, and their weighted-graph-coloring study [2] treats infinite-antiferromagnetic-coupling proper colorings, together with explicit formulas for several other graph families. Shrock and Xu [3] give a weighted-set extension and note multipartite generalizations of coloring bounds. These cover the model framework but do not explicitly provide the fixed finite-coupling, all-size \(K_{a,b,c}\) two-crossing ground-energy envelope or the critical labeled occupation polynomials above. Extracting these requires the particular induced-edge majorization and complete equality-case count. The general partition-function identity can of course be specialized, and that is a residual priority risk, not evidence of an independently certified novelty claim.

Related exact Potts field calculations on wheels, cubic line graphs, and isolated finite cubic graphs have different adjacency families and phase-count formulas; they are not equivalent through the above shore reduction. The present claim does not include a general result for arbitrary multipartite graphs, nonuniform fields, or positive temperature.

## Limitations
The field crossings \(H=Ja\) and \(H=J(a+b)\) scale with the degrees in this dense family. Residual entropy statements refer to graph-size sequences evaluated at size-dependent crossing fields, not a conventional fixed-intensive-field phase transition. The result is restricted to three spin colors, equal edge penalties, one preferred color, and strictly ordered positive shore sizes. The proof is self-contained; the archival originality assessment is limited to sources examined and does not exclude earlier unindexed or differently formulated specializations. No independent audit has been performed.

## References
[1] S.-C. Chang and R. Shrock, *Some Exact Results on the Potts Model Partition Function in a Magnetic Field*, arXiv:0907.0777, first public version 2009-07-04. https://arxiv.org/abs/0907.0777

[2] S.-C. Chang and R. Shrock, *Weighted Graph Colorings*, arXiv:0908.2375, first public version 2009-08-17. https://arxiv.org/abs/0908.2375

[3] R. Shrock and Y. Xu, *Weighted-Set Graph Colorings*, arXiv:0911.4218, first public version 2009-11-22. https://arxiv.org/abs/0911.4218
