# The first three binary two-plane Plücker shattering complexes

## Finding

Let \(\mathcal G_n\) be the Boolean concept class of Plücker-coordinate vectors of all two-dimensional subspaces of \(\mathbb F_2^n\), queried at the coordinate pairs \(E_n=\binom{[n]}2\). For \(n\in\{4,5,6\}\), the **complete** shattered-support polynomials, including the empty support, are
\[
\begin{aligned}
\Phi_4(z)&=1+6z+15z^2+20z^3+3z^4,\\
\Phi_5(z)&=1+10z+45z^2+120z^3+150z^4+72z^5+10z^6,\\
\Phi_6(z)&=1+15z+105z^2+455z^3+1185z^4+1833z^5+1210z^6+300z^7+15z^8.
\end{aligned}
\]
Thus \(\operatorname{VCdim}(\mathcal G_n)=2n-4\) in these three orders. Each shattered-support complex is **nonpure**. Its inclusion-maximal supports, treated as simple graphs on the \(n\) labeled ambient coordinates, are precisely the following graph types (with multiplicity of labeled instances):

| \(n\) | Number of edges | Complete facet classes, with counts |
| --- | --- | --- |
| 4 | 3 | \(K_{1,3}\) (4), \(K_3\sqcup K_1\) (4) |
| 4 | 4 | \(K_{2,2}\) (3) |
| 5 | 4 | \(K_{1,4}\) (5), \(K_3\sqcup K_2\) (10) |
| 5 | 5 | \(C_5\) (12) |
| 5 | 6 | \(K_{2,3}\) (10) |
| 6 | 5 | \(K_{1,5}\) (6), the six-vertex double-star with adjacent degree-three vertices (90) |
| 6 | 6 | \(C_6\) (60), \(K_3\sqcup K_3\) (10) |
| 6 | 7 | The theta graph with three internally disjoint terminal paths of lengths 2, 2, 3 (180) |
| 6 | 8 | \(K_{2,4}\) (15) |

Over \(\mathbb F_2\), the complete nonzero reduced homology ranks are
\[
\begin{array}{ll}
n=4:&\widetilde\beta_2=7,\\
n=5:&\widetilde\beta_3=5,\ \widetilde\beta_4=1,\\
n=6:&\widetilde\beta_4=111,\ \widetilde\beta_5=24.
\end{array}
\]
All other reduced Betti numbers vanish in those three orders. The maximum-size shattered supports form one vertex-relabeling orbit, represented by \(K_{2,n-2}\), in each order.

## Assumptions and scope

For each fixed integer \(n\in\{4,5,6\}\), the coordinates of the ambient binary vector space are labeled \(0,\ldots,n-1\). An element \(L\in\operatorname{Gr}(2,n)(\mathbb F_2)\) is a two-dimensional linear subspace. Select an ordered basis \(u,v\) of \(L\) and put \(p_{ij}(L)=u_iv_j+u_jv_i\in\mathbb F_2\), for \(i<j\). This vector is independent of the choice of basis, because every element of \(\mathrm{GL}_2(\mathbb F_2)\) has determinant one. The Boolean concept \(c_L:E_n\to\{0,1\}\) has \(c_L(ij)=p_{ij}(L)\).

A support \(S\subseteq E_n\) is *shattered* when every function \(b:S\to\{0,1\}\) is \(c_L|_S\) for some two-plane \(L\). Define \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}\). The shattering complex is the simplicial complex of such supports. Facet types refer to the simple graphs with vertex set \([n]\) and edge set \(S\); the count includes labeled isolated vertices. Homology is reduced simplicial homology over \(\mathbb F_2\), including the augmentation at dimension zero. These exact numerical and topological assertions are restricted to \(n=4,5,6\). No general higher-order classification or integral homotopy type is asserted.

## Proof

**1. Four-symbol normal form.** Treat the \(i\)-th column of the ordered two-row basis matrix as a symbol in \(\mathbb F_2^2=\{0,a,b,c\}\), with \(a,b,c\) the nonzero vectors. The determinant \(p_{ij}\) equals one exactly when the two column symbols are distinct and nonzero. Consequently the support graph of every concept is a complete tripartite graph on the three nonzero-symbol classes, with any zero-symbol vertices isolated. Conversely, every such assignment with at least two occupied nonzero classes yields a rank-two matrix, hence a two-plane. Changing row basis permutes the three nonzero column symbols. This proves the bijection between concepts and row-color assignments modulo \(S_3\) and yields exactly \((2^n-1)(2^n-2)/6\) distinct concepts, namely 35, 155, and 651 in the three orders.

**2. A conceptual lower bound.** Fix two coordinates \(i,j\) with column colors \(a,b\). For each other coordinate \(k\), its two queried edges \(ik,jk\) realize arbitrary bits \((0,0),(0,1),(1,0),(1,1)\) by choosing its column symbol \(0,a,b,c\), respectively. These choices are independent for distinct \(k\). Hence the \(2n-4\) edges of \(K_{2,n-2}\) are shattered, for every \(n\ge3\). Their presence proves the stated lower VC bounds, and supplies constructive witnesses for every trace on each top facet.

