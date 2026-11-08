# A sharp Padé positivity horizon for strongly regular graph diffusion

## Finding

Let \(G\) be any finite simple connected noncomplete strongly regular graph with parameters \((N,k,\lambda,\mu)\), using the ordinary unweighted combinatorial Laplacian \(L=kI-A\). Define the fourth-order, two-stage Gauss–Legendre heat update
\[
T(h)=F(hL),\qquad F(z)=\frac{z^2-6z+12}{z^2+6z+12},\qquad h\ge0.
\]
Put
\[
s=2k-\lambda+\mu,\qquad p=k(k-\lambda+\mu-1)+\mu=N\mu>0.
\]
Then the following sharp alternative holds:

* If \(s\ge N\), the matrix \(T(h)\) is entrywise nonnegative for every \(h\ge0\), and strictly positive entrywise for every \(h>0\).
* If \(s<N\), define
\[
h_* = \frac{3+\sqrt{9+12N(N-s)/p}}{N-s}.
\]
Equivalently, \(h_*=[3+\sqrt{9+12(N-s)/\mu}]/(N-s)\). Then \(T(h)\) is entrywise nonnegative if and only if \(0\le h\le h_*\). It is entrywise strictly positive for \(0<h<h_*\); at \(h=h_*\), exactly its entries indexed by adjacent distinct vertices vanish; and for every \(h>h_*\), exactly those adjacent entries are negative. All diagonal and nonadjacent-distinct-vertex entries are strictly positive for every \(h>0\).

For every step size, \(T(h)\) has row and column sums equal to one. The exact classification depends only on the four strongly regular parameters, not on the isomorphism type of the graph.

## Assumptions and scope

A strongly regular graph with parameters \((N,k,\lambda,\mu)\) is a simple \(k\)-regular graph on \(N\) vertices in which every adjacent distinct pair has exactly \(\lambda\) common neighbors and every nonadjacent distinct pair exactly \(\mu\) common neighbors. We assume connectedness and \(0<k<N-1\), so both adjacency and nonadjacency occur and the Laplacian has three distinct eigenvalues \(0<\alpha<\beta\) in addition to the zero eigenvalue. The equality \(s=\alpha+\beta\), \(p=\alpha\beta\) follows from the familiar strongly regular adjacency quadratic. No positivity is asserted for the internal Runge–Kutta stages, or for arbitrary weighted or directed graphs.

