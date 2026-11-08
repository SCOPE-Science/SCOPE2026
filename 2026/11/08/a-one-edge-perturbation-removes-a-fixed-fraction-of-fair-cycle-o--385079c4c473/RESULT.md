# A one-edge perturbation removes a fixed fraction of fair cycle orientations

## Finding

For every integer \(n\geq4\), take the simple cycle \(C_n\), with vertices \(0,\ldots,n-1\) and edge \(e_i=\{i,(i+1)\bmod n\}\). Each edge is an indivisible good, which is allocated to one of its two endpoints. An agent values each incident allocated edge at its positive common edge weight and every nonincident edge at zero. All edges have weight \(1\) except \(e_0\), whose weight is \(\tau>0\). Fairness means **zero-inclusive EFX**: after removal of *any* one good from any other agent's bundle, the first agent must not envy that reduced bundle.

Let \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\) and \(L_0=2,L_1=1,L_{j+2}=L_{j+1}+L_j\) be Fibonacci and Lucas numbers. Define the period-six sequence
\[
(\delta_0,\delta_1,\delta_2,\delta_3,\delta_4,\delta_5)=(1,1,0,-1,-1,0),\qquad \delta_{j+6}=\delta_j.
\]
The **exact number** \(N_n(\tau)\) of labeled edge orientations satisfying zero-inclusive EFX is
\[
\boxed{N_n(\tau)=\begin{cases}
L_n+2\cos(n\pi/3),&\tau=1,\\[2pt]
F_{n+1}+\delta_n,&0<\tau<1\ \text{or}\ \tau>1.
\end{cases}}
\]
Thus the count does not depend on the magnitude or sign of the nonzero deviation from equal weights. For every \(n\geq4\), any unequal positive weight deletes some fair orientations. More sharply, with \(\varphi=(1+\sqrt5)/2\),
\[
\lim_{n\to\infty}\frac{N_n(\tau)}{N_n(1)}=\frac{\varphi}{\sqrt5}\quad\text{for every fixed }\tau>0,\ \tau\ne1.
\]
The asymptotic loss is \(1-\varphi/\sqrt5\), approximately \(27.64\%\), even for an arbitrarily small positive or negative perturbation. For instance, the counts at \(n=4,6,10\) are respectively \((6,20,122)\) when \(\tau=1\) and \((4,14,88)\) when \(\tau\ne1\).

## Assumptions and scope

The result concerns complete (no discarded goods) endpoint orientations of a **simple** cycle, with distinguishable vertices and edges, common strictly positive values at the two endpoints of each edge, and additive incident-edge valuations. For all other agents an edge has value zero. It uses the strong definition of EFX which permits removal of goods worth zero to the envious agent, as in Definition 2.1 of Zeng--Mehta. The graph and valuations are fixed before choosing an orientation, and the count is over all \(2^n\) endpoint orientations, with no quotient by rotations or reflections.

The perturbation is only one edge. The case \(\tau=0\) is not covered. For arbitrary varying edge weights or general monotone/nonadditive valuations, the theorem makes no claim.

## Proof

**1. A local exact criterion.** Let \(B_v\) be the bundle of vertex \(v\), \(I_v\) its total value, and \(d^-_v=|B_v|\). In an arbitrary orientation of a simple graph with positive additive edge values, zero-inclusive EFX is equivalent to
\[
\text{for every oriented edge }u\to v\text{ with }d^-_v\ge2:\quad I_u\ge w_{uv}.\tag{1}
\]
Indeed, the only item in \(B_v\) that \(u\) can value is edge \(uv\). If \(d^-_v=1\), removal of that edge leaves zero value to \(u\). If \(d^-_v\ge2\), removal of another item leaves exactly \(w_{uv}\), and this is the maximal possible post-removal value of \(B_v\) to \(u\). Nonadjacent pairs have post-removal value zero, proving both directions.

