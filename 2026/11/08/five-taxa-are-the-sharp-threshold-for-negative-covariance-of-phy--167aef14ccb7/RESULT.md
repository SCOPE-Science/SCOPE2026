# Five taxa are the sharp threshold for negative covariance of phylogenetic diversity and mean pairwise distance

## Finding

Let \(T\) be a rooted ultrametric phylogenetic tree with \(n\) taxa, positive common root-to-leaf height \(H\), and nonnegative branch lengths. Select exactly \(k\) leaves uniformly without replacement, \(2\le k\le n\). The two statistics on this random leaf set \(S\) are rooted Faith phylogenetic diversity \(P(S)\), the sum of lengths of all edges lying on at least one path from the root to \(S\), and mean pairwise distance
\[
M(S)=\binom{k}{2}^{-1}\sum_{\{a,b\}\subseteq S}d_T(a,b).
\]
For every such tree with \(n\le4\) and every valid sample size, the covariance \(\operatorname{Cov}(P(S),M(S))\) is nonnegative. The threshold is sharp: a five-leaf tree with every edge strictly positive has \(\operatorname{Cov}(P(S),M(S))=-7/1000\) when \(k=4\). Its correlation is \(-3\sqrt5/7\).

For the five-leaf rooted full-binary shape \(((0,1),(2,(3,4)))\), let \(H\) denote common root-to-leaf height and \(x,x,y,z,z\) the respective pendant lengths. Assume \(0<x<H\) and \(0<z<y<H\). For uniform four-of-five sampling, the exact phase law is
\[
\operatorname{Cov}(P,M)=\frac{2}{75}\bigl(3Hx-Hy-2Hz+3x^2-5xy-4xz+3y^2+3z^2\bigr).
\]
Consequently, the strict negative-covariance region on this natural parameter domain is *exactly* where the polynomial in parentheses is negative. It is open and nonempty.

## Assumptions and scope

A rooted phylogenetic tree has labeled leaves, and its path lengths define the usual patristic leaf distance. Ultrametricity means every leaf is at distance \(H\) from the root. The sample is a uniformly random subset of **distinct** taxa, not independent draws with replacement, and \(P\) includes all branches in the minimal root-to-sample spanning subtree. Covariance is taken with respect to the uniform distribution on all \(\binom nk\) subsets; there is no population-versus-sample variance correction. Zero-length edges and multifurcations are allowed for the lower-bound assertion by contraction/continuity. The witness has all edges strictly positive.

The specific five-leaf family has internal root-to-clade depths \(H-x\) for clade \(\{0,1\}\), \(H-y\) for clade \(\{2,3,4\}\), and \(H-z\) for clade \(\{3,4\}\). All its edges are positive under the stated inequalities.

## Proof

**1. Two selected leaves.** If \(S=\{a,b\}\), let their most recent common ancestor be at root-depth \(h\). By ultrametricity, their pairwise distance is \(2(H-h)\) and their rooted phylogenetic diversity is \(2H-h\). Thus
\[
P(\{a,b\})=H+\tfrac12 M(\{a,b\}),\qquad
\operatorname{Cov}(P,M)=\tfrac12\operatorname{Var}(M)\ge0.
\]
For \(k=n\), both quantities are deterministic. These cases settle \(n\le3\), and for \(n=4\) leave only \(k=3\).

**2. Near-complete sampling identity.** For any tree with \(n\ge3\) and positive pendant lengths \(\ell_i\), when exactly leaf \(i\) is omitted,
\[
P(L\setminus\{i\})=P(L)-\ell_i,\qquad
M(L\setminus\{i\})=
\frac{D- s_i}{\binom{n-1}{2}},
\]
where \(D=\sum_{a<b}d_T(a,b)\) and \(s_i=\sum_{j\ne i}d_T(i,j)\). A pendant edge is the only edge whose descendant leaves all disappear on omitting one leaf; all other edges have at least two descendants. Therefore, for uniformly omitted \(i\),
\[
\operatorname{Cov}(P,M)
=\frac{\operatorname{Cov}_i(\ell_i,s_i)}{\binom{n-1}{2}}.
\]
The identity continues by continuity if some edges have length zero.

