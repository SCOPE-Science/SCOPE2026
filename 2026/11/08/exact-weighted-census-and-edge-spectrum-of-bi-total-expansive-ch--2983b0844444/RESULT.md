# Exact weighted census and edge spectrum of bi-total expansive chain correspondences

## Finding

For reflexive finite chains, expansive correspondences with nonempty rows and columns have an explicit weighted census by the numbers of related pairs. Their possible sizes are **all** integers from the larger chain size to the product of the chain sizes. The least, greatest and next-to-greatest coefficients are explicit. In equal dimensions the count has a sharp linear-order entropy deficit:
\[\log_2 E_{n,n}(1)=n^2-2n+O(\log n).\]
The complete formula below determines every coefficient, not merely the support of the counting polynomial.

## Assumptions and scope

Fix integers \(m,n\ge1\). The source and target are reflexive chains \([m]=\{0,\ldots,m-1\}\) and \([n]=\{0,\ldots,n-1\}\), each with the usual order. A binary relation \(R\subseteq[m]\times[n]\) is **expansive** when it satisfies both confluence conditions:

* (F) Whenever \(i\le i'\) and \((i,j)\in R\), there is \(j'\le j\) with \((i',j')\in R\).
* (B) Whenever \(j\le j'\) and \((i,j)\in R\), there is \(i'\le i\) with \((i',j')\in R\).

These are the forward confluence and its converse-direction counterpart, respectively. **Bi-total** means every source row and every target column is nonempty; this is stronger than merely left-total. The chains, including their orders, are fixed, so no quotient by relabelling is involved.

Write \(E_{m,n}(t)=\sum_R t^{|R|}\), over all bi-total expansive \(R\). For a nonincreasing map \(\alpha:[m]\to[n]\) and a nonincreasing map \(\beta:[n]\to[m]\), set
\[
D(\alpha,\beta)=\{(i,j):j\ge\alpha_i\text{ and }i\ge\beta_j\},
\]
\[
U(\alpha,\beta)=\{(i,\alpha_i):i\in[m]\}\cup\{(\beta_j,j):j\in[n]\}.
\]
If \(U\not\subseteq D\), discard that pair of profiles. Otherwise its weight is \(t^{|U|}(1+t)^{|D|-|U|}\). The complete exact formula is
\[
\boxed{E_{m,n}(t)=\sum_{\substack{\alpha:[m]\to[n],\;\beta:[n]\to[m]\\
\alpha,\beta\text{ nonincreasing}\\U(\alpha,\beta)\subseteq D(\alpha,\beta)}}
t^{|U(\alpha,\beta)|}(1+t)^{|D(\alpha,\beta)|-|U(\alpha,\beta)|}.}
\]
The sum is finite and explicitly computable by iterating over at most \(\binom{m+n-1}{m}\binom{m+n-1}{n}\) profile pairs. It does not involve enumeration of all \(2^{mn}\) Boolean matrices.

In particular:
\[
\operatorname{supp}E_{m,n}=\{\max(m,n),\max(m,n)+1,\ldots,mn\},
\quad [t^{\max(m,n)}]E_{m,n}(t)=\binom{\max(m,n)-1}{\min(m,n)-1}.
\]
The coefficient of \(t^{mn}\) is \(1\); for \(m,n\ge2\), the coefficient of \(t^{mn-1}\) is \(mn-m-n+2\). Finally,
\[
2^{(m-1)(n-1)}\le E_{m,n}(1)\le (m+1)(n+1)2^{(m-1)(n-1)}.
\]

## Proof

