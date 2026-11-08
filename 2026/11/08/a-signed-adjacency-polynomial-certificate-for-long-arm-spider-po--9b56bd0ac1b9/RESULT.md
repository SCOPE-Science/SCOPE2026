# A signed adjacency-polynomial certificate for long-arm spider powers

## Finding
For integers \(m\ge 3\), \(k\ge 3\), and \(\ell\ge 2k-1\), let \(T=S_m(\ell)\) be the tree with a center joined to \(m\) internally disjoint arms, each containing \(\ell\) additional vertices. Let \(A\) be the **unweighted** adjacency matrix of \(T\), and put
\[
\lambda_j=2\cos\left(\frac{j\pi}{\ell+1}\right),\qquad
p(x)=\prod_{j=1}^{k}(x-\lambda_j).
\]
The canonical, parameter-free polynomial matrix \(X=p(A)\) has all three properties:

1. For every two distinct vertices at tree distance \(d\), the entry \(X_{uv}\) is zero **exactly** for \(d>k\), and when \(1\le d\le k\) its sign is **exactly** \((-1)^{k-d}\).
2. Its nullity is **exactly** \((m-1)k\); the kernel contains an explicit basis of \(k(m-1)\) arm-contrast path eigenvectors.
3. Hence \(X\) is a real symmetric optimal-rank matrix supported on the ordinary graph power \(T^k\), with \(\operatorname{rank}X=m\ell+1-(m-1)k\).

This is an explicit spectral and sign-regularity **certificate**, rather than a claim that the numerical maximum-nullity or zero-forcing value is new: those values follow from already released stronger forcing constructions. Unlike the existing parameter-tuned matrix, this certificate is a single polynomial of the unweighted adjacency matrix, and its entire off-diagonal sign pattern depends only on distance.

## Assumptions and scope
All graphs are finite, simple, and undirected. The graph \(T\) has vertices \(c\) and \(v_{i,t}\) for \(1\le i\le m\), \(1\le t\le\ell\); its edges are \(cv_{i,1}\) and \(v_{i,t}v_{i,t+1}\). Put \(n=m\ell+1\). For a graph \(H\), let \(\mathcal S_{\mathbb R}(H)\) be the set of real symmetric \(n\times n\) matrices with arbitrary diagonal and with \(X_{uv}\ne0\) for distinct \(u,v\) if and only if \(uv\) is an edge of \(H\). Then \(M_{\mathbb R}(H)=\max_{X\in\mathcal S_{\mathbb R}(H)}\dim\ker X\) and \(\operatorname{mr}_{\mathbb R}(H)=n-M_{\mathbb R}(H)\). Zero forcing uses the ordinary unique-white-neighbor rule. The range \(k\ge3\) deliberately excludes the previously solved case of squares of trees; \(m\ge3\) excludes the path case.

## Proof
Let \(A\) be the unweighted adjacency matrix of \(T\). The path adjacency matrix on \(\ell\) vertices has eigenvalues
\[
\lambda_j=2\cos\left(\frac{j\pi}{\ell+1}\right),\quad 1\le j\le\ell,
\]
and corresponding independent eigenvectors with entries \(f_j(t)=\sin(j\pi t/(\ell+1))\). Define the monic degree-\(k\) polynomial
\[
p(x)=\prod_{j=1}^{k}(x-\lambda_j),\qquad X=p(A).
\]
The length hypothesis gives \(\lambda_1>\cdots>\lambda_{k-1}>0\) and \(\lambda_k\ge0\): at \(\ell=2k-1\) the last is zero, otherwise it is positive.

**Exact support and signs.** Write \(p(x)=\sum_{r=0}^{k}(-1)^{k-r}e_{k-r}(\lambda_1,\ldots,\lambda_k)x^r\), where \(e_s\) denotes the elementary symmetric polynomial and \(e_0=1\). For \(1\le r\le k\), every \(e_{k-r}\) is strictly positive: there are \(k-1\) strictly positive roots and \(0\le k-r\le k-1\). The tree is bipartite. Thus if distinct vertices \(u,v\) have distance \(d\), then \((A^r)_{uv}=0\) for \(r<d\), or for \(r\not\equiv d\pmod 2\); and \((A^d)_{uv}=1\), by the unique simple path. If \(1\le d\le k\), every nonzero term in
\[
X_{uv}=\sum_{\substack{d\le r\le k\\r\equiv d\ ({\rm mod}\ 2)}}
(-1)^{k-r}e_{k-r}(\lambda_1,\ldots,\lambda_k)(A^r)_{uv}
\]
has the common sign \((-1)^{k-d}\). The \(r=d\) summand is strictly nonzero. Hence \(\operatorname{sgn}(X_{uv})=(-1)^{k-d}\) throughout \(1\le d\le k\). If \(d>k\), every \((A^r)_{uv}\) with \(r\le k\) vanishes, so \(X_{uv}=0\). Therefore \(X\in\mathcal S_{\mathbb R}(T^k)\), with no generic-parameter or cancellation assumption.

