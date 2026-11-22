# Kemeny-optimal double-star walks and an exact reversal against fastest mixing

## Finding
Let \(D_{p,q}\) be the tree with adjacent hubs, \(p\ge2\) pendant vertices at the first hub and \(q\ge2\) at the second. Write \(N=p+q+2\), and optimize the zero-target Kemeny spectral sum
\[
\mathcal K(P)=\sum_{j=2}^{N}\frac{1}{1-\lambda_j(P)}
\]
over **all** symmetric, entrywise-nonnegative, irreducible row-stochastic matrices supported on the tree and diagonal, without requiring identical pendant-edge probabilities in advance. Define
\[
A=\frac{(N-1)(p^2+q^2)}{N},\qquad B=\frac{(p+1)(q+1)}{N}.
\]
There is exactly one optimal transition matrix. Its hub-to-hub probability and individual pendant probabilities are, respectively,
\[
z_* = \frac{\sqrt B}{\sqrt A+\sqrt B},\qquad
 a_* = \frac{\sqrt A}{p(\sqrt A+\sqrt B)},\qquad
 b_* = \frac{\sqrt A}{q(\sqrt A+\sqrt B)}.
\]
Both hubs have zero holding probability; the pendant vertices have holding probabilities \(1-a_*\) and \(1-b_*\). The exact global optimum is
\[
\boxed{\mathcal K_*(p,q)=(\sqrt A+\sqrt B)^2.}
\]
At a fixed total of \(s=p+q\ge4\) leaves, this minimum is strictly decreasing as \(pq\) increases: the most balanced double star minimizes it among allowable shapes, and \((p,q)=(2,s-2)\) or its reflection maximizes it. Equality occurs only for reflected parameter pairs.

There is a sharp, counterintuitive **objective reversal** on the balanced family \(p=q=k\ge2\). Write
\[
D_k=1+k(3+2\sqrt2),\qquad
 a_{\rm mix}=\frac{2+\sqrt2}{D_k},\qquad
 z_{\rm mix}=\frac{1+k(1+\sqrt2)}{D_k}.
\]
The unique symmetric stochastic walk minimizing the second-largest eigenvalue modulus (SLEM) assigns \(a_{\rm mix}\) to every pendant edge and \(z_{\rm mix}\) to the bridge, whereas the maximum-degree walk assigns probability \(1/(k+1)\) to every edge. **For every \(k\ge2\), the fastest-mixing chain has strictly *larger* Kemeny cost than even the maximum-degree chain.** More precisely, putting
\[
 A_k=\frac{k^2(2k+1)}{k+1},\qquad B_k=\frac{k+1}{2},
\]
we have
\[
\mathcal K_{\rm mix}=\frac{A_k}{1-z_{\rm mix}}+\frac{B_k}{z_{\rm mix}},\qquad
\mathcal K_{\rm md}=\frac{5k^2+4k+1}{2}
\]
and the *exact positive gap certificate*
\[
\boxed{
\mathcal K_{\rm mix}-\mathcal K_{\rm md}
=\frac{k(8+5\sqrt2)(k-1)\bigl(7k^2+(3\sqrt2-2)k+\sqrt2-3\bigr)}
{14(4+3\sqrt2)(k+1)(k-1+\sqrt2)}>0.}
\]
Furthermore, as \(k\to\infty\), the optimal-Kemeny bridge probability is asymptotic to \(1/(2\sqrt k)\), whereas \(z_{\rm mix}\to\sqrt2-1\). The exact performance-ratio limits are
\[
\lim_{k\to\infty}\frac{\mathcal K_{\rm mix}}{\mathcal K_*}
=1+\frac1{\sqrt2},\qquad
\lim_{k\to\infty}\frac{\mathcal K_{\rm md}}{\mathcal K_*}=\frac54.
\]
Thus a chain that is provably fastest mixing loses approximately \(70.7\%\) in the Kemeny metric relative to its optimum and asymptotically performs worse in that metric than the uncomplicated maximum-degree chain.

## Assumptions and scope
All graphs are finite, connected, undirected simple double stars. Each edge supports a strictly positive transition probability; nonedges carry none. A feasible \(P\) is real, symmetric, stochastic, nonnegative entrywise, and irreducible. Self-loops are allowed, so stochasticity imposes at most unit off-diagonal mass in every row. The spectral sum excludes the stationary eigenvalue \(1\), corresponding to the *zero-on-target* first-hitting-time convention (some sources add an overall constant \(1\) for return-on-target conventions). The minimization is over independently adjustable edge probabilities, **not** over fixed uniform neighbor probabilities or arbitrary reversible chains with nonuniform stationary distributions. The graph-shape comparison requires integer \(p,q\ge2\) with fixed sum; the mixing comparisons require balanced \(p=q=k\ge2\).

