# Fixed-weight cyclic independent sets: a one-logarithm online boundary effect

## Finding
For every integer \(n\ge3\) and \(0\le k\le\lfloor n/2\rfloor\), let \(\mathcal I^\circ_{n,k}\) be the Boolean concept class consisting of the vertex-incidence vectors of all independent sets of size exactly \(k\) on the labelled cycle \(C_n\). Put \(r=n-2k\). Then
\[
\operatorname{VCdim}(\mathcal I^\circ_{n,k})=\min\{k,r+1\}.
\]
For \(k\ge1\) and \(r\ge1\), let nonnegative integers \(b_1,\ldots,b_r\) sum to \(k\), with pairwise differences at most one. There are explicit online mistake trees yielding
\[
\sum_{i=1}^{r}\lfloor\log_2(b_i+1)\rfloor
\ \le\ \operatorname{Ldim}(\mathcal I^\circ_{n,k})
\ \le\ \left\lfloor\log_2\left(\frac{n}{n-k}\binom{n-k}{k}\right)\right\rfloor.
\]
Consequently, for each fixed \(r\ge1\), as \(k\to\infty\) along \(n=2k+r\),
\[
\operatorname{VCdim}(\mathcal I^\circ_{2k+r,k})=r+1\quad(k\ge r+1),
\qquad \operatorname{Ldim}(\mathcal I^\circ_{2k+r,k})=r\log_2 k+O_r(1).
\]
For \(r=0\), the two alternating independent sets give \(\operatorname{VCdim}=\operatorname{Ldim}=1\) (necessarily \(k\ge2\)); for \(k=0\), both dimensions are zero. Relative to the fixed-weight independent-set class on the path with the **same** \(n=2k+r\), the VC dimensions coincide but, for every fixed \(r\ge1\), the path's online dimension is \((r+1)\log_2 k+O_r(1)\). Closing a path into a cycle thus removes exactly one logarithmic degree of online freedom.

## Assumptions and scope
Vertices of \(C_n\) are \(0,1,\ldots,n-1\), with indices modulo \(n\). An independent set contains no consecutive vertices. A finite set of vertex queries is VC-shattered when every binary assignment is realized by some concept. Littlestone dimension is the greatest depth of a complete binary tree whose internal nodes are vertex queries, all root-to-leaf label sequences being realized by concepts. The asymptotic notation \(O_r(1)\) holds with \(r\) fixed, and makes no uniform claim when \(r\) grows with \(k\).

## Proof
**1. Counting available slack.** For the binary incidence word \(x_0\cdots x_{n-1}\) of an independent set with \(k\) ones, no cyclic adjacent pair is \(11\). Exactly \(2k\) cycle edges touch a one, so exactly \(r=n-2k\) cycle edges are \(00\). This identity is exact, including the alternating boundary case \(r=0\).

**2. VC upper bound.** Any shattered set \(S\) of \(t\) vertices must be independent, because the all-one labeling must be realizable, and hence \(t\le k\). List the queried vertices cyclically and let the successive positive edge distances be \(d_1,\ldots,d_t\), summing to \(n\). For prescribed queried bits \(a_1,\ldots,a_t\), write \(\delta_i\in\{0,1\}\) for the parity of \(d_i-(a_i\oplus a_{i+1})\), with cyclic subscripts. If a realizing word has \(c_i\) edges of type \(00\) on the \(i\)-th segment, then \(c_i\equiv\delta_i\pmod2\), because every other edge switches its bit. Thus \(r=\sum c_i\ge\sum\delta_i\).

As the query labels vary, the possible vectors \((\delta_1,\ldots,\delta_t)\) are *precisely* the binary vectors of parity \(n\bmod2=r\bmod2\). One direction follows by telescoping the XORs; for the other, prescribe one initial query label and recursively determine the rest. Hence the maximum \(\sum\delta_i\) over assignments is \(t\) if \(t\equiv r\pmod2\) and \(t-1\) otherwise. If \(t\ge r+2\), this maximum exceeds \(r\). Such a support cannot be shattered. This proves \(t\le\min\{k,r+1\}\). The case \(t=1\) follows from the same parity argument or directly.

**3. A VC witness for every parameter pair.** Suppose \(k\ge1\) and let \(t=\min\{k,r+1\}\). Query \(S=\{0,2,\ldots,2(t-1)\}\). For arbitrary bits \(a_0,\ldots,a_{t-1}\), fill each short two-edge segment between consecutive queried positions as \(101\) for endpoints \(11\), \(010\) for endpoints \(00\), \(100\) for endpoints \(10\), or \(001\) for endpoints \(01\). These segments use exactly \(m\) edges of type \(00\), where \(m\) is the number of changes between consecutive queried labels, so \(m\le t-1\le r\).

The remaining closing segment has length \(L=n-2(t-1)\ge r+2\), endpoints \(a_{t-1},a_0\), and must contain exactly \(c=r-m\) edges of type \(00\). Its parity is compatible because \(L-c\equiv a_{t-1}\oplus a_0\pmod2\). Also \(L-c\ge2\). For any two endpoint bits and any integer \(c\) with these properties, such a segment exists: take an alternating sequence of \(L-c\) changing edges between those endpoints, which visits zero, and insert \(c\) additional \(00\) edges at a zero. This gives a cyclic word with precisely \(r\) zero-zero edges, no \(11\), and therefore exactly \(k=(n-r)/2\) ones. It realizes the prescribed labels. Hence the proposed support is shattered and the VC bound is attained.

