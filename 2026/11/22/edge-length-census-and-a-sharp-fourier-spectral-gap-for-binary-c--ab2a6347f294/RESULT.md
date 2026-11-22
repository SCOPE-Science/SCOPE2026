# Edge-length census and a sharp Fourier spectral gap for binary cyclic transversal polytopes

## Finding

For integers \(d\ge1\) and \(n\ge2\), let \(q=2^d\), and let \(P_{d,n}\subset\mathbb R^{nq}\) be the convex hull of the one-hot encodings of every word \((x_1,\ldots,x_n)\in(\mathbb F_2^d)^n\) satisfying \(x_1+\cdots+x_n=0\). Equip its intrinsic affine span with the metric induced by the ordinary Euclidean inner product of \(\mathbb R^{nq}\). There are \(q^{n-1}\) vertices.

The **complete Euclidean edge-length enumerator** is
\[
E_{d,n}(z)=\frac{q^{n-1}}2\left((q-1)\binom n2 z^{\sqrt4}+\sum_{s=3}^{\min\{n,d+1\}}\binom ns\prod_{j=0}^{s-2}(q-2^j)\,z^{\sqrt{2s}}\right).
\]
Here each exponent denotes the **Euclidean length**, and the formula records the number of undirected edges of that length; the sum is empty if its upper limit is below three. In particular the graph is regular, with degree equal to twice the sum of the enumerator coefficients divided by \(q^{n-1}\). For all \(d\ge1\), the graph is complete when \(n=2\) or \(n=3\), and is not complete when \(n\ge4\).

The two asymptotic regimes contrast sharply. For fixed \(d\), the vertex degree is a polynomial of degree \(d+1\) in \(n\), with leading term \(\prod_{j=0}^{d-1}(q-2^j)\,n^{d+1}/(d+1)!\); the fraction of other vertices adjacent to a fixed vertex tends to zero exponentially. For fixed \(n\ge4\), as \(q=2^d\) grows, the fraction of other vertices adjacent to a fixed vertex is
\[
1-\frac{2^{n-1}-n-1}{q}+O_n(q^{-2}).
\]

In the first nontrivial binary rank \(d=2\) (four symbols), all adjacency eigenvalues and their multiplicities also admit an explicit **Fourier spectrum**. For every nonnegative four-tuple \(m=(m_0,m_1,m_2,m_3)\) with \(\sum m_u=n\), set
\[
\lambda_n(m)=16\sum_u\binom{m_u}{3}+4(3-n)\sum_u\binom{m_u}{2}-\binom n2+2\binom n3.
\]
The multiplicity of an eigenvalue \(t\) is
\[
\operatorname{mult}(t)=\frac14\sum_{m:\,\lambda_n(m)=t}\frac{n!}{m_0!m_1!m_2!m_3!}.
\]
The degree is \(\Delta_n=3\binom n2+6\binom n3\). The **smallest positive combinatorial Laplacian eigenvalue** is exactly
\[
\boxed{\mu_2(P_{2,n}^{(1)})=4(n-1)^2}. 
\]
Its multiplicity is three for \(n=2\), fifteen for \(n=3\), and \(3n\) for every \(n\ge4\). The superscript \((1)\) denotes the undirected one-skeleton, not a higher-dimensional Laplacian.

## Assumptions and scope

The symbol set is the additive vector space over \(\mathbb F_2\), without additional weights or vertex deletions. Words are encoded by the coordinate unit vectors \(\mathbf e_x\) in \(\mathbb R^q\). Distinct words give distinct polytope vertices (a linear functional selecting one symbol in each block exposes each admissible word). Graph adjacency is in the **polytope's one-skeleton**, not Hamming adjacency on the ambient code. Each changed one-hot block contributes exactly two to squared Euclidean distance. All formulas hold for all integers in their stated ranges. For \(d=2\), the Fourier spectral description assumes the full set of zero-sum words and the unweighted simple adjacency graph.

## Proof

**1. Criterion and circuit count.** For two words \(x,y\), put \(\delta_i=x_i+y_i\), with addition in \(\mathbb F_2^d\); then \(\sum_i\delta_i=0\). The standard cyclic-transversal adjacency criterion states that \(x,y\) are connected by a polytope edge precisely when their nonzero differences form a nonempty *minimal zero-sum sequence*: no proper nonempty subcollection sums to zero (Frede, thesis, Lemma 2.37). It follows directly by examining the smallest face of the product of coordinate simplices containing the two words: an independent proper zero-sum subcollection permits two independent moves and a midpoint decomposition, while its absence forces the endpoint segment to be a one-dimensional face. This criterion is prior work, not asserted as new.

