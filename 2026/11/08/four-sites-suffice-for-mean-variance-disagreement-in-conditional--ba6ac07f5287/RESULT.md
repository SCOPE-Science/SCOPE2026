# Four sites suffice for mean–variance disagreement in conditional Moran fixation time

## Finding

Consider the discrete-time, birth–death Moran process on a finite connected simple, undirected, unweighted graph, with mutant fecundity \(r>0\), resident fecundity \(1\), and precisely one mutant introduced at a specified vertex. Let \(T\) be the number of updates until either extinction or fixation, and let \(F\) be the event of fixation (all vertices ultimately mutant). Define the conditional mean and variance
\[
\mu_s(r)=\mathbb E_s[T\mid F],\qquad V_s(r)=\operatorname{Var}_s(T\mid F).
\]

**Sharp four-site theorem.** On every such graph with two or three vertices, for every \(r>0\), the initial-vertex weak rankings by \(\mu_s(r)\) and by \(V_s(r)\) agree: every minimizer of one is a minimizer of the other. On four vertices they can have disjoint minimizer sets, even for advantageous mutants. Explicitly, let \(G\) have vertices \(\{0,1,2,3\}\) and edges \(\{01,02,03,12,23\}\), the diamond \(K_4\) minus the edge \(13\). Set \(r=5\). Vertices \(0,2\), of degree three, uniquely minimize the conditional mean, while vertices \(1,3\), of degree two, uniquely minimize conditional variance. Thus four is the smallest admissible population size for this choice disagreement.

The exact strict comparisons (degree-three start minus degree-two start) are
\[
\mu_0(5)-\mu_1(5)=-\frac{3095643}{121414228}<0,
\qquad
V_0(5)-V_1(5)=\frac{4612716655893867}{14741414760835984}>0.
\]
By graph automorphism, \(\mu_0=\mu_2\), \(\mu_1=\mu_3\), and likewise for \(V\). Strict inequalities imply an open interval of fitness values around \(5\) with the same discrepancy, although its exact endpoints are not claimed.

## Assumptions and scope

At each integer update, select a reproducing vertex proportional to its fecundity (\(r\) for a mutant and \(1\) for a resident); then select one of that vertex's neighbors uniformly and replace the neighbor with its offspring. Same-type replacements count as time steps. Initially only the designated vertex is mutant. There is no mutation, no vertex or edge weighting, and no environmental variation. The graph is connected with at least two vertices; hence eventual absorption is almost sure and fixation has positive probability for every \(r>0\).

Conditioning is on *successful fixation*, not on absorption into either state. The variance is in squared update units, not a coefficient of variation. The comparison concerns optimal *starting vertices within the same graph*, not comparisons among network topologies or population-level average seeding. It is distinct from the likelihood of success.

## Proof

**1. Exact moment identities.** Let \(\mathcal S\) contain the nonempty proper mutant-vertex subsets. Denote by \(Q\) the substochastic transition matrix between states in \(\mathcal S\), and by \(b\) the column of one-step probabilities of fixation. The transition from a mutant set \(S\) to a set \(S\cup\{y\}\), where \(y\notin S\), is
\[
P(S,S\cup\{y\})=\frac{r}{r|S|+n-|S|}\sum_{x\in S\cap N(y)}\frac1{\deg(x)},
\]
and a transition losing \(y\in S\) has probability
\[
P(S,S\setminus\{y\})=\frac1{r|S|+n-|S|}\sum_{x\in N(y)\setminus S}\frac1{\deg(x)}.
\]
Every remaining probability contributes to the self-loop. In the transient index order set \(A=I-Q\). Because the population is finite and connected, \(A\) is invertible. Let \(h_S=\mathbb P_S(F)\), \(a_S=\mathbb E_S[T\mathbf1_F]\), and \(z_S=\mathbb E_S[T^2\mathbf1_F]\), taking \(T=0\) when already absorbed. First-step conditioning gives exactly
\[
Ah=b,\qquad Aa=h,\qquad Az=2a-h.
\]
Consequently, for a singleton initial mutant state \(S=\{s\}\),
\[
\mu_s=\frac{a_S}{h_S},\qquad V_s=\frac{z_S}{h_S}-\left(\frac{a_S}{h_S}\right)^2.
\]
These formulae include self-loops and all unsuccessful paths through the indicator \(\mathbf1_F\); they are not moment formulae for the unconditional absorption time.

**2. Minimality for at most three vertices.** The unique connected two-vertex graph is symmetric. Up to isomorphism, the three-vertex graphs are the triangle \(K_3\) (all seeds equivalent) and the path \(P_3\). For \(P_3\), let \(e\) be either endpoint and \(c\) the center. Applying the matrix identities above and simplifying over the rational-function field \(\mathbb Q(r)\) yields
\[
\mu_e(r)=\frac{2(5r^2+8r+5)}{2r^2+r+2},\quad
\mu_c(r)-\mu_e(r)=-\frac{3}{2r+1},
\]
\[
V_e(r)=\frac{2(24r^4+91r^3+148r^2+91r+24)}{(2r^2+r+2)^2},\quad
V_c(r)-V_e(r)=-\frac{6(r+2)}{(2r+1)^2}.
\]
The two differences are strictly negative for every real \(r>0\). Thus the center simultaneously minimizes both metrics for all fitnesses, and the other connected graph classes have equal metrics by symmetry. This proves the all-parameter three-site lower bound without a sampled-rate inference.

