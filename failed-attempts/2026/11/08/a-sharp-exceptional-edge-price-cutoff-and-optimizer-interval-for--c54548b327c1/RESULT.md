# A sharp exceptional-edge price cutoff and optimizer interval for fastest mixing on cycles

## Finding

Consider the undirected cycle \(C_n\), with \(n\ge5\), vertices \(1,\ldots,n\), consecutive edge conductances \(w_1,\ldots,w_{n-1}\ge0\), and closing-edge conductance \(z\ge0\). Each consecutive edge costs one unit per unit conductance, while the closing edge costs \(c>0\). Under budget \(B>0\), maximize the second-smallest eigenvalue \(\lambda_2(L)\) of the symmetric weighted combinatorial Laplacian subject to
\[
\sum_{i=1}^{n-1}w_i+cz\le B.
\]
Put \(C_n=(n-1)^2\) and \(\lambda_0=12B/[n(n^2-1)]\).

**Sharp screening law.** If \(c>C_n\), the unique optimizer deletes the closing edge and has
\[
z=0,\qquad w_i=\frac{\lambda_0}{2}i(n-i),\qquad \lambda_2^{\star}=\lambda_0.
\]
At \(c=C_n\), the optimal value is still \(\lambda_0\), but the **entire** optimizer set is the nontrivial closed interval
\[
0\le z\le\zeta_n,\qquad
w_i=\frac{\lambda_0}{2}i(n-i)-(n-1)z,
\]
where the explicit finite-dimensional generalized Rayleigh quotient below determines \(0<\zeta_n<\lambda_0/2\). If \(0<c<C_n\), the optimal value is **strictly larger** than \(\lambda_0\) and **every** optimizer funds the closing edge (\(z>0\)). No formula for all conductances in this low-price regime is asserted.

To specify the exact interval endpoint, define \(v_i=(n+1)/2-i\) and
\[
\mathcal H_n=\left\{f\in\mathbb R^n:\sum_i f_i=0,\ \sum_i f_iv_i=0\right\}.
\]
Then
\[
\boxed{\displaystyle
\zeta_n=\min_{\substack{f\in\mathcal H_n\\ f\ne0}}
\frac{\frac{\lambda_0}{2}\sum_{i=1}^{n-1}i(n-i)(f_i-f_{i+1})^2
-\lambda_0\sum_{i=1}^{n}f_i^2}
{(n-1)\sum_{i=1}^{n-1}(f_i-f_{i+1})^2-(f_n-f_1)^2}.}
\]
Both the numerator and denominator are strictly positive on nonzero \(\mathcal H_n\), so the displayed minimum is finite, positive and attained.

For the first new cycle size, \(n=5\), the closing-edge cutoff is \(c=16\), with \(\lambda_0=B/10\) and the *closed-form* optimizer interval
\[
\boxed{\displaystyle \zeta_5=\frac{10-\sqrt{10}}{20}\lambda_0
=\frac{10-\sqrt{10}}{200}B.}
\]
At \(c=16\), every optimal five-cycle has \((w_1,w_2,w_3,w_4)=(2\lambda_0-4z,3\lambda_0-4z,3\lambda_0-4z,2\lambda_0-4z)\) with precisely the stated range of \(z\). At the upper endpoint a second nonconstant eigenvalue reaches \(\lambda_0\), explaining the sharp limit of the optimal face.

## Assumptions and scope

All conductances are individually selectable nonnegative real numbers; zero conductance is allowed, and the graph must remain connected at an optimum because the optimal gap is positive. Costs are linear and positive. The Laplacian is \(L_{ii}=\sum_{j\sim i}w_{ij}\) and \(L_{ij}=-w_{ij}\) on an edge. Eigenvalues are sorted \(0=\lambda_1\le\lambda_2\le\cdots\le\lambda_n\), with multiplicity. The result is for continuous-time, symmetric, uniform-stationary diffusion; it is not the discrete-time stochastic-matrix SLEM problem. The \(n=4\) specialization was separately determined previously and is not claimed here.

## Proof

