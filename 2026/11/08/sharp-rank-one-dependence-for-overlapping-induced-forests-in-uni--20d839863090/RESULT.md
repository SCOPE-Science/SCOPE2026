# Sharp rank-one dependence for overlapping induced forests in uniform Cayley trees

## Finding

Let \(T\) be a uniformly sampled labelled spanning tree on \([n]\). For two fixed vertex sets meeting in exactly one vertex, the internal edge counts have an exact *rank-one departure from independence*. This resolves their joint distribution, every upper-tail covariance, and the exact total variation distance from the product of their marginal laws.

Write \(X=|E(T[A])|\) and \(Y=|E(T[B])|\). With the definitions below, their bivariate probability-generating function is
\[
G(z,w)=(1-p+pz)^{a-2}(1-r+rw)^{b-2}\big[(1-p+pz)(1-r+rw)-\delta(z-1)(w-1)\big].\tag{1}
\]
The individual laws are \(\operatorname{Bin}(a-1,p)\) and \(\operatorname{Bin}(b-1,r)\). The two-variable departure from independence is entirely encoded by a *single pair* of negatively coupled Bernoulli indicators.

Let \(f(j)\) and \(g(j)\) be the mass functions of \(\operatorname{Bin}(a-2,p)\) and \(\operatorname{Bin}(b-2,r)\), respectively, with the masses set to zero outside their natural supports. Then for all integers \(k,\ell\),
\[
\Pr(X=k,Y=\ell)-\Pr(X=k)\Pr(Y=\ell)
=-\delta\,[f(k-1)-f(k)]\,[g(\ell-1)-g(\ell)].\tag{2}
\]
For integers \(1\le s\le a-1\) and \(1\le t\le b-1\),
\[
\Pr(X\ge s,Y\ge t)-\Pr(X\ge s)\Pr(Y\ge t)=-\delta f(s-1)g(t-1)<0.\tag{3}
\]
The exact joint-vs-independent total variation distance is
\[
\boxed{d_{\mathrm{TV}}\big(\mathcal L(X,Y),\mathcal L(X)\otimes\mathcal L(Y)\big)
=2\delta\max_j f(j)\max_j g(j).}\tag{4}
\]
If \(a/n\to\alpha>0\), \(b/n\to\beta>0\), and \(\alpha+\beta\le1\), this has the sharp asymptotic
\[
\boxed{d_{\mathrm{TV}}=\frac{1}{\pi n\sqrt{(1-\alpha)(1-\beta)}}+o(n^{-1}).}\tag{5}
\]
In particular, the dependence is strictly negative at every nontrivial pair of upper-tail thresholds but diminishes at exact order \(n^{-1}\) for macroscopic subsets.

## Assumptions and scope

All graphs are simple and undirected. Assume an integer \(n\ge3\), and fixed subsets \(A,B\subseteq[n]\) with \(a=|A|\ge2\), \(b=|B|\ge2\), \(|A\cap B|=1\), hence \(a+b-1\le n\). The sample space consists of the \(n^{n-2}\) equally likely labelled spanning trees of \(K_n\). The notation \(T[A]\) means the graph induced by \(A\) in \(T\), which is necessarily a forest. Set
\[
p=\frac an,\qquad r=\frac bn,\qquad \delta=\frac{(a-1)(b-1)}{n^2}.
\]
Both \(p,r\) lie strictly between zero and one. Total variation is \(d_{\mathrm{TV}}(P,Q)=\frac12\sum_x|P(x)-Q(x)|\), with the sum over the joint integer support. The convention \(\operatorname{Bin}(0,p)\) assigns mass one to zero. In the asymptotic assertion, integer sequences of subsets and sizes may be arbitrary subject to the stated conditions.

## Proof

