# Parity-conditioned Walsh sampling on even derangements: exact eigenvalues and a nine-label phase reversal

## Finding

Let \(n\ge4\), and choose uniformly an **even, fixed-point-free permutation** \(\Pi\) of \([n]\). Encode it by the Boolean off-diagonal assignment indicators \(X_{ij}=\mathbf1\{\Pi(i)=j\}\), for \(i\ne j\). The normalized Walsh first-band restriction samples the constant character and the \(n(n-1)\) characters \(\chi_{ij}(X)=(-1)^{X_{ij}}=1-2X_{ij}\) on this finite subset of \(\mathbb F_2^{n(n-1)}\). Let \(G_n\) denote their probability-normalized Gram matrix.

Write \(D_0=1\), \(D_1=0\), \(D_r=(r-1)(D_{r-1}+D_{r-2})\) for \(r\ge2\), and set
\[
s=(-1)^{n-1},\quad F=D_n+s(n-1),\quad
C=D_{n-2}+2D_{n-3}+D_{n-4},\quad
\alpha=\frac1{n-1}+\frac C F,\quad
\beta=\frac{D_{n-4}-s(n-1)}F.
\]
Then the **complete Gram spectrum**, including all zero multiplicities, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\tau=1+\frac{n(n-3)^2}{n-1}&1\\
4(\alpha+\beta)&\frac{n(n-3)}2\\
4(\alpha-\beta)&\frac{(n-1)(n-2)}2\\
0&2n-1.
\end{array}
\]
For \(n=4\), the third listed eigenvalue is zero, so **the true zero multiplicity is ten** (and Gram rank three). For every \(n\ge5\), all three listed positive eigenvalues are strictly positive, the nullity is exactly \(2n-1\), and the rank equals \(n^2-3n+2\). The two nontrivial spectral spaces consist of symmetric versus skew-symmetric, zero-diagonal coefficient matrices with zero row sums; their dimensions are as displayed.

The sharp **centered first-degree** squared condition number on identifiable assignment-score contrasts is
\[
\kappa_n^2=\frac{\alpha+|\beta|}{\alpha-|\beta|},\qquad n\ge5,
\quad\text{with}\quad \kappa_n^2=1+\frac2{n^3}+O(n^{-4}).
\]
There is **no** exactly tight centered system for \(n\ge5\): \(\beta\ne0\) for every \(n\ge4\). The ordering of the two nontrivial eigenvalues has a sharp, nonmonotone transition: the skew sector is larger **only at \(n=5\) and \(n=7\)**; at \(n=4\) and \(n=6\), and at every \(n\ge8\), the symmetric sector is larger. The first permanent symmetric-over-skew ordering begins at \(n=9\) among odd sizes. In particular, unlike unconditioned derangements, parity conditioning eliminates the previously exact isotropy at five labels.

## Assumptions and scope

All sums and Gram products use the uniform probability measure over even derangements and the unscaled Walsh characters \(\chi_{ij}=(-1)^{X_{ij}}\). The constant character is included. The Gram matrix acts on coefficient space indexed by the constant and the \(n(n-1)\) **ordered** off-diagonal cells. Singular values of the sampling operator are square roots of the nonzero Gram eigenvalues. The centered condition number removes the deterministic mean and the row/column-potential directions; it does not refer to the generally much larger uncentered trivial eigenvalue \(\tau\).

## Proof

**1. Parity-constrained counting.** Let \(E\) and \(O\) denote the numbers of even and odd derangements. The determinant of the zero-diagonal all-ones matrix \(J-I\) gives their signed difference
\[
E-O=\sum_{\pi\text{ derangement}}\operatorname{sgn}(\pi)=(-1)^{n-1}(n-1)=s(n-1),
\]
so \(E=F/2\). Simultaneous relabeling acts transitively on all allowed ordered edges \((i,j)\), preserving permutation parity. Every sample has exactly \(n\) occupied cells, hence \(\mathbb E X_{ij}=p=1/(n-1)\).

For two distinct prescribed edges in different rows and columns, classify their four numerical endpoints: a reciprocal two-cycle (two labels), a directed length-two chain (three labels), or four distinct labels. Inclusion-exclusion for ordinary derangements gives, respectively, the **unrestricted** completion counts \(A=D_{n-2}\), \(B=D_{n-2}+D_{n-3}\), and \(C=D_{n-2}+2D_{n-3}+D_{n-4}\). In the signed counts (even minus odd), a prescribed reciprocal two-cycle contributes \(-s(n-3)\). Four distinct labels give zero signed count: the residual allowed permutation matrix has two identical unrestricted rows, hence zero determinant. All directed chains have the same signed completion count \(b\) by conjugation. Summing signed completions over the \(n-1\) other occupied edges after fixing one edge gives
\[
(n-1)s=-s(n-3)+2(n-2)b+(n-2)(n-3)\cdot0,
\]
so \(b=s\). The **even** two-edge completion counts are therefore
\[
A_e=\tfrac12(D_{n-2}-s(n-3)),\quad
B_e=\tfrac12(D_{n-2}+D_{n-3}+s),\quad
C_e=\tfrac12 C.
\]
Two prescribed edges sharing a row or column cannot both occur.

