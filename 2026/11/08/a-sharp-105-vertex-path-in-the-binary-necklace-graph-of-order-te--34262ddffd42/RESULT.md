# A sharp 105-vertex path in the binary necklace graph of order ten

## Finding
Let \(NG(10)\) have one vertex for each binary length-ten word up to cyclic rotation, and join two vertices when some respective representatives differ in exactly one bit. The longest simple path in \(NG(10)\) contains **exactly 105 vertices** (equivalently, 104 edges). Thus the previously known parity upper bound in Proposition 7.4 of Karhumäki–Puzynina–Rao–Whiteland is attained at \(n=10\), establishing this instance of their Conjecture 7.5. A complete 105-vertex witness appears in `CERTIFICATE.txt` and is checked by the self-contained `verify.py`.

## Assumptions and scope
A *binary word* is a string in \(\{0,1\}^{10}\). Two words represent the same *necklace* if one is a cyclic rotation of the other. The *canonical representative* of a necklace is the lexicographically least rotation. Distinct necklaces are adjacent precisely when one can be represented by words at Hamming distance one; equivalently, some rotation of the canonical representative of the second differs in exactly one coordinate from the canonical representative of the first. Paths are simple: no necklace can occur twice. Path length here is **number of vertices**, not edges. The theorem is only for order ten; it does not prove the even-order conjecture in general, nor the separate maximal-cycle-decomposition conjecture.

## Proof
**Upper bound.** There are \(108\) binary necklaces of length ten. This follows from Burnside's lemma:
\[
|V(NG(10))|=\frac{2^{10}+2^5+4\cdot 2^2+4\cdot2}{10}=108.
\]
The Hamming weight parity of a necklace is well-defined because rotation preserves the number of ones. The set of odd-weight necklaces has size
\[
|V_{\mathrm{odd}}|=\frac{2^{10}+4\cdot2^2}{20}=52,
\]
by the corresponding fixed-weight necklace count (also reproducible by enumerating all length-ten strings and taking least rotations). Therefore \(|V_{\mathrm{even}}|=56\). An edge changes exactly one bit, so the graph is bipartite, with these two parity classes. A simple path alternates classes and can use at most \(52\) odd vertices and at most \(53\) even vertices, hence at most \(105\) vertices. This is the order-ten specialization of the published parity bound \(BPL(n)\), not a new general upper bound.

**Attainment.** `CERTIFICATE.txt` contains 105 rows, each a distinct canonical binary necklace representative of length ten. It begins with `0000000000`, ends with `1111111111`, contains every one of the 52 odd-weight necklaces and 53 even-weight necklaces, and omits precisely `0001101001`, `0011110101`, and `0110111111` from the 108 vertices. Each consecutive pair of rows has representatives at Hamming distance one: for consecutive canonical representatives \(a,b\), one of the ten cyclic rotations of \(b\) has Hamming distance one from \(a\). The 104 checks of this last assertion, the canonical-representative tests, and the complete census of the graph are independently rerunnable using the transparent verifier included here. These finite, exhaustive checks establish a 105-vertex *simple* path. Together with the upper bound they prove the claimed optimum.

## Verification
In a directory containing both bundled files, run `python3 verify.py`. The verifier constructs all \(2^{10}=1024\) binary strings independently, identifies their canonical rotations, counts the parity classes, rejects duplicate or noncanonical certificate entries, verifies every cyclic adjacency, and checks the missing three classes and the bipartite upper bound. Its expected output begins with `CERTIFICATE_VALIDATED classes=108 even=56 odd=52 path=105 edges=104` and then lists the three omitted necklaces. There is no dependency other than a standard Python 3 interpreter. The derivation of the upper bound does not depend on a heuristic search or an optimization solver; the lower bound depends only on a fully specified finite witness and elementary checks.

## Relationship to prior work
Degni and Drisko (2007) study Gray-order and near-Gray-order binary necklaces, including parity obstructions for even lengths. Karhumäki, Puzynina, Rao and Whiteland (2016), Proposition 7.4, establish the general bipartite bound, state its attainability as Conjecture 7.5, and explicitly report verification only through even orders at most eight. Whiteland's 2019 thesis, Chapter 6, similarly records this necklace-path question and only the smaller even-order witnesses. This finding adds a concrete sharp witness at the next even order \(n=10\); it does not claim a new general parity bound, or solve the different and stronger maximal-cycle-decomposition conjecture. The direct and closely related texts inspected do not exhibit the order-ten 105-vertex witness. Historical priority is provisional because an unindexed or otherwise inaccessible equivalent construction may exist.

## Limitations
This is a single-order exact result, not an infinite family or an algorithm guaranteeing such paths at higher even orders. The certificate is reproducible, but no independent human mathematical audit has been performed. Failure to find a matching published construction does not establish absolute novelty; the 2007 Gray-order framework is a relevant possible source of implicit coverage not resolved by a theorem explicitly giving this witness.

## References
1. C. Degni and A. A. Drisko, *Gray-ordered Binary Necklaces*, Electronic Journal of Combinatorics **14** (2007), #R7, published January 3, 2007. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v14i1r7/pdf/
2. J. Karhumäki, S. Puzynina, M. Rao and M. A. Whiteland, *On cardinalities of k-abelian equivalence classes*, arXiv:1605.03319v1 (May 11, 2016), especially §7.1, Proposition 7.4 and Conjecture 7.5. https://arxiv.org/html/1605.03319v1
3. M. A. Whiteland, doctoral thesis (2019), Chapter 6, §6.4, Example 6.39 and Conjecture 6.40. https://www.utupub.fi/server/api/core/bitstreams/b3b51aff-6c73-43aa-854c-ca2a6e5ba99a/content
4. T. Mütze, *Combinatorial Gray codes—an updated survey*, Electronic Journal of Combinatorics **30** (2023), #DS26, especially the necklace discussion on p. 22. https://wrap.warwick.ac.uk/id/eprint/177071/7/11023-PDF%20file-45589-3-10-20230710.pdf
