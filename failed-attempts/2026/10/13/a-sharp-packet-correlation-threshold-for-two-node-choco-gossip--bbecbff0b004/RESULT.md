# A sharp packet-correlation threshold for two-node CHOCO-Gossip

## Finding

**Theorem (exact mask-correlation phase diagram).** Apply the two-node scalar, memory-based compressed-consensus iteration of Koloskova–Stich–Jaggi with complete-averaging weights and consensus gain \(\gamma=1\). In each iteration independently of previous iterations, the two nodewise transmission masks \(\delta_1,\delta_2\in\{0,1\}\) have joint law
\[
\Pr(0,0)=\Pr(1,1)=q,\qquad
\Pr(1,0)=\Pr(0,1)=\tfrac12-q,\qquad 0\le q\le\tfrac12.
\]
Thus each marginal is Bernoulli \(1/2\), regardless of \(q\); the Pearson correlation of the masks is \(4q-1\). Start with \(x_1^{(0)}=d_0/2\), \(x_2^{(0)}=-d_0/2\), \(d_0\ne0\), and zero cached states. Put \(d_k=x_1^{(k)}-x_2^{(k)}\). Then
\[
\begin{array}{ll}
0\le q<1/3:&\mathbb E[d_k^2]\longrightarrow0\text{ geometrically};\\
q=1/3:&\mathbb E[d_k^2]\longrightarrow\tfrac25 d_0^2;\\
1/3<q\le1/2:&\limsup_{k\to\infty}(\mathbb E[d_k^2])^{1/k}>1.
\end{array}
\]
Consequently mean-square consensus has the **sharp** condition \(q<1/3\), equivalent to mask correlation \(4q-1<1/3\). Independent masks (\(q=1/4\)) converge in mean square, whereas identically shared masks (\(q=1/2\)) exhibit a geometrically growing subsequence, despite equal per-node success probability and identical expected message volume.

## Assumptions and scope

There are exactly two scalar nodes. Their mixing matrix is \(W=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix}\). At each integer time \(k\ge0\), both nodes evaluate their differences from their cached states, apply masks, update caches, and then update node states:
\[
\hat x_i^{(k+1)}=\hat x_i^{(k)}+\delta_i^{(k)}(x_i^{(k)}-\hat x_i^{(k)}),
\quad
x_i^{(k+1)}=x_i^{(k)}+\tfrac12(\hat x_j^{(k+1)}-\hat x_i^{(k+1)}),\quad j\ne i.
\]
One pair of masks is drawn each round, independent of the current state and of other rounds, but the two masks within a round may be correlated. Both cached states initially equal zero; the initial node states are antisymmetric, so the conserved node mean is zero. The endpoint gain \(\gamma=1\) is an explicitly defined parameter choice outside the **sufficient small-step guarantee** in the original CHOCO-Gossip theorem, not a contradiction to that guarantee. Exact real arithmetic is assumed.

## Proof

Let \(d=x_1-x_2\), \(h=\hat x_1-\hat x_2\), \(c=\hat x_1+\hat x_2\), with state vector \(u=(d,h,c)^{\mathsf T}\). Setting \(s=(\delta_1+\delta_2)/2\) and \(t=(\delta_2-\delta_1)/2\), direct substitution gives
\[
 u^+=A_{\delta_1,\delta_2}u,\qquad
 A_{\delta_1,\delta_2}=\begin{pmatrix}
 1-s&s-1&-t\\s&1-s&t\\-t&t&1-s
 \end{pmatrix}.
\]
The law is invariant under exchanging the two one-sided masks. Since \(c_0=0\), the mixed moments \(\mathbb E[dc]\) and \(\mathbb E[hc]\) vanish at all times. In the invariant symmetric-moment sector \(m=(\mathbb E[d^2],\mathbb E[dh],\mathbb E[h^2],\mathbb E[c^2])^{\mathsf T}\), we obtain \(m_{k+1}=T(q)m_k\) with
\[
T(q)=\begin{pmatrix}
q/2+1/4&-q-1/2&q/2+1/4&1/4-q/2\\
1/4-q/2&q&-q/2-1/4&q/2-1/4\\
q/2+1/4&1/2-q&q/2+1/4&1/4-q/2\\
1/4-q/2&q-1/2&1/4-q/2&q/2+1/4
\end{pmatrix}.
\]
Because \(m_0=d_0^2(1,0,0,0)^{\mathsf T}\), a cofactor computation yields the rational generating function
\[
G_q(z):=\sum_{k\ge0}\frac{\mathbb E[d_k^2]}{d_0^2}z^k
=\frac{-2(z-2)(qz^2-4qz+2)}{D_q(z)},
\]
\[
D_q(z)=2qz^4-(6q+1)z^3+(18q+1)z^2-(20q+6)z+8.
\]
For \(q>1/3\), \(D_q(0)=8>0\) but \(D_q(1)=2(1-3q)<0\). Hence a real root \(z_*\in(0,1)\) exists. At every such \(z_*\), the numerator is nonzero: \(2-z_*>0\) and \(qz_*^2-4qz_*+2=2-qz_*(4-z_*)\ge1/2\) on the full domain. Therefore \(G_q\) has a singularity with modulus below one. Since its Taylor coefficients are nonnegative, Cauchy–Hadamard implies \(\limsup_k(\mathbb E[d_k^2]/d_0^2)^{1/k}>1\).

