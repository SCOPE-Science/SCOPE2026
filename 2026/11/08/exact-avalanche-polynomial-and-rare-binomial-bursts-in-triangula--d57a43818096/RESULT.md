# Exact avalanche polynomial and rare binomial bursts in triangular-book sandpiles

## Finding
Let \(n\ge2\) and consider the triangular-book graph \(B_n=K_{1,1,n}\), with \(n\) triangles sharing the spine edge. Declare one spine vertex \(s\) the sink, denote the other spine vertex \(v\), and label the \(n\) page tips \(w_1,\ldots,w_n\). The stationary Abelian sandpile uses a uniformly sampled recurrent stable configuration. A principal avalanche is caused by adding one grain at exactly one prescribed nonsink vertex. Its size \(T\) is the sum of individual vertex topplings; a zero-size avalanche is included.

For each recurrent state and each of the \(n+1\) nonsink sources, let the toppling-vector monomial be \(X^{t_v}\prod_{i=1}^nY_i^{t_{w_i}}\). The **complete multivariate principal-avalanche polynomial** is
\[
\boxed{\begin{aligned}
\mathcal A_n(X,Y_1,\ldots,Y_n)
&=n2^{n-1}+X\prod_{i=1}^{n}(1+Y_i)\\
&\quad +(n+1)2^{n-2}\sum_{j=1}^{n}(1+Y_j)
 +X\sum_{j=1}^{n}Y_j\prod_{i\ne j}(1+Y_i).
\end{aligned}}
\]
Its specialization at every variable equal to \(q\) is
\[
\mathcal A_n(q)=n2^{n-1}+n(n+1)2^{n-2}(1+q)
  +q(1+q)^n+nq^2(1+q)^{n-1}.
\]
There are exactly \((n+2)2^{n-1}\) recurrent configurations. For a fixed page-tip source, the exact stationary law is
\[
\Pr(T=0)=\Pr(T=1)=\frac{n+1}{2(n+2)},\qquad
\Pr(T=2+k)=\frac{\binom{n-1}{k}}{2^{n-1}(n+2)}\quad(0\le k\le n-1).
\]
For the spine source \(v\), it is
\[
\Pr(T=0)=\frac{n}{n+2},\qquad
\Pr(T=1+k)=\frac{\binom nk}{2^{n-1}(n+2)}\quad(0\le k\le n).
\]
At either specified source \(\mathbb E T=1\). The page-tip variance is \((n^2+5n+2)/(4(n+2))\), while the spine-source variance is \(n(n+3)/(2(n+2))\). In particular the variance grows linearly although the mean stays exactly one. The probability of a binomial-sized avalanche is \(1/(n+2)\) at a tip and \(2/(n+2)\) at the spine; conditioned on that event, \(T/n\) tends in probability to \(1/2\), and centered fluctuations satisfy the standard binomial central limit theorem. These are statements about the stationary distribution for a fixed specified source, not the transient distribution from an arbitrary initial state.

## Assumptions and scope
Work with the standard deterministic chip-firing model on the simple undirected graph \(B_n\), \(n\ge2\). The sink \(s\) never topples and absorbs incident chips. Vertex \(v\) has degree \(n+1\) and each \(w_i\) has degree \(2\). A stable configuration has integer heights \(0\le h_v\le n\), \(h_{w_i}\in\{0,1\}\). A configuration is recurrent in the ordinary sandpile-group sense, equivalently it passes Dhar's burning test. Each recurrent state has equal stationary weight. The polynomial counts one principal avalanche for each ordered recurrent-state/source pair, including zero topplings.

## Proof
Write \(h=h_v\), let \(\eta_i=h_{w_i}\in\{0,1\}\), and let \(z=|\{i:\eta_i=0\}|\). By the forbidden-subconfiguration version of Dhar's burning criterion, a stable state is recurrent **if and only if** \(h\ge z\). Indeed, when \(h<z\), the subset consisting of \(v\) and all \(z\) zero-height tips is forbidden: every tip has height \(0\), below its internal degree \(1\), while \(h<z\), the internal degree of \(v\). Conversely, any subset not containing \(v\) has tips of internal degree zero; a subset containing \(v\) and a height-one tip has that tip at least its internal degree one; and a subset containing \(v\) with only zero-height tips has at most \(z\) such tips, so \(h\ge z\) means \(v\) meets its internal degree. Thus no forbidden subset exists. Summing over the \(\binom nz\) tip strings with exactly \(z\) zeros and the \(n-z+1\) possible heights \(h\) gives
\[
\#\operatorname{Rec}(B_n,s)=\sum_{z=0}^n\binom nz(n-z+1)=(n+2)2^{n-1}.
\]

