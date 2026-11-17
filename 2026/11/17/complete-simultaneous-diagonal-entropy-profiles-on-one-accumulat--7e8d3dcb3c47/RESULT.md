# Complete simultaneous diagonal entropy profiles on one-accumulation compacta of the binary shift

## Finding
For every nonempty compact subset \(K\) of the one-sided binary full shift, define its diagonal entropy scales \(D_p(K)\), \(p\ge2\), as below. Its complete infinite profile is either identically zero, or for a unique integer \(p\ge2\) and real \(0<a\le1\) it has
\[
D_j(K)=0\ (2\le j<p),\qquad D_p(K)=a,\qquad D_j(K)=1\ (j>p).
\]
Every one of these profiles, including all endpoint cases \(a=1\), is attained by a **countably infinite compact set with exactly one accumulation point** in the binary full shift. These compact sets are not asserted to be invariant under the shift.

## Assumptions and scope
Let \(\Sigma_2=\{0,1\}^{\mathbb N_0}\) carry the metric \(d(x,y)=2^{-\min\{i:x_i\ne y_i\}}\) for distinct points, and let \(\sigma\) be the left shift. The Bowen metric is \(d_n(x,y)=\max_{0\le i<n}d(\sigma^ix,\sigma^iy)\). Write \(r_n(K,\epsilon)\) for the minimal number of Bowen balls of radius \(\epsilon\) covering \(K\). Set \(\ell_0(t)=t\), \(\ell_{q+1}(t)=\log(e+\ell_q(t))\). Write \(L_q=\log^{\circ q}\) on sufficiently large arguments. For every integer \(p\ge2\),
\[
D_p(K)=\lim_{\epsilon\downarrow0}\limsup_{n\to\infty}\frac{\ell_p(r_n(K,\epsilon))}{L_{p-1}(n)}.
\]
This is the upper-capacity diagonal-entropy convention of Huang–Li, not Bowen's covering entropy for arbitrary non-invariant subsets.

## Proof
**1. Universal compatibility.** Because a binary word of length \(n+C_\epsilon\) determines a Bowen ball, \(r_n(K,\epsilon)\le2^{n+C_\epsilon}\) for each fixed \(\epsilon\). Hence \(0\le D_p(K)\le1\). If \(D_p(K)>0\), there is a fixed \(\epsilon>0\), a constant \(c>0\), and arbitrarily large \(n\) with \(\ell_p(r_n(K,\epsilon))\ge c L_{p-1}(n)\). Applying another logarithm gives
\[
\ell_{p+1}(r_n(K,\epsilon))\ge \log(c L_{p-1}(n)) +o(1)=L_p(n)+O(1).
\]
Consequently \(D_{p+1}(K)=1\). Induction gives the stated necessary staircase pattern, since there is either no positive coordinate or a least such coordinate.

**2. A single-accumulation prefix construction.** Let \(f(n)\) be eventually increasing, unbounded, with \(\log n=o(f(n))\), \(f(n)\le n\), and with \(f(n+1)-f(n)\le1\) for all sufficiently large integers. Modify finitely many values and take \(k(n)=\lfloor f(n)\rfloor\), so that \(k(0)=0\), \(k(n+1)-k(n)\in\{0,1\}\), and \(k(n)=f(n)+O(1)\) eventually. Let \(F\subset\mathbb N_0\) contain exactly the positions where \(k\) increases; hence \(|F\cap[0,n)|=k(n)\). Select integers \(0=n_0<n_1<n_2<\cdots\) such that \(k(n_{j-1})/k(n_j)\to0\), and put \(B_j=F\cap[n_{j-1},n_j)\). Define
\[
K_f=\{0^\infty\}\ \cup\ \bigcup_{j\ge1}\{x\in\Sigma_2:\operatorname{supp}(x)\subseteq B_j\}.
\]
Every individual layer is finite and has support entirely in a disjoint finite interval receding to infinity; therefore \(K_f\) is countably infinite and compact, with \(0^\infty\) as its unique accumulation point. Let \(P_f(n)\) be its number of length-\(n\) prefixes. There are at most \(n\) nonempty contributing layers, so
\[
P_f(n_j)\ge 2^{k(n_j)-k(n_{j-1})}\quad\text{for each }j,\qquad P_f(n)\le 1+n2^{k(n)}\quad\text{for every }n\ge1.
\]
Since \(k(n)\gg\log n\) and \(k(n_{j-1})=o(k(n_j))\), fixed-resolution Bowen coverings satisfy \(r_n(K_f,2^{-R})=P_f(n+R)\) for an immaterial choice of integer radius convention. In particular, for each fixed \(q\ge2\),
\[
D_q(K_f)=\limsup_{n\to\infty}\frac{L_{q-1}(f(n))}{L_{q-1}(n)}
\]
whenever the right-hand ratio has a limit. For the upper bound take iterated logs of \(P_f(n)\le1+n2^{k(n)}\); for the lower bound use \(n_j\), noting \(k(n_j)-k(n_{j-1})\sim k(n_j)\). A shift of \(n\) by a fixed \(R\) does not change the limits for the controls used below.

