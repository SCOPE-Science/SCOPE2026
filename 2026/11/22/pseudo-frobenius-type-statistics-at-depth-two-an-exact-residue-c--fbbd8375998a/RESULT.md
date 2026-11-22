# Pseudo-Frobenius type statistics at depth two: an exact residue-chain product and a Gaussian law

## Finding

Let \(r\ge1\) and \(m\ge r+1\) be integers, set \(F=m+r\) and \(N=r-1\), and choose uniformly among numerical semigroups of multiplicity \(m\) and Frobenius number \(F\). There are exactly \(2^N\) such semigroups. Their Cohen–Macaulay types \(t(S)=|\operatorname{PF}(S)|\) have the following **exact mean**:

\[
\mathbb E[t(S)]=m-1-\frac{r-1}{2}+2^{-(r-1)}\sum_{j=1}^{r-1}a_{r,j},
\]

where an empty sum is zero and
\[
a_{r,j}=\begin{cases}
0,&j\mid r,\\
\displaystyle\prod_{\substack{1\le a<j\\a\not\equiv r\pmod j}}\left(2+\left\lfloor\frac{r-1-a}{j}\right\rfloor\right),&j\nmid r.
\end{cases}
\]

For any sequence \(r\to\infty\) with \(m\ge r+1\), uniformly in \(m\),
\[
\mathbb E[t(S)]=m-\frac{r-1}{2}+O\bigl(r(3/4)^{r/6}\bigr),
\qquad
\frac{t(S)-\bigl(m-(r-1)/2\bigr)}{\sqrt{r-1}/2}
\ \xrightarrow{\mathrm d}\ \mathcal N(0,1).
\]

The theorem gives more than a genus identity: distinct semigroups with the same multiplicity, Frobenius number, genus and embedding dimension may have different type.

## Assumptions and scope

A numerical semigroup is a cofinite additive submonoid of \(\mathbb N_0\). Its multiplicity is the least positive member, its Frobenius number the largest missing nonnegative integer, its genus the number of gaps, and
\[
\operatorname{PF}(S)=\{x\notin S:x+s\in S\text{ for all }s\in S\setminus\{0\}\}
\]
is its pseudo-Frobenius set. Its **type** is the cardinality of this set. Every assertion about asymptotics requires \(r\to\infty\), not merely \(m\to\infty\) with \(r\) fixed. The window \(m<F<2m\) is intentional; the boundary \(F=m\) is excluded and the formulas are not claimed for \(F\ge2m\).

For \(B\subseteq\{1,\dots,r-1\}\), set
\[
S_B=\{0,m\}\cup\{m+b:b\in B\}\cup\{F+1,F+2,\ldots\}.
\]
All such \(S_B\) are distinct numerical semigroups of multiplicity \(m\) and Frobenius \(F\), and all semigroups with these two invariants are of this form. Let
\[
H(B)=\#\{j\in B:(j+B)\cap\{1,\dots,r\}\subseteq B\}.
\]
The right side interprets \(r\notin B\) and \(j+B=\{j+b:b\in B\}\). The inclusion condition means that every sum \(j+b\le r\) belongs to \(B\).

## Proof

**1. Complete parameterization.** Because the least positive member is \(m\) and \(2m>F\), addition of two positive members cannot violate closure below the conductor \(F+1\). The element \(m\) is forced, the element \(F=m+r\) is missing, and each of \(m+1,\ldots,m+r-1\) may independently be present or absent. This proves the bijection with \(B\) and the count \(2^{r-1}\). It also gives the genus \(g(S_B)=m+r-1-|B|\).

**2. The complete pseudo-Frobenius set.** Every missing element above \(m\) is pseudo-Frobenius because adding any positive semigroup element gives a number greater than \(F\). For \(r<j<m\), adding \(m\) to the missing \(j\) also exceeds \(F\), so these are pseudo-Frobenius gaps. A smaller missing \(j\in\{1,\ldots,r\}\) fails the pseudo-Frobenius test whenever \(j\notin B\), because \(j+m\) is then a gap. For \(j\in B\), adding \(m\) succeeds; the remaining constraints from \(m+b\) with \(b\in B\) are precisely \(j+b>r\) or \(j+b\in B\). Therefore, disjointly,
\[
\operatorname{PF}(S_B)
=\{m+j:1\le j\le r,\ j\notin B\}
\;\dot\cup\;\{j:r<j<m\}
\;\dot\cup\;\{j\in B:(j+B)\cap[1,r]\subseteq B\}.
\]
The first part has \(r-|B|\) members and the middle part \(m-r-1\). Hence
\[
t(S_B)=m-1-|B|+H(B).
\]

**3. Exact residue-chain product.** Fix \(1\le j<r\). We count the subsets \(B\) for which \(j\) belongs to the third disjoint set above. Membership is binary on \(\{1,\dots,r-1\}\). Along each directed step-\(j\) residue chain, the requirement \(b\in B\Rightarrow b+j\in B\) whenever \(b+j\le r-1\) forces the binary membership word to be nondecreasing. Since \(j\in B\), the entire chain of positive multiples of \(j\) must contain only ones. Because \(r\notin B\), the vertex \(r-j\) must be absent, forcing the entire chain of residue \(r\bmod j\) to contain only zeros. If \(j\mid r\), these requirements contradict one another and the count is zero.

If \(j\nmid r\), the two forced chains are distinct, and every other chain beginning at residue \(a\in\{1,\ldots,j-1\}\), except \(a=r\bmod j\), contains \(1+\lfloor(r-1-a)/j\rfloor\) vertices. It has exactly one more nondecreasing binary words than its vertex count, yielding \(a_{r,j}\) as displayed. Independent fair coin choices of \(B\) now give
\[
\mathbb E H(B)=2^{-(r-1)}\sum_{j=1}^{r-1}a_{r,j},
\]
and \(\mathbb E|B|=(r-1)/2\), proving the exact mean.

