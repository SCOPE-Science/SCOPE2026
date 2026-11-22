# Exact Euclidean vertex-distance polynomial and Gaussian law for cycle graphical zonotopes

## Finding
For every integer \(n\ge3\), take the canonical unit-incidence Euclidean zonotope of the cycle graph:
\[
Z_n=\sum_{i=1}^{n}\left[-\tfrac12(e_i-e_{i+1}),\tfrac12(e_i-e_{i+1})\right]\subset\mathbf1^\perp\subset\mathbb R^n,\qquad e_{n+1}=e_1.
\]
Choose \(X_n,Y_n\) independently and uniformly among the **distinct vertices** of \(Z_n\), not by volume or by normal-cone angle. Put \(D_n=\|X_n-Y_n\|_2^2\), \(N_n=2^n-2\). Define polynomials by
\[
S_0(z)=2,\quad S_1(z)=3+z^4,\quad
S_n(z)=(3+z^4)S_{n-1}(z)-2(1-z^2)^2S_{n-2}(z)\quad(n\ge2).
\]
Then the **complete finite Euclidean vertex-distance distribution** is the polynomial identity
\[
\boxed{N_n^2\mathbb E z^{D_n}=A_n(z)
=S_n(z)+(1-z^4)^n-4\big((1+z)^n+(1-z)^n\big)+4.}
\]
Every coefficient is an exact nonnegative integer: \([z^d]A_n(z)\) counts ordered vertex pairs at squared Euclidean distance \(d\). In particular
\[
\boxed{\mathbb E D_n=\frac{n(4^n-2^{n+1})}{(2^n-2)^2},\qquad
\mathbb E D_n^2=\frac{4^n(n^2+2n)-2^n n(n+1)}{(2^n-2)^2}.}
\]
The fluctuations obey the two asymptotic laws
\[
\boxed{\frac{D_n-n}{\sqrt{2n}}\Longrightarrow N(0,1),\qquad
\sqrt{D_n}-\sqrt n\Longrightarrow N(0,\tfrac12).}
\]
As ancillary endpoint information, \(D_n\) takes only even integer values and its maximum equals \(4n\) for even \(n\), or \(4(n-1)\) for odd \(n\), attained by precisely \(2\) or \(2n\) ordered vertex pairs respectively. The central claimed contribution is the full distribution and its Euclidean limit laws, not a standalone assertion of diameter novelty.

## Assumptions and scope
The cycle \(C_n\) is simple, connected and unweighted, \(n\ge3\). The ambient metric is the ordinary Euclidean metric inherited from \(\mathbb R^n\) on the zero-sum hyperplane; the statement is not invariant under arbitrary affine deformations. Vertices, rather than volume-uniform points, are independently uniformly sampled. Ordered pairs permit \(X_n=Y_n\). The coefficient variable \(z\) marks **squared** Euclidean distances, which are integers in this normalization. All finite formulas are exact for every \(n\ge3\); distributional limits concern \(n\to\infty\). An auxiliary random-normal-direction sampling scheme would be a different measure.

## Proof
**1. Vertex parametrization and squared distance.** Direct the cycle edges cyclically and put \(b_i=e_i-e_{i+1}\), so \(\sum_i b_i=0\). The centered zonotope is a linear image of the edge-sign cube. A generic objective selects the sign \(s_i\in\{-1,1\}\) according to the sign of its difference between adjacent graph vertices. All nonconstant sign strings, and only those, are realizable: an assigned mixed-sign vector can be shifted by its mean to give a zero-sum vector with the same strict signs, then integrated around the cycle to produce a strictly exposing objective. The two constant strings represent cyclic directed orientations and cannot be exposed. The resulting \(2^n-2\) vectors \(v(s)=\tfrac12\sum_i s_i b_i\) are distinct: the incidence map has kernel exactly the constant edge strings, and the difference of two distinct mixed sign strings cannot be constant unless they are the two excluded complementary constants. Set \(w_i=(s_i-t_i)/2\in\{-1,0,1\}\). Directly from the incidence coordinates,
\[
\|v(s)-v(t)\|_2^2=\sum_{i=1}^n(w_i-w_{i-1})^2,\quad w_0=w_n.\tag{1}
\]

