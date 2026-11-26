# Eight affine semilinear orbits of shattered four-sets in the Paley graph of order 25

## Finding
Exactly 3,600 four-element supports are shattered by the open neighborhoods of the Paley graph on \(\mathbb F_{25}\). These are the maximum-cardinality shattered supports. They form precisely eight orbits under square scalings, translations and Frobenius, with the following representatives, sizes and stabilizer orders:

| Representative | Orbit size | Stabilizer order |
|---|---:|---:|
| \(\{0,1,2,5\}\) | 600 | 1 |
| \(\{0,1,2,8\}\) | 600 | 1 |
| \(\{0,1,5,6\}\) | 150 | 4 |
| \(\{0,1,5,11\}\) | 600 | 1 |
| \(\{0,1,5,15\}\) | 600 | 1 |
| \(\{0,1,5,23\}\) | 600 | 1 |
| \(\{0,1,8,15\}\) | 300 | 2 |
| \(\{0,1,10,11\}\) | 150 | 4 |

This gives the size and symmetry types of maximum witnesses for equality in the information bound \(\operatorname{VCdim}\le\lfloor\log_2 25\rfloor=4\), rather than just exhibiting a single witness.

## Assumptions and scope
Use \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\); label \(a+bt\) by \(a+5b\), with \(0\le a,b<5\). Let \(Q\) be the set of nonzero squares. The concept at center \(y\) is \(y+Q\). A center may lie in the support, but the zero difference is not a square for this adjacency test. A set \(A\) is shattered if all subsets of \(A\) are obtained as traces of the concepts. The group in the table is specifically \(x\mapsto s x^{5^\epsilon}+b\) with \(s\in Q\), \(b\in\mathbb F_{25}\), and \(\epsilon\in\{0,1\}\); no assertion about the full automorphism group is needed.

## Proof and reproducible census
The norm of a field element \(x=a+bt\) is \(x^6=a^2-2b^2\). A nonzero \(x\) is a square if and only if its norm is a nonzero square in \(\mathbb F_5\), since raising the norm to the second power gives \(x^{12}\). This also specifies the adjacency table without a graph database. For each of the \(\binom{25}{4}=12{,}650\) supports, list its elements increasingly and compute the four-bit trace mask at each of the 25 centers. The attached `paley25_verify.py` visits all these supports and retains exactly those whose mask sets have size 16. It checks that precisely 3,600 are retained. The group maps are distinct because values at zero and one determine \(b\) and \(s\), and Frobenius sends \(t\) to \(-t\). They preserve adjacency and hence shattering. For the lexicographically least remaining shattered support the verifier generates its complete orbit, checks containment in the remaining family and removes the orbit. It verifies the eight rows of the table and exhausts that family. Dividing 600 by each orbit size gives the stabilizer order. Finally 25 concepts cannot realize the 32 traces on a five-element set, or all traces on a larger set. This confirms maximal cardinality and proves that the table covers all maximum-size witnesses.

## Relation to prior results
McDonald, Sahay and Wyman, *The VC dimension of quadratic residues in finite fields*, [arXiv:2210.03789v2](https://arxiv.org/html/2210.03789v2), study shattering by quadratic-residue translates and give bounds and prime-field experiments. Their convention in the nonsquare-dilation argument of §4 excludes centers in the support, whereas the open-neighborhood census here permits them. The square-scaling and translation symmetries used here follow directly from graph adjacency and are not new.

The size-three obstruction is not an independent novelty claim. For a nonsquare \(c\), a support \(A\) has no all-positive open-neighborhood trace exactly when \(cA+(Q\cup\{0\})=\mathbb F_{25}\). Indeed \(-1\) is a square and multiplication by \(c\) sends nonzero squares to the complement of \(Q\cup\{0\}\); apply this pointwise to the differences between a center and the support. The earlier [three-shift covering census](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-complete-affine-square-orbit-spectrum-of-three-shift-quadratic-r--3e8343da37ce/RESULT.md) gives one orbit of 100 such closed covering triples at order 25. The [open Lovász neighborhood complex calculation](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-five-primary-torsion-in-the-open-neighborhood-complex-of-the-pal--94202559c076/RESULT.md) gives 9,475 four-sets having an all-positive trace. Neither the presence nor absence of one trace pattern tests all 16 masks. The assertion here is the narrower exact symmetry classification of the four-sets realizing every trace.

## Limitations
This is a complete finite enumeration for the stated field and open-neighborhood convention, not a formula for other field orders or for a modified notion of shattering. The group is the specified affine semilinear subgroup, not a claim about all graph or set-system symmetries.
