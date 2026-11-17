# Exact three-cycle chip-mass bands on \(K_{3,b}\)

## Finding
For every integer \(b\ge3\), let \(G=K_{3,b}\) carry the usual synchronous parallel chip-firing map \(U\). For a chip configuration \(\sigma\) of least period exactly three from time zero, let \(|\sigma|\) be its total chip count. Its exact generating polynomial is
\[
H_b(z)=\sum_{\substack{\sigma\ge0:\ U^3\sigma=\sigma,\ U\sigma\ne\sigma}}z^{|\sigma|}=(z^{4b}+z^{6b})Q_b(z),
\]
where the polynomial \(Q_b\) is given by either of the equivalent formulas
\[
Q_b(z)=6\sum_{\substack{r,s,t\ge1\\r+s+t=b}}\binom{b}{r,s,t}[r]_z[s]_z[t]_z
=\frac{6\bigl(3^b-3(2+z)^b+3(1+2z)^b-(3z)^b\bigr)}{(1-z)^3},\qquad [j]_z=1+z+\cdots+z^{j-1}.
\]
The right-hand rational expression is a polynomial, including at \(z=1\) by cancellation. Precisely the chip totals
\[
[4b,5b-3]\cap\mathbb Z\quad\text{and}\quad[6b,7b-3]\cap\mathbb Z
\]
support least-period-three configurations, with no others. The two activity classes (one firing or two firings per vertex per three updates) populate the lower and upper band respectively. Each band has \(6b(b-1)(b-2)3^{b-3}\) configurations, giving
\[
\#\{\text{primitive three-cycle configurations}\}=12b(b-1)(b-2)3^{b-3},\qquad
\#\{\text{three-cycle orbits}\}=4b(b-1)(b-2)3^{b-3}.
\]
The extreme chip totals \(5b-3=2|E(G)|-|V(G)|\) and \(6b=2|E(G)|\) each support exactly \(6(3^b-3\cdot2^b+3)\) configurations of least period three. Thus the strict mass inequalities in the known middle-stair period-two theorem cannot be extended to either endpoint for this natural family.

## Assumptions and scope
The bipartition has three distinguishable vertices \(L_1,L_2,L_3\) of degree \(b\) and \(b\) distinguishable vertices \(R_1,\ldots,R_b\) of degree three. Each vertex holding at least its degree fires one chip across each incident edge, simultaneously with all other firing vertices; all chip numbers are nonnegative integers. The count is over **labelled configurations already periodic at time zero**, not all initial configurations of eventual period three, and three configurations per least-period-three orbit are counted. The graph is undirected, loopless and has no sinks. No assertion is made about periods other than three or transient basins.

## Proof
**1. Exactly one or two firings per vertex.** If \(U^3\sigma=\sigma\), let \(k_v\) be the number of firings of \(v\) in the three rounds. Conservation at each vertex says \(\deg(v)k_v=\sum_{w\sim v}k_w\). The Laplacian kernel of a connected graph is the span of the constants, so all \(k_v\) are the same \(k\in\{0,1,2,3\}\). If \(k=0\) or \(k=3\), no firing indicators change between rounds and the chip configuration is fixed, contrary to least period three. Thus \(k=1\) or \(k=2\). If some chip count of a periodic nonfixed configuration were at least twice its vertex degree, that vertex would fire permanently: after any firing it has at least its degree again, even before incoming chips. Connectedness and equality of the firing counts would then force every vertex to fire always, contradiction. Hence for any least-period-three configuration, \(0\le\sigma(v)\le2\deg(v)-1\).

**2. The phase-interval lemma.** Suppose each vertex fires once, on exactly one phase \(j\in\{0,1,2\}\). Write \(A_j\) and \(B_j\) for the numbers firing on phase \(j\) on the three-vertex and \(b\)-vertex sides, so \(\sum_j A_j=3\) and \(\sum_jB_j=b\). For a degree-\(b\) vertex firing on phase \(j\), direct iteration of the threshold inequalities gives precisely \(B_{j-1}\) allowable initial chip values, with indices modulo three. More explicitly, the intervals for phases \(0,1,2\), respectively, are
\[
[b,b+B_2-1],\quad [b-B_0,b-1],\quad[B_2,B_1+B_2-1].
\]
The analogous intervals on the degree-three side each have \(A_{j-1}\) values. These are necessary and sufficient: inserting each interval endpoint into the three updates verifies the required firing/waiting decisions and returns all chips after one firing of each vertex.

**3. Phase rigidity at side size three.** Whenever \(A_j>0\), the interval length \(B_{j-1}\) must be positive; whenever \(B_j>0\), the interval length \(A_{j-1}\) must be positive. Therefore \(A_j>0\Rightarrow B_{j-1}>0\Rightarrow A_{j-2}>0\). Iterating around the three phases forces all \(A_j>0\); as their sum is three, \(A_0=A_1=A_2=1\). Then all \(B_j\ge1\). Conversely, for every ordered positive composition \((B_0,B_1,B_2)=(r,s,t)\) of \(b\), there are \(3!=6\) assignments of the three labelled left vertices to distinct firing phases, and \(\binom{b}{r,s,t}\) phase assignments of the right vertices. Right vertices firing at phases \(0,1,2\) have unique initial chip values \(3,2,1\) respectively. Each of the three left vertices has \(B_{j-1}\) choices, independently. Thus a composition contributes \(6\binom{b}{r,s,t}rst\) states in the lower activity class.

