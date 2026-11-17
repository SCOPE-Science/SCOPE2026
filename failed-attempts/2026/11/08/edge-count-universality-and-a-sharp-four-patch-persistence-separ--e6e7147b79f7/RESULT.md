# Edge-count universality and a sharp four-patch persistence separation

## Finding

Let \(G=(V,E)\) be a finite, simple, undirected graph with \(n=|V|\ge 2\) vertices and \(m=|E|\). In the finite-patch colonization–extinction (contact) process, every occupied vertex becomes vacant at rate \(1\) and every vacant vertex becomes occupied at rate \(\lambda\) times its number of occupied neighbors. Start with **all patches occupied**, let \(\tau_G\) be the first time that all patches are vacant, and write \(T_G(\lambda)=\mathbb E[\tau_G]\).

For \(\lambda\) in a neighborhood of zero,
\[
T_G(\lambda)=H_n+\frac{2m}{n(n-1)}\big((n+1)H_n-2n\big)\lambda+c_2(G)\lambda^2+O(\lambda^3),\qquad H_n=\sum_{j=1}^{n}\frac1j.
\]
Thus the linear response depends only on the number of links, regardless of how those links are arranged. The quadratic response has the motif form
\[
c_2(G)=a_nm+b_n\binom m2+d_nW(G),\qquad W(G)=\sum_{v\in V}\binom{\deg_G(v)}2,
\]
for rational constants \(a_n,b_n,d_n\) depending only on \(n\). This is a structural characterization; no all-\(n\) sign assertion is made for \(d_n\).

The smallest connected graphs with the same vertex and edge counts but different topology are the four-vertex star \(K_{1,3}\) and path \(P_4\). They have equal constant and linear terms, but
\[
T_{K_{1,3}}(\lambda)=\frac{25}{12}+\frac{29}{24}\lambda+\frac{11}{16}\lambda^2+O(\lambda^3),\quad
T_{P_4}(\lambda)=\frac{25}{12}+\frac{29}{24}\lambda+\frac{61}{144}\lambda^2+O(\lambda^3).
\]
Moreover **the star has strictly greater expected time to total vacancy at every positive colonization rate**:
\[
T_{K_{1,3}}(\lambda)-T_{P_4}(\lambda)=\frac{\lambda^2Q(\lambda)}{6(\lambda+1)(3\lambda+2)(4\lambda+3)(4\lambda^2+9\lambda+6)(12\lambda^3+31\lambda^2+32\lambda+12)}>0\quad(\lambda>0),
\]
where
\[
Q(\lambda)=324\lambda^8+2595\lambda^7+8941\lambda^6+17676\lambda^5+22477\lambda^4+19319\lambda^3+11195\lambda^2+4032\lambda+684.
\]
In particular the first arrangement-dependent gap is \((19/72)\lambda^2+O(\lambda^3)\). At zero rate both graphs have \(25/12\) mean extinction time. This four-patch comparison is sharp among connected simple graphs matched by both order and edge count.

## Assumptions and scope

There is no immigration from outside the graph, no spontaneous colonization, and the empty configuration is absorbing. All local extinction clocks have independent exponential rate one and all directed occupied-to-vacant transmission clocks have rate \(\lambda\) per undirected edge. All patches are initially occupied. \(\lambda\ge0\), with strict separation only for \(\lambda>0\). Finite \(n\) is arbitrary for the perturbative motif statements. The exact inequality refers **only** to the two connected four-vertex three-edge trees, with identical unit extinction and per-edge colonization rates; it asserts no extremal ordering for larger trees, other initial conditions, or heterogeneous rates. The model is the mathematical contact process, here interpreted as patch occupancy.

## Proof

For a nonempty occupied set \(S\subseteq V\), let \(u_S(\lambda)\) be the expected additional time to extinction from \(S\); put \(u_\varnothing=0\). The first-event identity is
\[
|S|u_S=1+\sum_{v\in S}u_{S\setminus\{v\}}+\lambda\sum_{\substack{v\notin S\\w\in S,\,\{v,w\}\in E}}(u_{S\cup\{v\}}-u_S).
\tag{1}
\]
The transient linear system has matrix \(M_0+\lambda M_1\), where \(M_0\) is invertible triangular with diagonal entries \(|S|\). For every finite \(\lambda\ge0\), absorption occurs almost surely with finite expectation: from each occupied state the next at most \(n\) deaths can occur without colonization with positive probability, uniformly over finitely many states. Hence its inverse exists and \(u_S\) is rational in \(\lambda\), analytic at zero.

At \(\lambda=0\), the number occupied is a pure-death chain \(n,n-1,\ldots,1,0\), giving \(T_G(0)=H_n\). The derivative of the inverse (or equation (1)) can be written as the expected integrated single-colonization excess during this zero-colonization process. From an occupied \(r\)-set, one colonization changes the zero-rate expected remaining lifetime by \(H_{r+1}-H_r=1/(r+1)\). While at size \(r\), the holding time has mean \(1/r\) and the surviving set is uniformly distributed among all \(r\)-subsets. The mean number of edges crossing it is \(2mr(n-r)/(n(n-1))\). Summing the resulting contributions gives
\[
T_G'(0)=\sum_{r=1}^{n-1}\frac1r\frac{2mr(n-r)}{n(n-1)}\frac1{r+1}=\frac{2m}{n(n-1)}\big((n+1)H_n-2n\big).
\]

