# Sharp four-extension recovery of eight-point Frobenius splitting from Aronhold heptads

## Finding
Let \(C/\mathbb F_q\) be any smooth genus-three hyperelliptic curve in odd characteristic, and let \(\mathcal A_C\) be its finite étale scheme of unordered Aronhold heptads of odd theta characteristics. There are exactly \(288\) geometric heptads. Write \(H_n=\#\mathcal A_C(\mathbb F_{q^n})\).

**Theorem.** The four integers \((H_1,H_2,H_3,H_4)\) uniquely determine the complete Frobenius cycle partition of the eight geometric Weierstrass points of \(C\). The bound four is optimal over **every** odd finite field: there are smooth genus-three hyperelliptic curves with Weierstrass cycle types \((8)\) and \((4,4)\), both having \((H_1,H_2,H_3)=(0,0,0)\), while their fourth counts are respectively \(0\) and \(288\). Their heptad zeta functions are consequently different.

More precisely, if \(f_n,t_n,u_n\) respectively count the cycles of lengths \(1,2,3\) of the \(n\)-th Frobenius power on the branch-point set, then
\[
H_n=f_n+4\binom{f_n}{4}+f_n(f_n-1)t_n+f_nu_n\qquad(n\geq1).
\]
The \(22\) possible eight-point branch cycle partitions give \(22\) different heptad zeta functions; their first \(1,2,3,4\) extension counts distinguish respectively \(12,19,21,22\) classes. The complete classification is in `aronhold_22_types.csv`.

## Assumptions and scope
The characteristic of \(\mathbb F_q\) is odd, the curve is smooth and geometrically connected, and its hyperelliptic map has eight distinct geometric branch points \(B\). A theta characteristic is a degree-two divisor class \(\theta\) with \(2\theta=K_C\); its parity is \(h^0(\theta)\bmod2\). An Aronhold heptad is an unordered set of seven distinct odd theta characteristics for which the sum, as quadratic refinements of the Weil pairing, of every three distinct members is even. This definition makes sense for hyperelliptic curves without invoking plane-quartic bitangents.

The class \(H\) of a hyperelliptic fiber has \(K_C=2H\), and \(H\) is an even theta characteristic. The odd theta characteristics are precisely the \(28\) classes \([W_i+W_j]\) indexed by unordered pairs of distinct branch points. The geometric Frobenius permutes these pairs through its permutation on \(B\); no assumption on rational branch points is made.

## Proof
**1. Translate heptads to seven-edge graphs.** For even-cardinality subsets \(S\subseteq B\), the two-torsion classes are represented by \(v_S=[\sum_{i\in S}W_i-(|S|/2)H]\), with \(v_S=v_{B\setminus S}\). Relative to the even theta characteristic \(H\), their parity quadratic form satisfies \(q(v_S)=|S|/2\pmod2\), and their Weil pairing satisfies \(b(v_S,v_T)=|S\cap T|\pmod2\). Thus an odd theta characteristic is an edge of the complete graph on \(B\), and three edges \(e_1,e_2,e_3\) form an azygetic triple precisely when \(b(e_1,e_2)+b(e_1,e_3)+b(e_2,e_3)=1\) in \(\mathbb F_2\).

**2. Classify the heptads.** There are two families of seven-edge graphs satisfying that triple criterion:

- A seven-edge star at one point \(c\in B\), giving \(8\) graphs.
- A four-edge star at \(c\) together with a triangle on a three-element subset \(T\subset B\setminus\{c\}\), disjoint from the four star leaves, giving \(8\binom73=280\) graphs.

Every triple of edges in either family has an odd number of intersecting edge pairs. The graphs are pairwise distinct. The total is \(288\), which is also the standard count of Aronhold heptads (index of the \(S_7\) stabilizer in \(\operatorname{Sp}_6(\mathbb F_2)\)); hence the two families exhaust all heptads. Independently, `verify_aronhold.py` enumerates every seven-subset of the \(28\) odd theta characteristics satisfying the defining triple condition and finds exactly these \(288\) graphs. The correspondence is equivariant for permutations of \(B\), so
\[
\mathcal A_C(\overline{\mathbb F}_q)\cong B\ \sqcup\ \{(c,T):c\in B,\ T\subseteq B\setminus\{c\},\ |T|=3\}.
\]
The underlying \(8+280\) symmetric-group orbit decomposition is classical and is **not** claimed as new.

**3. Count Frobenius-fixed heptads.** Fix a power \(\sigma\) of Frobenius, with \(f\) fixed points, \(t\) two-cycles and \(u\) three-cycles on \(B\). Exactly \(f\) stars are fixed. For a fixed center \(c\), the invariant triangles among the remaining seven points number \(\binom{f-1}{3}+(f-1)t+u\): they are unions of three singleton cycles, one singleton and one two-cycle, or one three-cycle. If \(f=0\), there are no fixed centers. Multiplication by \(f\) and the identity \(f\binom{f-1}{3}=4\binom f4\) yield the displayed uniform formula, including \(f=0\).

**4. Prove the sharp inverse cutoff.** A permutation of eight points is conjugate to exactly one of the \(22\) integer partitions of eight. For each partition, the formula in step 3 applied to powers \(1,2,3,4\) yields the complete explicit table `aronhold_22_types.csv`. The \(22\) four-tuples are pairwise distinct. The numbers of distinct prefixes of lengths one, two and three are respectively \(12,19,21\); the sole three-prefix collision is \((8)\) versus \((4,4)\). The direct heptad permutation computation in `verify_aronhold.py` checks independently every entry and the full cycle spectra, including all necessary powers. Since a finite étale scheme's zeta function is the product \(\prod_d(1-T^d)^{-a_d}\), where \(a_d\) is the number of cycles of length \(d\), the full heptad zeta function is also determined.

**5. Show sharpness for actual curves.** For every odd \(q\), there are monic irreducible degree-eight polynomials, and at least two distinct monic irreducible quartics: the number of the latter is \((q^4-q^2)/4\geq18\). Their respective squarefree degree-eight products define smooth genus-three curves of branch types \((8)\) and \((4,4)\). Explicit examples over \(\mathbb F_3\) are the equations \(y^2=x^8+x^2+2\) and \(y^2=(x^4+x+2)(x^4+2x+2)\). The irreducibility assertions for these displayed polynomials are checked by exact polynomial division in the verifier. For the two branch types, the four heptad counts are respectively \((0,0,0,0)\) and \((0,0,0,288)\), proving that three extensions can never suffice uniformly.

## Verification
The standalone Python-standard-library program `verify_aronhold.py` enumerates all \(\binom{28}{7}=1{,}184{,}040\) seven-subsets, compares the exact theta-condition set to the graph construction, checks all \(22\) branch cycle partitions, checks all Frobenius powers through each permutation's order against the closed formula, checks the four-prefix distinguishing counts, validates the attached CSV, and checks the explicit \(\mathbb F_3\) polynomial irreducibility certificates by trial division. Execute from the directory containing both standalone artifacts:

```bash
python3 verify_aronhold.py
```

The expected completion line is `ARONHOLD_288_THETA_GRAPH_EQUALITY_22_SPLITTINGS_4_EXTENSIONS_VERIFIED`.

## Relationship to prior work
The definition, geometric total \(288\), and symplectic interpretation of Aronhold heptads are classical; see Dalla Piazza–Fiorentino–Salvati Manni and Bergvall. Dolgachev explicitly records the two \(S_8\)-orbits of lengths \(8\) and \(280\), and Gizatullin constructs a related dissection into eight block designs. None of those orbit statements is presented as new here. Bergvall's 2021 preprint studies arithmetic point counts of *moduli spaces of plane quartics with markings*, a different object from the Frobenius action on the heptad fiber of a given hyperelliptic curve. The new content assessed here is the exact finite-field heptad fixed-point formula, complete twenty-two-type spectrum and the optimal four-extension inverse theorem, including universal realizability of its obstruction.

## Limitations
This reconstructs the branch-point **cycle partition**, not the curve's isomorphism class, coordinates of the Weierstrass points or the Jacobian's Weil polynomial. The paper's geometry is formulated in odd characteristic only. The table is an exhaustive finite check, not a claim about arbitrary larger branch sets or all genus-three curves. No independent mathematical audit has been performed. Although the literature reviewed did not exhibit an equivalent four-extension heptad inverse theorem, an unindexed prior cycle-index or permutation-character calculation could conceivably imply it.

## References
1. O. Bergvall, *Arithmetic and topology of classical structures associated to plane quartics*, arXiv:2106.13072, first posted 2021-06-24, §§2.4, 3.3. https://arxiv.org/abs/2106.13072
2. F. Dalla Piazza, A. Fiorentino and R. Salvati Manni, *Plane quartics: the matrix of bitangents*, arXiv:1409.5032 (2014), §3. https://arxiv.org/abs/1409.5032
3. I. V. Dolgachev, *Classical Algebraic Geometry: A Modern View*, Cambridge University Press (2012), Chapter 6, §6.1.2. https://doi.org/10.1017/CBO9781139084437
4. M. Kh. Gizatullin, *Combinatorics associated with inflections and bitangents of plane quartics*, Izvestiya: Mathematics 77 (2013), 675–695, §8. https://doi.org/10.1070/IM2013v077n04ABEH002655