## Proof
**1. An exact tree spectral identity.** Set \(L=I-P\), the weighted graph Laplacian with conductance \(w_e=P_{uv}\) on edge \(e=uv\). Since \(P\) is symmetric and irreducible, \(L\) is positive definite on \(\mathbf1^\perp\) and \(\mathcal K(P)=\operatorname{tr}(L^+)\). For a connected weighted graph of order \(N\), its Kirchhoff index is \(N\operatorname{tr}(L^+)\); this follows from
\[
\sum_{u<v}(e_u-e_v)(e_u-e_v)^\top=NI-\mathbf1\mathbf1^\top.
\]
A tree's resistance between two vertices is the sum of reciprocal edge conductances along their unique connecting path. Therefore, if deletion of \(e\) leaves components of sizes \(s_e\) and \(N-s_e\), then
\[
\mathcal K(P)=\frac1N\sum_e\frac{s_e(N-s_e)}{w_e}.
\]
No spectral approximation is used.

**2. Reduction without assuming exchangeability.** Denote individual pendant probabilities on the two sides by \(a_1,\ldots,a_p>0\) and \(b_1,\ldots,b_q>0\), and bridge probability by \(z>0\). Removing a pendant edge yields cut sizes \(1,N-1\); removing the bridge yields \(p+1,q+1\). Consequently,
\[
\mathcal K(P)=\frac{N-1}{N}\left(\sum_{i=1}^p\frac1{a_i}+\sum_{j=1}^q\frac1{b_j}\right)+\frac{(p+1)(q+1)}{Nz}.
\]
The two hub row-sum constraints are \(\sum_i a_i+z\le1\) and \(\sum_j b_j+z\le1\). Thus \(0<z<1\), and Cauchy–Schwarz gives
\[
\sum_i\frac1{a_i}\ge\frac{p^2}{\sum_i a_i}\ge\frac{p^2}{1-z},\qquad
\sum_j\frac1{b_j}\ge\frac{q^2}{1-z}.
\]
Equality throughout demands \(a_i=(1-z)/p\) and \(b_j=(1-z)/q\) **at every leaf**, making both hubs exactly saturated. The resulting weights also satisfy each leaf's row constraint since \(p,q\ge2\). Therefore
\[
\mathcal K(P)\ge f(z):=\frac{A}{1-z}+\frac{B}{z},\qquad 0<z<1.
\]
The second derivative \(f''(z)=2A/(1-z)^3+2B/z^3\) is strictly positive. The unique stationary point satisfies \(\sqrt A/(1-z)=\sqrt B/z\), giving precisely the displayed \(z_*,a_*,b_*\), and \(f(z_*)=(\sqrt A+\sqrt B)^2\). Equality requirements prove uniqueness even among asymmetric chains.

**3. Exact shape monotonicity.** Fix \(s=p+q\ge4\) and write \(u=pq\). Then
\[
\sqrt{(s+2)\mathcal K_*(p,q)}
=\sqrt{(s+1)(s^2-2u)}+\sqrt{u+s+1}.
\]
Its derivative with respect to the real variable \(u\) is strictly negative because the necessary and sufficient squared inequality
\[
4(s+1)(u+s+1)>s^2-2u
\]
holds for every \(u>0,s\ge4\) (the difference is \((4s+6)u+3s^2+8s+4>0\)). Hence balancing strictly improves the optimized Kemeny cost, with the stipulated equality cases.

**4. Comparison with independently optimized mixing.** The displayed fastest-mixing probabilities are the previously established unique SLEM minimizer for balanced double stars; they can also be verified by the sharp Rayleigh vector taking values \(\pm(1+\sqrt2)\) at the two leaf classes and \(\pm1\) at the hubs. This vector yields the lower bound \(\operatorname{SLEM}(P)\ge1-2/D_k\), and the displayed weights saturate it; the antisymmetric two-dimensional Laplacian block has characteristic polynomial
\[
 x^2-((k+1)a_{\rm mix}+2z_{\rm mix})x+2a_{\rm mix}z_{\rm mix},
\]
whose smaller root is \(2/D_k\), while the remaining spectrum does not exceed the corresponding SLEM bound. Equality in the Rayleigh and row constraints forces the individual leaf weights and bridge weight, establishing uniqueness (the referenced primary proof supplies full details). In particular, \(k a_{\rm mix}+z_{\rm mix}=1\), so the tree identity gives \(\mathcal K_{\rm mix}=A_k/(1-z_{\rm mix})+B_k/z_{\rm mix}\).

