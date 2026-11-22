# The forty Steiner triplets determine cubic-surface Frobenius

## Finding
Let \(S/\mathbb F_q\) be any smooth cubic surface. Its \(27\) geometric lines admit \(120\) unordered pairs of Steiner trihedra. Each pair is represented by its common nine-line support. An **unordered Steiner triplet** is a partition of all \(27\) geometric lines into three such nine-line supports. The classical configuration contains exactly \(40\) triplets. It is stable under Galois and thus defines a finite étale \(40\)-point scheme \(\mathcal T_S\).

**Reconstruction theorem.** The zeta function
\[
Z(\mathcal T_S,T)=\exp\left(\sum_{n\ge1}\frac{\#\mathcal T_S(\mathbb F_{q^n})}{n}T^n\right)
\]
determines the conjugacy class of geometric Frobenius in \(W(E_6)\). More precisely, the \(25\) conjugacy classes of \(W(E_6)\) induce \(25\) distinct cycle partitions on the \(40\) triplets.

The nine counts \(\#\mathcal T_S(\mathbb F_{q^n})\) for \(1\le n\le9\) suffice. This initial consecutive-degree cutoff is sharp: two distinct conjugacy classes, with respective triplet cycles \(1^1 3^1 12^3\) and \(1^1 3^1 9^4\), give identical counts for \(1\le n\le8\), but the degree-nine counts are \(4\) and \(40\), respectively.

A second consequence is that the complete Frobenius cycle partition on the \(27\) lines, together with the *single base-field count* \(\#\mathcal T_S(\mathbb F_q)\), also determines the conjugacy class. The line partition alone yields only \(20\) distinct signatures among the \(25\) classes. In particular, the triplet zeta function determines the geometric Picard-group Frobenius polynomial and therefore the Hasse–Weil zeta function of \(S\), but does not determine its isomorphism class.

## Assumptions and scope
The claim holds for every prime power \(q\) and every smooth cubic surface over \(\mathbb F_q\), including surfaces with Eckardt points. Neither a chosen rational line nor a split blowdown is assumed. The scheme \(\mathcal T_S\) is the finite étale Galois set of *unordered decompositions* into three Steiner trihedral pairs; the \(240\) ordered triplets are a different marking. Each nine-line support is itself unlabelled. All computations refer to the fixed geometric incidence structure of the \(27\) lines, not to arbitrary or singular cubics.

Use the standard blowup marking over an algebraic closure: let \(H\) be the pullback of a projective line and \(E_1,\ldots,E_6\) the six exceptional classes. Encode a class \(dH-\sum m_iE_i\) by \((d,m_1,\ldots,m_6)\), with intersection \(dd'-\sum m_im'_i\). The \(27\) line classes are the six \(E_i\), the fifteen \(H-E_i-E_j\), and the six \(2H-\sum_{j\ne i}E_j\). Their anticanonical class is \(3H-\sum_iE_i\).

## Proof
**Step 1: reconstruct incidence.** The \(45\) tritangent planes correspond exactly to unordered triples of line classes summing to the anticanonical class. This follows from the exceptional-curve intersection model and is independently checked by enumerating all \(\binom{27}{3}\) triples in `verify.py`. Every such triple consists of three pairwise intersecting lines.

**Step 2: reconstruct the Steiner configuration.** Enumerate unordered triples of tritangent planes whose line sets are pairwise disjoint, and index them by their nine-line unions. Exactly \(120\) supports have two distinct such triples. For each, the resulting two triples are row and column planes in a \(3\)-by-\(3\) Steiner array: every row meets every column in exactly one line, and all nine lines occur. This characterizes the \(120\) classical Steiner trihedral pairs; all six tritangent planes contained in such a support are recovered. Each nine-line support has precisely two other disjoint nine-line supports, and the three cover all \(27\) lines. They give \(40\) unordered triplets. An independent orbit calculation confirms the \(40\)-element set is one orbit under the full Weyl group, of stabilizer order \(1296\).

**Step 3: compute Weyl action without class-table assumptions.** Reflections in the five roots \(E_i-E_{i+1}\) and the root \(H-E_1-E_2-E_3\) act on the \(27\) line classes. Their full permutation closure contains exactly \(51{,}840\) elements, the order of \(W(E_6)\). Conjugation by these six generators partitions them into exactly \(25\) conjugacy classes, whose sizes sum to \(51{,}840\). This establishes completeness independently of any assumed cycle-class labels.

**Step 4: check inverse spectra.** For each conjugacy-class representative, induce its permutation on the \(40\) triplets and decompose it into cycles. `certificate.csv` records all \(25\) class sizes and triplet partitions. Every pair of rows has different triplet cycles; thus the triplet zeta function, which determines and is determined by the cycle partition of a finite Galois set, identifies the Weyl conjugacy class. The computed numbers of distinct signatures from the initial counts through degrees \(1,2,\ldots,9\) are exactly
\[
10,\ 14,\ 20,\ 22,\ 23,\ 24,\ 24,\ 24,\ 25.
\]
The order-twelve and order-nine class representatives have respective triplet spectra \(1^1 3^1 12^3\) and \(1^1 3^1 9^4\). For each degree below nine, the only fixed contributions come from the one-cycle and, when divisible by three, the three-cycle. Their degree-nine counts differ because nine divides one long-cycle length but not the other. This proves optimality for consecutive initial extension degrees.

**Step 5: line-side refinement and arithmetic consequence.** The same complete class table yields \(20\) distinct line-cycle partitions and shows that all \(25\) ordered pairs consisting of a line-cycle partition and the number of fixed triplets are distinct. Frobenius acts on the geometric Picard group through its Weyl conjugacy class. Its Picard action determines all smooth-cubic-surface point counts over finite extensions by the standard cohomological trace formula, hence the surface zeta function.

## Verification
Place `verify.py` and `certificate.csv` in the same directory, then execute `python3 verify.py certificate.csv` using Python 3 and the standard library. The program reconstructs the \(27\) lines, \(45\) planes, \(120\) Steiner supports and \(40\) triplets, enumerates \(W(E_6)\), computes all conjugacy classes and their triplet spectra, and verifies all separation and cutoff claims. It reconstructs the expected CSV in memory and compares its exact bytes with the supplied certificate. No Magma, GAP, Sage, external database, randomness or floating-point calculation is needed. A direct Weyl-orbit check independently verifies the generated \(40\)-object configuration.

## Relationship to prior work
The geometric \(27\)-line incidence structure, \(120\) pairs of Steiner trihedra, and their decomposition into \(40\) unordered triplets are classical. Elsenhans–Jahnel, *Cubic surfaces with a Galois invariant pair of Steiner trihedra* (arXiv:1006.1474, §2), explicitly establish the complementary-pair geometry and its Galois applications. Their *On the order three Brauer classes for cubic surfaces* (arXiv:1110.2086, §3) associates order-three Brauer phenomena to triplets and identifies \(40\) unordered decompositions, but does not state the \(25\)-class inverse zeta theorem or its sharp nine-degree cutoff. Das, *Arithmetic statistics on cubic surfaces* (arXiv:2002.11183, §§1–3), gives arithmetic distributions and tables of the \(25\) Weyl types; its arbitrary-marking framework is compatible with computing triplet actions but does not provide this inverse \(40\)-point spectral separation or the short-count assertions.

Other line, tritangent, double-six and sixer configurations have their own splitting data. In particular, a previous classification showing the \(72\)-sixer action distinguishes all \(25\) Weyl classes does not imply that the smaller, structurally different \(40\)-triplet action does so. The novelty assessed here is the triplet-side reconstruction property and its exact observation cutoff, not the existence of the classical triplets or the known list of Weyl classes.

## Limitations
The result distinguishes only the **Frobenius conjugacy class**, not the isomorphism class of a cubic surface. A finite-field surface need not realize every abstract Weyl type at every small field size; the theorem is conditional on its actual type. The proof is exhaustive but finite: it rests on the accepted classical identification of the cubic-surface line-incidence automorphism group with \(W(E_6)\) and on an explicitly reproducible \(51{,}840\)-element enumeration. The nine-degree minimality concerns **consecutive first extension degrees**; it is not a claim that every selection of fewer than nine nonconsecutive degrees fails. It is possible to obtain full discrimination with three much larger extension degrees. An unindexed historical permutation-character table may implicitly encode the triplet cycles; that remains the principal originality risk. No independent audit has been performed.

## References
1. A.-S. Elsenhans and J. Jahnel, *Cubic surfaces with a Galois invariant pair of Steiner trihedra*, arXiv:1006.1474v1 (8 June 2010), especially §2. https://arxiv.org/html/1006.1474v1
2. A.-S. Elsenhans and J. Jahnel, *On the order three Brauer classes for cubic surfaces*, arXiv:1110.2086v1 (10 October 2011), especially §3. https://arxiv.org/abs/1110.2086
3. R. Das, *Arithmetic statistics on cubic surfaces*, arXiv:2002.11183v1 (25 February 2020), especially §§1–3. https://arxiv.org/abs/2002.11183
4. F. Sottile and T. Yahl, *Splitting types of the 27 lines on cubic surfaces*, online mathematical exposition. https://franksottile.github.io/research/stories/27_Frobenius/index.html
