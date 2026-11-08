# All optimal binary weight-two single-grain codes

## Finding

A one-grain code uses the overwrite channel of Gabrys, Yaakobi and Dolecek (2013): on an indexed binary word of length \(n\), either nothing changes or one position \(j\), with \(1\le j<n\), takes the previous bit's value. Let \(A_{2,G}(n)\) be the largest size of a code consisting only of length-\(n\), Hamming-weight-two words, with pairwise disjoint received-word sets. Then

\[
A_{2,G}(n)=\begin{cases}1,&n=2,\\2,&n=3,\\n,&n\ge4.\end{cases}
\]

For every \(n\ge4\), the number of *indexed, labeled-position* optimal codebooks is precisely \((n-3)^2\), and the following are *all* of them. Identify a word with its unordered set of two one-positions in \(\{0,\ldots,n-1\}\). For an integer \(r\) with \(3\le r\le n-1\), put

\[
C_{r,*}=\bigl\{\{i,i+1\}:0\le i\le n-2\bigr\}\cup\bigl\{\{0,r\}\bigr\}.
\]

For any further integer \(j\) with \(4\le j\le n-1\), put

\[
C_{r,j}=\bigl(C_{r,*}\setminus\{\{j-1,j\}\}\bigr)\cup\{\{1,j\}\}.
\]

There are \(n-3\) choices of \(r\), and \(n-3\) choices of the second parameter (\(*\) or \(j=4,\ldots,n-1\)); all the resulting codebooks are distinct.

## Assumptions and scope

Only *one or zero* smearing errors are allowed, never two. The first bit, position \(0\), is not overwritten. For each support pair \(P\), let \(x(P)\in\{0,1\}^{n}\) be its indicator word, and define the received ball

\[
B_n(P)=\{x(P)\}\cup\{x(P)\oplus e_j:1\le j<n,\ x(P)_j\ne x(P)_{j-1}\}.
\]

A code is valid precisely when its balls are disjoint for distinct supports. There is no cyclic boundary, symbol relabeling, position permutation, Hamming-distance assumption, or use of overlapping errors in the claim. For \(n=2\) the only support is \(\{0,1\}\); at \(n=3\), two supports can coexist but all three cannot.

## Proof

**Singleton descendants.** For \(P=\{a,b\}\), \(0\le a<b<n\), write \(U(P)\subseteq\{0,\ldots,n-1\}\) for those positions whose one-hot words lie in \(B_n(P)\). Directly from the allowed overwrite operations,

\[
U(\{a,b\})=\begin{cases}
\varnothing,&(a,b)=(0,1),\\
\{0\},&a=0,\ b\ge2,\\
\{b\},&a\ge1,\ b=a+1,\\
\{a,b\},&a\ge1,\ b\ge a+2.
\end{cases}
\]

Hence every codeword except \(\{0,1\}\) has one or two singleton descendants. The singleton \(\{1\}\) can arise *only* from a two-descendant pair \(\{1,b\}\) with \(b\ge3\). Disjoint error balls imply that the sets \(U(P)\) for different codewords are pairwise disjoint.

**Upper bound.** In a code of size \(m\), let \(z\in\{0,1\}\) record whether \(\{0,1\}\) belongs to it, and let \(d\) count its codewords with two singleton descendants. Then all other words contribute exactly one singleton, so the number of distinct singleton descendants is \(m-z+d\), at most \(n\). If \(d=0\), singleton \(\{1\}\) is absent, whence \(m-z\le n-1\). Therefore \(m\le n\) in either case (if \(d\ge1\), use \(m-z+d\le n\)).

