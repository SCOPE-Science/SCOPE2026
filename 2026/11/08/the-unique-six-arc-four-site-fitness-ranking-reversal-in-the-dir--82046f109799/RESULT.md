# The unique six-arc four-site fitness-ranking reversal in the directed Moran process

## Finding

**Theorem (sharp small-digraph classification).** Consider the birth–death Moran process described below on a strongly connected, unweighted, loopless directed graph. Let \(\rho_i(r)\) be the fixation probability of one mutant initially at vertex \(i\) when the mutant's relative fecundity is \(r>1\). Among all such graphs with at most three vertices, the ordering of every pair \(\rho_i(r),\rho_j(r)\) is independent of \(r>1\). The same holds on every four-vertex graph with at most five arcs. Among four-vertex graphs with exactly six arcs, **precisely one isomorphism class** admits a strict reversal of a pairwise ranking on \(r>1\), and within this class precisely one unordered pair of vertices reverses (up to automorphisms).

A representative of this exceptional class, with vertices \(1,2,3,4\), has arc adjacency matrix

\[
A=\begin{pmatrix}0&0&0&1\\0&0&0&1\\0&1&0&0\\1&1&1&0\end{pmatrix}.
\]

For this graph, the reversal is between vertices \(2\) and \(4\). There exists exactly one \(r_*\in(3,4)\), numerically \(r_*=3.43583928029502\ldots\), such that

\[
\rho_2(r)<\rho_4(r)\quad (1<r<r_*),\qquad
\rho_2(r)=\rho_4(r)\quad (r=r_*),\qquad
\rho_2(r)>\rho_4(r)\quad (r>r_*).
\]

The word *unique* above applies only to the enumerated four-vertex, six-arc class; the theorem makes no global classification of larger directed graphs or of weighted/self-looped graphs.

## Assumptions and scope

Let \(G=(V,E)\) be a finite strongly connected simple directed graph, with \(|V|=n\) and no self-loops; an ordered pair is an arc if and only if its adjacency entry is one. Its outdegree is \(d_i=\sum_j A_{ij}>0\), and its replacement probability is \(W_{ij}=A_{ij}/d_i\). Every vertex carries exactly one resident or mutant. A resident has fecundity \(1\), and a mutant fecundity \(r>1\). At each discrete update an individual is selected for reproduction proportionally to fecundity and then independently selects an outgoing target according to its row of \(W\); the target is replaced by an offspring. There is no mutation after initialization. Fixation means reaching the all-mutant absorbing configuration; extinction means reaching the all-resident configuration. No fitness heterogeneity across sites, alternative death–birth updating, adaptive graph changes, or population-size variation is allowed.

The finite classification ranges over every loopless strongly connected digraph with \(n=2,3\), and with \(n=4\) and at most six arcs. The one-vertex case is trivial, with no pair of sites. In particular, the claim that four vertices are necessary is global within this graph class, whereas the minimum six arcs is claimed only **conditional on four vertices**.

## Proof

**1. Exact fixation equations.** Write \(S\subseteq V\) for the current mutant set and \(h(S)\) for fixation probability from \(S\), with \(h(\varnothing)=0\) and \(h(V)=1\). For \(i\in S\), \(j\notin S\), the transition rate *after removing a common positive normalization factor* that adds \(j\) is \(rW_{ij}\); for \(i\notin S\), \(j\in S\), the rate that removes \(j\) is \(W_{ij}\). Cancelling holding transitions gives the exact linear system

\[
\sum_{i\in S,j\notin S}rW_{ij}\bigl(h(S)-h(S\cup\{j\})\bigr)
+\sum_{i\notin S,j\in S}W_{ij}\bigl(h(S)-h(S\setminus\{j\})\bigr)=0
\]

for all \(\varnothing\ne S\ne V\). Strong connectivity ensures that from any nonabsorbing configuration there is a finite positive-probability succession of additions leading to fixation, and likewise a succession of removals leading to extinction. Hence absorption occurs almost surely and the finite Dirichlet system is nonsingular for every \(r>0\). In particular, all \(\rho_i(r)=h(\{i\})\) are uniquely defined rational functions of \(r\). Its reduced denominators cannot vanish at \(r>0\).

**2. Exact graph exhaustion and certification of noncrossing.** A graph with \(n\) vertices corresponds to a bit pattern over its \(n(n-1)\) possible arcs. Enumerate every pattern in the stated ranges, retain exactly those that are strongly connected by forward and reverse reachability, and identify two graphs if their off-diagonal adjacency strings agree after a simultaneous permutation of rows and columns. The complete list of isomorphism-class counts by \((n,|E|)\) is

\[
(2,2):1;\ (3,3):1;\ (3,4):2;\ (3,5):1;\ (3,6):1;
\ (4,4):1;\ (4,5):4;\ (4,6):16.
\]

For every representative and every unordered pair of sites, solve the \(2^n-2\) equations in step 1 over the exact rational-function field \(\mathbb Q(r)\), and reduce \(\rho_i(r)-\rho_j(r)\). Identically zero comparisons cannot cross. For all others, substitute \(r=1+t\) in the numerator and count coefficient sign variations. Descartes' rule of signs implies that a polynomial with no sign variations has no positive zero \(t>0\); continuity together with nonsingularity then proves that the corresponding fixation ranking cannot reverse for \(r>1\). The exhaustive calculation gives \(113\) nonidentically-zero pair comparisons; \(112\) have zero variations. The sole exception is the six-arc graph above and the pair \(\{2,4\}\), with one variation. The exhaustive enumeration, quotient rule, and exact symbolic checks are contained in the standalone `verify_symbolic.py`; no finite random experiments are used in this step.

