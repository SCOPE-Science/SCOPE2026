# Nonvanishing and exponential rational homology in the two-independence complexes of squared cycles

## Finding
For every integer \(n\ge5\), the two-independence complex \(X_n=\operatorname{Ind}_2(C_n^2)\) is not rationally acyclic. The signed face sum
\[
Z_n=\sum_{F\in X_n}(-1)^{|F|}=-\widetilde\chi(X_n)
\]
is nonzero for all \(n\ge5\). Its only negative term in that range is \(Z_9=-2\). The exact recurrence and initial values are
\[
Z_{n+7}=Z_{n+2}+2Z_{n+1}+Z_n\quad(n\ge5),
\qquad (Z_5,\ldots,Z_{11})=(6,10,8,1,-2,6,23).
\]
Writing \(\rho\) for the unique positive solution of \(\rho^7=(\rho+1)^2\), approximately \(1.262775453\), the asymptotic is \(Z_n=\rho^n+O(\sigma^n)\) for some \(0<\sigma<\rho\). Consequently,
\[
\liminf_{n\to\infty}\left(\sum_{j\ge0}\dim_{\mathbb Q}\widetilde H_j(X_n;\mathbb Q)\right)^{1/n}\ge\rho.
\]
This gives an exponential lower bound on total reduced rational homology without asserting which homological degrees contribute.

## Assumptions and scope
The graph \(C_n^2\) has vertex set \(\mathbb Z/n\mathbb Z\) and an edge between distinct residues whose circular distance is one or two. The lower bound \(n\ge5\) ensures that the four neighbors \(i-2,i-1,i+1,i+2\) of each vertex are distinct. The simplicial complex \(X_n\) contains the empty face and those subsets \(F\) such that the induced graph on \(F\) has maximum degree at most one; this is equivalent to all induced components having at most two vertices. Reduced homology is over \(\mathbb Q\) unless otherwise indicated. All recurrences have integer indices and refer to this single family of complexes.

## Proof
1. Encode a face by a cyclic binary word \(b_0,\ldots,b_{n-1}\). The membership condition is precisely that, for each index \(i\), either \(b_i=0\) or
\[
b_{i-2}+b_{i-1}+b_{i+1}+b_{i+2}\le1,
\]
where subscripts are reduced modulo \(n\). This local five-bit test holds for every \(n\ge5\).

2. Form a weighted \(16\)-state transfer matrix \(T\) indexed by four-bit strings \(u=(u_0,u_1,u_2,u_3)\). For each new bit \(e\in\{0,1\}\), let \(v=(u_1,u_2,u_3,e)\). Put \(T_{u,v}=(-1)^e\) if \(u_2=0\), or if \(u_2=1\) and \(u_0+u_1+u_3+e\le1\); put \(T_{u,v}=0\) otherwise. This definition is unambiguous: for each pair of length-four strings there is at most one possible incoming bit. A closed length-\(n\) walk in this automaton is uniquely determined by an indexed cyclic \(n\)-bit string, and it is permitted exactly for the faces in step 1. Its weight is \((-1)^{\sum_i b_i}\). Hence
\[
Z_n=\operatorname{tr}(T^n)\qquad(n\ge5).
\]

3. Exact integer characteristic-polynomial evaluation gives
\[
\det(xI_{16}-T)=x^{11}(x^5-x^4+x^2-x-1).
\]
The attached stand-alone program reconstructs all \(16\) matrix rows from the above transition rule and verifies the full characteristic polynomial using Newton identities with integer arithmetic. Thus \(Z_n\) is the sum of the powers \(\lambda^n\) of the five roots \(\lambda\) of the displayed quintic, counted with multiplicity. The identity
\[
(x^2+x+1)(x^5-x^4+x^2-x-1)=x^7-(x+1)^2
\]
therefore implies
\[
Z_{n+7}=Z_{n+2}+2Z_{n+1}+Z_n
\]
for all positive integer \(n\), in particular for every \(n\ge5\).