**1. Universal price-weighted upper bound.** The centered vector \(v\) has successive differences \(v_i-v_{i+1}=1\), closing difference \(v_1-v_n=n-1\), and norm
\[
N_n=\sum_{i=1}^n v_i^2=\frac{n(n^2-1)}{12}.
\]
By the Rayleigh variational principle, for arbitrary feasible nonnegative rates,
\[
\lambda_2(L)\le\frac{v^TLv}{N_n}
=\frac{\sum_iw_i+(n-1)^2z}{N_n}
\le\frac B{N_n}=\lambda_0
\quad\text{whenever }c\ge C_n.
\]
For \(c>C_n\), equality in both inequalities requires \(z=0\) and the full budget.

**2. Exact path certificate and its simple first eigenvalue.** Put \(w_i^0=\lambda_0 i(n-i)/2\), \(z=0\). The budget is \(\sum_iw_i^0=B\), and direct calculation gives \(L_0v=\lambda_0v\). To verify \(\lambda_0=\lambda_2(L_0)\), consider the tridiagonal Laplacian \(A_n\) with edge weights \(i(n-i)\), so \(L_0=\lambda_0 A_n/2\). Its action preserves the space of polynomials in the vertex index of degree at most \(k\), and on the monomial of degree \(k\) the leading coefficient is multiplied by \(k(k+1)\). In the polynomial basis of degrees \(0,\ldots,n-1\), the action is triangular, hence its full eigenvalue multiset is \(\{k(k+1):0\le k<n\}\). Therefore \(L_0\) has exact eigenvalues \(\lambda_0 k(k+1)/2\), so \(\lambda_0\) is a simple first positive eigenvalue. Step 1 proves global optimality of this path when \(c\ge C_n\). For \(c>C_n\), equality forces \(z=0\) and \(Lv=\lambda_0v\); the vertex equations determine each \(w_i=\lambda_0 i(n-i)/2\), proving uniqueness.

**3. Every optimizer at the boundary.** Let \(c=C_n\). Because \(\lambda_2^\star=\lambda_0\), any optimal design saturates the budget and the Rayleigh inequality. Hence \(Lv=\lambda_0v\). Solving these \(n\) linear vertex equations, using the closing-edge rate \(z\), gives uniquely
\[
w_i(z)=\frac{\lambda_0}{2}i(n-i)-(n-1)z\qquad(1\le i<n).
\]
The budget is automatically \(B\) for every \(z\) in this family. Positivity of all successive rates requires \(0\le z\le\lambda_0/2\). Set \(L(z)=L_0+zK\), with
\[
K=-(n-1)L(P_n,\mathbf1)+(e_1-e_n)(e_1-e_n)^T,
\]
where \(L(P_n,\mathbf1)\) is the unweighted path Laplacian. Both \(\mathbf1\) and \(v\) remain eigenvectors, of eigenvalues \(0\) and \(\lambda_0\), respectively. For \(f\in\mathcal H_n\),
\[
f^T(L(z)-\lambda_0 I)f
=\left[\frac{\lambda_0}{2}\sum_i i(n-i)(f_i-f_{i+1})^2-\lambda_0\|f\|^2\right]
-z\left[(n-1)\sum_i(f_i-f_{i+1})^2-(f_n-f_1)^2\right].
\]
The first square bracket is strictly positive for nonzero \(f\in\mathcal H_n\), by the spectral calculation in step 2. The second bracket is strictly positive by Cauchy–Schwarz; equality would force all successive differences equal, making \(f\) an affine combination of \(\mathbf1\) and \(v\), excluded by orthogonality. Thus \(\lambda_2(L(z))=\lambda_0\) exactly for \(0\le z\le\zeta_n\), with \(\zeta_n\) as in the finding. The upper endpoint is less than \(\lambda_0/2\): at \(z=\lambda_0/2\), the first and last consecutive rates are zero, while the closing rate is positive, disconnecting the vertices \(\{1,n\}\) from \(\{2,\ldots,n-1\}\); consequently \(\lambda_2=0\), while the vector \(v\) still has eigenvalue \(\lambda_0\). This proves the full interval, its nonzero length, and the sharp endpoint.