**4. Size of the class and online upper bound.** For \(k\ge1\), independently mark one of the \(k\) selected vertices. The \(k\) positive gaps of zeros around the circle are each at least one and sum to \(n-k\). The resulting marked count is \(n\binom{n-k-1}{k-1}\), whence
\[
|\mathcal I^\circ_{n,k}|=\frac{n}{k}\binom{n-k-1}{k-1}
=\frac{n}{n-k}\binom{n-k}{k}.
\]
Every complete mistake tree of depth \(d\) requires \(2^d\) distinct concepts; taking logarithms gives the stated upper bound.

**5. Independent online threshold blocks.** For \(r\ge1\), partition \(k=b_1+\cdots+b_r\). In block \(i\), for every \(j\in\{0,\ldots,b_i\}\) choose the word
\[
(10)^j\,0\,(10)^{b_i-j}
\]
of length \(2b_i+1\). Concatenating the \(r\) blocks produces a cyclic independent-set word: all block endings are zero, no block begins with adjacent ones, the length is \(2k+r=n\), and the weight is \(k\). At the local coordinate \(2q\), for \(0\le q<b_i\), the bit is one exactly when \(j>q\). Thus each block contains a threshold class on the ordered \(b_i+1\) values of \(j\), with Littlestone dimension \(\lfloor\log_2(b_i+1)\rfloor\). Querying the blocks sequentially produces a complete online tree whose depth is the sum of those dimensions. Balancing the \(b_i\)'s proves the explicit lower bound.

**6. Asymptotic separation.** At fixed \(r\ge1\), the lower bound equals \(r\log_2 k-O_r(1)\) and the counting upper bound equals \(r\log_2 k+O_r(1)\), since \(\binom{k+r}{r}=\Theta_r(k^r)\). For the path \(P_{2k+r}\), the number of independent \(k\)-sets is \(\binom{k+r+1}{r+1}=\Theta_r(k^{r+1})\). Conversely, concatenate \(r+1\) independent threshold blocks of the form in Step 5, with the \(b_i\) summing to \(k\), and delete the final zero. This yields words of length \(2k+r\) and \(k\) nonadjacent ones on the path while preserving all threshold queries. Balanced blocks give a depth \((r+1)\log_2 k-O_r(1)\) online tree, so the exact path leading coefficient is \(r+1\). The path VC dimension also equals \(\min\{k,r+1\}\). Indeed, pad a path incidence word by a zero at both ends: among its \(n+1\) edges exactly \(r+1\) are \(00\). For any \(t\) queried vertices, the \(t+1\) segment mismatch bits between consecutive queried positions and the two fixed-zero boundaries run over precisely the binary vectors of parity \(r+1\bmod2\) as query labels vary. Their maximum possible weight exceeds \(r+1\) whenever \(t\ge r+2\), so \(t\le r+1\); the all-one labeling also forces \(t\le k\). Every cyclic independent set is a path independent set, so the cycle VC witness in Step 3 attains this upper bound for paths as well. Thus closing the path leaves VC dimension unchanged while reducing its online leading coefficient by one.

## Verification
Run the standard-library Python file `check_cycle_learning.py`. The executable enumerates all independent sets for small cycles, computes exact VC dimensions from all support traces, checks the closing-segment witness for every prescribed label assignment in its range, evaluates exact recursive Littlestone dimensions for small lengths, and verifies the product-threshold block construction over additional parameters. Recorded output:

`FIXED_WEIGHT_CYCLE_LEARNING_PASS 45 32 284 203`

The four integers count finite VC tests, finite online tests, constructed labelings, and independent-block parameter tests. These experiments corroborate but do not establish the unrestricted formulas; the unrestricted arguments are in the preceding proof.

## Relationship to prior work
The ordinary independence polynomial and its coefficients for paths and cycles were studied by Beaton, Brown and Cameron (2018). In particular, their cycle independence polynomial supplies counting context, not a VC or online shattering theorem. General model-theoretic and online-learning dimensions appear in the work of Malliaris and Moran (2021) and in Guingona, Kolesnikov, Nierwinski and Soucy (2021); the latter concerns zero sets of linear combinations, not fixed-weight independent sets of cycles. The path comparison is proved directly here by a separate count and block construction. A previously derived cyclic-window formula covers the special case \(r=1\) after a relabeling. Neither special case implies the new sharp coefficient \(r\) for every fixed \(r\ge2\). The elementary exact class-count formula itself is not claimed as new.

## Limitations
The exact Littlestone dimension of \(\mathcal I^\circ_{n,k}\) at arbitrary individual pairs \((n,k)\) is not determined. No all-coefficient shattering polynomial is claimed. The online asymptotic holds only with \(r\) fixed. Search-based originality assessment cannot rule out priority under cyclic-word, hard-core-model, or learning-theoretic alternative terminology. No independent mathematical validation has been performed.

## References
1. I. Beaton, J. I. Brown, B. Cameron, *Independence Equivalence Classes of Paths and Cycles*, arXiv:1810.05317v1, first public 2018-10-12, https://arxiv.org/abs/1810.05317.
2. M. Malliaris, S. Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569v1, first public 2021-08-12, https://arxiv.org/abs/2108.05569.
3. V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1, first public 2021-09-10, https://arxiv.org/abs/2109.04805.
