# Exact rank-one centralizer spectra in finite Boolean relation monoids

## Finding
Fix an integer \(n\geq 1\) and let \(\mathcal B_n\) be the monoid of all binary relations on \([n]\), with ordinary relational composition (Boolean matrix multiplication). Its order is \(2^{n^2}\). For nonempty subsets \(U,V\subseteq[n]\), let \(R_{U,V}=U\times V\), the nonzero rank-one Boolean rectangle. Set \(a=|U|\), \(b=|V|\), and \(c=|U\cap V|\).

Define, for every integer \(c\geq0\),
\[
H_c=\sum_{i=0}^{c}\sum_{j=0}^{c}(-1)^{i+j}\binom{c}{i}\binom{c}{j}2^{(c-i)(c-j)}.
\]
Here \(H_c\) counts Boolean \(c\times c\) matrices having no zero row and no zero column; the empty matrix is counted once, so \(H_0=1\).

**Exact centralizer theorem.** The number of *all* relations commuting with \(R_{U,V}\), including arbitrary-rank relations and zero, is
\[
\boxed{\bigl|C_{\mathcal B_n}(R_{U,V})\bigr|=2^{(n-a)(n-b)}\left[1+H_c(2^a-1)^{a-c}(2^b-1)^{b-c}\right].}
\]
This is valid whether \(R_{U,V}\) is idempotent (\(c>0\)) or square-zero (\(c=0\)). In particular, the entire centralizer-size multiset on the \((2^n-1)^2\) nonzero rank-one elements is determined: the displayed value at parameters \((a,b,c)\) occurs with parameter multiplicity
\[
\boxed{M_n(a,b,c)=\binom nc\binom{n-c}{a-c}\binom{n-a}{b-c},}
\]
for \(1\leq a,b\leq n\), \(\max(0,a+b-n)\leq c\leq\min(a,b)\). If different triples yield the same number, their multiplicities add. Equivalently the centralizer-size enumerator is \(\sum_{a,b,c}M_n(a,b,c)z^{|C_{\mathcal B_n}(R_{U,V})|}\), over precisely the indicated triples.

The theorem exhibits a substantial contrast inside this one Boolean-rank stratum. For the complete relation \(J_n=[n]\times[n]\),
\[
|C_{\mathcal B_n}(J_n)|=1+H_n,
\qquad
\frac{|C_{\mathcal B_n}(J_n)|}{2^{n^2}}=1-2n2^{-n}+O(n^2 2^{-2n}).
\]
For any singleton rectangle, the corresponding commutation probability is exactly \(2^{-2n+2}\), which tends to zero. Thus one rank-one relation commutes with asymptotically almost every relation, whereas another commutes with an exponentially vanishing fraction.

## Assumptions and scope
All sets are labeled subsets of the same \(n\)-element set, not subsets of two disjoint universes. In matrix notation, \((XY)_{ij}=\bigvee_{k=1}^n(X_{ik}\wedge Y_{kj})\). The zero relation is allowed as a potential commuting partner, but the fixed rectangle has nonempty row and column supports. The count concerns the *full* monoid \(\mathcal B_n\), not merely its rank-one principal factor or the subgraph of rank-one idempotents. Boolean rank one here means exactly a nonempty Cartesian rectangle; distinct ordered pairs \((U,V)\) represent distinct such relations.

The parameter \(c\) ranges over the overlap of the row and column supports. The three parameters determine the cardinality, but the theorem does not assert that numerically equal centralizer sizes imply identical parameter triples. The big-O assertion is for integer \(n\to\infty\).

## Proof
**1. Reduce commutation to two mutually exclusive support regimes.** For a relation \(Y\), write \(Y(i)=\{j:(i,j)\in Y\}\). Define the union of the rows indexed by \(V\) and the set of rows meeting \(U\):
\[
W(Y)=\bigcup_{v\in V}Y(v),\qquad Z(Y)=\{i:Y(i)\cap U\neq\varnothing\}.
\]
Direct Boolean multiplication, without rank assumptions on \(Y\), gives
\[
R_{U,V}Y=U\times W(Y),\qquad YR_{U,V}=Z(Y)\times V.
\]
Two such rectangles coincide precisely if both are empty, or if both are nonempty and their respective first and second supports coincide. Since \(U,V\) are nonempty, the equality \(R_{U,V}Y=YR_{U,V}\) is therefore equivalent to one of the *disjoint* conditions
\[
\text{(I)}\quad W(Y)=Z(Y)=\varnothing,
\qquad
\text{(II)}\quad W(Y)=V,\ Z(Y)=U.
\]

