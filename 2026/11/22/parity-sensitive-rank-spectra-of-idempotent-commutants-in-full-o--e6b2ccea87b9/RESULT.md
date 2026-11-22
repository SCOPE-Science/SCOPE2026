# Parity-sensitive rank spectra of idempotent commutants in full order-decreasing partial-isometry monoids

## Finding

Let \(D_n\) be the monoid of all order-decreasing partial distance-preserving injections of the chain \([n]=\{1,\ldots,n\}\), including the empty map, and let \(n\ge1\). For \(0\le r\le n\), count ordered commuting pairs with an idempotent first coordinate and a second coordinate of rank \(r\):

\[
I_{n,r}=\#\{(e,f)\in D_n^2:e^2=e,\ ef=fe,\ |\operatorname{dom}f|=r\}.
\]

With the convention \(\binom ab=0\) when \(b<0\) or \(b>a\), the exact answer is

\[
\boxed{I_{n,r}=2^n\binom nr+\mathbf1_{r\ge1}2^{n-r}\binom n{r+1}+\mathbf1_{r\ge2}R_{n,r},}
\]

where, for \(r\ge2\), the contribution of the genuinely order-reversing maps is

\[
\boxed{\begin{aligned}
R_{2m,r}&=2^{2m-r}\left[4\binom{m+1}{r+1}+\binom mr\right],\\
R_{2m+1,r}&=2^{2m+1-r}\left[4\binom{m+1}{r+1}+3\binom mr+2\binom m{r-1}\right].
\end{aligned}}
\]

Thus reversing maps distinct from translations contribute only at ranks \(2\le r\le\lceil n/2\rceil\). At the largest permitted rank their commutation-incidence counts are \(R_{2m,m}=5\cdot2^m\) for \(m\ge2\), and \(R_{2m+1,m+1}=2^{m+1}\) for \(m\ge1\). The expressions cover every \(n\ge1\); there are no reversing-map corrections for \(n\le2\).

For example, the vectors \((I_{n,0},\ldots,I_{n,n})\) are \((8,36,30,8)\) for \(n=3\), \((16,112,132,66,16)\) for \(n=4\), and \((32,320,488,348,162,32)\) for \(n=5\). The total number of pairs with idempotent first coordinate is the sum of these coefficients.

## Assumptions and scope

Distance preservation means \(|f(x)-f(y)|=|x-y|\) for all points in the domain. Order decreasing means \(f(x)\le x\) wherever defined. Rank means domain cardinality. The first coordinate is any idempotent of \(D_n\); these are precisely the partial identities \(1_B\) for \(B\subseteq[n]\). The second coordinate may preserve or reverse order, with any permissible domain, and the empty transformation is counted once. In rank one, a reversing representation is the same function as a translation representation and is therefore not counted twice. The formula is not a count of pairs in which both coordinates are idempotent.

## Proof

**1. Commutation condition.** For a partial injection \(f\) and \(1_B\), equality \(1_Bf=f1_B\) holds precisely when for each \(x\in\operatorname{dom}f\), the binary membership indicators obey
\[
\mathbf1_B(x)=\mathbf1_B(f(x)).
\]
Every nonempty distance-preserving map of a subset of a chain has affine form \(f(x)=x-d\) or \(f(x)=s-x\). This follows immediately by choosing two distinct domain points and using equality of all pairwise distances; maps of rank at most one are treated separately.

**2. Identity and positive translations.** Each of the \(\binom nr\) partial identity maps of rank \(r\) commutes with all \(2^n\) idempotents. For a positive shift \(d\ge1\), its possible domain positions are \(d+1,\ldots,n\). Sum over all \(2^n\) indicator words for \(B\), marking each chosen domain point by \(z\). The edges \(x-d\to x\) split into \(d\) disjoint paths. On a path with \(L\) vertices, the two-state transfer matrix whose entry is \(1+z\) if endpoint bits agree and \(1\) otherwise has row sum \(2+z\); its total weight is \(2(2+z)^{L-1}\). Multiplication across paths gives \(2^d(2+z)^{n-d}\). Hence the rank-\(r\) count for \(d\) is \(2^{n-r}\binom{n-d}{r}\). Summing \(d=1,\ldots,n-1\), the hockey-stick identity gives \(2^{n-r}\binom n{r+1}\) for \(r\ge1\). The empty choice is excluded from positive-shift strata.