**Kernel.** For each \(1\le j\le k\) and \(1\le i\le m-1\), form a vector \(w_{i,j}\) with value zero at \(c\), values \(f_j(t)\) on arm \(i\), values \(-f_j(t)\) on arm \(m\), and zero on every other arm. Every arm equation is the path eigenvector equation, and the contributions to the center from arms \(i\) and \(m\) cancel. Thus \(Aw_{i,j}=\lambda_jw_{i,j}\), and consequently \(Xw_{i,j}=0\). For fixed \(j\), the \(m-1\) arm-contrast vectors are independent. Distinct \(j\) give distinct eigenvalues of the symmetric matrix \(A\), so their eigenspaces are independent. Therefore \(\dim\ker X\ge(m-1)k\).

**Matching upper bound.** The standard inequality \(M_{\mathbb R}(H)\le Z(H)\) applies to every simple graph \(H\). Abiad, Flagg, Ghasemi Nezhad, and Zeijlemaker, Proposition 9, give \(Z(S_m(\ell)^k)\le(m-1)k\) for \(m\ge2\) and \(\ell\ge k+1\), which the present parameters satisfy. Combining these inequalities with the explicit symmetric matrix yields
\[
(m-1)k\le\dim\ker X\le M_{\mathbb R}(T^k)\le Z(T^k)\le(m-1)k.
\]
The canonical polynomial has precisely the stated nullity and rank, completing the spectral and sign certificate. \(\square\)

## Verification
The accompanying standard-library program `artifacts/verify.py` constructs \(A\), forms \(p(A)\), and checks both exact-support signs and all \(k(m-1)\) explicit kernel vectors numerically for \(m\in\{3,4\}\), \(3\le k\le6\), and \(2k-1\le\ell\le2k+1\). It yields `SPECTRAL_SUPPORT_AND_KERNEL_OK 24` and `VERIFY_OK`. Floating-point comparisons are corroborative only; all quantifiers and boundary conditions in the finding follow from the exact proof above.

## Relationship to prior work
Abiad, Flagg, Ghasemi Nezhad, and Zeijlemaker (2026), Proposition 9, prove the upper bound for the ordinary zero-forcing number and their Theorem 20 explains why *any* degree-\(k\) adjacency polynomial having the correct support yields an eigenvalue-multiplicity lower bound. They do not choose the first \(k\) path eigenvalues on equal-legged spiders or prove the present distance-sign certificate for that canonical choice. The independently released resolution of their Conjecture 10 already proves the full zero-forcing equality for every \(\ell\ge k+1\), by a polynomial in a parameterized, generally nonsymmetric Jacobi-type matrix. That underlying tree matrix has positive products of opposite edge weights and may be diagonally symmetrized; accordingly, **the scalar real symmetric maximum-nullity formula is not claimed as original here**. The narrower result here supplies a *different, parameter-free, unweighted-adjacency* optimal matrix, with a uniform and exact sign on every distance layer and an explicit trigonometric kernel basis. The known numerical invariant does not specify such a matrix. Chang and Lin's square-of-tree theorem covers real symmetric maximum nullity for \(k=2\), but not the new \(k\ge3\) explicit adjacency filter. DeAlba and collaborators analyze ordinary powers of paths and strict powers of general trees, not this canonical higher-power spider spectral certificate.

## Limitations
The canonical certificate is proved for equal arms of length at least \(2k-1\), and it does not assert anything about this particular polynomial below that cutoff. Its nullity and rank consequences agree with, and are not novelty claims beyond, previously released full-domain forcing results and their possible diagonal symmetrization. The claimed contribution is the explicit **unweighted-adjacency polynomial** with exact layerwise signs and eigenvector decomposition. Other spectral-filter papers may contain equivalent formulas not found by the searches; that is the residual historical-priority risk. The finite numerical checks are corroborative only, and independent mathematical audit has not been performed.

## References
1. A. Abiad, M. Flagg, S. Ghasemi Nezhad, and S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892 (first public 2026-10-02), Proposition 9, Conjecture 10, and Theorem 20. https://arxiv.org/abs/2610.03892
2. G. J. Chang and J.-H. Lin, *Minimum Rank of Powers of Cycles and Trees*, Section 4, especially Theorem 4.1. https://www-math.nsysu.edu.tw/~chlin/Publications/Articles/GJpower.pdf
3. L. M. DeAlba, J. Grout, I.-J. Kim, S. Kirkland, J. J. McDonald, and A. Yielding, *Minimum Rank of Powers of Trees*, Electron. J. Linear Algebra **23** (2012), 151–163. https://doi.org/10.13001/1081-3810.1511
4. *Zero forcing the ordinary powers of equal-legged spiders*, released research dossier and resolution record concerning arXiv:2610.03892, https://www.trureturing.org/research/abiad-equal-legged-spider-power-zero-forcing/ (accessed 2026-11-06 UTC).