**2. The equal-weight orientation language.** Write \(s_i=+\) when \(e_i\) points from \(i\) to \((i+1)\bmod n\), and \(s_i=-\) in the opposite direction. With all weights equal, (1) fails precisely at an edge directed from a vertex with no incoming edge to a vertex with two incoming edges. These are exactly the cyclic triples \(+-+\) and \(-+-\) in the sign word \(s_0\cdots s_{n-1}\). Thus a cyclic sign word is EFX exactly when it avoids these two triples. Equivalently, a nonconstant word has every maximal cyclic run of either sign of length at least two. Both constant words are allowed.

**3. A heavier distinguished edge.** If \(\tau>1\), an ordinary outgoing edge directed into a two-edge bundle is acceptable exactly when its tail has an incoming edge; this is the equal-weight condition. The distinguished edge, however, cannot be directed into a two-edge bundle because its tail can receive at most one ordinary edge of value \(1<\tau\). Therefore the heavy-edge fair orientations are precisely the equal-weight fair words with
\[
(s_0=+\Rightarrow s_1=+)\quad\text{and}\quad(s_0=-\Rightarrow s_{n-1}=-).\tag{2}
\]

**4. A lighter distinguished edge.** If \(0<\tau<1\), the distinguished edge itself has the same admissibility condition as at equal weight: an ordinary incoming edge of value \(1\) suffices at its tail. For ordinary edges, the only new failure occurs when the tail has received solely the light distinguished edge, so its value \(\tau\) is smaller than the outgoing ordinary weight \(1\). In sign form the new exclusions, on top of the equal-weight language, are
\[
(s_1=+,\ s_2=-)\quad\text{and}\quad(s_{n-2}=+,\ s_{n-1}=-).\tag{3}
\]
Within equal-weight fair words, the first excluded pattern necessarily has \(s_0=+\), and the second necessarily has \(s_0=-\). The corresponding exclusions in (2) are, respectively, a marked edge **last** in a \(+\)-run, and **first** in a \(-\)-run. Those in (3) are a marked edge **next-to-last** in a \(+\)-run, and **second** in a \(-\)-run. Because every nonconstant fair word has sign runs of length at least two, cyclic shifting gives explicit bijections: the shift \(t_i=s_{i-1}\) maps the first heavy exclusion to the first light exclusion; \(t_i=s_{i+1}\) maps the second heavy exclusion to the second light exclusion. The two exclusions are disjoint in each case according to \(s_0\). Hence lighter and heavier perturbations remove exactly the same number of orientations, for all \(n\ge4\).

**5. Exact enumeration.** Index ordered sign-pair states by \((--,-+,+-,++)\) and let \(T\) transfer from \((a,b)\) to \((b,c)\), with unit weight unless \((a,b,c)\) is alternating. Explicitly,
\[
T=\begin{pmatrix}1&1&0&0\\0&0&0&1\\1&0&0&0\\0&0&1&1\end{pmatrix},
\qquad\det(xI-T)=(x^2-x-1)(x^2-x+1).
\]
The number of cyclic nonalternating words is \(\operatorname{tr}(T^n)\), so its eigenvalues yield
\[
N_n(1)=\operatorname{tr}(T^n)=L_n+2\cos(n\pi/3).
\]
For \(\tau>1\), the \(+\)-case in (2) consists of exactly the closed transfer walks starting at pair \((++)\). The \(-\)-case has the same count by sign complement and rotation. Thus
\[
N_n(\tau)=2(T^n)_{++,++}\qquad(\tau>1).
\]
By Cayley--Hamilton the sequence \(q_n=2(T^n)_{++,++}\) satisfies \(q_{n+4}=2q_{n+3}-q_{n+2}+q_n\), with \(q_0=q_1=q_2=q_3=2\). The sequence \(F_{n+1}+\delta_n\) satisfies the same recurrence and four initial values, because its Fibonacci component solves \(x^2-x-1\) and its periodic component solves \(x^2-x+1\). Therefore \(q_n=F_{n+1}+\delta_n\) for all \(n\ge0\). Step 4 extends this count to \(0<\tau<1\).

