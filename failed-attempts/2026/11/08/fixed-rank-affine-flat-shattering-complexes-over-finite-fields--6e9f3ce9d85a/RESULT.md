# Fixed-rank affine-flat shattering complexes over finite fields

## Finding

Fix a prime power \(q\), an integer \(d\ge1\), and an integer \(0\le k<d\). Put \(V=\mathbb F_q^d\), and let \(\mathcal A_{q,d,k}\) be the set system on the points of \(V\) consisting of **all affine \(k\)-flats** \(a+W\), where \(W\le V\) has linear dimension exactly \(k\). Each hypothesis is the membership indicator of one flat; no unions of flats, empty hypothesis, or flats of other dimensions are included.

**Theorem (complete supports, counts, and adaptive rank).** A finite point set \(S\subseteq V\) is VC-shattered by \(\mathcal A_{q,d,k}\) if and only if \(S\) is affinely independent and \(|S|\le k+1\). Thus the entire complex of shattered supports is the rank-\((k+1)\) truncation of the affine-geometry matroid independence complex. Writing \(s_m\) for the number of distinct unordered shattered \(m\)-point supports, its exact generating polynomial is

\[
\Phi_{q,d,k}(z)=1+\sum_{m=1}^{k+1}
\frac{q^d\prod_{i=0}^{m-2}(q^d-q^i)}{m!}z^m.
\]

The product for \(m=1\) is empty and equals one. In particular,

\[
\operatorname{VCdim}(\mathcal A_{q,d,k})=
\operatorname{Ldim}(\mathcal A_{q,d,k})=k+1.
\]

There is an additional exact conditional interpretation. For every affinely independent set \(T\subseteq V\) of size \(1\le t\le k+1\), restrict the class to those \(k\)-flats containing **every** point of \(T\), but retain the original point-query domain \(V\). The residual class has Littlestone dimension exactly \(k+1-t\). The unrestricted case has dimension \(k+1\), and this positive-evidence rank drops by precisely one whenever an additional affinely independent positive point is learned.

## Assumptions and scope

Here an affine \(k\)-flat is a coset of a \(k\)-dimensional linear subspace over \(\mathbb F_q\), not a real affine half-space and not a union of arbitrary lower-dimensional flats. A point set \(\{x_1,\ldots,x_m\}\) is affinely independent when the \(m-1\) vectors \(x_2-x_1,\ldots,x_m-x_1\) are linearly independent. The empty point set is declared affinely independent. VC-shattering means that for every \(B\subseteq S\) there exists a hypothesis \(H\in\mathcal A_{q,d,k}\) with \(H\cap S=B\). The Littlestone dimension is the largest depth of a fully shattered binary point-query tree, with a distinct fixed hypothesis permitted at each leaf.

The parameter restriction \(k<d\) is essential. For \(k=d\), the class contains only \(V\), has zero VC and Littlestone dimensions, and shatters only the empty support. Every prime power is allowed, including characteristic two and nonprime fields. Counting uses unordered supports, not ordered tuples.

## Proof

**1. Necessary affine independence.** Suppose \(S\) is affinely dependent. There is a point \(x\in S\) that lies in the affine span of \(S\setminus\{x\}\): take a minimal affine dependence and solve for a coefficient that is nonzero. Every affine flat that contains \(S\setminus\{x\}\) must then contain \(x\). Consequently the labeling positive on all of \(S\setminus\{x\}\) and negative on \(x\) is impossible. Thus a shattered support is affinely independent. Also, a \(k\)-flat cannot contain more than \(k+1\) affinely independent points, so shattering requires \(|S|\le k+1\).

**2. Sufficiency.** It is enough to shatter each affinely independent set of exactly \(k+1\) points; every smaller affinely independent set can be extended to such a set because \(d\ge k+1\). Fix one such set \(S\) and a desired positive trace \(B\subseteq S\). If \(B=\varnothing\), the affine hull of \(S\) is a \(k\)-flat and has a distinct parallel coset because \(d>k\). That coset misses \(S\).

If \(B\ne\varnothing\), select \(a\in B\). The difference vectors \(s-a\) for \(s\in S\setminus\{a\}\) are linearly independent. Assign a linear functional \(\lambda:V\to\mathbb F_q\) value zero on \(s-a\) for \(s\in B\setminus\{a\}\), and value one on \(s-a\) for \(s\in S\setminus B\); extend these prescriptions linearly to all of \(V\). If \(S\setminus B\) is nonempty, \(\lambda\) is nonzero and \(\ker\lambda\) is a hyperplane; otherwise take \(\lambda=0\). The span \(U\) of the positive differences lies in \(\ker\lambda\) and has dimension \(|B|-1\le k\). In the nonzero-functional case \(\ker\lambda\) has dimension \(d-1\ge k\); in the zero case \(\dim V=d>k\). Choose a \(k\)-dimensional subspace \(W\) with \(U\subseteq W\subseteq\ker\lambda\). Then \(a+W\) includes exactly the selected positive points of \(S\), since every excluded point has functional difference value one. All \(2^{k+1}\) traces occur, proving the characterization.

**3. Count every support.** To choose an ordered affinely independent \(m\)-tuple \((x_1,\ldots,x_m)\), there are \(q^d\) options for \(x_1\). After the first point, the next difference \(x_j-x_1\) must lie outside the span of the previous \(j-2\) difference vectors, a space of size \(q^{j-2}\). Hence the ordered count for \(1\le m\le k+1\) is \(q^d\prod_{i=0}^{m-2}(q^d-q^i)\). Dividing by \(m!\) yields exactly the stated coefficients; no other supports are shattered.

