# A binomial vacancy law for dimer jamming with a dilute third sublattice

## Finding

Irreversible random sequential adsorption of dimers on the complete tripartite graph \(K_{n,n,r}\) has a universal, nonvanishing finite-defect limit as the two principal parts grow. For integers \(n,r\ge 1\), let \(U_{n,r}\) be the number of unoccupied vertices after all edges have been offered in uniformly random order, each dimer being retained if both its endpoints are then free. Let \(B_r\sim\operatorname{Bin}(r,1/2)\). For every integer \(1\le h\le n\),

\[
 d_{\mathrm{TV}}\bigl(\mathcal L(U_{n,r}),\mathcal L(|2B_r-r|)\bigr)
 \le \frac{r(h+r)}{n+r}+\frac{r^2}{4h}.
\]

Consequently, for each fixed \(r\), \(U_{n,r}\) converges in total variation to the absolute position after \(r\) steps of a simple symmetric random walk. In particular, when \(r=2\), a graph admitting a perfect matching jams with exactly two uncovered sites with probability tending to \(1/2\), and ends perfectly covered with probability tending to \(1/2\). More generally, if \(r=r(n)\to\infty\) with \(r=o(n^{1/3})\), then

\[
 \frac{U_{n,r}}{\sqrt r}\ \Longrightarrow\ |Z|,\qquad Z\sim N(0,1).
\]

This is a single dilute-component vacancy-law result, including its finite-size estimate and scaling consequence.

## Assumptions and scope

The vertex set consists of three disjoint, labeled parts \(A,B,C\) of sizes \(n,n,r\). Every pair of vertices in distinct parts is connected and there are no edges within a part. All edges are proposed in a uniformly random permutation; a proposal is accepted precisely when its endpoints have not been covered by earlier accepted edges. Equivalently, eligible edges have independent rate-one exponential proposal clocks. No desorption or rearrangement occurs. The result is for every \(n,r\ge1\); the Gaussian conclusion assumes \(r\to\infty\) and \(r^3/n\to0\), not merely \(r=o(n)\). Total variation is \(d_{\mathrm{TV}}(P,Q)=\frac12\sum_k|P(k)-Q(k)|\).

## Proof

**1. Exact embedded chain.** At any stage let \((a,b,c)\) be the counts of free vertices in the three parts. The only eligible edges have respective multiplicities \(ab,ac,bc\). Conditional on an accepted event, these give the probabilities of the transitions

\[
 (a,b,c)\mapsto(a-1,b-1,c),\quad(a-1,b,c-1),\quad(a,b-1,c-1)
\]

with weights \(ab,ac,bc\), divided by \(ab+ac+bc\). The equivalence to random edge ordering follows by assigning independent identically distributed continuous arrival times to all edges. Because an edge never becomes eligible after an endpoint is covered, the first eligible arrival among remaining edges is uniform. This embedded chain continues until at most one part contains free vertices.

**2. A dilute vertex is unlikely to survive until depletion.** Put \(s=\min(a,b)\). Initially \(s=n\); each accepted edge decreases \(s\) by either zero or one. Fix a labeled vertex \(v\in C\), and suppose it is still free while \(s\ge1\). Its conditional probability of being chosen on the next accepted edge is

\[
 \frac{a+b}{ab+c(a+b)}
 =\frac{1}{ab/(a+b)+c}
 \ge\frac{1}{s+r},
\]

because \(ab/(a+b)\le\min(a,b)=s\) and \(c\le r\). On the event that \(v\) remains free until the first time \(s<h\), the process must visit each level \(s=n,n-1,\ldots,h\). At the first accepted edge of each level, conditional survival is at most \(1-1/(s+r)\). Iterated conditional expectation therefore gives

\[
 \Pr\{v\text{ is still free at first }s<h\}
 \le \prod_{s=h}^{n}\left(1-\frac1{s+r}\right)
 =\frac{h+r-1}{n+r}\le\frac{h+r}{n+r}.
\]

The first passage exists almost surely: if \(s\ge h\), eligible edges exist. By a union bound over all \(r\) vertices of \(C\), the probability that any of them survives to this passage is at most \(r(h+r)/(n+r)\).

**3. Coupling of all dilute matching choices to fair coins.** Throughout the process, \(|a-b|\le r\): edges between \(A,B\) reduce both counts equally, and each edge involving \(C\) changes their difference by one. At an accepted edge involving \(C\), conditional on the counts immediately before it, the chance that its other endpoint lies in \(A\) is \(a/(a+b)\), since the eligible \(A\)-\(C\) and \(B\)-\(C\) edges have rates \(ac\) and \(bc\). While \(s\ge h\),

