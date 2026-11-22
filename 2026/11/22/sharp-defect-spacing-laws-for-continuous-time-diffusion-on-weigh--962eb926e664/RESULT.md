# Sharp defect-spacing laws for continuous-time diffusion on weighted rings

## Finding

Let \(n\ge4\) and \(2\le k\le n-2\) be integers. On the cyclic nearest-neighbor lattice \(C_n\), assign resistance \(r=1+\delta>0\), with \(\delta\ne0\), to exactly \(k\) edges and resistance \(1\) to the others. The continuous-time nearest-neighbor process jumps across an edge at its reciprocal resistance. Write \(x_1<\cdots<x_k\) for the exceptional edge labels modulo \(n\), put \(g=\gcd(n,k)\), and define
\[
S(x)=\sum_{1\le i<j\le k}(x_j-x_i)\bigl(n-x_j+x_i\bigr).
\]
Its Kirchhoff index \(K=\sum_{0\le u<v<n} R_{\mathrm{eff}}(u,v)\), or equivalently \(n\) times its continuous-time Kemeny mean hitting time, obeys the exact law
\[
K(x)=\frac{n^2(n^2-1)/12+\delta kn(n^2-1)/6+\delta^2 S(x)}{n+k\delta}.
\]
The **unique minimizing geometry**, up to cyclic rotation, is a block of \(k\) consecutive exceptional edges. The **maximizing geometries** are exactly the circularly balanced configurations: if \(a_1,\ldots,a_k\) are the positive consecutive spacings of exceptional edge labels with total \(n\), then for every \(1\le\ell\le k-1\), every cyclic sum of \(\ell\) consecutive spacings is either \(\lfloor\ell n/k\rfloor\) or \(\lceil\ell n/k\rceil\). Such configurations exist, e.g. \(x_j=\lfloor jn/k\rfloor\), \(j=0,\ldots,k-1\).

The sharp values of the arrangement-dependent term are
\[
S_{\min}=\frac{k(k^2-1)(2n-k)}{12},\qquad
S_{\max}=\frac{n^2(k^2-1)-k^2+g^2}{12}.
\]
Consequently the *same extremizing arrangements* govern both faster exceptional bonds (\(-1<\delta<0\)) and slower ones (\(\delta>0\)); the sharp Kirchhoff-index contrast is
\[
K_{\max}-K_{\min}
=\frac{\delta^2\bigl[(k^2-1)(n-k)^2-k^2+g^2\bigr]}{12(n+k\delta)}>0.
\]
There is no first-order sensitivity to exceptional-bond placement as \(\delta\to0\): placement effects begin at the quadratic order.

## Assumptions and scope

Vertices are \(0,1,\ldots,n-1\), with undirected edge \(e_i=\{i,i+1\bmod n\}\). Write its resistance as \(r_i=1+\delta\mathbf 1_{\{i\in X\}}\) for a fixed \(k\)-element exceptional set \(X\). All resistances are positive. The Markov generator is
\[
(Lf)(v)=\frac{f(v+1)-f(v)}{r_v}+\frac{f(v-1)-f(v)}{r_{v-1}}.
\]
It is irreducible and reversible with uniform stationary measure. The Kemeny time is defined by \(\mathcal K=n^{-1}\sum_{y=0}^{n-1}\mathbb E_x[\tau_y]\), independent of \(x\), where the first-hitting time is zero if \(x=y\). The weighted graph has combinatorial Laplacian \(-L\). The standard resistance--spectral identity yields \(\mathcal K=K/n\). The optimization fixes \(n\), \(k\), and \(\delta\), changing only the placement of the selected edges.

## Proof

**1. Edge-pair expansion.** Put \(R=\sum_i r_i\). Between any two vertices, let \(A\) be the total resistance on one of the two connecting arcs. The two arcs are in parallel, hence their effective resistance is \(A(R-A)/R\). For a pair of distinct edges \(e_i,e_j\) separated by \(d\) edge positions, there are precisely \(d(n-d)\) unordered vertex pairs whose connecting arcs place those two edges on opposite sides. Expanding \(A(R-A)\) and summing over vertex pairs therefore gives the exact general weighted-cycle identity
\[
K=\frac1R\sum_{0\le i<j<n}(j-i)(n-j+i)r_i r_j.
\]
The unit-weight sum is \(n^2(n^2-1)/12\). For a fixed edge, its interaction with every other edge sums to \(n(n^2-1)/6\). Substituting \(r_i=1+\delta\mathbf1_{\{i\in X\}}\), \(R=n+k\delta\), produces the stated exact \(K(x)\). In particular, placement enters with strictly positive coefficient \(\delta^2/(n+k\delta)\).

**2. Cyclic-spacing expression.** Let \(a_i=x_{i+1}-x_i\) for \(i<k\) and \(a_k=n+x_1-x_k\); each \(a_i\ge1\) and \(\sum_i a_i=n\). Put \(f(t)=t(n-t)\) and \(A_{i,\ell}=a_i+\cdots+a_{i+\ell-1}\) cyclically. Each unordered pair of distinct exceptional edges is counted twice by all directed arcs, so
\[
S=\frac12\sum_{\ell=1}^{k-1}\sum_{i=1}^k f(A_{i,\ell}).
\]
On the real spacing simplex \(a_i\ge1\), \(\sum_i a_i=n\), this function is strictly concave: each summand is concave and the \(\ell=1\) block contributes \(-\tfrac12\sum_i a_i^2\). Thus its minimum occurs only at a vertex of the simplex, i.e. the cyclic permutations of \((n-k+1,1,\ldots,1)\). A direct evaluation of these contiguous placements gives
\[
S_{\min}=\sum_{d=1}^{k-1}(k-d)d(n-d)
=\frac{k(k^2-1)(2n-k)}{12}.
\]
Strict concavity excludes every nonvertex minimizer.

