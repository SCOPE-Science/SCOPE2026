# An explicit order-two class in the three-particle homology of Tietze’s graph

## Finding
Let \(T\) be Tietze’s graph, the twelve-vertex cubic graph obtained by replacing one Petersen-graph vertex with a triangle. Let \(B_3(T)\) be the unordered configuration space of three distinct points on its geometric realization. The integral group \(H_2(B_3(T);\mathbb Z)\) contains a nonzero class of exact order two. In addition, \(H_3(B_3(T);\mathbb Z)=0\).

This is an **existence statement**, not a complete calculation of \(H_2\): it neither asserts that its torsion subgroup is cyclic nor excludes torsion of other orders.

## Assumptions and scope
The graph is the finite simple graph on vertices \(\{0,1,\ldots,11\}\), with its eighteen edges given in the fixed lexicographic sequence in `verify_tietze_torsion.py`. It is obtained from the ordinary Petersen graph by replacing vertex zero with the triangle \(\{0,10,11\}\) and assigning the three former neighbors to those three vertices in ascending order. Graph vertices refer to a fixed cell structure; configuration points are allowed anywhere along the geometric edges. Particles are unordered and collisions are forbidden.

The relevant chain model is the **reduced Świątkowski complex** of this graph with **weight three** and integral coefficients, rather than the unsubdivided Abrams discretization of vertex configurations. The reduced complex computes the homology of the actual continuous configuration space by the comparison and quasi-isomorphism theorems [2]. No subdivision hypothesis on this particular graph is needed to apply that chain model.

## Proof
Fix the listed ordering of the graph edges and, at each vertex \(v\), let \(e_{v,0}<e_{v,1}<e_{v,2}\) be its three incident edges. Write \(a_{v,1}=h_{v,1}-h_{v,0}\) and \(a_{v,2}=h_{v,2}-h_{v,0}\), where \(h_{v,i}\) denotes the half-edge at \(v\) corresponding to \(e_{v,i}\). These generators have homological degree one and weight one. Edge-polynomial variables have homological degree zero and weight one; the empty local generator has degree and weight zero. The differential obeys
\[
\partial a_{v,j}=e_{v,j}-e_{v,0},\qquad
\partial(e_i)=0.
\]
Use the Koszul sign rule when differentiating an ordered product of degree-one generators. This is precisely the reduced Świątkowski chain model for this cubic graph [2, Definition 4.7 and Proposition 4.9].

For weight three, a degree-three basis consists of choosing three distinct graph vertices, each equipped with one of its two half-edge-difference generators, so it has \(\binom{12}{3}2^3=1760\) elements. A degree-two basis chooses two distinct vertices with their half-edge differences and one arbitrary edge-polynomial factor, giving \(\binom{12}{2}2^2\cdot18=4752\) elements. The degree-one basis has \(12\cdot2\binom{19}{2}=4104\) elements, with repeated polynomial edge factors allowed.

Write \(D_3\) for the integer matrix of the weight-three differential from degree three to degree two, and \(D_2\) for its next differential. The attached `tietze_certificate.json` specifies by their canonical zero-based column indices the support of an integral degree-three chain \(c\) with exactly \(224\) coefficients all equal to one. The canonical basis order is specified by the standalone program: lexicographic vertex subsets, then lexicographic choices of half-edge differences, then lexicographic polynomial multisets.

The exact checks in the package establish all of the following:
\[
\begin{gathered}
\operatorname{rank}_{\mathbf F_2}(D_3)=1759,\\
\operatorname{rank}_{\mathbf F_3}(D_3)=1760,\\
D_3c=2w,\quad w\in C_2(\mathbb Z),\quad |\operatorname{supp}(w)|=360,\\
D_2w=0,\qquad D_2D_3=0.
\end{gathered}
\]
Every nonzero coefficient of \(w\) is \(1\) or \(-1\). The complete row coefficients of \(w\) and all \(224\) indices of \(c\) are in the attached certificate; the program independently reconstructs both from the graph itself. It also finds full top-differential rank modulo \(5\) and \(101\).

