# Minimum Euclidean width of stable-set polytopes detects maximum cliques

## Finding

Let \(G=(V,E)\) be a nonempty finite simple graph with \(\chi(G)=\omega(G)=q\), and let \(K=\operatorname{STAB}(G)\) in its standard Euclidean coordinates. For a unit vector \(u\), write \(w=W_K(u)\) and \(\delta=qw^2-1\). The minimum width is \(1/\sqrt q\), and all its unit minimizers are the signed normalized indicators \(\sigma\mathbf 1_C/\sqrt q\) of maximum cliques \(C\). The quantitative result concerns directions of nearly minimum width:

**Stability theorem.** If \(q=1\), or if \(q\ge2\) and \((q-1)w^2<1\), then some maximum clique \(C\) and sign \(\sigma\in\{\pm1\}\) satisfy
\[
\left\|u-\sigma\frac{\mathbf1_C}{\sqrt q}\right\|_2
\le
\sqrt{\min\!\left\{\frac{2\delta^2}{w^2},\ \delta+\frac{\delta^2}{w^2}\right\}}
+\sqrt q\left(w-\frac1{\sqrt q}\right).
\]
In particular the rate is **linear** in \(\delta\) as \(\delta\to0\) at fixed \(q\), with constants independent of graph order. The near-minimum estimate, rather than the baseline width and exact minimizer characterization, is the contribution here.

## Assumptions and scope

The stable-set polytope is the convex hull of the indicators of all stable sets, including the empty set. It contains \(0\) and all standard basis vectors, so it is full dimensional. The support function is \(h_K(u)=\max_{x\in K}\langle x,u\rangle\) and the width is \(W_K(u)=h_K(u)+h_K(-u)\). The theorem assumes equality of the chromatic and clique numbers of \(G\), not perfection of all its induced subgraphs. No other coordinate realization is used.

For the comparability graph of a nonempty finite poset, \(K\) is Stanley's chain polytope, and maximum cliques are longest chains. Assigning to each element the maximum cardinality of a chain ending at it gives a coloring with the height of the poset many colors. The bound thus applies with normalized longest-chain indicators and with \(q\) the poset height.

## Proof

Fix a proper coloring with \(q\) nonempty classes \(A_j\). For unit \(u\) put \(L_j=\sum_{v\in A_j}|u_v|\) and \(Q_j=\sum_{v\in A_j}u_v^2\). Positive and negative supports within a class are stable, giving \(L_j\le w\). Thus \(1=\sum_jQ_j\le\sum_jL_j^2\le qw^2\). A size-\(q\) clique meets each stable set in at most one vertex, so its normalized indicator has width \(1/\sqrt q\).

Let \(d_j=w^2-Q_j\). These nonnegative numbers sum to \(\delta\). Pick a coordinate \(v_j\) of largest magnitude \(m_j\) in each class. The estimate \(Q_j\le m_jL_j\le m_jw\) gives \(0\le w-m_j\le d_j/w\). The squared mass of the other coordinates is at most either of the following bounds:
\[
\begin{aligned}
\sum_{v\in A_j\setminus\{v_j\}}u_v^2
&\le (L_j-m_j)^2\le (w-m_j)^2\le d_j^2/w^2,\\
Q_j-m_j^2&\le Q_j(1-Q_j/w^2)\le d_j.
\end{aligned}
\]
The first bound uses the residual \(\ell_1\) mass of the class to obtain the linear rate. With \(z_{v_j}=w\operatorname{sgn}(u_{v_j})\) and all other coordinates zero, summing these estimates and the squared peak errors gives
\[
\|u-z\|_2^2\le\min\{2\delta^2/w^2,\,\delta+\delta^2/w^2\},
\]
using \(\sum_jd_j^2\le\delta^2\). All selected coordinates are nonzero: for \(q=1\) this follows from \(\|u\|_2=1\), and for \(q\ge2\) from \(\delta<w^2\), equivalent to the stated threshold.

For \(q\ge2\) any two selected magnitudes sum to at least \(2w-\delta/w>w\). Opposite signs would give at least that sum in width by the two singleton tests. Two same-sign vertices with no edge would also give at least that sum by the two-element stable set and the empty set. Thus the selected vertices form a maximum clique and have one common sign \(\sigma\). This is automatic for \(q=1\). The distance from \(z\) to its signed normalized clique indicator is \(\sqrt q(w-1/\sqrt q)\); the triangle inequality now proves the estimate. Taking \(\delta=0\) also gives the exact minimizing directions.

