# Exact collision-tail law for one-per-cell random Lagrange interpolation

## Finding

Let \(m\ge 2\) be an integer, let \(I_j=[(j-1)/m,j/m]\), and draw independent \(X_j\sim\operatorname{Uniform}(I_j)\) for \(j=1,\ldots,m\). At any *fixed* evaluation point \(z\in[0,1]\), define the degree-\((m-1)\) Lagrange interpolation weights
\[
L_j(z)=\prod_{k\ne j}\frac{z-X_k}{X_j-X_k},\qquad W_m(z)=\left(\sum_{j=1}^m L_j(z)^2\right)^{1/2}.
\]
The nodes are distinct with probability one. Put \(b_i=i/m\) and
\[
K_m(z)=m^2\sum_{i=1}^{m-1}(z-b_i)^2
\prod_{k\notin\{i,i+1\}}
\left[m\int_{(k-1)/m}^{k/m}\left(\frac{z-u}{b_i-u}\right)^2\,du\right],
\]
with an empty product defined to be one. Then
\[
\boxed{\lim_{t\to\infty}t^2\Pr\{W_m(z)>t\}=K_m(z).}
\]
The integral factors are finite. For \(m\ge3\), \(K_m(z)>0\) for every \(z\in[0,1]\); for \(m=2\), \(K_2(z)=4(z-1/2)^2\). Consequently, for \(m\ge3\), or \(m=2\) and \(z\ne1/2\), every \(p>0\) satisfies
\[
\mathbb E[W_m(z)^p]<\infty\quad\Longleftrightarrow\quad p<2.
\]
At the sole exceptional case \(m=2,z=1/2\), the weights are nonnegative, sum to one, and \(W_2(1/2)\le1\).

In particular, for \(m=3,z=1/2\), the sharp coefficient has the closed form
\[
\boxed{K_3(1/2)=\frac9{16}-\frac{\log2}{2}=0.215926409720\ldots.}
\]
If the observed values are \(f(X_j)+\eta_j\) with independent centered errors \(\eta_j\) of common variance \(\sigma^2\in(0,\infty)\), independent of the nodes, their interpolation contribution at \(z\) has conditional variance \(\sigma^2 W_m(z)^2\). Its unconditional second moment is therefore infinite whenever \(K_m(z)>0\), even for \(f\equiv0\).

## Assumptions and scope

The nodes are independent and exactly uniform on each of the \(m\) adjacent *closed, full-width* equal cells. Endpoints have zero sampling probability; no ordering ambiguities occur almost surely. The evaluation location \(z\) is deterministic and does not depend on the samples. The rule is the exact polynomial interpolant, not a regularized or safeguarded approximation, and the norm is the Euclidean norm of the vector of sample-value coefficients. The tail variable \(t\) tends to infinity at fixed \(m,z\). No conclusion concerns growth as \(m\to\infty\), rounding errors in computing the weights, or noiseless approximation accuracy for smooth functions.

## Proof

**1. The only possible collisions are at shared cell boundaries.** Set \(h=1/m\) and \(\Delta_i=X_{i+1}-X_i\). For each adjacent pair, write \(X_i=b_i-u\), \(X_{i+1}=b_i+v\) with independent \(u,v\sim\operatorname{Uniform}([0,h])\). Then \(\Delta_i=u+v\) and, for \(0\le s\le h\),
\[
\Pr\{\Delta_i<s\}=\frac{m^2s^2}{2}.
\]
For \(|j-k|\ge2\), the node separation \(|X_j-X_k|\) is at least \(h\). For any interior index \(j\), \(\Delta_{j-1}+\Delta_j=X_{j+1}-X_{j-1}\ge h\). It follows by bounding the Lagrange products that there is a finite constant \(B_m\) such that, almost surely,
\[
W_m(z)\le\frac{B_m}{\min_{1\le i<m}\Delta_i},\qquad z\in[0,1].
\]
One can take a common bound by using \(|z-X_k|\le1\), \(|X_j-X_k|\ge h\) for \(|j-k|\ge2\), and the fact that at least one of two adjacent gaps is at least \(h/2\). Hence \(\{W_m(z)>t\}\) is contained in the union of \(\{\Delta_i<B_m/t\}\).

**2. A single collision has an explicit residue.** Fix \(i\) and all other nodes \(Y=(X_k)_{k\notin\{i,i+1\}}\), which almost surely do not coincide. Define
\[
C_i(z,Y)=(z-b_i)\prod_{k\notin\{i,i+1\}}\frac{z-X_k}{b_i-X_k}.
\]
When \(u,v\downarrow0\), with \(\Delta_i=u+v\), the product formula gives
\[
\Delta_i L_i(z)\longrightarrow-C_i(z,Y),\qquad
\Delta_i L_{i+1}(z)\longrightarrow+C_i(z,Y),
\]
while \(\Delta_i L_k(z)\to0\) for all other indices \(k\). Thus \(\Delta_iW_m(z)\to\sqrt2|C_i(z,Y)|\). All factors \((b_i-X_k)^{-1}\) in \(C_i\) are uniformly bounded by \(m\), since the other cells lie at least one cell-width from \(b_i\).

