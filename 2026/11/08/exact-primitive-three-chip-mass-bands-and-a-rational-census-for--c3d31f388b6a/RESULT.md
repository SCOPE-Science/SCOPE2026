# Exact primitive-three chip-mass bands and a rational census for fan graphs

## Finding
Let \(F_n=K_1\vee P_n\), with \(n\ge 2\), have a hub and an ordered path of \(n\) vertices. Under synchronous parallel chip-firing, a vertex with at least its degree in nonnegative integer chips sends one chip to every neighbor. Define \(H_n(z)=\sum_{U^3\sigma=\sigma,\ U\sigma\ne\sigma}z^{|\sigma|}\), where \(|\sigma|\) is the total chip count. Then
\[
\operatorname{supp}H_n=[2n-1,3n-3]_{\mathbb Z}\ \cup\ [4n-2,5n-4]_{\mathbb Z}.
\]
Every coefficient in both stated intervals is strictly positive; all other coefficients vanish. Furthermore,
\[
\boxed{\sum_{n\ge2}H_n(1)s^{n-2}=\frac{12(1-s)}{(1-3s+s^2)^2(1+s+s^2)}.}
\]
In particular the total counts for \(n=2,3,4,5,6,7\) are \(12,48,168,564,1788,5496\), and the number of distinct primitive-three state-orbits is \(H_n(1)/3\). More precisely, with \(\alpha=(3+\sqrt5)/2\),
\[
H_n(1)\sim\left(\frac{33}{10}+\frac{3\sqrt5}{2}\right)(n-1)\alpha^{n-2}.
\]
The complete mass polynomial is specified by a nine-state weighted matrix product below.

## Assumptions and scope
All graphs are finite, simple, undirected and labelled. The path vertices are \(v_1,\ldots,v_n\) in order, and the hub is \(h\). The hub has degree \(n\), the two path endpoints have degree \(2\), and all other path vertices have degree \(3\). Configurations lie in \(\mathbb Z_{\ge0}^{n+1}\). Every update is simultaneous, the threshold is the graph degree, and no chips are added or lost. The least period is defined for configurations already recurrent; transient configurations are not counted. The notation \([a,b]_{\mathbb Z}\) denotes all integers between the endpoints inclusive. The first case \(n=2\) is the triangle; no empty path is included.

## Proof
**1. Firing counts.** Suppose \(U^3\sigma=\sigma\). Let \(m_v\) be the number of times vertex \(v\) fires in those three rounds. The chip-change identity yields \(L m=0\), where \(L\) is the graph Laplacian. Connectedness gives a constant integer firing count \(m_v=m\). If \(m=0\), every vertex waits throughout; if \(m=3\), every vertex fires throughout. Both cases are fixed points. Any nonfixed solution has \(m=1\) or \(m=2\), and therefore has primitive period three.

**2. The one-fire interval.** For \(m=1\), assign each vertex its unique firing phase \(a_v\in\{0,1,2\}\). Let \(d_v\) denote its degree and \(b_j(v)\) the number of its neighbors of phase \(j\) (indices modulo three). The three threshold tests at times zero, one and two are jointly equivalent to exactly one of these intervals for its initial chip count:
\[
\begin{array}{ll}
 a_v=0:&d_v\le\sigma(v)\le d_v+b_2(v)-1,\\
 a_v=1:&d_v-b_0(v)\le\sigma(v)\le d_v-1,\\
 a_v=2:&b_2(v)\le\sigma(v)\le b_2(v)+b_1(v)-1.
\end{array}
\]
An interval is empty if and only if the vertex has no neighbor of the immediately preceding phase. Conversely, choosing independently any integer in the indicated interval at every vertex makes every indicated threshold test true, and the resulting three-round update returns the configuration. Thus these intervals characterize *all* one-fire primitive-three states without overcounting.