**Equality classification.** Suppose \(m=n\). The singleton accounting forces \(z=1\), and then \(d\le1\). If \(d=0\), the other \(n-1\) codewords must use each singleton in \(\{0,2,3,\ldots,n-1\}\) once. Their unique possible forms are \(\{0,r\}\) and \(\{k-1,k\}\), for \(2\le k<n\), plus \(\{0,1\}\). The choice \(r=2\) is impossible because \(B_n(\{0,2\})\) and \(B_n(\{0,1\})\) both contain the word supported on \(\{0,1,2\}\); hence \(3\le r\le n-1\), giving \(C_{r,*}\).

If \(d=1\), the singleton accounting uses all \(n\) singleton words. The unique two-descendant codeword must contain singleton \(\{1\}\), hence is \(\{1,j\}\), \(j\ge3\). All other nonexceptional words are forced to be \(\{0,r\}\) and the adjacent supports \(\{k-1,k\}\) for \(2\le k<n\), \(k\ne j\). The choice \(j=3\) is impossible: \(\{1,3\}\) and the necessarily present \(\{1,2\}\) both produce support \(\{1,2,3\}\). Again \(r=2\) is impossible because of its collision with \(\{0,1\}\). Thus \(j\ge4\), \(r\ge3\), giving exactly \(C_{r,j}\).

**Achievability and absence of remaining collisions.** In each displayed code, all singleton descendants are disjoint. For weight-two inputs, the only possible other nontrivial descendants have weight three: adjacent support \(\{i,i+1\}\) creates the consecutive triple \(\{i,i+1,i+2\}\) (when in range); \(\{0,r\}\) with \(r\ge3\) creates only \(\{0,1,r\}\) and possibly \(\{0,r,r+1\}\); \(\{1,j\}\) with \(j\ge4\) creates only \(\{1,2,j\}\) and possibly \(\{1,j,j+1\}\). All these triples are pairwise distinct among words in a proposed code: the first class is consecutive, the second contains zero but is nonconsecutive, and the third contains one but no zero and is nonconsecutive. An unchanged weight-two output identifies its own input. Thus every listed code is valid and has \(n\) members. Distinct \(r,j\) choices produce distinct support collections. Finally, direct inspection at \(n=2,3\) gives the exceptional optima. This proves the theorem.

## Verification

The independent standard-library script `verify.py` reconstructs every received ball from bit operations, checks disjointness and size for the complete constructed family through length \(30\), and checks representative larger constructions through length \(512\). It enumerates all maximal independent sets of the exact confusion graph for \(2\le n\le10\), without using the proof's singleton argument, and confirms the optima and all extremizers. The checker prints `VERIFY_OK`. This enumeration is a finite check; the all-length result follows from the proof above.

## Relationship to prior work

Gabrys, Yaakobi and Dolecek (2013, arXiv:1307.7087) define the grain overwrite model and obtain unrestricted code bounds and constructions. Kashyap and Zémor (2013, arXiv:1302.6154) give broader unrestricted-code upper bounds. Neither inspected text gives the stated constant-weight-two capacity and extremal-code classification. A published finite census of unrestricted six-bit single-grain codes addresses a different universe: it does not determine optimal subcodes restricted to Hamming weight two, let alone classify them for all lengths. The present result uses the same grain channel but specializes to the natural two-one support layer. Publication priority remains subject to discovery of unindexed equivalent formulations.

## Limitations

The claim concerns only a single grain overwrite and fixed weight exactly two; it does not determine general constant weights, unrestricted maximum code sizes, multiple grain errors, or cyclic media. The theorem is mathematically proved in the stated indexing convention but has not undergone independent external mathematical audit. Search-based originality assessment is necessarily incomplete.

## References

- R. Gabrys, E. Yaakobi and L. Dolecek, *Correcting Grain-Errors in Magnetic Media*, arXiv:1307.7087 (first publicly posted 2013-07-26), Sections II–VI. https://arxiv.org/abs/1307.7087
- N. Kashyap and G. Zémor, *Upper Bounds on the Size of Grain-Correcting Codes*, arXiv:1302.6154 (first publicly posted 2013-02-25). https://arxiv.org/abs/1302.6154