**4. The chip-mass polynomial.** Parameterize the three left initial chips by offsets \(u_0\in[0,t-1]\), \(u_1\in[0,r-1]\), \(u_2\in[0,s-1]\) from the respective interval minima. Summing the left and right chips shows exactly
\[
|\sigma|=4b+u_0+u_1+u_2.
\]
Hence the lower-band generating polynomial is \(z^{4b}Q_b(z)\) with the positive-composition formula above. Expand \([j]_z=(1-z^j)/(1-z)\); the multinomial theorem and inclusion-exclusion over the three factors give the displayed rational form for \(Q_b\). In particular,
\[
Q_b(1)=6\sum_{r+s+t=b}\binom{b}{r,s,t}rst=6b(b-1)(b-2)3^{b-3},
\]
by choosing one labelled element of each of the three phase classes, and distributing all other \(b-3\) vertices arbitrarily. Every summand \([r]_z[s]_z[t]_z\) is palindromic of common degree \(b-3\), so \(Q_b(z)=z^{b-3}Q_b(z^{-1})\). Its coefficients at every exponent \(0,\ldots,b-3\) are strictly positive: the composition \((r,s,t)=(b-2,1,1)\) already supplies each such exponent. This proves the exact lower band and its endpoints; \(Q_b(0)=6(3^b-3\cdot2^b+3)\).

**5. Complementary upper band.** For any nonfixed periodic configuration, define the chip complement \(\sigma^c(v)=2\deg(v)-1-\sigma(v)\). The bound in step 1 makes it nonnegative. Since the fire bit of every vertex is inverted, direct substitution into the update shows \(U(\sigma^c)=(U\sigma)^c\). It is a bijection between one-firing and two-firing period-three states. The complement's total chip mass is
\[
\sum_v(2\deg(v)-1)-|\sigma|=(11b-3)-|\sigma|.
\]
Thus the upper-band polynomial is \(z^{7b-3}Q_b(z^{-1})=z^{6b}Q_b(z)\). The two bands are disjoint for \(b\ge3\). Their total configuration counts and orbit counts follow. The upper endpoint assertion is immediate from the common boundary coefficient \(Q_b(0)\). This exhausts all nonfixed period-three states by step 1.

## Verification
The standalone `verify_bruteforce.py` enumerates all \((2b)^3 6^b\) chip configurations in the confinement box for \(b=3,4\), applies the actual synchronous map three times, and checks the exact mass histogram of least-period-three states against the independently computed positive-composition polynomial. It tests 46,656 and 663,552 configurations, respectively. The separate `verify_polynomial.py` compares the signed polynomial identity, positivity and palindromicity, mass support, boundary coefficient, and total formula for every integer \(3\le b\le30\). Both programs use only the Python standard library; commands are `python3 verify_bruteforce.py` and `python3 verify_polynomial.py`. Their captured outputs are provided. These finite checks supplement the all-parameter proof, and do not substitute for it.

## Relationship to prior work
Jiang's *On the Period Lengths of the Parallel Chip-Firing Game* (arXiv:1003.0943, originally public March 4, 2010), Proposition 3.9 and Theorem 3.10, established which periods occur on general complete bipartite graphs, including an explicit example of period three, but not a chip-mass-resolved census of every such configuration. Jiang, Scully and Zhang's *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game* (arXiv:1211.6786), Theorem 6.2, characterizes possible firing patterns; it does not supply the present labelled configuration polynomial. Ji, Li and Wang's *Non-Stabilizing Parallel Chip-Firing Games* (arXiv:2408.10508), Theorem 1, excludes primitive periods three and four in the strict middle mass range. Jung's *The Middle Stair for Complete Bipartite Parallel Chip-Firing* (arXiv:2608.01350), Theorem 1, proves period two throughout that strict interval. The two endpoint populations here establish sharp nonextension in \(K_{3,b}\), without contradicting any of those theorems. Earlier exact period-four enumeration for \(K_{2,b}\) concerns a different primitive period and graph side size, not these period-three populations.

## Limitations
This is a census solely of configurations *already* of least period three; it does not enumerate their incoming transient basins, classify longer periods, or establish a general formula for \(K_{a,b}\) with \(a\ge4\). The count uses labelled vertices and distinguishes the three cyclic phases. Exhaustive direct enumeration was performed for \(b=3,4\), not for all \(b\). A full independent mathematical audit has not yet been performed. The literature search did not locate an equivalent pre-existing census, but completeness of historical indexing cannot be guaranteed.

## References
1. T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (first public version March 4, 2010), https://arxiv.org/abs/1003.0943.
2. T.-Y. Jiang, Z. Scully, Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786 (2012), https://arxiv.org/abs/1211.6786.
3. D. Ji, M. Li, D. Wang, *Non-Stabilizing Parallel Chip-Firing Games*, arXiv:2408.10508 (2024), https://arxiv.org/abs/2408.10508.
4. M. Jung, *The Middle Stair for Complete Bipartite Parallel Chip-Firing*, arXiv:2608.01350 (2026), https://arxiv.org/abs/2608.01350.
