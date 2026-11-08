# Sharp amplification of stationary sandpile topplings by one edge on a tree

## Finding
For each integer \(N\ge1\), a tree with \(N+2\) vertices, a sink \(s\), and a source leaf \(r\) joined directly to the sink has exactly one mean toppling after a grain is added at \(r\). Adding one previously absent edge, while recomputing the uniform recurrent initial distribution on the new graph, can amplify the expectation. The sharp maximum over **every such tree and every missing edge** is
\[
M_N=\max_{1\le d\le N}\left(1+\frac{dN-d(d-1)/2-1}{d+2}\right).
\]
The maximizer is achieved by the path \(r,s,y_1,\ldots,y_N\) and the inserted edge \(\{r,y_d\}\). Writing \(d_*\) for the smallest maximizing distance, it is the first integer \(d\in[1,N]\) for which \((d+2)(d+3)\ge4(N+2)\). A tie with \(d+1\) occurs precisely when equality holds and \(d+1\le N\). In particular,
\[
M_N=N+\frac72-2\sqrt{N+2}+O(N^{-1/2}),
\]
so the attainable amplification factor diverges linearly while the optimal chord depth grows on a square-root scale.

## Assumptions and scope
The graph is finite, connected, undirected, simple, and unweighted, with one distinguished dissipative sink \(s\). Stable nonsink heights lie between zero and degree minus one. The starting state is sampled uniformly from recurrent stable states **for that graph**; after the edge insertion it is sampled anew from recurrent states of the modified graph. Add exactly one grain at \(r\) and stabilize; count every nonsink firing including repeats. The original graph is any tree \(T\) on \(N+2\) vertices with \(N\ge1\), where \(r\) is a leaf and \(\{s,r\}\) is an edge. The inserted edge joins two previously nonadjacent vertices, with no change to the sink designation. The maximum considers all original trees and all possible single-edge insertions, with vertex labels irrelevant.

## Proof
Let \(L\) be the reduced graph Laplacian, with the sink row and column removed, and \(e_r\) the source basis vector. If \(u\) is the toppling-count vector after adding at \(r\) to recurrent state \(h\), then the final recurrent state \(h'\) satisfies \(h'=h+e_r-Lu\). The sandpile addition map permutes the finite recurrent states, so the expected initial and final height vectors agree. Hence
\[
\mathbb E u=L^{-1}e_r,
\qquad \mathbb E X=\mathbf1^\mathsf TL^{-1}e_r.
\]
This is an exact finite-state stationary expectation, not a simulated approximation.

Root \(T\) at \(s\), writing \(\operatorname{dep}(v)\) for distance from \(s\). For nonsink vertices \(u,v\), the tree Green kernel is
\[
(L^{-1})_{uv}=\operatorname{dep}(\operatorname{LCA}(u,v)).
\]
To check, the matrix whose entries are the right side equals the sum, over tree edges directed away from the sink, of outer products of their descendant-set indicators; it is inverse to the grounded tree Laplacian by the tree path incidence factorization. Because \(r\) is the sink-adjacent leaf, \(L^{-1}e_r=e_r\), so \(\mathbb E X(T)=1\).

