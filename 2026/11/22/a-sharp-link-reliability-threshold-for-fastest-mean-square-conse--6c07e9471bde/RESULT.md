# A sharp link-reliability threshold for fastest mean-square consensus on the four-cycle

## Finding
Consider one step of synchronous linear consensus on the four-cycle, where every undirected edge is independently available with probability \(p\in(0,1]\). For a common gain \(h\in[0,1/2]\), write \(W=I-hL_\xi\), with \(L_\xi\) the Laplacian of the available edges. All these step matrices are nonnegative, symmetric and stochastic. Successive availability patterns are independent and identically distributed.

The exact worst-initial-condition asymptotic squared-disagreement rate is
\[
\mathcal R(p,h)=1-6ph+(7p^2+3p)h^2+ph\sqrt{(33p^2-6p+9)h^2-(20p+4)h+4}.
\]
Specifically, for the orthogonal mean-zero projection \(P\),
\[
\lim_{k\to\infty}\left(\sup_{Px=x,\,\|x\|_2=1}\mathbb E\|W_k\cdots W_1x\|_2^2\right)^{1/k}=\mathcal R(p,h).
\]
For \(0<p<1\) and \(0<h\le1/2\), the same limit holds for **every** nonzero mean-zero initial vector, without taking the supremum.

The gain minimizing this exact asymptotic rate over all nonnegative stochastic steps is unique. Define
\[
p_*=\frac{4-\sqrt5}{11}=0.160357456590928\ldots.
\]
For \(0<p\le p_*\), its value is exactly \(h_*(p)=1/2\). For \(p_*<p<1\), it is the unique root in \((0,1/2)\) of \(\partial_h\mathcal R(p,h)=0\). At \(p=1\), it equals \(1/3\) and the optimal asymptotic rate is \(1/9\). Thus the fastest reliable-edge consensus changes sharply from the largest stochastic gain to an interior gain at the algebraic reliability threshold \(p_*\).

## Assumptions and scope
The underlying graph is the simple four-cycle on vertices \(0,1,2,3\), with edges \((0,1),(1,2),(2,3),(3,0)\). Each edge's Bernoulli indicator is independent of every other edge and of all other rounds, with the same availability probability \(p\). Each active undirected edge contributes \((e_i-e_j)(e_i-e_j)^\mathsf T\) to \(L_\xi\). All agents update simultaneously. The performance criterion is the asymptotic exponential rate of expected **squared Euclidean disagreement from the initial arithmetic mean**, not the expected one-step norm or the expected matrix's spectral rate. There are no additive communication noises. The gain interval \(0\le h\le1/2\) is exactly the interval that makes all possible step matrices nonnegative, since a degree-two vertex can have both edges available.

## Proof
Let \(L\) be the deterministic four-cycle Laplacian. Its eigenvalues are \(0,2,2,4\). The projectors onto the eigenvalues \(2\) and \(4\) are
\[
P_2=\frac{L(4I-L)}4,\qquad P_4=\frac{L(L-2I)}8,
\]
with \(P=P_2+P_4\). Define the covariance operator \(\mathcal T(X)=\mathbb E[WXW]\). It is self-adjoint for the Frobenius inner product. The edge-availability distribution is invariant under every dihedral symmetry of the cycle. Consequently, \(\mathcal T\) maps the two-dimensional space of dihedrally invariant symmetric matrices annihilating the constant vector, spanned by \(P_2,P_4\), into itself.

Expand \(\mathcal T(P_j)=K_{2j}P_2+K_{4j}P_4\) for \(j\in\{2,4\}\). Direct expansion of the four independent Bernoulli edge indicators, or the identity \(\mathbb E[L_\xi XL_\xi]=p^2LXL+p(1-p)\sum_e B_eXB_e\), with \(B_e=(e_i-e_j)(e_i-e_j)^\mathsf T\), gives the exact coefficient matrix
\[
K(p,h)=\begin{pmatrix}
1-4ph+(2p^2+2p)h^2&2p(1-p)h^2\\
4p(1-p)h^2&1-8ph+(12p^2+4p)h^2
\end{pmatrix}.
\]
Its similar symmetric representation in the orthonormal Frobenius basis \(P_2/\sqrt2,P_4\) is
\[
S(p,h)=I-h\operatorname{diag}(4p,8p)+h^2
\begin{pmatrix}2p^2+2p&2\sqrt2p(1-p)\\2\sqrt2p(1-p)&12p^2+4p\end{pmatrix}.
\]
Its largest eigenvalue, by the quadratic formula, is exactly \(\mathcal R(p,h)\) displayed above; the discriminant simplifies to \(4p^2h^2[(33p^2-6p+9)h^2-(20p+4)h+4]\).

