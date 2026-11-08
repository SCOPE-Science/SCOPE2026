# Total-degree ranking of endemic infection on two equitable communities

## Finding

For the nonlinear discrete-time product-form SIS map used by Dung and Phuc (2026), a connected simple graph with an equitable partition into **exactly two** nonempty cells has a positive endemic fixed point if and only if \(\beta\rho(A)>\delta\). Above this threshold the endemic fixed point is unique and cell-constant. Write \(d_i\) for each cell's common *internal* degree and \(b_i\) for its common degree to the other cell. The two endemic infection probabilities \(u_1,u_2\) satisfy the **parameter-independent exact comparison**

\[
\operatorname{sgn}(u_1-u_2)=\operatorname{sgn}\bigl((d_1+b_1)-(d_2+b_2)\bigr)
\]

for every \(0<\beta,\delta<1\) with \(\beta\rho(A)>\delta\). Thus equilibrium prevalence is ordered by **full network degrees**, not necessarily by the isolated-community thresholds \(1/d_i\). These statements include both equal-degree and unequal-cell-size cases.

The six-vertex graph \(C_4\vee K_2\) is a smallest connected, internally connected two-cell equitable example with both isolated thresholds finite in which these rankings strictly disagree. Its two-cell quotient is \(Q=\left(\begin{smallmatrix}2&2\\4&1\end{smallmatrix}\right)\). The four-cycle has isolated threshold \(1/2\) and full degree \(4\), while the edge has isolated threshold \(1\) and full degree \(5\). Consequently, whenever the full graph is supercritical, the edge has **greater per-vertex endemic infection** despite its **higher (less vulnerable) isolated threshold**. For \(\beta=3/10\), \(\delta=2/5\), the edge is even isolated-subcritical while the cycle is isolated-supercritical. Exact rational sub/supersolutions enclose the endemic probabilities by

\[
855/1000<u_{C_4}<858/1000<896/1000<u_{K_2}<899/1000.
\]

The two-cell restriction is structural: with three equitable cells, full-degree ranking can already fail. A graph with three six-vertex cells and quotient \(\left(\begin{smallmatrix}4&1&0\\1&2&1\\0&1&5\end{smallmatrix}\right)\) has full degrees \((5,4,6)\), but near its invasion threshold the second cell has strictly **higher** endemic probability than the first, although its full degree is lower.

## Assumptions and scope

Let \(G=(V,E)\) be a finite connected undirected loopless simple graph with adjacency matrix \(A\). Choose \(0<\beta,\delta<1\). The deterministic independence-approximation recursion on \([0,1]^V\) is

\[
F_i(p)=1-\bigl[1-(1-\delta)p_i\bigr]\prod_{j\sim i}(1-\beta p_j).
\]

This is a discrete deterministic infection-probability map, **not** a claim about the stationary law of the finite stochastic SIS chain, whose absorbing healthy state remains present.

An equitable two-cell partition \(V=C_1\sqcup C_2\) means that every vertex of cell \(C_i\) has precisely \(d_i\) neighbors in its own cell and \(b_i\) in the other cell. Connectivity gives \(b_1,b_2>0\) and undirectedness gives \(|C_1|b_1=|C_2|b_2\). The primary ranking holds for internal degrees \(d_i\ge0\), including singleton cells. For **minimality of the threshold-ranking counterexample**, additionally require both induced communities connected with \(|C_i|\ge2\), so \(d_i\ge1\) and their isolated thresholds \(1/d_i\) are positive finite numbers.

The quotient \(Q=\left(\begin{smallmatrix}d_1&b_1\\b_2&d_2\end{smallmatrix}\right)\) is irreducible. Its Perron root \(\Lambda=\rho(Q)\) is also \(\rho(A)\): the strictly positive Perron eigenvector of \(Q\) lifts to a strictly positive eigenvector of \(A\), which therefore has the same Perron eigenvalue.

## Proof

**Existence and uniqueness at the exact threshold.** Every coordinate of \(F\) is nondecreasing in every component of \(p\); \(F(0)=0\) and \(F(\mathbf1)\ll\mathbf1\). The derivative at zero is

\[
DF(0)=(1-\delta)I+\beta A.
\]

If \(\beta\rho(A)>\delta\), let \(v\gg0\) be a Perron eigenvector. For sufficiently small \(\varepsilon>0\), Taylor's formula gives \(F(\varepsilon v)\gg\varepsilon v\). Monotone iteration from \(\varepsilon v\) increases and is bounded by \(\mathbf1\), hence reaches a strictly positive fixed point \(p^*\ll\mathbf1\).

For every \(p\gg0\) and \(0<t<1\), set \(a_0=(1-\delta)p_i\) and \(a_j=\beta p_j\) for neighbors \(j\sim i\). The scalar function \(h_i(t)=1-\prod_{j\in\{0\}\cup N(i)}(1-ta_j)\) has \(h_i(0)=0\) and