**2. The complete transfer polynomial.** Before deleting cyclic sign strings, each independently chosen pair of edge signs yields a state \(w_i\in\{-1,0,1\}\) with integer multiplicity \(1,2,1\). Thus the unrestricted *ordered count polynomial* is \(\operatorname{tr}M(z)^n\), where, in state order \((-1,0,1)\),
\[
M(z)=\begin{pmatrix}1&2z&z^4\\ z&2&z\\ z^4&2z&1\end{pmatrix}.
\]
Indeed, its \((a,b)\) entry is the multiplicity of state \(b\) multiplied by \(z^{(a-b)^2}\); a closed walk of length \(n\) has weight \(z^{D_n}\) by (1). Restricting one of the two input sign strings to be constant instead yields \(\operatorname{tr}T(z)^n\), where \(T(z)=\bigl(\begin{smallmatrix}1&z\\z&1\end{smallmatrix}\bigr)\). Inclusion-exclusion removes two constant choices for each of the two strings (four faces) and restores the four intersections (two choices each), all with distance zero:
\[
A_n(z)=\operatorname{tr}M(z)^n-4\operatorname{tr}T(z)^n+4.\tag{2}
\]
Since \(T\) has eigenvalues \(1+z\), \(1-z\), its trace equals \((1+z)^n+(1-z)^n\). The antisymmetric eigenvector \((1,0,-1)\) of \(M\) has eigenvalue \(1-z^4\). On the invariant symmetric two-space the other two eigenvalues have sum \(3+z^4\) and product \(2(1-z^2)^2\). Therefore their power sums satisfy the recurrence for \(S_n\) with initial values \(S_0=2,S_1=3+z^4\). Combining this with (2) gives the displayed complete exact polynomial. Since (2) arose from counting real pairs, coefficient nonnegativity needs no independent sign argument.

**3. Exact first and second moments.** For unrestricted independent uniform sign strings, the \(w_i\) are independent, with probabilities \(\Pr(w_i=0)=1/2\), \(\Pr(w_i=\pm1)=1/4\). Put \(Q_i=(w_i-w_{i-1})^2\). Direct moment calculations using \(\mathbb Ew_i=0\), \(\mathbb Ew_i^2=1/2\) and \(\mathbb Ew_i^4=1/2\) give \(\mathbb EQ_i=1\), \(\operatorname{Var}(Q_i)=3/2\), \(\operatorname{Cov}(Q_i,Q_{i+1})=1/4\), and zero covariance for disjoint edge pairs. For every \(n\ge3\) the cyclic total has
\[
\mathbb E D_n^{\rm unrestricted}=n,\quad\mathbb E(D_n^{\rm unrestricted})^2=n^2+2n.
\]
With one sign string fixed to a constant, each \(w_i\) is an independent Bernoulli state, up to global sign. In that case \(D_n\) counts binary transitions around the cycle, with mean \(n/2\), variance \(n/4\), and second moment \(n(n+1)/4\). There are \(4^n\) unrestricted sign pairs, four forbidden faces each of size \(2^n\), and four face-intersection pairs having \(D_n=0\). Subtracting their first and second raw moment sums, then dividing by \((2^n-2)^2\), proves both finite moment formulas.

**4. The limit laws.** For independent unrestricted \(w_i\), the stationary sequence \(Q_i\) is bounded and 1-dependent with positive asymptotic variance \(\operatorname{Var}(Q_i)+2\operatorname{Cov}(Q_i,Q_{i+1})=2\). The ordinary 1-dependent central limit theorem (or a direct separated-block characteristic-function proof) implies \((\sum_iQ_i-n)/\sqrt{2n}\Longrightarrow N(0,1)\); closing the linear chain changes only one bounded term and does not affect the limit. The probability that either input sign string is constant is at most \(2^{2-n}\), so conditioning both to be nonconstant changes the law by at most that amount in total variation. Thus the same normal limit holds for uniform zonotope vertices. Since \(D_n/n\to1\) in probability, the expansion \(\sqrt{D_n}-\sqrt n=(D_n-n)/(\sqrt{D_n}+\sqrt n)\), followed by Slutsky's theorem, gives the ordinary Euclidean-distance limit \(N(0,1/2)\).

**5. Support parity and endpoint checks.** Modulo two, \((w_i-w_{i-1})^2\equiv w_i-w_{i-1}\), whose sum vanishes around the cycle, so every squared distance is even. A contribution of \(4\) occurs exactly when two neighboring states are nonzero and opposite. For even \(n\), the unique maximizing patterns \(w\) are the two fully alternating \(\pm1\) strings, giving distance \(4n\), each arising from exactly one ordered sign pair. For odd \(n\), fully nonzero \(w\) has at most \(n-1\) opposite transitions, with equality exactly for configurations with one agreeing adjacent pair; there are \(2n\) such sign strings, each yielding a unique ordered vertex pair, hence distance \(4(n-1)\). If any \(w_i=0\), both incident terms contribute at most \(1\), so total distance is at most \(4(n-2)+2=4n-6<4(n-1)\). This proves the endpoint counts without relying on enumeration.

