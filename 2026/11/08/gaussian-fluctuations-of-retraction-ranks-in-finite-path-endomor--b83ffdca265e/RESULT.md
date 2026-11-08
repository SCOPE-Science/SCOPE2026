# Gaussian fluctuations of retraction ranks in finite path endomorphism monoids

## Finding
For each integer \(n\geq2\), let \(P_n\) be the *undirected simple path* with vertex set \(\{1,\ldots,n\}\) and edges between consecutive integers. Let \(\mathcal E_n\) be the monoid of graph endomorphisms \(f:P_n\to P_n\) satisfying \(|f(i+1)-f(i)|=1\). Write \(\mathcal I_n=\{f\in\mathcal E_n:f\circ f=f\}\). Here **rank** means cardinality of the image of an individual transformation, not the minimum number of monoid generators.

For \(r\geq2\), write \(A_r\) for the \(r\)-by-\(r\) zero-one adjacency matrix of \(P_r\), \(e_1\) for the first coordinate vector, and \(\mathbf 1\) for the all-ones vector. Define \(w_r(\ell)=e_1^T A_r^{\ell}\mathbf 1\) for each integer \(\ell\geq0\). For every \(n\geq2\), the exact number of idempotent path endomorphisms of rank \(r\) is
\[
\boxed{N_{n,r}=\sum_{\ell=0}^{n-r}w_r(\ell)w_r(n-r-\ell),\quad 2\leq r\leq n.}
\]
No rank-one idempotent exists for \(n\geq2\). In particular \(N_{n,n}=1\) and \(N_{n,2}=n-1\).

Put
\[
 a=\log2,\qquad c=\left(\frac{\pi^2}{a}\right)^{1/3},\qquad \sigma^2=\frac{c}{3a},\qquad K=\frac32ac.
\]
Here logarithms are natural. Let \(R_n\) be the image rank of a uniformly sampled element of \(\mathcal I_n\), and write \(I_n=|\mathcal I_n|=\sum_{r=2}^n N_{n,r}\). Then
\[
\boxed{\log I_n=n\log2-Kn^{1/3}+o(n^{1/3})},
\]
\[
\boxed{\frac{R_n-cn^{1/3}}{n^{1/6}}\ \Longrightarrow\ \mathcal N\left(0,\frac{c}{3\log2}\right)}.
\]
Consequently \(R_n/n^{1/3}\to c\) in probability. Moreover, for each \(\epsilon>0\), there is \(\gamma_\epsilon>0\) such that, for all sufficiently large \(n\),
\[
\Pr\left(\left|R_n/n^{1/3}-c\right|>\epsilon\right)\leq\exp(-\gamma_\epsilon n^{1/3}).
\]
The Gaussian fluctuation theorem, beyond the first-order cubic-root scale, is the main contribution; the finite convolution is included as its exact foundation.

## Assumptions and scope
All graphs are finite, simple, undirected, loopless and *labeled*. A graph homomorphism must map every edge to an edge; edge contractions are **not** permitted. The monoid operation is composition. All counts distinguish actual functions rather than conjugacy classes. The limit is over positive integers \(n\to\infty\), with no other parameter. The normal convergence is weak convergence of real-valued random variables.

## Proof
**1. Retractions and the exact convolution.** An endomorphism of a connected path has an interval as its vertex image, because its values change by one along each edge. If \(f^2=f\), it fixes every point in its image. Thus there is a unique interval \([s,s+r-1]\subseteq[1,n]\) fixed pointwise, with \(r\geq2\); the lower bound follows from the absence of loops. Conversely, a graph homomorphism into that interval that fixes it is an idempotent. Let \(\ell=s-1\) and \(m=n-r-\ell\). On the \(\ell\) vertices to the left, the images, read from the fixed endpoint outwards, form a walk of length \(\ell\) in \(P_r\) beginning at endpoint 1. The right-hand tail independently gives a walk of length \(m\) beginning at endpoint \(r\), counted by the same number \(w_r(m)\) by reflection. Summing over the unique possible locations of the fixed interval proves the exact convolution. For \(r=2\) there is exactly one walk of each length from a chosen endpoint; hence \(N_{n,2}=n-1\).