**Weighted spanning-tree determinant.** Let \(\mathbf 1^\perp\) denote the space of vectors in \(\mathbb R^n\) whose coordinate sum is zero. The combinatorial Laplacian of the unweighted complete graph is \(nI-J\), acting as \(nI\) on \(\mathbf1^\perp\). For a set \(C\subseteq[n]\) of size \(c\ge2\), let \(P_C\) be the orthogonal projection onto the space \(W_C\) of vectors supported on \(C\) and summing to zero on \(C\). The Laplacian of the clique induced by \(C\) is precisely \(cP_C\). Because \(A\) and \(B\) share just one vertex, the two cliques have no common edge. Give edges internal to \(A\) weight \(z\), edges internal to \(B\) weight \(w\), and all other edges weight one. The weighted matrix-tree theorem, initially for nonnegative \(z,w\) and then as a polynomial identity, gives
\[
G(z,w)=\det_{\mathbf1^\perp}\!\left[I+\frac an(z-1)P_A+\frac bn(w-1)P_B\right].\tag{6}
\]

**Reduction to one coupled plane.** Denote the common vertex by \(v\). The spaces of vectors supported on \(A\setminus\{v\}\) with zero sum, and similarly on \(B\setminus\{v\}\), have dimensions \(a-2\) and \(b-2\). Each is orthogonal to the other clique's entire zero-sum space. The only interaction is through the unit vectors in the directions
\[
u_A=e_v-\frac1a\mathbf1_A,\qquad
u_B=e_v-\frac1b\mathbf1_B.
\]
Their squared normalized inner product equals
\[
\frac{\langle u_A,u_B\rangle^2}{\|u_A\|^2\|u_B\|^2}
=\frac{(a-1)(b-1)}{ab}.\tag{7}
\]
For two unit vectors with squared inner product \(c^2\), the determinant of \(I+suu^{\mathsf T}+tvv^{\mathsf T}\) on their span is \((1+s)(1+t)-stc^2\). The orthogonal residual directions in (6) each contribute a factor \(1+p(z-1)\) or \(1+r(w-1)\). Taking \(s=p(z-1)\), \(t=r(w-1)\), and applying (7) proves (1).

**Independent binomials plus one coupled Bernoulli pair.** The bracket in (1) is the generating polynomial of a pair \((V_A,V_B)\) of Bernoulli random variables whose marginal success probabilities are \(p,r\), and whose joint success probability is \(pr-\delta=(a+b-1)/n^2\). Explicitly, with \(h_{ij}=\Pr(V_A=i,V_B=j)\),
\[
\begin{aligned}
h_{11}&=\frac{a+b-1}{n^2},& h_{10}&=p-h_{11},\\
h_{01}&=r-h_{11},&h_{00}&=\frac{(n-1)(n-a-b+1)}{n^2}.
\end{aligned}\tag{8}
\]
All entries are nonnegative because \(a,b\ge2\) and \(a+b-1\le n\). Thus \((X,Y)\) equals in law \((U_A+V_A,U_B+V_B)\), with independent \(U_A\sim\operatorname{Bin}(a-2,p)\), \(U_B\sim\operatorname{Bin}(b-2,r)\), and the Bernoulli pair independent of both. Substitution \(w=1\), respectively \(z=1\), gives the asserted marginal binomials.

**Signed local and upper-tail dependence.** Subtracting the product of the marginal generating functions from (1) yields \(-\delta(z-1)(w-1)F(z)H(w)\), where \(F(z)=(1-p+pz)^{a-2}\) and \(H(w)=(1-r+rw)^{b-2}\). Comparing coefficients gives (2). Summing in \(k\ge s\) and \(\ell\ge t\) telescopes separately: \(\sum_{k\ge s}[f(k-1)-f(k)]=f(s-1)\), and similarly for \(g\). This proves (3), with strictness because every mass on the binomial support is positive. In particular \(\operatorname{Cov}(X,Y)=-\delta\) by differentiating the generating function at \((z,w)=(1,1)\).

