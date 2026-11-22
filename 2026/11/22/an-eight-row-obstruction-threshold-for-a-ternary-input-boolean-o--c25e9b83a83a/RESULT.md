# An eight-row obstruction threshold for a ternary-input Boolean-outcome dependence split

## Finding

Let \(X=\{0,1,2\}\), let \(Y\) be any finite set, and let \(Z=\{0,1\}\). A *team* is a set \(T\subseteq X\times Y\times Z\) of distinct triples. Under ordinary lax team semantics, consider
\[
\varphi=\operatorname{dep}(x,y)\lor\operatorname{dep}(y,z).
\]
Here \(\operatorname{dep}(a,b)\) says that equal \(a\)-values determine equal \(b\)-values, and the disjunction requires a union of two subteams satisfying the respective dependencies. Call \(T\) *minimal failing* if \(T\not\models\varphi\) but all its proper subteams satisfy \(\varphi\).

**Theorem.** Every finite minimal failing team has cardinality in exactly the set
\[
\boxed{\{4,6,7,8\}}.
\]
Every listed size occurs, and in particular **eight is the sharp universal obstruction cutoff**: every failing finite team with three possible \(x\)-values and two possible \(z\)-values has a failing subteam of at most eight rows, independently of the number of possible \(y\)-values.

More precisely, after forgetting *only* the names of the used \(y\)-values, while keeping the three \(x\)-values and both \(z\)-values named, there are exactly 306 minimal-failure patterns. Their distribution by the number \(k\) of distinct used \(y\)-values is:

| \(k\) | size 4 | size 6 | size 7 | size 8 | total |
|---|---:|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 3 | 6 | 12 | 0 | 21 |
| 3 | 0 | 36 | 12 | 102 | 150 |
| 4 | 0 | 0 | 0 | 135 | 135 |
| Total | 3 | 42 | 24 | 237 | 306 |

Thus the value five is genuinely absent, while seven first occurs with two distinct \(y\)-values.

## Assumptions and scope

The two dependence atoms use exactly the displayed three variables. The input alphabet \(X\) is fixed and named, the Boolean output alphabet \(Z\) is fixed and named, and \(Y\) can have any finite cardinality, including zero. The team is a set, not a multiset. The disjunction is a splitting disjunction, not the Boolean disjunction of global assertions. Since dependence atoms are downward closed, overlapping witnesses may be converted to a partition. No other attributes are present.

## Proof

**1. Function-selection normal form.** A witnessing partition \(T=R\cup B\) with \(R\models\operatorname{dep}(x,y)\) chooses at most one \(y\)-value for each \(x\)-value. Extend these choices to a function \(f:X\to Y\cup\{\bot\}\), where \(\bot\) means no choice. Move into \(R\) every row whose first two coordinates satisfy \(f(x)=y\); this preserves the first dependency and only removes rows from \(B\). The second dependency is equivalent to having, for each \(y\), at most one \(z\)-value among the *unselected* rows. Conversely any such \(f\) produces a witnessing partition. Therefore
\[
T\models\varphi\iff \exists f:X\to Y\cup\{\bot\}\quad
\forall y\in Y:\quad
\left|\{z:\exists x\ ((x,y,z)\in T\ \wedge\ f(x)\ne y)\}\right|\le1.
\]
This equivalence is exact, with no assumption on the number of \(y\)-values.

**2. Reduction to four mixed fibres.** Call a \(y\)-fibre *mixed* if its rows collectively contain both Boolean values of \(z\). Any unmixed fibre can always be assigned entirely to \(B\) and imposes no condition on \(f\); hence it contains no row of a minimal failing team. Every mixed fibre requires \(f(x)=y\) for at least one \(x\). Because only three \(x\)-values exist, selecting two opposite-\(z\) rows at each of any four distinct mixed fibres already creates a failing eight-row team: four different fibres cannot all receive one of three selected \(x\)-values. Therefore a minimal failing team has at most four mixed fibres. If it has exactly four, it consists of precisely two opposite-\(z\) rows at each, so has size eight. Zero mixed fibres are satisfied by putting every row in \(B\); one mixed fibre is satisfied by setting all three values of \(f\) to that fibre. It remains to analyze two and three mixed fibres.