A minimally dependent sequence over \(\mathbb F_2\) is either two copies of one nonzero vector, or \(s\ge3\) **distinct** nonzero vectors \(v_1,\ldots,v_s\) with \(v_s=v_1+\cdots+v_{s-1}\) and \(v_1,\ldots,v_{s-1}\) linearly independent. In the second case \(s\le d+1\). Indeed, if a smaller nonempty dependency existed it would contradict minimality; conversely, independence of the first \(s-1\) vectors ensures that their unique nontrivial dependence after adjoining the last one uses all \(s\) vectors. Choose the \(s\) positions in \(\binom ns\) ways. Choosing the first \(s-1\) ordered independent differences gives \(\prod_{j=0}^{s-2}(q-2^j)\) possibilities and uniquely forces the last difference; each selected coordinate order is fixed, so no factorial overcount occurs. For \(s=2\), choose a pair of positions and one nonzero vector, producing \((q-1)\binom n2\) moves. Every move is reversible and translation of the words by a zero-sum word acts transitively on vertices. Hence the edge counts are half the vertex count times the corresponding number of moves, as stated, and squared Euclidean edge length is \(2s\).

A zero-sum difference supported on at most three positions must either be a repeated pair or a three-term minimal dependency; therefore the graph is complete for \(n=2,3\). For \(n\ge4\), any difference word with the same fixed nonzero element in four positions and zero elsewhere has total zero but contains a proper zero-sum pair, so it connects two distinct nonadjacent vertices.

**2. Complementary density limits.** For fixed \(d\), the highest nonzero circuit term is \(s=d+1\), proving the degree's leading term and exponential sparsity relative to \(q^{n-1}\). For fixed \(n\ge4\), count nonneighbors among the \(q^{n-1}\) zero-sum difference words by their first-order large-\(q\) degeneracies. Excluding the all-zero word, the dominant nonminimal words have exactly one *linear collision among the first \(n-1\) freely chosen differences*; such degeneracies are: one zero coordinate among the first \(n-1\), giving \(n-1\); their full-sum zero, giving one; and two of the first \(n-1\) vectors equal, giving \(\binom{n-1}{2}\), with the resulting last coordinate nonzero. But a single zero coordinate is not necessarily a failure of minimality: after removing zeros, generic nonzero differences are independent with their last forced sum and form a minimal circuit. Thus the actual first-order failures are when two **nontrivial independent subsets** partition the dependence, or a proper nonempty subset of the first \(n-1\) freely chosen differences sums to zero. Every nonempty proper subset of these \(n-1\) positions with at least two members contributes one distinct hyperplane, excluding singleton zeros. There are \(2^{n-1}-n-1\) such proper subsets with sizes from two through \(n-2\); pairwise intersections have codimension at least two, so inclusion-exclusion yields \((2^{n-1}-n-1)/q+O_n(q^{-2})\) nonminimal fraction. (Singleton-zero hyperplanes and the all-\(n-1\)-positions sum-zero hyperplane are excluded: in both cases the other generically nonzero differences form one minimal circuit on their reduced support.) Subtracting the unique zero word changes the neighbor fraction only by \(O(q^{-(n-1)})\), which is absorbed for \(n\ge4\).

**3. Fourier eigenvalues for rank two.** The graph is a Cayley graph of the additive group of zero-sum words. Characters of \(\mathbb F_2^{2n}\), modulo a common shift of all \(n\) labels, give its entire dual group. For a character labelled by \(a_1,\ldots,a_n\in\mathbb F_2^2\), a pair move on indices \(i,j\) has character sum \(4\mathbf1_{a_i=a_j}-1\) over its three possible nonzero repeated differences. A triple move on indices \(i,j,k\) has character sum \(16\mathbf1_{a_i=a_j=a_k}-4(\mathbf1_{a_i=a_j}+\mathbf1_{a_i=a_k}+\mathbf1_{a_j=a_k})+2\) over the six ordered nonzero distinct differences whose xor is zero. Summing over all pairs and triples yields the stated formula for \(\lambda_n\). The four common label shifts describe each character four times; a histogram with counts \(m_u\) has \(n!/\prod m_u!\) labelled sequences, giving the aggregate multiplicity formula.