**Exact and asymptotic total variation.** By (2),
\[
2d_{\mathrm{TV}}=\delta\left(\sum_k|f(k-1)-f(k)|\right)\left(\sum_\ell|g(\ell-1)-g(\ell)|\right).
\]
A binomial mass function is unimodal, and its boundary values outside support are zero. Hence each sum is exactly twice its maximal mass, proving (4), including the boundary cases \(a=2\) or \(b=2\). Under the limiting size assumptions, \(a,b\to\infty\), and the binomial Stirling estimate at any mode yields
\[
\max f=\frac{1+o(1)}{\sqrt{2\pi(a-2)p(1-p)}},\qquad
\max g=\frac{1+o(1)}{\sqrt{2\pi(b-2)r(1-r)}}.
\]
Since \(a/n\to\alpha\) and \(b/n\to\beta\), with \(\alpha,\beta>0\) and \(\alpha+\beta\le1\), both limits are strictly below one. Also \(\delta\to\alpha\beta\). Inserting into (4) proves (5). All steps are exact finite identities or ordinary Stirling estimates; no numerical extrapolation is used to establish the infinite claim.

## Verification

The accompanying standalone `verify.py` independently enumerates every labelled tree via Prüfer sequences for \(3\le n\le7\) and every admissible pair of subset sizes \((a,b)\), with canonical sets meeting at vertex zero. It compares the resulting exact rational joint probabilities with the Bernoulli decomposition and independently checks every marginal, the signed covariance, every nontrivial joint upper-tail gap, and the exact total variation formula. Running `python verify.py` prints `VERIFY_OK 777 exact assertions; exhaustive Pruefer n=3..7`. Exact finite enumeration tests (1)–(4), not the asymptotic for all sizes, which follows from the proof.

For numerical illustration only, along sequences with \(a/n\to0.35\) and \(b/n\to0.40\), the constant in (5) is approximately \(0.50970\). The full algebraic argument proves (5) for all admissible sequences under the stated hypotheses.

## Relationship to prior work

The matrix-tree theorem and spanning-tree transfer-current framework are classical. Stark (2011), Theorems 1–2, calculates individual edge inclusion and the distinction between adjacent and disjoint edge pairs in uniformly random complete-graph spanning trees; those statements are not the exact two-subset joint law (1). Hladký, Nachmias and Tran (first posted 2017) study local limits of uniform spanning trees on dense graphs; their scope does not give this exact finite overlapping-subset bivariate distribution. Dong and Ge (first posted 2021), with Moon's older containment result, enumerate trees containing prescribed spanning forests, a different general enumeration problem that supplies context but does not directly state (1)–(5). Avena and Gaudillière describe the general determinantal spanning-forest machinery. This result is a special closed-form consequence of the classical weighted matrix-tree principle, not a claim of novelty for that principle or for pairwise edge negative association.

## Limitations

The formula requires the two vertex sets to intersect in **exactly one** vertex and the underlying random tree to be uniform on the complete graph; larger overlaps and noncomplete graphs generally have higher-rank interactions. The strict upper-tail relation covers only the listed nontrivial integer thresholds. The leading constant in (5) requires both subset sizes to be macroscopic; no uniform rate in sparse or near-full boundary regimes is claimed. No general negative-association statement for arbitrary functions of the two induced forests is proved. Historical priority for the precise joint-count identity and sharp total variation constant remains unconfirmed despite the inspected sources; a 2018 transfer-current-related paper was not available in full text, though its abstract describes a general theorem rather than this calculation. Independent mathematical review has not been performed.

## References

- Hladký, J., Nachmias, A., and Tran, T. (2017 initial arXiv posting), *The local limit of the uniform spanning tree on dense graphs*. https://arxiv.org/abs/1711.09788
- Dong, Z. and Ge, H. (2021 initial arXiv posting), *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*. https://arxiv.org/abs/2103.05294
- Stark, D. (2011), *The Edge Correlation of Random Forests*, Annals of Combinatorics, 15, 529–539. https://doi.org/10.1007/s00026-011-0104-7
- Avena, L. and Gaudillière, A. (2013 initial arXiv posting), *Random spanning forests, Markov matrix spectra and well distributed points*. https://arxiv.org/abs/1310.1723
- Avena, L. and Gaudillière, A. (2018), *A proof of the transfer-current theorem in absence of reversibility*. https://doi.org/10.1016/j.spl.2018.06.007
