# Two noise-free leaders on unequal complete multipartite networks obey a smallest-part law

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a simple unweighted complete multipartite graph with \(r\ge3\), every \(n_i\ge2\), and at least two unequal part sizes. Put \(N=\sum_i n_i\), \(m=\min_i n_i\), and let \(L\) be its combinatorial Laplacian. For every two-element leader set \(S\), form the grounded Laplacian \(L_{FF}\) on \(F=V(G)\setminus S\) and set \(J(S)=\operatorname{tr}(L_{FF}^{-1})\). Then

\[
\underset{|S|=2}{\operatorname{argmin}}\, J(S)
=\bigcup_{i:n_i=m}\binom{V_i}{2}.
\]

That is, **every** optimum consists of two distinct nonadjacent vertices in one smallest part; no cross-part pair is optimal, and no pair in a larger part is optimal. There are exactly \(\#\{i:n_i=m\}\binom m2\) optimal two-leader sets, and the optimal value is

\[
J_*=\sum_{i=1}^r\left(\frac{n_i-1}{N-n_i}+\frac1N\right)
+\frac{N^2-8N+4m}{2N(N-m)}.
\]

For example, on \(K_{2,3,7}\) the unique optimal pair is the pair of vertices in its two-vertex part and its exact objective is \(361/180\). This two-leader concentration rule is not obtained by pretending the unequal parts are interchangeable.

## Assumptions and scope
Every cross-part edge has unit conductance; there are no within-part edges. Each leader is pinned to its reference signal with no leader noise, and every follower has identical stochastic forcing. The common performance normalization is the grounded-Laplacian inverse trace, without the inessential physical noise-variance factor. The budget is *exactly two* distinct vertices; \(r\ge3\), \(n_i\ge2\), and the part sizes are not all equal. The result does not assert an all-budget rule, a weighted-edge extension, or a classification when singleton parts occur.

## Proof
Write \(s_i=|S\cap V_i|\), \(f_i=n_i-s_i\), and \(\alpha_i=N-n_i>0\). Index the follower coordinates by their part. The grounded Laplacian is

\[
L_{FF}=M-\mathbf1\mathbf1^{\mathsf T},\qquad
M=\bigoplus_{i:f_i>0}(\alpha_i I_{f_i}+\mathbf1_{f_i}\mathbf1_{f_i}^{\mathsf T}).
\]

Each positive-size block is positive definite. Its inverse has trace \((f_i-1)/\alpha_i+1/(N-s_i)\); furthermore, its all-ones quadratic forms are \(f_i/(N-s_i)\) and \(f_i/(N-s_i)^2\) for the first and second inverse powers, respectively. Set

\[
U=\sum_i\frac{f_i}{N-s_i},\qquad V=\sum_i\frac{f_i}{(N-s_i)^2}.
\]

The identity

\[
1-U=\sum_i\frac{s_i(N-n_i)}{N(N-s_i)}>0
\]

holds because exactly two leaders are present. Sherman–Morrison therefore gives the exact, nonasymptotic formula

\[
J(S)=\sum_{i:f_i>0}\left(\frac{f_i-1}{N-n_i}+\frac1{N-s_i}\right)+\frac{V}{1-U}. \tag{1}
\]

Let \(C=\sum_i[(n_i-1)/(N-n_i)+1/N]\). If both leaders lie in a part of size \(u\), substituting into (1) and simplifying yields

\[
J_{uu}=C+\frac{N^2-8N+4u}{2N(N-u)}. \tag{2}
\]

For two available parts of sizes \(u\le v\), (2) implies

\[
J_{vv}-J_{uu}=\frac{(N-4)(v-u)}{2(N-u)(N-v)}\ge0, \tag{3}
\]

with equality exactly when \(u=v\). Here \(N\ge6\), so the coefficient of \(v-u\) is strictly positive.

It remains to show that a mixed pair is inferior to taking both leaders in the smaller of its two parts. A mixed pair has, directly from (1),

\[
J_{uv}=C-\frac1{N-u}-\frac1{N-v}+\frac2{N(N-1)}
+\frac{N(N-1)}{2N-u-v}
\left(\frac{N-u-v}{N^2}+\frac{u+v-2}{(N-1)^2}\right). \tag{4}
\]

Put \(h=u-2\ge0\), \(d=v-u\ge0\), and \(R=N-u-v\ge2\), so \(u=h+2\). Straight expansion of (2) and (4) gives

\[
J_{uv}-J_{uu}=\frac{P_0+dP_1+d^2P_2+d^3P_3+d^4P_4}{D}, \tag{5}
\]

where every coefficient below is nonnegative and \(P_0>0\):

\[
\begin{aligned}
P_0={}&2(R+h+2)^2[R^2+R(4h+9)+4h^2+16h+16],\\
P_1={}&(R+h+2)[R^3+R^2(6h+13)+R(12h^2+48h+54)\\
&\qquad+8h^3+44h^2+88h+64],\\
P_2={}&3R^3+R^2(15h+24)+R(24h^2+74h+58)\\
&\qquad+12h^3+54h^2+80h+40,\\
P_3={}&3R^2+R(9h+11)+6h^2+13h+4,\\
P_4={}&R+h,\\
D={}&2(R+u)(R+d+u)(R+d+2u)\\
&\qquad\cdot(2R+d+2u)(R+d+2u-1).
\end{aligned}
\]

All denominator factors are positive, hence \(J_{uv}>J_{uu}\). Equation (3) and this strict comparison exhaust the only two orbit types for a two-vertex set: same-part and cross-part. Thus only two vertices in a smallest part attain the optimum. Equation (2) gives the displayed value, and counting the allowed pairs gives \(\#\{i:n_i=m\}\binom m2\). This completes the proof.

## Verification
The self-contained Python 3 program `verify.py` uses only the standard library and exact rational arithmetic. It reconstructs the grounded Laplacian without using the rank-one derivation and compares every two-leader pair for 49 complete multipartite graph instances (3 or 4 parts, 3,322 exact matrix-pair evaluations). It checks the closed forms (2) and (4) against the block formula (1). It also checks (5) on a 729-point exact integer grid \(h,d,R\in\{0,\ldots,8\}\). After clearing its displayed denominator, the difference between the two expressions is a polynomial separately of degree at most eight in each of these three variables. Therefore the grid is also a finite exact identity test under the elementary polynomial interpolation theorem; positivity itself is evident from the displayed coefficients for nonnegative variables. Actual invocation: `python3 verify.py`. Recorded result: `VERIFY_OK identity_grid=729 graph_instances=49 exact_matrix_pair_comparisons=3322`.

## Relationship to prior work
Lin, Fardad and Jovanović [1] formulate the noise-free leader objective using grounded-Laplacian inverse traces and develop general-purpose optimization relaxations; the inspected problem formulation and examples do not supply the unequal complete multipartite two-leader classification. Fitch and Leonard [2] formulate a general two-leader joint-centrality criterion and solve path and cycle examples, but their criterion does not state which part receives the optimal pair in an unequal complete multipartite graph. A related earlier noise-free selection methodology [3] uses convex relaxations, not the present exact part-size comparison. Other previously available results for complete bipartite graphs and *balanced* multipartite graphs cover respective special domains and do not imply the present theorem for unequal part sizes with at least three parts. Those special domains are not claimed as new here.

## Limitations
The theorem makes no claim for singleton parts, more than two leaders, nonunit conductances, or heterogeneous noise. Its originality assessment is based on inspected primary literature, indexed-result searches, and accessible prior statements, not a proof of worldwide publication uniqueness. A publication-priority search beyond indexed materials remains warranted. No independent mathematical audit has been performed.

## References
1. F. Lin, M. Fardad, M. R. Jovanović, *Algorithms for leader selection in stochastically forced consensus networks*, arXiv:1302.0450, first submitted February 3, 2013. https://arxiv.org/abs/1302.0450
2. K. E. Fitch, N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first submitted July 7, 2014. https://arxiv.org/abs/1407.1569
3. M. Fardad, F. Lin, M. R. Jovanović, *Algorithms for Leader Selection in Large Dynamical Networks: Noise-Free Leaders*, CDC-ECC 2011. https://viterbi-web.usc.edu/~mihailo/papers/farlinjovCDC11.pdf
