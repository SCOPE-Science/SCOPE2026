# Exact Gini contraction of a left-to-right path gossip sweep

## Finding
For every integer \(n\ge2\), consider \(n\) real values arranged along a path. For \(i=1,\ldots,n-1\), let \(T_i\) replace coordinates \(i\) and \(i+1\) by their arithmetic mean, leaving every other coordinate unchanged. Apply these updates once each from left to right:
\[
P_n=T_{n-1}\cdots T_2T_1.
\]
Define the complete-pair Gini seminorm
\[
G_n(x)=\sum_{1\le i<j\le n}|x_i-x_j|.
\]
The exact two-input Lipschitz coefficient of one sweep, modulo constants, is
\[
\boxed{\gamma_n=\sup_{G_n(x-y)>0}\frac{G_n(P_nx-P_ny)}{G_n(x-y)}
=1-\min_{1\le k\le\lfloor n/2\rfloor}
\frac{2(1-2^{-k})}{k(n-k)}.}
\]
The minimum is attained at \(k=1\) for \(2\le n\le4\), at both \(k=1\) and \(k=2\) for \(n=5\), at \(k=2\) for \(n=6\), at \(k=3\) for \(n=7,8\), and **only at** \(k=\lfloor n/2\rfloor\) for every \(n\ge9\). The corresponding binary input \((0,\ldots,0,1,\ldots,1)\), with exactly \(k\) trailing ones, attains the sharp coefficient.

In particular, for every \(n\ge9\) the contraction factor has the closed form
\[
\gamma_n=1-\frac{2(1-2^{-m})}{m(n-m)},\qquad m=\lfloor n/2\rfloor,
\]
and hence
\[
\boxed{\lim_{n\to\infty}n^2(1-\gamma_n)=8.}
\]
The exact values for \(n=2,\ldots,9\) are respectively \(0,\,1/2,\,2/3,\,3/4,\,13/16,\,41/48,\,53/60,\,29/32\).

## Assumptions and scope
All statements concern finite-dimensional real vectors and unweighted arithmetic means. The order is precisely the deterministic path sequence \((1,2),(2,3),\ldots,(n-1,n)\), not simultaneous averaging, random edge choice, or a different permutation of the edges. The two-input coefficient is well-defined on the quotient \(\mathbb R^n/\operatorname{span}\{\mathbf1\}\), because each \(T_i\) is linear and preserves constant vectors. The unnormalized Gini seminorm is used; any fixed positive scalar normalization leaves the coefficient unchanged. The theorem is not a statement that the best coefficient for an arbitrary edge ordering equals this one.

## Proof
**1. Binary-cut reduction.** More generally, let \(P\) be a linear map with \(P\mathbf1=\mathbf1\). For any real vector \(x\), sort its distinct coordinate levels as \(v_1<\cdots<v_r\), and put \(S_j=\{i:x_i\ge v_{j+1}\}\). Then
\[
x=v_1\mathbf1+\sum_{j=1}^{r-1}(v_{j+1}-v_j)\mathbf1_{S_j}.
\]
Every increment is positive. By the triangle inequality and translation invariance,
\[
G_n(Px)\le\sum_{j=1}^{r-1}(v_{j+1}-v_j)G_n(P\mathbf1_{S_j}),
\]
whereas the exact layer-cake identity is
\[
G_n(x)=\sum_{j=1}^{r-1}(v_{j+1}-v_j)|S_j|(n-|S_j|).
\]
Thus the induced seminorm is the maximum over nonempty proper binary cuts \(S\) of
\[
\frac{G_n(P\mathbf1_S)}{|S|(n-|S|)}.
\]
No positivity assumption on \(P\) is required for this reduction.

**2. Each gossip's exact loss estimate.** Suppose the current pair has values \(a,b\), and let \(q=(a+b)/2\). Its contribution to \(G_n\) falls by \(|a-b|\). Every other coordinate \(w\) contributes an additional nonnegative decrease because
\[
|a-w|+|b-w|\ge 2|q-w|.
\]
Consequently, if \(z^{(i)}=T_i z^{(i-1)}\),
\[
G_n(z^{(0)})-G_n(z^{(n-1)})
\ge\sum_{i=1}^{n-1}|z^{(i-1)}_i-z^{(i-1)}_{i+1}|.
\tag{1}
\]
Equality holds at a step whenever every other coordinate lies outside the open interval between \(a\) and \(b\).

**3. Lower bound on binary-input dissipation.** Fix a binary initial vector with \(k\) ones. Define the carry \(a_1=x_1\) and recursively
\[
a_{i+1}=\frac{a_i+x_{i+1}}2\qquad (1\le i<n).
\]
The two entries averaged at step \(i\) are \(a_i,x_{i+1}\), so the right-hand side of (1) is \(\sum_{i=1}^{n-1}|a_i-x_{i+1}|\). If \(x_1=0\), the carry immediately before the \(j\)-th encounter with an original \(1\) is at most \(1-2^{-(j-1)}\): this holds initially, an encounter with \(0\) can only reduce the carry, and an encounter with \(1\) takes its half-average with \(1\). Thus this encounter contributes at least \(2^{-(j-1)}\). Summing the \(k\) encounters yields
\[
G_n(x)-G_n(P_nx)\ge\sum_{j=1}^k2^{-(j-1)}=2(1-2^{-k}).
\]
If \(x_1=1\), complement all bits. Both the variation and its loss are unchanged, and the number of zeros is \(n-k\). Combining the two cases gives, for every nonconstant binary input,
\[
G_n(P_nx)\le k(n-k)-2(1-2^{-\min(k,n-k)}).
\tag{2}
\]
Dividing by \(k(n-k)\) and applying Step 1 proves the claimed upper bound.

