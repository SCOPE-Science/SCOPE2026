# Parking-preference shattering is exactly partial parking: a pure nonmatroidal complex

## Finding

For an integer \(n\ge 1\), let \(\mathrm{PF}_n\subseteq[n]^n\) be the classical parking functions: a word is valid when its nondecreasing rearrangement \(b_1\le\cdots\le b_n\) obeys \(b_i\le i\) for every \(i\). Regard each \(a\in\mathrm{PF}_n\) as the Boolean incidence concept on \(Q_n=[n]\times[n]\) given by \(h_a(i,j)=[a_i=j]\).

**Theorem.** A query support \(S\subseteq Q_n\) of size \(s\) is VC-shattered by \(\{h_a:a\in\mathrm{PF}_n\}\) if and only if all of the following hold:

1. \(s\le n-1\);
2. the row coordinates \(i\) appearing in \(S\) are pairwise distinct;
3. the \(s\) queried target values, arranged in nondecreasing order \(j_{(1)}\le\cdots\le j_{(s)}\), satisfy \(j_{(r)}\le n-s+r\) for every \(1\le r\le s\).

The empty support satisfies these conditions by convention. Condition 3 says exactly that the target list is a **partial parking function** for \(s\) cars on \(n\) spots, in the classical one-way linear parking rule.

The complete face polynomial of the shattering complex \(\Delta_n\) is
\[
\Phi_n(z)=\sum_{s=0}^{n-1}\binom ns(n+1-s)(n+1)^{s-1}z^s
=(1+z)(1+(n+1)z)^{n-1}-(n+1)^{n-1}z^n.
\]
The \(s=0\) summand is understood to equal one. Hence \(\operatorname{VCdim}=n-1\) for every \(n\ge1\); the complex is pure of dimension \(n-2\) for \(n\ge2\), with exactly \(2n(n+1)^{n-2}\) facets. Its reduced Euler characteristic, defined from the augmented face polynomial, is
\[
\widetilde\chi(\Delta_n)=(-1)^n(n+1)^{n-1}.
\]
Despite this purity, \(\Delta_n\) is **not** a matroid independence complex for any \(n\ge3\). It *is* a matroid independence complex for \(n=1,2\).

## Assumptions and scope

The locations \([n]\) are labeled positions of the arriving cars; the values \([n]\) are their preferred parking spots, not necessarily where their cars eventually park. Queries are **equality predicates on preferences**, not questions about final occupancy, outcome permutations, or displacement. All Boolean patterns on a support must be realized by possibly different parking functions. The property of being a partial parking function is invariant under permutations of the selected rows.

## Proof

**Lemma 1: partial parking criterion.** For \(0\le s\le n\), an \(s\)-tuple \(p\in[n]^s\) is a successful preference sequence for \(s\) cars on a street of \(n\) spaces if and only if its sorted values satisfy \(p_{(r)}\le n-s+r\) for each \(r\le s\). Equivalently, appending \(n-s\) entries equal to \(1\) produces a classical parking function of length \(n\). The criterion follows directly from the familiar sorted-preference characterization of linear parking; it is included here to fix the normalization. The empty tuple is successful.

**Necessity.** Suppose \(S\) is shattered. Its queries cannot share a row: two distinct target-equality predicates in one row cannot both be true. Hence \(s\le n\). Realizing the all-positive labeling of \(S\) produces a classical parking function agreeing with all queried targets. Replacing the unqueried preferences by \(1\) decreases entries, so the resulting word is also a parking function (coordinatewise downward closure). By Lemma 1, its queried target list is a partial parking function on \(n\) spots.

If \(s=n\), the all-positive labeling forces a classical parking function and therefore contains at least one target \(1\). Now prescribe false to every query with target \(1\), and true to every query with target greater than \(1\). This pattern would force every car to prefer a value greater than \(1\), contradicting the necessary existence of a preferred \(1\) in any classical parking function. Thus \(s\le n-1\).

**Sufficiency.** Assume conditions 1–3, with \(s\le n-1\). Fix an arbitrary Boolean labeling on \(S\). For a queried row whose target is \(j\), assign preference \(j\) if the label is true; otherwise assign \(1\) when \(j>1\), or \(2\) when \(j=1\). Assign \(1\) to every unqueried row. These choices realize precisely the prescribed equality labels. The word constructed from the targets \(j\) and \(n-s\) additional ones is a classical parking function by Lemma 1. For the chosen labeling, all substituted entries are bounded above by \(\max(2,j)\). Replacing every target \(1\) by \(2\) still satisfies the partial parking inequalities because their first right-hand side is \(n-s+1\ge2\): in sorted order, \(\max(2,j_{(r)})\le\max(2,n-s+r)=n-s+r\). The labeling word is coordinatewise bounded by this valid classical parking word, so it too is valid. Every labeling is realized.

