# A two-round rank-loss obstruction for positive-diagonal consensus on stars

## Finding
For every integer \(m\ge2\), any sequence of nonnegative row-stochastic, positive-diagonal matrices supported on a bidirectional \(m\)-leaf star that produces a rank-one consensus product requires at least
\[
T\ge 2m-1=2n-3,\qquad n=m+1.
\]
In fact, if \(P_t=A_t\cdots A_1\) (with \(P_0=I\)), it is impossible to have both \(\operatorname{rank}(P_t)<\operatorname{rank}(P_{t-1})\) and \(\operatorname{rank}(P_{t+1})<\operatorname{rank}(P_t)\). At \(m=2\) the bound is attained by a three-round exact *average* consensus construction.

## Assumptions and scope
The vertices are \(0,1,\ldots,m\), with hub \(0\) and leaves \(1,\ldots,m\). Each \(A_t\) is a real \((m+1)\)-square nonnegative row-stochastic matrix, \((A_t)_{ii}>0\) for all vertices, and \((A_t)_{ij}=0\) whenever distinct \(i,j\) are both leaves. All other edge weights and holding probabilities may vary arbitrarily with \(t\); no reversibility, symmetry, preservation of arithmetic average, or fixed weighting is assumed. Exact consensus means all rows of the product coincide; since it is row stochastic, this is equivalent to rank one. This is a *lower bound*, not a characterization of the minimum feasible length at all star sizes.

## Proof
**1. Every admissible factor has corank at most one.** Write any such factor as
\[
A=\begin{pmatrix}
\alpha&b_1&\cdots&b_m\\
c_1&a_1&&0\\
\vdots&&\ddots&\\
c_m&0&&a_m
\end{pmatrix},\qquad a_i=1-c_i>0,\quad b_i\ge0,\quad c_i\ge0,\quad \alpha=1-\sum_i b_i>0.
\]
The \(m\) leaf rows are linearly independent because their restriction to the leaf columns is the invertible positive diagonal matrix \(\operatorname{diag}(a_i)\). Thus \(\operatorname{rank}(A)\ge m\), and any singular factor has rank exactly \(m\).

**2. Null-vector transversality.** If a factor \(A\) is singular, every nonzero *left* null vector \(w\) has \(w_0\ne0\), with
\[
w_i=-\frac{b_i}{a_i}w_0\qquad(1\le i\le m).
\]
For any singular factor \(B\), write its leaf self-weights as \(d_i>0\) and its leaf-to-hub entries as \(e_i\ge0\). Every nonzero *right* null vector \(k\) has \(k_0\ne0\) and
\[
k_i=-\frac{e_i}{d_i}k_0.
\]
Therefore
\[
w^{\mathsf T}k=w_0k_0\left(1+\sum_{i=1}^m\frac{b_i e_i}{a_i d_i}\right)\ne0.
\]
As \(\operatorname{im}A=(\ker A^{\mathsf T})^\perp\), the one-dimensional space \(\ker B=\operatorname{span}(k)\) intersects \(\operatorname{im}A\) trivially. Hence \(B\) is injective on \(\operatorname{im}A\).

**3. Rank drops must be separated.** A rank drop at time \(t\) implies \(A_t\) is singular. At the following round, if \(A_{t+1}\) is invertible, it cannot lower rank. If it is singular, Step 2 shows it is injective on \(\operatorname{im}A_t\), and thus also on the subspace \(\operatorname{im}(P_t)\subseteq\operatorname{im}A_t\). Therefore \(\operatorname{rank}(P_{t+1})=\operatorname{rank}(P_t)\). No two consecutive rank drops occur. Each drop decreases rank by at most one, and going from \(n=m+1\) to rank one requires at least \(m\) drops. A length-\(T\) binary sequence without adjacent marked positions has at most \(\lceil T/2\rceil\) marked positions. Consequently \(m\le\lceil T/2\rceil\), or \(T\ge 2m-1\).

**4. Attainment on the three-vertex star.** Let
\[
A_1=\begin{pmatrix}1/2&1/2&0\\1/2&1/2&0\\0&0&1\end{pmatrix},\quad
A_2=\begin{pmatrix}1/2&0&1/2\\0&1&0\\5/6&0&1/6\end{pmatrix},\quad
A_3=\begin{pmatrix}2/3&1/3&0\\2/3&1/3&0\\1/2&0&1/2\end{pmatrix}.
\]
All are row stochastic, have positive diagonal, and respect the star, and direct rational multiplication gives
\[
A_3A_2A_1=\frac13\mathbf1\mathbf1^{\mathsf T}.
\]
Thus the bound is optimal when \(m=2\).

## Verification
The proof is algebraic for every integer \(m\ge2\). The standalone standard-library script `verify_star.py` checks exact rational multiplication of the three-round witness and independently tests the key orthogonality obstruction on a finite collection of hand-constructed singular star factors; these finite checks are illustrative and are **not** used as evidence for the universal quantifiers. Run `python3 verify_star.py`.

## Relationship to prior work
Hendrickx, Shi and Johansson (arXiv:1302.6668; first made public 2013-02-27) establish finite-time averaging with positive-diagonal stochastic factors on connected undirected networks, including stars, and discuss the question of minimal round counts. Their existence construction and general step bounds do not by themselves imply this \(2n-3\) obstruction for arbitrary time-dependent star factors. Ko's 2010 thesis studies optimal schedules of pairwise and/or symmetric parallel averaging. Imposing symmetry changes the admissible factor class and does not directly entail the unrestricted row-stochastic lower bound here. Ghosh and Lee's 2013 finite-horizon decentralized-controller synthesis uses a different controller model; its accessible abstract does not establish this particular nonnegative-factor rank statement, but the uninspected complete work is a priority risk. The result here is a necessary condition and should not be misread as a claim of optimal general star scheduling.

## Limitations
No matching schedule is established for \(m\ge3\). The positive-diagonal condition is essential to the null-vector formulas. Signed coefficients, leaf–leaf communications, and zero holding probabilities are outside scope. The literature comparison cannot exclude unindexed or inaccessible equivalent proofs, particularly related rank-product results. The self-review does not constitute independent validation.

## References
1. J. M. Hendrickx, G. Shi and K. H. Johansson, *Finite-time consensus using stochastic matrices with positive diagonals*, arXiv:1302.6668, first posted 2013-02-27, https://arxiv.org/abs/1302.6668 ; journal DOI: 10.1109/TAC.2014.2352691.
2. C.-K. Ko, *On Matrix Factorization and Scheduling for Finite-Time Average-Consensus*, Caltech thesis (2010), https://thesis.caltech.edu/5763/01/consensus.pdf.
3. S. Ghosh and J.-W. Lee, *Optimal Finite-Time Consensus on Fixed and Periodic Graphs*, SIAM J. Control Optim. 51 (2013), 3946–3970, DOI: 10.1137/120862478, https://epubs.siam.org/doi/10.1137/120862478.