**3. Unique crossing on the exceptional graph.** Direct rational elimination of the same system yields

\[
\rho_2(r)-\rho_4(r)=\frac{r^3 P(r)}{D(r)},
\]

where

\[
\begin{aligned}
P(r)={}&77760r^{10}+163944r^9-423738r^8-2023272r^7\\
&-3747633r^6-4662639r^5-4212709r^4-2570307r^3\\
&-956688r^2-185526r-11880,
\end{aligned}
\]

and \(D(r)=\sum_{k=0}^{14}c_kr^{14-k}\), with the coefficient vector, in decreasing powers,

\[
(c_0,\ldots,c_{14})=(116640,1165428,5613462,17204508,37727010,63686499,86411496,95625178,86411496,63686499,37727010,17204508,5613462,1165428,116640).
\]

Every coefficient of \(D\) is positive; therefore \(D(r)>0\) for \(r>0\). The descending coefficients of \(P\) have exactly one sign change, so \(P\) has at most one positive real root. Exact evaluation gives \(P(3)=-3671332992<0\) and \(P(4)=42210962432>0\), establishing exactly one positive root \(r_*\in(3,4)\) and the claimed strict rank reversal. In particular,

\[
\rho_2(2)-\rho_4(2)=-\frac{34255931}{1147634834},\qquad
\rho_2(4)-\rho_4(4)=\frac{168843849728}{21235908109693}.
\]

**4. Sharpness.** Step 2 rules out every smaller graph and every four-site graph with fewer than six arcs. It also identifies the exceptional isomorphism class and the unique reversing pair among all four-site six-arc classes. Step 3 proves a real strict crossing for that pair. These establish all stated minimum and uniqueness quantifiers.

## Verification

The included `verify_symbolic.py` regenerates all loopless adjacency patterns, performs independent forward/reverse strong-connectivity checks, obtains canonical graph representatives by all vertex relabelings, solves exact symbolic absorption systems, checks the isomorphism count vector, verifies that exactly one of the \(113\) nontrivial comparisons has a positive shifted-polynomial sign variation, and checks the displayed rational identity and root bracket. The included `verify_numeric.py` separately builds and solves the fixation system with the Python standard library's exact `Fraction` arithmetic at seven rational fecundities. Both terminate with `PASS` when successful. Run them with Python 3.10 or newer, after installing the dependencies in `requirements.txt`, from the directory containing the scripts. These finite, exact calculations exhaust the explicitly bounded graph family; they say nothing about unbounded graph size.

## Relationship to prior work

Lieberman, Hauert, and Nowak (2005) define the directed replacement model and study random-location fixation, isothermal structures, and amplifiers and suppressors. Broom, Rychtář, and Stadler (2009, 2011) study vertex-specific fixation in connected **undirected** graphs; their order-eight census and fixed-graph approximation results do not classify directed four-site rank crossings. Zhang (2014) treats position dependence in special directed constructions (including graphs without strong connectivity), not a complete strongly connected six-arc census. Adlam and Nowak (2014) study aggregate fixation in random directed structures. Keller and Uğurlu (2024) investigate isothermal results with a different stationarity-based reproduction policy and explicit two-vertex examples, not this four-site class. These relationships support a distinct, finite directed-graph statement; they do not prove global priority over unexamined literature.

## Limitations

This is a theoretical constant-fitness birth–death process and a finite graph-classification result; empirical claims concerning evolutionary trajectories, ecological interventions, or evolving networks are not made. The four-vertex uniqueness statement does not extend to larger, weighted, looped, disconnected, or not-strongly-connected graphs; the six-arc minimum is conditional on four vertices. The numerical root approximation is supplementary to the algebraic uniqueness proof. Historical-priority risk remains for unlocated exact directed-graph fixation tables or earlier exhaustive symbolic treatments. No independent scientific validation is asserted.

## References

1. E. Lieberman, C. Hauert, M. A. Nowak, “Evolutionary dynamics on graphs,” *Nature* **433** (2005), 312–316. First published 2005-01-20. DOI: https://doi.org/10.1038/nature03204 . Open full-text scan: https://wiki.santafe.edu/images/5/58/Lieberman_nowak_sigmund_-_evolutionary_dynamics_on_graphs.pdf .
2. M. Broom, J. Rychtář, B. Stadler, “Evolutionary dynamics on small-order graphs,” *Journal of Interdisciplinary Mathematics* **12** (2009), 129–140. Public preprint: https://math-sites.uncg.edu/sites/math-bio-fellowship/preprints/BrRySt08.pdf .
3. M. Broom, J. Rychtář, B. T. Stadler, “Evolutionary dynamics on graphs—the effect of graph structure and initial placement on mutant spread,” *Journal of Statistical Theory and Practice* **5** (2011), 369–381. DOI: https://doi.org/10.1080/15598608.2011.10412035 . Author-hosted PDF: https://www.staff.city.ac.uk/mark.broom/Broom_et_al_JSTP2011.pdf .
4. P.-A. Zhang, “Fixation probabilities of evolutionary graphs based on the positions of new appearing mutants,” (2014). Full text: https://pdfs.semanticscholar.org/b20d/52d99defef343ca19683c17751c2c7580cec.pdf .
5. B. Adlam, M. A. Nowak, “Universality of fixation probabilities in randomly structured populations” (2014), arXiv:1407.2580. https://arxiv.org/abs/1407.2580 .
6. P. Keller, M. Uğurlu, “Fixation probability in Moran-like processes on graphs,” arXiv:2403.12598 (2024). https://arxiv.org/abs/2403.12598 .