**2. Count the zero-product regime.** The condition \(W(Y)=\varnothing\) forces every row indexed by \(V\) to be zero. The condition \(Z(Y)=\varnothing\) forces every entry in a column indexed by \(U\) to vanish. Precisely the \((n-b)(n-a)\) entries outside the rows \(V\) *and* columns \(U\) remain free. Hence case (I) contributes \(2^{(n-a)(n-b)}\).

**3. Count the nonzero-product regime.** Decompose the ground set into the four disjoint sets
\[
A=U\cap V,\quad B=U\setminus V,\quad C=V\setminus U,\quad D=[n]\setminus(U\cup V).
\]
The requirement \(W(Y)=V\) says that every entry in the rows \(V\) and outside the columns \(V\) is zero, while each column indexed by \(V\) has at least one \(1\) in some row indexed by \(V\). The requirement \(Z(Y)=U\) says that every entry outside rows \(U\) and inside columns \(U\) is zero, while each row indexed by \(U\) has at least one \(1\) in a column indexed by \(U\).

For the \(A\times A\) block, both nonemptiness requirements apply: each of its rows and each of its columns must be nonzero. Such blocks number \(H_c\). On the \(B\times U\) block, each of the \(a-c\) rows can independently be an arbitrary *nonzero* binary row of length \(a\), contributing \((2^a-1)^{a-c}\). On the \(V\times C\) block, each of the \(b-c\) columns can independently be an arbitrary *nonzero* binary column of length \(b\), contributing \((2^b-1)^{b-c}\). These three blocks do not overlap. All entries outside the rows \(V\) and columns \(U\) are freely chosen (\((n-b)(n-a)\) bits), while the remaining entries are forced zero. This yields exactly
\[
2^{(n-b)(n-a)}H_c(2^a-1)^{a-c}(2^b-1)^{b-c}
\]
relations in case (II), including the conventions for the empty \(A\times A\) block. Adding case (I) proves the centralizer formula.

**4. Establish the nonzero-block count.** Inclusion-exclusion on the \(c\) specified zero rows and \(c\) specified zero columns, first selecting \(i\) rows and \(j\) columns to force to zero and then assigning the remaining \((c-i)(c-j)\) bits, gives exactly the stated \(H_c\). Thus no unknown combinatorial term remains.

**5. Count every orbit parameter.** First choose the \(c\) intersection points, then the \(a-c\) members of \(U\setminus V\), then the \(b-c\) members of \(V\setminus U\), with all choices disjoint. This gives \(M_n(a,b,c)\). Summing over all permissible triples counts each ordered nonempty pair \((U,V)\) exactly once, yielding \((2^n-1)^2\). Since simultaneous permutations of rows and columns carry any pair of supports with a given \((a,b,c)\) into any other, the formula and these multiplicities comprise the full rank-one centralizer-size multiset.

**6. Opposite asymptotic commutation regimes.** At \(U=V=[n]\), \(a=b=c=n\), giving \(1+H_n\). A uniformly random binary \(n\times n\) matrix has a zero row with probability \(2^{-n}\) for each row, and a zero column with the same probability. Their \(2n\) failure events have total first-order mass \(2n2^{-n}\). Any pair has intersection probability at most \(2^{-2n+1}\), so the entire correction to the first-order inclusion-exclusion term is bounded by \(O(n^2 2^{-2n})\) (use the union bound on pairwise intersections for the remaining correction). Therefore \(H_n/2^{n^2}=1-2n2^{-n}+O(n^2 2^{-2n})\), and the extra \(2^{-n^2}\) is absorbed. At \(a=b=1\), both possible intersection counts give \(H_c(2^a-1)^{a-c}(2^b-1)^{b-c}=1\), and so the centralizer has order \(2^{(n-1)^2+1}\), dividing by \(2^{n^2}\) gives \(2^{-2n+2}\).