For an addition at the spine \(v\), if \(h<n\) no toppling occurs. If \(h=n\), then \(v\) topples once and sends one grain to every tip and to the sink. Precisely those tips with \(\eta_i=1\) topple once. The spine then holds at most \(n\) grains and no vertex can topple again. Every one of the \(2^n\) tip strings is recurrent at height \(h=n\); consequently the spine contributes \(n2^{n-1}\) zero monomials and the polynomial \(X\prod_i(1+Y_i)\) from its nonzero events.

For addition at a specified page tip \(w_j\): if \(\eta_j=0\) there is no toppling; if \(\eta_j=1\) and \(h<n\), only \(w_j\) topples; if \(\eta_j=1\) and \(h=n\), then \(w_j\) topples, triggers \(v\), and then precisely the other height-one tips topple. No vertex topples twice because after these firings \(v\) holds at most \(n-1\) grains, and the fired tip \(w_j\) returns to height one. Direct counting of recurrent states with \(\eta_j=0\) gives
\[
\sum_{z=1}^{n}\binom{n-1}{z-1}(n-z+1)=(n+1)2^{n-2}.
\]
The same number have \(\eta_j=1\) and \(h<n\), by subtracting the \(2^{n-1}\) height-\(n\) strings with \(\eta_j=1\) from all those with \(\eta_j=1\). Hence the fixed-tip polynomial contribution is \((n+1)2^{n-2}(1+Y_j)+XY_j\prod_{i\ne j}(1+Y_i)\). Summing over all source vertices proves the displayed multivariate identity.

The two source-conditioned probability laws follow by specializing all toppling variables to \(q\) and dividing by \((n+2)2^{n-1}\). In the rare positive-event branch at the tip the size is \(2+\operatorname{Bin}(n-1,1/2)\); at the spine it is \(1+\operatorname{Bin}(n,1/2)\). The event weights are respectively \(1/(n+2)\) and \(2/(n+2)\). Elementary binomial first and second moments yield both exact means and variances, while the weak-law and binomial central limit theorem yield the stated conditional limits. Nothing is inferred from finite enumeration.

## Verification
The standalone Python standard-library program `verify_book.py` independently computes recurrent states by Dhar burning (stabilizing after adding one grain from the sink to each neighbor), stabilizes all one-grain additions with a legal toppling queue, and compares the complete toppling-vector polynomial coefficientwise with an independently constructed closed form. It covers every stable configuration and every source for \(1\le n\le9\), including the triangle boundary case, and checks the exact source-conditioned size distributions and means. Running `python3 verify_book.py` returned `PASS 56453 exact checks`. These finite checks corroborate the proof; they do not establish the all-size theorem on their own.

## Relationship to prior work
Cori, Micheli and Rossin study avalanche polynomials on plane trees [1], while Austin et al. give multivariate avalanche-polynomial definitions, burning consequences, and explicit formulas for trees, cycles, complete graphs and wheels [2]. These do not state the triangular-book polynomial; a triangular book is not a tree, cycle, complete graph (for \(n\ge2\)), or wheel, and in particular it is not a friendship graph (triangles meeting only at a vertex). The present calculation applies the general definitions and burning criterion to the natural shared-edge triangle family and obtains its exact all-size, all-source generating function.

## Limitations
Only this sink choice and the standard undirected deterministic model are addressed. The mean-one law is not a claim of critical power-law scaling: the stationary distribution has explicitly separated microscopic and rare binomial-macroscopic components, with the latter probability decreasing as \(n^{-1}\). No result is asserted for other graph perturbations or other sandpile dynamics. Although source searches found no earlier statement of this full formula, unindexed historical overlap cannot be excluded; independent priority review remains open.

## References
[1] R. Cori, A. Micheli and D. Rossin, *Avalanche polynomials*, arXiv:0905.2823v1 (public 2009-05-18), https://arxiv.org/abs/0905.2823.

[2] D. Austin, M. Chambers, R. Funke, L. D. García Puente and L. Keough, *The Avalanche Polynomial of a Graph*, arXiv:1605.02713v1 (public 2016-05-09), https://arxiv.org/abs/1605.02713.
