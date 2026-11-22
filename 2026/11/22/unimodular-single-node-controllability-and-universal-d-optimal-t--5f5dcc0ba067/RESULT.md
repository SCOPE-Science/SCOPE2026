# Unimodular single-node controllability and universal D-optimal ties on paths

## Finding
For every integer \(n\ge2\), let \(L_n\) be the combinatorial Laplacian of the unit-edge path on labelled vertices \(1,\ldots,n\), and let \(e_j\) be the \(j\)-th coordinate vector. Its signed Kalman matrix
\[
\mathcal K_j=[e_j,(-L_n)e_j,\ldots,(-L_n)^{n-1}e_j]
\]
has determinant in \(\{-1,0,1\}\) for **every** vertex. More precisely,
\[
\boxed{|\det\mathcal K_j|=\mathbf 1_{\gcd(2j-1,n)=1}.}
\]
For all damping parameters \(\mu\ge0\) and finite horizons \(T>0\), define the single-input controllability Gramian
\[
W_j(T,\mu)=\int_0^T e^{-(L_n+\mu I)t}e_je_j^{\mathsf T}e^{-(L_n+\mu I)t}\,dt.
\]
Put \(a_k=\mu+2-2\cos(\pi k/n)\) for \(0\le k<n\), and let \(C(T,\mu)\) be the positive definite \(n\)-by-\(n\) matrix with entries
\[
C_{k\ell}(T,\mu)=\begin{cases}(1-e^{-(a_k+a_\ell)T})/(a_k+a_\ell),&a_k+a_\ell>0,\\ T,&a_k+a_\ell=0.\end{cases}
\]
Then the **exact determinant classification** is
\[
\boxed{\det W_j(T,\mu)=\begin{cases}
(2n)^{1-n}\det C(T,\mu),&\gcd(2j-1,n)=1,\\[2pt]
0,&\gcd(2j-1,n)>1.
\end{cases}}
\]
Thus precisely \(\varphi(2n)\) vertices maximize finite-horizon controllability-volume determinant, **all at exactly the same positive value regardless of damping or horizon**. In particular, if \(n\) is a power of two, **every vertex** is D-optimal, despite the lack of an automorphism carrying an endpoint to an interior vertex when \(n\ge4\).

## Assumptions and scope
The path has unit undirected edges, no loops, and labelled vertices \(1,\ldots,n\). The system is \(\dot x=-(L_n+\mu I)x+e_ju\), with scalar input \(u\) of fixed unit amplitude and standard Euclidean state coordinates. The horizon is a strictly positive finite real \(T\). D-optimality means maximizing the determinant \(\det W_j(T,\mu)\) among the \(n\) single-vertex actuator choices. The damping parameter \(\mu\ge0\) is common to all nodes. The theorem is not a statement about diagonal degree-normalized dynamics or about multiple actuators.

## Proof
**1. Simple spectrum and eigenvectors.** The combinatorial path Laplacian has distinct eigenvalues \(\lambda_k=2-2\cos(\pi k/n)\), \(0\le k<n\), and an orthonormal eigenbasis \(v_k\) with
\[
v_0(j)=n^{-1/2},\qquad v_k(j)=\sqrt{2/n}\cos\!\left(\frac{\pi k(2j-1)}{2n}\right),\quad1\le k<n.
\]
The endpoint equations follow from the cosine half-step identity, and the interior equations from the cosine addition formula; orthogonality follows from finite cosine sums.

**2. Exact support classification and universal cosine product.** Put \(a=2j-1\), an odd integer. If \(g=\gcd(a,n)>1\), then \(g\) is odd and \(k=n/g\) lies between \(1\) and \(n-1\). Since \(a/g\) is odd, \(v_k(j)=\sqrt{2/n}\cos(\pi(a/g)/2)=0\). Conversely, if \(\gcd(a,n)=1\), then \(a\) is a unit modulo \(2n\). Multiplication by \(a\) permutes the unordered nonzero residue pairs \(\{k,2n-k\}\), \(1\le k<n\). Since \(\cos^2(\pi(2n-k)/(2n))=\cos^2(\pi k/(2n))\), we obtain
\[
\prod_{k=1}^{n-1}\cos^2\!\left(\frac{\pi ak}{2n}\right)
=\prod_{k=1}^{n-1}\cos^2\!\left(\frac{\pi k}{2n}\right)
=\frac{n}{4^{n-1}}.
\]
The final identity follows by pairing the sine factors of \(\prod_{r=1}^{2n-1}\sin(\pi r/(2n))=2n/2^{2n-1}\), using \(\sin(\pi(n-k)/(2n))=\cos(\pi k/(2n))\), and isolating the central factor. Consequently
\[
\prod_{k=0}^{n-1}v_k(j)^2=\begin{cases}(2n)^{1-n},&\gcd(2j-1,n)=1,\\0,&\text{otherwise}.\end{cases}
\]