The linear rate cannot in general be replaced by \(o(\delta)\) for fixed \(q\). For \(q\ge2\), take \(G=K_q\), set \(e=\mathbf1/\sqrt q\), and consider \(u_t=(e+t e_1)/\|e+t e_1\|_2\) for \(t>0\) tending to zero. Its nearest minimizing direction is \(e\); its distance from \(e\) is asymptotic to \(\sqrt{1-1/q}\,t\), while its width, the largest coordinate, exceeds \(1/\sqrt q\) by \((1-1/q)t+O(t^2)\). For \(q=1\) use the edgeless graph on two vertices and \(u_t=(\sqrt{1-t^2},t)\), of width \(\sqrt{1-t^2}+t\) and distance asymptotic to \(t\) from \(e_1\).

## Prior coverage of the baseline theorem

The unquantified width and direction statements also follow from the fractional-antiblocker formulation in [*Fractional antiblockers determine every Hansen inradius*](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-fractional-antiblockers-determine-every-hansen-inradius-with-an--79ea53f863b0), Finding and proof inequalities (6)–(8). Indeed the height-zero section of the Hansen polytope is \((K-K)/2\), and its polar in the section is the projection of the Hansen polar. Those inequalities at height \(t\) bound the positive and negative parts of a projected polar point \(x\) by \(\|x^+\|_2\le(1-t)\sqrt\mu\) and \(\|x^-\|_2\le(1+t)\sqrt\mu\), where \(\mu=\max_{p\in Q(\bar G)}\|p\|_2^2\) and \(Q(\bar G)\) is the clique-inequality polytope of the complement. The squared projected norm is at most \(2(1+t^2)\mu\); the bound \(4\mu\) is attained only at \(t=\pm1\), by the projected signed doubled maximizers over \(Q(\bar G)\). Since minimum width is twice the centered inradius of the section, it is \(1/\sqrt\mu\) and the directions are exactly the signed normalized maximizers. On a \(q\)-coloring each class sums to at most one on \(Q(\bar G)\); equality in the norm bound \(\mu\le q\) requires one coordinate equal to one in every class, and any two such coordinates must be adjacent in \(G\). Clique indicators attain \(\mu=q\). This recovers the baseline theorem without a stability modulus. No ordering or priority within the shared publication date is inferred.

The earlier [enriched-chain inradius and contact theorem](https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-height-and-width-are-the-exact-euclidean-radii-of-enriched-chain--db93f92ff100) also yields the ordinary-chain baseline: the enriched support is \(h_K(|u|)\le W_K(u)\). Its unit inball-contact normals are the signed longest-chain indicators, and among these, only the constant-sign patterns can have ordinary-chain width \(1/\sqrt q\). The earlier perfect-graph stable-set inradius concerns inscribed balls in \(K\), not the widths of \(K\); order-polytope results concern the order polytope, not the chain polytope.

## Verification and limitations

The proof above is unrestricted in graph order. The bundled standalone `checks/graph_width_checker.py` tests the baseline value and the weaker squared-deficit estimate (the second term in the minimum) on finite examples; it does not certify the sharpened rate. Its recorded output counts 810 graphs, 23,936 directions, 7,284 qualifying instances and 2,391 maximum-clique contacts. No numerical check is used to prove the theorem. The sufficient width threshold and constants are not claimed optimal. The underlying polytopes are classical, and historical priority for the stability estimate remains provisional.

## References

1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23. [Author copy](https://math.mit.edu/~rstan/pubs/pubfiles/66.pdf).
2. I. Ahmad, G. Fourier and M. Joswig, *Order and chain polytopes of maximal ranked posets*, [arXiv:2309.01626](https://arxiv.org/abs/2309.01626).
3. R. Freij-Hollanti and T. Lundström, *\(f\)-vector inequalities for order and chain polytopes*, [arXiv:2312.13890](https://arxiv.org/abs/2312.13890).
4. S. Hu and M. Laurent, *On the linear extension complexity of stable set polytopes for perfect graphs*, [arXiv:1706.05496](https://arxiv.org/abs/1706.05496).
