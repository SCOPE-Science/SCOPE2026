# A quadratic closing-edge price boundary and its full optimal face for fastest diffusion on cycles

## Finding

For each integer \(n\geq3\), put \(S_n=n(n^2-1)/12\). Consider a cycle whose consecutive path edges \(\{i-1,i\}\), \(1\leq i\leq n-1\), have independently selectable conductances \(w_i\geq0\), while the closing edge \(\{0,n-1\}\) has conductance \(c\geq0\). With budget \(B>0\) and closing-edge unit price \(t>0\), impose
\[
\sum_{i=1}^{n-1}w_i+tc=B.
\]
The objective is to maximize the second-smallest eigenvalue \(\lambda_2(L(w,c))\) of the weighted graph Laplacian, equivalently the slowest nonconstant decay rate of symmetric continuous-time diffusion.

**Sharp activation boundary.** Let \(t_n=(n-1)^2\) and \(\Lambda=B/S_n\). For \(t>t_n\), the unique maximizing allocation has
\[
c=0,\qquad w_i=\frac{\Lambda}{2}i(n-i)\quad(1\leq i<n),
\qquad \max\lambda_2=\Lambda.
\]
For \(0<t<t_n\), every maximizing allocation has \(c>0\), and the maximum is strictly larger than \(\Lambda\). No formula for the optimal conductances throughout that lower-price phase is asserted.

**Entire boundary-price optimizer face.** Define the explicit \((n-1)\)-by-\((n-1)\) symmetric matrix
\[
C_{ij}=\frac{\min(i,j)(n-\max(i,j))}{n},\quad 1\leq i,j\leq n-1,
\]
and let \(A_n\) be the weighted complete-graph Laplacian on \(\{1,\ldots,n-1\}\) whose off-diagonal edge weights are \(C_{ij}\). Equivalently,
\[
(A_n)_{ij}=-C_{ij}\ (i\ne j),\qquad (A_n)_{ii}=\sum_{j\ne i}C_{ij}.
\]
Put
\[
\rho_n=\frac{\lambda_2(A_n)}{n-1}.
\]
Then \(0<\rho_n\leq(n-1)/(2n)<1/2\). At the exact price \(t=t_n\), **every** globally maximizing allocation, and no other one, is
\[
\boxed{c=\Lambda\delta,\qquad
w_i=\Lambda\left(\frac{i(n-i)}2-(n-1)\delta\right),
\qquad0\leq\delta\leq\rho_n.}
\]
All these allocations have optimal value \(\Lambda\), and all path-edge conductances remain strictly positive throughout the entire optimal face. At its nonzero right endpoint, the optimized Laplacian has \(\Lambda\) as an eigenvalue of multiplicity at least two. Thus the transition price has a nontrivial continuous family of optimal, mostly cyclic designs; the expensive link need not be deleted at equality.

The edge-space cutoff is explicit and exactly computable from a positive weighted complete-graph Laplacian, not from a numerical search over conductance allocations. Examples are \(\rho_3=\rho_4=1/3\), \(\rho_5=(10-\sqrt{10})/20\), and \(\rho_6=(31-\sqrt{97})/60\). For \(n=3\), the boundary-price optimal face joins a two-edge path with the equal-conductance triangle.

## Assumptions and scope

All quantities are real. The graph is a simple undirected \(n\)-cycle for \(n\geq3\), with vertex set \(\{0,1,\ldots,n-1\}\). Each edge can have zero conductance. An allocation may have disconnected positive support; by convention its algebraic connectivity is zero. The Laplacian is \(L=\sum_{uv}w_{uv}(e_u-e_v)(e_u-e_v)^{\mathsf T}\); its eigenvalues are arranged \(0=\lambda_1\leq\lambda_2\leq\cdots\). Diffusion is \(\dot z=-Lz\) and the equilibrium measure is uniform. The budget is exact, not an upper bound. There are no degree, stochastic-row-sum, or positive-holding constraints.

## Proof

