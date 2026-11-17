# The pentagonal-prism matching complex: a mixed sphere wedge and its symmetry

## Finding

Let \(G=C_5\square K_2\) be the pentagonal-prism graph, with vertices \((i,a)\) for \(i\in\mathbb Z/5\mathbb Z\), \(a\in\{0,1\}\), horizontal edges \(\{(i,a),(i+1,a)\}\), and vertical edges \(\{(i,0),(i,1)\}\). Let \(X=\mathcal M(G)\) be its **ordinary** matching complex, whose vertices are the fifteen graph edges and whose simplices are sets of pairwise vertex-disjoint graph edges.

Then the integral homotopy type, not merely the rational Betti vector, is
\[
 X\simeq (S^2\vee S^2)\vee(S^3\vee S^3).
\]

The full graph automorphism group is \(D_5\times C_2\). Let \(r(i,a)=(i+1,a)\), \(s(i,a)=(-i,a)\), and \(t(i,a)=(i,1-a)\). Write \(\delta\) for the rational one-dimensional character with \(\delta(r)=1\), \(\delta(s)=-1\), \(\delta(t)=1\), and \(\lambda\) for the character with \(\lambda(r)=\lambda(s)=1\), \(\lambda(t)=-1\). Their products are written multiplicatively. The induced representations satisfy
\[
 \widetilde H_2(X;\mathbb Q)\cong\delta\oplus\lambda,\qquad
 \widetilde H_3(X;\mathbb Q)\cong\mathbf1\oplus\delta\lambda.
\]
In particular, all fivefold rotations act trivially on both nonzero rational homology groups; the dimensions fixed by the entire automorphism group are respectively zero and one.

## Assumptions and scope

All graphs are finite, simple and undirected. The graph \(G\) has ten vertices and fifteen edges; \(C_5\square K_2\) denotes the Cartesian, not categorical, product. A face of \(X\) is any matching, whether or not it extends to a perfect matching. Orient each simplex by increasing edge index according to the explicit ordering in `verify_prism_matching.py`: the five edges of the first pentagon in cyclic order, five of the second, then five vertical edges. The last closing edge in each pentagon is stored as the unordered pair of its endpoints.

The rational character statements refer to the action on reduced homology induced by graph automorphisms, not to a claimed equivariant decomposition of a sphere wedge. The same homotopy statement also describes \(\operatorname{Ind}(L(G))\), the independence complex of the line graph.

## Proof

**1. Exhaustive face structure.** An arbitrary subset \(S\) of the fifteen graph edges is a face precisely when its endpoint bitmasks are pairwise disjoint. The standalone verifier enumerates all \(2^{15}=32768\) subsets independently of an incremental matching generation. Both produce 342 faces including the empty face, with nonempty face vector
\[
 (f_0,f_1,f_2,f_3,f_4)=(15,75,145,95,11).
\]
The resulting ordinary complex has dimension four, even though its homotopy is concentrated in degrees two and three.

**2. Integral discrete-Morse vector fields.** Let the face poset exclude the empty face. Process graph-edge indices in increasing order. At index \(i\), pair every still-unmatched face \(\sigma\) not containing \(i\) with \(\sigma\cup\{i\}\), provided the larger face is also still unmatched. This yields 168 pairs, exactly one critical vertex (edge mask 1), two critical triangles (masks 8258 and 11264), and two critical tetrahedra (masks 660 and 12816). There are no other critical cells. Every one of the 1020 nonempty-face Hasse incidences is oriented upward except for the matched ones, which are reversed. A complete topological-order check verifies that this directed incidence graph has no cycle. Reversing the index processing order gives an independent 168-pair acyclic matching with the same critical-cell dimensions.

**3. Signed integer attaching degrees.** For an oriented face \(\sigma\), use the integral simplicial boundary \(\partial\sigma=\sum_j(-1)^j(\sigma\setminus\{e_j\})\). If \(u\prec v\) is a matched incidence with coefficient \(\epsilon=\pm1\), replace each occurrence of \(u\) in a chain by \(u-\epsilon^{-1}\partial v\). As there are no closed gradient paths, this process terminates. Reducing the boundaries of both critical tetrahedra by this exact operation yields zero in the two-dimensional critical basis, independently for each of the two different matchings. Therefore the integer Morse differential from degree three to degree two is the zero \(2\times2\) matrix. This is an integral result, not a conclusion drawn from field homology.

The Morse CW model has one zero-cell, no one-cells, two two-cells and two three-cells. The two-cells attach to the point and produce \(S^2\vee S^2\). Attaching maps of the three-cells are classified by their integral degree vectors because \(\pi_2(S^2\vee S^2)\cong\mathbb Z^2\). Both vectors are zero, so both attaching maps are nullhomotopic, proving the displayed wedge equivalence.

