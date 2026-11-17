# A sharp two-sided Gini–Dobrushin comparison for finite Markov operators

## Finding

For every integer \(n\ge2\), let \(P\) be an \(n\)-by-\(n\) row-stochastic matrix. Define the oscillation seminorm \(D(x)=\max_i x_i-\min_i x_i\) and the complete-pair Gini seminorm \(G(x)=\sum_{i<j}|x_i-x_j|\) on real vectors. Write
\[
\delta(P)=\sup_{D(x)>0}\frac{D(Px)}{D(x)},\qquad
\gamma(P)=\sup_{G(x)>0}\frac{G(Px)}{G(x)}.
\]
Then the sharp, dimension-dependent **two-sided comparison** is
\[
\boxed{c_n^{-1}\delta(P)\le\gamma(P)\le c_n\delta(P),\qquad
c_n=\frac{\lfloor n^2/4\rfloor}{n-1}.}
\]
Both factors are optimal even when \(P\) is required to be **strictly positive and doubly stochastic**. Consequently, \(\gamma(P)=\delta(P)\) for all stochastic \(P\) at sizes two and three. Size four is the first at which either strict inequality is possible, including among strictly positive, symmetric, positive-semidefinite doubly stochastic matrices.

For odd \(n\), \(c_n=(n+1)/4\); for even \(n\), \(c_n=n^2/[4(n-1)]\). In particular, the optimal comparison loss grows linearly with the number of states.

## Assumptions and scope

All vectors, matrices, and seminorms are real. A row-stochastic matrix has nonnegative entries and each row sums to one. Its Dobrushin coefficient is
\[
\delta(P)=\frac12\max_{i,j}\sum_{r=1}^{n}|P_{ir}-P_{jr}|.
\]
Strictly positive means every entry is greater than zero; doubly stochastic means both row and column sums equal one. No irreducibility or reversibility is assumed for the main inequality. The result compares one-step induced seminorms and does not concern entropy divergences between probability distributions.

## Proof

**1. Sharp geometry of the two seminorms.** For every nonconstant \(x\),
\[
(n-1)D(x)\le G(x)\le \lfloor n^2/4\rfloor D(x). \tag{1}
\]
For the lower bound, choose a minimizing coordinate and a maximizing coordinate; their pair contributes \(D(x)\), and each of the other \(n-2\) coordinates contributes at least \(D(x)\) from its two pairs with the extreme coordinates. For the upper bound, subtract the minimum and divide by \(D(x)\). Convexity of \(G\) on the cube \([0,1]^n\) gives a maximizing binary vector. A cut with \(k\) ones has \(G=k(n-k)\), so its maximum is \(\lfloor n^2/4\rfloor\). Singleton cuts attain the lower bound; balanced cuts attain the upper bound.

**2. Operator comparison.** Since \(P\mathbf1=\mathbf1\), the two induced seminorms are well-defined on vectors modulo constants. Using (1),
\[
G(Px)\le \lfloor n^2/4\rfloor D(Px)
\le \lfloor n^2/4\rfloor\delta(P)D(x)
\le c_n\delta(P)G(x).
\]
Interchanging the two seminorms in the same argument yields
\(\delta(P)\le c_n\gamma(P)\). For each row difference, the maximum of its dot product with a vector in \([0,1]^n\) is half the row's \(\ell^1\)-mass, proving the stated Dobrushin formula.

**3. Two independent sharpness constructions.** Let \(k=\lfloor n/2\rfloor\), \(\ell=n-k\), \(J=\mathbf1\mathbf1^{\mathsf T}/n\), and \(\varepsilon=1/(4n)\). If \(u,v\) both have zero coordinate sum, then
\(P=J+\varepsilon uv^{\mathsf T}\) is doubly stochastic; the choices below have every entry strictly positive. Let
\[
\operatorname{TV}_0(v)=\tfrac12\sum_i|v_i|,\quad
G^*(v)=\sup_{G(x)>0}\frac{|v^{\mathsf T}x|}{G(x)}.
\]
A direct rank-one computation gives
\[
\delta(P)=\varepsilon D(u)\operatorname{TV}_0(v),\qquad
\gamma(P)=\varepsilon G(u)G^*(v). \tag{2}
\]
For the **upper comparison extremizer**, take \(u_i=\ell/n\) for the first \(k\) indices and \(u_i=-k/n\) for the remaining \(\ell\), and take \(v=e_1-e_2\). Then \(D(u)=1\), \(G(u)=k\ell\), \(\operatorname{TV}_0(v)=1\), and \(G^*(v)=1/(n-1)\) by the lower bound in (1), attained by a suitable singleton cut. Thus \(\delta(P)=\varepsilon\) and \(\gamma(P)=c_n\varepsilon\).

