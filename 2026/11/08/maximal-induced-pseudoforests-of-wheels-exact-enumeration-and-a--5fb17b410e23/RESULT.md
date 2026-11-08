# Maximal induced pseudoforests of wheels: exact enumeration and a gapped deletion spectrum

## Finding
For every integer \(n\ge 3\), let \(W_{n+1}=K_1\vee C_n\) be the wheel with its labelled rim in a fixed cyclic order. Let \(M_n(z)\) enumerate inclusion-maximal vertex sets inducing pseudoforests by their size:
\[
M_n(z)=\sum_{F:\,W_{n+1}[F]\text{ is an inclusion-maximal induced pseudoforest}}z^{|F|}.
\]
Then
\[
\boxed{M_n(z)=z^n+2\mathbf{1}_{2\mid n}z^{1+n/2}
+n\sum_{k=\lceil(n+2)/3\rceil}^{\lfloor(n+1)/2\rfloor}
\binom{k-1}{n-2k+1}z^{k+1}.}
\]
Here the parity contribution is present only for even \(n\), so every exponent is integral. Equivalently, the complete rational bivariate ordinary generating function is
\[
\boxed{\sum_{n\ge3}M_n(z)x^n=
\frac{z^3x^3}{1-zx}+\frac{2z^3x^4}{1-zx^2}
+x\frac{\partial}{\partial x}\left(\frac{z^3x^3(1+x)}{1-zx^2(1+x)}\right).}
\]
The cardinalities of inclusion-minimal vertex sets whose deletion leaves a pseudoforest are **exactly**
\[
\boxed{\{1\}\cup\{\lfloor n/2\rfloor,\lfloor n/2\rfloor+1,\ldots,n-\lceil(n+2)/3\rceil\}.}
\]
For \(n\ge6\), every cardinality from \(2\) through \(\lfloor n/2\rfloor-1\) is absent: an unbounded interval of missing minimal-solution sizes in a connected planar graph family. There are exactly \(n\) maximum-cardinality hub-containing induced pseudoforests for odd \(n\), and \(n(n-2)/2+2\) for even \(n\).

At \(z=1\), let \(\rho\in(0,1)\) be the positive root of \(\rho^2+\rho^3=1\), and \(\lambda=1/\rho\), the real root of \(\lambda^3-\lambda-1=0\). The total number obeys
\[
M_n(1)\sim\frac{n\lambda^n}{2\rho+3\rho^2}.
\]

## Assumptions and scope
All graphs are finite, undirected, and simple. A *pseudoforest* has at most one cycle in each connected component. The empty graph is a pseudoforest. An *inclusion-maximal induced pseudoforest* is a vertex subset \(F\) such that \(W_{n+1}[F]\) is a pseudoforest but adding any currently excluded vertex destroys this property. An *inclusion-minimal pseudoforest deletion set* is the complement of such an \(F\). Vertices on the rim are distinct and labelled; no quotient by rotational or reflectional symmetries is taken. The formulas include the triangular wheel \(W_4=K_4\).

## Proof
Write \(h\) for the hub and \(S\) for the selected rim vertices. The pseudoforest property is hereditary for induced subgraphs, so a feasible induced vertex subset is maximal exactly when adding each single excluded vertex makes it infeasible.

**Hub absent.** Every subset of the rim induces a disjoint union of paths or a cycle. Consequently the unique maximal feasible subset that omits \(h\) is the full rim. Adding \(h\) to the full rim gives cyclomatic number \(n>1\), so it is indeed maximal. This contributes \(z^n\).

**Hub present.** The graph induced by \(\{h\}\cup S\) is connected (when \(S\) is empty, it is a single vertex). It has \(|S|+1\) vertices and \(|S|+e(C_n[S])\) edges. Its cyclomatic number, edges minus vertices plus one, is therefore exactly \(e(C_n[S])\). Hence feasibility is equivalent to the induced rim having **at most one selected rim edge**. Maximality additionally demands that every omitted rim vertex, when added, create enough rim edges to make the total at least two.

If \(e(C_n[S])=0\), each omitted rim vertex must have **both** rim neighbors selected. Otherwise adding it creates at most one selected rim edge. The unique cyclic binary words with this property are the two alternating words, which exist precisely when \(n\) is even. They contribute \(2z^{1+n/2}\). (For the triangular rim the condition is impossible.)

If \(e(C_n[S])=1\), every omitted rim vertex must have at least one selected rim neighbor. This condition is equivalent to every maximal cyclic zero-run having length one or two. The selected binary word has a unique adjacent \(11\) pair and no other adjacent selected pair. Put \(k=|S|\). Starting at the first vertex of that unique clockwise \(11\), the word has \(k-1\) intervening zero-runs, each of length one or two, between the \(k-1\) selected blocks (one length-two block and \(k-2\) singleton blocks). If exactly \(t\) zero-runs have length two, then
\[
n=k+(k-1)+t=2k-1+t,\qquad 0\le t\le k-1.
\]
Thus \(\lceil(n+2)/3\rceil\le k\le\lfloor(n+1)/2\rfloor\). The unique ordered \(11\) pair has \(n\) possible positions, and choosing the \(t=n-2k+1\) long zero-runs among the \(k-1\) runs gives \(n\binom{k-1}{t}\) distinct labelled subsets, each with size \(k+1\) including the hub. This proves the coefficient formula without any symmetry division or overcounting.

