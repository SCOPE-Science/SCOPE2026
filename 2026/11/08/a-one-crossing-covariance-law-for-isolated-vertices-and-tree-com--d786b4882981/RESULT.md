# A one-crossing covariance law for isolated vertices and tree components in fixed-edge random graphs

## Finding
Let \(G\) be uniform among the simple graphs on \(n\ge3\) labeled vertices with exactly \(m\) edges. Let \(I\) be its number of isolated vertices and \(T_k\) its number of connected components that are trees of order \(k\), with \(2\le k\le n-1\). Put
\[
M=\binom n2,\quad A=\binom{n-1}2,\quad Q=\binom{n-k}2,\quad B=\binom{n-k-1}2,\quad r=m-k+1.
\]
For \(k-1\le m\le k-1+Q\), write \(\rho(a,b,t)=\binom at/\binom bt\), using zero if \(t>a\). Then
\[
\operatorname{Cov}(I,T_k)=\mathbb E T_k\left[(n-k)\rho(B,Q,r)-n\rho(A,M,m)\right],
\quad\mathbb E T_k=\binom nk k^{k-2}\frac{\binom Qr}{\binom Mm}>0.
\]
The covariance has **at most one sign crossing** as \(m\) traverses this entire feasible interval: its signs occur in the order positive, possibly one zero, then negative, with some regimes absent. Specifically, at \(m=k-1\) its sign is that of \(n-k-n\rho(A,M,k-1)\). If \(Q>0\), the last feasible covariance is strictly negative. For \(k=2\), the initial covariance is zero and all subsequent feasible values are strictly negative.

For any sequence \(k/n\to\alpha\in(0,1)\), the initial-edge covariance sign, away from the critical value, is eventually positive for \(0<\alpha<\alpha_*\) and negative for \(\alpha_*<\alpha<1\), where \(\alpha_*\in(0,1)\) is the unique positive root of \(1-\alpha=e^{-2\alpha}\) (approximately \(0.79681213\)). Thus the nontrivial threshold concerns tree-component size as well as edge count. The same covariance sign applies to the count of components having any specified unlabeled tree shape on \(k\) vertices.

## Assumptions and scope
The sample is the uniform \(G(n,m)\) model, not the independent-edge model. Edges are unoriented and simple. The primary nondegenerate domain is \(n\ge3\), \(2\le k\le n-1\) and \(k-1\le m\le k-1+Q\). Outside it, \(T_k=0\) identically, so the covariance is zero. Tree components include all isomorphism types; an individual tree type has the same conditional-isolation factor. All binomial probabilities above use exact integer arguments.

## Proof
For a fixed \(k\)-vertex set \(S\), a tree component on \(S\) has exactly \(k-1\) internal edges, all \(k(n-k)\) crossing edges absent, and \(r=m-k+1\) arbitrary edges among the \(Q\) pairs outside \(S\). Cayley's labeled-tree count gives \(\mathbb E T_k\) as stated. Conditional on any particular tree component event on \(S\), the outside graph is uniform \(G(n-k,r)\). Every vertex outside \(S\) is then isolated with probability \(\rho(B,Q,r)\), while none in \(S\) is isolated. Consequently \(\mathbb E[I\mid\text{that component}]=(n-k)\rho(B,Q,r)\), independently of the tree shape. Meanwhile \(\mathbb E I=n\rho(A,M,m)\). Summation over possible components proves the exact covariance identity.

When \(\rho(B,Q,r)>0\), compare the ratio
\[
R_m=\frac{(n-k)\rho(B,Q,r)}{n\rho(A,M,m)}.
\]
Its sign relative to one is the covariance sign. For consecutive feasible values with positive numerators,
\[
\frac{R_{m+1}}{R_m}=\frac{B-r}{Q-r}\frac{M-m}{A-m}.
\]
The difference of the right-hand cross-products is exactly
\[
(Q-r)(A-m)-(B-r)(M-m)=\frac{(n-k-1)[k(n-3)+2]}2+kr>0
\]
whenever such a step exists. Therefore \(R_m\) is strictly decreasing while positive and then becomes zero without returning positive. The first ratio comparison gives the initial sign; for \(Q>0\), \(r=Q>B\) at the final feasible edge count, while \(\rho(A,M,m)>0\), giving negative covariance. For \(k=2\), a graph with one edge has exactly \(n-2\) isolates, so its initial covariance is zero.

Finally, with \(k/n\to\alpha\in(0,1)\) and \(m=k-1\),
\[
\rho(A,M,k-1)=\prod_{j=0}^{k-2}\frac{A-j}{M-j}\longrightarrow e^{-2\alpha}.
\]
Hence the normalized initial sign factor converges to \(1-\alpha-e^{-2\alpha}\). The function \(\log(1-\alpha)+2\alpha\) is strictly concave, has positive derivative at zero and tends to minus infinity as \(\alpha\uparrow1\); it has exactly one root in \((0,1)\). This proves the sharp limiting cutoff.

## Verification
The attached standalone `verify.py` exhaustively checks the covariance identity in every \(G(n,m)\) stratum for \(3\le n\le6\), enumerating all graphs. It also checks the exact cross-product factorization and one-crossing sign property for \(4\le n<35\). The verified run reported 41,472 exact assertions. These finite calculations check the algebra but do not replace the proof for all orders.

## Relationship to prior work
Pittel's 1990 tree-census study establishes multivariate asymptotic covariance results in both fixed-edge and independent-edge random graphs, especially for component sizes fixed while \(n\) grows. The present assertion instead classifies **every finite feasible edge count and every component size**, including \(k\) proportional to \(n\), by a rational monotonicity certificate. Gunderson's 2013 connected-component lecture notes give foundational expectations and isolation probabilities in the independent-edge model; they do not provide this fixed-edge all-parameter one-crossing classification. The possibility that the finite formula is implicit in older component-census derivations remains a historical priority concern.

## Limitations
The coefficient \(\mathbb E T_k\) can be extremely small when \(k\) is proportional to \(n\); the sign statement does not assert that such components appear with appreciable probability. The critical-ratio assertion excludes the limiting boundary \(\alpha=\alpha_*\), where lower-order terms matter. No monotone coupling of the underlying random graphs, independent auditing, or uniqueness against the entire historical literature is claimed.

## References
- B. Pittel, *On tree census and the giant component in sparse random graphs*, Random Structures & Algorithms **1** (1990), 311–342. https://doi.org/10.1002/rsa.3240010306
- K. Gunderson, *Connected components in Erdős–Rényi random graphs*, lecture notes dated 26 November–3 December 2013. https://people.maths.bris.ac.uk/~maajg/teaching/complexnets/connected-giantcompt.pdf
