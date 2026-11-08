# A unique optimal edge conductance and a sharp Kemeny–Braess reversal on complete bipartite graphs

## Finding

Let \(a\ge3\) and \(b\ge1\) be integers. On the complete bipartite graph \(K_{a,b}\), give all existing edges unit conductance, and add one edge of positive conductance \(w\) between two vertices of the part of size \(a\). Let \(K_{a,b}(w)\) be the Kemeny constant of the discrete-time random walk that chooses its next neighbor proportionally to edge conductance. Then
\[
K_{a,b}(w)-K_{a,b}(0)
=\frac{w[4(a-2)w-3b]}{2(b+2w)(ab+w)},\qquad K_{a,b}(0)=a+b-\frac32.
\]
Consequently an added edge first *decreases* this global random-walk hitting-time invariant and ultimately *increases* it. The precise zero-crossing is \(w_0=3b/[4(a-2)]\). With \(t=w/b\),
\[
K_{a,b}(bt)-K_{a,b}(0)=\frac{t[4(a-2)t-3]}{2(1+2t)(a+t)},
\]
which is independent of \(b\). It has a unique global minimum over \(t>0\) at the positive root \(t_*\) of
\[
(8a^2-12a-2)t^2+8a(a-2)t-3a=0,
\qquad 0<t_*<\frac3{4(a-2)}.
\]
In particular, the unique optimal added-edge conductance is \(w_*=bt_*\). The ordinary unweighted edge case is known; the full conductance response and optimization are the conclusions here.

## Assumptions and scope

All graphs are finite and connected. The walk is *discrete-time*, non-lazy, and reversible, with transition probability \(P_{uv}=c_{uv}/\sum_x c_{ux}\), where the symmetric conductances \(c_{uv}\) are as specified above. The stationary law is proportional to weighted vertex degrees. For starting vertex \(i\), let \(T_j\) be the first time \(j\) is reached, with \(T_i=0\). Then \(K(P)=\sum_j\pi_j\mathbb E_i[T_j]\), independent of \(i\). Equivalently, if \(1=\lambda_1,\lambda_2,\ldots,\lambda_n\) are the eigenvalues of \(P\), including multiplicities, then \(K(P)=\sum_{j=2}^n(1-\lambda_j)^{-1}\). Irreducibility suffices; periodicity of the unperturbed bipartite walk causes no difficulty.

## Proof

