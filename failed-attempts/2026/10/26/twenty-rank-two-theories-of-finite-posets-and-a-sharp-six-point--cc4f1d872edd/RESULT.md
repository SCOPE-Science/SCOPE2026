# Twenty rank-two theories of finite posets and a sharp six-point representative bound

## Finding
Let \(P\) range over all **nonempty finite strict partial orders** in the pure language \(\{<,=\}\), with no colours, constants or auxiliary functions. Write \(P\equiv_2 Q\) when \(P\) and \(Q\) satisfy the same first-order sentences of quantifier rank at most \(2\). There are **exactly twenty** \(\equiv_2\)-classes. Every class has a representative on at most **six points**; six is necessary for one class. Their least representative sizes have distribution
\[
\begin{array}{c|rrrrrr}
\text{least size}&1&2&3&4&5&6\\\hline
\text{number of classes}&1&2&4&7&5&1.
\end{array}
\]
If the empty order is included, it contributes one additional class, yielding twenty-one in total, without changing the maximal representative size.

## Assumptions and scope
All orders here are finite and strict: \(<\) is irreflexive and transitive, and the vocabulary is exactly a single binary order symbol with equality. Quantifier rank means maximum **nesting depth** of first-order quantifiers, not total number of occurrences. No counting quantifiers are allowed. Empty orders are excluded from the principal count.

For a point \(x\in P\), define three Boolean predicates: \(L(x)\) means that a distinct point lies strictly below \(x\); \(U(x)\) means that a distinct point lies strictly above \(x\); and \(I(x)\) means that a point incomparable with \(x\) exists. Define the mask
\[
m_P(x)=\mathbf{1}_{L(x)}+2\mathbf{1}_{U(x)}+4\mathbf{1}_{I(x)}\in\{0,\ldots,7\},
\]
and its spectrum \(T(P)=\{m_P(x):x\in P\}\). For a compact table, encode a spectrum by the integer \(s(P)=\sum_{j\in T(P)}2^j\). These integer encodings are not order cardinalities.

## Proof
**1. Full rank-two invariant.** In the pure strict-order language, the possible quantifier-free relations between \(x\) and another variable \(y\) are exactly equality, being below, being above, and incomparability. Equality has a witness \(y=x\) for every \(x\). Consequently the truth values of all rank-at-most-one formulas in the single free variable \(x\) are determined by the three bits \(L(x),U(x),I(x)\): atomic formulas with only \(x\) have fixed truth values; quantification over one additional variable detects precisely which of the four atomic relation cases have a witness; and Boolean combinations preserve this property. Every rank-at-most-two *sentence* is, by induction over its syntax, a Boolean combination of assertions that a rank-at-most-one one-free-variable formula has some realization. Its truth therefore depends only on \(T(P)\).

Conversely, for every mask \(j\), the formula \(\theta_j(x)\) asserting the three exact existential/nonexistential relations encoded by \(j\) has quantifier rank one. The sentence \(\exists x\,\theta_j(x)\) has rank two and asserts precisely \(j\in T(P)\). Therefore
\[
P\equiv_2 Q\quad\Longleftrightarrow\quad T(P)=T(Q).
\]

**2. Upper bound of twenty spectra.** A one-point poset has only mask \(0\), and mask \(0\) cannot occur in a larger poset. An isolated point in a poset of at least two points has mask \(4\); its presence forces every other point to have an incomparable companion. If every point is isolated, the spectrum is \(\{4\}\). Otherwise there is at least one comparability, and there are points of masks \(5\) and \(6\) (take a maximal and a minimal point of a nontrivial comparability component). Every nonisolated interior point has mask \(7\). Thus with an isolated point there are precisely the three *possible* spectra \(\{4\}\), \(\{4,5,6\}\), and \(\{4,5,6,7\}\).

Suppose instead that \(P\) has at least two points and **no** isolated point. Every maximal point lies above something. If there is a unique maximal element it is above every other element and has mask \(1\); otherwise every maximal element is incomparable to another maximal element and has mask \(5\). Hence exactly one of masks \(1,5\) occurs. Dually, exactly one of masks \(2,6\) occurs among minimal points. Every other point lies both above and below something, and its mask is \(3\) if comparable to every point, or \(7\) otherwise. Each of masks \(3,7\) may be present or absent. Thus at most \(2\cdot2\cdot2\cdot2=16\) spectra occur without isolated points. Including the singleton and the three isolated-point possibilities gives at most \(1+3+16=20\).

**3. Exact attainment, least sizes, and sharpness.** The table below lists **all** possible spectrum codes and the cardinality of their smallest representatives. For each row, `witnesses.json` records the actual strict order by upward bitsets, where bit \(j\) in row \(i\) asserts \(i<j\). The entries are genuine transitive irreflexive relations; directly computing \(L,U,I\) from each relation yields the claimed distinct spectrum. In particular, this proves that all sixteen logically possible nonisolated spectra and all three isolated spectra really occur.

