# Logarithmic Gaussian jamming and a parity-folded Poisson crossover on clique coronas

## Finding
Let \(H_n=K_n\circ K_1\), consisting of an \(n\)-vertex complete core with one private pendant leaf at each core vertex. Run irreversible random sequential edge-dimer adsorption, with unit deposition rate per currently available core–core edge and rate \(w>0\) per currently available core–leaf edge. Let \(K_{n,w}\) count deposited pendant dimers, and let \(V_{n,w}\) count unoccupied leaves at jamming. All core vertices are eventually occupied and \(V_{n,w}=n-K_{n,w}\), with \(K_{n,w}\equiv n\pmod 2\).

For every \(n\ge1\), the exact generating polynomial \(F_{n,w}(z)=\mathbb E[z^{K_{n,w}}]\) is determined by
\[
F_{0,w}(z)=1,\qquad F_{1,w}(z)=z,\qquad
F_{n,w}(z)=\frac{2wz}{n-1+2w}F_{n-1,w}(z)+\frac{n-1}{n-1+2w}F_{n-2,w}(z)\quad(n\ge2).
\]
For every **fixed** \(w>0\), as \(n\to\infty\),
\[
\mathbb EK_{n,w}=w\log n+O_w(1),\quad
\operatorname{Var}(K_{n,w})\sim w\log n,\quad
\frac{K_{n,w}-w\log n}{\sqrt{w\log n}}\ \Longrightarrow\ N(0,1).
\]
For the unweighted case \(w=1\), writing \(H_r=\sum_{j=1}^{r}1/j\) and \(H_0=0\), the means are exactly
\[
\mathbb EK_{2r,1}=2H_{2r}-H_r-1+\frac1{2r+1}\quad(r\ge1),\qquad
\mathbb EK_{2r+1,1}=2H_{2r+2}-H_{r+1}-1\quad(r\ge0).
\]
In particular, \(\mathbb EK_{n,1}=\log n+\gamma+\log2-1+o(1)\).

There is a distinct weak-channel limit. Let \(w_n>0\) satisfy \(w_n\log n\to c\), for some \(0\le c<\infty\). If \(P_c\) has the Poisson distribution of mean \(c\), then, **separately along each parity subsequence**,
\[
K_{2r,w_{2r}}\ \Longrightarrow\ P_c+\mathbf1_{\{P_c\text{ odd}\}},\qquad
K_{2r+1,w_{2r+1}}\ \Longrightarrow\ P_c+\mathbf1_{\{P_c\text{ even}\}}.
\]
Thus the inverse-logarithmic pendant-edge weight is a sharp natural crossover between finitely many, parity-constrained leaf depositions and logarithmically many Gaussian-fluctuating depositions.

## Assumptions and scope
The graph is finite and simple; there are \(n\) core vertices and \(n\) private leaves. A deposited dimer permanently occupies both endpoints. Every unoccupied edge with unoccupied endpoints has an independent exponential attempt clock with the stated rate, equivalently the next deposited edge is drawn proportionally to its rate among available edges. All statements concern the terminal configuration, not physical deposition duration. The weight is strictly positive for every finite \(n\); the weak-channel theorem permits positive weights tending to zero, but not setting them identically to zero. The probability laws concern deposited pendant dimers, or equivalently the deficit \(n-V_{n,w}\) in unoccupied leaves.

## Proof
**Exact reduction and parity.** Suppose \(k\) core vertices remain unoccupied. Their private leaves also remain unoccupied, while all formerly active leaves belong to already occupied core vertices and are isolated. Hence exactly \(\binom{k}{2}\) core–core edges of rate one and \(k\) pendant edges of rate \(w\) are available. The conditional probability of selecting a pendant edge is
\[
p_k(w)=\frac{kw}{\binom{k}{2}+kw}=\frac{2w}{k-1+2w} \quad(k\ge1).
\]
A pendant deposition decreases \(k\) by one and adds one to \(K\); a core–core deposition decreases \(k\) by two. At \(k=1\) the pendant edge is certain to deposit. Thus the core empties completely, \(n=K+2C\) for the number \(C\) of core–core dimers, and the generating-function recurrence follows by conditioning on the first transition.

**A pairwise compensator bound.** Visit levels \(k=n,n-1,\dots,0\) downward, with jumps of one or two. Exclude the forced level \(k=1\) and write \(Y_n\) for the number of pendant transitions at levels \(k\ge2\). Let \(I_k\) indicate a pendant deposition at a visited level, and define its predictable compensator and bracket
\[
A_n=\sum_{\substack{k\ge2\\k\text{ visited}}}p_k(w),\qquad
Q_n=\sum_{\substack{k\ge2\\k\text{ visited}}}p_k(w)(1-p_k(w)).
\]
Then \(M_n=Y_n-A_n\) is a square-integrable martingale with jumps of absolute size at most one and predictable quadratic variation \(Q_n\).

