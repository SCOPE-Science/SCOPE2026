# First balanced Fourier cancellation in nonedge theta graphs: the eight-vertex \(\Theta_{2,3,4}\) obstruction

## Finding
Let \(\Theta_{a,b,c}\) be the simple graph formed from two distinct terminals by joining them with three pairwise internally vertex-disjoint paths of respective edge lengths \(2\le a\le b\le c\). Put \(n=a+b+c-1\). Identify the three named vertex colours with \(\mathbb Z/3\mathbb Z\). For every frequency \(k\in (\mathbb Z/3\mathbb Z)^{V(\Theta_{a,b,c})}\), define the unnormalized Fourier multiplier
\[
W_{a,b,c}(k)=\sum_{x:V\to\mathbb Z/3\mathbb Z\atop x\text{ proper}}\omega^{\sum_{v\in V}k_vx_v},\qquad \omega=\exp(2\pi i/3).
\]
For **all** seven nonisomorphic nonedge theta graphs with \(n\le8\), the only Fourier zeros apart from those imposed by global colour translation occur for \(\Theta_{2,3,4}\). Its balanced frequencies have exactly 584 extra zeros, by character support degree \(d\):

| \(d\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Extra zeros | 0 | 0 | 4 | 8 | 74 | 106 | 210 | 138 | 44 |

Since balanced frequencies number \(3^{n-1}\), the rank of unnormalized counting convolution by the proper-colouring indicator equals \(3^{n-1}\) for the other six theta graphs and equals **1603** (out of 6561 ambient dimensions) for \(\Theta_{2,3,4}\). All four degree-two cancellations arise from exactly two unordered vertex pairs whose colours are **independent and uniform** under the uniform measure on proper three-colourings.

## Assumptions and scope
All vertices and path interiors are labelled; path lengths refer to edges. The two terminals are labelled 0 and 1. Along each path, internal vertices are assigned fresh consecutive integer labels in order from terminal 0 to terminal 1. The paths occur in nondecreasing length order. The seven triples are \((2,2,2),(2,2,3),(2,2,4),(2,2,5),(2,3,3),(2,3,4),(3,3,3)\); their respective vertex numbers are 5, 6, 7, 8, 7, 8, 8. No path of length one is admitted, because such a path is a direct terminal edge and yields a distinct edge-gluing construction.

By **balanced** we mean \(\sum_vk_v=0\pmod3\). Global translation \(x_v\mapsto x_v+z\) of all colours shows that \(W(k)=0\) for every unbalanced frequency. An **extra** zero is a balanced frequency with \(W(k)=0\). Degree means \(\#\{v:k_v\ne0\}\).

## Proof
The finite classification is proved by an exact transfer recurrence, with the complete exhaustiveness boundary specified above. Work in the integer group ring \(R=\mathbb Z[t]/(t^3-1)\). Every element has a representative \(A+Bt+Ct^2\), with multiplication implemented as a three-entry cyclic convolution. Evaluation at a primitive cube root satisfies
\[
A+B\omega+C\omega^2=0\quad\Longleftrightarrow\quad A=B=C.
\]
The equivalence is exact because \(1,\omega\) are linearly independent over \(\mathbb Q\) and \(\omega^2=-1-\omega\).

Fix terminal colours \(u,v\in\{0,1,2\}\). For one path \(P=(0,w_1,\ldots,w_{\ell-1},1)\), define \(B_P(u,v;k;t)\in R\) by summing \(t^{\sum_{j=1}^{\ell-1}k_{w_j}x_{w_j}}\) over its proper internal colourings with endpoint colours \(u,v\). It is computed by the recurrence
\[
D_0(s)=\mathbf1_{s=u},\qquad D_j(s)=t^{k_{w_j}s}\sum_{r\ne s}D_{j-1}(r),\quad 1\le j<\ell,
\]
followed by \(B_P(u,v;k;t)=\sum_{r\ne v}D_{\ell-1}(r)\). Thus the exact Fourier polynomial for the whole graph is
\[
F(k;t)=\sum_{u,v=0}^2t^{k_0u+k_1v}\prod_{P\in\{P_a,P_b,P_c\}}B_P(u,v;k;t)\in R.
\]
For each frequency \(k\) there are at most three short paths and nine pairs of terminal colours; all sums and products are integers. In particular \(W(k)=F(k;\omega)\).

There are precisely seven integer triples satisfying \(2\le a\le b\le c\) and \(a+b+c-1\le8\). The standalone program `transfer_check.py` evaluates this recurrence at **every one** of the \(3^n\) frequencies for each triple. It tests the exact coefficient equality \(A=B=C\). The independently structured `direct_check.py` instead enumerates **all** \(3^n\) vertex-colour assignments, filters the proper ones from graph edges, and counts the three exponent residues for every frequency. The standalone `replay_check.py` verifies equality of the complete output vectors from both constructions at every one of **25,029** frequencies. These checks produce the following exhaustive table:

| Paths | \(n\) | Proper colourings | Extra balanced zeros | Nonzero multipliers |
|---|---:|---:|---:|---:|
| (2,2,2) | 5 | 30 | 0 | 81 |
| (2,2,3) | 6 | 42 | 0 | 243 |
| (2,2,4) | 7 | 102 | 0 | 729 |
| (2,3,3) | 7 | 78 | 0 | 729 |
| (2,2,5) | 8 | 186 | 0 | 2187 |
| (2,3,4) | 8 | 162 | 584 | 1603 |
| (3,3,3) | 8 | 186 | 0 | 2187 |

In the specified labelling of \(\Theta_{2,3,4}\), the paths are \((0,2,1)\), \((0,3,4,1)\), and \((0,5,6,7,1)\). The four balanced degree-two zero frequencies have respective nonzero coordinate pairs \((3,7)\) and \((4,5)\), each with the two opposite assignments of frequencies \(1\) and \(2\). These pairs have exactly 54 equal-colour outcomes among the 162 proper colourings. For any unordered pair of vertices, palette-permutation symmetry gives
\[
W(e_i-e_j)=N_{\mathrm{equal}}-\tfrac12(162-N_{\mathrm{equal}})=\tfrac12(3N_{\mathrm{equal}}-162).
\]
Consequently its opposite-character pair vanishes precisely at \(N_{\mathrm{equal}}=54\), which is also exactly the independence condition for two uniformly distributed three-valued variables under the global palette-permutation symmetry. Absence of any further degree-two zeros proves there are exactly two such unordered vertex pairs. Finally, Fourier diagonalization of convolution on the finite abelian colour group makes its rank exactly the number of nonzero Fourier multipliers.

## Verification
With Python 3 and only the standard library, put `direct_check.py`, `transfer_check.py`, and `replay_check.py` in one directory and run `python replay_check.py`. The resulting `census.json` table and full per-frequency equality assertion are included. Running either named checker separately reproduces the same seven-row census. Both constructions use integer arithmetic only; no floating-point threshold or random trial is involved. This establishes exhaustiveness *within the stated seven graphs*, not for larger theta graphs.

## Relationship to prior work
Brown, Hickman, Sokal and Wagner (2000, arXiv:math/0012033v1) define generalized theta graphs and give their chromatic-polynomial formula, including the special status of paths of length one (Section 2). Their chromatic polynomial determines the zero-frequency colouring total, not the full 3-ary Fourier transform or its frequencywise zeros. Published work on first-harmonic sampling of cycles and complete bipartite colourings addresses lower-order evaluation Gram matrices rather than this characterwise convolution spectrum. The previously available full ternary colouring transform for complete bipartite graphs covers the special graph \(\Theta_{2,2,2}\), not the 584-zero obstruction at \(\Theta_{2,3,4}\). No examined source supplied or implied the seven-case first-obstruction table.

## Limitations
The classification is finite and ends at eight vertices; larger theta graphs may have other cancellation types. The displayed degree counts classify zeros by degree but not by every graph-automorphism orbit. Exact computations certify the finite ranges they enumerate and do not prove an all-order nonvanishing theorem. Unindexed historical evaluations, especially vertex-weighted chromatic computations, remain a possible priority risk. No independent external mathematical audit has been performed.

## References
- J. Brown, C. Hickman, A. D. Sokal, D. G. Wagner, *On the Chromatic Roots of Generalized Theta Graphs*, arXiv:math/0012033v1 (public 2000-12-05), https://arxiv.org/abs/math/0012033; especially Section 2 and equation (2.6).
- MSC2020, 43A25, Fourier and Fourier-Stieltjes transforms on locally compact and other abelian groups, https://msc2020.org/MSC_2020.pdf.
