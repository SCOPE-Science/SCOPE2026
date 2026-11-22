# Intermediate antagonism and the quartic entropy of frozen multiplex opinion states

## Finding

In a pair of **identical** connected finite simple \(d\)-regular social-contact graphs, the synchronous antagonistic sign-update model has a complete absorbing-state classification in the intermediate-coupling window \(d-2<a<d\) (\(d\ge2\), antagonistic cross-layer weight \(-a\)). Every absorbing state is exactly one of:

1. The two fully **aligned**, uniform configurations: every vertex has \((A_i,B_i)=(+1,+1)\) or every vertex has \((A_i,B_i)=(-1,-1)\).
2. A sitewise **opposed** configuration \(B_i=-A_i\) at all vertices, where each vertex has at least one neighbor in the *same layer* with its own opinion. Such configurations may be spatially mixed.

In particular, every sitewise opposed configuration with no singleton-colored vertex is absorbing; there are no other absorbing configurations. This distinguishes structural frozen heterogeneity from the two uniform oppositely polarized states already identified in the originating work.

For the naturally cubic prism contact graph \(G_n=C_n\square K_2\), \(n\ge3\), the complete number of absorbing configurations is
\[
F_n=2+\operatorname{tr}(T^n),
\]
with the fully specified \(16\times16\) binary transfer matrix \(T\) below. Its characteristic polynomial is exactly
\[
\det(zI-T)=z^8(z^2+2)(z^2-z+1)(z^4-3z^3-z^2+2).
\]
Consequently, \(F_3=36\), \(F_4=120\), \(F_5=366\), and, writing \(\alpha\) for the unique real root in \((3,4)\) of \(z^4-3z^3-z^2+2=0\),
\[
F_n=\alpha^n+O(2^n),\qquad
\alpha=3.2494533945\ldots .
\]
Thus the number of nonuniform *frozen* bilayer configurations grows exponentially at a precise natural graph-family entropy: \(\lim_{n\to\infty}\frac1{2n}\log F_n=\frac12\log\alpha\) per vertex of one contact layer. Every conclusion holds for every real \(a\in(1,3)\), without dependence on its exact value inside that interval.

## Assumptions and scope

Let \(G=(V,E)\) be a connected finite simple undirected \(d\)-regular graph, \(d\ge2\), with \(|V|=N\). Both multiplex layers use **the same labeled graph** \(G\). Each site has signs \(A_i,B_i\in\{-1,+1\}\), and the simultaneous microscopic update is
\[
A_i'=\operatorname{sign}\left(\sum_{j\sim i} A_j-aB_i\right),\qquad
B_i'=\operatorname{sign}\left(\sum_{j\sim i} B_j-aA_i\right).
\]
As in the motivating model, a zero argument is resolved randomly with both signs having positive probability. An **absorbing configuration** means a configuration maintained with probability one under one update. In the stated open window no field in a fixed configuration vanishes, so the classification agrees with deterministic strict fixed points. Define a **singleton-colored vertex** of \(A\) to mean a vertex \(i\) with \(A_j=-A_i\) for every \(j\sim i\). A coloring with no such vertex is sometimes described as a binary partition into two (possibly empty) vertex sets each inducing minimum degree at least one. No proper graph coloring condition is intended.

The prism graph has vertices \((i,h)\), \(i\in\mathbb Z/n\mathbb Z\), \(h\in\{0,1\}\), with edges to \((i-1,h)\), \((i+1,h)\), and \((i,1-h)\). It is a connected cubic graph for each \(n\ge3\), including the triangular prism at \(n=3\). In the multiplex, the prism is repeated as the same graph in both layers, with corresponding sites coupled by \(-a\). The total number of physical binary signs is \(4n\).

## Proof

