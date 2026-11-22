# The first odd-primary torsion in alternating-group permutation complexes occurs on six letters

## Finding
Let \(X(A_6)\) denote the finite regular CW complex whose cells are nonempty injective words of six labels that occur as order-preserving subsequences of a permutation in the alternating group \(A_6\), with each cell of word length \(k\) having dimension \(k-1\). Then
\[
\widetilde H_i(X(A_6);\mathbb Z)=
\begin{cases}\mathbb Z^{95}\oplus\mathbb Z/3,&i=4,\0,&i\ne4.\end{cases}
\]
The three-primary torsion contrasts with the previously determined two-primary torsion for the four- and five-letter alternating groups. In particular, it is the first odd-primary occurrence in this sequence through six letters.

## Assumptions and scope
The generating permutations are **all** even permutations on \(\{0,1,2,3,4,5\}\), not alternating up-down patterns. Cells retain the *order* of letters. The boundary is signed deletion: on the word \((v_0,\ldots,v_k)\),
\[
\partial(v_0,\ldots,v_k)=\sum_{j=0}^k(-1)^j(v_0,\ldots,\widehat v_j,\ldots,v_k).
\]
This is the standard ordered-injective-word CW model of a permutation complex; it is not the ordinary unordered simplicial complex on the six labels.

## Proof
**Skeleton identification.** Every word containing at most five of the six letters appears in some even permutation: append the missing labels and, when the word has five letters, insert its unique missing letter in any of six positions. Consecutive insertions reverse permutation parity, so three completions are even. For shorter words, first extend to five letters. Thus the four-skeleton of \(X(A_6)\) is the complete four-skeleton of the injective-word complex \(J_6\). The only five-cells are the 360 even full permutations.

**Low homology and chain ranks.** The classical complete injective-word complex has reduced integral homology concentrated in top degree five (Björner–Wachs/Farmer; see Chachólski–Levi–Meshulam). Hence its cellular complex is exact below degree five. The chain ranks through dimension four are \(6,30,120,360,720\); the successive boundary ranks, from dimensions one through four, are \(5,25,95,265\). In particular, the kernel of the four-dimensional boundary is a **free** group of rank \(720-265=455\); and degrees below four remain acyclic in the partial complex.

**Integral top-boundary certificate.** Enumerate all 360 even permutations in lexicographic order, and all 720 length-five injective words likewise. Form the signed deletion matrix \(B\) of size \(720\times360\). The included independent script `verify_a6.py` regenerates its 2160 nonzero entries. Exact integer elementary row elimination using unit pivots removes 354 independent rows and columns, leaving a \(366\times6\) integral matrix. Its exact Smith diagonal is \((1,1,1,1,1,3)\). Consequently the original matrix has Smith invariant factors consisting of 359 ones and a single three. This proves that its integer rank is 360, so degree-five homology vanishes, and the free rank of degree-four homology is \(455-360=95\).

Finally, the inclusion \(\ker\partial_4\hookrightarrow C_4\) is saturated, since the quotient is isomorphic to the free group \(\operatorname{im}\partial_4\). Therefore the torsion subgroup of \(\ker\partial_4/\operatorname{im} B\) equals the torsion subgroup of \(C_4/\operatorname{im}B\), namely \(\mathbb Z/3\). This completes the integral classification.

## Verification
Execute `python verify_a6.py` with Python 3 and SymPy. The checker constructs the exact integer boundary, performs documented unimodular row operations, and computes the residual Smith form over \(\mathbb Z\). Independent finite-field elimination returns full-boundary ranks 360, 359, 360, 360, 360 over primes 2, 3, 5, 7, 11, respectively. The mod-three deficiency supports the three-primary Smith factor but does not replace the integer proof. All matrices are regenerated from permutations rather than read from unverified logs.

## Relationship to prior work
Govc (first made public 8 November 2026) proves freeness of the fundamental groups of permutation complexes, but this does not determine their higher integral homology. Chachólski, Levi and Meshulam study their cellular and homotopical framework and the full injective-word complex. A closely related published finite calculation determines \(X(A_4)\) and \(X(A_5)\), including two-primary torsion; its publicly indexed theorem has no six-letter result and does not imply the odd-primary Smith invariant here. The appearance of three-primary torsion is not a consequence of those known ranks. The complete text of that closely related published calculation was inaccessible for this comparison, leaving a priority risk.

## Limitations
This is a finite six-letter integral classification, not a theorem for all alternating groups. It does not identify an explicit geometric Moore-space attaching map, a homotopy wedge decomposition, or the symmetry action on homology. The source-priority check cannot establish global uniqueness; independent review has not occurred.

## References
- Dejan Govc, *Fundamental Groups of Permutation Complexes*, arXiv:2611.11362v1, publicly posted 8 November 2026, https://arxiv.org/abs/2611.11362.
- Wojtek Chachólski, Ran Levi, and Roy Meshulam, *On the topology of complexes of injective words*, arXiv:1908.03394, publicly posted 9 August 2019, https://arxiv.org/abs/1908.03394.
- *Integral two-torsion in alternating-permutation word complexes on four and five letters*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-integral-two-torsion-in-alternating-permutation-word-complexes-o--e61a258467d9.