**2. Exact spectral expansion.** Let \(\theta_r=\pi/(r+1)\) and \(\lambda_r=2\cos\theta_r\). The orthonormal eigenvectors of \(A_r\) have entries \(\sqrt{2/(r+1)}\sin(jx\theta_r)\), with eigenvalues \(2\cos(j\theta_r)\), for \(1\leq j,x\leq r\). Summing each eigenvector over \(x\) gives zero for even \(j\), while the coefficient of the odd-\(j\) eigenvalue in \(w_r(\ell)\) is \(2(1+\cos(j\theta_r))/(r+1)\). Therefore
\[
 w_r(\ell)=\sum_{\substack{1\leq j\leq r\\j\text{ odd}}}
 \frac{2(1+\cos(j\theta_r))}{r+1}\bigl(2\cos(j\theta_r)\bigr)^\ell.
\]
Write \(b_r=2(1+\cos\theta_r)/(r+1)\). If \(r\) is odd, the last eigenvalue is \(-\lambda_r\), with coefficient \(d_r=2(1-\cos\theta_r)/(r+1)\); if \(r\) is even, set \(d_r=0\). Thus \(b_r\asymp r^{-1}\), \(d_r=O(r^{-3})\), and
\[
 \lambda_r^{-\ell}w_r(\ell)=b_r+d_r(-1)^\ell+\varepsilon_r(\ell).
\]
For \(r\geq4\), all remaining eigenvalues have absolute value at most \(\rho_r=2\cos(2\theta_r)<\lambda_r\). More precisely, if \(c_{r,j}=2(1+\cos(j\theta_r))/(r+1)\) and \(\eta_{r,j}=|\cos(j\theta_r)|/\cos\theta_r\) for odd \(j\notin\{1,r\}\), then
\[
 |\varepsilon_r(\ell)|\leq E_r(\ell):=\sum_{j}c_{r,j}\eta_{r,j}^{\ell},\quad
 \sum_{\ell\geq0}E_r(\ell)=O(r),\quad
 E_r(\ell)\leq\exp(-\kappa\ell/r^2)
\]
for an absolute \(\kappa>0\) and all large \(r\). The constants are uniform in \(r\). To justify the middle bound, divide the indices at \((r+1)/2\). For the lower half \(1-\eta_{r,j}\geq C(j^2-1)/(r+1)^2\) and \(c_{r,j}\leq4/(r+1)\), giving a convergent \(O(r)\) sum of \((j^2-1)^{-1}\). For the upper half put \(t=r+1-j\geq2\): then \(c_{r,j}=O(t^2/r^3)\) and \(1-\eta_{r,j}\geq C(t^2-1)/r^2\), giving an \(O(1)\) total. These inequalities follow directly from \(\cos u-\cos v=2\sin((u+v)/2)\sin((v-u)/2)\) and elementary bounds on sine. The last estimate follows from \(\log(\cos\theta_r/\cos2\theta_r)\geq3\theta_r^2/2\). The finitely many small \(r\) are irrelevant to the asymptotic statements.

**3. Uniform local rank estimate.** Fix \(0<u<v<\infty\) and suppose \(u n^{1/3}\leq r\leq v n^{1/3}\). Write \(k=n-r\). Substitute the preceding decomposition in the convolution. The \(b_r^2\) terms contribute \((k+1)b_r^2\lambda_r^k\); the parity terms contribute relative \(O(r^{-4})\), because \(d_r/b_r=O(r^{-2})\). Each cross term involving a single \(\varepsilon\) is at most \(O(b_r r\lambda_r^k)\) in absolute value, by the summability bound. For products of two errors, in every summand at least one argument is \(\geq k/2\), so their total is \(O(r\lambda_r^k\exp(-\kappa k/(2r^2)))\). It follows uniformly on this window that
\[
 \boxed{N_{n,r}=(n-r+1)b_r^2\lambda_r^{n-r}(1+o(1)).}
\]
In fact the relative error is \(O(r^2/n+r^{-4})\) plus an exponentially small term. In particular, \(\log N_{n,r}=(n-r)\log\lambda_r+O(\log n)\) uniformly in such windows.

**4. Cubic-root saddle.** Uniformly for \(r=sn^{1/3}\) with \(s\) in a compact subinterval of \((0,\infty)\), the Taylor expansion of cosine gives
\[
 (n-r)\log\lambda_r
 =n\log2-n^{1/3}F(s)+o(n^{1/3}),\qquad
 F(s)=s\log2+\frac{\pi^2}{2s^2}.
\]
The unique minimum is at \(s=c\), with \(F(c)=K\). To control outside compact windows, the spectral-norm bound \(w_r(\ell)\leq\sqrt r\lambda_r^\ell\) gives \(N_{n,r}\leq n^2\lambda_r^{n-r}\). For \(r\leq u n^{1/3}\), the inequality \(\log\cos\theta\leq-\theta^2/2\) gives a loss at least \(\pi^2 n/(4(r+1)^2)\) for large \(n\); choosing \(u\) small makes it larger than \(Kn^{1/3}\) by a fixed margin. For \(r\geq v n^{1/3}\), use \(\lambda_r\leq2\) and choose \(v\) large, yielding a loss of at least \(v(\log2)n^{1/3}\). The Laplace comparison therefore proves the stated exponential concentration and the asymptotic logarithm of \(I_n\), because summing at most \(n\) ranks changes its logarithm by only \(O(\log n)\).