\[
 \left|\frac a{a+b}-\frac12\right|
 =\frac{|a-b|}{2(a+b)}\le\frac r{4h}.
\]

Using independent uniforms for the successive choices of an endpoint by the \(r\) vertices in \(C\), couple these choices to \(r\) independent fair coins. Until \(s<h\), the chance of at least one disagreement is at most \(r^2/(4h)\). We may complete any unused coins arbitrarily if some \(C\) vertex survives beyond that threshold.

**4. Identification of terminal vacancies.** Outside the union of these two failure events, all \(r\) vertices of \(C\) were matched before \(s<h\), and their choices agreed with the fair coins. If \(X\) of them matched vertices of \(A\), the free-count difference is \(a-b=r-2X\) after the last \(C\) match. Only \(A\)-\(B\) dimers can then be accepted; they consume all vertices of the smaller remaining part, leaving \(|r-2X|\) free vertices. Hence \(U_{n,r}=|2X-r|\) on the good event, where the coupled \(X\) is binomial \(\operatorname{Bin}(r,1/2)\). The coupling inequality gives the stated total-variation estimate.

**5. Limits.** For fixed \(r\), set \(h=\lceil\sqrt n\rceil\) (capped at \(n\)); the bound tends to zero. For \(r=o(n^{1/3})\), choose \(h=\min(n,\lceil\sqrt{nr}\rceil)\), giving a bound of order \(r^{3/2}/\sqrt n+r^2/n\), which tends to zero. For \(r\to\infty\), the classical binomial central limit theorem and continuity of the absolute-value map yield \(|2B_r-r|/\sqrt r\Rightarrow|Z|\); the total-variation approximation transfers this law to \(U_{n,r}\). For fixed \(r\), the limiting probabilities are explicitly

\[
 \Pr\{U_{n,r}=u\}\longrightarrow 2^{-r}\sum_{k:\,|2k-r|=u}\binom rk.
\]

## Verification

The accompanying `verify_model.py` independently implements a recursive count-based Markov chain and a labeled-vertex state recursion, as well as exhaustive edge-permutation enumeration on three small instances. It checks equality of rational terminal distributions, support and normalization, and the finite-size total-variation inequality. The executed verification passed 16 labeled-vs-count distribution comparisons, 40,446 exhaustive edge orders, and 855 rational bound comparisons. These finite computations test normalization and implementation; the all-parameter and asymptotic claims follow from the analytic proof above.

## Relationship to prior work

Evans (1993) reviews random sequential adsorption and kinetic jamming on lattices and surfaces, establishing the broad physical framework. Dyer and Frieze (1991) study random-edge greedy matching on arbitrary fixed graphs, emphasizing worst-case behavior and sparse classes rather than a limiting vacancy law on a dense tripartite family. Turban (2019) analyzes adsorption/covering times for fully connected one-type substrates; its complete-graph process lacks the three-part forbidden-edge geometry that creates the finite vacancy law here. Arnosti (2021) analyzes several greedy matching algorithms on bipartite random graphs; that setup has two parts and random edges, rather than a deterministic complete tripartite graph with a dilute third part. Published mathematical-result and literature searches identified related studies but no equivalent binomial/half-normal jamming theorem with this quantitative coupling bound; absence from searches alone does not prove historical priority.

## Limitations

This theorem concerns complete tripartite graph substrates with uniform edge proposal rates, not Euclidean lattice embeddings, arbitrary adsorption networks, or nonuniform rates. The explicit total-variation estimate is not claimed optimal. The half-normal regime is proved only for \(r=o(n^{1/3})\). The results concern the final jammed configuration, not adsorption time or kinetics. Older general matching literature was not available in full in every case; equivalently stated prior coverage cannot be ruled out categorically.

## References

- J. W. Evans, "Random and cooperative sequential adsorption," *Reviews of Modern Physics* **65** (1993), 1281–1329, DOI:10.1103/RevModPhys.65.1281. Public article date: 1993-10-01.
- M. Dyer and A. Frieze, "Randomized greedy matching," *Random Structures & Algorithms* **2** (1991), 29–45, DOI:10.1002/rsa.3240020104.
- L. Turban, "Random sequential adsorption of k-mers on the fully-connected lattice: probability distributions of the covering time and extreme value statistics," 2019 preprint, arXiv:1908.00940.
- N. Arnosti, "Greedy Matching in Bipartite Random Graphs," 2021 open manuscript, https://nickarnosti.com/ResearchPapers/Arnosti_GreedyMatching.pdf; published in *Stochastic Systems* **12** (2022), 133–150.