**4. The strict low-price side.** For any \(0<c<C_n\), take a boundary-optimal design with \(0<z<\zeta_n\). Its cost at price \(c\) is \(B-(C_n-c)z<B\). Scaling every rate by \(B/[B-(C_n-c)z]>1\) produces a feasible design whose gap is strictly larger than \(\lambda_0\). Conversely every design with \(z=0\) has gap at most \(\lambda_0\), by the same Rayleigh bound. Hence every optimizer at \(c<C_n\) has \(z>0\), completing the if-and-only-if edge-deletion threshold.

**5. Five-cycle radical.** On \(n=5\), put \(\lambda=\lambda_0\) and use the boundary family in step 3. A direct characteristic-polynomial determinant calculation gives, with spectral variable \(x\),
\[
\det(xI-L(z))=x(x-\lambda)(x-6\lambda+10z)
\bigl[x^2+(-13\lambda+20z)x+30\lambda^2-100\lambda z+80z^2\bigr].
\]
The first additional eigenvalue to cross \(\lambda\) comes from the quadratic factor and occurs at the smaller positive solution of \(9\lambda^2-40\lambda z+40z^2=0\), namely \(z=(10-\sqrt{10})\lambda/20\). The linear factor would cross later, at \(z=\lambda/2\); the other quadratic root also crosses later. Strict monotonicity of the quadratic form on \(\mathcal H_5\) from step 3 excludes any earlier crossing. This proves the stated radical endpoint.

## Verification

A standalone symbolic checker is included as `verify.py` (Python 3 with SymPy). It verifies the edge-budget identities and the common eigenvector for several symbolic cycle lengths, the full parabolic-path eigenvalues, the five-vertex characteristic-polynomial factorization and radical crossing, and exact rational sample matrices and the strict cost-improvement construction. The script reported `VERIFY_OK 178` in the completed replay. These finite replays check algebra and sample boundaries; the all-\(n\) assertions follow from the proof above, not from exhaustive enumeration.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006) formulated precisely this continuous-time edge-price spectral-gap optimization problem and its maximum-variance dual. Their Result 5 solves the path problem, and Section 5.3 solves uniform-price cycles and establishes a two-dimensional bound for arbitrary-price cycles, but does not state the exact one-defect cutoff, the all-size boundary optimizer interval or the five-cycle radical derived here. The path optimum and general Rayleigh/duality framework are credited, not claimed as new. Shafi, Arcak and El Ghaoui (2012) give a general Laplacian spectral-constraint design framework rather than this explicit price transition. Fiedler's earlier tree and minimax work is also relevant to the underlying spectral optimization, and may require further priority checking. The previously determined four-cycle instance is excluded from the new domain.

## Limitations

The low-price regime is characterized only by strict edge activation and strict improvement over the optimal path; the entire rate allocation and optimum value for \(c<C_n\) remain open in this result. The boundary endpoint has a finite-dimensional variational formula for general \(n\), not an elementary radical in every dimension. No independent mathematical audit has been performed. A complete priority assessment against unindexed or inaccessible early weighted-graph minimax literature remains outstanding; independent publication review is recommended before asserting first publication.

## References

1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699. Published electronically 2006-11-02. DOI: https://doi.org/10.1137/S0036144504443821. Author full-text PDF: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. S. Y. Shafi, M. Arcak and L. El Ghaoui, *Graph Weight Allocation to Meet Laplacian Spectral Constraints*, IEEE Transactions on Automatic Control 57 (2012), 1872–1877. DOI: https://doi.org/10.1109/TAC.2011.2181795. Author full-text PDF: https://people.eecs.berkeley.edu/~elghaoui/Pubs/Laplace_tac2012.pdf.
3. M. Fiedler, *Absolute algebraic connectivity of trees*, Linear and Multilinear Algebra 26 (1990), 85–106; *Some minimax problems for graphs*, Discrete Mathematics 121 (1993), 65–74. Full text of the latter was not obtained for comparison.
