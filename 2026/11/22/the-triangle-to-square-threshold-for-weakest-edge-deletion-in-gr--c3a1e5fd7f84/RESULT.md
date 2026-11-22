# The triangle-to-square threshold for weakest-edge deletion in graph heat flow

## Finding

For a connected weighted undirected graph with combinatorial Laplacian \(L\), let \(L_{-e}\) be the Laplacian after removing an edge without changing the other conductances. For a deletion leaving the graph connected define the **integrated heat-trajectory error**
\[
\mathcal E_L(e)=\int_0^\infty\!\left\|e^{-tL}-e^{-tL_{-e}}\right\|_F^2\,dt.
\]
The time scale is fixed by the original conductances; no separate normalization is made after deletion. On **every positively weighted triangle**, \(\mathcal E_L(e)\) is minimized exactly at the smallest-weight edge(s), with strict preference whenever edge weights differ. This fails already on the four-cycle: with cyclic edge weights \((100,10,11,11)\), deletion of the edge of weight \(11\) between vertices \(2\) and \(3\) uniquely minimizes \(\mathcal E_L\), strictly beating the unique weakest edge of weight \(10\). Therefore the four-cycle is the smallest simple cycle on which weakest-edge deletion can be suboptimal for this metric.

## Assumptions and scope

Graphs are finite, simple, undirected, with strictly positive symmetric conductances, and the evolution is the continuous-time linear ODE \(\dot u=-Lu\) on real vertex states. The vertex set and all retained conductances are unchanged upon removal. The cycle has three or four vertices, and each one-edge deletion is connected, making the integral finite. The Frobenius error is also the expected squared trajectory discrepancy for isotropic mean-zero random initial states of covariance equal to the orthogonal projector onto \(\mathbf1^\perp\). The criterion is not a spectral-gap, effective-resistance, or fixed-time criterion; the conclusion does not assert anything about more general graph classes.

## Proof

**1. Exact time integral.** For either connected graph Laplacian \(L\) or \(K\), let \(Q\) be the \(n\times(n-1)\) matrix with columns \(e_i-e_{n-1}\) for \(0\le i<n-1\), and set \(G=Q^\top Q\), \(M=G^{-1}Q^\top LQ\), \(N=G^{-1}Q^\top KQ\). These are the matrices of the restricted operators on \(\mathbf1^\perp\), in the common, possibly nonorthonormal basis. Both have strictly positive real spectra. The trace of any endomorphism is basis independent. The matrix
\[
Z=\int_0^\infty e^{-tM}e^{-tN}\,dt
\]
is the unique solution of the Sylvester equation \(MZ+ZN=I\). This follows by differentiating the integrand and using its decay at infinity. Expanding the squared Frobenius error, using symmetry of the original Laplacians and cyclicity of trace, gives the exact identity
\[
\mathcal E(L,K)=\tfrac12\operatorname{tr}(M^{-1})+\tfrac12\operatorname{tr}(N^{-1})-2\operatorname{tr}(Z).
\tag{1}
\]
For rational conductances (1) involves only exact rational linear algebra.

**2. Triangle ordering.** Label triangle edges \((0,1),(1,2),(0,2)\) by positive weights \(a,b,c\), respectively, and call the errors from deletion of \(a,b,c\) by \(E_a,E_b,E_c\). Substituting their Laplacians into (1), and clearing positive denominators, yields the exact identity
\[
E_b-E_a=\frac{(b-a)P(a,b,c)}{3ab\,U(a,b,c)V(a,b,c)},
\tag{2}
\]
where the explicit polynomials \(P,U,V\), with **strictly positive coefficients in every present monomial**, are recorded in `FACTOR_CERTIFICATE.md`. Both sides of (2) are identical rational functions, verified by exact coefficient arithmetic in `CHECK.py`; it also independently reconstructs the Sylvester equation. In particular, \(\operatorname{sgn}(E_b-E_a)=\operatorname{sgn}(b-a)\). Any transposition of the three triangle edges is induced by relabeling triangle vertices, so the same comparison holds for every edge pair. Hence the minimum error occurs exactly at the minimum edge conductance, with equality precisely for tied weights.

