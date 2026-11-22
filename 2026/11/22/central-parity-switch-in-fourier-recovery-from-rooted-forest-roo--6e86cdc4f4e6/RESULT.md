# Central parity switch in Fourier recovery from rooted-forest root sets

## Finding
Let \(n\ge2\) and let \(G=K_{n,n}\) have two distinguished, labelled shores of size \(n\). For every \(R\subseteq V(G)\), let \(f_n(R)\) count undirected spanning forests of \(G\), with **exactly one distinguished root in each tree**, whose complete set of roots is \(R\). Forests and root choices are counted with multiplicity. On the Boolean group \(H=(\mathbb Z/2\mathbb Z)^{2n}\), let \(T_ng=f_n*g\) denote unnormalized convolution.

For a Walsh character indexed by \(S\subseteq V(G)\), write \(p=|S\cap A|\) and \(q=|S\cap B|\). Its unnormalized multiplier is
\[
\widehat f_n(S)=(n+1)^{2n-p-q}(n-1)^{p+q}
\left(1-\frac{\big(n(n-1)+2p\big)\big(n(n-1)+2q\big)}{(n^2-1)^2}\right).
\]
It vanishes **if and only if** \(n\) is odd and \(p=q=(n-1)/2\). Consequently
\[
\operatorname{nullity}(T_n)=
\begin{cases}
0,&n\text{ even},\\
\binom{n}{(n-1)/2}^{2},&n\text{ odd},
\end{cases}
\qquad \operatorname{rank}(T_n)=4^n-\operatorname{nullity}(T_n).
\]
When \(n\) is odd, all lost characters have Walsh degree exactly \(n-1\), so every character of degree at most \(n-2\) survives. The nullity fraction along odd \(n\) is asymptotic to \(2/(\pi n)\). The largest absolute multiplier is exactly \((2n+1)(n+1)^{2n-2}\), attained at the trivial character.

## Assumptions and scope
All graphs are simple and unweighted, with fixed vertex labels and both shores of equal size \(n\ge2\). A rooted forest means one chosen vertex per connected component; multiple root choices on one unrooted forest contribute separately. Fourier transforms and convolutions use **no normalization**; the operator is on the full complex (or real) function space \(\mathbb C^{H}\). No claim about a sharp least positive multiplier or stability in other norms is made. The case \(n=1\) is deliberately excluded: for \(K_{1,1}\) there are no vanishing Fourier coefficients.

## Proof
**1. Root-set generating polynomial.** For a finite graph with Laplacian \(L\), the all-minors matrix-tree identity says the principal minor \(\det L_{V\setminus R,V\setminus R}\) counts spanning forests rooted at the prescribed set \(R\). Expanding a determinant in independent diagonal variables gives the multiaffine identity
\[
\det(L+\operatorname{diag}(z_v:v\in V))
=\sum_{R\subseteq V} f_G(R)\prod_{v\in R}z_v.
\]
The empty-root term vanishes whenever the graph is nonempty, because \(\det L=0\). Substituting \(z_v=-1\) for \(v\in S\), and \(z_v=1\) otherwise, produces exactly \(\widehat f_G(S)=\det(L+\operatorname{diag}(\epsilon_S))\).

**2. Bipartite rank-one determinant.** For \(G=K_{n,n}\), in shore order the Laplacian is
\[
L=\begin{pmatrix}nI_n&-J_n\\-J_n&nI_n\end{pmatrix}.
\]
The signed diagonal entries are \(n+1\) and \(n-1\), both nonzero for \(n\ge2\). Taking the Schur complement of one diagonal block and applying the rank-one determinant lemma yields the formula in the Finding section, since the reciprocals in the two shores sum respectively to
\[
\frac{n-p}{n+1}+\frac p{n-1}=\frac{n(n-1)+2p}{n^2-1},\qquad
\frac{n-q}{n+1}+\frac q{n-1}=\frac{n(n-1)+2q}{n^2-1}.
\]

**3. Complete zero classification.** Put \(Q=n^2-1\), \(u=2p-(n-1)\), and \(v=2q-(n-1)\). The zero equation becomes \(Q(u+v)+uv=0\), with each of \(u,v\) in \([-(n-1),n+1]\) and with \(u+v\) even. If \(u,v\) are both nonnegative or both nonpositive, the equation forces \(u=v=0\). If they have opposite signs, then \(|uv|\le(n-1)(n+1)=Q\). As a nonzero even value of \(u+v\) has absolute value at least two, it would give \(|Q(u+v)|\ge2Q>|uv|\). Thus \(u+v=0\), and then \(uv=0\), again forcing \(u=v=0\). The same direct equation handles either zero variable. Therefore the sole possible solution is \(p=q=(n-1)/2\), which is integral precisely when \(n\) is odd.

**4. Nullity, first loss, and maximal multiplier.** There are \(\binom np\binom nq\) sign characters with prescribed \((p,q)\), and the Walsh transform diagonalizes convolution. This gives the exact rank and nullity. For odd \(n\), the zero characters all have weight \(p+q=n-1\); none with smaller degree vanish. Stirling's central-binomial estimate gives \(\binom n{(n-1)/2}^2/4^n\sim2/(\pi n)\). Finally, the triangle inequality bounds every multiplier by \(\sum_R f_n(R)=\det(I+L)\). The Laplacian spectrum of \(K_{n,n}\) consists of \(0\), \(n\) with multiplicity \(2n-2\), and \(2n\), giving \(\det(I+L)=(2n+1)(n+1)^{2n-2}\); equality holds at the trivial character.

## Verification
Run `python check.py` with Python 3 and no external dependencies. It independently enumerates every acyclic edge set and all component-root choices for \(n=2,3,4\), computes the full Walsh spectrum, and compares each multiplier to the claimed formula. It separately uses exact Bareiss determinants for every shore-sign class through \(n=7\) and verifies the arithmetic zero condition and binomial multiplicities for every \(2\le n\le60\). The exhaustive finite checks are independent corroboration; the all-\(n\) assertion is proved algebraically above, not inferred from a finite cutoff.

## Relationship to prior work
Chebotarev and Shamis established matrix-forest determinant identities, and Chebotarev and Agaev studied forest matrices and their Laplacian expansions. These establish the underlying root-set enumeration method, **not an explicit Walsh zero-locus or convolution rank theorem for balanced complete bipartite graphs**. The present conclusion additionally solves the two-shore signed determinant's integral zero equation. Results concerning edge-incidence Fourier transforms of forests, and results aggregating forests only by component count, do not by themselves give this character-by-character root-set classification.

## Limitations
The result treats the **root-set counting measure**, not the edge-incidence indicator of forests and not the unweighted indicator of feasible root sets. It does not classify unbalanced \(K_{a,b}\), perturbed bipartite graphs, or the minimum nonzero singular value. The exact zero-locus specialization is elementary once the classical multivariate forest identity is available; its historical priority may be affected by unindexed signed vertex-weight specializations. No independent validation has been performed.

## References
1. P. Chebotarev and R. Agaev, *Forest matrices around the Laplacian matrix*, first public arXiv version 2005-08-10, https://arxiv.org/abs/math/0508178.
2. P. Chebotarev and E. Shamis, *Matrix-Forest Theorems*, first public arXiv version 2006-02-25, https://arxiv.org/abs/math/0602575. See the all-minors rooted-forest lemma and determinant theorem.
