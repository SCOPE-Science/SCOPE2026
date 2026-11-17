# Integral fixed-point persistence of uniform-matroid rank filtrations

## Finding
Let \(H\leq\mathfrak S_n\) be any permutation group on \([n]\), with nonempty orbits \(O_1,\ldots,O_m\), numbered so that \(w_1=|O_1|\leq\cdots\leq w_m=|O_m|\). For integers \(0\leq r\leq n\), let \(K_r\) be the uniform-matroid independence complex \(\{T\subseteq[n]:|T|\leq r\}\), and let \(X_r=|K_r|^H\) be its actual geometric fixed-point space. Put \(w(S)=\sum_{i\in S}w_i\) for \(S\subseteq\{2,\ldots,m\}\).

**Theorem.** For every \(q\geq0\), the entire reduced integral persistence module \(\{\widetilde H_q(X_r;\mathbb Z)\}_{r=0}^{n}\), with maps induced by inclusion, is naturally isomorphic after choosing one minimal orbit to a direct sum of interval modules
\[
\bigoplus_{\substack{\varnothing\ne S\subseteq\{2,\ldots,m\}\\ |S|=q+1}}\mathbb Z_{[w(S),\,w(S)+w_1)}.
\]
Here \(\mathbb Z_{[a,b)}\) denotes one copy of \(\mathbb Z\) at each integer \(a\leq r<b\), with identity transition maps inside the interval and zero elsewhere. Thus every positive-degree and reduced degree-zero bar has **the identical length \(w_1\)**, and all persistent groups and maps are free and split over \(\mathbb Z\). The complex \(X_r\) is empty for \(r<w_1\), and the terminal \(X_n\) is contractible. For \(m=1\), the above direct sum is empty.

If the smallest orbit \(O_1\) is unique, this decomposition is equivariant for the normalizer \(N_{\mathfrak S_n}(H)\). That normalizer permutes the other orbits by weight-preserving permutations. At level \(r\), \(\widetilde H_q(X_r;\mathbb Z)\) is exactly the signed permutation lattice on those \((q+1)\)-element subsets \(S\) of the other orbits with \(r-w_1<w(S)\leq r\), where the sign is the sign of the induced permutation on the ordered elements of \(S\). The rank-inclusion maps preserve precisely the common basis labels \(S\).

## Assumptions and scope
The group \(H\) is any subgroup of the finite symmetric group; the action is by permuting labels, not by a free-action assumption. All statements concern *geometric* fixed points of the ordinary rank filtration of the uniform matroids, not homotopy fixed points, quotient orbit spaces, or weighted boundary homology. The filtration parameter \(r\) is integral and inclusive. The zero-rank space is empty. We assert reduced homology in degrees \(q\geq0\); an augmented-chain formal interval in degree \(-1\) is not included in the displayed barcode. For the equivariant refinement, uniqueness of the minimum orbit size is essential to the specified natural normalizer-stable basis; the non-equivariant formula requires no such uniqueness.

## Proof
**1. Actual fixed points.** Write each point of \(|K_r|\) in its unique barycentric coordinates indexed by \([n]\). It is \(H\)-fixed if and only if its coordinates are constant on every \(H\)-orbit. Its positive support is a union of orbits whose total cardinality does not exceed \(r\). Mapping each orbit vertex \(i\) to the barycenter of \(O_i\) yields a filtration-preserving PL homeomorphism
\[
X_r\cong_{\mathrm{PL}}|L_r|,\qquad L_r=\{S\subseteq[m]:\sum_{i\in S}w_i\leq r\}.
\]

**2. Filtered integral chain basis.** Use augmented oriented simplicial chains \(\widetilde C_*(\Delta^{m-1};\mathbb Z)\), where the empty simplex has degree \(-1\), and give each oriented simplex \([S]\) filtration value \(w(S)\). Label the first vertex \(1\), and always list it first. For \(S\subseteq\{2,\ldots,m\}\), define
\[
y_S=[1,S],\qquad z_S=\partial[1,S]=[S]-[1,\partial S].\]
The last expression denotes the usual alternating simplicial boundary, with \(\partial[1]=[\varnothing]\) for \(S=\varnothing\). Because \(w_1\leq w_i\) for every \(i\in S\), every term \([1,S\setminus\{i\}]\) in \(z_S\) has filtration \(w_1+w(S)-w_i\leq w(S)\). Thus \(z_S\) enters the filtration exactly at \(w(S)\). The transformation replacing every \([S]\) without vertex \(1\) by \(z_S\) is unitriangular and filtration-preserving in both directions, with integer diagonal entries \(+1\). Together with the unchanged \(y_S\), it is an integral filtered basis.