**4. Exact extremizing cuts.** Choose any integer \(1\le k\le\lfloor n/2\rfloor\) and start with \(n-k\) zeros followed by \(k\) ones. Until the first cross-block interaction, all averaged pairs are zeros. On each following interaction, the carried value increases successively through \(1/2,3/4,7/8,\ldots\); the untouched right coordinate equals \(1\). Every previously processed coordinate is no larger than the carry and every untouched coordinate is at least the right member of the averaged pair. Hence every third-party triangle inequality in Step 2 is an equality. The pairwise differences on the nontrivial steps are exactly
\[
1,\quad 1/2,\quad \ldots,\quad 2^{-(k-1)}.
\]
Therefore
\[
G_n(P_nx)=k(n-k)-2(1-2^{-k}),
\]
so every candidate in the minimum formula is genuinely attained; the maximum of their ratios is the exact induced norm.

**5. Optimize the integer parameter.** Put \(d_n(k)=2(1-2^{-k})/[k(n-k)]\). For any \(1\le k<\lfloor n/2\rfloor\), direct cross-multiplication gives
\[
d_n(k+1)<d_n(k)
\ \Longleftrightarrow\
k(n-k)<2(2^k-1)(n-2k-1).
\tag{3}
\]
For \(k=1\), inequality (3) holds exactly when \(n>5\) and is an equality at \(n=5\). For \(k=2\) it holds when \(n\ge7\); for \(k=3\) it holds when \(n\ge9\). For every \(k\ge4\) in the admissible range, \(n\ge2k+2\). The right side of (3) minus the left side increases with \(n\), since its slope is \(2(2^k-1)-k>0\). It is already strictly positive at \(n=2k+2\), because
\[
2(2^k-1)>k(k+2)\quad\text{for all integers }k\ge4.
\]
The last inequality holds at \(k=4\), and its positive margin strictly increases when \(k\) is incremented. These comparisons give the stated exceptional small sizes and show strict decrease of \(d_n(k)\) through the entire admissible range for \(n\ge9\). Finally, \(m(n-m)=\lfloor n^2/4\rfloor\), while \(1-2^{-m}\to1\), so \(n^2(1-\gamma_n)\to8\). This proves every assertion.

## Verification
The standalone file `check_gossip_gini.py` uses exact rational arithmetic, computes \(P_n\) explicitly for every nontrivial binary cut at \(2\le n\le12\), and compares the resulting maximum with the theorem's formula. It also checks the claimed suffix witnesses and compares all candidate integer minima for \(9\le n\le160\). Its last line is `ALL_ORDERED_GOSSIP_GINI_EXACT_CHECKS_PASS`. These finite checks corroborate the formula; they do not establish its unrestricted validity, which follows from Steps 1–5.

## Relationship to prior work
Pairwise averaging and deterministic complete gossip sequences are classical, notably in Liu–Mou–Morse–Anderson–Yu, *Deterministic Gossiping* (2011), which studies periodic and aperiodic convergence and spectral/singular-value contraction. Liu–Morse–Anderson–Yu, *The Contraction Coefficient of a Complete Gossip Sequence* (2010), studies a matrix Euclidean seminorm for complete sequences. Charron-Bost–Függer–Nowak (2014) treat averaging algorithms in highly dynamic networks, with general consensus and time-complexity results. Boyd–Ghosh–Prabhakar–Shah (2006) study randomized gossip by spectral methods. Cao (2021) studies Gini decay in an averaged stochastic interaction model. The present statement instead fixes a deterministic, one-pass path edge order and determines the *exact induced complete-pair absolute-difference seminorm*, including the sharp optimizing cut and its size transition. Neither a spectral-gap convergence estimate nor a per-edge nonincrease inequality, by itself, determines this exact coefficient. A comprehensive historical priority claim is not made.

## Limitations
The coefficient depends on the fixed left-to-right order. No exact claim is made for nonuniform averaging weights, other edge orders, weighted Gini dispersions, nonlinear updates, simultaneous sweeps, or repeated sweeps' *optimal* long-time rate. The theorem provides the one-sweep induced norm; its powers need not have norms equal to corresponding powers of \(\gamma_n\). The proof does not classify *all* possible nonbinary extremizers. The literature review cannot exclude every unindexed or inaccessible treatment of the same specific seminorm.

## References
1. J. Liu, S. Mou, A. S. Morse, B. D. O. Anderson, C. Yu, *Deterministic Gossiping*, Proceedings of the IEEE 99 (2011), 1505–1524. DOI: 10.1109/JPROC.2011.2159689.
2. J. Liu, A. S. Morse, B. D. O. Anderson, C. Yu, *The Contraction Coefficient of a Complete Gossip Sequence*, in *Distributed Computing and Networking* (2010). DOI: 10.1007/978-3-642-11278-2_19.
3. B. Charron-Bost, M. Függer, T. Nowak, *Approximate Consensus in Highly Dynamic Networks: The Role of Averaging Algorithms*, arXiv:1408.0620, first submitted August 4, 2014. https://arxiv.org/abs/1408.0620
4. S. Boyd, A. Ghosh, B. Prabhakar, D. Shah, *Randomized Gossip Algorithms*, IEEE Transactions on Information Theory 52 (2006). DOI: 10.1109/TIT.2006.874516.
5. F. Cao, *Explicit decay rate for the Gini index in repeated averaging model*, arXiv:2108.07904 (2021). https://arxiv.org/abs/2108.07904
