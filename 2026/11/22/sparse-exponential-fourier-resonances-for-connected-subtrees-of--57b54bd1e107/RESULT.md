# Sparse exponential Fourier resonances for connected subtrees of subdivided stars

## Finding
For an integer \(m\ge2\), let \(S_m\) be the tree with central vertex \(c\) and \(m\) pairwise disjoint length-two arms \(c-u_i-v_i\) (\(1\le i\le m\)). Let \(\mathcal C_m\) be its family of **nonempty, connected, vertex-induced subsets**, considered as binary vertex-incidence vectors in \(G_m=\mathbb F_2^{2m+1}\). Let \(T_m h=\mathbf1_{\mathcal C_m}*h\) denote unnormalized counting convolution.

For any Fourier character \(\xi\in G_m\), define \(k(\xi)\) to be the number of arms for which both coordinates of \(\xi\) vanish. The complete signed Walsh spectrum is the multiset
\[
\left\{\left(4j-m+3^j,\binom{m}{j}3^{m-j}\right),\;
\left(4j-m-3^j,\binom{m}{j}3^{m-j}\right):0\le j\le m\right\},
\]
where equal numerical levels have their multiplicities added. In particular, \(T_m\) is singular **if and only if**
\[
 m=4r+3^r\quad\text{for some integer }r\ge1.
\]
The exceptional arm counts start at \(7,17,39,97,\ldots\). The integer \(r\) is unique at each exceptional arm count. At \(m=4r+3^r\),
\[
\operatorname{nullity}(T_m)=\binom{m}{r} 3^{m-r},\qquad
\operatorname{rank}(T_m)=2^{2m+1}-\binom{m}{r} 3^{m-r}.
\]
The smallest strictly positive absolute Walsh multiplier at that singular order is **exactly**
\[
 g_r=4+2\cdot3^{r-1}.
\]
Consequently the exact Hilbert-space pseudoinverse norm is \(\|T_m^\dagger\|_{2\to2}=1/g_r\), and the ratio of largest to smallest nonzero singular values is \((3^m+3m)/g_r\). At the first nondegenerate resonance \(m=7\), the \(15\)-coordinate convolution has exactly \(5103\) vanishing frequencies, rank \(27665\), sharp nonzero gap \(6\), and nonzero singular-value ratio \(368\).

## Assumptions and scope
All graphs are finite, simple, and vertex-labelled by \(c,u_1,v_1,\ldots,u_m,v_m\). A singleton vertex is a connected subtree. The empty set is excluded. Two connected vertex subsets that happen to be isomorphic as unlabeled trees are **distinct** when their vertex sets differ. The coefficient kernel takes value one on each allowed binary vector, zero otherwise; there are no extra orientations, edge weights, or multiplicities. Characters are \(\chi_\xi(x)=(-1)^{\langle\xi,x\rangle}\), and the Fourier transform is the **unnormalized** sum \(\widehat f(\xi)=\sum_{x\in G_m}f(x)\chi_\xi(x)\). The convolution is on complex-valued functions with counting measure; the same rank statements hold over the reals.

The exceptional classification is asserted for every integer \(m\ge2\), without a finite-size ceiling. The excluded degenerate one-arm path has four zero modes among eight and is not part of the stated exceptional list.

## Proof
Let \(s_0=(-1)^{\xi_c}\), \(a_i=(-1)^{\xi_{u_i}}\), and \(b_i=(-1)^{\xi_{v_i}}\). Partition the connected vertex sets according to whether they contain the center. If the center is present, each arm contributes independently either no vertex, its near vertex, or both vertices. The signed sum of this class is
\[
 s_0\prod_{i=1}^m(1+a_i+a_ib_i).
\]
If the center is absent, connectedness forces the subset to be contained entirely in one arm, with exactly three possibilities \(\{u_i\}\), \(\{v_i\}\), and \(\{u_i,v_i\}\). Thus the remaining signed sum is
\[
 \sum_{i=1}^m(a_i+b_i+a_ib_i).
\]
This decomposition is exhaustive and disjoint.

The four assignments of \((a_i,b_i)\) give the ordered pair of local factors
\[
\begin{array}{c|cccc}
(a_i,b_i)&(+1,+1)&(+1,-1)&(-1,+1)&(-1,-1)\\ \hline
(1+a_i+a_ib_i,\;a_i+b_i+a_ib_i)&(3,3)&(1,-1)&(-1,-1)&(1,-1)
\end{array}.
\]
If exactly \(j\) arms have \((a_i,b_i)=(+1,+1)\), the sum of the second factors is \(3j-(m-j)=4j-m\), while the first product has magnitude \(3^j\). Its sign can be switched by the freely chosen central character \(s_0\). Choosing which \(j\) arms are positive-positive and the three other sign pairs on the remaining arms gives \(\binom{m}{j}3^{m-j}\) assignments; each has exactly one central sign for each of \(4j-m\pm3^j\). This proves the spectrum, including every multiplicity and possible collision of levels.