**6. Strictness and asymptotics.** For every \(n\ge4\), the cyclic word having a \(+\)-run of length two followed by a \(-\)-run of length \(n-2\), positioned with the marked edge last in its \(+\)-run, is fair at equal weights and excluded by (2). Thus the drop is strict. Binet's formulas give \(L_n\sim\varphi^n\) and \(F_{n+1}\sim\varphi^{n+1}/\sqrt5\); the trigonometric and period-six corrections are bounded. Their ratio tends to \(\varphi/\sqrt5\), as claimed. Since the numbers of orientations jump at \(\tau=1\) for every \(n\ge4\), even arbitrarily small weight changes exhibit a genuine combinatorial discontinuity.

## Verification

The standalone `verify.py` recomputes the EFX condition directly from every ordered agent pair and every possible removed good, rather than relying on (1). It compares that decision to the independent local inequality (1) and the forbidden-pattern criteria for five exact rational weights \(\tau\in\{1/2,3/4,1,5/4,2\}\) on all \(2^n\) labeled orientations for every \(3\le n\le13\): \(81{,}880\) direct cases with no discrepancies. It also verifies transfer-matrix counts against the formulas through \(n=100\). The script uses only Python's standard library and can be executed with `python verify.py`.

## Relationship to prior work

Christodoulou, Fiat, Koutsoupias and Sgouritsa (EC 2023) introduced the graphical goods model and analyzed existence and hardness of EFX orientations. Zeng and Mehta (arXiv:2404.13527, 2024) defined strong EFX-orientability and proved existence for all bipartite graphs, with results for other chromatic classes and binary valuations. Deligkas, Eiben, Goldsmith and Korchemna (arXiv:2409.13616, 2024) developed EF1 algorithms and EFX hardness/parameterized algorithms. Zhou, Wei, Li and Li (IJCAI 2024) compared multiple EFX variants in graphical mixed-manna settings. Kanellopoulos and collaborators (arXiv:2512.25033, 2025) subsequently developed structural parameterized algorithms for EF and EFX orientations. These results concern existence, complexity or other fairness variants; their relevant inspected statements do not imply the exact one-edge sensitivity census here.

A previous calculation for a unit-weight four-cycle, viewed as \(K_{2,2}\), gives six EFX orientations and is consistent with this theorem's \(n=4\) equal-weight specialization. The new statement addresses all cycle lengths and a distinct one-edge perturbation, and proves the asymptotic fraction of orientations lost. No claim is made that enumerating binary words without isolated runs is new in combinatorics; its role is to establish the fairness sensitivity law.

## Limitations

This is a special-family exact theorem, not a classification for all weighted cycles or graphs. The discontinuity concerns the **number** of fair orientations, not the existence of a fair orientation (both constant directed cycles remain fair). Strict positivity is essential to the local comparison. The threshold \(\tau=1\) is exact: arbitrarily small perturbations cause a fixed asymptotic percentage loss even though the surviving orientations depend only on whether the exceptional edge is heavier or lighter. Independent mathematical audit and exhaustive worldwide publication-priority certification have not been performed; an unindexed equivalent enumeration remains a residual risk.

## References

1. G. Christodoulou, A. Fiat, E. Koutsoupias, A. Sgouritsa, *Fair Allocation in Graphs*, EC 2023, DOI: https://doi.org/10.1145/3580507.3597764 .
2. J. A. Zeng, R. Mehta, *On the Structure of EFX Orientations on Graphs*, arXiv:2404.13527, first submitted April 21, 2024, https://arxiv.org/abs/2404.13527 .
3. A. Deligkas, E. Eiben, T.-L. Goldsmith, V. Korchemna, *EF1 and EFX Orientations*, arXiv:2409.13616, https://arxiv.org/abs/2409.13616 .
4. Y. Zhou, T. Wei, M. Li, B. Li, *A Complete Landscape of EFX Allocations on Graphs: Goods, Chores and Mixed Manna*, IJCAI 2024, https://doi.org/10.24963/ijcai.2024/338 .
5. S. Kanellopoulos et al., *EF(X) Orientations: A Parameterized Complexity Perspective*, arXiv:2512.25033, https://arxiv.org/abs/2512.25033 .
