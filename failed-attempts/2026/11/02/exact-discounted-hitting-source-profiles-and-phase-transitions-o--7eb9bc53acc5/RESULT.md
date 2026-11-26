# Exact discounted-hitting source profiles and phase transitions on friendship graphs

## Finding

For every integer \(m\ge1\), every \(0<\lambda<1\), and every \(0<\tau\le1\), the following formula counts **all** source sets satisfying the uniform discounted first-hitting floor on the friendship graph \(F_m=K_1\vee mK_2\). This graph has a central hub and \(m\) peripheral pairs, each pair joined by an edge and to the hub. Vertices and colors are distinguishable; a source set is any nonempty vertex subset.

Let \(\mathcal H_{m,\lambda,\tau}(z)=\sum_{S\text{ feasible}}z^{|S|}\). Classify each pair by the number of selected vertices: \(a\) pairs contain zero, \(b\) contain one, and \(c\) contain two, where \(a+b+c=m\). Put
\[
 d=\frac{\lambda}{2-\lambda},\qquad
 X_{a,b,c}=\frac{\lambda[b(1+\lambda/2)+2c]}{2m-2\lambda ad-(\lambda^2/2)b}.
\]
When the hub is selected, define
\[
 M^{(1)}_{a,b,c}=\begin{cases}d&a>0,\\\lambda&a=0,\ b>0,\\1&a=b=0.\end{cases}
\]
When the hub is not selected, define \(M^{(0)}_{m,0,0}=0\) and, for \(b+c>0\),
\[
 M^{(0)}_{a,b,c}=\begin{cases}dX_{a,b,c}&a>0,\\\lambda(1+X_{a,b,c})/2&a=0,\ b>0,\\\lambda&a=b=0.\end{cases}
\]
The complete generating polynomial is
\[
 \boxed{\mathcal H_{m,\lambda,\tau}(z)=\sum_{a+b+c=m}\frac{m!2^b}{a!b!c!}z^{b+2c}
 \left({\bf1}_{M^{(0)}_{a,b,c}\ge\tau}+z{\bf1}_{M^{(1)}_{a,b,c}\ge\tau}\right).}
\]
The only empty-set convention is \(M^{(0)}_{m,0,0}=0\), since \(\tau>0\). Thus every coefficient is an exact count, including at threshold equality.

The least exponent with a positive coefficient is
\[
 \boxed{\delta_{\lambda,\tau}(F_m)=
 \begin{cases}1&0<\tau\le d,\\m+1&d<\tau\le\lambda,\\2m+1&\lambda<\tau\le1.\end{cases}}
\]
Moreover, for \(m\ge2\), define two additional exact transitions
\[
 \beta_m=\frac{\lambda^2}{\lambda^2+4m(1-\lambda)},\qquad
 \alpha_m=\frac{\lambda[(2+\lambda)m+\lambda]}{4m-\lambda^2(m-1)}.
\]
They strictly interlace as \(0<\beta_m<d<\alpha_m<\lambda<1\). The number \(A_{m,\lambda,\tau}\) of minimum-cardinality source sets is
\[
 \boxed{A_{m,\lambda,\tau}=\begin{cases}
 2m+1&0<\tau\le\beta_m,\\
 1&\beta_m<\tau\le d,\\
 2^m+m2^{m-1}&d<\tau\le\alpha_m,\\
 2^m&\alpha_m<\tau\le\lambda,\\
 1&\lambda<\tau\le1.
 \end{cases}}
\]
For \(m=1\), the graph is \(K_3\); its minimum-set counts are three for \(\tau\le\lambda\) and one for \(\lambda<\tau\le1\), with minimum sizes prescribed above.

For example, on \(F_2\) with \(\lambda=4/5\), the four successive critical values are \(\beta_2=2/7\), \(d=2/3\), \(\alpha_2=16/23\), and \(\lambda=4/5\). In the middle cardinality regime the number of optimizers drops from eight to four exactly after \(16/23\), even though the optimum size stays three.

## Assumptions and scope

All graphs are finite, simple, undirected, with the standard simple random walk choosing uniformly among neighbors. Every selected vertex \(s\in S\) is pinned at support one. For each unselected vertex \(v\), support is \(h_v^S=\lambda\sum_{w\sim v}h_w^S/\deg(v)\), equivalently \(\mathbb E_v[\lambda^{T_S}]\). Here \(T_S\) is the first hitting time of the nonempty source set, with \(\lambda^\infty=0\). A source set is feasible if \(h_v^S\ge\tau\) for all vertices. Strictly \(0<\lambda<1\) and \(0<\tau\le1\); no extension to \(\lambda=1\) or heterogeneous transition weights is asserted. The relevant primary classification is 05C69.

## Proof

**Existence and pairwise reduction.** The support equations on unselected vertices form a strict contraction in the sup norm (operator norm at most \(\lambda<1\)); they have a unique fixed point. When the hub is selected, each source-free peripheral pair has equal support \(x=\lambda(1+x)/2=d\). A pair containing one source has its other vertex at support \(\lambda(1+1)/2=\lambda\); fully selected pairs have support one. These are exactly the three branches of \(M^{(1)}\).

