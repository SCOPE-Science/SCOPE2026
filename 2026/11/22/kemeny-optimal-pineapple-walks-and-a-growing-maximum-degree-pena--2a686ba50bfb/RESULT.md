# Kemeny-optimal pineapple walks and a growing maximum-degree penalty

## Finding

For integers \(n\ge3\) and \(r\ge1\), let \(G_{n,r}\) consist of the complete graph \(K_n\) with \(r\) pendant vertices attached to one distinguished gateway vertex. Consider **all** real symmetric, entrywise nonnegative, row-stochastic transition matrices \(P\) supported on this graph, allowing holding probabilities and zero weights on allowed edges, but requiring irreducibility. Define the zero-at-target convention of Kemeny's constant by
\[
\mathcal K_0(P)=\sum_{\lambda\in\operatorname{spec}(P)\setminus\{1\}}\frac1{1-\lambda}=\operatorname{tr}((I-P)^+).
\]
Eigenvalues are counted with multiplicity; the alternative first-return convention adds exactly one and has the same minimizer.

There is a **unique** global minimizer, with one edge probability \(a_*\) on every gateway-to-other-clique edge, \(b_*\) on every gateway-to-leaf edge and \(c_*\) on every edge between other clique vertices. It has
\[
 a_* = \frac{z_*}{n-1},\qquad
 b_* = \frac{1-z_*}{r},\qquad
 c_* = \frac{1-z_*/(n-1)}{n-2},
\]
where \(z_*\) is the unique solution in \((0,1)\) of
\[
-\frac{(r+1)(n-1)}{(n+r)z^2}
+\frac{r^2(n+r-1)}{(n+r)(1-z)^2}
+\frac{(n-2)^2(n-1)}{((n-1)^2-z)^2}=0.
\]
The gateway and all ordinary clique vertices have **zero holding probability**, every pendant vertex has positive holding probability, and **every allowed nonloop edge has positive optimal probability**. These conclusions hold without restricting competitors to symmetric edge orbits.

For each fixed integer \(r\ge1\), as \(n\to\infty\),
\[
(n-1)a_*\longrightarrow\frac{\sqrt{r+1}}{r+\sqrt{r+1}},\qquad
 b_*\longrightarrow\frac1{r+\sqrt{r+1}},
\]
\[
\mathcal K_0(P_*)=n-3+(r+\sqrt{r+1})^2+o(1).
\]
The maximum-degree walk assigns probability \(1/(n+r-1)\) to each allowed nonloop edge and makes up the remaining mass with holding. Writing \(P_{\rm md}\) for that walk, the **exact penalty** is
\[
\mathcal K_0(P_{\rm md})=(n+r-1)\left(r+\frac1{n+r}+\frac{n-2}{n}\right),
\qquad
\lim_{n\to\infty}\frac{\mathcal K_0(P_{\rm md})}{\mathcal K_0(P_*)}=r+1.
\]
Thus the standard maximum-degree heuristic has an arbitrarily large asymptotic multiplicative regret as the fixed number of pendant vertices increases. The result does not compare all possible heuristic policies.

## Assumptions and scope

The vertex set is a gateway \(h\), ordinary clique vertices \(u_1,\ldots,u_{n-1}\), and leaves \(\ell_1,\ldots,\ell_r\). Only hub–ordinary, hub–leaf and ordinary–ordinary offdiagonal entries may be nonzero. Symmetry means \(P_{ij}=P_{ji}\), not necessarily equality within edge orbits. The stationary law is uniform on all \(n+r\) vertices. All allowable holding probabilities are nonnegative; zero holding is permitted. Irreducibility means the positive-weight support is connected. The graph is a canonical one-vertex attachment of a clique and a star. Its optimal transition design, not the unweighted simple random walk's Kemeny invariant, is the object studied here.

## Proof

**Strict global convexity and orbit reduction.** Write \(N=n+r\), \(L=I-P\) and \(Q=\mathbf1\mathbf1^{\mathsf T}/N\). Every connected feasible support has \(L+Q\succ0\), and
\(\mathcal K_0(P)=\operatorname{tr}((L+Q)^{-1})-1\).
The map \(X\mapsto\operatorname{tr}(X^{-1})\) is strictly convex on positive-definite matrices: in any nonzero symmetric direction \(H\), its second derivative is \(2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0\). The affine map \(P\mapsto L+Q\) is injective, so the objective is strictly convex in \(P\). Feasibility is convex, including irreducible matrices because any convex mixture of two connected nonnegative edge supports remains connected. The objective tends to infinity approaching a disconnected support. Hence a unique minimizer exists. Conjugation by permutations of ordinary vertices and leaves preserves the objective and feasible set; uniqueness makes the minimizer invariant under \(S_{n-1}\times S_r\).

**Exact spectrum.** For an invariant matrix write \(a,b,c\) for hub–ordinary, hub–leaf and ordinary–ordinary probabilities. Nonnegative holding requires
\[
 a,b,c\ge0,\qquad (n-1)a+rb\le1,\qquad a+(n-2)c\le1.
\]
The leaf hold constraint \(b\le1\) follows from the hub constraint. Irreducibility forces \(a,b>0\). On the leaf-sum-zero subspace, \(L\) has eigenvalue \(b\) with multiplicity \(r-1\). On the ordinary-clique-sum-zero subspace, it has eigenvalue \(a+(n-1)c\) with multiplicity \(n-2\). On the three-dimensional subspace constant on leaves, gateway, and ordinary clique vertices, the nonzero eigenvalues \(\xi_\pm\) have sum \((r+1)b+na\) and product \(Nab\). These follow by orthonormalizing the three block-indicators, or by the characteristic polynomial of their quotient Laplacian. The remaining eigenvalue is zero. Therefore
\[
\mathcal K_0(a,b,c)=\frac{r+1}{Na}+\frac{r(N-1)}{Nb}+\frac{n-2}{a+(n-1)c}.
\]

