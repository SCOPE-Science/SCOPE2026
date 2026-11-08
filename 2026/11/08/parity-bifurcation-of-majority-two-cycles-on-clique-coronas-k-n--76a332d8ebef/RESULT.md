# Parity bifurcation of majority two-cycles on clique coronas \(K_n\odot K_1\)

## Finding
For each integer \(n\ge2\), let \(G_n=K_n\odot K_1\) be a labelled clique with one private pendant leaf attached to every clique vertex. Under synchronous strict open-neighbor binary majority with retention on ties, let \(P_j(n)\) denote the number of configurations whose **least temporal period equals** \(j\), starting at time zero. Then
\[
P_1(n)=\begin{cases}2+\binom{n}{n/2},&n\text{ even},\\2,&n\text{ odd},\end{cases}
\qquad
P_2(n)=\begin{cases}
\binom{n}{n/2}\left(\binom{n}{n/2}-1\right),&n\text{ even},\\
2n\binom{n-1}{(n-1)/2}+2\binom{n}{(n-1)/2},&n\text{ odd}.
\end{cases}
\]
There are precisely \(P_2(n)/2\) distinct period-two temporal orbits and no periodic configurations of higher least period. In the uniform distribution on all \(2^{2n}\) initial configurations, the **immediate primitive-two probability** has two different asymptotic regimes:
\[
\frac{P_2(n)}{2^{2n}}\sim\begin{cases}
\frac{2}{\pi n},&n\to\infty\text{ through even integers},\\
\sqrt{\frac{2n}{\pi}}\,2^{-n},&n\to\infty\text{ through odd integers}.
\end{cases}
\]
Thus the same core-plus-one-leaf construction has a polynomially small immediate oscillation population in even clique orders, but an exponentially small one in odd clique orders.

## Assumptions and scope
The graph has hub vertices \(v_1,\ldots,v_n\), mutually adjacent, and leaves \(w_i\), each adjacent only to \(v_i\). States are bits, each of the \(2n\) labelled vertices being independently assignable at initialization. At every time step every vertex examines its **open** neighborhood and takes the strict majority bit; if the two bit counts tie, it retains its previous bit. Updates are synchronous. The enumerations concern the initial state itself satisfying \(F^j(x)=x\), not its eventual attractor or the size of an attractor basin. No quotient by graph isomorphism, vertex relabelling, or bit complement is taken.

Write \((a,b)\) for a state in which the \(n\) hub bits form \(a\) and the \(n\) leaf bits form \(b\). For a vector \(a\), let \(k=|a|\) be its number of one-bits. Define the majority-with-tie-retention function
\[
\mathcal M_n(s,\alpha)=\begin{cases}1,&2s>n,\\0,&2s<n,\\\alpha,&2s=n.\end{cases}
\]
Then, exactly,
\[
F(a,b)=(c,a),\qquad c_i=\mathcal M_n(k-a_i+b_i,a_i).
\]
The hub has \(n\) neighbors, and the leaf copies the old hub bit in one update; no boundary exception is omitted.

## Proof
**Fixed configurations.** If \(F(a,b)=(a,b)\), then \(b=a\). Every hub then sees exactly \(k=|a|\) one-bits, independently of its position. For odd \(n\), all hubs must therefore be equal, giving the two unanimous fixed configurations. For even \(n\), the same two unanimous configurations coexist with all \(\binom n{n/2}\) balanced hub configurations, each with matching leaf states. These cases are disjoint and give \(P_1\).

**Reduction for period two.** Suppose \(F^2(a,b)=(a,b)\). As the leaf bits always copy the old hub bits, the intervening state is exactly \((b,a)\), so the conditions are
\[
\mathcal M_n(k-a_i+b_i,a_i)=b_i,\qquad
\mathcal M_n(\ell-b_i+a_i,b_i)=a_i
\]
for all \(i\), where \(k=|a|\), \(\ell=|b|\). Conversely these conditions imply \(F^2(a,b)=(a,b)\); no other leaf choices are possible.

**Even order.** Write \(n=2r\), \(r\ge1\). The exact hub update above simplifies to
\[
c=\begin{cases}0^n,&k<r,\\b,&k=r,\\1^n,&k>r.\end{cases}
\]
For a nonfixed period-two state, neither hub word can be constant: a constant hub word at either phase sends the next hub word to the same constant, making the two-period relation fixed. The displayed update forces \(k=\ell=r\). Conversely every ordered pair \((a,b)\) of balanced words satisfies \(F(a,b)=(b,a)\) and \(F(b,a)=(a,b)\). There are \(\binom n r^2\) ordered pairs and \(\binom n r\) diagonal fixed pairs, yielding the claimed even-order \(P_2\).

**Odd order.** Write \(n=2r+1\), \(r\ge1\). The four possible ordered types \((a_i,b_i)\) impose the following simultaneous inequalities when they occur:

| Type | Necessary and sufficient inequalities |
| --- | --- |
| \((0,0)\) | \(k\le r\) and \(\ell\le r\) |
| \((1,1)\) | \(k\ge r+1\) and \(\ell\ge r+1\) |
| \((0,1)\) | \(k\ge r\) and \(\ell\le r+1\) |
| \((1,0)\) | \(k\le r+1\) and \(\ell\ge r\) |

