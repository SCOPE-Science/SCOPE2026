# Fastest mixing on a clique with one pendant vertex: a complete optimizer face

## Finding

Let \(n\ge4\), and let \(G_n\) consist of the complete graph \(K_n\) on \(h,u_1,\ldots,u_{n-1}\), together with one new leaf \(\ell\) adjacent only to \(h\). Consider **every** real symmetric, entrywise nonnegative, row-stochastic matrix \(P\) whose off-diagonal support is contained in the edges of \(G_n\); holding probabilities are permitted. If the eigenvalues of \(P\) are ordered as \(1=\theta_1\ge\theta_2\ge\cdots\ge\theta_{n+1}\), its second-largest eigenvalue modulus is \(\mu(P)=\max\{\theta_2,-\theta_{n+1}\}\); this correctly counts extra unit eigenvalues when \(P\) is reducible. Write
\[
D=5n-4,\quad p=\frac3D,\quad q=\frac{2n-1}D,\quad
\lambda=\frac{n+1}D,\quad t=\frac{4n-5}D.
\]

**Theorem (optimal value, forced edges, and all optimizers).** The global minimum is \(\min_P\mu(P)=t\). Every optimal matrix satisfies
\[
P_{\ell h}=q,\qquad P_{hu_i}=p\quad(1\le i\le n-1),\qquad P_{hh}=0.
\]
Conversely, these entries extend to an optimizer precisely as follows. Choose arbitrary symmetric weights \(w_{ij}=w_{ji}\ge0\) on unordered pairs of ordinary vertices \(u_i,u_j\), with \(w_{ii}=0\); write \(d_i=\sum_{j\ne i}w_{ij}\), and set \(P_{u_i u_i}=1-p-d_i\). These define an optimal stochastic matrix if and only if \(d_i\le1-p\) for every \(i\) and **every eigenvalue of the weighted Laplacian \(L_W\) on \(\mathbf1^\perp\subset\mathbb R^{n-1}\)** lies in
\[
\boxed{\left[\frac{n-2}{5n-4},\ \frac{9n-12}{5n-4}\right].}
\]
All unspecified off-diagonal entries are zero, and \(P_{\ell\ell}=1-q\). This condition includes the case of disconnected internal weights, which is automatically excluded by the strictly positive spectral lower bound. The optimizer face has positive dimension: in particular, the uniform internal weight \(w_{ij}=(1-p)/(n-1)\) is optimal and lies in the relative interior of a nontrivial interval of feasible uniform internal weights.

A further sharp, general **hub-holding penalty** holds for every feasible \(P\), not merely optimal ones:
\[
\boxed{\mu(P)\ge t+\lambda P_{hh}.}
\]
Thus making the hub lazy has a provable linear cost, independent of how the other transitions are chosen.

## Assumptions and scope

The cardinal \(n\) counts the original clique vertices, not the appended leaf; there are \(n+1\) total states. The probabilities are symmetric, so the invariant distribution is uniform over all \(n+1\) vertices. Edges not in \(G_n\) may not carry off-diagonal mass; allowed edges may receive zero mass. No automorphism-invariance restriction is imposed. The theorem is stated for all integers \(n\ge4\). The proof also recovers the previously published four-state instance \(n=3\), which is not claimed to be new. The conclusion concerns discrete-time SLEM, not mixing-time constants or arbitrary nonreversible chains.

## Proof

**1. A universal lower bound.** Put \(L=I-P\) and order coordinates as \((\ell,h,u_1,\ldots,u_{n-1})\). Take the centered vector
\[
v=(2n-1,\ n-2,\underbrace{-3,\ldots,-3}_{n-1\text{ entries}})^T.
\]
Then \(\mathbf1^Tv=0\) and \(\|v\|^2=(n+1)(5n-4)\). Across every permitted edge from \(h\), the difference of endpoint coordinates is \(n+1\), while the differences along all internal clique edges vanish. With \(a=\sum_{j\ne h}P_{hj}=1-P_{hh}\), the Dirichlet energy is exactly
\[
v^TLv=(n+1)^2a.
\]
The Courant–Fischer minimum principle gives
\[
\lambda_2(L)\le\frac{v^TLv}{v^Tv}
=\frac{n+1}{5n-4}(1-P_{hh})=\lambda(1-P_{hh}).
\]
Here the statement also holds for disconnected feasible matrices, with \(\lambda_2(L)=0\). Since \(\mu(P)\ge1-\lambda_2(L)\), this proves \(\mu(P)\ge t+\lambda P_{hh}\ge t\).

**2. Equality rigidly determines all edges incident to the hub.** If \(\mu(P)=t\), both inequalities above are equalities. Hence \(P_{hh}=0\), \(\lambda_2(L)=\lambda\), and the centered test vector \(v\) is a \(\lambda\)-eigenvector of \(L\): equality in its Rayleigh quotient is sufficient for this conclusion. At the leaf coordinate,
\[
(n+1)P_{\ell h}=(Lv)_\ell=\lambda(2n-1),
\]
so \(P_{\ell h}=q\). At every ordinary clique coordinate,
\[
-(n+1)P_{hu_i}=(Lv)_{u_i}=-3\lambda,
\]
so \(P_{hu_i}=p\) independently of all other edges. Finally, \(q+(n-1)p=1\), consistent with zero hub holding. This forces the same star of weights in every optimizer, including every asymmetric choice of the internal clique weights.

