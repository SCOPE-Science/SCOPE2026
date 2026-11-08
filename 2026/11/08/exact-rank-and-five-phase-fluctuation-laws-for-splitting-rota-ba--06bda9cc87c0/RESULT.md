# Exact rank and five-phase fluctuation laws for splitting Rota–Baxter projections on finite Heisenberg Lie algebras

## Finding

Fix a prime power \(q\) and an integer \(n\ge 2\). Let \(H=H_{2n+1}(\mathbb F_q)=V\oplus\mathbb F_q z\), where \(\dim_{\mathbb F_q}V=2n\), \(\omega\) is a nondegenerate alternating bilinear form on \(V\), and \([u+az,v+bz]=\omega(u,v)z\). A **splitting Rota–Baxter projection** is an \(\mathbb F_q\)-linear map \(P:H\to H\) such that \(P^2=P\) and

\[
[Px,Py]=P\bigl([Px,y]+[x,Py]-[x,y]\bigr)\quad(x,y\in H).
\]

For \(0\le s\le n\), define the number of totally isotropic \(s\)-spaces

\[
I_{n,s}(q)={n\brack s}_q\prod_{i=0}^{s-1}(q^{n-i}+1),
\]

where the Gaussian binomial coefficient is \({n\brack s}_q=\prod_{i=0}^{s-1}(q^{n-i}-1)/(q^{s-i}-1)\), with empty products equal to \(1\). Put

\[
M_{n,s}(q)=I_{n,s}(q)q^{s(2n-s+1)}.
\]

**Exact rank law.** The number \(N_{n,r}(q)\) of distinct splitting Rota–Baxter projections of ordinary vector-space rank \(r\) is

\[
N_{n,r}(q)=\begin{cases}
M_{n,r}(q),&0\le r\le n,\\
M_{n,2n+1-r}(q),&n+1\le r\le2n+1.
\end{cases}
\]

Every rank occurs, and \(N_{n,r}(q)=N_{n,2n+1-r}(q)\). In particular the exact total is \(2\sum_{s=0}^{n}M_{n,s}(q)\).

**Entropy and five-phase concentration.** For fixed \(q\), as \(n\to\infty\),

