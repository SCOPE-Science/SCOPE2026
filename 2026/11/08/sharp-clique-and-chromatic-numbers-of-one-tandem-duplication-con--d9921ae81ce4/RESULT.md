# Sharp clique and chromatic numbers of one-tandem-duplication confusability graphs

## Finding
For all integers \(q\ge 2\), \(k\ge1\), and \(n\ge k\), define the simple graph \(G_{q,k,n}\) with vertex set \(\mathbb Z_q^n\). Two distinct vertices are adjacent if and only if their sets of distinct descendants under **exactly one** length-\(k\) tandem duplication have nonempty intersection. Then
\[
\boxed{\chi(G_{q,k,n})=\omega(G_{q,k,n})=\max\{1,n-2k+1\}.}
\]
In particular, all \(q^n\) sources can be partitioned into exactly \(\max\{1,n-2k+1\}\) single-duplication-correcting codes, and no partition into fewer such codes exists. The coloring is explicit and computable in time \(O(n)\) for fixed-cost alphabet arithmetic.

## Assumptions and scope
The alphabet \(\mathbb Z_q\) is the additive cyclic group of order \(q\), but \(q\) need not be a prime or prime power. For a word \(x=uvw\) with \(|v|=k\), a tandem duplication replaces it with \(uvvw\). A descendant set includes all distinct results of choosing a valid occurrence of \(v\); distinct duplication positions can lead to identical descendants. Exactly one operation is performed, not zero or at most one. Word positions are indexed, and the graph has no loops. The chromatic number \(\chi\) is the least number of vertex colors separating adjacent sources; the clique number \(\omega\) is the largest size of a complete subgraph.

Let \(m=n-k\) and define the bijective \(k\)-step derivative
\[
\phi_k(x)=(a,b),\qquad a=(x_1,\ldots,x_k),\quad b_i=x_{i+k}-x_i\pmod q\quad (1\le i\le m).
\]
The inverse reconstructs \(x_{i+k}\) sequentially from \(x_i\) and \(b_i\), so no property of a field is used. Write the unique zero-run decomposition
\[
b=0^{r_0}w_1 0^{r_1}\cdots w_s0^{r_s},\qquad w_j\ne0,\quad r_j\in\mathbb Z_{\ge0}.
\]
There are \(d=s+1\) zero runs. For each \(i\in\{0,\ldots,s\}\), set \(u_i=\lfloor r_i/k\rfloor\). Define the color
\[
\kappa(x)=\left(\sum_{i=0}^{s}i u_i\right)\bmod d
\]
when some \(r_i\ge k\), and set \(\kappa(x)=0\) if every \(r_i<k\). All displayed representatives lie in \(\{0,\ldots,\max(1,n-2k+1)-1\}\). A singleton modulus \(d=1\) gives color zero.

## Proof
**Derivative reduction.** Suppose a duplication begins after the first \(p\) symbols, so the copied block is \(x_{p+1},\ldots,x_{p+k}\). Direct substitution in the derivative shows that \(\phi_k\) transforms the duplicated word into the same prefix \(a\) and derivative tail obtained from \(b\) by inserting \(k\) zeros at the gap after the first \(p\) derivative symbols, where \(0\le p\le m\). This is also the standard derivative lemma of Jain, Farnoud, Schwartz, and Bruck. Such an insertion acts on exactly one zero run, replacing \(r_i\) by \(r_i+k\), leaving \(a\) and the ordered nonzero skeleton \((w_1,\ldots,w_s)\) unchanged.

**Exact adjacency.** Two distinct source words \(x,y\) can have a common descendant only when their derivative prefixes and nonzero skeletons agree. For the two respective zero-run vectors \(r,t\), a common descendant means
\[
r+k e_i=t+k e_j
\]
for some indices \(i,j\). Since the words differ, \(i\ne j\). Thus \(t-r=k(e_i-e_j)\), with the donor coordinate nonnegative after subtraction. Conversely, any such legal transfer yields a common descendant, by inserting a block of \(k\) zeros into run \(i\) of one tail and run \(j\) of the other. Consequently, the residues \(r_i\bmod k\) are invariant under an edge, and, after writing \(r_i=\rho_i+k u_i\) with \(0\le\rho_i<k\), edges move exactly one unit of the vector \(u\) between two distinct positions.

**Upper bound.** Every edge transfers one unit between positions \(i\ne j\), so \(\kappa\) changes by \(i-j\pmod d\). Because \(0\le i,j<d\), this difference is nonzero modulo \(d\). When \(\sum_i u_i=0\), there are no possible donors and the word is isolated. When \(\sum_i u_i>0\), the tail has at least \(k\) zeros, hence \(m=s+\sum_i r_i\ge s+k\), which gives \(d=s+1\le n-2k+1\). Thus \(\kappa\) is a proper coloring using at most \(K=\max(1,n-2k+1)\) globally shared colors, even though different invariant components have different values of \(d\). This proves \(\chi\le K\).