## Verification
Run `python3 check_cycle.py` using Python 3 standard library; no external dependencies or downloaded datasets are needed. It independently enumerates the zonotope vertices and every ordered pair at \(3\le n\le8\), comparing their squared-distance histogram coefficient by coefficient with the transfer polynomial. It checks the transfer representation through \(n=10\), and a separately implemented integer-polynomial recurrence, both moment formulas, parity and diametral multiplicities for every \(3\le n\le40\). Successful replay prints `CYCLE_ZONOTOPE_VERTEX_DISTANCE_EXACT_PASS` and `CYCLE_ZONOTOPE_RECURRENCE_MOMENTS_PASS 38`. These finite tests corroborate, but do not establish, the infinite statements or asymptotic limits, which follow from the preceding proof.

## Relationship to prior work
Padrol, Pilaud and Poullot (2021) give graphical zonotopes' deformation/normal-fan framework and the standard orientation correspondence. Pešović and Stojadinović (2022) study graph-to-associahedron interpolations and quasisymmetric weighted integer-point enumerators, not this canonical Euclidean vertex-pair statistic. A prior complete calculation of the **one-skeleton Laplacian spectrum** of the same cycle zonotope uses the antipodally punctured hypercube graph but does not determine Euclidean distances between embedded vertices: the intrinsic Euclidean metric is not the graph's Hamming metric. A prior complete calculation of the **uniform-vertex covariance** for cactus graphical zonotopes gives the first squared-distance moment of a cycle but cannot determine this full distance polynomial, its higher moments, or its Gaussian limit. A prior **Löwner ellipsoid** calculation for unicyclic graphical zonotopes provides some outer-radius/contact facts but not the pairwise metric distribution; the endpoint discussion here is therefore ancillary. A prior **intrinsic-volume index** limit for the cycle zonotope concerns a different sampling measure and random variable. The classical finite-state transfer method and 1-dependent CLT are tools, not claimed new theorems. The new assertion is the explicit evaluated all-dimensional Euclidean pair-distance polynomial and its two limit laws.

## Limitations
No general graphical zonotope, edge-weighted cycle, noncanonical affine embedding, Gaussian-exposed vertex measure, or volume-uniform sampling measure is covered. The asymptotic statement is a weak distributional limit, not a local central limit theorem or a convergence rate. The diameter consequence may overlap preexisting outer-geometry results and is not presented as a separate novelty assertion. The literature comparison is based on located, read sources and does not establish independent priority against inaccessible or unindexed sources. No independent mathematical audit has been performed.

## References
1. A. Padrol, V. Pilaud and G. Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first posted 2021-11-24. https://arxiv.org/abs/2111.12422
2. M. Pešović and T. Stojadinović, *Between Graphical Zonotope and Graph-Associahedron*, arXiv:2209.12053, first posted 2022-09-24. https://arxiv.org/abs/2209.12053
3. C. Ding, *Geometric Bijections Between Spanning Subgraphs and Orientations of a Graph*, Journal of the London Mathematical Society, DOI:10.1112/jlms.12776 (online 2023-06-13). https://doi.org/10.1112/jlms.12776
4. *Laplacian spectrum and spanning-tree complexity of cycle graphical zonotopes*, published mathematical research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-laplacian-spectrum-and-spanning-tree-complexity-of-cycle-graphic--8dfabf4d984d
5. *A sharp vertex–volume covariance sandwich for cactus graphical zonotopes*, published mathematical research record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-vertex-volume-covariance-sandwich-for-cactus-graphical-z--b39706fc7ceb
6. *Exact Löwner ellipsoids and sharp cycle-length extremizers of unicyclic graphical zonotopes*, published mathematical research record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-l-wner-ellipsoids-and-sharp-cycle-length-extremizers-of-un--1583727c8ad6
7. *Gaussian intrinsic-volume profiles for cycle graphical zonotopes*, published mathematical research record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-gaussian-intrinsic-volume-profiles-for-cycle-graphical-zonotopes--3ae59b7ce98c