For the rational generating function, the hub-free rim contributes \(z^3x^3/(1-zx)\), and the even alternating cases contribute \(2z^3x^4/(1-zx^2)\). Before weighting by the \(n\) choices of unique \(11\) position, the single-edge cases have generating function
\[
\sum_{k\ge2}z^{k+1}x^{2k-1}(1+x)^{k-1}
=\frac{z^3x^3(1+x)}{1-zx^2(1+x)}.
\]
Applying \(x\partial/\partial x\) introduces the correct factor \(n\), proving the bivariate identity.

The complements of maximal feasible subsets are precisely inclusion-minimal pseudoforest vertex-deletion sets. The full rim yields the singleton deletion \(\{h\}\). The hub-containing sets have sizes \(k+1\), with every integer \(k\) in the interval just derived attainable, because \(0\le t\le k-1\). Complementing against \(n+1\) vertices gives exactly the stated second interval. Its lower endpoint is \(n-\lfloor(n+1)/2\rfloor=\lfloor n/2\rfloor\). The two alternating words (when present) have exactly the maximum size already covered by \(k=\lfloor(n+1)/2\rfloor\). At this maximum, the binomial sum has exactly \(n\) cases when \(n\) is odd; for even \(n\), it has \(n(n/2-1)\) cases plus two alternations. For \(n=3\) the full rim and the hub-containing sets all have three vertices, but are distinct and counted correctly.

Finally, specializing the generating function at \(z=1\), the sole exponentially dominant contribution is \(x\partial_x G(x)\), where \(G(x)=x^3(1+x)/(1-x^2-x^3)\). The unique root of minimum modulus of \(1-x^2-x^3\) is the positive root \(\rho\), since equality in the triangle inequality for the \(x^2,x^3\) terms forces a common phase and their coprime exponents force phase zero. At the simple pole, \(G(x)\sim(2\rho+3\rho^2)^{-1}(1-x/\rho)^{-1}\). Coefficient extraction after applying \(x\partial_x\) proves the claimed asymptotic; the hub-free and alternating contributions are bounded as \(n\to\infty\).

## Verification
The standard-library program `verify.py` independently constructs wheel graphs and tests the pseudoforest property component by component through the inequality that each component's number of edges does not exceed its number of vertices. It tests inclusion-maximality by attempting to insert every excluded vertex. It compares all resulting cardinality distributions with the proved closed formula for \(3\le n\le16\), then checks the rational-generating-function recurrence, complete deletion-size spectrum, and extremal multiplicities for \(3\le n\le180\). The finite checks examined 262,114 nonempty induced vertex subsets, including 1,504 maximal induced pseudoforests, and tested rational coefficients through rim order 180. These are finite cross-checks rather than proofs of unrestricted validity. The exact execution output and instructions are in `VERIFICATION.md`; to reproduce, run `python verify.py` with Python 3.10 or later in the directory containing the extracted file.

## Relationship to prior work
Pseudoforest vertex deletion is a standard graph-optimization problem. The 2015/2018 treatment by Philip, Rai and Saurabh develops uniform kernelization and fixed-parameter algorithms; Gowda, Lonkar, Panolan, Patel and Saurabh's first publicly posted version of their improved algorithms is dated September 26, 2020 (arXiv:2009.13949). Their results concern existence of bounded-size deletions, not a complete labelled enumeration of **all inclusion-minimal** deletion sets of wheels. Sheng and Gutin's subsequent work on generalized feedback vertex-set algorithms likewise does not state the wheel distribution. An edge-maximal spanning pseudoforest (a bicircular-matroid basis) is a distinct object from an inclusion-maximal *vertex-induced* pseudoforest. These comparisons are differences of mathematical implications, not a claim that failed search proves priority.

## Limitations
This is a theorem for wheel graphs only; it does not give a universal formula for arbitrary apex graphs. The coefficients count distinct labelled vertex subsets, not isomorphism classes. The originality comparison is best-knowledge based on inspected accessible primary text and record searches, not an independently certified exhaustive literature classification. The numerical checks are finite. Independent mathematical audit has not been performed.

## References
1. K. N. Gowda, A. Lonkar, F. Panolan, V. Patel, S. Saurabh, *Improved FPT Algorithms for Deletion to Forest-Like Structures*, arXiv:2009.13949 (first public September 26, 2020); ISAAC 2020, DOI: 10.4230/LIPIcs.ISAAC.2020.34.
2. G. Philip, A. Rai, S. Saurabh, *Generalized Pseudoforest Deletion: Algorithms and Uniform Kernel*, SIAM J. Discrete Math. 32 (2018), 882–901, DOI: 10.1137/16M1100794; preliminary conference version MFCS 2015.
3. B. Sheng, G. Gutin, *Fixed Parameterized Algorithms for Generalized Feedback Vertex Set Problems*, Theor. Comput. Sci. 953 (2023), DOI: 10.1016/j.tcs.2023.113798.