Because the reduction of \(D_3\) modulo three has full column rank, \(D_3\) is injective over \(\mathbb Q\) and hence over \(\mathbb Z\). Since \(D_3c=2w\), the class \([w]\) has order dividing two. If it vanished, some integral degree-three chain \(z\) would satisfy \(D_3z=w\). Consequently \(D_3(c-2z)=0\), forcing \(c=2z\) by injectivity, impossible because \(c\) has odd coefficients. Thus \([w]\ne0\) and has **exact order two**. Injectivity also yields \(H_3(B_3(T);\mathbb Z)=0\), since this weight-three complex has no degree-four chains. The chain-model comparison transfers both conclusions to the actual continuous configuration space [2].

## Verification
Run `python3 verify_tietze_torsion.py` from a directory containing that standalone program. The script uses only the Python standard library and regenerates `tietze_certificate.json`. It constructs all integer columns of \(D_3\) and \(D_2\), computes a one-dimensional kernel modulo two, checks that its \(224\)-term lift has an even boundary, checks \(D_2w=0\), and verifies \(D_2D_3=0\) on all \(1760\) degree-three generators. Exact sparse Gaussian elimination proves that \(D_3\) has full column rank separately modulo \(3\), \(5\), and \(101\).

The package's `verification_output.txt` is the recorded output of the script, and the attached JSON certificate is the complete explicit chain witness. The argument about non-boundaries requires no Smith-normal-form extrapolation: full column rank modulo three already proves the needed integral injectivity.

## Relationship to prior work
Tietze introduced the underlying graph in 1910 [1]. Ko and Park gave a landmark general formula for **first** homology of graph braid groups [3], whose first public arXiv version dates to 2011-01-13; that first-homology result alone does not imply the present **second-degree** torsion statement. The Świątkowski comparison and reduced model from An, Drummond-Cole and Knudsen [2] is the computational framework, not a previously published value for the Tietze graph.

An and Knudsen's second-homology generator theorem assumes a *planar* graph [4]; Tietze's graph is nonplanar because contracting its distinguished triangle gives the nonplanar Petersen graph. Their specific nonplanar example concerns a different graph. Maciążek and Sawicki's inspected computations concern other graph families and particle numbers [5]. The later general torsion theorem for complete bipartite graphs [6] gives broad context but, according to its accessible abstract, specializes to \(K_{a,b}\) families, not this graph. A final literature and mathematical-record search did not identify a statement determining this cycle or implying its existence in this graph.

## Limitations
The result does not compute the complete integral group \(H_2\), classify its free summands, or exclude odd-order torsion. Its finite chain certificate is exhaustive for the specified boundary matrices, but it does not assert a classification for all graphs or all numbers of particles. Independently checking the comparison theorem is outside the computational certificate, and equivalent unindexed or inaccessible literature may still exist. A recent broader article [6] was available in abstract but its full text could not be inspected in this run; that publication-priority risk remains explicit.

## References
[1] Heinrich Tietze, “Einige Bemerkungen zum Problem des Kartenfärbens auf einseitigen Flächen,” *Jahresbericht der Deutschen Mathematiker-Vereinigung* **19** (1910), 155–159. The original publication year is known, but no specific original day or month is assumed.

[2] Byung Hee An, Gabriel C. Drummond-Cole, Ben Knudsen, “Subdivisional spaces and graph braid groups,” *Documenta Mathematica* **24** (2019), 1513–1583, especially Theorem 4.5, Definition 4.7, Proposition 4.9. arXiv:1708.02351; https://arxiv.org/abs/1708.02351.

[3] Ki Hyoung Ko, Hyo Won Park, “Characteristics of graph braid groups,” arXiv:1101.2648v1, publicly posted 2011-01-13, especially Theorem 3.16. https://arxiv.org/abs/1101.2648.

[4] Byung Hee An, Ben Knudsen, “On the second homology of planar graph braid groups,” arXiv:2008.10371, especially Theorem 1.1 and Example 6.8. https://arxiv.org/abs/2008.10371.

[5] Tomasz Maciążek, Adam Sawicki, “Non-abelian Quantum Statistics on Graphs,” *Communications in Mathematical Physics* **371** (2019), 921–973; arXiv:1806.02846. https://arxiv.org/abs/1806.02846.

[6] Byung Hee An, “Torsion of every finite order in the homology of graph braid groups,” arXiv:2610.04305, publicly posted 2026-10-03, abstract inspected; full text not obtained. https://arxiv.org/abs/2610.04305.