**3. Reflection parameters and disjoint paired edges.** Write \(f(x)=s-x\), with \(2\le s\le2n\). Its allowed order-decreasing positions form
\[
Q_s=\{x\in[n]:1\le s-x\le x\}.
\]
Among them \(p_s\) positions are noncentral, each matched to a distinct smaller point \(s-x\) outside those noncentral positions, and \(f_s\in\{0,1\}\) central positions satisfy \(2x=s\). Precisely,
\[
p_s=\left\lfloor\frac{\min(s-1,2n+1-s)}2\right\rfloor,
\qquad f_s=\mathbf1_{s\ \mathrm{even}}.
\]
The \(p_s\) pairs are disjoint and the center, if present, is distinct from them. On a pair the sum over its four binary labels, marking the larger domain point when the bits agree, is \(4+2z\); on a central point it is \(2(1+z)\); each remaining free point contributes \(2\). Consequently the complete domain-rank polynomial of admissible reflected domains, aggregated over all \(B\), is
\[
\sum_{B\subseteq[n]}(1+z)^{\#\{x\in Q_s:\mathbf1_B(x)=\mathbf1_B(s-x)\}}
=2^{n-p_s}(2+z)^{p_s}(1+z)^{f_s}.
\]
Its coefficient for rank \(r\ge2\) is
\[
2^{n-r}\left[\binom{p_s}{r}+2f_s\binom{p_s}{r-1}\right].
\]
Every such reflected map is genuinely order reversing and cannot coincide with a translation because its domain has at least two points. Conversely every order-reversing element outside the translation stratum occurs uniquely in one such reflection family.

**4. Parity-dependent grouping.** If \(n=2m\), each \(p=1,\ldots,m-1\) occurs for four values of \(s\), two with \(f_s=1\) and two with \(f_s=0\); the top value \(p=m\) occurs once with \(f_s=0\). If \(n=2m+1\), each \(p=1,\ldots,m-1\) again occurs four times with two of each center type, while \(p=m\) occurs three times, once with a center and twice without. The cases \(p=0\) cannot contribute rank \(r\ge2\). A four-member group contributes
\[
4\cdot2^{n-r}\left[\binom pr+\binom p{r-1}\right]
=4\cdot2^{n-r}\binom{p+1}r.
\]
Applying \(\sum_{p=1}^{m-1}\binom{p+1}r=\binom{m+1}{r+1}\), valid for \(r\ge2\), and adding the terminal group gives both displayed expressions for \(R_{n,r}\). The bound on possible rank and the two sharp terminal coefficients follow by direct substitution. Adding the identity and positive-translation strata proves the claimed formula for every rank, including \(r=0,1\). \(\square\)

## Verification

A standalone standard-library Python checker (`checker.py`) enumerates *actual partial maps* as translation or reflection restrictions, deduplicates maps, and tests commutation by computing both compositions with every partial identity. Its output matched the formula for all \(1\le n\le8\), including all ranks. Counts for \(n=6,7,8\) are respectively \((64,864,1584,1440,984,386,64)\), \((128,2240,4800,5248,4664,2716,898,128)\), and \((256,5632,13696,17344,18896,14560,7200,2050,256)\). The finite checker supports but does not establish the general all-size result, which follows from the preceding combinatorial argument.

## Relationship to prior work

Ayık, Ayık and Fernandes, *On semigroups of order-decreasing partial isometries: presentations and ranks of certain ideals* (arXiv:2611.12150v1, 9 November 2026), study generating sets, ranks of ideals and monoid presentations for both orientation-preserving and unrestricted order-decreasing partial isometries, but do not supply the rank-graded idempotent-commutation incidence formula. Earlier finite-chain work of Kehinde, Makanjuola and Umar (arXiv:1101.2558) and Al-Kharousi, Kehinde and Umar (arXiv:1702.04485) develops Green-class and cardinality enumerations; these are relevant structural background but do not, from their inspected material, determine the present commutation spectrum. An available exact *aggregate* commutation result for the larger semigroup of all partial isometries also does not determine this order-decreasing, rank-refined polynomial: counting all orientations without the restriction does not specify the restricted incidence by rank. The contribution beyond the order-preserving case is the full reflection correction, with its parity split and sharp rank frontier. Classical two-state transfer calculations are used as proof tools, not presented as novel lemmas.

## Limitations

The result counts only commuting ordered pairs whose **first** coordinate is idempotent, refined by the rank of the second. It does not determine all commuting pairs in \(D_n\), nor individual centralizer cardinalities for every \(B\). Historical priority is conditional on coverage of specialist sources not fully accessible and on indexing; an inaccessible full copy cannot be treated as a whole-document negative comparison. Finite enumeration is not an infinite proof. No independent mathematical audit has been performed.

## References

1. G. Ayık, H. Ayık and V. H. Fernandes, *On semigroups of order-decreasing partial isometries: presentations and ranks of certain ideals*, arXiv:2611.12150v1 (2026-11-09), https://arxiv.org/abs/2611.12150 .
2. R. Kehinde, S. O. Makanjuola and A. Umar, *On the semigroup of order-decreasing partial isometries of a finite chain*, arXiv:1101.2558v1 (2011), https://arxiv.org/abs/1101.2558 .
3. F. Al-Kharousi, R. Kehinde and A. Umar, *Combinatorial results for certain semigroups of order-decreasing partial isometries of a finite chain*, arXiv:1702.04485v1 (2017), https://arxiv.org/abs/1702.04485 .
