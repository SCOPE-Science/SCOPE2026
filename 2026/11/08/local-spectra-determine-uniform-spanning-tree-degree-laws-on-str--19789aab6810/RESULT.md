# Local spectra determine uniform-spanning-tree degree laws on strongly regular graphs

## Finding
Let \(G\) be a finite, connected, noncomplete strongly regular graph with parameters \((v,k,\lambda,\mu)\), where \(\mu>0\). For any vertex \(u\), let \(H_u=G[N(u)]\) be its induced neighbor graph, and let its adjacency eigenvalues (including multiplicities) be \(\theta_1=\lambda,\theta_2,\ldots,\theta_k\), with the first eigenvector taken to be the all-ones vector. Define
\[
 t=k-\lambda+\mu,\qquad Q=k(k-1-\lambda+\mu)+\mu=v\mu.
\]
For a uniformly sampled spanning tree \(T\), denote by \(D_u\) the degree of \(u\) in \(T\). Its exact generating polynomial is
\[
 \boxed{\mathbb E[z^{D_u}]=z\prod_{j=2}^{k}\left(1+\frac{t+\theta_j}{Q}(z-1)\right).}
\]
Consequently, among rooted strongly regular graphs with the **same parameters**, equality of uniform-spanning-tree root-degree laws is equivalent to equality of the adjacency spectra of their induced root neighborhoods. All such root degrees have the same first two moments. Let \(\tau_u\) denote the number of triangles in \(H_u\), and define the third factorial cumulant by
\[
 \kappa_3^{F}(D)=\left.\frac{d^3}{ds^3}\log \mathbb E[(1+s)^D]\right|_{s=0}.
\]
For any two roots (possibly in different graphs) with these same parameters,
\[
 \boxed{\kappa_3^{F}(D_u)-\kappa_3^{F}(D_w)=\frac{12(\tau_u-\tau_w)}{Q^3}.}
\]

In particular, let \(R=K_4\square K_4\) be the sixteen-vertex rook graph and let \(S\) be the Shrikhande graph. These are nonisomorphic strongly regular graphs with the same parameters \((16,6,2,2)\) and the same number \(2^{35}\) of spanning trees. The distributions of the spanning-tree degree at any vertex have generating functions
\[
 P_R(z)=z\frac{3+z}{4}\left(\frac{27+5z}{32}\right)^4,
 \qquad
 P_S(z)=z\frac{7+z}{8}\left(\frac{25+7z}{32}\right)^2\left(\frac{27+5z}{32}\right)^2.
\]
Their exact difference is
\[
 \boxed{P_R(z)-P_S(z)=\frac{z(z-1)^3(5z+27)^2}{2^{23}}.}
\]
Thus the mean and variance agree (respectively \(15/8\) and \(183/256\)), but the first differing factorial moment is the third, with difference \(3/4096\). The leaf probabilities differ by
\[
 \Pr(D_R=1)-\Pr(D_S=1)=-\frac{729}{2^{23}}.
\]
This gives a finite local probabilistic invariant distinguishing these adjacency-cospectral, parameter-equivalent graphs.

## Assumptions and scope
A strongly regular graph with parameters \((v,k,\lambda,\mu)\) is a simple graph in which every vertex has \(k\) neighbors, adjacent vertices have \(\lambda\) common neighbors, and nonadjacent distinct vertices have \(\mu\) common neighbors. The assertion concerns connected noncomplete graphs, hence \(0<k<v-1\) and \(\mu>0\). Eigenvalues are repeated with algebraic multiplicity; the graph \(H_u\) is \(\lambda\)-regular, so its all-ones vector accounts for one designated eigenvalue \(\lambda\), even if the eigenvalue is repeated. All spanning trees are equally likely. The identity is exact for every such finite graph and root. The equivalence of degree laws and neighborhood spectra assumes the common parameters are known; it is not an assertion that degree laws recover arbitrary graphs.

## Proof
**1. Graph Laplacian inverse on constants' orthogonal complement.** Write \(A\) for the adjacency matrix of \(G\), \(J\) for the all-ones matrix, and \(L=kI-A\) for its Laplacian. The strongly regular identity is
\[
 A^2=(k-\mu)I+(\lambda-\mu)A+\mu J.
\]
From the identity \(k(k-1-\lambda)=\mu(v-k-1)\), obtain \(Q=v\mu\). With \(t=k-\lambda+\mu\), direct multiplication gives
\[
 L(tI+A)=QI-\mu J,
 \qquad L\frac{tI+A}{Q}=I-\frac{J}{v}.
\]
Consequently the Moore--Penrose inverse \(L^+\) differs from \((tI+A)/Q\) only by an additive scalar multiple of \(J\), which disappears in all edge-voltage differences.

**2. Exact star transfer-current kernel.** Index the \(k\) edges \(\{u,x\}\), \(x\in N(u)\), oriented from \(u\) to \(x\). Their transfer-current matrix is
\[
 K_{xy}=(e_u-e_x)^TL^+(e_u-e_y)
 =\frac{t\delta_{xy}+t-2+\mathbf1_{\{x,y\}\in E(H_u)}}{Q}.
\]
Thus
\[
 K=\frac{tI+A(H_u)+(t-2)J_k}{Q}.
\]
Because \(H_u\) is \(\lambda\)-regular, the all-ones vector has \(K\)-eigenvalue \([t+\lambda+k(t-2)]/Q=1\), while the other eigenvalues are \((t+\theta_j)/Q\), \(2\le j\le k\). By the transfer-current determinantal identity, or equivalently by applying the matrix-tree theorem and the matrix-determinant lemma after changing all incident conductances to \(z\),
\[
 \mathbb E[z^{D_u}]=\det(I_k+(z-1)K).
\]
Its eigenvalue factorization proves the first display. All factors have parameters in \((0,1]\): they are eigenvalues of a determinantal kernel, and positivity also follows because all incident star edges can be included in a spanning tree.

