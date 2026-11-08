# Distance-histogram rigidity of rectangular flat tori and sharp three-moment recovery

## Finding
Let \(d\ge3\). A rectangular Euclidean flat torus is
\[
T_{\boldsymbol a}=\mathbb R^d/(a_1\mathbb Z\oplus\cdots\oplus a_d\mathbb Z),\qquad a_i>0,
\]
with its intrinsic geodesic metric and normalized Riemannian volume. For independent uniform points \(X,Y\), write \(D=d_T(X,Y)\). The complete probability distribution of \(D\) determines the dimension and the unordered multiset of side lengths \(\{a_i\}\). A recursive zero-peeling reconstruction is given below.

In dimension three the **first three even-distance moments** \(\mathbb E[D^2]\), \(\mathbb E[D^4]\), \(\mathbb E[D^6]\) already determine the three side lengths, with repetitions allowed. The first two moments in this sequence do not suffice, even with known dimension three and positive side lengths.

## Assumptions and scope
The torus is formed from an orthogonal lattice with positive periods, not a general skew lattice. The metric is the shortest-path (intrinsic geodesic) distance on the quotient, not an extrinsic embedding distance. Sampling is independent and uniform under normalized volume. The results concern ideal exact distributions or exact moments. Dimension may be unknown for full-distribution reconstruction; the finite-moment assertion assumes dimension three.

Set \(s_i=a_i^2/4\), and let \(U_1,\ldots,U_d\) be independent uniform variables on \([-1,1]\). Coordinate differences modulo the rectangular lattice, represented in shortest centered intervals, are independent and uniform; hence
\[
D^2\ \overset{\mathrm{law}}=\ \sum_{i=1}^d s_iU_i^2.
\]

## Proof
### Full-distribution identification in every dimension
Put
\[
F(z)=\int_0^1\exp(zu^2)\,du={}_1F_1(1/2;3/2;z),\qquad
G(z)=\mathbb E[\exp(zD^2)]=\prod_{i=1}^dF(s_i z).
\]
These are entire functions because \(D\) and \(U_i\) are bounded. Moreover \(F(0)=1\) and \(|F(z)|\le\exp(|z|)\), so \(F\) has entire order at most one. Its first two logarithmic derivatives at zero are \(1/3\) and \(4/45\), respectively; consequently it is not \(\exp(Az+B)\). If \(F\) had no zeros, the zero-free case of the order-at-most-one Hadamard factorization would force \(F=\exp(Az+B)\), a contradiction. Therefore \(F\) has nonzero complex zeros. Since \(F(0)=1\), their moduli have a strictly positive attained minimum \(\rho\).

