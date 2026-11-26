# Complete Gaussian vertex-angle law and rare-collision condensation for split graphical zonotopes

## Finding

For integers \(r\ge2\) and \(s\ge2\), let \(G=K_r\vee\overline{K_s}\) be the graph obtained by connecting every vertex of a labeled \(r\)-clique to every vertex of a labeled independent \(s\)-set. Its graphical zonotope has exactly \(r!(r+1)^s\) vertices. These are in bijection with a clique order \(\pi\) and a choice of one of the \(r+1\) gaps around that order for each independent vertex.

Let \(m=(m_0,\ldots,m_r)\) be the gap occupancies, with \(m_j\ge0\) and \(\sum_jm_j=s\). The normalized spherical angle of the vertex normal cone is

\[
\alpha(\pi,m)=\frac{\prod_{j=0}^r m_j!}{(r+s)!}.
\]

For every integer \(t\ge2\), the probability of a \(t\)-direction collision (all \(t\) independent isotropic objective directions expose the same zonotope vertex) is

\[
C_t(r,s)=\frac{r!s!}{((r+s)!)^t}
 \sum_{\substack{m_0+\cdots+m_r=s\\m_j\ge0}}
 \prod_{j=0}^r (m_j!)^{t-1}.
\]

For each fixed \(r\ge2\) and integer \(t\ge2\), as \(s\to\infty\),

\[
C_t(r,s)\sim (r+1)r!s^{-rt}.
\]

Three exact or limiting gap-profile sampling laws differ: with one random objective, \(m\) is uniform on all weak compositions of \(s\) into \(r+1\) parts, so \(m/s\) converges to the uniform Dirichlet simplex law; with a uniformly chosen polytope vertex, \(m\) is multinomial with equal cell probabilities and \(m/s\) converges to the equal-coordinate point; conditional on a \(t\)-direction collision, \(m\) is supported asymptotically on the \(r+1\) corners \(s e_j\), equally likely. In particular, the \(r!(r+1)\) corner vertices comprise an exponentially vanishing proportion of all vertices but dominate collision events.

When \(r=2\), the graph differs from \(K_{2,s}\) by exactly one edge. Its two-direction collision probability is asymptotic to \(6s^{-4}\), whereas that of \(K_{2,s}\) is asymptotic to \(10s^{-4}\). The sharp ratio is \(3/5\).

## Assumptions and scope

All graphs are simple, undirected, and labeled. Define the canonical Euclidean graphical zonotope in \(\mathbb R^{r+s}\) by

\[
Z_G=\sum_{\{u,v\}\in E(G)}[e_u,e_v].
\]

Translation does not affect its normal fan or angular measurements. Its affine span has direction subspace \(\{x:\sum x_i=0\}\), with the inherited Euclidean metric. An isotropic direction is Haar-uniform on the unit sphere of this subspace, or equivalently the normalized projection of a standard Gaussian vector; ties have measure zero. A normal-cone angle here means the probability that such a direction uniquely exposes its vertex. The permutation-model argument works because independent Gaussian coordinates have all strict orders equally likely.

For a fixed increasing order of clique objective coordinates, gap \(0\) is below the first clique coordinate, gap \(j\) lies between clique positions \(j\) and \(j+1\), and gap \(r\) is above the last. Individual independent-set labels have independently specifiable gap indices; no order is imposed inside one gap.

## Proof

**1. Vertex classification.** The graphical zonotope's normal fan is the graphical arrangement, with chambers in bijection with acyclic orientations. Each clique edge forces a total order \(\pi\) of the clique vertices. Every independent vertex is adjacent to the whole clique and to no other independent vertex, so its edge signs select exactly one gap. Conversely, any clique order and any gap assignment are realized by strictly ordered real coordinates; each gives a different orientation. Consequently there are \(r!(r+1)^s\) vertices.

**2. Angle formula.** Fix \(\pi\) and an assignment of the \(s\) independent labels to gaps with occupancy vector \(m\). Of the \((r+s)!\) strict total orders of all coordinate values, precisely \(\prod_jm_j!\) induce these edge orientations: the clique order and the positions of the gap blocks are fixed, while labels inside a gap may be permuted. Exchangeability of Gaussian coordinates proves the angle formula. Summing over assignments yields

\[
\sum_{\pi}\sum_{m}
\frac{s!}{\prod_jm_j!}\frac{\prod_jm_j!}{(r+s)!}
=\frac{r!s!}{(r+s)!}\binom{s+r}{r}=1.
\]

**3. All collision moments.** A particular occupancy vector \(m\) permits \(r!s!/\prod_jm_j!\) orientations. Sum the \(t\)-th powers of their angles to obtain the displayed exact formula for \(C_t\). The conditional occupancy law given a collision is therefore proportional to \(\prod_j(m_j!)^{t-1}\).

**4. Factorial-composition bound.** For fixed integers \(k\ge1\) and \(a\ge1\), put

\[
S_{k,a}(s)=\sum_{m_1+\cdots+m_k=s}\prod_i (m_i!)^a.
\]