**3. Realization, including the endpoints.** Define \(E_0(u)=u\) and \(E_{h+1}(u)=\exp(E_h(u))\). For first positive scale \(p=2\), choose \(f(n)=n^a\), \(0<a\le1\). For \(p\ge3\) and \(0<a<1\), choose
\[
f(n)=E_{p-2}\big((L_{p-2}(n))^a\big).
\]
For \(p\ge3\) and the endpoint \(a=1\), choose
\[
f(n)=E_{p-2}\big(L_{p-2}(n)/L_{p-1}(n)\big).
\]
All are increasing and satisfy the preceding conditions for sufficiently large \(n\): in the latter two cases \(f(n)=n^{o(1)}\), \(f(n)/\log n\to\infty\), and \(f'(n)\to0\); for \(n^a\) the claims are immediate. Finite initial modifications produce the required integer control. For \(0<a<1\), the iterated-log ratios at scales \(p-1\) and \(p\) are respectively zero and \(a\). At the endpoint \(p\ge3\), these are respectively zero and one, because
\[
L_{p-2}(f(n))=L_{p-2}(n)/L_{p-1}(n),\quad
L_{p-1}(f(n))=L_{p-1}(n)-\log L_{p-1}(n).
\]
At \(p=2\), \(L_1(n^a)/L_1(n)=a\). Universal compatibility sets every subsequent coordinate to one, and monotonic propagation backwards shows earlier coordinates are zero. For the all-zero profile take \(K_0=\{0^\infty\}\cup\{x^{(j)}:j\ge0\}\), where \(x^{(j)}\) has one 1 in coordinate \(j\); then \(P_{K_0}(n)=n+1\), and direct iterated-log comparison yields \(D_q(K_0)=0\) for all \(q\ge2\).

## Verification
The identities for the selected control functions follow directly by cancellation of paired iterated logarithms and exponentials; finite prefix checks in `verify.py` provide reproducibility but cannot certify the asymptotic statements. For every fixed radius, Bowen balls here correspond to finite prefixes, so the covering-count bounds hold uniformly in \(n\) with only a fixed indexing shift. The proof applies to every integer \(q\ge2\), not only to finitely many sampled scales.

## Relationship to prior work
Huang and Li (2026), Theorem 1.1, establish hereditary lowerability of **one specified** diagonal-entropy scale at a time; their Section 6.1 also exhibits settings where the upper endpoint is unavailable within the one-accumulation class. Their Section 6.2 gives one-scale constructions inside the full binary shift. The present claim is the simultaneous infinite-coordinate compatibility/classification, including exact first-positive endpoints \(a=1\) in the countable one-accumulation class. The prior single-scale theorem alone does not assert this classification. Xie, Chen, and Zhou (2026) develop entropy scales for topological systems; the complete simultaneous compact-subset classification here is not claimed by their abstract. Historical priority remains subject to further inspection of related literature.

## Limitations
The full converse concerns the one-sided **binary full shift**, not arbitrary positive-entropy dynamical systems. The realizing compact sets need not be shift invariant. It concerns upper-capacity diagonal entropy with the iterated-log normalization above, not variational entropy, measure entropy, or pointwise Lyapunov exponents. Independent review and definitive historical priority have not been established.

## References
1. X. Huang and Z. Li, *Hereditary lowerability of diagonal entropy scales*, arXiv:2611.02638v1 (2026-11-02), https://arxiv.org/abs/2611.02638 .
2. Y. Xie, E. Chen, X. Zhou, *Entropy Scales in Topological Dynamical Systems*, arXiv:2608.10460 (2026), https://arxiv.org/abs/2608.10460 .
3. W. Huang, X. Ye, G. Zhang, *Lowering topological entropy over subsets*, 2010, https://arxiv.org/search/?query=Lowering+topological+entropy+over+subsets&searchtype=all .