For the quadratic term, expand \((M_0+\lambda M_1)^{-1}\) to order two. The coefficient is the full-state component of \(M_0^{-1}M_1M_0^{-1}M_1M_0^{-1}{\bf1}\). Since \(M_1\) is a sum of contributions, one per graph edge, this coefficient is a sum over ordered pairs of graph edges. The zero-rate matrix and full-occupancy state are invariant under every vertex permutation. Consequently each ordered pair contributes a constant depending only on whether the two edges are identical, share one vertex, or are disjoint. Counting those classes yields the stated \(a_nm+b_n\binom m2+d_nW(G)\) form (with coefficients rational because \(M_0\) is integer triangular). No additional graph motif can enter at order two.

On four vertices the two nonisomorphic connected graphs with three edges are precisely \(K_{1,3}\) and \(P_4\). Direct exact elimination of (1) for the 15 nonempty configurations gives
\[
T_{K_{1,3}}(\lambda)=\frac{9\lambda^6+60\lambda^5+193\lambda^4+439\lambda^3+554\lambda^2+331\lambda+75}{6(\lambda+1)(3\lambda+2)(4\lambda+3)},
\]
\[
T_{P_4}(\lambda)=\frac{12\lambda^8+100\lambda^7+427\lambda^6+1280\lambda^5+2628\lambda^4+3527\lambda^3+2961\lambda^2+1424\lambda+300}{2(4\lambda^2+9\lambda+6)(12\lambda^3+31\lambda^2+32\lambda+12)}.
\]
Subtracting and factoring yields the displayed positive quotient: \(Q\) has strictly positive integer coefficients and every denominator factor is positive at \(\lambda>0\). Independent coefficient-by-coefficient recursion in (1), without the symbolic rational matrix inverse, gives the four-vertex Taylor coefficients above; their quadratic difference is \(11/16-61/144=19/72\). With fewer than four vertices, two connected simple graphs of equal vertex and edge counts are necessarily isomorphic, so four vertices is minimal for a same-budget topology distinction.

## Verification

Run `python verification.py` with Python 3.10+ and SymPy 1.12 or later. The program builds the complete 15-state first-event matrix from the named edge sets, verifies both rational expressions and the full polynomial-factor difference symbolically, and uses a separate exact-`Fraction` recurrence to verify the expansion coefficients. It checks representative positive parameter values as secondary diagnostics. The proof of the all-rate inequality is **coefficient positivity of the exact polynomial**, not a finite sample of parameter values. The script also checks that small-\(\lambda\) linear coefficients agree between one common-link pair arranged incidently and disjointly for \(4\le n\le7\); this is auxiliary, not the proof of the general derivative formula.

## Relationship to prior work

The contact-process generator and full-occupancy extinction-time setting are classical. Mountford, Mourrat, Valesin and Yao (2012 preprint) study exponential-order lifetimes on families of growing graphs; their results do not give the finite equal-edge four-vertex star–path inequality or the graph-motif Taylor hierarchy. Van de Bovenkamp and Van Mieghem (2015) derive exact lifetime formulas for stars and complete graphs and compare path, star and other graphs numerically on 64-vertex networks using a fixed metastable infection fraction or spectral-threshold-normalized rates. Neither comparison is the four-vertex, same-per-edge-rate, all-positive-rate inequality given here. Cator and Van Mieghem (2013) analyze metastable modifications on stars and complete graphs, not this full-occupancy pairwise lifetime inequality. General finite-state Markov-chain equations precede this result; no general novelty is claimed for the method or the ecological interpretation.

## Limitations

This is a finite-network, homogeneous-clock mathematical comparison, not an estimate of extinction risk for any field population. The second-order motif classification says which graph statistics *can* enter; it does not give explicit \(a_n,b_n,d_n\) for all \(n\) nor assert their signs universally. The all-rate comparison does not extend to arbitrary larger graphs without further argument. The closest published full texts were examined for implication coverage, but unindexed earlier exact small-graph tables and other historical sources remain priority risks. All statements were reviewed in a self-review; no independent scientific audit has been performed.

## References

1. T. Mountford, J.-C. Mourrat, D. Valesin, and Q. Yao, *Exponential extinction time of the contact process on finite graphs*, arXiv:1203.2972v1 (public 2012-03-13), https://arxiv.org/html/1203.2972v1 .
2. R. van de Bovenkamp and P. Van Mieghem, *Survival time of the susceptible-infected-susceptible infection process on a graph*, Physical Review E **92**, 032806 (2015), https://doi.org/10.1103/PhysRevE.92.032806 .
3. E. Cator and P. Van Mieghem, *Susceptible-infected-susceptible epidemics on the complete graph and the star graph: Exact analysis*, Physical Review E **87**, 012811 (2013), https://doi.org/10.1103/PhysRevE.87.012811 .