For any fixed mean-zero \(x\), independence across rounds, self-adjointness of \(\mathcal T\), and invariance of \(P\) imply
\[
\mathbb E\|W_k\cdots W_1x\|_2^2=x^\mathsf T\mathcal T^k(P)x.
\]
The coefficient vector of \(\mathcal T^k(P)\) is \(K^k(1,1)^\mathsf T\). If \(0<p<1\) and \(h>0\), every entry of \(K\) is strictly positive: off-diagonals are manifestly positive, while the no-edge event contributes \((1-p)^4P_j\) to each diagonal. Perron–Frobenius therefore gives the strictly positive leading coefficient and asymptotic rate \(\rho(K)=\mathcal R(p,h)\) for every nonconstant \(x\). At \(p=1\), the deterministic two-mode multipliers are \((1-2h)^2\) and \((1-4h)^2\), so the worst-case rate is their maximum, which equals the same formula. At \(h=0\) the rate is \(1\).

The quadratic coefficient \(C(p)\) of \(S(p,h)\) is positive definite for \(p>0\), because its upper-left entry is \(2p(p+1)>0\) and
\[
\det C(p)=16p^3(p+3)>0.
\]
Thus \(S(p,h)\) is **strictly convex in the positive-definite matrix order** as a function of \(h\). Its largest eigenvalue is consequently strictly convex in \(h\). For \(0<p<1\), its off-diagonal is positive whenever \(h>0\), making \(\mathcal R\) differentiable there; its right derivative at zero is \(-4p<0\). Hence there is exactly one unconstrained minimizer, and the minimizer on \([0,1/2]\) is at the upper boundary exactly when \(\partial_h\mathcal R(p,1/2)\le0\).

Writing \(Q(p)=33p^2-46p+17\) and \(N(p)=33p^2-36p+11\), which are strictly positive on \([0,1]\), direct differentiation gives
\[
\frac{\partial_h\mathcal R(p,1/2)}p=7p-3+\frac{N(p)}{\sqrt{Q(p)}}.
\]
For \(p\ge3/7\) this is positive. For \(0<p<3/7\), both \(N(p)\) and \(3-7p\) are positive; thus the sign of the derivative equals the sign of
\[
N(p)^2-(3-7p)^2Q(p)=-16(p-1)(3p-2)(11p^2-8p+1).
\]
Within \((0,3/7)\), this changes sign exactly at the smaller root \((4-\sqrt5)/11\): negative below and positive above. Strict convexity now proves every asserted optimizing regime and the uniqueness at the transition. At \(p=1\), minimizing \(\max\{(1-2h)^2,(1-4h)^2\}\) gives the unique \(h=1/3\), with rate \(1/9\).

## Verification
Run `python verify_c4.py` with SymPy installed. The standalone checker independently enumerates all \(16\) Bernoulli subgraphs for each spectral projector, reconstructs \(K\), checks the discriminant and positive-definite quadratic coefficient symbolically, verifies the exact factorization for the threshold, and checks example rates. It reports `PASS`. These finite and symbolic checks corroborate the explicit algebra; the proof above supplies the all-parameter and infinite-iteration justification.

At \(p=3/4\) and \(h=2/5\), one obtains \(\mathcal R=7/25\); this is **not** the optimizing gain for infinite-round decay, despite being the gain equalizing the two one-step spectral energies. At \(p=1\), the unique optimal rate is \(1/9\).

## Relationship to prior work
Patterson, Bamieh and El Abbadi (2010) give a general covariance-recursion and spectral-radius characterization for consensus with independent stochastic link failures, including the uniform-probability model. Their operator framework is an essential precursor, but the inspected complete paper does not provide the closed four-cycle spectral formula or the exact reliability threshold for optimizing a nonnegative gain. The present result is a graph-specific **optimization of the true asymptotic covariance rate**, rather than a new general covariance theory or an optimal *one-step* energy bound. Battilotti, Cacace and d'Angelo (2023) analyze random-subgraph consensus in distributed filtering, using sufficient gain conditions and error bounds; their examined formulas do not yield this exact four-cycle switching threshold. Other consensus-rate and deterministic fastest-mixing results employ different objectives or non-random communication patterns. These comparisons support provisional priority only, not exhaustive historical novelty.

## Limitations
This theorem concerns the four-cycle, iid equal-probability undirected link availability, common fixed scalar gain and nonnegative stochastic updates. It neither optimizes unequal edge weights nor handles temporal correlation, directed failures, asynchronous updates, noisy messages, arbitrary graphs or finite-time expected squared error. The general covariance-recursion method is previously known. Independent verification of historical priority and mathematical correctness has not been performed.

## References
- S. Patterson, B. Bamieh, A. El Abbadi, *Convergence Rates of Distributed Average Consensus with Stochastic Link Failures*, IEEE Transactions on Automatic Control 55 (2010), 880–892, https://doi.org/10.1109/TAC.2010.2041998 ; publicly available author's version: https://sites.engineering.ucsb.edu/~bamieh/pubs/patbamela09tac.pdf .
- S. Battilotti, F. Cacace, M. d'Angelo, *Consensus analysis of random sub-graphs for distributed filtering with link failures*, first public arXiv submission 2023-05-08, https://arxiv.org/abs/2305.04555v1 .
- S. Patterson, B. Bamieh, A. El Abbadi, *Distributed average consensus with stochastic communication failures*, Proceedings of the 46th IEEE Conference on Decision and Control (2007), https://doi.org/10.1109/CDC.2007.4434917 .