The update is the scalar rational stability function of the unmodified fourth-order Gauss–Legendre method applied to \(u'(t)=-Lu(t)\), not a polynomial Taylor truncation or a Crank–Nicolson update.

## Proof

Write \(E_0=J/N\), \(E_\alpha\), and \(E_\beta\) for the mutually orthogonal spectral projectors of \(L\). Since \(G\) is connected,
\[
E_\alpha+E_\beta=I-J/N,\qquad
\alpha E_\alpha+\beta E_\beta=L.
\]
Let \(\delta=\beta-\alpha>0\). For two distinct vertices \(i,j\), solving these two projector identities gives
\[
(E_\alpha)_{ij}=\begin{cases}
(1-\beta/N)/\delta,&i\sim j,\\
-\beta/(N\delta),&i\not\sim j.
\end{cases}
\]
In the first line \(i\sim j\) means an edge, while \(i\not\sim j\) in the second means two distinct nonadjacent vertices. These values, together with the two projector identities, determine all off-diagonal entries of every function of \(L\).

Define \(D_\gamma(h)=12+6\gamma h+\gamma^2h^2\) for \(\gamma\in\{\alpha,\beta\}\). Both are strictly positive on \(h\ge0\), and the exact identity
\[
F(h\gamma)-1=-\frac{12h\gamma}{D_\gamma(h)}
\]
allows direct substitution into the projectors. For distinct nonadjacent \(i,j\), cancellation of the linear terms yields
\[
T(h)_{ij}=\frac{12\alpha\beta h^2[6+(\alpha+\beta)h]}{N D_\alpha(h)D_\beta(h)}.
\]
It is strictly positive for every \(h>0\). For adjacent \(i,j\), the same substitution gives
\[
T(h)_{ij}=\frac{12h}{D_\alpha(h)D_\beta(h)}
\left[12+\frac{6\alpha\beta}{N}h+
\frac{\alpha\beta(\alpha+\beta-N)}{N}h^2\right].
\]
The expression is independent of the chosen edge, as is the nonedge expression above.

The rational stability function is positive on the entire nonnegative real axis: its numerator \(z^2-6z+12=(z-3)^2+3\) is positive, and its denominator is positive. As every orthogonal spectral projector has nonnegative diagonal,
\[
T(h)_{ii}=\frac1N+F(h\alpha)(E_\alpha)_{ii}
+F(h\beta)(E_\beta)_{ii}>0
\]
for every \(h\ge0\) and vertex \(i\).

Since \(\alpha\beta=p>0\) and \(\alpha+\beta=s\), the sign of each adjacent entry for \(h>0\) is the sign of
\[
Q(h)=\frac{12N}{p}+6h+(s-N)h^2.
\]
For \(s\ge N\), all terms are nonnegative and the constant is positive; therefore every edge entry is positive. For \(s<N\), this quadratic has a negative leading coefficient, a positive value at zero, and exactly one positive root, namely \(h_*\) as stated. It is positive before that root, zero there, and negative thereafter. Together with the nonedge and diagonal formulas, this proves the full entrywise classification, including all boundary cases. Finally \(L\mathbf1=0\) and \(F(0)=1\), so \(T(h)\mathbf1=\mathbf1\); symmetry gives column sums one.

The identity \(p=N\mu\) follows from the standard two-walk count \((N-k-1)\mu=k(k-\lambda-1)\), obtained by counting neighbors of a fixed vertex reached through two edges and ending at nonneighbors. The other parameter identities follow from the two nontrivial adjacency eigenvalues \(r,t\), which obey \(r+t=\lambda-\mu\) and \(rt=\mu-k\). Their Laplacian counterparts are \(k-r\) and \(k-t\), with sum \(2k-\lambda+\mu=s\) and product \(k(k-\lambda+\mu-1)+\mu=p\), completing the proof without an unspecified spectral normalization.

As concrete consequences, the Petersen graph has \((N,k,\lambda,\mu)=(10,3,0,1)\), so \((s,p)=(7,10)\) and \(h_*=1+\sqrt5\). For the triangular graph on unordered pairs from an \(n\)-element set, \(n\ge4\), one has \(N=n(n-1)/2\), \((\alpha,\beta)=(n,2n-2)\); unconditional positivity holds precisely for \(n\le6\), whereas for \(n\ge7\) the sharp root is
\[
h_* =\frac{6+\sqrt{36+6(n^2-7n+4)}}{n^2-7n+4},\qquad
\lim_{n\to\infty}nh_*=\sqrt6.
\]
For every Paley graph of admissible prime-power order \(N\equiv1\pmod4\), \(s=N\), giving unconditional strict positivity for positive timesteps. The rook graph on a \(4\)-by-\(4\) board and the Shrikhande graph have the same parameters \((16,6,2,2)\), hence the same exact cutoff \((3+\sqrt{33})/4\).

## Verification

The accompanying standalone script `check.py` uses only Python's standard library and exact rational arithmetic. Running `python3 check.py` constructs seven graphs (Petersen, triangular graphs for three orders, rook graphs for two orders, and Shrikhande), derives their parameters from adjacency matrices, independently evaluates the original rational matrix update by fraction-preserving Gaussian elimination, and checks the proved formulas for 8,172 off-diagonal entries at six rational positive timesteps each in the aggregate. It also checks all row sums, positive diagonals, and exact eigenvalue-parameter relations.

Exact computation validates the selected finite examples and the derived rational identities on those graphs. The general statement for every strongly regular graph, every allowed parameter tuple, and every real timestep follows from the symbolic spectral projector proof above, not from enumeration or numerical approximation.

## Relationship to prior work

Lóczi and Ketcheson (first publicly posted March 26, 2013) study rational stability functions and absolute-monotonicity radii for Runge–Kutta methods. Their analysis concerns method-level positivity criteria and does not evaluate the complete strongly regular graph family with a sharp graph-parameter threshold. Zappavigna, Colaneri, Kirkland, and Shorten study positivity failures of diagonal Padé approximations and give sufficient criteria for certain Metzler systems; their analyzed counterexample is a directed nilpotent chain, not this symmetric graph-Laplacian classification. Lin and Weng develop strongly regular Laplacian eigenvalue relations, which supply the established spectral background used here, not an exact Gauss–Legendre positivity horizon.

Related graph-heat results on explicit RK4, complete multipartite graphs, Hamming graph products, and windmill graphs use either different integrators or more restricted graph families. The Cartesian-product statement already covers the rook graph special cases; the complete-multipartite statement already covers some unconditionally positive special cases. Those overlaps are not treated as separate new claims here. The present claim is the exact general strongly regular graph criterion, including examples such as the Petersen and triangular families and a single parameter-law for all adjacency types. The method-specific eight-state Padé Markov-chain obstruction is directed and does not imply this exact reversible-graph classification.

## Limitations

The result is restricted to connected, simple, unweighted, noncomplete strongly regular graphs and the completed fourth-order Gauss–Legendre endpoint update. It does not imply unconditional positivity for all regular graphs, all Markov generators, or internal Runge–Kutta stages. The zero-timestep transition matrix is the identity and therefore has zero off-diagonal entries; strict entrywise positivity is asserted only for strictly positive timesteps in the permitted range. Literature and database searching cannot establish absolute publication priority; older special-function or association-scheme results could contain an equivalent formulation.

## References

1. L. Lóczi and D. I. Ketcheson, *Rational functions with maximal radius of absolute monotonicity*, arXiv:1303.6651, first public version March 26, 2013. https://arxiv.org/abs/1303.6651
2. A. Zappavigna, P. Colaneri, S. Kirkland, and R. Shorten, *Essentially Negative News About Positive Systems*, openly available manuscript, displayed date January 3, 2012. https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf (displayed manuscript date is not used as verified first-public date).
3. F.-H. Lin and C.-W. Weng, *Strongly Regular Graphs as Laplacian Extremal Graphs*, arXiv:1411.6532, first public version November 24, 2014. https://arxiv.org/abs/1411.6532
