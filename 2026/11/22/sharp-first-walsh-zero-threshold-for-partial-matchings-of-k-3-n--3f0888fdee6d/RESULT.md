# Sharp first Walsh-zero threshold for partial matchings of \(K_{3,n}\)

## Finding

For every integer \(n\ge3\), let \(\mathcal M_n\) be the set of all partial matchings of the complete bipartite graph \(K_{3,n}\), including the empty matching. On the Boolean edge group \(G_n=(\mathbb Z/2\mathbb Z)^{3n}\), let \(T_nf=\mathbf 1_{\mathcal M_n}*f\) be unnormalized counting convolution, where \(\mathcal M_n\) is identified with its incidence vectors. At a frequency support \(S\subseteq E(K_{3,n})\), define
\[
W_n(S)=\sum_{M\in\mathcal M_n}(-1)^{|M\cap S|}.
\]
If \(n\) is even, \(W_n(S)\ne0\) for **every** \(S\); hence \(T_n\) is invertible on all real- or complex-valued functions on \(G_n\). If \(n\ge3\) is odd, put \(r=(n+1)/2\). Then
\[
|S|\le r\quad\Longrightarrow\quad W_n(S)\ge2n>0,
\]
and the bound is attained by every \(r\)-edge star centered at one vertex in the three-vertex bipartition class. Yet there are Fourier zeros of support size exactly \(r+1=(n+3)/2\). In particular,
\[
\min\{|S|:W_n(S)=0\}=\frac{n+3}{2}\qquad(n\ge3\text{ odd}).
\]
There are at least \(6r\binom nr\) *distinct* zeros at that first support degree. Thus for odd \(n\), convolution is injective on the Walsh polynomial space of degree at most \(r\), and is not injective on the space of degree at most \(r+1\). The last count is a certified lower bound, **not** a classification of all minimum-degree zeros.

## Assumptions and scope

The vertices on the small side are labeled \(u_0,u_1,u_2\); the other side has \(n\) labeled vertices. A partial matching may use zero, one, two, or three edges, with no repeated endpoint. The convolution and Walsh transforms are unnormalized, and frequency degree is the cardinality of the edge support. No weighting or restriction to maximum-cardinality matchings is used. This theorem concerns every \(n\ge3\), even or odd, and only the first Fourier zero degree, not the complete spectrum or nullity.

## Proof

**Matching totals and one-edge incidence.** For \(K_{3,n}\), the number of matchings is
\[
N_n=\sum_{j=0}^3\binom3j\binom nj j!=n^3+2n+1.
\]
Fix any edge \(e\). Matchings containing \(e\) correspond bijectively to arbitrary matchings of \(K_{2,n-1}\). Hence their number is
\[
Q_n=1+2(n-1)+(n-1)(n-2)=n^2-n+1.
\]
For any frequency support \(S\), write \(B_S\) for the number of matchings whose intersection with \(S\) has odd cardinality. Every such matching contains at least one edge of \(S\), whence \(B_S\le|S|Q_n\) and
\[
W_n(S)=N_n-2B_S\ge N_n-2|S|Q_n.
\]
If \(n\) is even, \(N_n\) is odd, and \(W_n(S)\equiv N_n\pmod2\) excludes a zero at every frequency. If \(n\) is odd and \(r=(n+1)/2\), then for \(|S|\le r\) the preceding inequality gives
\[
W_n(S)\ge N_n-(n+1)Q_n=2n>0.
\]

**Sharp positive boundary.** Choose a row vertex \(u\) and a set \(A\) of exactly \(r\) columns. Let \(S_0=\{(u,v):v\in A\}\). The matchings avoiding \(u\) are those of \(K_{2,n}\), numbering \(n^2+n+1\). A matching containing \(u\) chooses one column, with total signed column sum \(n-2r=-1\), and then has \(Q_n\) completions. Therefore
\[
W_n(S_0)=n^2+n+1+(n-2r)Q_n=2n,
\]
so the lower bound at degree \(r\) is attained.