**3. Four-taxon lower bound.** Every rooted full-binary four-taxon topology is balanced or caterpillar, up to relabeling. In the balanced topology, the four pendant lengths are \((u,u,v,v)\), and the respective leaf distance sums are
\[
(2u+4H,\;2u+4H,\;2v+4H,\;2v+4H).
\]
Thus \(s_i=2\ell_i+4H\), so \(\operatorname{Cov}_i(\ell_i,s_i)=2\operatorname{Var}_i(\ell_i)\ge0\). In the caterpillar topology the pendant lengths are \((u,u,v,H)\) with \(0\le u\le v\le H\); their distance sums are
\[
(2u+2v+2H,\;2u+2v+2H,\;4v+2H,\;6H).
\]
Both sequences are similarly ordered, since the successive nontrivial sum differences are \(2(v-u)\) and \(4(H-v)\). The exact identity
\[
\operatorname{Cov}(X,Y)=\frac{1}{2n^2}\sum_{i,j}(X_i-X_j)(Y_i-Y_j)
\]
shows nonnegative covariance for similarly ordered sequences. Every nonbinary four-leaf rooted ultrametric tree is a zero-internal-edge limit of a binary topology, and covariance is continuous in lengths. This exhausts all \(n\le4\).

**4. Five-taxon phase law.** On \(((0,1),(2,(3,4)))\), the pendant length vector is \(\ell=(x,x,y,z,z)\) and the distance-sum vector is
\[
s=(2x+6H,\;2x+6H,\;4H+4y,\;4H+2y+2z,\;4H+2y+2z).
\]
Insert these vectors in the near-complete covariance identity with \(n=5\) and denominator \(\binom42=6\). Expansion yields
\[
\frac2{75}(3Hx-Hy-2Hz+3x^2-5xy-4xz+3y^2+3z^2).
\]
This is an identity, and hence its negativity is equivalent to the stated strict polynomial inequality.

**5. A strictly positive witness.** Take \(H=1\), \(x=1/10\), \(y=3/10\), and \(z=1/4\). The nonpendant positive branch lengths are \(9/10\), \(7/10\), \(1/20\). As one leaf is omitted uniformly, the five \((P,M)\) values (with multiplicities) are
\[
\bigl(51/20,77/60\bigr)\ (2\text{ times}),\quad
\bigl(47/20,29/20\bigr)\ (1\text{ time}),\quad
\bigl(12/5,22/15\bigr)\ (2\text{ times}).
\]
Their exact covariance is \(-7/1000\); their separate variances are \(7/1000\) and \(343/45000\), giving correlation \(-3\sqrt5/7\). The polynomial is strictly negative at an interior parameter point, hence by continuity negative covariance persists throughout a nonempty open neighborhood of strictly positive lengths. Combined with the four-taxon argument, five leaves are necessary and sufficient.

## Verification

The accompanying standalone `check.py` uses Python 3 standard-library exact rational arithmetic. It computes each subset's phylogenetic diversity by summing edge lengths with nonempty intersection with the subset, and its mean pairwise distance by summing edge lengths that separate each selected pair. It independently checks the five exact witness outcomes and correlation, evaluates the five-taxon polynomial against 120 other rational ultrametric choices, and tests 720 exact sampled distributions over both four-leaf topologies. Executed with `python check.py`, it reports `PASS`. The infinite quantifiers and minimality follow from the explicit arguments above; random numerical tests alone are not used as proof.

## Relationship to prior work

Nipperess and Matsen established exact expectation and variance of rooted phylogenetic diversity under rarefaction, including the fixed-sample framework. Mazel and collaborators found that phylogenetic diversity and mean pairwise distance can give discordant ecological summaries in simulated and empirical communities; that qualitative discordance is **prior work**, not claimed here. Tucker and collaborators reviewed families of phylogenetic metrics and their noninterchangeability. What is assessed here is the exact *covariance under a uniform fixed-size subset* for the same tree, the sharp four-versus-five-taxon boundary, and the explicit complete sign region for the specified five-leaf topology. The inspected articles do not state these exact results, but historical priority cannot be certified by a finite literature search.

## Limitations

The theorem requires an ultrametric tree and uniform fixed-size taxon sampling. It makes no claim for arbitrary non-ultrametric trees, abundance-weighted or replacement sampling, or relationships under phylogeny reconstruction error. The phase law is complete only for the explicitly defined five-leaf topology and does not classify all larger trees or other five-leaf sampling sizes. The conclusion concerns an ensemble covariance, not a causal relationship between metrics on individual communities. Independent mathematical audit and historical-priority assessment remain outstanding.

## References

1. Nipperess, D. A., and Matsen IV, F. A. *The mean and variance of phylogenetic diversity under rarefaction*. First publicly submitted 2012-08-31. https://arxiv.org/abs/1208.6552
2. Mazel, F., Davies, T. J., Gallien, L., Renaud, J., Groussin, M., Münkemüller, T., and Thuiller, W. *Influence of tree shape and evolutionary time-scale on phylogenetic diversity metrics*. Ecography 39, 913–920 (2016), first online 2015. https://doi.org/10.1111/ecog.01694
3. Tucker, C. M. et al. *A guide to phylogenetic metrics for conservation, community ecology and macroecology*. Biological Reviews 92, 698–715 (2017), first online 2016. https://doi.org/10.1111/brv.12252