\[
h_i''(t)=-\sum_{r\ne s}a_ra_s\prod_{m\ne r,s}(1-ta_m)<0.
\]

The strict inequality holds because each graph vertex has a neighbor, all inputs are positive, and all factors lie in \((0,1]\) for \(0\le t\le1\). Therefore \(F(tp)\gg tF(p)\). If distinct positive fixed points \(x,y\) existed, interchange them if necessary so \(t=\min_i x_i/y_i<1\). The monotonicity and strict ray-sublinearity imply \(x=F(x)\ge F(ty)\gg ty\), a contradiction in a coordinate attaining the minimum. Thus the positive fixed point is unique.

Conversely, for \(p\gg0\) the strict union bound gives \(F(p)\ll[(1-\delta)I+\beta A]p\). At any positive fixed point, pairing with a positive left Perron vector gives \(1<1-\delta+\beta\rho(A)\). Thus a positive fixed point is impossible when \(\beta\rho(A)\le\delta\). No global convergence statement for every initial condition is required here.

**Cell reduction and equality.** Since the partition is equitable, the cell-constant subspace is invariant under \(F\), with induced map

\[
F_1(x,y)=1-[1-(1-\delta)x](1-\beta x)^{d_1}(1-\beta y)^{b_1},
\]
\[
F_2(x,y)=1-[1-(1-\delta)y](1-\beta y)^{d_2}(1-\beta x)^{b_2}.
\]

An increasing iteration from a small lifted Perron eigenvector produces a cell-constant positive equilibrium; full-system uniqueness forces this to equal \(p^*\). If \(x=y=q>0\), the two fixed-point identities yield \((1-\beta q)^{d_1+b_1}=(1-\beta q)^{d_2+b_2}\), hence \(d_1+b_1=d_2+b_2\). Conversely, if these full degrees coincide, the constant-vector subspace is invariant, and its supercritical fixed point is uniform; hence \(x=y\).

**Strict sign from the threshold and continuity.** The supercritical parameter domain \(\{(\beta,\delta)\in(0,1)^2:\delta<\beta\Lambda\}\) is convex and connected. The positive fixed point varies continuously there: in a compact neighborhood of any supercritical parameters, one can choose a common sufficiently small strictly positive Perron subsolution; any limit of equilibria stays strictly positive, and uniqueness identifies the limit. The sign of \(x-y\) thus cannot change anywhere in this domain when the full degrees differ, since the preceding paragraph excludes equality.

To determine the sign, fix a sufficiently small \(0<\beta_0<1/\Lambda\) and let \(\delta\uparrow\beta_0\Lambda\) from below. The equilibria tend to zero; otherwise their positive limit would contradict nonexistence at equality. The fixed-point expansion \(p=DF(0)p+O(\|p\|^2)\) implies that normalized equilibrium vectors converge to the positive Perron direction \(v\) of \(Q\). If \(r=v_1/v_2>0\), the Perron equations reduce to

\[
b_2r^2+(d_2-d_1)r-b_1=0.
\]

This quadratic has exactly one positive root, and its value at \(r=1\) equals \((d_2+b_2)-(d_1+b_1)\). Thus \(r>1\) exactly when \(d_1+b_1>d_2+b_2\). Continuity and absence of equality propagate this strict sign to every supercritical parameter pair. This completes the primary theorem.

**Smallest isolated-threshold inversion.** In \(C_4\vee K_2\), the quotient rows are \((2,2)\) and \((4,1)\), full degrees are \(4,5\), and isolated spectral radii are \(2,1\), respectively. The Perron eigenvalue is \(\Lambda=(3+\sqrt{33})/2\), so at \((\beta,\delta)=(3/10,2/5)\), \(\beta\Lambda>\delta\) and \(\beta/\delta=3/4\) lies strictly between the two isolated thresholds. The rational vectors \(L=(855/1000,896/1000)\) and \(U=(858/1000,899/1000)\) satisfy \(F(L)\gg L\) and \(F(U)\ll U\) **exactly**, as checked by the attached standalone code. Their monotone iterates bound the unique positive fixed point, giving the displayed strict, nonoverlapping coordinate bounds.

No example satisfying the two connected nontrivial-cell assumptions can have fewer than six vertices. If the cell sizes total at most four, differing positive internal degrees are impossible. At five vertices, the only possible differing positive induced degrees are \((2,1)\) on cell sizes \((3,2)\). Equitability of the cross edges demands \(3b_1=2b_2\), \(1\le b_1\le2\), \(1\le b_2\le3\). The sole solution is \((b_1,b_2)=(2,3)\), where both full degrees equal \(4\), so no strict inversion occurs. The six-vertex example is therefore minimal.

