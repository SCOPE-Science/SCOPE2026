# Exact two-adic valuation of spinor-variety degrees
## Finding
For each integer \(n\ge1\), let
\[
S_n=\operatorname{OG}(n+1,2n+2)
\]
be either connected component of the variety of maximal isotropic \(n+1\)-planes in a complex quadratic vector space of dimension \(2n+2\). Equip \(S_n\) with its minimal homogeneous embedding in a projectivized half-spin representation. Its complex dimension is
\[
M=\frac{n(n+1)}2.
\]
Let \(s_2(m)\) denote the number of ones in the binary expansion of a nonnegative integer \(m\). Then
\[
\deg S_n
=
\frac{M!\prod_{a=2}^{n-1}a!}{\prod_{a=2}^{n}(2a-1)!},
\]
and the exact two-adic valuation is
\[
\boxed{\nu_2(\deg S_n)=n-s_2\!\left(\frac{n(n+1)}2\right)}.
\]

In particular,
\[
\deg S_n\text{ is odd}\quad\Longleftrightarrow\quad n\in\{1,2\},
\]
and
\[
\deg S_n\equiv2\pmod4
\quad\Longleftrightarrow\quad
n\in\{3,5\}.
\]
Thus the six-dimensional spinor quadric has degree \(2\), the spinor tenfold has degree \(12\), and the fifteen-dimensional spinor variety has degree \(286\); after these small cases the exact power of two dividing the degree is controlled by the binary digit sum of the triangular number \(n(n+1)/2\).

Equivalently, a transverse linear section of complementary codimension in the minimal half-spin embedding consists of exactly \(\deg S_n\) complex points counted with multiplicity, so its enumerative count is divisible by
\[
2^{\,n-s_2(n(n+1)/2)},
\]
and by no higher universal power of two.

## Assumptions and scope
The ground field is \(\mathbb C\). The degree is taken in the minimal half-spin embedding, not in the Pluecker embedding. The latter is obtained from the minimal embedding by a quadratic Veronese map, so confusing the two polarizations changes the degree.

The two connected components of the maximal orthogonal Grassmannian are isomorphic and have the same degree. The indexing is chosen so that \(S_n=\operatorname{OG}(n+1,2n+2)\) has dimension \(n(n+1)/2\), matching the strict-partition staircase \((n,n-1,\ldots,1)\).