**3. Sharp lower-band support.** For a fixed feasible phase assignment, each interval in step 2 is consecutive. Summing its lower endpoints over all vertices gives
\[
 |E(F_n)|+e_{=},
\]
where \(e_{=}\) counts edges with equal-colored endpoints. Indeed, every unequal-color edge contributes one chip and every equal-color edge contributes two chips to the total lower endpoint sum. The interval length at \(v\) is \(b_{a_v-1}(v)\). Summing the interval *upper* endpoints gives
\[
 |E(F_n)|+e_{=}+\sum_v\big(b_{a_v-1}(v)-1\big)=2|E(F_n)|-|V(F_n)|,
\]
because every unequal-color edge contributes exactly one to the summed predecessor-neighbor count and an equal-color edge contributes zero. For the fan, \(|E|=2n-1\) and \(|V|=n+1\), so all one-fire masses are in \([2n-1,3n-3]_{\mathbb Z}\).

For the reverse inclusion, set the hub phase to zero and alternate path phases \(1,2,1,2,\ldots\). Every vertex has a predecessor-phase neighbor, including the hub, and every edge is heterochromatic. Hence the sum of interval minima is exactly \(2n-1\); the sum of maxima is exactly \(3n-3\). Since the choices at distinct vertices are independent consecutive integer intervals, every intermediate chip total is realized. The low-mass support is therefore exactly the stated first band.

**4. The high band and exhaustiveness.** Any one-fire state obeys \(0\le\sigma(v)\le2d_v-1\) for every vertex. Define the chip complement \(C\sigma(v)=2d_v-1-\sigma(v)\). Direct substitution in the update equation shows \(UC\sigma=CU\sigma\), and the firing indicator is replaced by its complement. Consequently \(C\) is a bijection between one-fire and two-fire primitive-three states. It reverses chip mass about \(\sum_v(2d_v-1)=4|E|-|V|=7n-5\), producing precisely the second band \([4n-2,5n-4]_{\mathbb Z}\) with positive coefficients. Step 1 excludes all other primitive-three possibilities.

**5. Exact weighted transfer and total count.** Write \(S_j(z)=1+z+\cdots+z^{j-1}\) for \(j\ge1\) and \(S_0(z)=0\). Given a vertex of degree \(d\), phase \(a\), and neighbor-phase counts \((b_0,b_1,b_2)\), define the polynomial
\[
 W(a;d,b_0,b_1,b_2;z)=\begin{cases}
 z^d S_{b_2}(z),&a=0,\\
 z^{d-b_0}S_{b_0}(z),&a=1,\\
 z^{b_2}S_{b_1}(z),&a=2.
 \end{cases}
\]
Thus \(W\) is the exact chip-mass polynomial for the allowed interval. Index a nine-dimensional matrix by ordered phase pairs \((a,b)\in\{0,1,2\}^2\). Define a row \(\ell\), transition matrix \(M\), and column \(r\) using the formulas
\[
\begin{aligned}
 \ell_{(a,b)}(t,z)&=t^{\mathbf1_{a=2}}W(a;2,\mathbf1_{0=0}+\mathbf1_{b=0},\mathbf1_{b=1},\mathbf1_{b=2};z),\\
 M_{(a,b),(b,c)}(t,z)&=t^{\mathbf1_{b=2}}W(b;3,1+\mathbf1_{a=0}+\mathbf1_{c=0},\mathbf1_{a=1}+\mathbf1_{c=1},\mathbf1_{a=2}+\mathbf1_{c=2};z),\\
 r_{(a,b)}(t,z)&=t^{\mathbf1_{b=2}}W(b;2,1+\mathbf1_{a=0},\mathbf1_{a=1},\mathbf1_{a=2};z).
\end{aligned}
\]
All other entries of \(M\) are zero. Define \(Q_n(t,z)=\ell(t,z)M(t,z)^{n-2}r(t,z)\). Its coefficient of \(t^k\) is the path-chip polynomial restricted to phase words containing exactly \(k\) path vertices of phase two while the hub has phase zero. In that case the hub fires at time zero and has chip interval \([n,n+k-1]_{\mathbb Z}\). Cyclic time-shift gives three equally populated hub phases. Therefore the exact *one-fire* mass polynomial is
\[
 L_n(z)=\frac{3z^n}{1-z}\Big(Q_n(1,z)-Q_n(z,z)\Big),
\]
interpreted as a polynomial at \(z=1\) by cancellation. The complete answer is
\[
 H_n(z)=L_n(z)+z^{7n-5}L_n(z^{-1}).
\]
This determines every coefficient with a matrix of fixed size, independently of \(n\).

