# Three-state Potts frustration and a split-pair entropy anomaly on cocktail-party graphs

## Finding
For every integer \(m\ge 2\), let \(G_m\) be the graph obtained from the complete graph on \(2m\) labeled vertices by deleting a fixed perfect matching \(\mathcal M\). Each vertex has a spin in \(\{0,1,2\}\), with antiferromagnetic energy
\[
H_m(\sigma)=J\sum_{\{u,v\}\in E(G_m)}\mathbf1_{\{\sigma_u=\sigma_v\}},\qquad J>0.
\]
Put \(m=3t+s\), where \(t\ge0\) and \(s\in\{0,1,2\}\). The exact minimum energy is
\[
\frac{E_m}{J}=2(3t^2+2st+s)-2m.
\]
The exact number \(g_m\) of labeled, named-color ground-state assignments is
\[
g_m=\begin{cases}
\displaystyle\frac{(3t)!}{(t!)^3},&s=0,\\
\displaystyle 3(2t+3)\frac{(3t+1)!}{(t+1)!(t!)^2},&s=1,\\
\displaystyle 3(2t+3)\frac{(3t+2)!}{((t+1)!)^2t!},&s=2.
\end{cases}
\]
A matched pair is called *split* when its endpoints have different spin colors. If \(s=0\), no ground state contains a split pair. If \(s\in\{1,2\}\), every ground state has either zero or exactly one split pair, and under the uniform ground-state measure
\[
\Pr(\text{one split pair})=\frac{2(t+1)}{2t+3},\qquad
\Pr(\text{no split pair})=\frac{1}{2t+3}.
\]
Conditional on a split pair, its location is uniformly distributed among the \(m\) matching pairs. Thus an entropy-selected single split pair is present with probability tending to one for sequences \(m\to\infty\) with \(m\not\equiv0\pmod3\), while the probability is identically zero in the divisible-by-three subsequence.

The residual entropy per vertex exists along all three residue classes and is \(\frac12\log3\). More precisely,
\[
g_m\sim\begin{cases}
\displaystyle\frac{3\sqrt3}{2\pi m}\,3^m,&m\equiv0\pmod3,\\
\displaystyle\frac{3\sqrt3}{\pi}\,3^m,&m\equiv1,2\pmod3.
\end{cases}
\]
The subexponential degeneracy prefactor therefore has a genuine modular change, not merely a shift of the minimum energy.

## Assumptions and scope
The graph is the **labeled** complete \(m\)-partite graph with all parts of size two, equivalently the matching-deleted complete graph. Colors \(0,1,2\) are distinct and named. There is no external field, no unequal edge coupling, no spin disorder, and no assertion concerning finite-temperature transitions. Energy is measured in the standard zero-energy-for-unlike-neighbors convention above, without normalization by the number of edges. A matching pair contains no interacting edge. The theorem is stated for \(m\ge2\), so the graph contains interacting edges.

## Proof
For a configuration \(\sigma\), let \(N_c\) be the number of vertices with color \(c\), and let \(b\) be the number of split matching pairs. Since \(\sum_cN_c=2m\) and exactly \(m-b\) matching pairs are monochromatic, the number of monochromatic interacting edges obeys the exact identity
\[
\frac{H_m(\sigma)}J=F(N_0,N_1,N_2)-m+b,
\qquad F(N_0,N_1,N_2)=\sum_{c=0}^2\binom{N_c}{2}.
\tag{1}
\]
The function \(F\) is discretely convex: moving one vertex from a color class with population at least two greater than another strictly decreases \(F\). Its unconstrained integer minimum \(F_0\) occurs at the three populations differing by at most one. For \(s=0\), these are \((2t,2t,2t)\); for \(s=1\), they are permutations of \((2t+1,2t+1,2t)\); for \(s=2\), permutations of \((2t+2,2t+1,2t+1)\).

Every split pair changes the parity of the population of exactly two colors. Thus the balanced populations for \(s=0\) can be realized with \(b=0\), by assigning each matching pair one monochromatic color. Equation (1) proves optimality and shows that equality requires exactly these balanced monochromatic pairs.

For \(s\in\{1,2\}\), the balanced populations have exactly two odd entries and so require \(b\ge1\). Exactly one split matching pair between those two odd color classes, with all other pairs monochromatic, realizes \(F=F_0\) and \(b=1\). Conversely, configurations with \(F=F_0\) and minimum energy must have \(b=1\). There also exists an all-even population triple with \(F=F_0+1\): permutations of \((2t+2,2t,2t)\) for \(s=1\), and permutations of \((2t+2,2t+2,2t)\) for \(s=2\). It is realized by monochromatic pairs, with \(b=0\), and has the same energy.

These are the only two equality cases. Indeed, integer convexity gives \(F\ge F_0\); when \(s\ne0\), equality forces two odd populations and hence \(b\ge1\). Equality of (1) with \(F_0-m+1\) therefore requires either \((F,b)=(F_0,1)\) or \((F_0+1,0)\). For the latter, all color populations are even; writing \(N_c=2a_c\) with \(\sum_ca_c=m\) gives
\[
F=\sum_c(2a_c^2-a_c)=2\sum_ca_c^2-m.
\]
Its integer minimum is achieved exactly by balanced integers \(a_c\in\{t,t+1\}\), with exactly \(s\) of them equal to \(t+1\). A one-unit transfer in the original balanced populations shows that its \(F\)-value is \(F_0+1\). This establishes both the equality structure and the minimum-energy formula, since \(F_{\mathrm{even}}-m=2\sum_ca_c^2-2m=2(3t^2+2st+s)-2m\).