**First zero and its multiplicity lower bound.** Choose any other row vertex \(w\ne u\) and any \(v\in A\), and put \(e=(w,v)\) and \(S=S_0\cup\{e\}\). Matchings containing \(e\) leave a \(K_{2,n-1}\) with row \(u\) having exactly \(r-1\) negative columns. Matchings omitting \(u\) on the residual graph number \(n\). Those using \(u\) have total signed column sum
\[
(n-1)-2(r-1)=n+1-2r=0.
\]
Thus
\[
\sum_{M\in\mathcal M_n\, :\,e\in M}(-1)^{|M\cap S_0|}=n.
\]
Adding \(e\) to the negative-frequency support flips the sign for exactly these matching terms, giving
\[
W_n(S)=W_n(S_0)-2n=0.
\]
There is no lower-degree zero by the previous bound, so the first zero occurs at degree \(r+1\). For \(n\ge3\), \(r\ge2\), and the row containing \(r\) selected edges is uniquely distinguishable from the row containing the one extra edge. All constructed supports are consequently distinct as \(u\), \(A\), \(w\), and \(v\) vary. Their number is
\[
3\cdot\binom nr\cdot2\cdot r=6r\binom nr.
\]
Finally, the Walsh characters diagonalize convolution on the finite abelian group \(G_n\), with eigenvalues \(W_n(S)\). All invertibility and degree-filtered injectivity conclusions follow.

## Verification

The self-contained standard-library programs `verify_walsh.py` and `verify_structural.py` perform exact-integer, independently organized checks. Run `python3 verify_walsh.py` to enumerate all matchings and perform the full Walsh transform at \(n=3,4,5,6,7\), validating parity, the strict positive bound, and every constructed first-degree zero. Run `python3 verify_structural.py` to enumerate signed row-column assignments directly for each integer \(3\le n\le23\), checking the total and boundary identities without a Walsh transform. Expected final markers are `VERIFY_WALSH_OK` and `VERIFY_STRUCTURAL_OK`. These finite checks are supplemental; the preceding proof covers all graph orders.

## Relationship to prior work

Classical rectangular-board rook polynomial coefficients count the same underlying matchings and yield \(N_n\); they do **not by themselves** provide the first frequency degree where the parity-weighted matching sum cancels. Walter's matching-polytope paper studies a quadratic extension of incidence-vector convex hulls, not Walsh zero sets. Leake and Ryder study matching/independence polynomial stability and real-root bounds, not this Fourier recovery threshold. Earlier finite analyses of the complete bipartite matching model at one fixed board size and work on spanning-tree indicators address different claims; no all-\(n\) implication of the present matching threshold follows from them. The signed-root and parity interpretation remains a possible route to an unindexed equivalent result.

## Limitations

No claim is made that the exhibited \(6r\binom nr\) zeros exhaust all first-degree zeros; for example, direct enumeration at \(n=5\) finds \(270\) first-degree zeros compared with \(180\) from this construction. Neither the full spectral multiplicity nor the total nullity at odd widths is determined here. The proof assumes a complete bipartite graph with exactly three vertices on one side and includes *all* partial matchings with weight one. The published-priority comparison is bounded rather than a proof of global novelty.

## References

1. E. W. Weisstein, “Rook Polynomial,” Wolfram MathWorld, https://mathworld.wolfram.com/RookPolynomial.html (rectangular-board matching counts, citing Riordan's 1958 treatment).
2. Matthias Walter, “Complete Description of Matching Polytopes with One Linearized Quadratic Term for Bipartite Graphs,” first posted 2016-07-07, arXiv:1607.01880, https://arxiv.org/abs/1607.01880 .
3. Jonathan Leake and Nick Ryder, “Generalizations of the Matching Polynomial to the Multivariate Independence Polynomial,” first posted 2016-10-04, arXiv:1610.00805, https://arxiv.org/abs/1610.00805 .