For the unweighted count, let \(\ell(t)=\ell(t,1)\), \(M(t)=M(t,1)\), and \(r(t)=r(t,1)\). Matrix multiplication and rational simplification give the exact finite-dimensional identity
\[
 \left.\frac{\partial}{\partial t}\left(\ell(t)(I-sM(t))^{-1}r(t)\right)\right|_{t=1}
 =\frac{2(1-s)}{(1-3s+s^2)^2(1+s+s^2)}.
\]
The identity follows by multiplying by \(\det(I-sM(t))\) and equating polynomial coefficients; the standalone symbolic checker constructs these nine-state matrices independently and checks the identity exactly. The derivative counts the hub's \(k\) possible chip values; three hub phases and the one-fire/two-fire complement contribute an overall factor six. Summing the identity over \(n\ge2\) yields the claimed rational generating function. Its dominant singularity is the double root \(s=(3-\sqrt5)/2\) of \(1-3s+s^2\), proving the stated linear-times-exponential growth.

## Verification
The accompanying `check_symbolic.py` constructs the transfer matrix over exact polynomial rational functions and checks the rational identity by symbolic cancellation; it independently builds each one-fire mass coefficient from all phase words for \(2\le n\le8\). The accompanying `check_states.py` enumerates all states in the necessary periodic range \(0\le\sigma(v)<2d_v\), and directly tests \(U^3\sigma=\sigma\ne U\sigma\) for \(2\le n\le6\). These finite experiments are checks, not an infinite proof. Both scripts use only Python 3; the symbolic checker additionally requires SymPy. Their exact commands and captured output are in `VERIFICATION.md` and the included `.txt` transcripts.

## Relationship to prior work
The ordinary parallel chip-firing rule originates in Bitar and Goles (1992). Jiang, Scully and Zhang (arXiv:1211.6786, Sections 2, 5–7) establish general structural restrictions on firing patterns, not the fan-specific period-three generating function or coefficient census. Levine (arXiv:0811.2800, Sections 1 and 4) establishes short-period behavior on complete graphs; the fan is not a complete graph for \(n\ge3\). Ji, Li and Wang (arXiv:2408.10508, Theorem 1) exclude primitive period three from the *open* middle chip-density interval on all connected graphs, but do not determine equality or the full fan mass populations. The boundary \(2|E|-|V|\) is attained here. Prior results on wheel graphs concern \(K_1\vee C_n\); removal of a rim edge changes path-endpoint thresholds and does not imply the present rational generating function. A pre-existing fan-graph polynomial for dissociation sets counts a different static invariant and does not imply dynamical states.

## Limitations
Only *initially* primitive-three states are classified. No claim is made about trajectories whose eventual period is three after a transient, about higher periods, or about the entire recurrent-state census. The rational formula is for the total primitive-three count; the full mass distribution is represented by the fixed-size transfer matrix rather than a single displayed scalar rational expression. Historical-priority verification is not exhaustive: the full Bitar–Goles 1992 paper could not be obtained through available lawful routes, so an unindexed equivalent claim remains possible. The public mathematical claims are self-reviewed only; no independent audit is asserted.

## References
1. J. Bitar and E. Goles, *Parallel chip firing games on graphs*, Theoretical Computer Science 92 (1992), 291–300, DOI: `10.1016/0304-3975(92)90316-8`.
2. T.-Y. Jiang, Z. Scully, and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:`1211.6786` (first public version 2012-11-29).
3. L. Levine, *Parallel Chip-Firing on the Complete Graph: Devil's Staircase and Poincare Rotation Number*, arXiv:`0811.2800` (first public version 2008-11-17).
4. D. Ji, M. Li, and D. Wang, *Non-Stabilizing Parallel Chip-Firing Games*, arXiv:`2408.10508` (first public version 2024-08-20).