An added edge not incident to \(r\) leaves \(r\) a degree-one vertex attached only to the sink. Its grounded Laplacian component remains \([1]\), and its expected total topplings remain \(1\). Otherwise the added edge is \(\{r,x\}\) for a nonsink vertex \(x\ne r\). Let \(s=y_0,y_1,\ldots,y_d=x\) be the sink-to-\(x\) path; \(1\le d\le N\). Denote by \(q_i\) the size of the descendant subtree rooted at \(y_i\). The reduced Laplacian becomes \(L'=L+bb^\mathsf T\) with \(b=e_r-e_x\). In the original tree, the electrical effective resistance between \(r\) and \(x\) is \(d+1\); hence \(b^\mathsf TL^{-1}b=d+1\). Also
\[
\mathbf1^\mathsf TL^{-1}e_x=\sum_{i=1}^d q_i,
\qquad b^\mathsf TL^{-1}e_r=1.
\]
Applying the exact Sherman--Morrison identity gives
\[
\mathbb E X(T+\{r,x\})=1+\frac{\sum_{i=1}^d q_i-1}{d+2}. \tag{1}
\]
There are exactly \(N\) nonsink vertices other than \(r\). For the \(i\)-th vertex along the chosen root-to-\(x\) path, at least the preceding \(i-1\) vertices lie outside its descendant subtree. Thus \(q_i\le N-i+1\). Consequently
\[
\sum_{i=1}^d q_i\le dN-\frac{d(d-1)}2,
\]
and (1) yields the displayed bound for the depth \(d\). The path \(r,s,y_1,\ldots,y_N\) makes every inequality an equality for every \(1\le d\le N\), proving sharpness even when the original and augmented maximum degrees are at most three.

Set \(F_N(d)=1+(dN-d(d-1)/2-1)/(d+2)\). Direct subtraction gives
\[
F_N(d+1)-F_N(d)=\frac{2(N+2)}{(d+2)(d+3)}-\frac12.
\]
The right side decreases strictly with \(d\), so the smallest maximizing index is the first \(d\in[1,N]\) with \((d+2)(d+3)\ge4(N+2)\); the endpoint case \(N=1\) is included. Equality gives the stated adjacent tie when the next index is admissible. For \(h=d+2\), polynomial division gives
\[
F_N(d)=N+\frac72-\frac h2-\frac{2(N+2)}h.
\]
The continuous optimizer is \(h=2\sqrt{N+2}\), and minimizing over a neighboring integer changes the value by \(O(N^{-1/2})\). This proves the asymptotic formula, and the theorem.

## Verification
The standalone standard-library programs `verify_extremal.py` and `verify_formula.py` require Python 3 and must be located in the same directory. Run `python verify_extremal.py` and `python verify_formula.py`. The first independently solves rational grounded-Laplacian systems, enumerating every labeled tree satisfying the hypotheses and all missing-edge insertions through \(N=5\), comprising 20,796 edge tests; its observed maxima for \(N=1,2,3,4,5\) are \(1,3/2,2,13/5,16/5\), matching the theorem. The second checks all 7,035 source-incident chord instances through \(N=5\) against the rooted-descendant expression and checks the integer maximizer through \(N=499\). All comparisons are exact rational arithmetic. These finite checks corroborate but do not replace the all-\(N\) proof above.

## Relationship to prior work
Stationary recurrent sandpile dynamics and the Laplacian/toppling framework are standard; Járai (2011) surveys these foundations. Cori, Micheli and Rossin (2009) study mean avalanche statistics and tree avalanche polynomials. Matter and Nagnibeda (2011), especially Proposition 2.3.4, establish block-path dependence of avalanches on separable graphs; their cycle formula also covers a narrow triangle-with-attached-tree specialization. Austin et al. (2016) characterize avalanche polynomials for trees, cycles, wheels and complete graphs. **None of the examined primary claims provides the maximum over all trees and all one-edge augmentations with the sink-adjacent leaf condition, the exact maximizing chord depth, and the square-root optimality deficit.** The general stationary Green-function identity is not claimed as new; the new point is the universal sharp extremal optimization of its rank-one perturbation. A separate previously recorded chorded-cycle result concerns perturbations of cycles rather than trees and does not imply this extremal classification.

## Limitations
Only the expected **total firing count** under the uniform stationary recurrent measure is optimized; no assertion is made about stochastic dominance, maximum single-avalanche size, or nonstationary initial conditions. The special assumption that the source is a sink-adjacent leaf is essential to the baseline value and bound. The result does not determine the entire avalanche distribution. The proof is exact; finite enumeration is supporting verification. Historical priority has not been independently certified, particularly for unindexed specialized one-edge computations.

## References
- R. Cori, A. Micheli, D. Rossin, *Avalanche polynomials*, arXiv:0905.2823, first public 2009-05-18, https://arxiv.org/abs/0905.2823.
- M. Matter, T. Nagnibeda, *Abelian Sandpile Model on Randomly Rooted Graphs and Self-Similar Groups*, arXiv:1105.4036, first public 2011-05-20, https://arxiv.org/abs/1105.4036.
- A. A. Járai, *Abelian sandpiles: an overview and results on certain transitive graphs*, arXiv:1106.5358, first public 2011-06-27, https://arxiv.org/abs/1106.5358.
- D. Austin et al., *The Avalanche Polynomial of a Graph*, arXiv:1605.02713, first public 2016-05-09, https://arxiv.org/abs/1605.02713.