If a state is nonfixed, both flipping types must occur. Indeed, if only \((0,1)\) occurs, then \(\ell>k\); its inequalities force \((k,\ell)=(r,r+1)\). The stationary types are then both forbidden, forcing every position to be \((0,1)\), which would give \(k=0\ne r\). The case with only \((1,0)\) is symmetric. With both flipping types present one must have \(k,\ell\in\{r,r+1\}\), and the stationary types \((0,0)\) and \((1,1)\) cannot coexist.

If \((0,0)\) occurs then \(k=\ell=r\), with one fixed zero and \(r\) positions of each flipping type. This gives \(n\binom{n-1}{r}\) labelled configurations. If \((1,1)\) occurs, the bit-complementary argument gives another \(n\binom{n-1}{r}\). In the remaining case all positions flip, so \(b=\mathbf1-a\) and \((k,\ell)\) is \((r,r+1)\) or \((r+1,r)\). These yield \(2\binom nr\) configurations. The three families are disjoint, exhaustive and nonfixed, proving the odd-order formula.

**Absence of longer recurrent periods.** This also follows from the classical symmetric-threshold theorem, but it has a short direct argument here. Convert bits to spins \(s_i(t)\in\{-1,1\}\), and let \(W\) be the symmetric adjacency matrix with diagonal \(\varepsilon I\), for any fixed real \(0<\varepsilon<1\). The tie-retaining update is exactly \(s_i(t+1)=\operatorname{sgn}((Ws(t))_i)\), with no zero field possible. Set \(E_t=-s(t)^\mathsf{T}Ws(t-1)\) for \(t\ge1\). Symmetry gives
\[
E_{t+1}-E_t=-\sum_i\bigl(s_i(t+1)-s_i(t-1)\bigr)(Ws(t))_i\le0,
\]
strictly whenever any coordinate at \(t+1\) differs from that at \(t-1\). Because the state space, hence the possible energy values, is finite, eventually \(s(t+1)=s(t-1)\). Therefore every trajectory eventually has least period one or two; the immediate population above is the entire recurrent population.

**Asymptotics.** For even \(n\), \(\binom{n}{n/2}\sim2^n\sqrt{2/(\pi n)}\), so dividing its square-minus-itself by \(2^{2n}\) gives \(2/(\pi n)\). For odd \(n\), \(\binom{n-1}{(n-1)/2}\sim2^{n-1}\sqrt{2/(\pi(n-1))}\), while the second term in \(P_2\) is smaller by a factor of order \(1/n\). Thus \(P_2(n)\sim 2^n\sqrt{2n/\pi}\), yielding the odd asymptotic.

## Verification
Two independently formulated executable checks accompany this document. Run `python3 verify_exhaustive.py` and `python3 verify_types.py` from the directory containing the files. The first constructs the full labelled graph and applies the majority rule vertex-by-vertex, enumerating all \(21{,}840\) initial states for \(2\le n\le7\). It verifies \(P_1\), \(P_2\) and the observed finite transient times. The second counts two-periodic pairs by independent four-type multinomial enumeration rather than vertex-by-vertex dynamics, and checks the formulas for every integer \(2\le n\le60\). Full exact terminal outputs appear in `exhaustive_output.txt` and `types_output.txt`. These are finite corroborations only; the arguments above establish the theorem for every \(n\ge2\).

For illustration, \((P_1,P_2)\) for successive orders \(n=2,3,4,5,6,7,8,9\) are respectively \((4,2)\), \((2,18)\), \((8,30)\), \((2,80)\), \((22,380)\), \((2,350)\), \((72,4830)\), \((2,1512)\).

## Relationship to prior work
Goles–Olivos (1980) established eventual period at most two for symmetric threshold systems. Kaaser–Mallmann-Trenn–Natale (arXiv:1508.03519v1, 14 August 2015) give the matching tie-retaining majority rule and analyze voting times and graph modules, but their theorems concern stabilization-time bounds rather than exact recurrent-state counts on the one-leaf-per-hub clique corona. Benjamini–Chan–O'Donnell–Tamuz–Tan (arXiv:1405.2486v1) study convergence and opinion disagreement on infinite unimodular and random graphs; their results do not imply the present labelled finite-graph counts. A graph-theoretic study of complete-graph coronas concerning general-position sets addresses another invariant and does not imply majority dynamics.

The new binomial formulas enumerate *initial* periodic points. Other exact majority-census formulas for pineapple graphs, split graphs, and complete multipartite graphs concern different neighborhoods: in particular, a pineapple graph has all leaves at a single hub rather than one separately matched to each hub. These formulas do not imply this result by deleting or duplicating vertices because changing those neighborhoods changes their majority updates.

## Limitations
The theorem uses unweighted, synchronous, binary, strict open-neighbor majority with **tie retention**; tie-flipping, asynchronous, weighted, and multistate variants are not covered. It does not give all transient-basin sizes or the exact stabilization-time distribution for arbitrary \(n\). The case \(n=1\) is excluded. The literature comparison does not establish priority against every unindexed paper or all equivalent formulations; no independent audit of the present proof has been performed.

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI: https://doi.org/10.1016/0012-365X(80)90121-1.
2. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1, publicly posted 2015-08-14. https://arxiv.org/html/1508.03519v1.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, publicly posted 2014-05-11. https://arxiv.org/html/1405.2486v1.
