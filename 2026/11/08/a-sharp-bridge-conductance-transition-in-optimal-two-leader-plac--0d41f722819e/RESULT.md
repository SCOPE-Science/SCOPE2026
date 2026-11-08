# A sharp bridge-conductance transition in optimal two-leader placement on unequal clique barbells

## Finding

For integers \(3\le p\le q\) and a real bridge conductance \(t>0\), join disjoint unit-edge complete graphs \(K_p\) and \(K_q\) by a single edge of conductance \(t\) between distinguished gateway vertices \(g_p\) and \(g_q\). All other vertices are *internal*. Let \(L\) be the weighted combinatorial Laplacian. For each two-element leader set \(S\), let \(F=V\setminus S\) and minimize
\[
J(S)=\operatorname{tr}\bigl((L_{FF})^{-1}\bigr).
\]
Every grounded matrix is positive definite, since the graph is connected and \(S\ne\varnothing\). The complete optimal-set classification is:

- If \(p=q\), **every and only** optimal pair consists of one internal vertex in each clique, for all \(t>0\).
- If \(p<q\), define the sharp threshold
\[
\tau(p,q)=\frac{p^2(q+2)}{4(q-p)}.
\]
For \(0<t<\tau(p,q)\), **every and only** optimal pair consists of one internal vertex in each clique. At \(t=\tau(p,q)\), these pairs tie exactly with pairs comprising an internal vertex of \(K_p\) and the gateway \(g_q\). For \(t>\tau(p,q)\), **every and only** optimal pair comprises an internal vertex of \(K_p\) and \(g_q\).

Consequently the respective counts of optimal pairs for \(p<q\) are \((p-1)(q-1)\), \(q(p-1)\), and \(p-1\); for \(p=q\) the count is \((p-1)^2\). The optimal inverse trace is exactly
\[
J_* = 4-\frac2p-\frac2q-\max\left\{
\frac{t[p^2(q+2)+q^2(p+2)]}{pq[pq+2(p+q)t]},\quad
\frac{t(p+2)}{p(p+2t)}\right\}.
\]
At equal clique sizes, the first improvement in the maximum is always strictly larger.

## Assumptions and scope

All within-clique edges have unit conductance; the only inter-clique edge joins the two gateways and has conductance \(t>0\). The sizes \(p,q\) are arbitrary **integers at least three**, with labels chosen so that \(p\le q\). Leaders are noise-free: their states are fixed, leaving the grounded follower matrix \(L_{FF}\). Two **distinct** vertices are selected, and all choices are allowed. The objective is the unscaled inverse trace; for unit-intensity independent white disturbances in the follower consensus dynamics, steady-state total variance is \(J(S)/2\). Equal and unequal clique orders, exact threshold equality, and all positive bridge conductances are included. The claim concerns neither a controllability rank test nor zero forcing.

## Proof

**1. Exhaustion of placement types.** In either clique, a vertex is a distinguished gateway \(G\) or one of the exchangeable internal vertices \(I\). The automorphism group fixing the gateways is transitive on internal vertices within each clique. Thus all two-element sets fall into exactly eight types. Use subscripts \(p,q\) where necessary, and let \(\Phi=4-2/p-2/q\). Types \(GG,IG,GI,II\) have one leader in each clique; in these labels the first letter refers to \(K_p\). Types \(GA,AA\) consist of a gateway plus internal vertex, or two internal vertices, within \(K_p\), respectively. Types \(GB,BB\) are the analogous two configurations in \(K_q\). Their objective values are precisely
\[
\begin{aligned}
J_{GG}&=\Phi,\\
J_{IG}&=\Phi-\frac{t(p+2)}{p(p+2t)},\\
J_{GI}&=\Phi-\frac{t(q+2)}{q(q+2t)},\\
J_{II}&=\Phi-\frac{t[p^2(q+2)+q^2(p+2)]}{pq[pq+2(p+q)t]},\\
J_{GA}&=\Phi+\frac qt-\frac{p+2}{2p},\\
J_{GB}&=\Phi+\frac pt-\frac{q+2}{2q},\\
J_{AA}&=J_{GA}+\frac{3q}{2p},\\
J_{BB}&=J_{GB}+\frac{3p}{2q}.
\end{aligned}
\]

Here is a direct finite-dimensional derivation, valid for all the stated parameters. If a clique of order \(s\in\{p,q\}\) contains \(r\ge1\) internal *followers*, then its \(r-1\)-dimensional zero-sum internal subspace is an invariant eigenspace of \(L_{FF}\) with eigenvalue \(s\). On the complementary space of vectors constant on each internal-follower class, the row-value quotient has internal-class diagonal \(s-r\), internal-to-follower-gateway coefficient \(-1\), gateway-to-internal coefficient \(-r\), and follower-gateway diagonal \(s-1+t\). If both gateways are followers, their cross coefficients are \(-t\); otherwise those entries are omitted. When \(r=0\), omit the internal class entirely. Thus the inverse trace equals the inverse trace of a nonsingular quotient matrix of dimension at most four, plus \(\sum_s(r_s-1)/s\) over nonempty internal-follower classes. This restriction is similar to the symmetric normalized-constant restriction, so its inverse trace is basis independent. Substituting the zero, one, or two removed vertices for each of the eight types and inverting the displayed at-most-four-dimensional quotient gives the eight rational expressions above. This derivation also includes \(p=3\) or \(q=3\), where a zero-sized follower class is omitted.