**Sharp clique.** If \(n\le2k\), an adjacent pair would require a nonzero skeleton of length at least one together with a donor zero run of length at least \(k\), hence derivative length at least \(k+1\). But \(m=n-k\le k\), so no edges exist and \(\chi=\omega=1\). Now suppose \(n\ge2k+1\), put \(s=n-2k\ge1\), and fix the same derivative prefix \(a=0^k\) for all vertices. Fix the nonzero skeleton \(w_1=\cdots=w_s=1\). For each index \(j\in\{0,\ldots,s\}\), take the unique source word whose derivative has exactly \(k\) zeros in zero run \(j\) and no other zeros. The \(s+1=K\) words are distinct. Each two differ by one transfer of the entire block of \(k\) zeros; they have a common one-duplication descendant obtained by inserting \(k\) zeros into the opposite run. Therefore these vertices form a \(K\)-clique. Hence \(\omega\ge K\), and \(\omega\le\chi\le K\), proving both equalities.

The lower-bound argument is an explicit **all-pairs clique witness**, not a finite computational extrapolation. The upper bound is a **global coloring**, not a componentwise coloring with independently named palettes. Both arguments hold for every quantified value of \(q,k,n\).

## Verification
The standalone `check_direct.py` enumerates word-level descendant sets, constructs all pairs of source words with a shared descendant, checks the proposed coloring for every edge, and constructs and tests the prescribed clique. It covers all eligible small cases for \(q\in\{2,3\}\), \(k\in\{1,2,3\}\), and lengths up to the script's stated finite bounds, including the edgeless boundary. The independent `verify_components.py` exhaustively checks \(72\) integer-composition graphs with \(1\le d\le8\) and \(0\le B\le8\): the modular coloring separates all unit-transfer edges and a sharp clique uses all \(d\) colors when \(B\ge1\). Both scripts use only the Python standard library and terminate with explicit `VERIFY_*_OK` markers on success. Their finite tests corroborate the all-length proof; they are not the reason it is valid.

Run using `python3 check_direct.py` and `python3 verify_components.py` from any directory, with Python 3. The scripts are separately embedded with this result.

## Relationship to prior work
Jain, Farnoud, Schwartz, and Bruck's 2016 paper introduced and analyzed the same fixed-length tandem-duplication channel and the derivative/zero-run reduction. That foundational reduction is assumed, explicitly rederived, and not claimed as new. The new claim is the sharp **global vertex coloring and matching clique**, equivalently an exact minimal partition into one-error-correcting codebooks for every alphabet and every legal length.

An existing exact-edge-count result for this very confusability graph determines the total number of confusable pairs and proves uniqueness of their common descendants. Its edge-count theorem does not give a chromatic or clique number, and no graph-theoretic implication from that count determines the present claim. The 2015 simplicial rook graph article studies vectors of fixed coordinate sum with adjacency whenever **any positive number of units** is transferred between two positions; the present invariant components use only **one-unit** transfers. A result about the larger graph's spectrum or maximum clique therefore does not establish this coloring of the smaller graph.

Earlier repetition-error correction work and later duplication-correcting constructions are important precedence risks. Accessible literature and published-result searches did not locate the exact global equality or this sharp coloring, but the absence of a search hit is not a proof of priority.

## Limitations
This concerns exactly one **fixed-length** tandem duplication. It does not assert analogous colorings for variable duplication lengths, noisy duplication, multiple duplications, or different editing channels. A minimum number of codebooks is not the maximum size of a single code, and the theorem does not establish an optimal independent-set size, a superior coding rate to existing schemes, or an independently certified novelty claim. An inaccessible full text of an earlier repetition-coding source and unindexed prior work remain historical-priority risks.

## References
1. S. Jain, F. Farnoud, M. Schwartz, and J. Bruck, “Duplication-Correcting Codes for Data Storage in the DNA of Living Organisms,” first public arXiv posting 2016-06-01, arXiv:1606.00397v1, https://arxiv.org/abs/1606.00397.
2. L. Dolecek and V. Anantharam, “Repetition Error Correcting Sets: Explicit Constructions and Prefixing Methods,” SIAM Journal on Discrete Mathematics, 2010, https://doi.org/10.1137/080730093 (full text not verified in the present review).
3. A. E. Brouwer, S. M. Cioabă, W. H. Haemers, and J. R. Vermette, “Notes on simplicial rook graphs,” 2015, https://doi.org/10.1007/s10801-015-0633-y.
4. “Exact confusability edge count for one fixed-length tandem duplication,” 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-confusability-edge-count-for-one-fixed-length-tandem-dupli--c5496661aaac.
