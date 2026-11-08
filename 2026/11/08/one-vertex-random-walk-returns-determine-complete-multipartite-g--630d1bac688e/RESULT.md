# One-vertex random-walk returns determine complete multipartite graphs of known order

## Finding
Let \(N\ge 2\) be known. For any connected simple complete multipartite graph \(G=K_{n_1,\ldots,n_r}\) of order \(N\), with \(r\ge 2\) and positive part sizes, choose an arbitrary vertex \(v\). Run ordinary discrete-time, non-lazy simple random walk started at \(v\), and write \(p_t=\Pr_v(X_t=v)\). The finite vector
\[
(p_0,p_1,\ldots,p_{2N-1})
\]
uniquely determines the multiset \(\{n_1,\ldots,n_r\}\) and the size of the part containing \(v\). In particular it reconstructs the rooted graph up to isomorphism, without observing any vertex other than \(v\).

An explicit rational decoder is given below. Knowing \(N\) cannot simply be dropped: for any fixed \(a\ge1\), all rooted complete bipartite graphs \((K_{a,b},v)\), where \(v\) belongs to the size-\(a\) part and \(b\ge1\), have exactly the same return sequence.

## Assumptions and scope
The graph is finite, unweighted, undirected, loopless, connected, and complete multipartite; \(N\) is supplied and \(v\) may lie in any part, including a singleton. A step chooses uniformly among the current vertex's neighbors. The probabilities are exact, not sample estimates. There is no holding or resetting. The rooted reconstruction distinguishes parts of different sizes but does not attempt to label vertices within a part.

## Proof
Write \(a=n_i\) for the size of the part containing \(v\), and let \(P\) be the \(N\)-by-\(N\) transition matrix. Let \(U\) be the space of functions constant on each part, and \(W\) the space of functions whose sum within every part is zero. These spaces form a direct sum. The operator \(P\) annihilates \(W\); it preserves \(U\) and acts there through the \(r\)-by-\(r\) quotient matrix
\[
Q_{jk}=\begin{cases} n_k/(N-n_j),&k\ne j,\\0,&k=j.\end{cases}
\]
The partwise-constant projection of a coordinate vector at \(v\) is \(a^{-1}\) times the indicator of part \(i\). Consequently, for every \(t\ge1\),
\[
p_t=\frac{(Q^t)_{ii}}{a},\qquad p_0=1.
\]
Set \(d_j=n_j/(N-n_j)>0\), \(u_j=(N-n_j)^{-1}\), and \(w_j=n_j\). Then \(Q=uw^\mathsf T-\operatorname{diag}(d_j)\). The matrix determinant lemma gives
\[
\det Q=(-1)^r(1-r)\prod_{j=1}^r d_j\ne0,
\]
because \(w_j u_j/d_j=1\) for every \(j\). Thus \(P\) has zero eigenspace precisely \(W\). Since an undirected random walk is similar to a real symmetric matrix and every degree is constant within its part, its spectral projector at eigenvalue zero has diagonal entry \(1-1/a\) at \(v\).

Define the rational return resolvent
\[
F(z)=\sum_{t\ge0}p_tz^{-t-1}=[(zI-P)^{-1}]_{vv}.
\]
Its zero-eigenvalue residue is \(\omega_0=\lim_{z\to0}zF(z)=1-1/a\). Hence the observed return sequence recovers \(a=(1-\omega_0)^{-1}\). More precisely, after determining the rational function \(F\), set
\[
G(z)=a\left(F(z)-\frac{1-1/a}{z}\right)
=[(zI-Q)^{-1}]_{ii}.
\]
Now \(d=d_i=a/(N-a)\) is known. Put
\[
X(z)=\sum_{j\ne i}\frac{d_j}{z+d_j}.
\]
Applying the rank-one resolvent identity to \(Q=uw^\mathsf T-\operatorname{diag}(d_j)\) and simplifying its \((i,i)\) entry yields
\[
G(z)=\frac{1-X(z)}{(z+d)(1-X(z))-d}.
\]
Thus, with \(B(z)=z-G(z)^{-1}\), direct rearrangement gives the explicit inversion
\[
X(z)=\frac{B(z)}{d+B(z)}.
\]
For each distinct part size \(s\) among the *other* parts, \(X\) has a simple pole at \(-s/(N-s)\) with residue \(m_s s/(N-s)\), where \(m_s\) is the number of these other parts of size \(s\). No two distinct positive \(s<N\) give the same pole, and residues are positive, so no poles cancel. Pole locations and residues therefore recover every \(s\) and its multiplicity \(m_s\). Adding the already recovered size \(a\) reconstructs the entire rooted multipartition. This completes infinite-sequence uniqueness.