Write \(n=a+b\). Partition the states into the two selected endpoints \(E\), the remaining \(a-2\) vertices of the first part \(R\), and the \(b\) vertices of the second part \(B\). These classes are equitable for the transition operator, with stochastic quotient matrix
\[
Q=\begin{pmatrix}
\frac{w}{b+w}&0&\frac{b}{b+w}\\
0&0&1\\
\frac2a&\frac{a-2}{a}&0
\end{pmatrix}.
\]
The antisymmetric vector supported on the two selected endpoints has eigenvalue \(-w/(b+w)\). All vectors whose coordinate sums vanish separately on \(R\) and \(B\) are zero eigenvectors. There are \((a-3)+(b-1)=n-4\) such zero eigenvalues; these account, with the two quotient eigenvalues besides \(1\), for the full spectrum. The characteristic polynomial of \(Q\), up to a nonzero scalar, is
\[
(\lambda-1)g(\lambda),\qquad
g(\lambda)=a(b+w)\lambda^2+ab\lambda+w(2-a).
\]
Let \(\mu_1,\mu_2\) be the roots of \(g\). Since \(g(1)=2(ab+w)>0\),
\[
\frac1{1-\mu_1}+\frac1{1-\mu_2}=\frac{g'(1)}{g(1)}
=\frac{a(3b+2w)}{2(ab+w)}.
\]
Thus direct spectral summation yields
\[
K_{a,b}(w)=n-4+\frac{b+w}{b+2w}
+\frac{a(3b+2w)}{2(ab+w)}.
\]
Substitution of \(w=0\) gives \(n-3/2\). Subtraction and a common denominator give the displayed difference formula. Because its denominator is positive for \(a\ge3,b\ge1,w>0\), the sign is controlled exactly by \(4(a-2)w-3b\), proving the reversal and sharp boundary.

Next put \(t=w/b\). The difference is \(F_a(t)=t(4(a-2)t-3)/[2(1+2t)(a+t)]\). Direct differentiation gives
\[
F_a'(t)=\frac{(8a^2-12a-2)t^2+8a(a-2)t-3a}{2(1+2t)^2(a+t)^2}.
\]
For every integer \(a\ge3\), the derivative numerator has strictly positive quadratic and linear coefficients and strictly negative constant term. Hence it has exactly one positive zero \(t_*\), with \(F_a'<0\) before that zero and \(F_a'>0\) after it. The strict negativity \(F_a(t)<0\) for \(0<t<3/[4(a-2)]\), followed by \(F_a(3/[4(a-2)])=0\), forces \(t_*\) to lie inside that interval. This establishes a unique global minimizer, including the conductance scaling law. For context, \(\lim_{t\to\infty}F_a(t)=a-2>0\).

## Verification

Run `python check_kemeny.py` with Python 3 and no third-party dependencies. It builds the *full labeled* weighted adjacency matrix, constructs the stationary probabilities and Markov transition matrix, and computes \(K=\operatorname{tr}(I-P+\mathbf1\pi^T)^{-1}-1\) by exact rational Gauss–Jordan elimination. This is independently implemented from the quotient spectral proof. The actual run passed 175 exact full-matrix comparisons across \(3\le a\le7\), \(1\le b\le5\) and seven conductances including zero, plus 252 rational scaling identities and threshold boundary tests. Algebraic differentiation and sign arguments prove the all-parameter statements; finite checker cases are corroboration only.

## Relationship to prior work

Hu and Kirkland, *Complete Multipartite Graphs and Braess Edges* (2019), Theorem 2.0.1, already treat insertion of an *unweighted* edge into a complete bipartite graph and use an equitable partition. In particular, their exact unit-weight sign comparison is the specialization \(w=1\) of the first displayed identity and **is not new here**. The present assertion concerns the full continuum of conductance strengths, the change of sign at fixed topology, independence of the normalized conductance response from \(b\), and the unique optimized conductance.

Altafini, Bini, Cutini, Meini and Poloni (first public March 12, 2022), *An edge centrality measure based on the Kemeny constant*, study weighted graphs and general matrix formulas for the Kemeny change under edge deletion, but their examined results do not state the all-parameter complete-bipartite conductance profile or its minimizing edge strength. Breen, deBlieck and Vander Meulen (2026) extend the unit-weight comparison to adding complete cliques, without prescribing positive continuous weights. Faught, Kempton and Knudson (2021) analyze one-separation formulas, not this parameter family. General-purpose methods may enable alternative derivations; they are not claimed to be novel.

## Limitations

The theorem requires exactly one added edge inside the \(a\)-part and unit conductances on all original cross edges; it makes no claim for arbitrary weighted base bicliques, multiple added edges, directed walks, or continuous-time clocks. The unit-weight sign case is previously published. No claim of independence or exhaustive historical priority is made. Further verification by others is outstanding.

## References

1. Hu and Kirkland, *Complete Multipartite Graphs and Braess Edges* (2019), Theorem 2.0.1; open manuscript: https://mspace.lib.umanitoba.ca/server/api/core/bitstreams/04a4246d-2b67-4e4c-9c4b-60f0c5417031/content.
2. Altafini, Bini, Cutini, Meini and Poloni, *An edge centrality measure based on the Kemeny constant*, arXiv:2203.06459 (first public 2022-03-12), https://arxiv.org/abs/2203.06459.
3. Breen, deBlieck and Vander Meulen, *Kemeny's constant and Braess cliques in graphs*, arXiv:2608.04150 (2026), especially Section 4.2, https://arxiv.org/abs/2608.04150.
4. Faught, Kempton and Knudson, *A 1-Separation Formula for the Graph Kemeny Constant and Braess Edges*, arXiv:2108.01061 (2021), https://arxiv.org/abs/2108.01061.