Differentiating under the integral and integrating the derivative of \(u\exp(zu^2)\) gives
\[
F(z)+2zF'(z)=\exp(z).
\]
If \(F(z_0)=0\), then \(z_0\ne0\) and \(F'(z_0)=\exp(z_0)/(2z_0)\ne0\), so every zero is simple. Let \(s_*\) be the maximum of the finitely many positive parameters, and let \(m\) be its multiplicity. Each factor \(F(s_i z)\) has nearest zero modulus \(\rho/s_i\). Thus the least zero modulus of \(G\) is \(r=\rho/s_*\), and at every zero of \(G\) of modulus \(r\), exactly the \(m\) factors with \(s_i=s_*\) vanish. Its complex multiplicity is therefore precisely \(m\). From exact \(G\), recover \(s_*=\rho/r\) and \(m\), divide \(G\) by \(F(s_*z)^m\), and repeat. This terminates at the constant function one and produces the complete multiset of parameters, including repeated ones. The number of recovered parameters is \(d\), and \(a_i=2\sqrt{s_i}\).

### Three-dimensional finite-moment recovery
For \(W=U^2\) with \(U\) uniform on \([-1,1]\), its first three raw moments are \(1/3\), \(1/5\), and \(1/7\). Its first three cumulants are
\[
\kappa_1(W)=\frac13,\qquad \kappa_2(W)=\frac4{45},\qquad \kappa_3(W)=\frac{16}{945}.
\]
With \(Z=D^2\), independence and cumulant scaling give
\[
\kappa_j(Z)=\kappa_j(W)\sum_{i=1}^3s_i^j,\qquad j=1,2,3.
\]
The cumulants are computable from the supplied three raw moments. Define
\[
q_1=3\kappa_1(Z),\qquad q_2=\frac{45}{4}\kappa_2(Z),\qquad q_3=\frac{945}{16}\kappa_3(Z).
\]
The sought parameters are all positive roots, with multiplicities, of
\[
t^3-q_1t^2+\frac{q_1^2-q_2}{2}t-\frac{q_1^3-3q_1q_2+2q_3}{6}=0.
\]
The unordered positive roots uniquely determine the periods.

For sharpness, the positive triples \(\boldsymbol s=(1,2,3)\) and \(\boldsymbol s'=(17/7,19/7,6/7)\) both have first power sum \(6\) and second power sum \(14\), but their third power sums differ. Therefore their \(\mathbb E[D^2]\) and \(\mathbb E[D^4]\) agree, although their period multisets \(\{2\sqrt{s_i}\}\) differ. Thus two initial even-distance moments are insufficient in dimension three.

## Verification
Run `python torus_distance_verifier.py` with Python, NumPy, and mpmath. The verifier reconstructs first-three cumulants from exact rational arithmetic, checks the cubic on four positive examples including repeated periods, checks the exact two-moment ambiguity, numerically checks the differential identity at complex points, locates illustrative zeros of the entire function, and simulates independent uniformly sampled point pairs on a rectangular three-torus. The output in the inspected package was:

```
VERIFY_OK exact_cumulants=3 exact_inverse_shapes=4 exact_two_moment_counterexample=1 complex_zero_samples=6 monte_carlo_pairs=120000
```

The infinite uniqueness theorem follows from the analytic proof, **not** from finitely many computed zeros or sampled pairs. Numerical root searches do not establish the global least zero modulus.

## Relationship to prior work
Boutin and Kemper (2003) study reconstructibility of **finite point configurations** from unlabeled Euclidean pair distances. Their setting does not imply reconstructibility of a continuous quotient metric using independent intrinsic-geodesic distances; it motivates the historical inverse question.

Osada et al. (2002) introduce shape distributions from sampled Euclidean geometric distances; their external-distance descriptors differ from the intrinsic flat-torus distribution here.

Mémoli and Needham (first publicly posted in 2018, journal 2022) formalize metric-measure distance distributions, including explicit **nonisometric skew flat two-tori** with identical distributions in their Example 3.18. This demonstrates why an orthogonality hypothesis is substantial. Their inspected manuscript does not provide full-distribution rigidity for rectangular tori in arbitrary dimension or the sharp three-dimensional moment budget. The new claim is deliberately confined to the rectangular family (and dimension at least three); it does not assert uniqueness among skew lattices or all flat tori. Existing two-dimensional results are not claimed as new.

## Limitations
No statement is made about nonorthogonal lattice quotients, arbitrary flat tori, finite-sample statistical stability, optimal noisy reconstruction, or numerical conditioning of complex-zero peeling. The exact infinite-dimensional zero-based reconstruction can be severely ill-conditioned. A historical-priority comparison is based on identified literature and indexed records and is not an independent exhaustive bibliographic certification.

## References
- M. Boutin and G. Kemper, *On reconstructing n-point configurations from the distribution of distances or areas*, arXiv:math/0304192, first public 15 April 2003. https://arxiv.org/abs/math/0304192
- R. Osada et al., *Shape Distributions*, ACM Transactions on Graphics 21 (2002). https://www.cs.princeton.edu/~chazelle/pubs/ShapeDistributions.pdf
- F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646, first public 23 October 2018; Studies in Applied Mathematics 149 (2022), 943–1001. https://arxiv.org/html/1810.09646v5