**2. Elimination of all but two types.** Direct subtraction from the expressions gives the following exact nonnegative-gap certificates for \(q\ge p\ge3\) and \(t>0\):
\[
\begin{aligned}
J_{GG}-J_{II}&=\frac{t[p^2q+2p^2+pq^2+2q^2]}{pq[pq+2(p+q)t]}>0,\\
J_{GI}-J_{IG}&=\frac{t(q-p)[pq+2p+2q+4t]}{pq(p+2t)(q+2t)}\ge0,\\
J_{GA}-J_{IG}&=\frac{2pq+(4q-p-2)t}{2t(p+2t)}>0,\\
J_{GB}-J_{IG}&=\frac{2p^3q+p^2(3q-2)t+4(q-p)t^2}{2pqt(p+2t)}>0,\\
J_{AA}-J_{GA}&=\frac{3q}{2p}>0,\\
J_{BB}-J_{GB}&=\frac{3p}{2q}>0.
\end{aligned}
\]
The second gap is zero only for equal clique sizes; nevertheless that case still cannot be optimal because \(J_{IG}>J_{II}\), as shown next. Each omitted type is strictly dominated by either \(IG\) or \(II\). This comparison exhausts **all** leader choices, not just representative examples.

**3. Exact switching boundary.** The remaining difference factors as
\[
J_{IG}-J_{II}=\frac{t[p^2(q+2)-4(q-p)t]}{q(p+2t)[pq+2(p+q)t]}.
\]
Its denominator is positive. When \(p=q\), the numerator is positive for every \(t>0\); when \(p<q\), its sign changes exactly once, at \(\tau(p,q)\). The sign establishes the three regimes including exact equality. All members of any optimal type are equivalent under permutations of internal vertices, so their counts are as stated. Taking the lesser of \(J_{II}\) and \(J_{IG}\) proves the claimed optimal value.

## Verification

The accompanying standard-library Python file `verify.py` constructs the weighted graph and grounded Laplacian **independently** of the quotient formulas. It performs exact rational Gauss–Jordan inversion, exhausts every two-leader set for \(114\) choices of small clique orders and rational bridge weights (including ten threshold ties), and compares all \(5109\) resulting objectives to the eight rational formulas. It additionally checks each sign-factor identity over a separate exact-rational parameter grid. The recorded replay terminates with `VERIFY_OK`. Exact finite tests support the algebra but are **not** used as proof for infinitely many orders or real conductances; that follows from the quotient derivation and rational sign certificates in the proof.

Reproduce with `python3 verify.py` in the same directory. No third-party packages or source downloads are required.

## Relationship to prior work

Lin, Fardad and Jovanović (arXiv:1302.0450, first public 2013-02-03) establish the noise-free inverse-grounded-Laplacian selection formulation and general relaxation/greedy algorithms, but not an exact two-clique barbell weight transition. Fitch and Leonard (arXiv:1407.1569, first public 2014-07-07) derive general joint-centrality expressions and explicit path/cycle cases, rather than the present asymmetric bridge-weight classification. Patterson, McGlohon and Dyagilev (arXiv:1412.6595, first public 2014-12-20) provide algorithms for weighted one-dimensional path/ring networks; a barbell with cliques of order at least three is not in those families. Patterson, Yi and Zhang (arXiv:1708.06873, first public 2017-08-23) formulate a resistance-distance method and analyze cycles, paths and trees; their exact listed classes do not supply this result. The known zero-forcing polynomial of bridge barbells addresses a different property of input placement and does not imply optimal inverse trace or the conductance threshold.

These comparisons distinguish the explicit global eight-orbit classification and strict threshold from the general, already-known leader-selection objective and inverse-trace machinery. They do not constitute a proof of publication priority.

## Limitations

The theorem does not extend by this proof to more than two leaders, clique orders below three, nonuniform edges inside cliques, multiple inter-clique bridges, finite-gain noisy leaders, or objectives other than the stated inverse trace. Its scientific contribution is the **sharp all-size weight-dependent placement transition and all minimizers** on this natural graph family; it does not claim that inverse-trace optimization, its general matrix formulas, or graph automorphism quotienting are new. Relevant literature outside the identified inspected sources could contain equivalent or stronger statements, so publication priority remains subject to further specialist verification.

## References

1. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for leader selection in stochastically forced consensus networks*, arXiv:1302.0450, first public 2013-02-03, https://arxiv.org/abs/1302.0450 .
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first public 2014-07-07, https://arxiv.org/abs/1407.1569 .
3. S. Patterson, N. McGlohon, and K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first public 2014-12-20, https://arxiv.org/abs/1412.6595 .
4. S. Patterson, Y. Yi, and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873, first public 2017-08-23, https://arxiv.org/abs/1708.06873 .