**2. Covariance action.** Consider real zero-diagonal coefficient matrices. Row and column sums of each sampled permutation matrix are deterministically one, so the covariance operator annihilates the row/column-potential subspace \(\{u_i+v_j:i\ne j\}\), of dimension \(2n-1\). Its perpendicular complement \(U\) consists exactly of matrices with all row and column sums zero. On \(U\), for a fixed \((i,j)\), the sum of all reciprocal-edge coefficients is \(H_{ji}\), of all two-edge-chain coefficients is \(-2H_{ji}\), and of all four-distinct-label edge coefficients is \(H_{ij}+H_{ji}\). The shared-row/column and diagonal terms are treated directly. Using the even completion probabilities \(A_e/E,B_e/E,C_e/E\) yields
\[
(\operatorname{Cov}X\,H)_{ij}=
\left(p+\frac{C_e}{E}\right)H_{ij}
+\left(\frac{A_e-2B_e+C_e}{E}\right)H_{ji}
=\alpha H_{ij}+\beta H_{ji}.
\]
The symmetric zero-row-sum matrices in \(U\) have dimension \(n(n-3)/2\), and the skew-symmetric ones have dimension \((n-1)(n-2)/2\): these follow from ranks \(n\) and \(n-1\) of unsigned and oriented complete-graph incidence maps, respectively. Transposition acts by \(+1\) and \(-1\) on these sectors, so their covariance eigenvalues are \(\alpha+\beta\) and \(\alpha-\beta\).

**3. Walsh Gram and exceptional kernel.** Every Walsh character satisfies \(\chi_{ij}=1-2X_{ij}\), with common mean \(\mu=1-2p=(n-3)/(n-1)\). The constant and all coordinate means contribute one rank-one Gram eigenvalue \(\tau=1+n(n-1)\mu^2\). On the orthogonal zero-row/column subspace the Walsh Gram is four times \(\operatorname{Cov}X\); all row/column potential directions in coefficient space that cancel the constant lie in its kernel. For \(n=4\), direct substitution \(D_0=1,D_1=0,D_2=1,D_4=9\) gives \(\alpha=\beta=2/3\), hence the skew sector is also null. For odd \(n\ge5\), both \(\alpha\pm\beta\) are positive: after multiplication by \(F\), the smaller candidate is bounded below by \(D_n/(n-1)-(n-2)>0\). For even \(n\ge6\), the potentially smaller one has numerator \(D_n/(n-1)+D_{n-2}+2D_{n-3}-n>0\); the other is manifestly positive. These inequalities use \(D_n/(n-1)=D_{n-1}+D_{n-2}\), and the elementary growth of positive derangement numbers from \(n=5\) onward. This proves all ranks and multiplicities.

**4. Exact ordering and asymptotics.** The eigenvalue difference is \(8\beta\) for the Walsh Gram. If \(n\) is even, \(s=-1\) and \(D_{n-4}+n-1>0\). If \(n\) is odd, \(s=1\); at \(n=5,7\), respectively \(D_1=0<4\) and \(D_3=2<6\), so \(\beta<0\). At \(n=9\), \(D_5=44>8\), and the derangement recurrence gives \(D_{n-4}>n-1\) for every larger odd \(n\). Thus \(\beta\) is never zero and the ordering statement follows. Finally \(D_n/n!\to e^{-1}\) gives \(\beta\sim n^{-4}\), \(\alpha\sim n^{-1}\), yielding the exact asymptotic formula for \(\kappa_n^2\).

## Verification

The standalone `check.py` enumerates the even derangements at every size \(4\le n\le8\). It independently counts one-edge and every two-edge inclusion frequency, checks the exact probability and transposition-operator formulas with rational arithmetic, and verifies the covariance action on explicit zero-row/column test matrices. The execution passes 7,799 exact assertions. The proof covers all \(n\ge4\) and does not rely on the finite checker.

## Relationship to prior work

Ku and Wong (2012) study the spectrum of a Cayley **derangement graph on the nonabelian symmetric group**, not the additive-coordinate Walsh sampling Gram studied here. Miska (2015), Section 5, gives arithmetic formulas for even and odd derangement counts, including the parity imbalance that supplies the basic normalization in this proof; that count is not claimed as new. The earlier published *Complete covariance spectrum of uniform derangement assignment scores* treats **all** derangements and proves exact isotropy at \(n=5\). Its uniform covariance cannot be substituted into the even-conditioned measure: already for \(n=4\) the new skew sector has zero variance, whereas the unrestricted one is positive, and for \(n=5\) the previously coincident positive levels split to \(1/4\) and \(5/12\). The genuinely additional claim is the full parity-restricted Gram spectrum, sharp rank and sector-order phase reversal.

## Limitations

No claim is made about higher Walsh bands, parity-odd derangements, nonlinear recovery or sampling under arbitrary weights. Classical counting identities and unsigned derangement covariance are credited. The exact source priority of the all-length parity-restricted Gram law is subject to independent literature verification. Exhaustive finite tests do not establish the infinite-family theorem.

## References

1. C. Y. Ku and K. B. Wong, *Solving the Ku-Wales conjecture on the eigenvalues of the derangement graph* (first public 2012-07-17), arXiv:1207.3878, https://arxiv.org/abs/1207.3878 .
2. Piotr Miska, *Arithmetic Properties of the Sequence of Derangements and its Generalizations* (first public 2015-08-09), especially Section 5, arXiv:1508.01987, https://arxiv.org/abs/1508.01987 .
3. *The complete covariance spectrum of uniform derangement assignment scores*, published-finding corpus (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-the-complete-covariance-spectrum-of-uniform-derangement-assignme--a208797ec285 .