\[
\log_q\bigl(\#\{P\}\bigr)=\tfrac85n^2+\tfrac65n+O_q(1).
\]

Choose \(P\) uniformly, write \(R=\operatorname{rank}P\), and set \(S=\min\{R,2n+1-R\}\), which lies in \(\{0,\ldots,n\}\). For each residue \(t\in\{0,1,2,3,4\}\), along \(n=5m+t\), the integer random variable \(J=S-4m\) converges **in total variation** to the discrete distribution

\[
\Pr(J_\infty=j)=\frac{q^{((8t+3)j-5j^2)/2}}{\displaystyle\sum_{h\in\mathbb Z}q^{((8t+3)h-5h^2)/2}},\qquad j\in\mathbb Z.
\]

The law gives five residue-class-dependent profiles (with possible reflection or translation relations between profiles). Moreover, the events \(R\le n\) and \(R\ge n+1\) each have probability exactly \(1/2\); conditional on either, its lower-side index is distributed as \(S\). Thus the rank lies in two narrow packets near \(4n/5\) and \(6n/5\), with bounded (rather than growing) fluctuations.

## Assumptions and scope

The base field is any finite field \(\mathbb F_q\), including characteristic \(2\). A Lie subalgebra need not contain the center. All operators are distinct linear maps, not equivalence classes under automorphisms. The Rota–Baxter weight is exactly \(-1\); replacing \(P\) with \(-P\) gives an operator of weight \(+1\) satisfying \((-P)^2=-(-P)\). This theorem concerns the *idempotent* weight-\(-1\) subclass, not the set of all Rota–Baxter operators. The main scope is \(n\ge2\); the three-dimensional case \(n=1\) is included only as a finite verification boundary.

## Proof

**1. The splitting criterion.** Let \(P^2=P\), \(B=\operatorname{im}P\), and \(C=\ker P\). Then \(H=B\oplus C\). For \(x=b+c\) and \(y=b'+c'\), the Rota–Baxter identity reduces to

\[
[b,b']=P([b,b']-[c,c']).
\]

With \(c=c'=0\), the equality holds precisely when \([B,B]\subseteq B\). With \(b=b'=0\), it holds precisely when \([C,C]\subseteq C\). These two conditions are also sufficient. Hence splitting Rota–Baxter projections correspond bijectively to **ordered** complementary pairs of Lie subalgebras \((B,C)\).

**2. Subalgebras and the center.** Let \(\pi:H\to V\) be the quotient by \(\mathbb F_qz\). If a Lie subalgebra \(L\) contains \(z\), then \(L=\pi^{-1}(U)=U\oplus\mathbb F_qz\) for one (arbitrary) subspace \(U\le V\). If \(z\notin L\), then \(\pi|_L\) is injective, so \(L\) is the graph \(\{w+\ell(w)z:w\in W\}\) of a unique linear functional \(\ell:W\to\mathbb F_q\) on \(W=\pi(L)\). Lie closure forces \(\omega|_{W\times W}=0\), and this condition is sufficient. Every such \(W\) has dimension at most \(n\).

In a complementary pair \(H=B\oplus C\), both subalgebras cannot contain \(z\), as their intersection would be nontrivial. Neither can both avoid \(z\), since then \(\dim B+\dim C\le2n<2n+1\). Thus exactly one contains \(z\). Suppose it is \(B\). Fix a totally isotropic \(s\)-space \(W=\pi(C)\). The choice of the complement \(U=\pi(B)\) to \(W\) in \(V\) has \(q^{s(2n-s)}\) possibilities (the graphs of arbitrary linear maps from a fixed complement to \(W\)); the graph functional \(\ell:W\to\mathbb F_q\) has \(q^s\) possibilities. This gives \(M_{n,s}(q)\) pairs with \(\operatorname{rank}P=2n+1-s\). Reversing the roles gives the same number with rank \(s\). There is no overcount because \(B\) and \(C\) uniquely determine \(P\).

**3. The symplectic isotropic count.** An ordered basis of an isotropic \(s\)-space is built sequentially. After \(i\) independent mutually orthogonal vectors have been selected, the next vector belongs to their symplectic orthogonal (of dimension \(2n-i\)) but not their span (of size \(q^i\)). Therefore there are \(\prod_{i=0}^{s-1}(q^{2n-i}-q^i)\) ordered isotropic independent tuples. Each isotropic \(s\)-space has \(\prod_{i=0}^{s-1}(q^s-q^i)\) ordered bases. Dividing and rearranging gives the stated formula for \(I_{n,s}(q)\), proving the exact rank law.

**4. A uniformly controlled weight factor.** The preceding product also yields

\[
M_{n,s}(q)=q^{E_{n,s}}F_{n,s}(q),\qquad
E_{n,s}=4ns-\frac{5s^2-3s}{2},
\]

with

\[
F_{n,s}(q)=\frac{\prod_{a=n-s+1}^{n}(1-q^{-2a})}{\prod_{a=1}^{s}(1-q^{-a})}.
\]

Set \(c_q=\prod_{a=1}^{\infty}(1-q^{-2a})>0\) and \(C_q=\prod_{a=1}^{\infty}(1-q^{-a})^{-1}<\infty\). Uniformly for all \(0\le s\le n\),

\[
0<c_q\le F_{n,s}(q)\le C_q<\infty.
\]

The quadratic exponent \(E_{n,s}\) has its real maximum at \((8n+3)/10\). Completing the square yields

\[
E_{n,s}=\frac{(8n+3)^2}{40}-\frac52\left(s-\frac{8n+3}{10}\right)^2.
\]

Hence \(\sum_{s=0}^{n}q^{E_{n,s}}=q^{(8n+3)^2/40+O_q(1)}\): a nearest integer supplies the lower bound, and the uniformly summable discrete-Gaussian tail supplies the upper bound. Multiplication by \(F_{n,s}\in[c_q,C_q]\) changes the logarithm by at most a bounded amount, establishing the entropy statement.

For \(n=5m+t\) and \(s=4m+j\), simple subtraction gives the exact identity

\[
E_{5m+t,4m+j}-E_{5m+t,4m}=\frac{(8t+3)j-5j^2}{2}.
\]

For each fixed integer \(j\), the numerator and denominator products in \(F_{5m+t,4m+j}\) respectively approach \(1\) and \(C_q^{-1}\), so \(F_{5m+t,4m+j}\to C_q\). The preceding uniform bounds dominate all normalized masses by a fixed summable discrete-Gaussian sequence in \(j\). Dominated convergence for series gives convergence of the entire probability mass functions in \(\ell^1(\mathbb Z)\), equivalent to total variation. Finally, swapping \(B,C\) is a fixed-point-free rank-complement involution, so the two rank packets have exactly equal mass.

## Verification

The included `verify.py` uses only the Python standard library. It generates *all* subspaces by reduced row-echelon matrices, independently checks Lie closure and complementary-subalgebra conditions, and compares rank counts for \((n,q)=(1,2),(1,3),(2,2)\). Its separate full-matrix procedure enumerates all \(q^9\) linear endomorphisms in the three-dimensional case for \(q\in\{2,3\}\), directly tests \(P^2=P\), the Rota–Baxter identity on basis pairs, and rank. It also compares the exact rank law to each of the five predicted limiting discrete-Gaussian profiles at \(n=60,61,62,63,64\) over \(\mathbb F_2\).

The checked rank vectors (ranks in increasing order) are

\[
(n,q)=(1,2):\ (1,12,12,1),\quad
(1,3):\ (1,36,36,1),\quad
(2,2):\ (1,240,960,960,240,1).
\]

Every test passed and the verifier printed `VERIFY_OK`. These computations support finite boundary cases and the normalization of the formulas; only the proof covers all finite fields and arbitrary dimension. No external theorem prover, infinite certificate, or independent mathematical audit is claimed.

## Relationship to prior work

The correspondence between splitting Rota–Baxter maps and Lie-subalgebra factorizations is established background (Guo–Lang–Sheng, 2020; Jiang–Sheng–Zhu, 2021). Ji–Hua (2018) and Rathee (2024) classify Rota–Baxter operators on the three-dimensional Heisenberg Lie algebra over algebraically closed or complex fields, respectively. The latter explicitly revisits the former and notes the sign convention for weights. Their rank-one symplectic case is **not** claimed here as new. The present result addresses all higher Heisenberg dimensions \(2n+1\) with \(n\ge2\), counts distinct idempotent maps over every finite field, and proves five nontrivial limiting rank profiles for fixed \(q\).

Published records on subalgebra commutativity degrees of finite Heisenberg Lie algebras concern commuting pairs of subalgebras and different invariants, rather than ordered complementary subalgebra decompositions. The isotropic Grassmannian count is a standard ingredient, explicitly used here rather than claimed as a new count. A comprehensive proof of publication priority is not asserted.

## Limitations

The theorem is restricted to ordinary Heisenberg Lie algebras \(H_{2n+1}(\mathbb F_q)\), \(n\ge2\), and idempotent Rota–Baxter maps of weight \(-1\). It does not enumerate non-idempotent Rota–Baxter maps, Lie-group Rota–Baxter maps, or decompositions of arbitrary two-step nilpotent Lie algebras. The limiting laws hold for fixed \(q\), along the five residue classes of \(n\) modulo \(5\). The finite checker covers small prime fields and two low-dimensional cases, not an exhaustive unbounded verification. Novelty is assessed against inspected accessible evidence and remains subject to external literature review.

## References

- N. Rathee, *Rota–Baxter operators and skew left brace structures over Heisenberg Group*, arXiv:2402.15428v1, first publicly submitted 2024-02-23; full text of v3 (2024-09-26) used for section-level comparison, https://arxiv.org/abs/2402.15428.
- G. Ji and X. Hua, *Rota-Baxter operators of 3-dimensional Heisenberg Lie algebra*, Korean Journal of Mathematics 26 (2018), 53–60, https://doi.org/10.11568/kjm.2018.26.1.53.
- L. Guo, H. Lang and Y. Sheng, *Integration and geometrization of Rota-Baxter Lie algebras*, arXiv:2009.03492v1, first submitted 2020-09-08, https://arxiv.org/abs/2009.03492.
- J. Jiang, Y. Sheng and C. Zhu, *Lie theory and cohomology of relative Rota-Baxter operators*, arXiv:2108.02627v1, first submitted 2021-08-04, https://arxiv.org/abs/2108.02627; journal open-access full text https://doi.org/10.1112/jlms.12863.
