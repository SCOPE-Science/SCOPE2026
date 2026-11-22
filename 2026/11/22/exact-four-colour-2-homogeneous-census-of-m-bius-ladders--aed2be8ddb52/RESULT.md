# Exact four-colour 2-homogeneous census of Möbius ladders

## Finding

For every integer \(m\ge3\), let \(M_{2m}\) denote the Möbius ladder on \(2m\) vertices. A proper vertex colouring \(c\) is *2-homogeneous* if each open neighbourhood has exactly two colours: \(|\{c(w):w\in N(v)\}|=2\) for all vertices \(v\). Let \(h_m\) be the number of such colourings using the **named** palette \(\{0,1,2,3\}\), with the vertex positions also labelled and unused colours in principle permitted.

Set \(A(z)\) equal to

\[(1-z)(1+z^2)^3(1-2z-4z^2)(1-z+2z^2)(1+2z+4z^2)^3(1-z^2-2z^3)^3(1-z-3z^2-3z^3+4z^4+8z^5)^2.\]

and set \(B(z)\) equal to

\[(1-2z)(1+z)^2(1-z+z^2+z^3)^3(1+z-z^2+7z^3+2z^4-16z^6)^3.\]

Then the all-order exact enumeration is the formal-series identity

\[\boxed{\sum_{m\ge3}h_mz^m=z\left(\frac{B'(z)}{B(z)}-\frac{A'(z)}{A(z)}\right).}\]

The first eight values, at \(m=3,\ldots,10\), are \(216,48,600,720,5544,8160,59400,98880\). Moreover

\[\boxed{h_m=(1+\sqrt5)^m+O(3^m)\quad(m\to\infty).}\]

The number of 2-homogeneous colourings from three colours is zero at every width \(m\ge3\), so every colouring counted above uses all four colours. The four-colour minimum itself is treated as previously known; the claim concerns its **complete enumerator and growth rate**.

## Assumptions and scope

The graph is finite, simple, cubic and has columns \(v_i=(a_i,b_i)\), \(0\le i<m\). Each column has a vertical rung, consecutive columns are joined in the same row, and the last column is joined **crosswise** to the first. This presentation is isomorphic to the cycle on \(2m\) vertices with antipodal chords. Properness requires unequal colours at every edge. Each three-neighbour colour multiset must have multiplicities \(2,1\), not \(3\) or \(1,1,1\). The palette has four distinct named labels; counts are not quotiented by colour permutations or graph automorphisms. Statements below apply to every integer \(m\ge3\).

## Proof

**1. Local transfer and twisted boundary.** Let \(Q\) be the 12 ordered pairs \((a,b)\) of distinct colours from \(\{0,1,2,3\}\). The set of legal adjacent-column states is

\[\mathcal S=\{(u,v)\in Q^2:u_0\ne v_0,\ u_1\ne v_1\},\qquad |\mathcal S|=84.\]