**Enumeration.** Choose the \(s\) queried rows in \(\binom ns\) ways. For each choice, the allowed ordered target lists are exactly the \(s\)-car partial parking functions on \(n\) spaces. Their known number is \((n-s+1)(n+1)^{s-1}\), including the empty tuple by convention. For completeness: place \(n+1\) spots on a circle, let \(s\) cars choose arbitrary preferred spots among all \(n+1\) (there are \((n+1)^s\) sequences), and park sequentially clockwise. Exactly \(n+1-s\) places remain empty; rotating all preferences rotates these vacancies. Therefore the number of preference sequences leaving a distinguished spot \(n+1\) empty is \((n+1-s)(n+1)^{s-1}\). Those sequences are precisely the successful linear-parking lists on the first \(n\) spots. This proves the coefficient formula; multiplying out the derivative of \((1+(n+1)z)^n\) yields
\[
\sum_{s=0}^{n}\binom ns(n+1-s)(n+1)^{s-1}z^s=(1+z)(1+(n+1)z)^{n-1}.
\]
The \(s=n\) term, which is not shattered, is \((n+1)^{n-1}z^n\) and must be removed.

**Facets and Euler characteristic.** Any shattered support of size \(s<n-1\) can be extended by selecting a previously unused row and querying its target value \(1\). The new ordered target sequence is still a partial parking list: the new first target is \(1\), and every old threshold \(n-s+r\) remains unchanged after insertion and increasing \(s\) by one. Thus every face extends to size \(n-1\). The formula at \(s=n-1\) gives \(2n(n+1)^{n-2}\) facets. The identity \(\widetilde\chi=-\Phi_n(-1)\) gives the stated reduced Euler characteristic, but **does not by itself imply a wedge-of-spheres or a homology concentration claim**.

**Matroid boundary.** For \(n\ge3\), the support \(A=\{(1,n)\}\) and \(B=\{(1,1),(2,n)\}\) are both faces. The first candidate \(A\cup\{(1,1)\}\) repeats a row, while \(A\cup\{(2,n)\}\) has two target values \(n\), violating the two-car partial parking bound \(j_{(1)}\le n-1\). Neither element of \(B\setminus A\) augments \(A\), contradicting the matroid exchange axiom. For \(n=1\) the complex has rank zero; for \(n=2\) it consists of the empty face and every singleton of \(Q_2\), namely the uniform rank-one matroid.

## Verification

The standalone program `check_parking.py` enumerates every parking function and every row-distinct support for \(2\le n\le5\), reconstructs all Boolean traces without using the theorem, and checks the classification and the face polynomials. It independently enumerates target lists for \(2\le n\le6\) and checks the closed coefficient formula, and tests the exchange obstruction through \(n=8\). The corresponding console output is in `check_output.txt`. These finite checks corroborate but do not replace the all-parameter proof.

For instance \(\Phi_3(z)=1+9z+24z^2\), \(\Phi_4(z)=1+16z+90z^2+200z^3\), and \(\Phi_5(z)=1+25z+240z^2+1080z^3+2160z^4\).

## Relationship to prior work

The classical criterion and the exact count for partial parking functions are **pre-existing** results; in particular, Kenyon and Yin (2021), Proposition 2.1 and Theorem 2.2, record both in the same normalization. Adeniran et al. (2019/2020) study counting parking completions under fixed positive preferences by lattice-path methods. Diaconis and Hicks (2017) analyze coordinate distributions of random classical parking functions. The claim here is the complete **positive-and-negative Boolean preference-query shattering equivalence**, its induced full face polynomial and the pure-but-nonmatroidal boundary, not a new formula for the number of partial parking functions in isolation. Existing enumerative results are inputs, not substituted originality claims.

## Limitations

The exact Littlestone dimension and the integral homotopy type of \(\Delta_n\) are not asserted. The Euler-characteristic formula does not imply homology is concentrated in top degree. Results concern all classical parking preference vectors, not restricted parking variants or arbitrary finite graphs. Although relevant published descriptions and indexed research results were compared, an equivalent unindexed formulation may exist and independent validation is outstanding.

## References

1. A. Adeniran, S. Butler, G. Dorpalen-Barry, P. E. Harris, C. Hettle, Q. Liang, J. L. Martin and H. Nam, *Enumerating Parking Completions Using Join and Split*, first public preprint 2019-12-03, Electron. J. Combin. 27(2) (2020), P2.44. https://arxiv.org/abs/1912.01688 ; https://doi.org/10.37236/9194.
2. R. Kenyon and M. Yin, *Parking Functions: From Combinatorics to Probability*, initial arXiv version 2021-03-31; Proposition 2.1, Theorem 2.2. https://arxiv.org/abs/2103.17180.
3. P. Diaconis and A. Hicks, *Probabilizing Parking Functions*, Advances in Applied Mathematics (2017), https://doi.org/10.1016/j.aam.2017.05.004.