**Step 1: one agreeing site forces global agreement.** Suppose an absorbing state has \(A_i=B_i=s\) at some vertex \(i\), with \(s=\pm1\). For the first field to preserve \(s\),
\[
0<s\left(\sum_{j\sim i} A_j-aB_i\right)=\sum_{j\sim i}sA_j-a.
\]
Since \(a>d-2\), this requires \(\sum_{j\sim i}sA_j=d\), i.e. \(A_j=s\) for **every** neighbor. Applying the second field likewise gives \(B_j=s\) for every neighbor. Hence every neighbor of \(i\) is aligned with sign \(s\). Graph connectedness propagates this through all vertices. Thus any absorbing state with even one aligned pair must be one of the two completely uniform aligned states. Both are absorbing because their local signed fields equal \(d-a>0\) times their own signs; the inequality \(a<d\) is essential.

**Step 2: all other absorbing states are sitewise opposed.** In a state with no aligned pairs, \(B_i=-A_i\) for every \(i\). Let \(r_i\) be the number of neighbors of \(i\) with \(A_j\ne A_i\). The local field signed by \(A_i\) equals \(d-2r_i+a\). The \(B\)-layer signed field is the *same* number because both its spin and its neighbor sum are sign-reversed. If \(r_i\le d-1\), the expression is at least \(a-(d-2)>0\). If \(r_i=d\), it equals \(a-d<0\). These are the only possibilities, so the configuration is absorbing if and only if \(r_i\le d-1\) for each vertex, exactly the no-singleton-color condition. This completes the graph-uniform classification. Strict inequalities guarantee no undecided ties in any classified state.

**Step 3: a finite transfer for every prism size.** Let the four rung letters be \(\mathcal S=\{(-1,-1),(-1,+1),(+1,-1),(+1,+1)\}\). For rung letters \(x,y,z\in\mathcal S\), define the local predicate
\[
P(x,y,z)=[y_0=y_1]\quad\text{or}\quad
\bigwedge_{h=0}^1[x_h=y_h\ \text{or}\ z_h=y_h].
\]
If the two spins in the central rung \(y\) agree, their rung edge already supplies each a same-colored neighbor, so no restriction on adjacent rungs is needed. Otherwise each central spin requires a matching left or right neighbor, exactly as the second disjunct says. Index a \(16\times16\) matrix by ordered letter pairs \((x,y)\in\mathcal S^2\), and define the entry from \((x,y)\) to \((u,z)\) by
\[
T_{(x,y),(u,z)}=\mathbf 1_{\{u=y\}}\mathbf 1_{\{P(x,y,z)\}}.
\]
A closed length-\(n\) walk through this overlap transfer uniquely specifies the cyclic sequence of \(n\) labeled rung letters obeying the condition at every vertex. Conversely each such sequence gives precisely one rooted closed walk of length \(n\), with the first column fixed at the labeled rung zero. This is a bijection, including for \(n=3\) where previous and next rung are different. Thus the number of sitewise opposed absorbing configurations is \(\operatorname{tr}(T^n)\), while the two globally aligned absorbing states are disjoint, proving \(F_n=2+\operatorname{tr}(T^n)\).

**Step 4: exact finite algebra and asymptotics.** The explicitly defined \(16\times16\) integer matrix has characteristic polynomial
\[
\chi_T(z)=z^8(z^2+2)(z^2-z+1)(z^4-3z^3-z^2+2).
\]
This **finite integer identity** is checked from the matrix entries by the standalone `verify.py`, using exact integer matrix multiplication and the Faddeev–LeVerrier/Newton identities, with no floating-point computation. Therefore its eigenvalues, counted with algebraic multiplicity, provide exact power-trace expressions for every integer \(n\ge1\); finite initial calculations alone are not being extrapolated to all \(n\).

For the final quartic write \(q(z)=z^3(z-3)-(z^2-2)\). On \(|z|=2\), \(|z^3(z-3)|\ge8\) while \(|z^2-2|\le6\). Rouché's theorem thus shows that \(q\) has three roots strictly inside \(|z|=2\) and one outside. Since \(q(3)=-7<0\) and \(q(4)=50>0\), the exterior root is a unique real \(\alpha\in(3,4)\). All other characteristic roots have absolute value below \(2\): the nonquartic roots have modulus \(\sqrt2\), \(1\), or \(0\). Consequently
\[
\operatorname{tr}(T^n)=\alpha^n+O(2^n)
\]
with leading coefficient one. Addition of the two uniform states proves the claimed asymptotic and entropy limit.