We prove \(S_{k,a}(s)=k(s!)^a(1+O_{k,a}(s^{-1}))\) as \(s\to\infty\). For \(k=1\) this is exact. The convolution identity is

\[
S_{k+1,a}(s)=S_{k,a}(s)+(s!)^a+
\sum_{j=1}^{s-1}(j!)^a S_{k,a}(s-j).
\]

Induction gives a uniform finite bound \(S_{k,a}(h)\le A_{k,a}(h!)^a\) for all \(h\ge0\). Dividing the interior sum by \((s!)^a\), its size is at most \(A_{k,a}\sum_{j=1}^{s-1}\binom{s}{j}^{-a}\). For \(s\ge4\), the two endpoint terms contribute \(2/s\), and each of the other \(s-3\) terms is bounded by \(2/(s(s-1))\), so the whole sum is at most \(4/s\). This also propagates the uniform bound, and yields the asserted asymptotic by induction. Apply it with \(k=r+1\), \(a=t-1\), and \((r+s)!/s!\sim s^r\) to obtain \(C_t(r,s)\sim(r+1)r!s^{-rt}\).

**5. The three limiting sampling regimes.** Summing angles over assignments with one fixed \(m\) gives \(r!s!/(r+s)!=\binom{s+r}{r}^{-1}\), independent of \(m\); hence Gaussian-exposed gap counts are exactly uniform weak compositions. Their scaled lattice points converge by Riemann sums to the uniform Dirichlet law. Uniform vertex sampling instead makes the \(s\) independent labels choose gaps independently and uniformly, giving the stated multinomial law and concentration. Conditional on collision, the weight of all \(r+1\) extreme occupancy vectors is \((r+1)(s!)^{t-1}\), asymptotically the entire sum by Step 4. Thus the collision-conditioned occupancy measure concentrates equally at the corners.

**6. One-edge sensitivity.** For \(r=2\), deleting the edge joining the clique vertices produces \(K_{2,s}\). Orientation pairs differing only in the order of the two clique vertices merge precisely when no independent vertex lies between them, i.e. \(m_1=0\). Their equal angle contributions are summed into one cone. Each merge replaces two squared probabilities by their combined square, increasing the two-direction collision probability by twice their product. Explicitly,

\[
C_2(K_{2,s})-C_2(K_2\vee\overline{K_s})
=\frac{2s!}{((s+2)!)^2}\sum_{j=0}^s j!(s-j)!.
\]

The two endpoints of this last sum contribute \(2s!\), and Step 4 (at \(k=2,a=1\)) shows the remainder is \(O(s!/s)\). The gap is therefore asymptotic to \(4s^{-4}\); the split-graph collision is asymptotic to \(6s^{-4}\), giving \(10s^{-4}\) for the bipartite graph and a ratio of \(3/5\).

## Verification

The attached `check_angles.py` constructs normal-cone orientations directly from all \((r+s)!\) strict coordinate orders, without using the gap-angle formula. It checks the complete orientation histogram, the vertex count, the exact \(t=2,3,4\) collision probabilities and the single-edge deletion identity for ten split parameters with \(4\le r+s\le7\). It prints `SPLIT_ANGULAR_CONE_EXACT_PASS cases=10` when all assertions hold. The all-parameter statements and limits are proved above; finite checks are supporting tests, not an infinite certificate.

## Relationship to prior work

Padrol, Pilaud and Poullot establish the graphical-zonotope normal fan and its orientation correspondence, alongside deformation-cone results; those structural facts are prior work. Carballosa, Khera and Reyes encode and count acyclic orientations for complete multipartite graphs, a family containing the complete split graphs here; their general labeled-orientation counts are likewise prior. The present contribution evaluates every Euclidean spherical vertex-angle and its collision moments, then establishes their asymptotic concentration and the sharp effect of adding the hub edge to \(K_{2,s}\). Earlier results on angular collisions of complete-bipartite graphical zonotopes concern a different normal fan and do not give these split-graph formulas by changing a parameter alone.

## Limitations

The formulas assume the canonical ordinary Euclidean embedding, equal unit edge generators, independent isotropic objective directions and labeled vertices. Fixed-\(r\) asymptotics do not cover regimes where the clique size grows with \(s\). Historical originality is conditional on the publicly checked sources; an unindexed equivalent derivation is possible. No independent mathematical audit is claimed.

## References

1. Arnau Padrol, Vincent Pilaud and Germain Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, first posted 24 November 2021, especially Section 1.3 and Proposition 1.3. https://arxiv.org/abs/2111.12422
2. Walter Carballosa, Jessica Khera and Francisco Reyes, *Encoding and Enumerating Acyclic Orientations of Graphs*, arXiv:2303.09021, first posted 16 March 2023, especially Section 3. https://arxiv.org/abs/2303.09021
3. *Angular collision laws for complete-bipartite graphical zonotopes*, previous published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-angular-collision-laws-for-complete-bipartite-graphical-zonotope--d8c7504cb6f5
