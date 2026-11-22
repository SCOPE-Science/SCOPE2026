# A sharp degree-eighteen descent bound for plane contractions of degree-two del Pezzo surfaces

## Finding
Let \(q\) be an odd prime power and let \(S/\mathbb F_q\) be a smooth degree-two del Pezzo surface. Among the seven-element sets of pairwise disjoint geometric exceptional curves on \(S\), let \(d_{\mathrm{bd}}(S)\) be the least positive extension degree over which one such **unordered set** is Galois-invariant. Equivalently, it is the least degree over which \(S\) admits a morphism contracting seven exceptional curves to \(\mathbb P^2\).

Then
\[
d_{\mathrm{bd}}(S)\in\{1,2,3,4,6,8,9,12,18\}.
\]
The bound \(18\) is attained by a smooth surface over **every odd prime-power field with \(q\ge9\)**. These are precise field-of-definition statements about actual contractions of the specified surface, not merely rationality or geometric existence claims.

More precisely, the geometric configuration has exactly \(576\) unordered contraction sets. Across the \(2{,}903{,}040\) elements of the Weyl group \(W(E_7)\), the distribution of the shortest orbit length on this configuration is:

| Shortest orbit length | Number of Weyl elements |
|---:|---:|
| \(1\) | \(694477\) |
| \(2\) | \(1012627\) |
| \(3\) | \(99008\) |
| \(4\) | \(30240\) |
| \(6\) | \(139328\) |
| \(8\) | \(362880\) |
| \(9\) | \(161280\) |
| \(12\) | \(241920\) |
| \(18\) | \(161280\) |

There is an order-eighteen class whose action on the \(56\) exceptional curves has cycle lengths \(2^1 18^3\) and on the \(576\) contraction sets has \(18^{32}\). Under the natural two-to-one quotient by the Geiser involution, these \(576\) sets give \(288\) Aronhold heptads, on which that same class has \(9^{32}\). Thus a degree-nine Aronhold heptad may be defined while **neither of its two geometric plane contractions descends before degree eighteen**.

## Assumptions and scope
The surface is smooth, geometrically integral, and of anticanonical degree two; the base field is finite of odd characteristic. An exceptional curve means a geometrically irreducible \((-1)\)-curve. Seven curves are disjoint as curves, not merely as divisor classes. A contraction set is unordered and consists of seven distinct pairwise disjoint exceptional curves. The invariant counts the minimal \(m\ge1\) such that the entire set is invariant under the \(m\)-th power of geometric Frobenius; it does **not** require every constituent exceptional curve to be defined individually over the extension.

The finite étale set of all \(576\) contraction sets is acted upon by the Picard-lattice Frobenius class in \(W(E_7)\). A Galois-stable disjoint exceptional collection can be contracted over the ground field by equivariant Castelnuovo contraction. Its target is a smooth degree-nine del Pezzo surface, hence a Severi–Brauer surface; over a finite field it is isomorphic to \(\mathbb P^2\). Conversely, the geometric exceptional locus of any such contraction is Galois-stable. Therefore the shortest orbit length is exactly the least extension degree in the finding.

## Proof
Fix a geometric blow-up marking of \(S\). In the lattice with basis \(H,E_1,\ldots,E_7\), intersection matrix \(\operatorname{diag}(1,-1,\ldots,-1)\), and canonical class \(K=-3H+\sum E_i\), all \(56\) exceptional classes occur in four standard families:
\[
E_i\ (7),\quad H-E_i-E_j\ (21),\quad
2H-\sum_{i\in I}E_i\ (|I|=5;\ 21),\quad
3H-2E_i-\sum_{j\ne i}E_j\ (7).
\]
Each has square \(-1\) and canonical intersection \(-1\). On a degree-two del Pezzo surface these are precisely the exceptional curves; distinct members are disjoint exactly when their intersection is zero. Enumerating their seven-element, pairwise-disjoint subsets yields exactly \(576\) contraction sets.

The roots \(E_i-E_{i+1}\), for \(1\le i\le6\), together with \(H-E_1-E_2-E_3\), generate the Weyl reflections of type \(E_7\). For a root \(\alpha\), the reflection acts by \(s_\alpha(D)=D+(D\cdot\alpha)\alpha\). The accompanying standalone generator constructs their seven permutations on the \(56\) exceptional classes and checks that they preserve the \(576\) contraction sets.