For each consecutive pair of levels \(\{2j-1,2j\}\), at least one level is visited (jumps never exceed two). If exactly one is visited and \(j\ge2\), its contribution to \(A_n\) is \(w/j+O_w(j^{-2})\). Both levels can be visited only when a pendant transition occurs at level \(2j\); the probability of that event is at most \(p_{2j}(w)=O_w(j^{-1})\). The extra contribution in a double-visited pair is \(O_w(j^{-1})\). The lowest pair, and the possible top unpaired level, contribute \(O_w(1)\). Summing the deterministic errors and applying Minkowski's inequality to the random extras gives
\[
A_n=wH_{\lfloor n/2\rfloor}+O_{L^2,w}(1)=w\log n+O_{L^2,w}(1).
\]
Indeed, if \(B_j\) is the indicator that both levels of pair \(j\) are visited, then \(\mathbb EB_j\le p_{2j}(w)\le C_w/j\) and
\[
\left\|\sum_{j\ge2}\frac{B_j}{j}\right\|_2
\le\sum_{j\ge2}\frac{\sqrt{\mathbb EB_j}}j
\le\sqrt{C_w}\sum_{j\ge2}j^{-3/2}<\infty.
\]
Moreover \(0\le A_n-Q_n\le\sum_{k\ge2}p_k(w)^2=O_w(1)\). Hence \(Q_n/\log n\to w\) in probability and \(\mathbb EQ_n=w\log n+O_w(1)\). The bounded-jump martingale central limit theorem yields \(M_n/\sqrt{w\log n}\Longrightarrow N(0,1)\). Finally, parity determines whether level \(1\) is visited:
\[
K_{n,w}=Y_n+\mathbf1_{\{n-Y_n\text{ odd}\}}.
\]
This correction is bounded by one. The stated central limit theorem and mean follow. The \(L^2\) bound on \(A_n-w\log n\), together with \(\mathbb EM_n^2=\mathbb EQ_n\), shows \(\operatorname{Var}(K_{n,w})=w\log n+O_w(\sqrt{\log n})\), proving its asserted equivalent.

**Exact mean at unit weight.** At \(w=1\), set \(\mu_k=\mathbb EK_{k,1}\) and \(\Delta_k=\mu_k-\mu_{k-1}\). The recurrence yields \(\Delta_1=1\) and
\[
\Delta_k=\frac{2}{k+1}-\frac{k-1}{k+1}\Delta_{k-1}.
\]
Multiplying by \(k(k+1)\) and solving the alternating recurrence gives \(\Delta_{2j-1}=1/(2j-1)\) and \(\Delta_{2j}=1/(2j+1)\). Summation yields the two displayed harmonic-number identities and their asymptotic constant.

**Weak-channel Poisson crossover.** Put \(w=w_n\to0\). For \(j\ge2\), uniformly for \(0<w\le1\), a single visit within \(\{2j-1,2j\}\) contributes \(w/j+O((w+w^2)/j^2)\). An extra visit has mean at most \(O(w^2/j^2)\). Including the bottom and top boundaries,
\[
\mathbb E\big|A_n-w_n H_{\lfloor n/2\rfloor}\big|=O(w_n+w_n^2),
\]
so \(A_n\to c\) in \(L^1\). Also \(\max_{k\ge2}p_k(w_n)\to0\), \(\sum_{k\ge2}p_k(w_n)^2=O(w_n^2)\), and \(\sum_{k\ge2}p_k(w_n)\le2w_n H_{n-1}=O(1)\). For any \(0\le z\le1\), the stopped process
\[
\frac{z^{Y_n}}{\prod_{\substack{k\ge2\\ k\text{ visited}}}(1+(z-1)p_k(w_n))}
\]
is the terminal value of a mean-one nonnegative martingale; its denominator is bounded away from zero uniformly for large \(n\). The denominator converges in \(L^1\) to \(e^{c(z-1)}\) by the compensator and squared-hazard bounds. Uniform boundedness permits taking expectations, yielding \(\mathbb Ez^{Y_n}\to e^{c(z-1)}\). Hence \(Y_n\Longrightarrow\operatorname{Poisson}(c)\). The exact parity identity for \(K_{n,w}\) then gives the two claimed subsequential laws.

## Verification
Run `python3 verify_corona.py` using Python 3.9 or later and only the standard library. The checker independently enumerates the full labeled edge process, and compares its exact rational output to the two-step reduced recursion for multiple edge weights and sizes. It checks exact parity and the closed harmonic means, and tests selected large-size moment asymptotics numerically. The reported run passed 259 assertions. The infinite-limit results are established by the proof above, not by finite enumeration.

## Relationship to prior work
Gamarnik and Goldberg (arXiv:0807.1277, first publicly posted 2008-07-08) study greedy matchings on regular high-girth or bounded-degree graphs; their Theorems 5–6 do not yield the exact distribution or the logarithmic/weak-channel crossover on this highly heterogeneous degree-growing corona. Pippenger (1989) studies graph adsorption and edge matching, primarily on low-cycle and regular structures; its accessible abstract does not establish the present corona results, and its full text could not be checked. Tavakoli (2022) classifies extremal saturation numbers for corona graph products, not the stochastic greedy output law. Separate research on general-position polynomials of the same corona graph concerns a different graph invariant and does not determine this adsorption process. The precise terminal distribution, logarithmic normal law, and parity-folded rare-event crossover are not implications of these inspected results.

## Limitations
No conclusion is claimed for a different deposition convention, for weights that are exactly zero at finite size, or for arbitrary graph cores. The fixed-weight central limit theorem assumes \(w\) does not depend on \(n\); the Poisson regime assumes strictly positive \(w_n\) with \(w_n\log n\) convergent. The proof gives terminal statistics, not the elapsed adsorption time. Historical priority is provisional: the 1989 Pippenger full text and possibly unindexed equivalent work were inaccessible, so outside coverage cannot be ruled out by search alone. Independent scientific audit has not been performed.

## References
1. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277v1 (2008-07-08), https://arxiv.org/abs/0807.1277.
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. **2** (1989), 393–401, https://doi.org/10.1137/0402034.
3. M. Tavakoli, *On a Conjecture about the Saturation Number of Corona Product of Graphs*, Journal of Mathematics **2022**, 3375246, https://doi.org/10.1155/2022/3375246.