For the maximum-degree walk, each edge has probability \(1/(k+1)\); substitution into the same identity gives \(\mathcal K_{\rm md}=(5k^2+4k+1)/2\). Direct rationalization in the field \(\mathbb Q(\sqrt2)\) yields the displayed exact gap factorization. Every denominator is positive, and \(7k^2+(3\sqrt2-2)k+\sqrt2-3>0\) for \(k\ge2\); hence the gap is strict. The case \(k=1\), outside our double-star shape range, would be equality, showing the boundary is sharp.

**5. Limiting ratios.** In the balanced case,
\[
 A_k=2k^2+O(k),\qquad B_k=k/2+O(1),\qquad z_*\sim\frac1{2\sqrt k}.
\]
The known mixing optimizer satisfies \(z_{\rm mix}\to\sqrt2-1\). Thus
\[
\mathcal K_*\sim2k^2,\qquad
\mathcal K_{\rm mix}\sim(2+\sqrt2)k^2,\qquad
\mathcal K_{\rm md}\sim\frac52 k^2,
\]
proving both ratios. The derivation is exact up to the expressly identified asymptotic statements.

## Verification
The standalone `verify.py` reconstructs weighted Laplacians and compares the trace of an exact shifted inverse against the tree cut formula for \(16\) heterogeneous rational configurations, checks all derived optimizer probabilities, compares \(1{,}800\) fully nonuniform feasible assignments, scans integer shape balancing on leaf totals through \(64\), checks the independently known fastest-mixing probabilities on \(39\) sizes, symbolically factors the fastest-mixing versus maximum-degree gap, and checks all the asserted limits. Execute `python verify.py` with dependencies in `requirements.txt`. Its successful report is `VERIFY_OK: 2008 independent exact/numerical checks; bridge and Kemeny asymptotic limits`. Exact inequalities and uniqueness for infinite graph families are established by the proof, not by finite computational tests.

## Relationship to prior work
Boyd, Diaconis and Xiao (2004) formulated globally fastest symmetric Markov mixing under graph constraints, with SLEM rather than Kemeny as objective. Patel, Agharkar and Bullo (2015, with a 2014 conference version) showed convexity and semidefinite representability of the fixed-stationary Kemeny design problem but did not report a double-star exact optimizer or our cross-objective comparisons in the inspected material. Zeng (2021) studied standard *degree-stationary* random walks on weighted trees with a fixed multiset of weights and optimization over tree shapes; that feasible set differs from freely chosen **uniform-stationary symmetric transition matrices**. Durastante, Gnazzo and Meini (2026) developed constrained Kemeny-improving perturbation algorithms, not this exact parametric double-star classification. A previously published sharp SLEM solution on balanced double stars gives the explicitly cited mixing-optimal weights used in this comparison, but its objective does not imply Kemeny minimization, and inserting those weights here actually gives a strictly worse Kemeny score than maximum-degree weights. Generic convex SDP formulations cannot by themselves imply the explicit formulas, balancing law or the positive gap certificate.

## Limitations
The theorem assumes perfect symmetry of transition probabilities \(P_{ij}=P_{ji}\), a uniform stationary distribution, positive permitted tree-edge probabilities and optional holding, and optimizes the *zero-target* Kemeny sum rather than SLEM or other objectives. The exact optimum is graph-specific; no general optimum for arbitrary trees is asserted. The comparison to the already published fastest-mixing theorem uses its explicit known optimal allocation, with the new algebraic Kemeny gap verified independently. Coincidental equivalent results outside the inspected literature cannot be categorically excluded.

## References
1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review 46 (2004), 667–689; electronic release 2004-10-29; DOI:10.1137/S0036144503423264. https://stanford.edu/~boyd/papers/pdf/fmmc.pdf
2. R. Patel, P. Agharkar, F. Bullo, *Robotic Surveillance and Markov Chains with Minimal Weighted Kemeny Constant*, IEEE Transactions on Automatic Control 60 (2015), 3156–3167; DOI:10.1109/TAC.2015.2426317. https://motion.me.ucsb.edu/pdf/2014b-pab.pdf
3. J. Zeng, *On average hitting time and Kemeny's constant for weighted trees*, arXiv:2109.09249v1 (2021-09-19). https://arxiv.org/abs/2109.09249
4. F. Durastante, M. Gnazzo, B. Meini, *Kemeny’s constant minimization for reversible Markov chains via structure-preserving perturbations*, BIT Numer. Math. 66 (2026), article 59; DOI:10.1007/s10543-026-01152-6. https://link.springer.com/article/10.1007/s10543-026-01152-6
5. *A sharp and unique fastest-mixing walk on balanced double stars* (2026), publicly accessible result and proof. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-and-unique-fastest-mixing-walk-on-balanced-double-stars--12785a469e7f