For the **lower comparison extremizer**, take \(u=e_1-\mathbf1/n\), and take \(v_i=1/k\) on the first \(k\) indices and \(v_i=-1/\ell\) elsewhere. Then \(D(u)=1\), \(G(u)=n-1\), \(\operatorname{TV}_0(v)=1\). Moreover,
\[
|v^{\mathsf T}x|=\left|\frac1{k\ell}\sum_{i\le k<j}(x_i-x_j)\right|
\le\frac{G(x)}{k\ell},
\]
with equality for the indicator of the first group. Hence \(G^*(v)=1/(k\ell)\), so \(\delta(P)=\varepsilon\) and \(\gamma(P)=\varepsilon/c_n\). The perturbations of \(J\) have magnitude less than \(1/(4n)\) entrywise, so positivity is strict in both constructions. This proves simultaneous optimality of the two constants within strictly positive doubly stochastic kernels.

**4. Reversible examples at the first nontrivial size.** For \(n=4\), set \(P_{\pm}=J+\tfrac1{32}B_{\pm}\), where
\[
B_+=\begin{pmatrix}2&-1&-1&0\\-1&1&0&0\\-1&0&1&0\\0&0&0&0\end{pmatrix},
\quad B_-=\begin{pmatrix}1&0&0&-1\\0&1&-1&0\\0&-1&2&-1\\-1&0&-1&2\end{pmatrix}.
\]
Each \(B_{\pm}\) is a combinatorial graph Laplacian and therefore symmetric, positive semidefinite, and annihilates constants. Thus both \(P_{\pm}\) are strictly positive, symmetric, doubly stochastic, and positive semidefinite. Exact binary-cut calculations give \(\gamma(B_+)=10/3\), \(\delta(B_+)=3\), \(\gamma(B_-)=7/2\), and \(\delta(B_-)=4\). These are inherited after multiplication by \(1/32\), so \(\gamma(P_+)>\delta(P_+)\) while \(\gamma(P_-)<\delta(P_-)\). The cut calculations are reproduced in the checker.

## Verification

A finite cut formula makes all matrix calculations exact:
\[
\gamma(T)=\max_{\varnothing\ne S\subsetneq\{1,\dots,n\}}
\frac{G(T\mathbf1_S)}{|S|(n-|S|)}
\]
for every linear \(T\) preserving constants (with the same formula for zero-row-sum maps). Indeed, a real vector is a constant plus a nonnegative linear combination of nested indicator cuts, and \(G\) is subadditive. The provided Python 3 checker uses rational arithmetic and independently checks the two sharp rank-one constructions for sizes \(2\) through \(11\), the four-dimensional symmetric examples, and the geometric cut extremizers. The infinite-dimensional-family assertions are supplied by the analytical proof above, not by extrapolation from these finite checks.

## Relationship to prior work

Gaubert and Qu's 2013 public preprint establishes the classical Hopf-oscillation/Dobrushin coefficient identity for Markov operators, including its total-variation dual, but not the Gini seminorm induced coefficient or its two-sided sharp comparison. Cohen, Iwasa, Rautu, Ruskai, Seneta, and Zbaganu (1993) compare Dobrushin coefficients with contractions of componentwise relative \(\phi\)-entropies between two probability laws. Those divergences differ from pairwise dispersion of one real signal and, unlike the present ratio, obey a one-sided domination by Dobrushin's coefficient. The present result uses elementary optimal norm equivalence but adds simultaneous attainment within strictly positive bistochastic kernels and reversible examples with opposite coefficient rankings.

## Limitations

The optimal coefficient \(c_n\) is for general positive bistochastic Markov matrices, not claimed sharp for the symmetric/reversible subclass. The symmetric examples establish both possible orderings but not its best constants. The theorem concerns a fixed finite state space, one step, and unweighted complete-pair Gini variation. An unindexed equivalent comparison in older ergodicity-coefficient literature cannot be ruled out, and no independent mathematical audit has been performed.

## References

1. S. Gaubert and Z. Qu, *Dobrushin ergodicity coefficient for Markov operators on cones, and beyond*, first public arXiv submission 2013-02-21, arXiv:1302.5226, https://arxiv.org/abs/1302.5226 (particularly Section 4, stochastic-matrix example and Dobrushin formula).
2. J. E. Cohen, Y. Iwasa, Gh. Rautu, M. B. Ruskai, E. Seneta and Gh. Zbaganu, *Relative Entropy Under Mappings by Stochastic Matrices*, Linear Algebra and its Applications 179 (1993), 211–235, DOI:10.1016/0024-3795(93)90331-H, https://lab.rockefeller.edu/cohenje/assets/file/205CohenIwasaRautuRuskaiSenetaZbaganuRelativeEntropyMappingsStochasticMatricesLAA1993.pdf (Definitions 2.2–2.3, Theorems 3.1 and 4.1–4.2).