**4. A sharp bound on the correction term.** Let \(E_{r,j}\) be the event counted by \(a_{r,j}\). If \(j>r/2\), the two constraints \(j\in B\) and \(r-j\notin B\) concern distinct coordinates. The \(r-j-1\) remaining implications \(b\in B\Rightarrow b+j\in B\), for \(1\le b<r-j\), concern mutually disjoint coordinate pairs, disjoint also from the two forced coordinates. Consequently
\[
\mathbb P(E_{r,j})=\tfrac14(\tfrac34)^{r-j-1},
\quad
\sum_{j=\lfloor r/2\rfloor+1}^{r-1}\mathbb P(E_{r,j})
=1-(\tfrac34)^{r-1-\lfloor r/2\rfloor}.
\]
If \(j\le r/2\), its implication graph comprises directed paths with \(r-1-j\) total edges and maximum degree two. Some matching contains at least \((r-1-j)/3\) pairwise vertex-disjoint edges. Each matched implication \(b\in B\Rightarrow b+j\in B\) is independently satisfied with probability \(3/4\). Requiring all of them gives
\[
\mathbb P(E_{r,j})\le (\tfrac34)^{(r-1-j)/3}.
\]
Summing proves \(\mathbb E H(B)=1+O(r(3/4)^{r/6})\); this is uniform in \(m\).

**5. Gaussian law.** As \(B\) is uniformly random, \(|B|\) has the binomial distribution with \(r-1\) trials and success probability \(1/2\). The preceding estimate makes \(\sup_r\mathbb E H(B)<\infty\), whence Markov's inequality gives \(H(B)/\sqrt r\to0\) in probability. Apply the binomial central limit theorem and Slutsky's theorem to \(t(S_B)=m-1-|B|+H(B)\) and the centering \(m-(r-1)/2\). The fixed difference in centering is negligible after division by \(\sqrt{r-1}/2\). This proves the asserted normal limit.

**6. Invariant separation.** For \(m=6\), \(F=11\), \(r=5\), let \(B_1=\{1,2,3\}\) and \(B_2=\{1,3,4\}\). Both semigroups have genus \(7\) and embedding dimension \(4\); the direct pseudo-Frobenius sets are respectively \(\{10,11\}\) and \(\{3,8,11\}\). Thus their types are \(2\) and \(3\), not determined by the pair of genus and embedding dimension.

## Verification

Run `python3 verify.py` from a directory containing the accompanying standalone script. It exhaustively checks the complete pseudo-Frobenius set against its defining universal quantifier, the type identity, exact product counts and mean for every subset \(B\) for \(1\le r\le12\), using three distinct admissible multiplicities for each \(r\). The expected terminal line is `VERIFY_OK 12285 semigroups; r=1..12, three m values`. The asymptotic theorem is proved analytically above; no finite enumeration is represented as a proof of an infinite statement.

## Relationship to prior work

Bras-Amorós and Torra (originally arXiv:2607.23111v1, July 2026; split theoretical paper arXiv:2611.11559v1, November 2026) count semigroups jointly by Frobenius number, genus and multiplicity and prove general recurrences. Their inspected preprint includes the depth-two counting framework but not the pseudo-Frobenius type residue-chain product, its exact expectation or its limiting law. Singhal's work on genus distribution under fixed Frobenius number gives related binomial statistics; his separate work on small and large type considers extremal regimes rather than this conditional type law. Li treats Frobenius, multiplicity and depth enumeration; Moreno-Frías and Rosales give an algorithmic fixed-Frobenius covariety. Earlier pseudo-Frobenius-set algorithms do not directly imply the stated closed product. The additional \(H(B)\) term is not recoverable from genus and embedding dimension, as the explicit counterexample demonstrates.

## Limitations

The exact formula pertains to depth two, \(m<F<2m\), only. The central limit theorem needs \(r=F-m\to\infty\). The estimate does not claim a limiting distribution for the unscaled correction \(H(B)\), nor a complete type histogram. The searched published sources and research records did not disclose a covering theorem, but absence from searches is not a proof of historical priority. This is a mathematical proof and a finite independent check, not an independently audited result.

## References

- M. Bras-Amorós and V. Torra, *Algorithms and results on multiparameter counting of numerical semigroups*, arXiv:2607.23111v1, first submitted 2026-07-25, https://arxiv.org/abs/2607.23111.
- M. Bras-Amorós and V. Torra, *Multiparameter counting of numerical semigroups by Frobenius number, genus, and multiplicity*, separated theoretical paper arXiv:2611.11559v1, first submitted 2026-11-08, https://arxiv.org/abs/2611.11559.
- D. Singhal, *Distribution of genus among numerical semigroups with fixed Frobenius number*, Semigroup Forum (2022), https://doi.org/10.1007/s00233-022-10282-6.
- D. Singhal, *Numerical semigroups of small and large type*, arXiv:2008.08110, https://arxiv.org/abs/2008.08110.
- S. Li, *Counting numerical semigroups by Frobenius number, multiplicity, and depth*, Combinatorial Theory (2023), https://arxiv.org/abs/2208.14587.
- M. A. Moreno-Frías and J. C. Rosales, *The covariety of numerical semigroups with fixed Frobenius number*, J. Algebraic Combinatorics 60 (2024), https://doi.org/10.1007/s10801-024-01342-x.
- M. Delgado, P. A. García-Sánchez and A. M. Robles-Pérez, *Numerical semigroups with a given set of pseudo-Frobenius numbers*, https://arxiv.org/abs/1505.08111.