**5. Gaussian fluctuations.** Let \(r_0=cn^{1/3}\) be real and define the smooth function \(\Phi_n(x)=(n-x)\log(2\cos(\pi/(x+1)))\) near \(r_0\). Direct differentiation gives
\[
 \Phi_n'(r_0)=O(n^{-1/3}),\quad
 \Phi_n''(r_0)=-\frac{3\log2}{c}n^{-1/3}+O(n^{-2/3}),\quad
 \sup_{|x-r_0|\leq\delta n^{1/3}}|\Phi_n'''(x)|=O(n^{-2/3})
\]
for a sufficiently small fixed \(\delta>0\). Hence, uniformly for bounded real \(t\), with integer \(r=r_0+t n^{1/6}+O(1)\),
\[
 \log\frac{N_{n,r}}{N_{n,\lfloor r_0\rfloor}}
 =-\frac{3\log2}{2c}t^2+o(1).
\]
Here the prefactor \((n-r+1)b_r^2\) varies by \(1+o(1)\) over the fluctuation window, and the rank estimate from Step 3 is uniform. Within \(|r-r_0|\leq\delta n^{1/3}\), the second derivative is bounded above by a negative multiple of \(n^{-1/3}\), so the same estimate gives summable Gaussian tails in \((r-r_0)/n^{1/6}\). Step 4 makes the remaining ranks exponentially negligible. Riemann-sum normalization on the integer lattice of mesh \(n^{-1/6}\) proves convergence to the centered normal law with variance \(c/(3\log2)\).

## Verification
The standalone script `verify.py` uses only the Python standard library. It separately enumerates every edge-preserving self-map of \(P_n\) by choosing an initial vertex and all successive \(\pm1\) steps, tests \(f^2=f\) directly, and compares the image-rank histogram to the independent transfer-matrix convolution for every \(2\leq n\leq11\). Exact sample histograms for \(n=5\) and \(n=8\) are, respectively, \((4,5,2,1)\) and \((7,24,20,10,5,2,1)\), ordered by ranks beginning at two. Further exact rank histograms at \(n=30,100,300\) corroborate the scale and variance qualitatively; finite checks are not proofs of the infinite-limit assertions. The completed run printed `VERIFY_OK`.

## Relationship to prior work
Dimitrova, Fernandes, Koppitz, and Quinteiro (first arXiv public version October 22, 2018) classify and generate endomorphism monoids of paths and study their semigroup generator ranks; their use of the word 'rank' concerns the whole monoid's minimal generating set, not the image size of a uniformly sampled idempotent. Their interval-image characterization is used here as established background. Earlier path-homomorphism enumeration by Eggleton and Morayne (online November 24, 2012) counts unrestricted path homomorphisms with specified endpoints; it supplies relevant walk-count context but not the idempotent rank law. A 2012 thesis chapter on endo-regularity of paths and cycles already states the fixed-image-interval criterion for idempotents, which is **not** claimed as new. The new claim is the Gaussian fluctuation limit, together with its specific centering, variance, and a complete proof through the exact finite convolution.

A related enumeration of idempotents for *weak cycle* graph endomorphisms, where edge contraction is allowed and the graph is cyclic, has a cubic-root leading scale. It concerns a different monoid and does not entail the non-lazy path convolution or its Gaussian fluctuation law. General spectral/Laplace methods themselves are standard. No uniqueness or publication priority beyond the inspected sources is asserted.

## Limitations
The theorem does not cover weak endomorphisms, directed paths, arbitrary trees, or graph homomorphisms that contract edges. The operator rank is not a semigroup generator rank. The original fixed-interval retraction criterion and path-walk recurrences are established prior mathematics. The result has not received independent mathematical validation; an unlocated broader transfer-matrix asymptotic theorem could imply some or all of the limiting law. Numerical checks involve finite \(n\) only. Public-source priority remains provisional.

## References
1. I. Dimitrova, V. H. Fernandes, J. Koppitz, and T. M. Quinteiro, *Ranks of monoids of endomorphisms of a finite undirected path* (2018 preprint), arXiv:1810.09307, https://arxiv.org/abs/1810.09307 ; accessible author manuscript https://research.unl.pt/ws/files/18723855/endpn.pdf .
2. R. B. Eggleton and M. Morayne, *A Note on Counting Homomorphisms of Paths*, *Graphs and Combinatorics* 30 (2014), 159–170, first online November 24, 2012, DOI:10.1007/s00373-012-1261-0, https://link.springer.com/article/10.1007/s00373-012-1261-0 .
3. *Endo-Regularity of Paths and Cycles*, a 2012 thesis chapter, §3.1, especially Lemma 3.1.8, https://archive.lib.cmu.ac.th/full/T/2012/math20712np_ch3.pdf .
4. J. Focke, L. A. Goldberg, and S. Živný, *The Complexity of Approximately Counting Retractions* (2018), arXiv:1807.00590, https://arxiv.org/abs/1807.00590 ; concerns the complexity of general retraction counting rather than the rank law here.
