# Two equality types for seven-row binary 2-disjunct codes
## Finding
Let \(X\) be a seven-point set and let \(\mathcal F\subseteq 2^X\setminus\{\varnothing\}\). Call \(\mathcal F\) 2-cover-free when, for every three distinct members \(A,B,C\in\mathcal F\),
\[
A\nsubseteq B\cup C.
\]
Then every such family satisfies \(|\mathcal F|\le 7\). There are exactly \(31\) labeled families of size \(7\): one is the family of all seven singletons, and the other \(30\) are the labeled Steiner triple systems on \(X\). Hence point relabeling has exactly two equality orbits. Their orbit sizes are \(1\) and \(30\), and their stabilizer orders in \(S_7\) are \(5040\) and \(168\).

Equivalently, among binary matrices with seven rows whose columns are required to be 2-disjunct, the largest possible number of distinct nonzero columns is \(7\). Every square optimum is, up to row and column permutations, either the identity matrix or the incidence matrix of the Fano plane.

A representative of the nontrivial orbit has blocks
\[
\{123,145,167,246,257,347,356\}.
\]

## Assumptions and scope
Columns are identified with their nonempty supports in a fixed seven-element row set. A binary matrix is 2-disjunct when every column has a row containing a \(1\) in that column and \(0\)s in any prescribed pair of other columns. For three distinct support sets \(A,B,C\), this is exactly the condition \(A\nsubseteq B\cup C\), together with the analogous conditions obtained by permuting the three sets. Column order is immaterial for the family count; labeled means that the seven rows are labeled.

The claim concerns the unrestricted family of nonempty supports. It is not a constant-weight classification.

## Proof
The upper bound and equality census are established by a finite exhaustive search over the \(127\) nonempty subsets of a seven-point set. Supports are encoded by nonzero seven-bit integers. The search builds a family in increasing integer order. After choosing a new support \(S\), a future candidate \(T\) is retained exactly when every triple consisting of \(S,T\) and one previously chosen support is 2-cover-free. Thus each unordered family appears once, and every pruned branch already contains a forbidden triple.

The search finds no eight-member family and finds exactly \(31\) seven-member families. One of these consists of the seven singletons. Every other maximum family consists of seven triples. For each of those \(30\) families, the verifier independently counts the \(21\) unordered pairs of points and checks that each pair occurs in exactly one block. Hence every nonsingleton maximum is a Steiner triple system on seven points, therefore a Fano plane.

For the symmetry statement, the verifier applies all \(7! = 5040\) point permutations to the displayed Fano system. Its orbit has exactly \(30\) members and equals the full nonsingleton census. Therefore its stabilizer has order \(5040/30=168\). The singleton family is fixed by every point permutation, so its orbit has size \(1\) and stabilizer order \(5040\).

## Verification
The standalone `verify.py` reproduces the exhaustive search from the definition, not from a stored list of maxima. It reports

`VERIFY_OK target8=0 nodes8=116093 maximum=7 maxima=31 singleton=1 fano=30 row_group=5040 orbits=2 orbit_sizes=1,30 stabilizers=5040,168 nodes7=134096 census_sha256=c6d843cb81ba620e9f5dec28c20e01b50e3c2ce72e1f2616971ea0f0c2d78027`

The search tree is finite and deterministic. The certificate hash is the SHA-256 digest of the canonically sorted textual census of all \(31\) maximum families.

## Relationship to prior work
Kautz and Singleton introduced binary superimposed codes in the Boolean-sum formulation and described constructions based on combinatorial arrangements, including block designs. The seven-line Fano incidence matrix is therefore a classical type of construction, not a new construction here. Later cover-free-family literature treats the same incidence-matrix model and proves uniqueness results for several other parameter sets.

A database result for the constant-weight-three subproblem shows that extremal 3-uniform 2-cover-free families are maximum triple packings; at seven points this already accounts for the Fano branch. That result does not cover unrestricted supports and therefore does not imply that the only other unrestricted equality case is the singleton family or that mixed-weight equality cases do not exist. The present claim is precisely the unrestricted equality classification and labeled census.

## Limitations
This is a finite seven-row classification. It does not classify larger 2-disjunct matrices, error-tolerant variants, or cover-free families with different covering parameters. The literature search did not reveal an implication-equivalent statement of the unrestricted equality classification, but an obscure or poorly indexed historical classification remains a residual originality risk. The oldest foundational source was not fully machine-readable in this run; its accessible scan summary and bibliographic material were used only to establish the model and historical construction context, not to justify a negative whole-document claim.

## References
1. W. H. Kautz and R. C. Singleton, “Nonrandom Binary Superimposed Codes,” *IEEE Transactions on Information Theory* 10(4), 363–377 (1964), DOI 10.1109/TIT.1964.1053689.
2. H. K. Kim and V. Lebedev, “On the Optimality of Trivial \(w,r\)-Cover-Free Codes,” *Problems of Information Transmission* 40(3), 195–201 (2004), DOI 10.1023/B:PRIT.0000044255.42299.4F.
3. H. K. Kim, V. Lebedev, and D. Y. Oh, “Some New Results on Superimposed Codes,” *Journal of Combinatorial Designs* 13, 276–285 (2005), DOI 10.1002/jcd.20029.
