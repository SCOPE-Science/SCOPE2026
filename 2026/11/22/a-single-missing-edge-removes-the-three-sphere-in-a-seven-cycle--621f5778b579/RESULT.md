# A single missing edge removes the three-sphere in a seven-cycle categorical-product independence complex

## Finding
Let \(G=C_7\times K_3\) be the categorical graph product, and let \(e\) be **any** of its 42 edges. Set \(X=\operatorname{Ind}(G)\) and \(Y=\operatorname{Ind}(G-e)\), with the ordinary independence complex of a graph consisting of all its independent vertex sets. Then
\[
X\simeq S^3\vee\bigvee^3 S^4,
\qquad Y\simeq\bigvee^3 S^4.
\]
The inclusion \(i:X\hookrightarrow Y\) induces an isomorphism \(\widetilde H_4(X;\mathbb Z)\xrightarrow{\sim}\widetilde H_4(Y;\mathbb Z)\), and the map on \(\widetilde H_3\) kills the unique free generator. More precisely, there are homotopy identifications of source and target under which \(i\) is the standard map collapsing the \(S^3\) wedge summand and retaining all three \(S^4\) summands. Its homotopy cofiber is \(S^4\), and the integral cofiber connecting homomorphism \(\widetilde H_4(Y/X;\mathbb Z)\to\widetilde H_3(X;\mathbb Z)\) has degree \(\pm1\).

## Assumptions and scope
The 21 vertices of \(G\) are \((r,c)\) where \(r\in\mathbb Z/7\mathbb Z\) and \(c\in\{0,1,2\}\), with adjacency exactly when \(r-s\equiv\pm1\pmod7\) and the colors differ. Vertex \((r,c)\) is encoded by the integer \(3r+c\); a simplex is encoded by a 21-bit subset mask. All homotopy types and homology groups are integral unless stated otherwise. A deletion means deleting one graph edge while keeping all vertices and every other edge. The conclusion is for a single missing edge, not for multiple deletions or different cycle lengths.

## Proof
**1. The exhaustive complexes and the edge link.** Fix \(u=(0,0)\) and \(v=(1,1)\), and put \(e=\{u,v\}\). The complete independence-face enumeration contains 5,282 faces, including the empty face, before deletion and 5,647 afterward. Define \(L=\operatorname{Ind}(G-N_G[u]-N_G[v])\). It has 365 faces including the empty one, on the 13 remaining vertices with indices \(1,3,7,9,10,11,12,13,14,15,16,17,18\). Every newly allowed independent face is uniquely \(\{u,v\}\cup\sigma\), for \(\sigma\in L\); the standalone checker verifies this identity over the entire face sets. Therefore the edge-deletion cofibration is realized by the simplicial pushout
\[
Y=X\cup_{\partial\Delta^1*L}(\Delta^1*L),
\qquad Y/X\simeq\Sigma^2|L|.
\]
The second equivalence uses the ordinary unreduced double suspension; the nonempty link here is connected.

**2. Three complete acyclic discrete-Morse matchings.** For any face family \(F\), start with all nonempty faces unmatched. Given an ordered list of 21 vertex indices, process the indices in order. At index \(j\), take every still-unmatched lower face \(\sigma\) not containing \(j\) whose coface \(\sigma\cup\{j\}\) is also still unmatched; pair them and remove both from further consideration. A face may be used in at most one pair, and each pair is a codimension-one face relation. The lists, in order, are:

- \(X\): `3,10,4,0,19,15,18,13,8,9,14,12,17,5,2,16,7,6,11,1,20`.
- \(Y\): `3,13,4,0,20,10,17,15,5,7,9,8,11,12,14,1,18,6,16,2,19`.
- \(L\): `16,10,6,8,13,11,4,1,15,2,18,0,9,19,20,12,17,7,5,3,14`.

The complete matching outputs are respectively 2,638, 2,821 and 181 pairs, leaving one critical vertex plus, respectively, one critical 3-face and three critical 4-faces; three critical 4-faces; and one critical 2-face. For each family, direct every nonmatched face-cover incidence from coface to face and reverse the direction of each matched incidence. The executable constructs the **entire** directed Hasse graph and exhaustively topologically sorts it, obtaining 5,281, 5,646 and 364 visited nonempty faces, exactly the complete cardinalities. This finite check proves acyclicity, not merely the absence of short cycles. Discrete Morse theory supplies CW models with exactly the stated critical-cell dimensions.

