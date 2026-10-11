# Sharp TxGraffiti equality on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\) and \(\Delta(G)\ge2\). Let \(\alpha(G)\) be its independence number, \(a(G)\) its annihilation number, and \(R(G)\) its Havel--Hakimi residue. Then
\[
\Delta(G)\alpha(G)=a(G)+R(G)
\]
holds if and only if
\[
G\cong P_3,\quad K_3,\quad C_4,\quad\text{or}\quad K_4.
\]
A structural estimate used in the classification is
\[
a(G)\le \Delta(G)
\]
for every connected complete multipartite graph.

## Assumptions and scope
All graphs are finite, simple, and undirected. A complete multipartite graph is written \(K_{n_1,\ldots,n_r}\) with all \(n_i\ge1\) and \(r\ge2\). If its order is \(N\), let \(m=\min_i n_i\) and \(M=\max_i n_i\). Then \(\Delta(G)=N-m\) and \(\alpha(G)=M\). The annihilation number is the largest integer \(j\) for which the sum of the \(j\) smallest degrees is at most \(e(G)\). The residue is the number of zeros left after iterated Havel--Hakimi reduction.

The source theorem of Gupta applies to connected graphs with \(\Delta\ge2\), and its equality criterion states that equality in \(\Delta\alpha\ge a+R\) holds exactly when \(a=(\Delta-1)\alpha\) and \(R=\alpha\).

## Proof
First prove \(a(G)\le\Delta(G)\). There are \(N\) degrees. The \(m-1\) largest degrees are each at most \(\Delta=N-m\). Therefore the sum of the remaining \(N-m+1=\Delta+1\) smallest degrees is at least
\[
2e(G)-(m-1)\Delta.
\]
A smallest part has \(m\) vertices, each adjacent to all \(\Delta\) vertices outside that part, so the \(m\Delta\) edges incident with this part are distinct. Hence \(e(G)\ge m\Delta>(m-1)\Delta\). Consequently
\[
2e(G)-(m-1)\Delta>e(G).
\]
Thus the \(\Delta+1\) smallest degrees already have sum greater than \(e(G)\), proving \(a(G)\le\Delta\).

Now suppose equality holds in Gupta's inequality. Its equality criterion gives
\[
a=(\Delta-1)\alpha=(\Delta-1)M.
\]
Combining this with \(a\le\Delta\) gives
\[
(\Delta-1)M\le\Delta.
\]
If \(\Delta\ge3\), then \(M<2\), so \(M=1\). Hence every part is a singleton and \(G=K_N\), with \(\Delta=N-1\). For \(K_N\), one has \(a=\lfloor N/2\rfloor\), \(R=1\), and \(\alpha=1\). Equality requires
\[
N-1=\lfloor N/2\rfloor+1,
\]
which, for \(N\ge4\), holds only at \(N=4\). Thus \(K_4\) is the only equality graph with \(\Delta\ge3\).

It remains to consider \(\Delta=2\). Then \(N-m=2\), and the inequality above gives \(M\le2\). If \(m=1\), then \(N=3\), and the complete multipartite possibilities are \(K_{2,1}\cong P_3\) and \(K_{1,1,1}\cong K_3\). If \(m=2\), then \(N=4\), and the only possibility is \(K_{2,2}\cong C_4\). Direct calculation gives respectively
\[
(\alpha,a,R,\Delta)=(2,2,2,2),(1,1,1,2),(2,2,2,2),(1,2,1,3),
\]
for \(P_3,K_3,C_4,K_4\), so each listed graph attains equality. This completes the classification.

## Verification
The accompanying `verify.py` independently constructs degree multisets for every complete multipartite isomorphism type of order at most \(20\), computes \(a\) from its defining degree-sum inequality, computes \(R\) by Havel--Hakimi reduction, and checks both \(a\le\Delta\) and the equality classification. It checks \(2693\) multipartite types. The finite computation is a stress test only; the theorem is proved analytically above.

## Relationship to prior work
Gupta's 2026 paper proves \(\Delta\alpha\ge a+R\) for every connected graph with \(\Delta\ge2\), gives the exact equality criterion \(a=(\Delta-1)\alpha\) and \(R=\alpha\), and records \(K_4\) as an equality example. The paper does not discuss complete multipartite graphs or classify equality within that family. The present finding turns the invariant-based equality criterion into an isomorphism classification for the entire complete multipartite class, and shows that the only equality examples there are \(P_3,K_3,C_4,K_4\).

Larson and Pepper characterize graphs satisfying \(a=\alpha\), which is a different equality problem. Their result does not imply the classification above because Gupta's sharpness condition requires \(a=(\Delta-1)\alpha\) together with \(R=\alpha\).

## Limitations
The classification is only for complete multipartite graphs. It does not classify all equality graphs for Gupta's inequality. The finite verifier covers orders through \(20\) and is not used as a proof of the infinite statement. Literature searches can miss unindexed or newly posted sources; no covering complete-multipartite sharpness classification was located in the checked sources.

## References
1. C. Gupta, *An annihilation-number Caro-Wei bound: a TxGraffiti conjecture and an independence-number bracket*, arXiv:2606.29553v1, first public 2026-06-28, DOI 10.48550/arXiv.2606.29553.
2. C. E. Larson and R. Pepper, *Graphs with equal Independence and Annihilation Numbers*, Electronic Journal of Combinatorics 18 (2011), P180, DOI 10.37236/667.