**1. Confluence is exactly antitonicity of the first occupied rows and columns.** Because all rows and columns are nonempty, put \(\alpha_i=\min\{j:(i,j)\in R\}\) and \(\beta_j=\min\{i:(i,j)\in R\}\). Condition (F) applied to \((i,\alpha_i)\) and \(i\le i'\) gives \(\alpha_{i'}\le\alpha_i\). Conversely, if \(\alpha\) is nonincreasing and \((i,j)\in R\), then the existing cell \((i',\alpha_{i'})\) witnesses (F), because \(\alpha_{i'}\le\alpha_i\le j\). The symmetric argument proves that (B) is equivalent to \(\beta\) being nonincreasing. These equivalences use reflexivity at equal indices and do not assume that every cell in a row is occupied.

**2. Weighted normal form.** Every cell in row \(i\) has column at least \(\alpha_i\), and every cell in column \(j\) has row at least \(\beta_j\), hence \(R\subseteq D\). Every row minimum and column minimum is compulsory, hence \(U\subseteq R\). Conversely, whenever \(U\subseteq D\), each \(R\) satisfying \(U\subseteq R\subseteq D\) has exactly these prescribed row and column minima: compulsory cells attain the bounds, while the region forbids smaller indices. The sequences are nonincreasing, so both confluence conditions hold by Step 1. Thus profiles uniquely partition the admissible relations, and the \(|D|-|U|\) optional cells are independent. Summing their binomial weights proves the displayed formula.

**3. Minimum, spectrum and extremal coefficients.** Since all \(m\) rows and \(n\) columns are occupied, \(|R|\ge\max(m,n)\). Suppose first \(m\ge n\). Equality requires one cell in every source row, so \(R\) is the graph of a weakly decreasing surjection \(f:[m]\to[n]\). Conversely, such a graph satisfies (F) by monotonicity, and (B) because every target value at least \(f(i)\) is realized at some source index no larger than \(i\). Its nonempty constant-fibre blocks form a composition of \(m\) into \(n\) positive parts, giving exactly \(\binom{m-1}{n-1}\) choices. If \(m<n\), transpose the relation and interchange the chains.

To realize every intermediate edge count when \(m\ge n\), begin with any such graph. First insert all cells strictly right of its graph, one at a time. For an added \((i,j)\) with \(j>f(i)\), later source rows have a graph cell at column at most \(f(i)<j\), while all target columns at least \(j\) already have a graph cell in a source row at most \(i\). Thus both confluences persist. Next process rows from bottom to top. In each row, insert missing cells left of the graph from right to left. When \((i,j)\) is added, all later source rows are already full (witnessing (F)), and every cell to its right in the same row is already present (witnessing (B)). The operation of adding a cell leaves existing witnesses intact, so every stage is expansive and bi-total. This adds exactly one cell per step until the full rectangle is reached. Transposition handles \(m<n\). The full rectangle is the unique size-\(mn\) relation.

For \(m,n\ge2\), delete exactly one cell from the full rectangle. The result fails (B) when the missing cell lies in the top row outside its leftmost position, and fails (F) when it lies in the leftmost column below its top position. Conversely, deleting any of the remaining \(mn-m-n+2\) cells preserves both confluences and bi-totality: for every obligation of (F), a later row has a leftmost-column witness, unless the relevant cell is unchanged in that same row, and analogously for (B) using the top row; if the removed cell is the top-left one, witnesses from later rows and columns still exist. This proves the next-to-leading coefficient.

**4. Sharp linear-order entropy deficit.** Any relation containing the full first row and the full first column is expansive: for strict row advancement use the first-column entry, and for strict column advancement use the first-row entry. Its \((m-1)(n-1)\) interior cells can be chosen arbitrarily, giving the lower bound. Conversely, in an expansive relation the occupied cells of the first column form a suffix of the source chain, by (F); the occupied cells of the top row form a suffix of the target chain, by (B). Each boundary has at most \(m+1\) or \(n+1\) patterns, and the remaining \((m-1)(n-1)\) cells have at most two choices each. This gives the upper bound. Taking base-two logarithms at \(m=n\) proves the entropy formula. Among all \(2^{n^2}\) binary relations the bi-total expansive fraction is therefore \(2^{-2n+O(\log n)}\).

## Verification

The standalone `checker.py` tests the confluence axioms directly, independently enumerates all Boolean relation matrices for \(1\le m,n\le4\), and compares their full-support edge polynomials with the profile formula. It also checks the interval of possible sizes, the two extremal coefficients, the next-to-leading coefficient, and constructs a complete edge-by-edge admissible chain for every tested shape. The square-case counts for \(n=1,2,3,4\) are \(1,4,58,2698\), respectively. Running `python checker.py` prints `FULL_CHECKS_OK`. These finite tests are not used as a proof for arbitrary \(m,n\).

## Relationship to prior work

Fernández-Duque's 2026 paper introduces forward and backward confluence for expansive relations of transitive frames and uses them in a finite-model-property proof for intuitionistic modal logic. It does not provide the weighted finite-chain correspondence census stated here. Earlier published results cover strict-chain expansive relations and other, distinct confluence conditions for birelational modal frames on a single chain; their conditions and enumerations should not be conflated with the reflexive, two-chain, bi-total correspondence problem here. The distinct scope is essential: in the strict-chain result the largest relation has an entirely different size constraint, while the present full reflexive rectangle is always admissible.

## Limitations

The result is restricted to finite reflexive **linear** orders and relations total on both sides. It does not count arbitrary transitive orders or equivalence classes under nontrivial order automorphisms. The entropy statement controls the exponent to within a logarithmic term and does not determine a finite limiting multiplicative constant. Historical priority against some less accessible specialized confluence literature is not independently settled. The formula gives a finite exact sum, not a claimed constant-time algorithm.

## References

1. David Fernández-Duque, *Fine Selection for Intuitionistic Modal Logic*, arXiv:2609.27078, first submitted September 22, 2026; see especially Definitions 2.2–2.3 and Proposition 2.4. https://arxiv.org/abs/2609.27078
2. *Endpoint normal form for expansive relations between finite strict chains*, published mathematical research record, identifier `03b1c1fd9c86` (strict-order result).
3. *Maxima normal form and exact census for chain birelational relations*, published mathematical research record, identifier `f1e0f9b64170` (different frame-interaction requirements).
4. *Gaussian-binomial census of FIK relations on finite chains*, published mathematical research record, identifier `75c9508e987d` (one-sided confluence).
