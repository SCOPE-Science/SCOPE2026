# A linear path-length guarantee for one-vertex D-optimal sensing at low bandwidth

## Finding

Let the unit-edge path have vertices \(0,\ldots,n\) and use its symmetric normalized Laplacian. For \(r\ge5\), restrict signals to the first \(r\) normalized-Laplacian modes. At a single vertex take \(r\) observations at times \(0,\ldots,r-1\) under any spectral evolution with distinct eigenvalues on these modes. If \(n\ge12(r-1)\), then exactly the two vertices \(1\) and \(n-1\) adjacent to the endpoints maximize the determinant of the information Gramian. The claim is a uniform sufficient bound, not an exact cutoff.

## Assumptions and scope

The signal space is complex with the standard Euclidean inner product. Write \(d_j=1\) for \(j=0,n\) and \(d_j=2\) otherwise. For ordinary adjacency \(A\) and diagonal degree matrix \(D\), the normalized Laplacian is \(I-D^{-1/2}AD^{-1/2}\). The evolution \(T\) has the selected modes as eigenvectors, with pairwise distinct, possibly complex eigenvalues. The observation map at \(j\) is \(f\mapsto((T^t f)(j))_{t=0}^{r-1}\) on the selected subspace, and its information Gramian is the observation map's adjoint times the observation map. Thus the objective is the squared absolute analysis determinant; it is not the condition number or minimum singular value.

## Proof

**Reduction to a cosine product.** The normalized-path eigenvectors have entries \(c_\ell\sqrt{d_j}\cos(\pi\ell j/n)\), where \(c_\ell\ne0\) are normalization constants. Indeed, the cosine vectors satisfy the averaging recursion for \(D^{-1}A\) by the cosine addition identity at interior vertices and reflection at the endpoints. Conjugating by \(D^{1/2}\) gives the symmetric normalized eigenvectors, with eigenvalues \(1-\cos(\pi\ell/n)\) in increasing order for the normalized Laplacian. In these orthonormal coordinates the observation matrix is a Vandermonde matrix in the evolution eigenvalues, times a diagonal matrix of vertex-mode entries. Its squared absolute determinant, divided by the positive determinant at vertex 0, is the known one-sensor ratio
\[
d_j^r H_k(\pi j/n),\qquad H_k(\theta)=\prod_{\ell=1}^k\cos^2(\ell\theta),\qquad k=r-1.
\]
Reflection across the midpoint preserves the ratio, and all interior vertices have the same degree factor \(2^r\).

**Uniform control away from the endpoint.** The product \(H_k\) decreases strictly on \([0,\pi/(2k)]\): the factors are nonnegative and decreasing there, with the first strictly decreasing and every factor positive before the upper endpoint. For \(\pi/(2k)\le\theta\le\pi/2\), the geometric sum gives
\[
 \left|\sum_{\ell=1}^k e^{2i\ell\theta}\right|\le \frac1{\sin\theta}\le\frac{k}{\sqrt2}.
\]
For the last inequality use \(\sin \theta\ge\sin(\pi/(2k))\), then the chord bound \(\sin x\ge (2\sqrt2/\pi)x\) on \([0,\pi/4]\), which applies since \(k\ge4\). Consequently
\[
 \sum_{\ell=1}^k\sin^2(\ell\theta)
 =\tfrac12\left(k-\operatorname{Re}\sum_{\ell=1}^k e^{2i\ell\theta}\right)
 \ge \tfrac12(1-1/\sqrt2)k>7k/50.
\]
Applying \(1-u\le e^{-u}\) to the squared cosine factors gives \(H_k(\theta)<\exp(-7k/50)\) throughout this interval, including locations with a vanishing factor.

**The nearest interior vertex beats that bound and the endpoints.** If \(n\ge12k\), each \(t=\ell\pi/n\) with \(1\le\ell\le k\) satisfies \(0\le t\le\pi/12\). Hence \(\cos^2 t\ge1-t^2\), and \(\log(1-t^2)\ge-2t^2\) since \(t^2\le1/2\). Summing and using \(\sum_{\ell=1}^k\ell^2\le k^3\) gives
\[
 H_k(\pi/n)\ge\exp(-2\pi^2 k^3/n^2)\ge\exp(-\pi^2 k/72)>\exp(-7k/50),
\]
where the strict inequality uses \(\pi^2<10\). In the first interval, \(\pi/n\) is the smallest positive grid angle, so strict monotonicity gives a strict advantage over larger grid angles there. Thus, among the interior vertices, only \(1,n-1\) maximize. Moreover \(2^r H_k(\pi/n)>2^{k+1}\exp(-7k/50)>1\) since \(\log 2\ge 1/2\). The endpoint ratio is 1, so this is also the global maximizing pair of vertices for the one-sensor problem.

## Verification and limits

The theorem is proved by exact estimates above; in particular, the bound on the geometric sum is uniform in both the vertex angle and the mode count. No finite numerical classification is needed. The condition is sufficient and its constant is not claimed optimal. This result compares individual sensors across all path vertices. It does not optimize a pair of simultaneously used sensors, a different time grid, a different loss, or a different graph family.

## Relationship to prior work

*Sharp low-bandwidth path sensor phase diagram for three temporal observations* (Resultary record `e45b195df1c5`, 2026-11-02) gives the one-vertex determinant factorization used here and the exact maximizing sites for two, three and four modes. Those are prior results, including the endpoint-to-neighbor switch at seven vertices for three modes. The claim here is a uniform linear sufficient length for larger bandwidths, including bandwidths growing with path length. *A dynamics-independent sensor-placement transition on finite normalized paths* (Resultary record `d31afb5d0f31`, 2026-11-02) analyzes a determinant ratio between the endpoint pair and inward pair; it does not compare one-vertex designs over all interior sites. The distinction in the present proof is the uniform off-endpoint product estimate, which is needed even when the inward site already beats the endpoint. Bulai et al., *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472, study the finite-path framework and conditioning of sampling designs; the objective here is the one-site determinant.