## Proof
Kresch and Tamvakis describe the classical cohomology of \(\operatorname{OG}(n+1,2n+2)\) by Schubert classes \(\tau_\lambda\) indexed by strict partitions \(\lambda\) contained in the staircase
\[
\rho_n=(n,n-1,\ldots,1).
\]
The codimension-one class \(\tau_1\) is the positive generator of the Picard group, hence the hyperplane class for the minimal half-spin embedding. Their classical Pieri rule says that multiplication by \(\tau_k\) adds a horizontal strip with coefficient \(2^{N'(\lambda,\mu)}\). For \(k=1\), the strip is one box and \(N'(\lambda,\mu)=0\), so every allowed one-box step has coefficient one.

It follows that the coefficient of the top class \(\tau_{\rho_n}\) in \(\tau_1^M\), hence \(\deg S_n\), is the number of saturated chains of strict partitions from the empty partition to \(\rho_n\). These chains are exactly the standard shifted tableaux of staircase shape \(\rho_n\).

The shifted hook-length formula, equivalently Schur's product formula for a strict partition \(\lambda=(\lambda_1>\cdots>\lambda_\ell>0)\), gives
\[
g^\lambda
=
\frac{|\lambda|!}{\prod_i\lambda_i!}
\prod_{i<j}\frac{\lambda_i-\lambda_j}{\lambda_i+\lambda_j}.
\]
For \(\lambda=\rho_n\), the numerator difference product is
\[
\prod_{1\le b<a\le n}(a-b)=\prod_{a=1}^n(a-1)!,
\]
while
\[
\prod_{1\le b<a\le n}(a+b)
=
\prod_{a=2}^n\frac{(2a-1)!}{a!}.
\]
After cancellation one obtains
\[
\deg S_n
=
\frac{M!\prod_{a=2}^{n-1}a!}{\prod_{a=2}^{n}(2a-1)!}.
\]

Now use Legendre's identity
\[
\nu_2(m!)=m-s_2(m).
\]
Applying it to the factorial quotient gives
\[
\nu_2(\deg S_n)
=
\nu_2(M!)
+
\sum_{a=2}^{n-1}\nu_2(a!)
-
\sum_{a=2}^{n}\nu_2((2a-1)!).
\]
The linear terms cancel because
\[
M+\sum_{a=2}^{n-1}a
=
\sum_{a=2}^{n}(2a-1)
=
n^2-1.
\]
For the binary terms, use
\[
s_2(2a-1)=s_2(a-1)+1.
\]
Therefore
\[
\begin{aligned}
\nu_2(\deg S_n)
&=-s_2(M)-\sum_{a=2}^{n-1}s_2(a)
+\sum_{a=2}^{n}s_2(2a-1)\\
&=-s_2(M)-\sum_{a=2}^{n-1}s_2(a)
+\sum_{b=1}^{n-1}s_2(b)+(n-1)\\
&=n-s_2(M).
\end{aligned}
\]
This proves the valuation formula.

For the residue classifications, direct evaluation gives valuations
\[
0,0,1,2,1,3
\]
for \(n=1,2,3,4,5,6\). For \(n\ge7\),
\[
\frac{n(n+1)}2<2^{n-2},
\]
starting at \(n=7\), and the inequality propagates because \((n+2)/n<2\). Hence \(s_2(M)\le n-2\), so the valuation is at least two. This proves both the oddness and modulo-four assertions.

## Verification
The bundled exact checker evaluates the factorial quotient with arbitrary-precision integers and verifies
\[
\nu_2(\deg S_n)=n-s_2(n(n+1)/2)
\]
for \(1\le n\le200\).

As an independent combinatorial replay for the geometric coefficient, it recursively counts all saturated chains in the strict-partition poset for \(1\le n\le15\) and checks equality with the factorial product. The state space is finite because strict partitions contained in \(\rho_n\) correspond to subsets of \(\{1,\ldots,n\}\).

The finite checks are regression evidence only. The infinite theorem follows from the classical one-box Pieri rule, the shifted hook-length formula, and Legendre's exact factorial valuation.

## Relationship to prior work
Kresch and Tamvakis provide the Schubert basis and Pieri rule for the maximal orthogonal Grassmannian. Manivel explicitly distinguishes the minimal half-spin embeddings of the two spinor components from their Pluecker embeddings. Fischer gives a bijective proof of the shifted hook-length formula used to evaluate the saturated-chain count.

The inspected sources do not state the closed two-adic identity
\[
\nu_2(\deg S_n)=n-s_2(n(n+1)/2),
\]
nor the resulting complete classifications of odd degree and degree congruent to \(2\pmod4\). Searches for the same statement using spinor-variety, orthogonal-Grassmannian, shifted-staircase-tableau, parity, and two-adic terminology did not locate a covering result.

A nearby body of work studies arithmetic and representation-theoretic properties of shifted tableaux in much greater generality. That literature supplies context but, in the material retrieved and inspected here, does not give this staircase spinor-degree valuation identity.

## Limitations
The theorem concerns the minimal homogeneous polarization. It does not claim an analogous formula for arbitrary embeddings or for non-maximal orthogonal Grassmannians.

The result determines only the two-adic valuation; it does not classify odd prime divisibility of the degree. The originality search cannot exclude an unindexed older observation obtained by combining the same classical formulas.

## References
Andrew Kresch and Harry Tamvakis, *Quantum cohomology of orthogonal Grassmannians*, arXiv:math/0306338, first submitted 24 June 2003; Compositio Mathematica 140 (2004), 482--500. Primary MSC 14M15.

Ilse Fischer, *A bijective proof of the hook-length formula for shifted standard tableaux*, arXiv:math/0112261, first submitted 23 December 2001.

Laurent Manivel, *On Spinor Varieties and Their Secants*, arXiv:0904.0565, first submitted 3 April 2009; SIGMA 5 (2009), 078. Primary MSC 14M17.