**3. Simultaneous integer-balancing upper bound.** Fix \(1\le\ell\le k-1\). The \(k\) integers \(A_{i,\ell}\) sum to \(\ell n\). Write \(\ell n=kq_\ell+s_\ell\) with \(0\le s_\ell<k\). Since \(f(t)=t(n-t)\), a pairwise smoothing step replacing \((u,v)\) by \((u+1,v-1)\) when \(v\ge u+2\) strictly increases \(f(u)+f(v)\). Hence the sum at each \(\ell\) is uniquely maximized among integer vectors of this sum by the \(k-s_\ell\) values \(q_\ell\) and \(s_\ell\) values \(q_\ell+1\). Their exact sum is
\[
\sum_i f(A_{i,\ell})\le\frac{n^2\ell(k-\ell)}k-\frac{s_\ell(k-s_\ell)}k,
\]
with equality precisely when all length-\(\ell\) block sums differ by at most one. A mechanical placement \(x_j=\lfloor jn/k\rfloor\) (indices \(0\le j<k\)) realizes equality simultaneously for all \(\ell\). Summing the sharp upper bounds, and using
\[
\sum_{\ell=1}^{k-1}\ell(k-\ell)=\frac{k(k^2-1)}6,\qquad
\sum_{\ell=1}^{k-1}s_\ell(k-s_\ell)=\frac{k(k^2-g^2)}6,
\]
gives
\[
S_{\max}=\frac{n^2(k^2-1)-k^2+g^2}{12}.
\]
All summands have individually sharp upper bounds. Therefore equality in the total occurs exactly for placements satisfying the circular block-balancing criterion for *every* \(\ell\). The difference of sharp values simplifies to the advertised positive factor because \(k<n\) and at least two unselected edges exist.

**4. Transport interpretation.** For the symmetric continuous-time generator \(L\), its nonzero eigenvalues \(\lambda_1,\ldots,\lambda_{n-1}\) are positive for \(-L\). The usual pseudoinverse identities give \(K=n\sum_j\lambda_j^{-1}\) and the stationary-target mean first-passage time \(\mathcal K=\sum_j\lambda_j^{-1}\). Thus the resistance theorem is precisely an exact optimal arrangement result for long-time diffusive hitting behavior. No assertion about spectral-gap optimizers is made.

## Verification

`cyclic_resistance_verify.py` independently evaluates effective resistances by parallel-arc reduction and compares them with the claimed closed form for every exceptional-edge subset for \(4\le n\le12\), \(2\le k\le n-2\), at resistance contrasts \(r=1/2\) and \(r=3\). Exactly 16,028 rational cases, including all minimizer and maximizer equality criteria, passed. A separate grounded-Laplacian inverse check using exact rational SymPy matrices confirmed 30 additional selected cases for \(4\le n\le8\). The unrestricted-in-\(n\) proof is the algebraic argument above, not an inference from finite enumeration.

For a simple example, \(n=12\), \(k=4\), and \(r=2\) give \(S_{\min}=100\), \(S_{\max}=180\), \(K_{\min}=185\), and \(K_{\max}=190\). The corresponding stationary-target hitting-time range is \(185/12\) to \(190/12\).

## Relationship to prior work

The electrical resistance law for two parallel arcs, the Kirchhoff-index/spectral relation, and weighted-cycle resistance formulas are classical, not claimed as new. Zhang and Yang derived explicit resistance-distance and Kirchhoff-index formulas for unweighted circulant graphs (first public 2006). Carmona, Encinas, and Mitjana treat weighted unicycle chains, including weighted cycles, with general resistance/Kirchhoff identities (2014); their exact weighted-cycle formulas supply powerful prior general coverage of the evaluation problem. This result instead identifies, for a fixed **binary multiset of arbitrary positive edge resistances**, every globally extremizing cyclic *placement*, the strict equality classes, a closed arithmetic gcd correction, and the bias-insensitive ordering for faster and slower defects. General formulas alone do not state that discrete placement classification. The claim is about a constrained rearrangement theorem, not an entirely new resistance method. Searches did not locate an exact earlier rearrangement theorem, but incomplete bibliographic access leaves priority risk.

## Limitations

The theorem holds for a cycle with two resistance levels and fixed counts, and the continuous-time symmetric nearest-neighbor process specified above. It makes no statement for three or more distinct edge resistance values, directed jumps, edge-independent holding clocks, arbitrary graphs, spectral gaps, or entropy-production fluctuations. The correct and valuable mathematical result may have an unindexed equivalent in the older electrical-network rearrangement literature; an independent historical review remains unperformed. All numerical checks are finite and supplemental to the proof.

## References

- H. Zhang and Y. Yang, *Resistance distance and Kirchhoff index in circulant graphs*, International Journal of Quantum Chemistry 107 (2007), 330–339. First published 2006-09-05. https://doi.org/10.1002/qua.21068
- À. Carmona, A. M. Encinas, and M. Mitjana, *The Kirchhoff index of unicycle weighted chains*, Electronic Notes in Discrete Mathematics 46 (2014), 217–224. https://doi.org/10.1016/j.endm.2014.08.029
- Related but distinct published optimization literature: equal/unequal-price spectral-gap design for weighted cycles and total-resistance design on other graph topologies. These do not supply the fixed-two-level cyclic rearrangement statement in the inspected material.