At \(q=1/3\),
\[
D_{1/3}(z)=\tfrac13(z-1)(2z^3-7z^2+14z-24).
\]
For \(|z|\le1\), \(|2z^3-7z^2+14z|\le23<24\); therefore all other poles lie strictly outside the closed unit disk. The simple pole at one has coefficient \(\lim_{z\to1}(1-z)G_{1/3}(z)=2/5\). Coefficient extraction yields \(\mathbb E[d_k^2]/d_0^2=2/5+O(\rho^k)\) for some \(0<\rho<1\).

For \(0\le q<1/3\), define
\[
P_q=\frac1{1-3q}\begin{pmatrix}2(2-3q)&-1&0\\-1&5-6q&0\\0&0&5-12q\end{pmatrix}.
\]
Direct multiplication establishes the exact identity
\[
P_q-\sum_{a,b\in\{0,1\}}\Pr(\delta_1=a,\delta_2=b)A_{a,b}^{\mathsf T}P_qA_{a,b}=I_3.
\]
The three leading principal minors are
\[
\frac{2(2-3q)}{1-3q},\qquad
\frac{36q^2-54q+19}{(1-3q)^2},\qquad
\frac{(5-12q)(36q^2-54q+19)}{(1-3q)^3},
\]
all strictly positive for \(0\le q<1/3\). Thus \(P_q\) is positive definite. Conditional expectation yields strict mean-square contraction in the positive-definite \(P_q\)-norm, so \(\mathbb E\|u_k\|^2\), and hence \(\mathbb E[d_k^2]\), decay geometrically. This also proves mean-square stability of all three state coordinates in this range. The three regimes are exhaustive.

## Verification

Run `python verify.py` with Python 3.10 or later and SymPy. The standalone checker reconstructs the nodewise update for all four mask outcomes, derives the exact symmetric second-moment operator, verifies the rational generating numerator and denominator, checks the critical pole and Lyapunov identity, and independently enumerates all nonzero exact-weight paths through six updates for \(q\in\{0,1/4,1/3,1/2\}\). It completes 11,176 exact path cases. The symbolic identities and analytic inequalities above, not finite enumeration, establish the claims for every \(q\) in the interval and every iteration count.

## Relationship to prior work

Koloskova, Stich and Jaggi introduced CHOCO-Gossip, the cached-state update and Bernoulli message transmission; their general result gives a sufficient, smaller consensus gain rather than the exact endpoint-gain phase diagram under varying cross-node mask dependence. Shi, Johansson and Johansson established the importance of correlated bidirectional failures for a **different, memoryless asynchronous gossip operator**; its criteria do not determine the cached-state second-moment threshold here. Suresh, Sun, Ro and Yu analyzed correlated communication for distributed mean estimation and optimization, rather than this specific memory-based gossip recurrence. The contribution is not the cached-state algorithm or Bernoulli compression, but the exact phase boundary when the two marginals are held fixed and only their within-round coupling varies.

## Limitations

The result concerns two scalar nodes, symmetric mixing, a fixed endpoint gain, Bernoulli half-success marginals, independent rounds, and the stated initialization. It does not establish a universal sharp bound for arbitrary graphs, dimensions, node-success probabilities, time correlations, or small-step regimes. It distinguishes second moments; no almost-sure classification is claimed. An equivalent independent analysis in unindexed literature cannot be excluded; independent audit has not been performed.

## References

1. A. Koloskova, S. U. Stich and M. Jaggi, *Decentralized Stochastic Optimization and Gossip Algorithms with Compressed Communication*, arXiv:1902.00340v1 (first public 2019-02-01), particularly Algorithm 1, §3.4–3.5 and Appendix C. https://arxiv.org/html/1902.00340v1
2. G. Shi, M. Johansson and K. H. Johansson, *Randomized Gossip Algorithm with Unreliable Communication*, arXiv:1203.6028v1 (2012). https://arxiv.org/html/1203.6028v1
3. A. T. Suresh, Z. Sun, J. H. Ro and F. Yu, *Correlated Quantization for Distributed Mean Estimation and Optimization*, arXiv:2203.04925v2 (2022). https://arxiv.org/html/2203.04925v2