**1. The optimal weighted path and its spectral separation.** Put \(u_i=i(n-i)/2\) and \(x_j=j-(n-1)/2\). Direct summation gives
\[
\sum_{i=1}^{n-1}u_i=\sum_{j=0}^{n-1}x_j^2=S_n.
\]
For the path Laplacian \(L_u\) with edge weights \(u_i\), the endpoint and interior equations give \(L_ux=x\). Moreover its entire spectrum is \(\{k(k+1)/2:0\leq k<n\}\). To prove this without a limiting approximation, note that the action of \(L_u\) on the function \(j\mapsto j^k\) is a polynomial of degree at most \(k\), with leading coefficient \(k(k+1)/2\). This follows by expanding both nearest-neighbor finite differences and the quadratic coefficient \(u_i\), with \(u_0=u_n=0\) handling the endpoints. The invariant flag of spaces of functions polynomial in \(j\) of degree at most \(k\), for \(0\leq k<n\), triangularizes this real symmetric matrix. Its diagonal eigenvalues are precisely the stated distinct numbers. In particular, \(\lambda_2(L_u)=1\) is simple and the next eigenvalue is \(3\).

Scaling the path allocation by \(\Lambda=B/S_n\) gives \(\lambda_2=\Lambda\). Conversely, for every budget-feasible path allocation, the Rayleigh quotient of \(x\) bounds \(\lambda_2\) above by \(B/S_n\). Equality forces \(Lx=\Lambda x\); solving the consecutive vertex equations gives exactly \(w_i=\Lambda u_i\). Hence the path optimum is unique.

**2. The closing-link threshold.** For arbitrary budget-feasible cycle weights, since \(x_i-x_{i-1}=1\) and \(x_{n-1}-x_0=n-1\),
\[
\lambda_2(L(w,c))\leq\frac{x^{\mathsf T}L(w,c)x}{x^{\mathsf T}x}
=\frac{B-\bigl(t-(n-1)^2\bigr)c}{S_n}.
\]
When \(t>t_n\), equality at the path-optimal value requires \(c=0\), after which path uniqueness applies. When \(0<t<t_n\), start from the path optimum and increase \(c\) from zero by \(\varepsilon>0\), decreasing each path weight by \(t\varepsilon/(n-1)\). The budget remains exact and all weights are feasible for small \(\varepsilon\). Because the initial second eigenvalue is simple, the first derivative of \(\lambda_2\) is the Rayleigh derivative along \(x\):
\[
\left.\frac{d\lambda_2}{d\varepsilon}\right|_{0+}
=\frac{(n-1)^2-t}{S_n}>0.
\]
The compact feasible simplex has a maximizer, and its value strictly exceeds the best chord-free value. Thus every maximizer has \(c>0\). The price \(t_n\) is sharp.

**3. Every allocation at the boundary price.** At \(t=t_n\), the preceding Rayleigh quotient is exactly \(\Lambda\) for **every** budget-feasible allocation. Therefore an allocation attains the global upper bound precisely when \(x\) is a Fiedler eigenvector of eigenvalue \(\Lambda\). The eigenvector equations \(L(w,c)x=\Lambda x\), beginning at vertex zero and propagating along the path, force
\[
w_i=\Lambda u_i-(n-1)c\qquad(1\leq i<n).
\]
Conversely these formulas satisfy the eigenvector equations and the budget at price \(t_n\). Write \(\delta=c/\Lambda\).

