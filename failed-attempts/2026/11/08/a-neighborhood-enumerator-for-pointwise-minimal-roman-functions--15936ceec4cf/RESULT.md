# A neighborhood enumerator for pointwise-minimal Roman functions on one-leaf coronas

## Finding
Let \(H\) be any finite simple graph on \(n\ge1\) vertices, and let \(C(H)=H\circ K_1\) attach one private leaf \(v'\) to every vertex \(v\) of \(H\). A Roman dominating function on \(C(H)\) is a labeling \(f:V(C(H))\to\{0,1,2\}\) such that each vertex labeled \(0\) has a neighbor labeled \(2\). It is **pointwise-minimal** if decreasing any positive label, even together with other decreases, cannot preserve Roman domination. Define
\[
M_H(z)=\sum_{f\text{ pointwise-minimal on }C(H)}z^{\sum_w f(w)}.
\]
For \(X\subseteq V(H)\), put \(u_H(X)=|V(H)\setminus N_H[X]|\), where \(N_H[X]\) denotes the union of the closed neighborhoods of vertices of \(X\) and \(N_H[\varnothing]=\varnothing\). Then
\[
\boxed{M_H(z)=\sum_{X\subseteq V(H)}2^{u_H(X)}z^{n+|X|+u_H(X)}.}
\]
Equivalently, if \(b_H(X)=|N_H(X)\setminus X|\) denotes the external neighborhood size, then
\[
M_H(z)=\sum_{X\subseteq V(H)}2^{n-|N_H[X]|}z^{2n-b_H(X)}.
\]
The formula is an exact count of all pointwise-minimal functions by **every** weight, not just an optimization formula.

There is a structural bijection with independent sets of the bipartite graph \(B_H\) whose vertices are \(L_v,R_v\) for \(v\in V(H)\) and whose edges are \(L_vR_w\) whenever \(v=w\) or \(vw\in E(H)\). In particular,
\[
M_H(1)=|\{I\subseteq V(B_H): I\text{ is independent}\}|.
\]
Two extremal consequences are
\[
\min\{k:[z^k]M_H(z)>0\}=n+\gamma(H),
\]
where \(\gamma(H)\) is the ordinary domination number, and
\[
[z^{2n}]M_H(z)=\prod_{Q\text{ component of }H}(2^{|V(Q)|}+1).
\]
Thus for connected \(H\), the largest weight is \(2n\), attained by precisely \(2^n+1\) pointwise-minimal functions.

A closed two-parameter specialization is obtained for complete bipartite bases \(H=K_{a,b}\), \(a,b\ge1\), with \(n=a+b\):
\[
\begin{aligned}
M_{K_{a,b}}(z)={}&2^nz^{2n}+(3^a-2^a)z^{2a+b}
+(3^b-2^b)z^{a+2b}\\
&+z^n\big((1+z)^a-1\big)\big((1+z)^b-1\big).
\end{aligned}
\]
Coefficients at coinciding powers must be added. For example, \(M_{K_{1,1}}(z)=2z^3+5z^4\), the minimal-Roman enumerator of the four-vertex path.

## Assumptions and scope
All graphs here are finite, undirected, and simple. The base \(H\) need not be connected and may contain isolated vertices. The corona has exactly \(2n\) vertices, one original and one private leaf per base vertex. In the pointwise order, \(g\le f\) means \(g(w)\le f(w)\) for every vertex. "Minimal" refers only to this order; it is not the alternative weight-maximizing notion of Roman irredundance. The formula counts labeled functions on a fixed graph, so there is no automorphism quotient.

## Proof
Roman feasibility is monotone in the pointwise order: increasing a label cannot turn a valid Roman function into an invalid one. Hence a valid function is pointwise-minimal if and only if decreasing each individual positive label by one destroys validity. We classify the pair \((f(v),f(v'))\) for every base vertex \(v\).

First, if \(f(v)=2\), its leaf must be \(0\). A leaf labeled \(1\) could decrease to \(0\) because \(v\) defends it, and a leaf labeled \(2\) could decrease to \(1\) because that leaf has no \(0\)-neighbor depending on its \(2\). Conversely, \((2,0)\) is locally minimal because decreasing the base label deprives its private leaf of its sole \(2\)-neighbor.

Second, if \(f(v)=1\), the leaf must also be \(1\): leaf \(0\) would be undefended, while leaf \(2\) would make the base's \(1\) reducible. Such a \((1,1)\) pair is minimal exactly when \(v\) has no base neighbor labeled \(2\); otherwise the base's \(1\) is reducible to \(0\).

Third, if \(f(v)=0\), its leaf cannot be \(0\). The pair \((0,1)\) is Roman-feasible precisely when some base neighbor is labeled \(2\). Then the leaf's \(1\) cannot decrease because its unique neighbor has label \(0\). The pair \((0,2)\) is Roman-feasible, but it is minimal precisely when no base neighbor is labeled \(2\): the leaf's \(2\) is then the only defender of \(v\), whereas any base \(2\)-neighbor would make that leaf's label reducible.

Let \(X\) be the set of base vertices with label \(2\). The preceding cases force exactly the following assignments:

- For \(v\in X\), the pair is \((2,0)\).
- For \(v\in N_H(X)\setminus X\), the pair is \((0,1)\).
- For each \(v\notin N_H[X]\), the pair is either \((0,2)\) or \((1,1)\), independently.

Every assignment produced in this way is Roman-feasible and pointwise-minimal: every label \(2\) has a private dependent \(0\) in its own pair, every label \(1\) lacks a \(2\)-neighbor, and every \(0\) is defended. Conversely, the preceding forced-pair analysis exhausts all minimal functions. Thus for fixed \(X\) there are exactly \(2^{u_H(X)}\) functions, each having weight
\[
2|X|+|N_H(X)\setminus X|+2u_H(X)
=n+|X|+u_H(X).
\]
Summing over \(X\) proves the polynomial.

To prove the independent-set correspondence, record the chosen base-\(2\) set \(X\) as selected left-copy vertices \(\{L_v:v\in X\}\) of \(B_H\). Among the \(u_H(X)\) unexposed base vertices, record one of the two pair choices by selecting the corresponding right-copy vertex \(R_v\). The right choices form any subset \(Y\subseteq V(H)\setminus N_H[X]\), which is equivalent to saying no left vertex in \(X\) is adjacent to a right vertex in \(Y\) in \(B_H\). This construction is invertible.

For the minimum exponent, \(X\cup(V(H)\setminus N_H[X])\) is a dominating set of \(H\), so \(|X|+u_H(X)\ge\gamma(H)\). Choosing \(X\) to be a minimum dominating set gives equality, proving the minimum weight \(n+\gamma(H)\). The exponent cannot exceed \(2n\), since the external neighborhood size is nonnegative. Equality holds precisely when \(N_H(X)\setminus X=\varnothing\), that is, \(X\) is a union of whole connected components of \(H\). For a component \(Q\), either \(Q\subseteq X\), contributing one labeling, or \(Q\cap X=\varnothing\), contributing \(2^{|V(Q)|}\) labelings. Multiplying proves the leading-coefficient formula.

For \(H=K_{a,b}\), partition the core-\(2\) sets \(X\) into four mutually exclusive cases: \(X=\varnothing\); nonempty \(X\) contained in the first part; nonempty \(X\) contained in the second part; and \(X\) meeting both parts. These contribute respectively \(2^nz^{2n}\), \((3^a-2^a)z^{2a+b}\), \((3^b-2^b)z^{a+2b}\), and \(z^n((1+z)^a-1)((1+z)^b-1)\). This proves the specialization.

## Verification
The included executable `verify_roman_corona.py` independently checks the defining Roman condition and tests minimality through every possible single-step positive-label decrease. Every labeled graph on one through four vertices and eleven further five-vertex bases is examined. Altogether it checks 86 graphs and 1,075,446 candidate functions, of which 4,370 are pointwise-minimal. All full polynomials agree. Separate tests check the minimum and highest-weight coefficients, the independent-set correspondence for every base of order at most four, and the complete-bipartite specialization for all \(1\le a,b\le4\). The observed output is

`VERIFY_OK graphs=86 labelings=1075446 minimal_functions=4370 full_polynomials=PASS extremal_weights=PASS independent_set_bridge=PASS bicliques=16`

This finite exhaustion is corroboration only; the preceding argument proves the formulas for every finite base graph.

## Relationship to prior work
Abu-Khzam, Fernau, and Mann (2022) establish general structural criteria for pointwise-minimal Roman dominating functions and a polynomial-delay enumeration algorithm. Their general characterization gives important background but neither states the above corona-specific local-state bijection nor its exact weight polynomial, auxiliary independent-set identity, and leading-coefficient product. Their subsequent Roman Census study (2022 preprint; MFCS 2023) derives counting recurrences for paths and input-sensitive bounds for broader graph classes; it does not give this unrestricted one-leaf-corona weight enumerator. Earlier work of Siva Parvathi and Maheswari (2013) constructs specific minimal Roman functions on cycle–clique coronas, including a one-leaf specialization. Their January 2014 paper likewise exhibits a particular minimal Roman function on coronas of paths with stars. Neither supplies all-function classifications or weight enumerators for arbitrary one-leaf coronas. The domination-number consequence is a natural baseline and is not independently claimed as a novel minimum-parameter discovery.

## Limitations
The formula sums over all core subsets, so it is not claimed to be polynomial-time evaluable for arbitrary base graphs. It does not assert that any general counting problem becomes easy, nor establish a new complexity-theoretic classification. It counts **pointwise-minimal** rather than minimum-weight Roman dominating functions alone; these are different notions. Publication priority is provisional: a 2013 thesis broadly concerned with domination functions of corona graphs was identified bibliographically but its complete contents were not established. No independent mathematical audit has been performed.

## References
1. F. N. Abu-Khzam, H. Fernau, K. Mann, *Minimal Roman Dominating Functions: Extensions and Enumeration*, arXiv:2204.04765 (first posted 2022-04-10); *Algorithmica* 86 (2024), 1862–1887. https://arxiv.org/abs/2204.04765 ; https://doi.org/10.1007/s00453-024-01211-w
2. F. N. Abu-Khzam, H. Fernau, K. Mann, *Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes*, arXiv:2208.05261 (first posted 2022-08-10); MFCS 2023, LIPIcs 272, article 6. https://arxiv.org/abs/2208.05261 ; https://doi.org/10.4230/LIPIcs.MFCS.2023.6
3. M. Siva Parvathi and B. Maheswari, *Some Variations of Y-Dominating Functions of Corona Product Graph of a Cycle with a Complete Graph*, *International Journal of Computer Applications* 81(1) (November 2013), 16–21. https://research.ijcaonline.org/volume81/number1/pxc3891966.pdf
4. M. Siva Parvathi, *Some Studies on Dominating Functions of Corona Product Graphs*, PhD thesis, Sri Padmavati Mahila Visvavidyalayam (cited in 2013–2014 papers; complete thesis not inspected).
5. M. Siva Parvathi and B. Maheswari, *Roman Dominating and Total Dominating Functions of Corona Product Graph of a Path with a Star*, *International Journal of Computer Engineering and Technology* 5(1) (January 2014), 21–27. https://iaeme.com/MasterAdmin/Journal_uploads/IJCET/VOLUME_5_ISSUE_1/IJCET_05_01_003.pdf