**3. Complete finite certificate for two or three fibres.** For a fixed \(y\), record a state vector \(p_y\in\{0,1,2,3\}^3\), where its \(x\)-component is the bit mask of the Boolean \(z\)-values occurring at that \((x,y)\) cell: \(0\) for neither, \(1\) for \(z=0\), \(2\) for \(z=1\), and \(3\) for both. A mixed fibre is exactly a state vector whose three components jointly contain both bits. By inclusion-exclusion there are \(4^3-2^3-2^3+1=49\) such vectors. Renaming \(y\)-values permits their vectors to be sorted without losing any configuration; for \(k\) used mixed fibres, exactly \(\binom{48+k}{k}\) sorted vectors must be checked.

The standalone `verify.py` enumerates all \(49\), \(1225\), \(20825\), and \(270725\) sorted vectors for \(k=1,2,3,4\). For each it enumerates every \(f\in\{\bot,0,\ldots,k-1\}^3\) and tests the criterion in Step 1. It calls a configuration minimal failing precisely when it is unsatisfied and every one-row deletion becomes satisfied. Downward closure makes the one-row test equivalent to checking every proper subteam. The four exact census rows appear in the table above. The algorithm is finite and exhaustive because Step 2 bounds \(k\) and the state vector encodes every possible fibre. The source is standard-library-only Python and prints its actual counts; it also independently checks 400 small cases by direct red/blue partition enumeration and explicitly verifies witnesses of each allowed size. No unexamined number of \(y\)-values remains.

**4. Sharp witnesses.** One minimal failing eight-row team is
\[
\begin{aligned}
\{&(2,0,0),(2,0,1),\\
  &(1,1,0),(2,1,1),\\
  &(0,2,0),(2,2,1),\\
  &(0,3,0),(1,3,1)\}.
\end{aligned}
\]
The first fibre forces \(f(2)=0\). The other three then require respectively \(f(1)=1\), \(f(0)=2\), and \(f(0)=3\) or \(f(1)=3\), an impossibility. Deleting either row from the first fibre leaves three coverable mixed fibres; deleting a row from any other fibre leaves only two coverable mixed fibres in addition to the forcing fibre. Hence all single deletions are satisfiable. The verifier gives and directly checks separate four-, six-, and seven-row examples. This completes the claimed spectrum and sharp cutoff. \(\square\)

## Verification

Run `python3 verify.py` with Python 3.10 or later. The expected final line is `VERIFY_OK canonical=292824 independent_split_crosschecks=400`. The full enumeration covers every canonical state tuple for one through four used mixed fibres, not merely randomly generated teams. The 400 additional independently implemented direct-split tests are finite cross-checks; the exhaustive state encoding and reduction give the universal conclusion.

## Relationship to prior work

Fröhlich, Kolaitis and Meier prove the *unrestricted* formula \(\operatorname{dep}(x,y)\lor\operatorname{dep}(y,z)\) incoherent; their construction allows the determinant alphabet to grow. The available published result imposing only two \(x\)-values gives a sharp six-row cutoff, with four- and six-row minimal failures. Neither statement implies the present three-\(x\), Boolean-\(z\) eight-row theorem: the second is restricted to a smaller \(x\)-alphabet, and the first supplies no finite cutoff under this promise. Barlag and coauthors prove general coherence/first-order-rewritability results and complexity bounds, not this restricted minimum-obstruction spectrum. The new theorem concerns a different, explicitly bounded attribute-domain slice of the same natural chained functional-dependency constraint.

## Limitations

No assertion is made for four or more \(x\)-values, three or more \(z\)-values, multiset teams, or additional unprojected attributes. The numerical classification depends on an exhaustive finite certificate and has not undergone independent formal or peer verification. Literature priority may be affected by earlier database-theoretic forbidden-pattern classifications under other terminology. The six-row two-input result and the general incoherence theorem are credited as prior work, not claimed new.

## References

1. T. Barlag, N. Fröhlich, M. Hannula, P. G. Kolaitis, J. Kontinen, A. Meier and J. Väänänen, *Aspects of Coherence in Dependence Logic*, arXiv:2605.31269, first posted 2026-05-29, https://arxiv.org/abs/2605.31269.
2. N. Fröhlich, P. G. Kolaitis and A. Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146, first posted 2025-08-22; *CSL 2026*, DOI: 10.4230/LIPIcs.CSL.2026.10. Open full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol363-csl2026/html/LIPIcs.CSL.2026.10/LIPIcs.CSL.2026.10.html.
3. *A sharp six-tuple obstruction theorem for a binary determinant in dependence logic*, published research record dated 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-six-tuple-obstruction-theorem-for-a-binary-determinant-i--1faf692a71cb.