The exhaustive integer census enumerates the generated group as **exactly \(2{,}903{,}040\) distinct permutations**, groups its elements into all **\(60\) conjugacy classes** using conjugation by the seven generators, and computes the full cycle decomposition of one representative of each class on the \(576\) sets. Conjugate elements have identical cycle decompositions. Summing class sizes by shortest cycle length gives the complete nine-row table above; the displayed counts sum to the full group order. This proves the upper bound and excludes every other shortest-degree value. The relevant certificate is finite and exhaustive: it does not assume that a sample of fields or conjugacy classes is representative.

One class of size \(161280\) has all \(576\) contraction sets in \(32\) cycles of length \(18\). The exact representative permutation and class size are printed in the census certificate; the independent witness checker confirms its \(56\)-curve cycle structure, its \(576\)-set structure and the commuting Geiser quotient, which has \(32\) nine-cycles on the \(288\) Aronhold heptads. This establishes the geometric sharpness and the arithmetic two-sheet distinction.

Finally, Loughran–Trepalin's inverse-Galois classification, Theorem 1.2, asserts that **every** conjugacy class of \(W(E_7)\) is realized by a smooth degree-two del Pezzo surface over each \(\mathbb F_q\) with \(q\ge9\). Therefore every odd such field admits a surface whose shortest contraction-set orbit is \(18\), proving fieldwise sharpness.

## Verification
The complete, self-contained reproducibility files are `make_markings.py`, `markings.txt`, `census.cpp`, `census.out`, and `verify_witness.py`. From a directory containing them, run:

```sh
python3 make_markings.py
c++ -O2 -std=c++17 census.cpp -o census
./census > census.out
python3 verify_witness.py
```

Generation asserts all \(56\) distinct exceptional classes, all \(576\) disjoint seven-curve sets, the seven root-reflection permutations and the \(288\) fixed-point-free Geiser pairings. The C++ census asserts the full group order and all \(60\) conjugacy classes; its output lists every class's exact representative and cycle histogram, followed by the nine degree totals. The witness script checks the \(18^{32}\) orbit decomposition and the \(9^{32}\) Geiser quotient. The first enumeration was additionally cross-checked by an independent direct, element-by-element \(W(E_7)\) enumeration rather than by conjugacy representatives; it gave the same nine totals.

## Relationship to prior work
The \(56\) exceptional curves, the \(W(E_7)\) marking action, the Geiser quotient, and its \(288\) Aronhold heptads are classical; they are not claimed here as original. Bergvall, *Arithmetic and topology of classical structures associated with plane quartics* (2023), explains the relationship between plane blow-up markings and heptads. Bergvall, *Frobenius actions on Del Pezzo surfaces of degree 2* (2022), tabulates and counts Frobenius Weyl types of surfaces. Loughran–Trepalin (2018), Theorem 1.2, determines which types occur over finite fields. Those results supply the geometric framework and the existence theorem, but do not report the evaluated shortest-orbit census on the **\(576\) unordered seven-curve contraction sets** or the exhibited degree-nine-versus-degree-eighteen Geiser distinction. The new claim concerns the arithmetic descent of an actual contraction, not the existence of a single bitangent, an Aronhold heptad, or a rational point.

## Limitations
No explicit polynomial equation is provided for a degree-eighteen extremal surface: realization for every odd \(q\ge9\) follows from the cited inverse-Galois theorem. Possible sharper classifications restricted to \(q=3,5,7\) are not asserted. The result does not claim that degree \(18\) is the minimum field over which the surface is rational; a plane contraction is a stronger, specified geometric requirement. It does not claim that the Weil-group arithmetic frequencies in the table are frequencies of isomorphism classes of surfaces at a fixed finite field, nor does it address characteristic two. The irreducible priority risk of an older unpublished or unindexed equivalent \(576\)-point permutation calculation remains.

## References
1. D. Loughran and A. Trepalin, *Inverse Galois problem for del Pezzo surfaces over finite fields*, arXiv:1811.06785, first public 2018-11-16; *Math. Res. Lett.* **27** (2020), 845–853, Theorem 1.2. https://arxiv.org/abs/1811.06785 ; https://doi.org/10.4310/MRL.2020.v27.n3.a11
2. O. Bergvall, *Frobenius actions on Del Pezzo surfaces of degree 2*, arXiv:2211.12855, first public 2022-11-23. https://arxiv.org/abs/2211.12855
3. O. Bergvall, *Arithmetic and topology of classical structures associated with plane quartics*, *European Journal of Mathematics* **9** (2023), article 117. https://doi.org/10.1007/s40879-023-00711-3
4. B. Banwait, F. Fité and D. Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, *Math. Proc. Cambridge Philos. Soc.* **167** (2019), 35–60. https://doi.org/10.1017/S0305004118000166