**3. The integral attaching degrees.** Orient simplices by increasing encoded vertex index. In the matching on \(X\), denote the critical three-face by \(c\). Define the integral Morse projection \(P_3\) on any oriented three-face \(\sigma\): it is \(1\) for \(\sigma=c\), \(0\) for an upper-matched three-face, and when \(\sigma\) is lower-matched to a four-face \(\tau\), recursively set
\[
P_3(\sigma)=-[\tau:\sigma]^{-1}\sum_{\rho\subset\tau,\,\dim\rho=3,\,\rho\ne\sigma}[\tau:\rho]P_3(\rho).
\]
Here every bracket is the signed incidence \(\pm1\). The gradient acyclicity makes this a finite recursion. For the three critical four-faces, whose decimal bitmasks are `590402`, `1180036` and `1180228`, the directly recomputed integer coefficients \(P_3(\partial\tau)\) are exactly `0,0,0`. Thus the Morse differential from degree four to three vanishes over \(\mathbb Z\). The three-skeleton of the CW model for \(X\) is \(S^3\), where the attaching homotopy class of a four-cell is its integer degree in \(\pi_3(S^3)\cong\mathbb Z\). All attaching maps are therefore null-homotopic, proving \(X\simeq S^3\vee\bigvee^3S^4\). The model for \(Y\) has only one vertex and three four-cells, and that for \(L\) only one vertex and one two-cell; hence \(Y\simeq\bigvee^3S^4\) and \(|L|\simeq S^2\), without additional attaching-degree computations.

**4. Exact integral inclusion.** By step 1, \(Y/X\simeq\Sigma^2 S^2\simeq S^4\). The reduced integral long exact sequence contains
\[
0\longrightarrow\mathbb Z^3\xrightarrow{i_*}\mathbb Z^3\longrightarrow\mathbb Z\xrightarrow{\partial}\mathbb Z\longrightarrow0.
\]
The last map \(\partial\) is surjective and therefore multiplication by \(\pm1\). Exactness forces \(i_*\) to be an isomorphism, and it kills the degree-three class because \(\widetilde H_3(Y)=0\). All maps \(S^3\to\bigvee^3S^4\) are null, whereas homotopy classes of maps \(S^4\to\bigvee^3S^4\) are detected by \(H_4\) through the Hurewicz theorem. Choosing the induced integral basis identifies \(i\) with the standard wedge map in the statement.

**5. Every edge.** The dihedral symmetries of \(C_7\) and the color permutations of \(K_3\) act by graph automorphisms and transitively on its 42 edges. The verifier enumerates their orbit on \(e\) and checks that it is the complete graph-edge set. Thus the argument applies to every single edge.

## Verification
Run `python3 verify.py` using standard-library Python 3; no downloads, external packages or previous computational files are required. It rebuilds both 21-vertex graphs, enumerates their independent faces twice (once by recursive face extension and once by checking all \(2^{21}\) Boolean masks), constructs the 365-face edge link, verifies the exact relative-face identity, tests every Morse pair and every directed Hasse cover for acyclicity, recomputes the signed integral critical differential, and exhausts the complete 42-edge symmetry orbit. The checker prints `C7_K3_SINGLE_EDGE_FAULT_CERTIFICATE_OK` only after its assertions pass. `verification_output.txt` contains the reproduced output. These are exhaustive finite calculations for this fixed graph; their interpretation via discrete Morse theory, the cofibration and the long exact sequence are the mathematical proof, not an extrapolation.

## Relationship to prior work
Antolín Camarena and Carnero Bravo (first public arXiv posting 2023-07-23) analyze independence complexes of categorical products \(C_k\times K_n\). Their Theorem 23 constrains the homology for seven-cycles, and their auxiliary-graph construction includes the edge-neighborhood deletion graph. They do **not** establish the present homotopy type of \(\operatorname{Ind}(C_7\times K_3-e)\) or its inclusion map. Adamaszek's 2011 edge-deletion cofibration already explains the general relationship \(Y/X\simeq\Sigma^2 L\); it alone does not identify the attaching degree or the faulted homotopy type.

A published exact integral homotopy classification for \(\operatorname{Ind}(C_7\times K_n)\), and a published three-color equivariant refinement, establish the **intact** \(S^3\vee3S^4\) baseline for \(n=3\). That baseline is not claimed as new. Their inspected complete result statements and proofs contain no one-edge-deletion classification or primitive connecting degree. The distinctive contribution here is the exact relative homotopy response and the proof that deletion removes the sole three-sphere without losing a four-sphere.

## Limitations
No assertion is made about two or more deleted edges, other cycle lengths, a functorial equivariant splitting, or optimality of any stability threshold. This is an exact finite-graph computation with a reproducible acyclic-Morse certificate; it is not a parameter-uniform theorem. Targeted source inspection cannot rule out independently obtained unindexed or otherwise inaccessible equivalent results. Independent scientific validation remains outstanding.

## References
1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401, initial public posting 2023-07-23, especially Section 3, Theorem 23, and Question 24. https://arxiv.org/abs/2307.12401
2. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250, initial public posting 2011-06-30, especially the edge-deletion cofibration. https://arxiv.org/abs/1106.6250
3. *Uniform integral sphere wedges for seven-cycle categorical products*, mathematical result published in 2026, full result and proof available in the public published-finding corpus research collection. https://github.com/published-finding corpus/2026
4. *Integral homotopy and joint dihedral–color homology of the seven-cycle categorical product*, mathematical result published in 2026, full result and proof available in the public published-finding corpus research collection. https://github.com/published-finding corpus/2026