**4. Symmetry module.** Let \(V\) send a matched lower face \(u\) to \(-\epsilon^{-1}v\), where \(u\prec v\), and send all other faces to zero. The integral chain flow \(\Phi=1+\partial V+V\partial\) stabilizes because the matching is acyclic. Stabilizing each critical simplex produces an integral cycle with exactly its own coefficient one among the critical cells; stabilizing the signed image under an automorphism and reading its critical coefficients yields the corresponding integral homology matrix.

In bases ordered by the critical masks above, exact calculation gives \(r_* =I_2\) in both homological degrees and
\[
 \begin{array}{c|cc}
 &s_*&t_*\\ \hline
 \widetilde H_2&\begin{pmatrix}1&1\\0&-1\end{pmatrix}&\begin{pmatrix}-1&-1\\0&1\end{pmatrix}\\
 \widetilde H_3&\begin{pmatrix}1&-1\\0&-1\end{pmatrix}&\begin{pmatrix}1&-1\\0&-1\end{pmatrix}
 \end{array}
\]
These commuting involutions diagonalize over \(\mathbb Q\), giving \(\delta\oplus\lambda\) in degree two and \(\mathbf1\oplus\delta\lambda\) in degree three. The reverse-order Morse model independently reproduces the three generating character traces in each degree. Signed simplicial Lefschetz traces supply a further consistency check. The only pentagonal cycles are the two horizontal rim cycles: any odd closed walk has at least five horizontal steps, and a length-five cycle cannot contain two vertical steps. Hence every automorphism permutes the two rims, acts dihedrally on each, and must use the same rim permutation on both because the five vertical edges form a matching. Thus the full automorphism group is exactly \(D_5\times C_2\), of order twenty, generated by \(r,s,t\).

## Verification

Run `python3 verify_prism_matching.py` in the same folder. The script has no external Python dependencies. It independently enumerates faces twice, checks every Hasse incidence and the acyclicity of both Morse fields, computes the two zero integral Morse boundary matrices, checks that the stabilized critical generators are genuine integral cycles, computes the symmetry matrices, validates traces using a second Morse field, and independently obtains mod-two simplicial boundary ranks \((14,61,82,11)\). It also records that the perfect-matching subcomplex has eleven facets and 241 nonempty faces, while exactly 100 nonempty ordinary faces are not perfect-extendible. The matching's absence of torsion follows from the integral Morse differential, not merely mod-two ranks. `verification_output.txt` contains the output of an actual execution of this standalone script.

## Relationship to prior work

Gupta, Sarkar, Sawant and Shukla (arXiv:2403.15298, first public March 22, 2024) compute topological information for matching complexes of **categorical products of paths** and distinguish those products from Cartesian graph products. Their theorems neither concern cycles nor apply to \(C_5\square K_2\). Bayer, Jelić Milutinović and Vega (arXiv:2209.02803, first public September 6, 2022) study **perfect matching** subcomplexes of honeycomb graphs, also distinct from the ordinary complex considered here.

Agarwal and Basak (arXiv:2608.30601v2, September 14, 2026) study independence and perfect matching complexes of Möbius and circular ladders. Their Main Theorem 2 makes the **perfect matching complex** of the five-sided circular ladder contractible; it does not determine the ordinary matching complex. In fact, Problem 26 explicitly identifies the ordinary matching complexes of circular ladders as a direction for investigation. Their result is not implied by the present one, and the present result is not a restatement of their perfect-matching theorem. Nearby finite calculations of ordinary matching complexes for Möbius ladders concern nonisomorphic graphs: the ten-vertex Möbius ladder is bipartite, whereas the pentagonal prism has pentagonal cycles. Nor do published computations for total cut, Vietoris–Rips, or ordinary neighborhood complexes of circular ladders determine its ordinary matching complex.

## Limitations

Only the five-sided circular ladder is classified; no homotopy-type periodicity or formula for all circular ladders is claimed. The decompositions of rational symmetry modules do not assert the direct-sum splitting of integral representations or equivariant sphere-wedge splittings. This is an exact finite result with a complete executable Morse certificate, but the absence of a discovery in searched literature is not an absolute proof of priority. An equivalent result in unindexed literature remains possible, especially under the line-graph independence-complex formulation. Independent external validation has not been performed.

## References

1. R. K. Gupta, S. Sarkar, S. S. Sawant and S. Shukla, *On the matching complexes of categorical product of path graphs*, arXiv:2403.15298 (first version March 22, 2024), https://arxiv.org/abs/2403.15298.
2. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803 (first version September 6, 2022), https://arxiv.org/abs/2209.02803.
3. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2 (September 14, 2026), https://arxiv.org/abs/2608.30601.