| spectrum code | least size | spectrum code | least size |
|---:|---:|---:|---:|
| 1 | 1 | 6 | 2 |
| 14 | 3 | 16 | 2 |
| 36 | 3 | 44 | 4 |
| 66 | 3 | 74 | 4 |
| 96 | 4 | 104 | 5 |
| 112 | 3 | 134 | 4 |
| 142 | 5 | 164 | 4 |
| 172 | 5 | 194 | 4 |
| 202 | 5 | 224 | 5 |
| 232 | 6 | 240 | 4 |

For the lower bounds on these small representative sizes, `verify.py` enumerates all subsets of the \(\binom n2\) forward relation pairs for \(1\le n\le6\), closes transitively, and determines which spectra first appear at each size. This is exhaustive: every finite poset has a linear extension, and its strict order relations are a subset of the forward pairs in that extension. The code reports the exact first-appearance distribution \(1,2,4,7,5,1\).

There is also a direct conceptual proof of the **global** sharp bound. Spectrum code \(232\) is the mask set \(\{3,5,6,7\}\). Mask \(5\) requires at least two distinct maximal points, and mask \(6\) requires at least two distinct minimal points. Masks \(3\) and \(7\) require two distinct nonextremal points. These three categories are disjoint, so every realization needs at least six points. A six-point realization appears in the witness table; explicitly, on \(\{0,1,2,3,4,5\}\), the upward sets are \((\{2,3,4,5\},\{2,3,4,5\},\{3,4,5\},\{4\},\varnothing,\varnothing)\). This establishes the sharp universal bound.

## Verification
The package contains `witnesses.json`, `verify.py`, and `verification_output.txt`. Execute `python3 verify.py` from the directory containing the witness file. The script checks each witness's transitivity and spectrum, exhaustively enumerates all naturally labeled order seeds through six points, checks every claimed minimal representative size, and independently evaluates the ordinary two-round Ehrenfeucht--Fraïssé game on all \(210\) unordered pairs of the twenty representatives (including identical pairs), plus \(1000\) additional comparisons with naturally labeled posets of size at most four. It terminates with `CLASSIFICATION_OK`.

The infinite-all-orders assertion does **not** rest on finite enumeration. Its two general parts—the rank-two spectrum criterion and the universal twenty-spectrum restriction—are proved in the preceding paragraphs. Finite computations establish the small witness construction and the minimal-size census.

## Relationship to prior work
The Ehrenfeucht--Fraïssé characterization of quantifier rank is classical. Fagin, Lenchner, Regan and Vyas (2021) restate it, then study a different multi-structural game measuring the number of quantifier **occurrences**, primarily on linear orders. Mwesigye and Truss (2018) classify two-round equivalence for **coloured linear orders**, using point characters and optimal representatives. That is a proper subclass with a different vocabulary and cannot imply the above count for **all finite partial orders**, where incomparability fundamentally changes the possible point profiles. Kellerman and Goranko (2021) consider first-order theories of certain classes of infinite or path-order-type trees, rather than the twenty finite-pure-poset rank-two spectra. The general character/spectrum idea is prior methodology; the specific twenty-class census, all-class witnesses, and sharp six-point representative bound are not attributed to those sources. Failure to locate another source is not a uniqueness theorem.

## Limitations
This concerns pure first-order **quantifier rank two only**. It does not classify rank three, coloured posets, infinite posets, arbitrary relational structures, total quantifier count, or formulas with free parameters. The sharp six-point compression is an equivalence-class representative, not a claim that every given poset has a six-point **induced subposet** in its class. A complete historical priority search is not proved, and the mathematical proof and finite checker have not been independently audited.

## References
1. R. Fagin, J. Lenchner, K. W. Regan and N. Vyas, *Multi-Structural Games and Number of Quantifiers*, arXiv:2104.14709, first public version 2021-04-30; see especially the ordinary E--F equivalence theorem and distinction between rank and quantifier count. https://arxiv.org/abs/2104.14709
2. F. Mwesigye and J. K. Truss, *On Optimal Representatives of Finite Coloured Linear Orders*, Order 36 (2019), 107--117, public repository deposit 2018-04-06; see Section 2 and Theorem 1.1. https://doi.org/10.1007/s11083-018-9458-3
3. R. Kellerman and V. Goranko, *Approximating Trees as Coloured Linear Orders and Complete Axiomatisations of Some Classes of Trees*, Journal of Symbolic Logic 86 (2021), 1035--1065, published online 2021-06-08. https://doi.org/10.1017/jsl.2021.40