**3. Exhaustive upper bound, face coefficients, and maximal types.** In each of the three specified orders, independently generate the finite set of concepts either (a) by all \(4^n\) column-symbol assignments with the tripartite rule, removing degenerate and duplicate concepts, or (b) by all ordered pairs of linearly independent binary rows and their two-by-two minors, removing duplicate concepts. In either construction the number of retained concepts matches the count of Step 1. Encode each concept as a bitmask on the lexicographically ordered pairs of coordinates. Inspect *every* one of the \(2^{\binom n2}\) possible support masks \(S\), retaining \(S\) precisely when
\[
\bigl|\{c\cap S:c\in\mathcal G_n\}\bigr|=2^{|S|}.
\]
This is the definition of shattering and no pruning beyond the logically necessary comparison \(2^{|S|}\le|\mathcal G_n|\) is applied. Count retained masks by size to obtain the three asserted polynomials. A shattered support is maximal precisely when no one-edge extension is shattered; downward closure proves that this tests all strict extensions. Canonicalize each maximal support under *all* \(n!\) permutations of the coordinate labels. The resulting six, ten, and fifteen coordinate-edge bitmasks identify exactly the graph-isomorphism types and labeled multiplicities in the table, with facet-size distributions \(8,3\) at \(n=4\); \(15,12,10\) at \(n=5\); and \(96,70,180,15\) at \(n=6\). In particular there are no faces larger than \(2n-4\) in the respective finite cases. Every maximal support has one of the listed types, so each complex is nonpure.

**4. Exact homology.** For each \(k\ge1\), list all \(k\)-element shattered supports as \((k-1)\)-simplices and form the simplicial boundary matrix \(\partial_{k-1}\) over \(\mathbb F_2\), one column per support and one row for each deletion of a queried edge; the augmentation rank at the first nonempty level is one. Exact binary Gaussian elimination gives ranks for \(\partial_{k-1}\), listed by face size \(k\):
\[
\begin{array}{c|l}
n& (k:\operatorname{rank}\partial_{k-1})\\\hline
4&(2:5),(3:10),(4:3)\\
5&(2:9),(3:36),(4:84),(5:61),(6:10)\\
6&(2:14),(3:91),(4:364),(5:821),(6:901),(7:285),(8:15).
\end{array}
\]
For \(k\ge1\), the reduced Betti rank at degree \(k-1\) is \(f_{k-1}-\operatorname{rank}\partial_{k-1}-\operatorname{rank}\partial_k\), where \(f_{k-1}\) is the number of shattered supports of size \(k\), \(\operatorname{rank}\partial_0=1\), and the final boundary rank is zero. Substitution gives exactly the displayed nonzero reduced Betti numbers, with all others zero. This is an exact finite-field rank computation; it does not assert torsion freedom or wedge-of-spheres homotopy type.

## Verification

`verify_plucker_python.py` and `verify_plucker_cpp.cpp` are standalone, independently structured implementations of Steps 1, 3, and 4; the former generates tripartite masks from column colors, and the latter generates minors from independent binary rows. They enumerate respectively \(2^6=64\), \(2^{10}=1024\), and \(2^{15}=32768\) query supports. Both exhaustively compare every support's distinct traces against the exact full mask count; verify facet maximality; compute every permutation canonical representative; and perform independent exact mod-two Gaussian elimination on simplicial boundary matrices. Their outputs agree byte for byte, included as `checks.txt`. Only the finite instances explicitly listed above are exhaustively verified. These programs use no third-party libraries and run under Python 3 and a C++17 compiler.

## Relationship to prior work

The Plücker embedding, two-plane enumeration and Grassmann codes are classical. Beelen--Singh, *Point-line incidence on Grassmannians and majority logic decoding of Grassmann codes* (first arXiv posting 2020-01-17, arXiv:2001.06278), defines the same Grassmannian point coordinates and studies point-line paths and majority decoding. Its Theorem 4.4 constructs parity-check families, not the full projection-trace or shattering complex. Piñero--Singh, *The weight spectrum of certain affine Grassmann codes* (2019; DOI below), studies weights of linear **codewords** on Grassmannian points, not restrictions of a **single point** to arbitrary collections of Plücker coordinates. The distinct quantifiers matter: a codeword weight or a full-code dual relation does not by itself give all trace masks for every selected set of minors. Fitzpatrick--Iosevich--McDonald--Wyman (2021) studies sphere-membership VC dimension over finite fields, not these coordinate incidence hypotheses. Searches of published mathematical finding records for shattering, binary Plücker incidence, alternating-matrix and Grassmannian projection aliases located nearby mathematical subjects, but no exact covering implication among the inspected results. The three enumerations, facet types, and homology ranks here are the assessed contribution; the Grassmannian normal form and known code-theoretic facts are not claimed as new.

## Limitations

The assertion of original priority is provisional: unindexed papers, tables, software and inaccessible earlier records could contain equivalent finite calculations. The exhaustive algorithm is a valid proof *only* for the stated three orders, not an all-order theorem. The mod-two Betti numbers are not integral-homology or homotopy classifications. No independent mathematical audit has been carried out.

## References

1. P. Beelen and P. Singh, *Point-line incidence on Grassmannians and majority logic decoding of Grassmann codes*, arXiv:2001.06278, first posted 2020-01-17. https://arxiv.org/abs/2001.06278
2. F. L. Piñero and P. Singh, *The weight spectrum of certain affine Grassmann codes*, *Designs, Codes and Cryptography* **87** (2019), 817--830, DOI:10.1007/s10623-018-0567-1. https://doi.org/10.1007/s10623-018-0567-1
3. D. Fitzpatrick, A. Iosevich, B. McDonald, and E. Wyman, *The VC-dimension and point configurations in finite fields*, arXiv:2108.13231 (2021). https://arxiv.org/abs/2108.13231
4. J. A. Castillo and J. Samper, *Finiteness theorems for matroid complexes with prescribed topology*, arXiv:1809.00281. https://arxiv.org/abs/1809.00281