4. Exact evaluations of the transfer matrix give
\[
(Z_5,Z_6,\ldots,Z_{16})=(6,10,8,1,-2,6,23,34,27,8,3,33).
\]
All terms indexed \(10\) through \(16\) are positive. Inductively, the seven-step relation makes every later term positive, because its three right-hand terms have smaller indices and are positive. Terms indexed \(5\) through \(9\) are nonzero, with only \(n=9\) negative. This proves nonvanishing for every permitted index.

5. Let \(g(r)=r^7/(r+1)^2\) for \(r>0\). It is strictly increasing from zero to infinity, since its logarithmic derivative is \(7/r-2/(r+1)>0\). It therefore has a unique positive solution \(\rho\) to \(g(\rho)=1\), and \(\rho>1\). The quintic factor vanishes at this solution because \(\rho^2+\rho+1>0\). For any complex root \(\lambda\) of the quintic, the factorization implies
\[
|\lambda|^7=|\lambda+1|^2\le(|\lambda|+1)^2.
\]
Monotonicity of \(g\) gives \(|\lambda|\le\rho\); equality in the triangle inequality would force \(\lambda\) to be a nonnegative real number, hence \(\lambda=\rho\). The root \(\rho\) is simple because \(g\) is strictly increasing with positive derivative at \(\rho\). All other roots have modulus strictly smaller than \(\rho\), proving \(Z_n=\rho^n+O(\sigma^n)\) for an appropriate \(\sigma<\rho\).

6. Euler–Poincaré gives \(\widetilde\chi(X_n)=\sum_j(-1)^j\dim_{\mathbb Q}\widetilde H_j(X_n;\mathbb Q)=-Z_n\). The sum of nonnegative Betti numbers is therefore at least \(|Z_n|\). The nonzero signed sum shows that reduced rational homology never vanishes, and taking \(n\)-th roots yields the claimed exponential lower bound.

## Verification
The attached executable `verify_square_cycle.py` uses only Python's standard library. It constructs the matrix directly from the five-bit condition and derives its full degree-sixteen characteristic polynomial from the first sixteen traces via Newton identities. It verifies the seven-step identity for sixty-three further indices, and separately enumerates all vertex subsets of \(C_n^2\) for every \(5\le n\le16\), checking each of two local membership routines and comparing the alternating sum to the transfer trace. The recorded output `verify_square_cycle.out` is reproducible with `python3 verify_square_cycle.py`. These finite checks support the exact transfer calculation; the proof of nonvanishing for unbounded \(n\) is the induction in step 4, not finite enumeration.

## Relationship to prior work
The first higher-independence parameter is the degree-at-most-one or dissociation condition. Taylan's 2015 work classifies devoid complexes of ordinary cycles and paths, with Theorem 5.2 concerned with \(\mathcal D(C_n;P_k)\) rather than cycle squares. Adamaszek and Adams's 2015 work classifies Vietoris–Rips *clique* complexes of sampled circles; their graph at scale two can have the same one-skeleton \(C_n^2\), but a flag clique complex has a different simplex membership rule. Deshpande and Singh's 2020 preprint determines higher-independence homotopy types for the original cycle graphs, not their graph squares. Orlovich et al. study extremal dissociation sets, not these topological Euler signs. None of those inspected theorems implies the present signed recurrence or universal nonvanishing statement. No definitive publication-priority claim is made against unindexed or inaccessible work.

## Limitations
The theorem establishes nonvanishing and an exponential lower bound on the *sum* of reduced rational Betti numbers. It does not determine individual Betti numbers, homotopy types, integral torsion or equivariant homology. The transfer matrix covers only cycle squares and the degree-at-most-one condition; it is not a classification for higher graph powers or higher independence parameters. The originality assessment is limited to the specified accessible primary literature and indexed comparisons, and independent mathematical validation has not been performed.

## References
- D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1 (first posted 2015-01-27), especially Theorem 5.2. https://arxiv.org/abs/1501.06754
- M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669v1 (first posted 2015-03-12), Sections 2–4. https://arxiv.org/abs/1503.03669
- P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448v1 (first posted 2020-01-15), Theorem 4.6. https://arxiv.org/abs/2001.05448
- Y. Orlovich, A. Dolgui, G. Finke, V. Gordon and F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366, doi:10.1016/j.dam.2011.04.023.