A zero requires \(m=4j+3^j\) or \(m=4j-3^j\). For \(j=0\) the positive solution is \(m=1\). For \(j=1\), the latter equation also gives \(m=1\). For all integers \(j\ge2\), \(3^j>4j\) (base case \(j=2\), then induction), so the latter equation has no positive solution. Thus for \(m\ge2\) a zero exists precisely when \(m=4r+3^r\) for some \(r\ge1\). The function \(4r+3^r\) is strictly increasing, so \(r\) is unique. The indicated multiplicity is therefore the exact nullity. The finite-group character diagonalization yields the rank formula.

To find the smallest nonzero magnitude at a resonant order, write \(m=F(r)\) with \(F(j)=4j+3^j\). The first branch of the spectrum is \(F(j)-F(r)\), which vanishes only at \(j=r\). Since \(F(j)\) is strictly increasing and its consecutive increments \(4+2\cdot3^j\) increase with \(j\), the smallest nonzero magnitude in that branch is \(F(r)-F(r-1)=4+2\cdot3^{r-1}\), achieved at \(j=r-1\). The second branch is \(4j-m-3^j\). Because \(3^j-4j\ge-1\) for all \(j\ge0\) (the minimum occurs at \(j=1\), since consecutive differences beyond it are \(2\cdot3^j-4>0\)), its absolute value is at least \(m-1\); and \(m-1\ge4+2\cdot3^{r-1}\) for \(r\ge1\), because their difference is \(4r-5+3^{r-1}\ge0\). This proves sharpness over both branches.

The zero-frequency coefficient is the number of allowed subtrees, \(3^m+3m\), and it is a largest-magnitude Walsh coefficient by the triangle inequality. Finally, Walsh characters form a unitary eigenbasis after normalization, so the Moore–Penrose pseudoinverse has norm the reciprocal of the least positive multiplier magnitude. The stated nonzero condition ratio follows.

## Verification
The accompanying standalone `verify_spider.py` independently enumerates connected vertex subsets from the actual graph adjacency lists, computes their complete integer Walsh transform by the butterfly algorithm, and compares the signed multiplicity histogram with the formula for every \(1\le m\le8\). The arithmetic resonances are independently checked for \(2\le m<500\), with singular gaps checked at the first seven exceptional indices. The verifier checks Parseval's identity and the nonempty-kernel Fourier-sum identity in each exhaustive case. The program exits with `PASS` if and only if its assertions succeed.

Selected exhaustive counts are:

| Arm count | Vertex count | Connected subsets | Fourier zeros | Least nonzero magnitude |
|---:|---:|---:|---:|---:|
| 2 | 5 | 15 | 0 | 1 |
| 3 | 7 | 36 | 0 | 2 |
| 4 | 9 | 93 | 0 | 3 |
| 5 | 11 | 258 | 0 | 2 |
| 6 | 13 | 747 | 0 | 1 |
| 7 | 15 | 2208 | 5103 | 6 |
| 8 | 17 | 6585 | 0 | 1 |

These finite computations **supplement**, rather than substitute for, the all-orders proof.

## Relationship to prior work
Tittmann, Averbouch and Makowsky introduced the ordinary subgraph-component polynomial \(Q(G;x,y)\) and the univariate connected-induced-subgraph polynomial, with vertex-elimination and articulation recurrences [1]. Li and Wang studied exact unsigned subtree counts and extremizers among tree families, explicitly including balanced spiders [2]. Both provide the natural enumeration framework; the present claim is instead a multivariate **signed** evaluation, its complete Walsh multiplicity law, and an infinite sparse arithmetic description of invertibility and sharp nonzero spectral gaps. The known unsigned count \(3^m+3m\) alone cannot determine Fourier zeros. Related binary Fourier results for consecutive-ones path supports and complete split-graph connected sets concern different graph families and do not imply the subdivided-star spectrum. The proof here is self-contained and makes no novelty claim for the general concept of a connected-subgraph polynomial.

## Limitations
No arbitrary-arm-length spider, general tree, edge-incidence embedding, endpoint \(\ell^1\) projection norm, or closed form for the least multiplier at **all nonresonant** values of \(m\) is asserted. The reported sharp pseudoinverse norm is the counting-measure \(\ell^2\)-operator norm. Published-source and mathematical-record comparisons cannot exclude an unindexed equivalent treatment of the signed multivariate spider specialization. Independent external mathematical validation has not been performed.

## References
[1] P. Tittmann, I. Averbouch and J. A. Makowsky, *The Enumeration of Vertex Induced Subgraphs with respect to the Number of Components*, arXiv:0812.4147, first posted 2008-12-22. https://arxiv.org/abs/0812.4147.

[2] S. Li and S. Wang, *Further analysis on the total number of subtrees of trees*, arXiv:1204.6152, first posted 2012-04-27. https://arxiv.org/abs/1204.6152.