**3. Exact block diagonalization and sufficiency.** Fix the forced hub and leaf weights. Write \(W=(w_{ij})\) for the off-diagonal weights within the \(n-1\) ordinary clique vertices, and \(L_W=\operatorname{diag}(d_i)-W\). Their constant vector and the leaf and hub coordinates span an invariant three-dimensional subspace. In its nonorthonormal constant-coordinate basis, the restriction of \(L\) is
\[
Q=\begin{pmatrix}
q&-q&0\\
-q&q+(n-1)p&-(n-1)p\\
0&-p&p
\end{pmatrix}.
\]
Its characteristic polynomial factors exactly as
\[
\det(sI-Q)=s(s-\lambda)
\left(s-\frac{3(2n-1)}{5n-4}\right).
\]
Thus the eigenvalues of \(P\) on this subspace are \(1,t,-\lambda\). The latter has absolute value at most \(t\) for \(n\ge4\). On the orthogonal complement of the constant vector within the ordinary clique coordinates, \(P\) acts as \((1-p)I-L_W\). All its eigenvalues therefore have modulus at most \(t\) exactly when
\[
1-p-t\le\lambda_j(L_W|_{\mathbf1^\perp})\le1-p+t,
\]
which simplifies to the asserted interval. Nonnegative diagonal entries require exactly \(d_i\le1-p\). This proves the full characterization in both directions.

**4. Attainment and nonuniqueness.** Set \(w_{ij}=y=(1-p)/(n-1)\) for all distinct ordinary vertices. Then \(d_i=(n-2)y<1-p\), the internal Laplacian has constant-complement eigenvalue \((n-1)y=1-p\), and hence every transverse eigenvalue of \(P\) equals zero. The only nontrivial eigenvalues are \(t,-\lambda\) and zeros, so the universal lower bound is attained. All inequalities for this uniform \(y\) are strict, so sufficiently small common perturbations of \(y\) produce distinct optimizers. This completes the proof.

## Verification

The standalone `verify.py` uses symbolic algebra to check the three-dimensional characteristic polynomial and normalization identities for symbolic \(n\), constructs exact-rational matrices for 11 clique sizes, and compares spectral predictions with 40 additional randomly chosen internal weighting patterns for five clique sizes. It also reproduces the published four-state special case with \(\mu=7/11\). Run `python verify.py` with Python 3, SymPy and NumPy; the expected completion marker is `VERIFY_OK 68 symbolic/exact comparisons`. The randomized comparisons use floating-point symmetric eigensolvers, whereas the theorem rests on the exact proof above. No computation over finitely many graphs is asserted to prove an infinite statement.

## Relationship to prior work

Boyd, Diaconis and Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), Table 1 and Figure 1(b), explicitly solve the \(n=3\) pendant-clique graph: the minimum SLEM is \(7/11\), the leaf bridge has probability \(5/11\), and each hub-to-other edge has probability \(3/11\). They also demonstrate nonuniqueness of the internal edge (pp. 674–675) and give a rank-one dual test vector proportional to \((5,1,-3,-3)\) (pp. 677–679). The present theorem **does not claim novelty for that instance**; its addition is the uniform all-\(n\ge4\) exact value, all-optimizer spectral characterization without symmetry assumptions, and the quantitative holding penalty.

Boyd, Diaconis, Parrilo and Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), §§4.3 and 5.4.4, analyze **two equal-sized cliques** connected by a bridge; their symmetry-reduction methods are relevant but their stated formula does not cover one singleton and one arbitrary-sized clique. Roch, *Bounding Fastest Mixing*, arXiv:math/0409429 (2004), provides general variational bounds, but formulates its principal spectral optimization using the second eigenvalue rather than the two-sided SLEM in this theorem. No claim is made that a web or database search proves absolute novelty.

## Limitations

The result does not determine SLEM optima for longer pendant paths, for arbitrary unequal stationary distributions, or for nonsymmetric kernels. Interior clique transitions are deliberately nonunique. It does not claim the optimal SLEM equals the optimal total-variation mixing-time constant. Earlier unindexed exact results could imply portions of the family. Scientific assessment here has not been independently audited.

## References

1. S. Boyd, P. Diaconis and L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review **46** (2004), 667–689, DOI: 10.1137/S0036144503423264; full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf (electronic publication October 29, 2004).
2. S. Boyd, P. Diaconis, P. A. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization **20** (2009), 792–819, DOI: 10.1137/070689413; full text: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf (preprint arXiv:0709.0955, first posted September 6, 2007).
3. S. Roch, *Bounding Fastest Mixing*, arXiv:math/0409429v1 (September 22, 2004), https://arxiv.org/pdf/math/0409429.