When the hub is unselected, call its support \(X\). In a pair with zero sources, both peripheral vertices have value \(dX\). In a pair with one source, the unselected vertex has value \(\lambda(1+X)/2\). In a fully selected pair, both have value one. Averaging all \(2m\) peripheral neighbors at the hub therefore gives
\[
 X=\frac{\lambda}{2m}\left(2adX+b[1+\lambda(1+X)/2]+2c\right),
\]
whose unique solution is the displayed \(X_{a,b,c}\). Its denominator is positive, since \(2m-2\lambda ad-(\lambda^2/2)b>0\): \(2ad\lambda<2a\), \(\lambda^2b/2< b\), and \(2a+b\le2m\), with at least one strict inequality. For nonempty \(S\), \(0<X\le\lambda<1\). If \(a>0\), then \(dX\) is below \(X\) and below \(\lambda(1+X)/2\), because \(0\le X\le1\) and \(dX<\lambda(1+X)/2\). If \(a=0\), any selected set contains at least one peripheral source per pair. The configuration with exactly one source in each pair gives \(X=d\), and adding sources cannot decrease first-hitting support. Thus \(X\ge d=\lambda(1+d)/2\), so the least nonsource support is \(\lambda(1+X)/2\) whenever \(b>0\). If \(a=b=0\) all peripheral vertices are pinned and the hub has \(X=\lambda\). This proves the branches of \(M^{(0)}\).

**Polynomial.** There are precisely \(m!/(a!b!c!)\) ways to choose which labelled pairs have zero, one, or two sources, and \(2^b\) orientations for their singleton selections. Each such configuration with the hub excluded has exactly \(b+2c\) sources, and the hub-included version has one more. The just-proved least-support conditions are necessary and sufficient for feasibility. Summing their disjoint contributions gives \(\mathcal H\) for all \(m,\lambda,\tau\) and verifies all coefficients.

**Minimum cardinality.** Selecting only the hub gives worst support \(d\). Thus for \(0<\tau\le d\), one source suffices and zero cannot. If \(d<\tau\le\lambda\), any feasible set including the hub must select at least one vertex from each peripheral pair, hence has \(m+1\) or more sources; the hub together with one source per pair attains \(m+1\), with worst support \(\lambda\). Any feasible set excluding the hub cannot leave any pair source-free, because then its support \(dX\le d<\tau\); hence it has at least \(m\) sources. At exactly \(m\) sources it has one per pair, so \(X=d\) and every nonsource support is \(d\), again infeasible. Thus it too needs at least \(m+1\). Finally, for \(\lambda<\tau\), every unselected vertex has support \(\lambda\) times an average of values bounded by one, so no proper set is feasible; all \(2m+1\) vertices must be selected. This proves the minimum formula.

**Counting all minima.** Suppose \(m\ge2\). A singleton consisting of the hub gives worst support \(d\). Any singleton consisting of one peripheral vertex leaves \(m-1\) entirely source-free pairs. Solving its hub equation yields
\[
 X=\frac{\lambda(2-\lambda)}{\lambda^2+4m(1-\lambda)},
\]
and its worst support \(dX=\beta_m\). There are exactly \(2m\) such singleton sets. In the middle regime, the hub together with one vertex from each pair gives exactly \(2^m\) minima. A hub-free optimum of size \(m+1\) must have precisely one fully selected pair and one selected vertex from each of the other \(m-1\) pairs. There are \(m2^{m-1}\) such sets, and substituting \((a,b,c)=(0,m-1,1)\) into the support formula gives worst support \(\alpha_m\). Hence they are feasible precisely for \(\tau\le\alpha_m\). In the top regime the only optimum is the whole vertex set. The inequalities \(\beta_m<d\) follow from \(m\ge2\) and \(\lambda<1\). Direct positive-factor comparisons give \(d<\alpha_m<\lambda\) throughout the permitted parameter range. For \(m=1\), the graph is a triangle and all subsets of each size are symmetric, giving three optima for sizes one and two and one optimum for size three. This proves the complete minimum-profile classification. \(\square\)

## Verification

The accompanying standalone `verify.py` constructs each labelled graph directly, independently solves the nonsource first-step linear equations over exact rational numbers, and exhaustively checks every nonempty source set for \(1\le m\le5\) at \(\lambda\in\{1/2,2/3,4/5\}\). At 202 exact rational parameter tests, including every claimed phase boundary and adjacent intervals, it checks the entire source-set size histogram and minimum-cardinality counts, not just the cardinality optimum. All checks returned `VERIFY_OK`. Finite tests provide corroboration, not a proof of the infinite parameter theorem; the algebraic case split above supplies that proof.

## Relationship to prior work

Allagan, Pereyra, and Massey introduced discounted hitting domination as a uniform-coverage optimization and proved a first-hitting equilibrium representation, global bounds, and special results for spider trees, complete graphs, and stars. The present result uses their definition and elementary fixed-point framework but establishes a new all-set polynomial and exact optimizer phase transitions for friendship graphs, which have cycles and are neither spider trees nor complete graphs for \(m\ge2\). Existing group-hitting-probability research studies evaluation and ranking for given target sets, not this uniform-floor exact friendship graph census. In particular, the 2024 paper by Guo and collaborators addresses pairwise and top-k hitting probability queries rather than this graph family's full optimum profile. Overlap and priority are qualified by the limitations below.

## Limitations

The theorem assumes unweighted simple random walks, one homogeneous fidelity factor, positive floor, and friendship graphs; it does not determine analogous quantities for arbitrary windmill graphs, heterogeneous fidelities or arbitrary graphs. Its historical priority is conditional on available indexed literature and the inspected primary texts. The accompanying computation is finite and not a substitute for independent mathematical review. No independent validation is claimed.

## References

1. Julian D. Allagan, Kevin Pereyra, and William A. Massey, *Discounted Hitting Domination on Graphs with Submodularity, Complexity and Exact Algorithms*, arXiv:2609.31535v1 (first posted 2026-09-25), https://arxiv.org/abs/2609.31535.
2. Qintian Guo, Dandan Lin, Sibo Wang, Raymond Chi-Wing Wong, and Wenqing Lin, *Efficient Algorithms for Group Hitting Probability Queries on Large Graphs*, IEEE Transactions on Knowledge and Data Engineering 36(7) (2024), 2995–3008, DOI:10.1109/TKDE.2023.3349164.
