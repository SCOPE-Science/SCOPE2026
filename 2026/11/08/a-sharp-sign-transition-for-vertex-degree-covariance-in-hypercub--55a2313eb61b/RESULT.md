# A sharp sign transition for vertex-degree covariance in hypercube spanning trees

## Finding

Let \(Q_d\) be the graph on \(\{0,1\}^d\) joining binary strings differing in one coordinate, \(d\ge1\), and select uniformly from its spanning trees. Write \(D_u\) for the degree of vertex \(u\) in the selected tree and \(t\) for the Hamming distance between distinct vertices \(u\) and \(v\). The exact degree covariance depends only on \(d,t\), and has the following complete sign classification:

- \(\operatorname{Cov}(D_u,D_v)=0\) when \(d=1\) or \((d,t)=(2,1)\);
- \(\operatorname{Cov}(D_u,D_v)>0\) when \(d\ge3\) and \(t=1\);
- \(\operatorname{Cov}(D_u,D_v)<0\) whenever \(2\le t\le d\).

More sharply, put \(N=2^d\). For \(d\ge3\), adjacent vertices have
\[
\operatorname{Cov}(D_u,D_v)=
\frac{(N-2d)\bigl(N(d-4)+2d+4\bigr)}{N^2d(d-1)(d-2)}.
\]
The first positive example occurs in \(Q_3\): adjacent vertices have covariance \(1/96\), whereas distances two and three give respectively \(-5/32\) and \(-1/32\). Although different edges of a uniform spanning tree are negatively correlated, two *overlapping collections* of incident edges can therefore have positive aggregate degree covariance.

## Assumptions and scope

All edges of \(Q_d\) have unit conductance; each spanning tree is equiprobable. Vertex degrees are unweighted. Only distinct vertices are considered. For integers \(0\le j<d\), define
\[
h_j=\frac{N-\sum_{q=0}^j\binom dq}{N\binom dj(d-j)},
\qquad p=2h_0=\frac{2(N-1)}{dN}.
\]
Every \(h_j\) is strictly positive. For \(1\le t\le d\), put
\[
\begin{aligned}
\Xi_{d,t}={}&4t h_{t-1}^2+4(d-t)h_t^2
+t(t-1)(h_{t-2}-h_{t-1})^2\\
&+2t(d-t)(h_t-h_{t-1})^2
+(d-t)(d-t-1)(h_t-h_{t+1})^2.
\end{aligned}
\]
A term with zero integer multiplier is **omitted before evaluating any subscript**; consequently this formula is meaningful also at \(t=1\), \(t=d\), and \(d=1\). The complete exact covariance is
\[
\operatorname{Cov}(D_u,D_v)=p\,\mathbf1_{\{t=1\}}-\Xi_{d,t}.
\]

## Proof

**1. Hypercube Green-function differences.** Let \(L\) be the combinatorial Laplacian and \(G=L^+\) its Moore–Penrose inverse. The function \(x\mapsto G_{0,x}\) depends only on the Hamming weight \(|x|\); denote its value at weight \(j\) by \(g_j\). Because \(LG_{\cdot,0}=\delta_0-N^{-1}\mathbf1\), summing this equation over the Hamming ball of radius \(j\) gives the outward flux \(1-N^{-1}\sum_{q=0}^j\binom dq\). The ball boundary has \(\binom dj(d-j)\) edges and every crossing has potential difference \(g_j-g_{j+1}\). Thus
\[
g_j-g_{j+1}=h_j,\qquad 0\le j<d.
\]
In particular, the effective resistance between neighboring vertices, hence the marginal spanning-tree edge inclusion probability, is \(p=2(g_0-g_1)=2h_0\).

**2. Transfer-current covariance.** Give an arbitrary orientation to every cube edge, write \(b_e\) for its signed incidence vector, and set \(K(e,f)=b_e^{\mathsf T}Gb_f\). The standard transfer-current determinantal identity gives, for distinct edges, \(\operatorname{Cov}(\mathbf1_{e\in T},\mathbf1_{f\in T})=-K(e,f)^2\), and for a single edge it gives \(\operatorname{Var}(\mathbf1_{e\in T})=p-p^2\). Summing the edge indicators over the stars at \(u\) and \(v\) therefore yields
\[
\operatorname{Cov}(D_u,D_v)=p\,\mathbf1_{\{u\sim v\}}-
\sum_{e\ni u}\sum_{f\ni v}K(e,f)^2.
\]
The extra \(p\) occurs precisely when the stars share their unique connecting edge, since its negative squared diagonal contribution must be replaced by \(p-p^2\).