## Verification

The standalone standard-library script `verify.py` reconstructs the exact rung-transfer matrix independently from the verbal predicate, computes its entire characteristic polynomial with integer arithmetic, and verifies its power traces for \(3\le n\le12\). A separate microscopic-sign test directly enumerates all \(4^N\) two-layer sign configurations for the cubic graphs \(K_4\), \(K_{3,3}\), the triangular prism, and the square prism, comparing the true microscopic absorption inequalities to the graph classification for \(a=2\). The enumeration checks, respectively, \(256\), \(4096\), \(4096\), and \(65536\) states. All comparisons pass; the prism fixed-state totals are \(36\) and \(120\) for \(n=3,4\). The exact matrix polynomial is a finite certificate usable for *all* \(n\); the graph-general classification is independently proved analytically in Steps 1–2.

Reproduce with `python3 verify.py` using Python 3 and no external packages. The checker neither simulates random tie outcomes nor purports to prove behavior away from absorbing configurations.

## Relationship to prior work

Hughes et al. [1, Sections 2–4] specify the same two-layer sign rule and prove that the two spatially uniform opposed states are absorbing; their inspected main text does not classify all absorbing microstates in the intermediate-inhibition interval or give a prism transfer entropy. The homogeneous aligned states occurring here rely on \(a<d\) and are **not** the uniform oppositely polarized states of that paper.

A separate published result [2] proves that at *dominant* inhibitory strength \(a>d\), the complete update becomes the immediate involution \((A,B)\mapsto(-B,-A)\). That regime has \(2^N\) absorbing states on arbitrary layer graphs and is disjoint from \(d-2<a<d\). Its enumeration neither implies the present no-singleton graph condition nor the prism polynomial.

A separate prism census [3] concerns a **single** uncoupled graph \(C_n\square K_2\) with open-neighbor majority, whose fixed-state count grows as a Lucas number. Our system has two coupled copies of this graph, an antagonistic local field, and exponentially different absorption count. Classical symmetric-threshold theory [4] bounds eventual temporal periods by two under its hypotheses but does not give the intermediate-coupling fixed microstates or this exact graph-family count. The binary no-singleton-color interpretation is related to familiar zero-temperature Ising local-minimum conditions, so the generic local-neighbor rule itself is not asserted as a novel mathematical technique; the precise coupled-model reduction and evaluated prism entropy are the claimed contribution.

## Limitations

Both contact layers must use the **same** graph; identical degrees but different edge sets are not covered. The graph must be connected, simple, and regular, and the inhibitory magnitude must lie strictly in the open window \(d-2<a<d\). The endpoints may have ties or other absorbing states; no endpoint classification is claimed. The result counts only time-independent absorbing configurations, not all two-cycles, their attraction basins, likely outputs of simulations or convergence times. The fixed-state asymptotic is per prism rung, with exactly two vertices per rung in each original contact layer; it is not a mean-field entropy or a probability of ultimately reaching a nonuniform state. The exact quartic enumeration is a natural special-family refinement rather than a graph-universal closed formula. Earlier general enumeration frameworks may contain indirectly related statements; accessible comparisons do not constitute exhaustive historical-priority certification. Independent scientific review remains to be done.

## References

[1] J. C. M. Hughes, A. Kusmartseva, G. Muschert, H. F. Jelinek and F. V. Kusmartsev, *Metastability and Entropy Peaks in Antagonistic Multiplex Consensus Dynamics*, Entropy **28** (2026), article 857; first public online date 1 August 2026, https://doi.org/10.3390/e28080857 ; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC13512852/ .

[2] *Exact involution and exponential prevalence of two-cycles under dominant antagonistic coupling*, publicly indexed research finding, 12 October 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-involution-and-exponential-prevalence-of-two-cycles-under--39f67e98d2ad .

[3] *A Lucas-number orbit census for synchronous majority on prism graphs*, publicly indexed research finding, 17 November 2026; https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-lucas-number-orbit-census-for-synchronous-majority-on-prism-gr--f39104b86e05 .

[4] E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 .