In this basis the *entire augmented chain complex* splits as a direct sum of two-term filtered complexes, one per \(S\):
\[
\partial y_S=z_S,\qquad \partial z_S=0,\qquad
f(z_S)=w(S),\quad f(y_S)=w(S)+w_1.
\]
No field coefficients, extension splitting assumptions, or finite computation are needed. For nonempty \(S\), this two-term complex gives exactly one reduced homology interval in degree \(|S|-1\), born at \(w(S)\) and killed at \(w(S)+w_1\). The empty \(S\) contributes only a formal augmented degree \(-1\) interval. This proves the whole persistence module and its integral splitting, including every boundary rank and the empty and terminal cases.

**3. Residual symmetry.** If \(O_1\) is uniquely shortest, every element of \(N_{\mathfrak S_n}(H)\) maps \(O_1\) to itself and induces a weight-preserving permutation of the remaining orbit vertices. It acts on \([1,S]\) by the orientation sign of the permuted \(S\), and commutes with \(\partial\), so it sends \(y_S,z_S\) to the same signed pair with permuted label. The displayed filtered splitting is therefore normalizer-equivariant. At rank \(r\), precisely the summands with \(w(S)\leq r<w(S)+w_1\) contribute, proving the signed orbit-basis assertion.

## Verification
A standalone independent modulo-two boundary-matrix reduction and integral chain-identity checker enumerates all 205 nondecreasing weight tuples of length \(2\) through \(6\) with entries in \(\{1,2,3,4\}\). It compares their positive-length persistence intervals with the theorem, confirms 3,964 exact integral cycle/boundary-filtration identities, and checks 289 residual weight-preserving normalizer permutations in the unique-minimum cases of length at most five. The exact reproducible command is `python3 verify.py`; the recorded output is `verify_output.txt`.

For orbit weights \((1,3,3)\), the nonnegative-degree intervals are two degree-zero intervals \([3,4)\) and one degree-one interval \([6,7)\). For \((2,2,2)\), they are two degree-zero intervals \([2,4)\) and one degree-one interval \([4,6)\). These checks are finite corroboration only; the filtered integral chain splitting above is the proof for all groups and ranks.

## Relationship to prior work
The basic persistence framework goes back to Edelsbrunner, Letscher, and Zomorodian (2000), and filtered discrete Morse methods are developed by Mischaikow and Nanda (2013). Dawson (1990) studies an *arithmetically weighted boundary operator*, rather than ordinary homology of sublevel sets indexed by additive orbit cardinalities; the two notions are not interchangeable. Standard uniform-matroid topology gives sphere-wedge ranks at individual ordinary ranks; the result here concerns simultaneous *geometric group fixed loci*, all transition maps over \(\mathbb Z\), and—when the minimal orbit is unique—the complete normalizer module at each stage. No claim is made that the general persistence machinery or ordinary uniform-matroid homology is new.

## Limitations
The theorem does not determine homotopy types, multiplication or Steenrod operations, equivariant stable homotopy, or quotient-space homology. When several orbits tie for minimum size, the non-equivariant decomposition remains valid, but the chosen direct-sum basis is not asserted to be equivariant for a normalizer that interchanges the tied minimum orbits. The possibility of an equivalent earlier statement in general weighted-simplex persistence literature remains an originality risk.

## References
1. H. Edelsbrunner, D. Letscher, A. Zomorodian, *Topological Persistence and Simplification*, Proceedings of the 41st IEEE Symposium on Foundations of Computer Science (2000), 454–463. DOI: 10.1109/SFCS.2000.892133. https://ieeexplore.ieee.org/abstract/document/892133/
2. K. Mischaikow, V. Nanda, *Morse Theory for Filtrations and Efficient Computation of Persistent Homology*, Discrete & Computational Geometry **50** (2013), 330–353. DOI: 10.1007/s00454-013-9529-6. https://link.springer.com/content/pdf/10.1007/s00454-013-9529-6.pdf
3. R. J. MacG. Dawson, *Homology of Weighted Simplicial Complexes*, Cahiers de Topologie et Géométrie Différentielle Catégoriques **31** (1990), 229–243. https://www.numdam.org/item/CTGDC_1990__31_3_229_0/