**3. Exact Hamming-distance kernel.** By translation and coordinate-permutation symmetry take \(u=0\) and \(v=x\), \(|x|=t\). Index the star at each vertex by a coordinate \(i\) or \(j\). Apart from an irrelevant orientation sign, its transfer-current entry is
\[
K_{ij}=g_t-g_{|x\oplus e_j|}-g_{|x\oplus e_i|}+g_{|x\oplus e_i\oplus e_j|}.
\]
There are five disjoint types of ordered coordinate pairs: \(i=j\) inside the support of \(x\) (count \(t\), squared value \(4h_{t-1}^2\)); \(i=j\) outside the support (count \(d-t\), squared value \(4h_t^2\)); distinct \(i,j\) both inside (count \(t(t-1)\), squared value \((h_{t-2}-h_{t-1})^2\)); one inside and one outside (count \(2t(d-t)\), squared value \((h_t-h_{t-1})^2\)); distinct coordinates both outside (count \((d-t)(d-t-1)\), squared value \((h_t-h_{t+1})^2\)). These exhaust all \(d^2\) pairs and give \(\Xi_{d,t}\) exactly.

**4. Sharp sign.** If \(2\le t\le d\), the sum \(\Xi_{d,t}\) contains the strictly positive term \(4t h_{t-1}^2\). Since the stars do not share an edge, the covariance is strictly negative. For \(t=1\), direct substitution gives \(0\) at \(d=1,2\). For \(d\ge3\), using \(h_0=(N-1)/(dN)\), \(h_1=(h_0-1/N)/(d-1)\), and \(h_2=(2h_1-1/N)/(d-2)\), the formula reduces by elementary rational expansion to
\[
p-\Xi_{d,1}=\frac{(N-2d)(N(d-4)+2d+4)}{N^2d(d-1)(d-2)}.
\]
For \(d=3\), its numerator factors are \(2\) and \(2\); for \(d\ge4\), \(N>2d\) and \(N(d-4)+2d+4>0\). Hence it is strictly positive for every \(d\ge3\). The cases \(d=1\) and \(d=2\) follow directly from the exact kernel, completing the proof.

## Verification

The included standalone `verify_hypercube.py` uses only Python 3 standard-library exact arithmetic. Run `python3 verify_hypercube.py`. It enumerates all spanning trees for \(Q_1,Q_2,Q_3\) (respectively 1, 4, 384 trees), computes their exact degree covariances, and compares them with the formulas. Separately, for every \(2\le d\le8\) and every \(1\le t\le d\), it constructs the pseudoinverse Green function by the Walsh-character spectral formula and checks exact agreement of the direct transfer-current sum, binomial-flux formula and adjacent rational factorization, plus the predicted signs. There are 105 recorded exact assertions in this latter loop. Finite checks supplement but do not replace the preceding all-dimensional proof.

## Relationship to prior work

Bernardi [1] studies hypercube spanning-tree enumerators and independence of oriented edge spins, not the vertex-pair degree-covariance sign diagram. Kassel and Wu [2] supply transfer-current/Green-function machinery on general graphs and scaling limits; this existing determinantal theorem is explicitly used, not claimed as new. Rapoport [3] supplies general-graph joint degree distributions, encompassing the abstract observable, but does not evaluate the stated finite binary-hypercube sign transition. The specific contribution here is the evaluated Hamming-distance covariance and the exceptional positive adjacent regime, not the general determinantal formula.

## Limitations

The result concerns finite **binary hypercubes** with unit edge weights, not every Cartesian product or the infinite cubic lattice. It gives second moments, not a joint degree probability law, concentration inequality or limit theorem. A general-graph determinantal formula underlies the computation, and historical implicit coverage in further spanning-tree degree literature remains possible; the statement should not be represented as independently validated.

## References

[1] O. Bernardi, *On the spanning trees of the hypercube and other products of graphs*, first public arXiv version 2012-07-04, https://arxiv.org/abs/1207.0896 .

[2] A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, first public arXiv version 2013-12-10, https://arxiv.org/abs/1312.2946 .

[3] A. Rapoport, *Correlations in Uniform Spanning Trees: a Fermionic Approach*, preprint 2023-12-22, https://arxiv.org/abs/2312.14992 .