**4. The exact missing spectral condition.** For any centered vector \(y\in\mathbb R^n\), set \(d_i=y_i-y_{i-1}\), \(1\leq i<n\). Centering the cumulative sums gives the exact discrete Brownian-bridge identity
\[
\|y\|_2^2=\sum_{i,j=1}^{n-1}C_{ij}d_id_j.
\]
The path energy is \(\sum_i u_id_i^2\), while the closing-link gradient is \(\sum_i d_i\). Consequently, for the candidate boundary-price allocation,
\[
\frac{y^{\mathsf T}(L-\Lambda I)y}{\Lambda}
=d^{\mathsf T}\left[\operatorname{diag}(u_i)-C
-\delta\bigl((n-1)I-\mathbf1\mathbf1^{\mathsf T}\bigr)\right]d.
\]
A direct summation of \(C_{ij}\) yields \(\sum_jC_{ij}=u_i\), so \(\operatorname{diag}(u_i)-C=A_n\), a complete-graph Laplacian with strictly positive weights \(C_{ij}\) for distinct indices. Both matrices in the bracket annihilate \(\mathbf1\). On its perpendicular complement, \((n-1)I-\mathbf1\mathbf1^{\mathsf T}\) acts as \((n-1)I\). Thus the bracket is positive semidefinite **if and only if**
\[
\delta\leq\frac{\lambda_2(A_n)}{n-1}=\rho_n.
\]
Since \(\lambda_2(L)\geq\Lambda\) is equivalent to nonnegativity of \(L-\Lambda I\) on the centered vertex subspace, this proves sufficiency and necessity and exhausts the optimal face. Strict positivity of \(\rho_n\) follows from positivity of every weight of the complete graph. Testing the vector \(d=(1,0,\ldots,0)\) in the generalized Rayleigh quotient gives \(\rho_n\leq(n-1)/(2n)<1/2\); consequently \(u_i-(n-1)\delta>0\) for all \(\delta\leq\rho_n\). At \(\delta=\rho_n\), a nonconstant null vector of the edge-space bracket produces an additional centered eigenvector of \(L\) at eigenvalue \(\Lambda\). The stated small-order radicals follow from the exact characteristic polynomials of \(A_n\).

## Verification

The accompanying standalone Python 3 program `verify.py` uses only the standard library and exact rational arithmetic. Run `python3 verify.py`. It checks the weighted path eigenvector, the entire polynomial eigenvalue triangularization, the bridge covariance and zero-row-sum identities, the boundary-price budget and eigenvector equations, exact positive-definiteness of anchored edge-space certificates at several rational parameters, and exact small-order endpoint singularities. Its completed run reports `VERIFY_OK 200 exact rational assertion groups`. A separate constrained numerical optimization on \(n\in\{3,4,5,7\}\), with price multipliers \(0.7,1,1.3\) times \(t_n\), corroborated activation below and deletion above the boundary. These finite checks are corroboration only; the proof is the arbitrary-order argument above.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis formulate the general fastest-mixing continuous-time Markov-process problem as a semidefinite program, derive its geometric dual, solve the standalone path exactly (their Result 5), and discuss cycles with uniform and arbitrary edge costs (their Section 5.3). The parabolic path allocation, the basic Rayleigh method, and nonuniqueness of some optimal Markov rates are therefore established prior work, not discoveries asserted here. The present theorem concerns the particular one-exceptional-price cycle and explicitly identifies its quadratic link-activation boundary and **the complete boundary-price optimizer face**, whose endpoint is the spectral gap of an explicit Brownian-bridge complete-graph Laplacian. The general SDP and path solution do not themselves state that spectral endpoint or give this full price-boundary classification. Boyd's ICM overview and Ghosh–Boyd's edge-augmentation paper supply further context, but treat generic SDP or discrete augmentation rather than this exact price geometry.

## Limitations

The optimal conductances and objective are not classified for all prices below \(t_n\), only the strict positivity of the closing edge and a strict improvement over the path. No asymptotic formula for \(\rho_n\), no uniqueness assertion in the lower-price phase, and no claim about discrete-time stochastic kernels are made. An equivalent specialized treatment of one-priced-edge fastest-mixing cycles may exist in unindexed literature. An earlier general tree-optimization source by Fiedler was available only through metadata/abstract and its quotation in the inspected Sun–Boyd–Xiao–Diaconis article, not by a full independent text inspection. Independent mathematical audit has not been performed.

## References

1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, DOI: 10.1137/S0036144504443821. Public author version: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf. Online publication date: 2006-11-02.
2. S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, Proceedings ICM 2006, 1311–1319. Author-accessible full text: https://people.csail.mit.edu/jrennie/trg/papers/boyd-convex-06.pdf.
3. A. Ghosh and S. Boyd, *Growing Well-Connected Graphs*, IEEE CDC (2006), 6605–6611, DOI: 10.1109/CDC.2006.377282. Public author version: https://web.stanford.edu/~boyd/papers/pdf/growing_fast_graphs.pdf.
4. M. Fiedler, *Absolute Algebraic Connectivity of Trees*, Linear and Multilinear Algebra 26 (1990), 85–106, DOI: 10.1080/03081089008817967. Historical path-optimality antecedent, with full-text access limitation as stated above.