**3. Tail asymptotics and addition of faces.** In the integral over \(X_i,X_{i+1}\), substitute \(u=s/t,v=r/t\). For almost every fixed \(Y\) and \(s,r\ge0\),
\[
\frac{W_m(z)}{t}\longrightarrow\frac{\sqrt2|C_i(z,Y)|}{s+r}.
\]
The event \(W_m(z)>t\) requires some \(\Delta_j<B_m/t\), and on the \(i\)-th such event the scaled triangle \(s+r<B_m\) has finite area. Dominated convergence therefore gives the single-face coefficient
\[
m^2\int_{s,r\ge0}{\bf1}\{s+r<\sqrt2|C_i(z,Y)|\}\,ds\,dr
=m^2C_i(z,Y)^2.
\]
Two adjacent gaps cannot both be smaller than \(B_m/t\) when \(t>2mB_m\). Two nonadjacent gaps depend on disjoint node pairs, so the probability that both are below \(B_m/t\) is \(O(t^{-4})\). Their intersections thus vanish after multiplying by \(t^2\), and summation over the \(m-1\) collision faces is justified. Taking the expectation of \(C_i^2\) over the independent remaining nodes produces exactly the displayed product-integral expression for \(K_m(z)\). These estimates also cover \(C_i=0\) at a boundary evaluation location.

**4. Positivity, moments, and the exception.** Each factor in every product-integral is strictly positive and finite, because \(z-X_k\ne0\) almost surely and \(|b_i-X_k|\ge h\). If \(m\ge3\), at least one of the distinct boundaries \(b_i\) differs from a fixed \(z\), hence \(K_m(z)>0\). For \(m=2\), the empty products give \(K_2(z)=4(z-1/2)^2\). If \(z=1/2\), both interpolation weights are the two nonnegative relative subsegment lengths and sum to one. For \(K_m(z)>0\), integration of \(p\int_0^\infty t^{p-1}\Pr(W_m(z)>t)\,dt\) gives finiteness exactly for \(p<2\), including divergence at \(p=2\).

**5. The three-node constant.** At \(m=3,z=1/2\), the two collision faces are reflection-symmetric. Each has \((z-b_i)^2=1/36\), and the one remaining cell contributes
\[
3\int_{2/3}^{1}\left(\frac{1/2-u}{1/3-u}\right)^2du
=\frac98-\log2.
\]
Therefore \(K_3(1/2)=9\cdot2\cdot(1/36)(9/8-\log2)=9/16-(\log2)/2\), as claimed. Independent centered evaluation noise yields the variance statement by conditioning on the nodes and applying the law of total expectation.

## Verification

A standalone Python script `verify.py` independently evaluates the integral for \(K_3(1/2)\) using numerical quadrature, checks the Lagrange reproduction identities on many generated node triples, verifies the near-collision scaling for explicit triples, and compares rare-event frequencies with the proven constant using a seeded Monte Carlo diagnostic. All infinity and moment classifications are mathematical deductions above, **not** empirical certifications. Run `python verify.py` with Python 3 and NumPy installed; the script prints its own check counts and diagnostic frequencies.

## Relationship to prior work

Dell'Accio, Sommariva and Vianello (first public preprint 2023-03-24) prove almost-sure nonsingularity of random polynomial interpolation matrices in an analytic-function framework, which is compatible with but does not imply any finite moments for inverse interpolation weights. Xu and Narayan (first preprint 2021-01-11) treat high-probability norming properties of random *oversampled meshes* rather than one-node-per-cell exact interpolation. Shen and Serkh (first preprint 2022-12-20) analyze basis choice, Vandermonde conditioning and backward stability for general interpolation nodes, not the probability distribution of colliding full-cell jittered nodes. Occorsio and Themistoclakis (2020) study deterministic filtered Chebyshev interpolation and bounded Lebesgue constants, not this random-noise law. Thus almost-sure unisolvency, high-probability norming, and deterministic interpolation stability are not stronger statements yielding the claimed sharp \(t^{-2}\) coefficient.

## Limitations

The result gives a fixed-degree tail law for exact one-dimensional polynomial interpolation with independent full-cell uniform jitter. Arbitrary correlated jitter, truncated nodes held away from cell boundaries, nonlinear robust reconstruction, multiple samples per cell, and extrapolation outside \([0,1]\) are not covered. Existing literature on worst-case near-collision instability could contain equivalent special cases; a complete publication-precedence guarantee is not asserted. No independent scientific audit has been conducted.

## References

- F. Dell'Accio, A. Sommariva, M. Vianello, *Random sampling and unisolvent interpolation by almost everywhere analytic functions*, arXiv:2303.14074 (first public 2023-03-24), https://arxiv.org/abs/2303.14074 ; lawful author preprint https://www.math.unipd.it/~marcov/pdf/unisolv.pdf.
- Y. Xu and A. Narayan, *Randomized weakly admissible meshes*, arXiv:2101.04043 (first public 2021-01-11), https://arxiv.org/abs/2101.04043.
- Z. Shen and K. Serkh, *On polynomial interpolation in the monomial basis*, arXiv:2212.10519 (first public 2022-12-20), https://arxiv.org/abs/2212.10519.
- D. Occorsio and W. Themistoclakis, *On the filtered polynomial interpolation at Chebyshev nodes*, arXiv:2008.00240 (first public 2020-08-01), https://arxiv.org/abs/2008.00240.