Now count the ground states. When \(s=0\), all pairs are monochromatic, with \(t\) pairs of each color, giving \(g_m=(3t)!/(t!)^3\). For \(s=1\) or \(s=2\), the number of no-split ground states is
\[
A_m=3\frac{m!}{((t+1)!)^s(t!)^{3-s}}.
\tag{2}
\]
The factor three chooses which one color is exceptional when \(s=1\), or which one color is not elevated when \(s=2\). A one-split ground state has a balanced population triple. There are three choices for the even-population color when \(s=1\), or the high even-population color when \(s=2\), then \(m\) choices of split pair and two assignments of its endpoint colors. Distributing the remaining \(m-1\) monochromatic pairs yields
\[
B_m=\begin{cases}
\displaystyle 6m\frac{(m-1)!}{(t!)^3},&s=1,\\
\displaystyle 6m\frac{(m-1)!}{(t+1)!(t!)^2},&s=2.
\end{cases}
\tag{3}
\]
The factorial identities in (2)–(3) give \(B_m=2(t+1)A_m\). Consequently \(g_m=A_m+B_m\) has the stated form, and the split/no-split probabilities follow. Matching-pair permutation symmetry makes the unique split location uniform.

For the asymptotic counts, Stirling's formula gives the balanced ternary multinomial coefficient \(m!/\prod_ca_c!\sim (3\sqrt3/(2\pi m))3^m\). In the nonzero residue classes, (2)–(3) multiply this by \(3(2t+3)\sim2m\), giving the stated constant. Finally \(\lim_{m\to\infty}\frac{\log g_m}{2m}=\frac12\log3\), uniformly across the three residue classes.

## Verification
Two standalone Python programs accompany the proof. `check_bruteforce.py` enumerates **all** \(3^{2m}\) named spin assignments directly on the actual edge set for \(2\le m\le6\), checking the minimum energy, ground-state count, and one-split count. `check_transfer.py` independently uses a nine-choice-per-matched-pair transfer count grouped only by two color populations and the split count, checking the formulas for \(2\le m\le18\), and numerical convergence of the Stirling prefactors at six much larger indices. Both ran to completion and printed their PASS markers. These finite tests are regression evidence, not a substitute for the all-size combinatorial proof above.

## Relationship to prior work
The standard Potts partition-function formulation and its graph-polynomial relations are established in Sokal's 2005 survey (especially section 2.2). Shrock and Tsai (1998) study ground-state entropy and chromatic polynomials for homeomorphically expanded graph families; Salas and Shrock (2001) treat lattice tubes, including complete-bipartite cross-section tubes, and Yamaguchi and Okabe (2001) study the three-dimensional antiferromagnetic model by simulation. In contrast, this claim concerns **positive minimum frustration** when a fixed three-color palette is insufficient to properly color a graph with more than three parts. In particular, evaluating the chromatic polynomial at three colors vanishes for \(m>3\) and does not provide the minimum positive number of monochromatic edges or its degeneracy. The classification of competing all-monochromatic-pair and single-split-pair optimal structures, with exact modular entropy prefactors, was not located in the examined sources. These observations are a scoped literature comparison, not proof of worldwide priority.

## Limitations
The infinite-family proof depends on uniform positive antiferromagnetic coupling and exactly three named colors; it does not extend without further analysis to arbitrary coupling disorder, fields, or different part sizes. The residual entropy is defined as the zero-temperature limit for each finite graph followed by \(m\to\infty\), not as an assertion about a finite-temperature thermodynamic Gibbs phase. A direct earlier treatment of this specific matching-deleted family might exist under graph-partition terminology not reached by the indexed searches. Independent audit has not been performed.

## References
1. R. Shrock and S.-H. Tsai, *Ground State Entropy of Potts Antiferromagnets: Cases with Noncompact \(W\) Boundaries Having Multiple Points at \(1/q=0\)* (public preprint October 6, 1998), https://arxiv.org/abs/cond-mat/9810057 .
2. J. Salas and R. Shrock, *Exact \(T=0\) Partition Functions for Potts Antiferromagnets on Sections of the Simple Cubic Lattice* (public preprint February 10, 2001), https://arxiv.org/abs/cond-mat/0102190 .
3. C. Yamaguchi and Y. Okabe, *Three-dimensional antiferromagnetic \(q\)-state Potts models: application of the Wang-Landau algorithm* (public preprint August 31, 2001), https://arxiv.org/abs/cond-mat/0108540 .
4. A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids* (public preprint March 25, 2005), https://arxiv.org/abs/math/0503607 .
5. E. W. Weisstein, *Cocktail Party Graph*, MathWorld, https://mathworld.wolfram.com/CocktailPartyGraph.html .