**4. Online upper bound.** First consider the Boolean class \(\mathcal U_{D,r}\) of all \(r\)-dimensional *linear* subspaces of an arbitrary \(D\)-dimensional vector space, with point-membership queries, where \(0\le r<D\). We prove \(\operatorname{Ldim}(\mathcal U_{D,r})\le r\) by induction on \(r\). For \(r=0\) there is only the zero subspace. For \(r\ge1\), a query at the zero vector has a constant positive answer. For any nonzero query \(v\), the positive hypotheses are exactly the \(r\)-spaces containing \(\langle v\rangle\); after taking the quotient by \(\langle v\rangle\), their remaining membership concepts are the \((r-1)\)-spaces of a \((D-1)\)-space. By induction this positive branch has Littlestone dimension at most \(r-1\). A fully shattered depth-\((r+1)\) tree would require at least depth \(r\) in **both** branches following its root, which is impossible. This proves the linear upper bound.

For affine \(k\)-flats, every root query at a point \(a\) has positive hypotheses \(a+W\) for all \(k\)-spaces \(W\), identified by translation with \(\mathcal U_{d,k}\). This positive branch has Littlestone dimension at most \(k\); therefore the unrestricted class has dimension at most \(k+1\). Since its VC dimension already equals \(k+1\), a fixed shattered support gives a complete (level-balanced) mistake tree of that depth. The two dimensions coincide.

**5. Conditional online rank.** If \(T=\{a,x_2,\ldots,x_t\}\) is affinely independent and all its points are required to be positive, put \(U=\operatorname{span}\{x_i-a:2\le i\le t\}\). The allowed \(k\)-flats are exactly \(a+W\) for \(W\supseteq U\), and quotienting by \(U\) identifies the hypothesis class with all \((k-t+1)\)-dimensional linear subspaces of \(V/U\). The linear bound gives at most \(k-t+1\). Conversely, complete \(T\) to an affinely independent set \(T\cup R\) of cardinality \(k+1\). The trace construction in Step 2 realizes every labeling on \(R\) while keeping all of \(T\) positive, giving VC, hence Littlestone, dimension at least \(|R|=k+1-t\). Equality follows. No claim is made for arbitrary mixed positive-negative transcripts.

## Verification

The standalone file `verify_affine_flats.py` constructs vector spaces and all affine flats directly, computes the Boolean traces on every support of the tested sizes, and compares each outcome to an independent Gaussian-elimination test for affine independence and the coefficient formula. It also calculates the exact Littlestone dimension by the minimax recurrence when the enumerated concept families are small enough. Test cases include prime fields and a genuine extension field of order four. The script needs only Python's standard library and runs with `python3 verify_affine_flats.py`. Its actual recorded output is embedded in `verification_output.txt`.

These finite tests are not an exhaustive proof for unbounded \(q,d,k\); Steps 1–5 give the general proof. Higher-support enumeration is exhaustive only for test cases flagged as such in the executable. The standalone script reconstructs flats afresh and never reads the coefficient formula as a substitute for incidence traces.

## Relationship to prior work

Pradeep, Nachum and Gastpar (arXiv:2206.13257v1, first public 2022-06-27), in Example 1 and Section VI, discuss indicators of affine subspaces over a real vector space and explicitly state Littlestone dimension \(d+1\) for the at-most-dimension family they introduce. Consequently the numerical online-rank formula for affine subspaces must **not** be presented as an entirely new phenomenon. Their setting and claimed results do not state the coefficientwise VC-shattering polynomial or the full characterization of point supports for the restricted class of exactly-\(k\)-dimensional affine flats over finite fields.

Guingona, Kolesnikov, Nierwinski and Soucy (arXiv:2109.04805v1, first public 2021-09-10), Theorem 3.10, establish VC and Littlestone dimensions of nontrivial linear-combination zero-set families over any field. That is a broad hyperplane-type family, not the all-fixed-rank affine-flat incidence system; its theorem does not supply the coefficients of the finite-field shattering polynomial for every \(k\).

Counting affinely independent point sets is classical finite-matroid combinatorics and **is not claimed as a new counting technique**. In particular, Kordecki (2000) studies the probabilities of ranks of random subsets of finite affine geometries, which may contain equivalent numerical coefficient data under rank terminology. The complete VC-shattering interpretation (every support, not just its size) and its joint relation to the fixed-rank online class are the focused findings. The Kordecki article notice and abstract were accessible but the linked primary text was not; that is a residual priority and numerical-overlap risk, not evidence of a novel count. No claim of independent review or comprehensive priority certification is made.

## Limitations

The theorem treats **all** affine flats of one exact rank on the full point domain of a finite vector space; it does not treat arbitrary field subsets, projective flats, arbitrary unions, non-field chain rings, or incomplete collections of flats. The conditional assertion applies only to constraints that points of one affinely independent set are positive. Historical originality beyond the checked sources remains uncertain, especially for the matroid-rank enumeration and terminology describing shattering complexes. The finite verification is supplementary, and an independent scientific audit has not been performed.

## References

1. A. Pradeep, I. Nachum and M. Gastpar, *Finite Littlestone Dimension Implies Finite Information Complexity*, arXiv:2206.13257v1 (first posted 2022-06-27), Example 1 and Section VI. https://arxiv.org/abs/2206.13257
2. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-Dimension of Families of Zero Sets*, arXiv:2109.04805v1 (first posted 2021-09-10), Theorem 3.10. https://arxiv.org/abs/2109.04805
3. W. Kordecki, *On the Rank of Random Subsets of Finite Affine Geometry*, *Discussiones Mathematicae Graph Theory* 20 (2000), 209–217; notice and abstract accessible at https://geodesic.mathdoc.fr/item/DMGT_2000_20_2_a4/ (primary full text not inspected).