**Active constraints and unique scalar optimizer.** At fixed \(a>0\), the displayed objective is strictly decreasing separately in \(b>0\) and \(c\ge0\). Hence the optimal solution uses the largest feasible values
\[
 b=\frac{1-(n-1)a}{r},\qquad c=\frac{1-a}{n-2},\qquad 0<a<\frac1{n-1}.
\]
Set \(z=(n-1)a\). The reduced objective is
\[
 F_{n,r}(z)=\frac{(r+1)(n-1)}{Nz}
+\frac{r^2(N-1)}{N(1-z)}
+\frac{(n-2)^2}{n-1-z/(n-1)},\qquad 0<z<1.
\]
Each term has a strictly positive second derivative; \(F_{n,r}\to\infty\) at both endpoints. Its derivative is exactly the displayed equation in the finding and increases strictly from negative infinity to positive infinity. Thus the root \(z_*\) exists uniquely and yields the unrestricted unique optimum. Since \(z_*\in(0,1)\), all three edge probabilities are positive; the hub and ordinary clique rows saturate, and the leaves hold with probability \(1-b_*>0\).

**Sharp asymptotics and benchmark.** For fixed \(r\), subtract \(n-3\) from \(F_{n,r}\) and let \(n\to\infty\) with \(z\) bounded away from the endpoints. Uniform convergence on compact subintervals gives the strictly convex limit
\[
 f_r(z)=\frac{r+1}{z}+\frac{r^2}{1-z}.
\]
The endpoint barriers and first-order equations ensure the unique minimizers converge to \(z_\infty=\sqrt{r+1}/(r+\sqrt{r+1})\). The limiting minimum is \((r+\sqrt{r+1})^2\), proving the asserted two limiting probabilities and objective expansion. For the maximum-degree walk, substitute \(a=b=c=1/(N-1)\) into the exact spectrum formula to obtain the displayed finite-size expression. Divide by \(\mathcal K_0(P_*)=n+O_r(1)\) to obtain the ratio \(r+1\). Adding one to each Kemeny convention leaves these limits unchanged.

## Verification

Run `python verify.py` with Python 3 and SymPy. It directly constructs \(L\) and evaluates \(\operatorname{tr}((L+Q)^{-1})-1\) in exact rational arithmetic for many small pairs \((n,r)\), independently comparing it with the claimed eigenvalue reduction. The script checks scalar minimizers, benchmark identities, and quantitative large-size convergence. Its expected output is `VERIFY_OK 585 exact and numerical assertions`. The proof, not finite testing or floating-point minimization, establishes the result for every allowed \(n,r\). The code tests exact rational samples, not exhaustive floating or real competitors.

## Relationship to prior work

Boyd, Diaconis, and Xiao (2004) formulate symmetric fastest-mixing Markov-chain design by a semidefinite program, give standard maximum-degree weights, and study a small clique with one pendant vertex. That paper optimizes the second-largest eigenvalue modulus; the present claim optimizes the inverse Laplacian spectral sum, for any clique size and any positive pendant multiplicity. Patel, Agharkar, and Bullo (2015; preliminary 2014) establish convex optimization of Kemeny's constant for fixed support, but provide no evaluated all-size pineapple weights or the \(r+1\) heuristic penalty in the inspected sections. Faught, Kempton, and Knudson (2021) study a one-separation formula for **fixed simple random walks** with degree-proportional stationary law, not arbitrary symmetric uniform-stationary transition design. A separately published exact pineapple fastest-mixing classification gives a sharp phase transition for a different objective and does not supply the formula here. General convexity and symmetry are used as antecedents, not claimed as discoveries.

## Limitations

The design class fixes uniform stationary distribution, symmetry, one-step transitions and the graph's allowed support. No claims are made for nonreversible chains, arbitrary stationary masses, longer tails or finite-horizon detection objectives. This is an exact analytical classification, not an independently audited publication-priority certificate. The best-knowledge novelty comparison can miss equivalent unindexed treatments. The limit \(n\to\infty\) holds with \(r\) fixed, not jointly growing without further analysis.

## References

1. S. Boyd, P. Diaconis, L. Xiao, *Fastest Mixing Markov Chain on a Graph*, SIAM Review **46** (2004), 667–689; DOI 10.1137/S0036144503423264; https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf (public electronic date October 29, 2004).
2. R. Patel, P. Agharkar, F. Bullo, *Robotic surveillance and Markov chains with minimal weighted Kemeny constant*, IEEE Transactions on Automatic Control **60** (2015), 3156–3167; DOI 10.1109/TAC.2015.2426317; https://motion.me.ucsb.edu/pdf/2014b-pab.pdf .
3. N. Faught, M. Kempton, A. Knudson, *A 1-Separation Formula for the Graph Kemeny Constant and Braess Edges*, preprint (August 2, 2021), https://arxiv.org/abs/2108.01061 .
4. *Sharp fastest-mixing transition on pineapple graphs*, public research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-fastest-mixing-transition-on-pineapple-graphs--2240321d233d/RESULT.md .
5. *Fastest mixing on a clique with one pendant vertex: a complete optimizer face*, public research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-fastest-mixing-on-a-clique-with-one-pendant-vertex-a-complete-op--30d4b04d1192/RESULT.md .