## Verification
The standalone \(\texttt{verify.py}\) performs Boolean matrix multiplication explicitly, rather than using the reduction in this proof. It compares actual centralizer sizes to the formula for *every* nonzero rectangle against *every* Boolean matrix in dimensions \(n=1,2,3\), and for one representative of each of the \(26\) feasible overlap triples in dimension \(n=4\) against all \(65{,}536\) Boolean matrices. It also checks every triple multiplicity against direct enumeration of the support pairs and verifies \((H_0,H_1,H_2,H_3,H_4)=(1,1,7,265,41503)\). All assertions passed on replay under Python 3 with no dependencies. These finite tests corroborate but do not prove the all-\(n\) result.

For an illuminating small example, at \(n=4\) the three possible intersection sizes \(c=0,1,2\) among supports of fixed size \(a=b=2\) produce respective centralizer sizes \(1312,160,128\), with respective numbers of such rectangles \(6,24,6\). Thus even the two support cardinalities do not determine centralizer size: overlap matters strongly.

## Relationship to prior work
Kim and Roush (1981) established structural results for the full binary-relation semigroup and its rank-one Boolean matrices. Bremner and El Bachraoui (2010), Lemmas 5–15 and Theorem 21, develop the rectangular rank-one ideal of its *semigroup algebra*, and demonstrate its matrix-algebra structure. Their rectangle factorization and zero-product criteria are antecedents to the present elementary products; their reported theorem does not enumerate arbitrary-rank Boolean matrices commuting with each fixed rectangle. Dolžan, Kokol Bukovšek and Oblak (2010), Section 2, treat Boolean-matrix commuting-graph diameters and the centralizer of a fixed nilpotent shift; their Section 3, Lemma 3.1, gives a row-and-column maximum condition for the all-ones matrix in the tropical setting, analogous to the familiar Boolean all-ones special case. These results do not provide the present overlap-refined complete rank-one centralizer-size census. The all-ones support criterion itself is not claimed to be new.

The published result *Clique and maximal-clique enumerators for rank-one idempotent Boolean relations* classifies commuting *families within the rank-one idempotents*. Its documented scope explicitly excludes all arbitrary-rank commuting elements, so its clique formulas do not imply the present full-monoid centralizer spectrum. Existing rectangle products and two-sided support identities are credited as background; the precise three-parameter counting formula, its global multiplicity census, and the quantitative comparison of contrasting asymptotic regimes are the claims assessed here; the zero-row/zero-column criterion for the all-ones special case is background.

## Limitations
No formula is claimed for centralizers of arbitrary higher-Boolean-rank relations, or for centralizer *subsemigroup isomorphism types*. Some distinct parameter triples yield equal numerical values; the multiplicity formula sums the corresponding contributions rather than giving an injectivity classification. Priority risk remains from a possible earlier implicit enumeration of full Boolean-relation centralizers not located in the inspected literature, especially literature phrased in terms of relation algebras or multifunctions. The standalone computations have finite scope; the all-dimensions conclusions rely on the combinatorial proof. Independent proof and literature-priority review have not been performed.

## References
1. K. H. Kim and F. W. Roush, *The algebraic structure of the semigroup of binary relations on a finite set*, Glasgow Mathematical Journal **22** (1981), 57–68, https://doi.org/10.1017/S0017089500004468.
2. M. R. Bremner and M. El Bachraoui, *On the semigroup algebra of binary relations*, Communications in Algebra **38** (2010), 3499–3505, https://doi.org/10.1080/00927870902939418 (published online 2010-09-30).
3. D. Dolžan, D. Kokol Bukovšek and P. Oblak, *Diameters of commuting graphs of matrices over semirings*, arXiv:1012.5505v1 (first posted 2010-12-26), https://arxiv.org/abs/1012.5505.
4. *Clique and maximal-clique enumerators for rank-one idempotent Boolean relations*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-clique-and-maximal-clique-enumerators-for-rank-one-idempotent-bo--a2f16599b2ee.