**3. Unimodularity of the Kalman matrix.** Let \(Q\) have columns \(v_k\). The matrix \(Q^{\mathsf T}\mathcal K_j\) is the product of the diagonal matrix with entries \(v_k(j)\) and the Vandermonde matrix with entries \((-\lambda_k)^r\), \(0\le r<n\). Its determinant is zero precisely when some \(v_k(j)=0\). The absolute nonzero determinant is independent of \(j\), by Step 2, since the Vandermonde factor is fixed. At the endpoint \(j=1\), the \(r\)-th column of \(\mathcal K_1\) is supported on vertices \(1,\ldots,r+1\), and its entry at vertex \(r+1\) is exactly one: the unique length-\(r\) path contributes \((-1)^r\) to \(L_n^re_1\), cancelled by the sign in \((-L_n)^r\). Hence \(\mathcal K_1\) is upper triangular with unit diagonal and determinant one. All other nonsingular \(\mathcal K_j\) therefore have determinant \(\pm1\). This proves the first boxed formula.

**4. All-horizon Gramian determinant.** Orthogonally diagonalize \(L_n\) using \(Q\). In its modal coordinates,
\[
Q^{\mathsf T}W_j(T,\mu)Q=\operatorname{diag}(v_k(j))\,C(T,\mu)\,\operatorname{diag}(v_k(j)).
\]
The matrix \(C\) is the Gram matrix in \(L^2[0,T]\) of the linearly independent functions \(t\mapsto e^{-a_kt}\), so it is strictly positive definite even at \(\mu=0\). Taking determinants and applying Step 2 yields the second boxed formula, including the zero cases.

**5. Number of maxima.** For \(j=1,\ldots,n\), the odd integers \(2j-1\) represent every odd residue class modulo \(2n\) exactly once. They are units modulo \(2n\) precisely when coprime to \(n\). Their count is Euler's totient \(\varphi(2n)\). Since \(\det C>0\), exactly these vertices maximize \(\det W_j\). For \(n=2^s\), all odd integers are coprime to \(n\), so all \(n\) locations tie.

For strictly positive damping \(\mu>0\), the same equality persists as \(T\to\infty\), with the further explicit positive constant
\[
\det W_j(\infty,\mu)=(2n)^{1-n}\frac{\prod_{0\le k<\ell<n}(a_\ell-a_k)^2}{\prod_{k,\ell=0}^{n-1}(a_k+a_\ell)}
\]
at each controllable location, by the Cauchy determinant identity. This last infinite-horizon expression is not asserted for \(\mu=0\), since the undamped constant mode prevents a finite limiting Gramian.

## Verification
The standalone Python verifier `check.py` constructs integer Kalman matrices directly from the path Laplacian for every \(2\le n\le18\), confirming the complete \(0,\pm1\) determinant and coprimality rule. At 65-digit precision it checks the modal determinant factorization for \(2\le n\le9\), three pairs of damping and horizon values, and independently approximates the physical-coordinate Gramians by 240-point Gauss–Legendre time integration for \(2\le n\le7\). All 602 assertions passed. These are finite checks only; the general theorem rests on the proof above.

The equality is not explained by ordinary graph symmetry: for \(n\ge4\), an endpoint and an interior vertex have different degrees. In fact the trace expansion
\[
\operatorname{tr}W_j(T,\mu)=T-(\mu+\deg(j))T^2+O(T^3)
\]
shows that their traces differ for all sufficiently small positive horizons, even when their determinants coincide.

## Relationship to prior work
Parlangeli and Notarstefano (arXiv:1109.3556v1, first public September 16, 2011), Theorem 4.4, give a complete arithmetic characterization of path Laplacian reachability and observability. The **coprimality criterion alone is prior art**; this work instead establishes the stronger integer-Kalman **unimodularity** and a quantitative **equality of every positive finite-horizon reachability-volume determinant** across all controllable nodes. Neither the Gramian determinant nor all-horizon D-optimal ties is treated in the inspected source.

Summers and Lygeros (arXiv:1306.2491v1, June 11, 2013) study actuator placement based on controllability Gramians and prove modularity of their **trace**, not equality of path-vertex Gramian determinants. A separate published result, *Universal endpoint optimality for dynamical sampling on normalized paths* (finding identifier `d0ca7333cb0f`, full result inspected), gives a spectral-Vandermonde determinant for the **symmetric degree-normalized adjacency**, where endpoints are generically strictly optimal. That operator is not the combinatorial Laplacian used here, and the former endpoint-only conclusion cannot imply the all-vertex ties on dyadic unnormalized paths. The present theorem does not claim a result for the normalized setting.

## Limitations
This is a single-input, one-dimensional, unit-conductance path theorem, not a universal statement for weighted paths, arbitrary graphs, nonidentical vertex input gains, multiple actuators, or degree-normalized dynamics. Equality of determinants does not imply equal Gramian spectra, worst-case input energy, traces, or numerical condition numbers. Positivity of the determinant is an exact theoretical statement and may be difficult to resolve numerically for long paths at short horizons. Priority against unindexed equivalent literature is not certified; independent mathematical audit has not been performed.

## References
1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1, September 16, 2011. https://arxiv.org/abs/1109.3556
2. T. H. Summers and J. Lygeros, *Optimal Sensor and Actuator Placement in Complex Dynamical Networks*, arXiv:1306.2491v1, June 11, 2013. https://arxiv.org/abs/1306.2491
3. *Universal endpoint optimality for dynamical sampling on normalized paths*, published technical finding `d0ca7333cb0f` (comparative reading; distinct normalized operator).
4. Classical Vandermonde, Cauchy determinant, cosine-product and finite-dimensional spectral identities (derived or used explicitly above).