**4. Sharp spectral gap.** Let \(A=\sum_{u<v}m_um_v\) count pairs with different labels, and \(R=\sum_{u<v<w}m_um_vm_w\) count triples of three different labels. Expanding the displayed eigenvalue gives the exact identity
\[
\frac{\Delta_n-\lambda_n(m)}4=(n-1)A-2R.
\]
For each such triple, all three cross-label pairs are present; any cross-label pair can be extended to at most \(n-2\) such triples. Therefore \(3R\le(n-2)A\), yielding \((\Delta_n-\lambda_n(m))/4\ge(n+1)A/3\). Let \(M=\max m_u\) and \(r=n-M\). If \(n\ge16\) and \(r\ge4\), then \(n/4\le M\le n-4\), so
\[
A\ge M(n-M)\ge\min\{3n^2/16,4(n-4)\}>3(n-1)^2/(n+1).
\]
Thus all such nonconstant characters have gap strictly greater than \(4(n-1)^2\). If \(r=1\), the exact expression is \((n-1)^2\). If \(r\in\{2,3\}\), split the \(r\) minority labels into three remaining colors. Their cross-pair count \(A_0\le\binom r2\) and their rainbow-triple count \(R_0\le\binom r3\); then
\[
(n-1)A-2R=(n-1)r(n-r)+(2r-n-1)A_0-2R_0.
\]
For \(n\ge16\) both coefficients of the correction are nonpositive, so compared with \((n-1)^2\) this is at least \((n-2)(n-3)>0\) when \(r=2\), and \((2n-7)(n-3)>0\) when \(r=3\). For \(2\le n\le15\), exhaustive integer checking of all \(\binom{n+3}3\) four-color histograms proves the same bound; the precise check is independently reproducible from the accompanying code. For \(n\ge4\), equality occurs exactly at the histogram permutations \((n-1,1,0,0)\), which correspond to \(3n\) distinct characters (one exceptional coordinate and one of three nonzero label differences). At \(n=2,3\), the graph is respectively complete on \(4\) and \(16\) vertices, and so all \(3\) and \(15\) nonconstant modes respectively attain the gap. This finishes the claimed spectrum and spectral gap.

## Verification

The standalone `check_spectrum.py` evaluates the circuit length census by direct exhaustive zero-sum word enumeration for eleven small parameter pairs, checks the resulting graph completeness threshold, verifies every one of the \(4^{n-1}\) character values against a direct Fourier transform for \(n=3,4\), and checks **every** four-color histogram for \(2\le n\le15\). It uses exact Python integers; the infinite-parameter conclusions rest on the proofs above, not on finite testing. Run `python3 check_spectrum.py` from the folder containing the two files. A successful run prints `FULL_CTP_EDGE_AND_FOURIER_EXACT_PASS`.

## Relationship to prior work

The definition, vertices and foundational inequalities of binary cyclic transversal polytopes are due to Frede, Kaibel and Merkert (2024). Frede's 2023 dissertation establishes the general edge-adjacency criterion (Lemma 2.37) and explicitly raises vertex-degree and elementary-circuit enumeration questions (Questions 2.38–2.39). The criterion and the idea of minimal zero-sum sequences are **not** new. The present work specializes that criterion to the full elementary abelian \(2\)-group and derives the complete Euclidean length counts, opposite growth regimes, and the full rank-two Fourier spectrum with exact algebraic connectivity. General graph-code minimal-word results and generic Cayley Fourier principles do not supply these explicit CTP counts or the sharp all-order gap without additional calculation. No assertion of universal historical novelty is made.

## Limitations

This result is for the full, unweighted binary cyclic transversal polytope, not arbitrary cyclic groups, subgroups, projections, or all facets of the polytope. The complete Fourier diagonalization and spectral-gap formula are proved for binary rank exactly two; rank three and above are not spectrally classified here. The first-order dense limit fixes \(n\) while \(q\) grows, whereas the sparse limit fixes \(d\) as \(n\) grows; these statements do not assert a joint limit. Historical priority cannot exclude unindexed or inaccessible equivalent derivations. No independent mathematical audit has been performed.

## References

1. Jonas Frede, *Cyclic Transversal Polytopes*, doctoral dissertation, Martin Luther University Halle–Wittenberg (2023), DOI: `10.25673/110908`, public record https://opendata.uni-halle.de/handle/1981185920/112863 ; especially Lemma 2.37 and Questions 2.38–2.39.
2. Jonas Frede, Volker Kaibel, and Maximilian Merkert, *Binary Cyclic Transversal Polytopes*, arXiv:2404.06088, version 1 (2024-04-09), https://arxiv.org/abs/2404.06088.
3. Standard finite-character Fourier orthogonality and elementary linear dependence over finite fields, used with explicit derivations above.