**Three-cell boundary.** Use three six-vertex cells, respectively: \(K_6\) with a perfect matching deleted, a six-cycle, and \(K_6\). Add a perfect matching between the first and second cells and between the second and third cells. This produces a connected undirected equitable graph with quotient

\[
Q_3=\begin{pmatrix}4&1&0\\1&2&1\\0&1&5\end{pmatrix}.
\]

Its full degrees are \((5,4,6)\). Its Perron root \(\Lambda_3>5\), since \(Q_3\) is symmetric irreducible and has a diagonal entry \(5\). For the positive Perron vector, the first row gives \(v_2=(\Lambda_3-4)v_1>v_1\). By the same near-threshold expansion as above, the positive equilibrium for any fixed sufficiently small \(\beta\) and \(\delta\) sufficiently close to \(\beta\Lambda_3\) from below has \(u_2>u_1\), despite \(D_2<D_1\). Hence the two-cell ranking theorem does not extend unchanged to three cells.

## Verification

Run `python3 check.py` from the extracted package. The checker uses only Python's standard library and exact rational arithmetic. It reconstructs the six-vertex graph, verifies its equitable quotient and full degrees, checks that the full map restricts identically to the quotient at rational test points, verifies the stated rational sub- and supersolution inequalities, exhausts the integer cross-degree possibilities for the five-vertex minimality boundary, and checks a strict Rayleigh bound for the three-cell example. These finite computations verify the concrete certificates; the full all-parameter comparison follows from the analytic proof, not from finite testing.

## Relationship to prior work

Dung and Phuc (arXiv:2607.14048, July 15, 2026) define local epidemic thresholds by internal-community adjacency spectral radii and prove comparison with the global threshold, then simulate aggregate infection. They do not state the exact endemic per-vertex rank rule, its six-vertex threshold-rank inversion, or a two-versus-three-cell boundary. The original Chakrabarti et al. 2008 paper supplies the **same** nonlinear product-form SIS update and eigenvalue threshold; neither the original equation nor threshold is claimed as new here. Bonaccorsi et al. (Phys. Rev. E 90, 012810, 2014) also study steady endemic community probabilities for a continuous-time, full-mesh cloud model with distinct intra- and intercluster infection rates; their equations (5), (12) and Theorem 3 do not imply the present strict discrete product-map degree ordering. Bonaccorsi et al. (arXiv:1412.6157, especially Section 4 and their equation (16)) prove equitable quotient reduction for continuous-time NIMFA, and Prasse et al. (arXiv:2102.13151) give broader NIMFA equitable-clustering results. These are substantial predecessors, but their continuous-time quadratic-incidence dynamics are not the discrete-time product map; the present parameter-uniform comparison and minimal inverse ranking are not supplied by their stated results. The underlying monotone-system and Perron-vector techniques are classical; the contribution is the complete sharp comparison for the specified recent community-threshold setting.

## Limitations

The theorem concerns fixed points of a deterministic independence approximation, not stochastic stationary persistence; the finite-state stochastic SIS process can reach extinction. The sign theorem requires exactly two equitable cells and homogeneous transmission and recovery. It does not assert full trajectory convergence, a ranking for nonequitable partitions, rank monotonicity of total community infection sums when group sizes differ, or a three-cell analogue. Literature equivalence in unindexed sources remains a possibility; independent review has not been performed.

## References

- Hoang Phi Dung and Nguyen Hong Phuc, *An Epidemic Threshold Set for Networks*, first posted 2026-07-15, arXiv:2607.14048, https://arxiv.org/abs/2607.14048 .
- Deepayan Chakrabarti, Yang Wang, Chenxi Wang, Jurij Leskovec, Christos Faloutsos, *Epidemic Thresholds in Real Networks*, ACM TISSEC 10 (2008), DOI:10.1145/1284680.1284681, author's open PDF https://faculty.mccombs.utexas.edu/deepayan.chakrabarti/mywww/papers/tissec08epidemic.pdf .
- Stefano Bonaccorsi, Stefania Ottaviano, Simone Mugnolo, and Francesco De Pellegrini, *Epidemic Outbreaks in Networks with Equitable or Almost-Equitable Partitions*, arXiv:1412.6157, https://arxiv.org/abs/1412.6157 .
- Stefano Bonaccorsi, Stefania Ottaviano, Francesco De Pellegrini, Annalisa Socievole and Piet Van Mieghem, *Epidemic outbreaks in two-scale community networks*, Physical Review E 90, 012810 (2014), DOI:10.1103/PhysRevE.90.012810, https://www.nas.ewi.tudelft.nl/people/Piet/papers/PhysRevE2014_SIS_Community.pdf .
- Bastian Prasse, Karel Devriendt and Piet Van Mieghem, *Clustering for epidemics on networks: A geometric approach*, Chaos 31, 063115 (2021), arXiv:2102.13151, https://arxiv.org/abs/2102.13151 .