Define the integer matrix \(T\), indexed by \(\mathcal S\), with \(T_{(u,v),(v',w)}=1\) exactly if \(v=v'\), \(v_0\ne w_0\), \(v_1\ne w_1\), and

\[|\{u_0,v_1,w_0\}|=|\{u_1,v_0,w_1\}|=2.\]

Every other entry is zero. These two cardinality conditions are precisely the two open-neighbourhood conditions at the middle rung. Let \(J\) simultaneously exchange the upper and lower colours in both columns of a state. The Möbius boundary requires a length-\(m\) state walk to finish at the row exchange of its start. Therefore the labelled count is **exactly** \(h_m=\operatorname{tr}(T^mJ)\); the trace does not divide by the rung positions or any symmetry. The row exchange is an involution without fixed states and commutes with \(T\).

**2. An exact finite algebra certificate.** The 84 states form 42 row-exchange pairs. Pick the lexicographically smaller representative \(r\) from each pair and define 42-by-42 matrices \(T_+\) and \(T_-\) by

\[(T_\pm)_{r,s}=T_{r,s}\pm T_{r,Js}.\]

These matrices represent the two eigenspaces of \(J\). Hence

\[h_m=\operatorname{tr}(T_+^m)-\operatorname{tr}(T_-^m).\]

Direct exact **integer** computation from these fully specified matrices, through the Faddeev–LeVerrier recurrence, yields the identities

\[\det(I-zT_+)=A(z),\qquad \det(I-zT_-)=B(z).\]

Both characteristic identities are independently reproducible with the supplied standalone `verify.py` (the degree deficits correspond to zero eigenvalues). For any square matrix \(D\), the formal logarithmic-derivative identity

\[-z\frac{d}{dz}\log\det(I-zD)=\sum_{m\ge1}\operatorname{tr}(D^m)z^m\]

holds. The traces at \(m=1\) and \(m=2\) cancel exactly between these two matrices, so the resulting series starts at \(m=3\) and is precisely the displayed formula. The script checks the full degree-42 integer characteristic coefficients of both matrices, not just initial Taylor coefficients; therefore the rational generating identity holds at **every** width.

**3. Three-colour exclusion and nonempty census.** Apply exactly the same local construction to a three-colour named palette. This produces 18 states. The supplied verifier computes the entire finite directed reachability closure and checks for every source state \(s\) that its row exchange \(Js\) is **unreachable**. Since a legal twisted colouring would be such a directed walk, this finite, exhaustive reachability certificate excludes three-colour solutions at all lengths. The nonemptiness of the four-colour census is independently constructive: starting at the two-column state \(((0,1),(2,3))\), there is a legal two-step return walk and legal three- and four-step walks to the row-exchanged state. Concatenating any number of two-step return walks with one of the latter gives a valid twisted closed colouring for each odd or even \(m\ge3\). These paths are explicitly constructed and checked in `verify.py`.

**4. Sharp asymptotic.** The factor \(1-2z-4z^2\) occurs exactly once in \(A\) and not in \(B\); it corresponds to eigenvalues \(1\pm\sqrt5\). Every other eigenvalue of both transfer blocks has modulus strictly less than \(3\): this follows directly for the linear and quadratic factors; for the cubic factors one applies Rouché's theorem to the reversed monic polynomials on the circle \(|x|=3\); for the degree-five factor \(x^5-x^4-3x^3-3x^2+4x+8\) the sum of the magnitudes of lower terms on that circle is \(209<243=3^5\); and for the degree-six factor \(x^6+x^5-x^4+7x^3+2x^2-16\) it is \(547<729=3^6\). Thus the unique dominant eigenvalue contributes exactly \((1+\sqrt5)^m\) and all remaining terms are \(O(3^m)\).

## Verification

The standalone standard-library Python script `verify.py` rebuilds the 84-state transition, splits its two row-exchange sectors, computes and verifies **every integer characteristic-polynomial coefficient**, verifies the Newton power sums through width 35, independently enumerates proper 2-homogeneous colourings of the graph itself at widths 3, 4 and 5, constructs all-width twisted walks from three basic paths, and performs complete reachability for the 18-state three-colour automaton. Its replay ends in `VERIFY_OK`. The graph-based checks are finite corroboration; unrestricted enumeration follows from the all-coefficient characteristic certificate and transfer proof, and the three-colour impossibility from complete finite-automaton reachability, not bounded sample widths.

## Relationship to prior work

Hao, Liu and Romaniello (first publicly submitted 12 November 2026) prove a four-colour **existence upper bound** for every cubic bipartite graph; this does not count 2-homogeneous four-colourings, and Möbius ladders of odd rung count are nonbipartite. Madaras and Šurimová determine palette feasibility for the **untwisted** prism \(C_m\square K_2\), not a twisted named-colouring census. An earlier result determines that Möbius ladders require four colours for the distinct two-dynamic neighbourhood condition; the minimum four is not new here. A published published-finding corpus record gives the exact four-palette count for **proper conflict-free** colourings on the same Möbius family, but that condition permits three distinct neighbour colours and so counts a strictly larger class than 2-homogeneous colourings; at rung count 4 it gives 336 rather than 48, and at rung count 5 it gives 3600 rather than 600. Thus the presently claimed exact enumeration is neither its formula nor a mere renaming. These comparisons are about mathematical implications and admit the residual risk of an older unindexed enumerator.

## Limitations

Only the four-label 2-homogeneous census on the specified Möbius ladders is counted; no counting statement for larger palettes, all cubic graphs, or graph-automorphism orbits follows. The exact factorizations rest on a reproducible nontrivial finite integer-algebra certificate rather than a short symbolic hand factorization. A relevant older result could remain unidentified outside accessible indexed full texts. Independent mathematical audit has not been performed.

## References

- Rong-Xia Hao, Jianbing Liu, Federico Romaniello, *On 2-Homogeneous Colourings of Cubic Bipartite Graphs*, arXiv:2611.16649v1, first submitted 12 November 2026. https://arxiv.org/abs/2611.16649
- Tomáš Madaras and Mária Šurimová, *Homogeneous colourings of graphs*, published online 28 April 2022; *Mathematica Bohemica* 148 (2023), 105–115. https://doi.org/10.21136/MB.2022.0007-21
- R. C. Laskar and J. Lyle, *Fall colouring of bipartite graphs and cartesian products of graphs*, *Discrete Applied Mathematics* (2009). https://doi.org/10.1016/j.dam.2008.03.003
- *Twisted transfer enumeration of proper conflict-free colorings of Möbius ladders*, published mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-twisted-transfer-enumeration-of-proper-conflict-free-colorings-o--15a66a7edbf3
- *A chirality obstruction for dynamic three-colourings of cubic ladders*, published mathematical record. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-chirality-obstruction-for-dynamic-three-colourings-of-cubic-la--a86238493a14