For the finite-data claim, the reversible transition matrix \(P\) is similar to a symmetric \(N\)-by-\(N\) matrix. Its rooted return sequence has the representation \(p_t=\sum_{\lambda}\alpha_\lambda\lambda^t\) with nonnegative weights and at most \(N\) distinct real support points. Comparing two rooted graphs of the same known order \(N\), subtract their representations and combine coinciding eigenvalues. The difference is a signed exponential sum on at most \(2N\) distinct real support points. If the first \(2N\) moments (times \(0\) through \(2N-1\)) vanish, the Vandermonde matrix is invertible and all combined weights vanish. Therefore all return probabilities agree and the preceding decoder gives the same rooted multipartition.

Finally, on \(K_{a,b}\), the walk alternates deterministically between its two parts and, on each even positive time, its position in the initial part is uniform. Thus \(p_{2t}=1/a\) for every \(t\ge1\), \(p_{2t+1}=0\), and \(p_0=1\), irrespective of \(b\). This proves the claimed necessity of an order assumption for unrestricted reconstruction.

## Verification
Running `python3 verify.py` checks exact rational state-space return powers against the quotient formula, verifies the resolvent inversion independently via full matrices and quotient matrices, and exhaustively checks distinct rooted return signatures within the complete multipartite class through order \(N=11\). It also verifies the complete-bipartite unknown-order ambiguity. The submitted standalone checker returned `VERIFY_OK 25856 exact-rational checks`. The general proof is algebraic; finite enumeration is a corroboration, not its logical foundation.

## Relationship to prior work
Zatloukal (2020 preprint, 2021 journal article) develops local-time observables in terms of random-walk resolvents and treats complete graphs and stars explicitly. Sun and Das (2020) derive the normalized-Laplacian characteristic polynomial of complete multipartite graphs and investigate determination by the *global* normalized spectrum. These forward spectral methods do not by themselves assert reconstruction of arbitrary rooted multipartitions from the *single-vertex* return law, and the above residue decoder provides a distinct local inverse result. The classical relationship between return probabilities and rooted spectral measures is used without a novelty claim. Another existing reconstruction result based on the degree marginal of a uniform spanning tree on complete multipartite graphs concerns a different random experiment and neither entails nor is entailed by this theorem.

## Limitations
Graph order must be known. The observations are exact probabilities, so no sampling-complexity, robustness, or finite-sample statistical guarantee is proved. The bound \(2N-1\) on the largest lag is sufficient, not asserted optimal. The theorem is specific to connected complete multipartite simple graphs; it does not assert reconstruction of unrestricted graphs from one rooted return sequence. Prior normalized-spectral and resolvent results create historical-priority risk for the inverse formulation; independent mathematical review has not been performed.

## References
- V. Zatloukal, *Local time of random walks on graphs*, first publicly posted 2020-12-31, arXiv:2012.15399, https://arxiv.org/abs/2012.15399; Physical Review E 104 (2021), 044302.
- S. Sun and K. C. Das, *Normalized Laplacian spectrum of complete multipartite graphs*, Discrete Applied Mathematics 284 (2020), 234–245, https://doi.org/10.1016/j.dam.2020.03.041.
- *Sharp Bounds on Random Walk Eigenvalues via Spectral Embedding*, International Mathematics Research Notices (2018), https://academic.oup.com/imrn/article/2018/24/7555/3859207 (general rooted spectral-measure background).