**3. Four-cycle obstruction.** Label vertices cyclically \(0,1,2,3\), with edge conductances \((100,10,11,11)\) on \((0,1),(1,2),(2,3),(3,0)\). Applying (1) yields the exact rational errors, in this edge order:
\[
\begin{aligned}
E_0&=\frac{1436863131833465}{20857430364786048},\\
E_1&=\frac{12484655540506124917}{629870805581225287200},\\
E_2&=\frac{38496709664197}{2114507504264100},\\
E_3&=\frac{827146948257857}{35144400164887200}.
\end{aligned}
\]
Exact cross-multiplication gives \(E_2<E_1<E_3<E_0\). In particular
\[
E_1-E_2=\frac{18976950041406901787484663}{11750543650483124820155055200}>0.
\]
The weakest edge is index \(1\) (conductance \(10\)); the uniquely optimal deletion is index \(2\) (conductance \(11\)). As the triangle is the only smaller simple cycle, this is the first possible cycle size for failure. \(\square\)

## Verification

`CHECK.py` independently builds the Laplacian restrictions, constructs and solves the Sylvester equations over \(\mathbb Q\) and \(\mathbb Q(a,b,c)\), verifies the two symbolic triangle comparison identities by exact rational equality, and checks strict positivity of all coefficients in the resulting numerator and denominator polynomials. It reproduces all four rational four-cycle errors and their ordering. Run with `python CHECK.py`; Python 3 and SymPy are the only dependencies. No finite sampling is used to infer the global triangle theorem.

## Relationship to prior work

The 2025 preprint by D'Inverno, Ajavon, and Brugiapaglia treats diffusion equations over weighted graphs and surrogate solutions, motivating quantitative fidelity under altered network structure. Krishnagopal's 2026 spectral-sparsifier work proves filter and representation stability under spectral approximation, rather than selecting one edge by the full-time trajectory integral. Bravo-Hermsdorff and Gunderson formulate sparsification/coarsening through pseudoinverse preservation. The November 2026 study of Fitz-Gibbon and colleagues develops an integrated diffusion spectral-error objective and broader sparsification algorithms; its first public date follows the frozen source window and it is compared here only as potential prior coverage, not used as the qualifying source. Its general evaluation formula is compatible with (1), but the inspected material did not establish the all-weight triangle optimality theorem or the explicit four-cycle reversal. The contribution claimed here is the sharp **minimum cycle size** and its universal three-edge boundary under this particular trajectory error, not the invention of heat fidelity or Sylvester integration.

## Limitations

This is a self-review, not an independent expert audit. There may exist unlocated earlier numerical examples or special-case graph-sparsification results. The result concerns a deliberately fixed comparison: deleting one edge without reweighting or renormalizing while keeping connectivity; it does not automatically extend to joint edge deletions, arbitrary graphs, directed diffusion, or normalized Laplacians. The symbolic certificate is finite and exactly reproducible; the mathematical argument proving it applies to all positive real conductances is the rational identity and coefficient-positivity argument, not numerical sampling.

## References

- D'Inverno, G. A., Ajavon, K., and Brugiapaglia, S., *Surrogate models for diffusion on graphs via sparse polynomials*, arXiv:2502.06595, first publicly posted 2025-02-10; journal open-access version at https://doi.org/10.1007/s10915-026-03353-1.
- Krishnagopal, S., *Spectral Graph Sparsification Preserves Representation Geometry in Graph Neural Networks*, arXiv:2605.01136, first publicly posted 2026-05-01.
- Bravo-Hermsdorff, G. and Gunderson, L. M., *A Unifying Framework for Spectrum-Preserving Graph Sparsification and Coarsening*, arXiv:1902.09702 (2019).
- Fitz-Gibbon, E., Jerdee, M., Zhang, Y., Braun, R., and Moore, C., *Dynamics-preserving graph sparsification*, arXiv:2611.23176, first publicly posted 2026-11-17 (considered for overlap, not the qualifying literature source).
