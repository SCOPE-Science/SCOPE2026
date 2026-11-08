# Scientific review

## Correctness

PASS. The word-to-edge correspondence is bijective under the stated rotation normalization; all admissible edges are distinct. The overlap graph is balanced and strongly connected, including the critical three-symbol case. The proof eliminates off-diagonal triple coordinates and decomposes the remaining pair-function space into constant, two standard copies, symmetric zero-sum, and antisymmetric zero-sum summands; the dimensions and scalar determinants account for the entire Laplacian characteristic polynomial. The matrix-tree and BEST formulas then yield the precise count. The source package includes a direct exhaustive ternary tour count, a separate exact Bareiss determinant implementation, and full SymPy characteristic-polynomial checks for alphabets three through six. Finite tests support the symbolic argument but are not presented as its proof.

## Originality

PASS at the stated scope, with historical-priority qualification. Penne (2010) establishes restricted de Bruijn existence for separation constraints; the full paper was not accessible, so priority remains uncertain. Alhakim (2020/2022), Section 4.1, constructs such sequences but applies the word 'square-free' to adjacent-letter separation, not to forbidding both period-one and period-two squares. Shur (2010) studies globally square-free circular words, with a distinct existence/classification problem. Generic BEST and matrix-tree formulas give an unevaluated determinant, but not the explicit factorization and closed multiplicity product here. Searches of related mathematical records and published literature located no equivalent evaluated result, which is not a proof of publication uniqueness.

## Value

PASS. The family consists of every legal local four-symbol pattern avoiding the first two square lengths; precisely the shortest nontrivial window in which period-two square avoidance matters. The closed all-alphabet enumeration sizes the full solution space of a constrained de Bruijn/symbolic scheduling problem, rather than constructing one representative, and reveals a nontrivial quadratic and cubic spectral decomposition. This is a natural full family, not an arbitrary finite parameter slice.

## Sources and limitations

Closest sources: Penne (2010), DOI 10.1016/j.disc.2009.10.009; Shur (2010), arXiv:1009.5759v1; Alhakim (2020 preprint, 2022 journal), DOI 10.1007/s10623-022-01077-5. The first has only abstract and subsequent-source discussion accessible; the latter two have relevant material inspected directly. Restricted to four-letter local square-freeness and labeled-alphabet/rotation equivalence; no claim of independent audit or exhaustive historical priority.

Self-review: passed. Independent audit: not yet performed.