**3. Exact four-site witness.** For the diamond graph and \(r=5\), applying the same recurrence on its \(2^4-2=14\) transient mutant configurations gives the conditional values

| Starting-vertex orbit | Fixation probability | Conditional mean | Conditional variance |
|---|---|---|---|
| Degree three \(\{0,2\}\) | \(1122875/1488426\) | \(72659908801/8913687172\) | \(1954046189090893922205/79453819000277357584\) |
| Degree two \(\{1,3\}\) | \(422375/496142\) | \(6854218276/838231909\) | \(136482613376588448261/5621061866126274248\) |

Subtracting the two means and the two variances and reducing yields the strict rational inequalities stated in the finding. This establishes the four-site example and completes the sharpness proof.

## Verification

`verify_moran.py` constructs the full transient transition matrix using exact symbolic arithmetic. It checks the path mean and variance differences as identities in \(\mathbb Q(r)\), verifies the triangle and two-node symmetries, and reproduces all diamond fractions and strict inequalities at \(r=5\). Requires Python 3 and SymPy; run `python verify_moran.py`.

`verify_doob.py` is a separate standard-library-only exact-rational implementation using frozenset configurations, explicit Gaussian elimination and the conditional Doob transition matrix \(\widetilde Q_{S,R}=Q_{S,R}h_R/h_S\). It independently computes the conditional first and second moments for all four diamond seed vertices and matches every rational value. Run `python verify_doob.py`. Both programs were executed successfully against the files accompanying this result.

## Relationship to prior work

Hindersin and Traulsen (2014) analyzed four-vertex Moran fixation probabilities, mean conditional fixation times, and their dependence on the starting vertex, including the diamond. In particular, they identified a fitness-dependent crossover in *mean* fixation time. That work's examined results do not compare conditional variances of different starting vertices or establish a sharp population-size threshold for mean–variance minimizer disagreement. Its matrix formulation supplies the starting point of the present calculation, not the claimed qualitative result.

Ashcroft, Traulsen and Galla (2015) developed full fixation-time distributions for one-dimensional birth–death chains; the diamond has configuration-dependent transitions and cannot be reduced to mutant count alone. Hindersin, Möller, Traulsen and Bauer (2015 preprint/2016 publication) presented exact fixation-probability and *mean*-time computations for arbitrary small graphs and gave the conditional transition transform; the paper's inspected sections do not give the seed-wise variance reversal. Hathcock and Strogatz (2018 preprint/2019 publication) treated fixation-time distributions on complete graphs and rings, chiefly in the large-population regime, not the heterogeneous four-site diamond. These published techniques may be used to recover the new fractions, but their stated results do not imply the cross-objective rankings or sharp minimum. This is a best-knowledge originality assessment, not a claim of exhaustive historical priority.

## Limitations

The theorem addresses conditional moments in the discrete-time birth–death Moran process only. It does not claim a result for death–birth updating, directed or weighted networks, unconditional absorption-time variance, or arbitrary graph sizes. The exact fitness interval around \(5\) is not characterized. A different fixation success probability across initial-vertex classes remains relevant to applications. No independent external verification or empirical biological validation is claimed.

## References

1. L. Hindersin and A. Traulsen, “Counterintuitive properties of the fixation time in network-structured populations,” *Journal of the Royal Society Interface* 11 (2014), 20140606. Earliest identified public preprint: arXiv:1406.4415, 2014-06-17. https://arxiv.org/abs/1406.4415 ; https://doi.org/10.1098/rsif.2014.0606
2. P. Ashcroft, A. Traulsen and T. Galla, “When the mean is not enough: Calculating fixation time distributions in birth-death processes,” *Physical Review E* 92 (2015), 042154. arXiv:1504.04249. https://arxiv.org/abs/1504.04249 ; https://doi.org/10.1103/PhysRevE.92.042154
3. L. Hindersin, M. Möller, A. Traulsen and B. Bauer, “Exact numerical calculation of fixation probability and time on graphs,” *BioSystems* 150 (2016), 87–91. arXiv:1511.02696. https://arxiv.org/abs/1511.02696 ; https://doi.org/10.1016/j.biosystems.2016.08.010
4. D. Hathcock and S. H. Strogatz, “Fitness dependence of the fixation-time distribution for evolutionary dynamics on graphs,” *Physical Review E* 100 (2019), 012408. arXiv:1812.05652. https://arxiv.org/abs/1812.05652 ; https://doi.org/10.1103/PhysRevE.100.012408