**3. Spectral recovery and low-order moments.** For fixed parameters the nonzero Bernoulli factors can be recovered, with multiplicity, from the roots of \(\mathbb E[z^{D_u}]/z\), and then transformed affinely to recover \(\{\theta_2,\dots,\theta_k\}\); appending the designated eigenvalue \(\lambda\) recovers the local spectrum. Each root of the polynomial corresponds to a unique nonzero Bernoulli parameter \((t+\theta_j)/Q\). The local adjacency matrix has
\[
 \sum_{j=2}^k\theta_j=-\lambda,
 \quad\sum_{j=2}^k\theta_j^2=k\lambda-\lambda^2,
 \quad\sum_{j=2}^k\theta_j^3=6\tau_u-\lambda^3.
\]
The first two sums are fixed by the strongly regular parameters, so the mean and variance of \(D_u\) are parameter-invariant. Since \(D_u\) has the independent Bernoulli-sum generating polynomial from Step 2, its third factorial cumulant is
\[
 \kappa_3^F(D_u)=2\left(1+\sum_{j=2}^k\left(\frac{t+\theta_j}{Q}\right)^3\right).
\]
Subtracting two instances with equal parameters cancels every term except the trace-cube term. The final difference is \(2(6\tau_u-6\tau_w)/Q^3=12(\tau_u-\tau_w)/Q^3\). Equality of ordinary first and second moments is sufficient to identify the same difference of third factorial moments.

**4. The sixteen-vertex distinguishing pair.** The rook graph is defined on \((\mathbb Z/4\mathbb Z)^2\), where two different vertices are adjacent when either coordinate agrees; its root neighborhood is \(K_3\sqcup K_3\), with spectrum \(2,2,-1,-1,-1,-1\). Construct the Shrikhande graph on the same vertex set by adjoining differences \((\pm1,0),(0,\pm1),(1,1),(-1,-1)\) modulo \(4\). Every root neighborhood is a six-cycle, with spectrum \(2,1,1,-1,-1,-2\). Both graphs have parameters \((16,6,2,2)\), whence \(t=6\) and \(Q=32\). Step 2 yields the two asserted products. Their subtraction factors to the stated polynomial. The local triangle counts are \(2\) and \(0\); Step 3 gives \(24/32^3=3/4096\). Coefficients of \(z\) give the leaf-probability difference. Finally both Laplacian spectra are \(0^1,4^6,8^9\); the matrix-tree theorem gives the common tree count \(4^6 8^9/16=2^{35}\).

## Verification
The standalone Python 3 file `verify.py` constructs both sixteen-vertex graphs from their edges, verifies all pairwise strongly regular common-neighbor counts, computes neighborhood characteristic polynomials via Newton identities, and **independently** computes root-degree generating polynomials from integer weighted-Laplacian cofactors using the fraction-free Bareiss determinant. Values at seven distinct integer weights \(z=0,1,\ldots,6\) suffice because each rooted degree polynomial has degree at most six. The checker also tests the Petersen graph (parameters \((10,3,0,1)\)), all polynomial coefficients and the third factorial-moment difference. Its observed output ends `VERIFY_OK 551 exact assertions`. This finite verification checks the explicit examples; the general theorem is established by the preceding symbolic proof. Run with `python3 verify.py` in any Python 3 environment; no third-party packages are required.

## Relationship to prior work
The transfer-current determinant and uniform spanning-tree edge determinantal law are classical. General finite-graph vertex-degree mass functions were obtained in [1], and general formulas for expectations and variances in [2]; the contribution here is **not** a new general transfer-current principle. The evaluated result is a structural spectral-recovery equivalence throughout the class of strongly regular graphs, the invariant first-two-moments/triangle-sensitive third-cumulant separation, and the explicitly resolved Shrikhande--rook discrepancy. The rook-only degree factorization is already known and is not independently claimed here. The large-degree local limit in [3] concerns a different asymptotic regime. The earlier general generating-function method in [4] is acknowledged. None of the material inspected from these sources gives the full strongly-regular local-spectrum recovery theorem or the exact distinguishing polynomial. Earlier general methods may permit independent derivations; historical priority remains an explicit limitation.

## Limitations
The equivalence of distributions and local spectra requires fixed strongly regular parameters. It does not prove graph isomorphism, nor recover a neighborhood graph beyond its adjacency spectrum. The specific example is finite and not an asymptotic separation. General finite-graph tree generating formulas can be specialized to the example, but they do not by themselves state the global local-spectrum recovery equivalence or the first-moment separation across a parameter class. An older pertinent full text [4] could not be obtained for an exhaustive priority comparison; only its available abstract and introductory excerpt were assessed. All computations were exact, but independent mathematical audit has not been performed.

## References
[1] A. Rapoport, *Correlations in uniform spanning trees: a fermionic approach*, arXiv:2312.14992, first public 2023-12-22, https://arxiv.org/abs/2312.14992.

[2] E. Fita Sanmartín, C. Schnörr, F. A. Hamprecht, *Expectation and Variance of the Degree of a Node in Random Spanning Trees*, arXiv:2409.13472, first public 2024-09-20, https://arxiv.org/abs/2409.13472.

[3] A. Nachmias, Y. Peres, *The local limit of uniform spanning trees*, arXiv:2011.08833, first public 2020-11-17, https://arxiv.org/abs/2011.08833.

[4] C. Pozrikidis, *Node degree distribution in spanning trees*, Journal of Physics A 49 (2016) 125101, https://doi.org/10.1088/1751-8113/49/12/125101 (full-text comparison unavailable).
