# Exact nonbinary variance of two-deletion sphere cardinality

## Finding
Let \(q\ge3\) and \(n\ge2\) be integers, and let \(X\) be uniformly distributed over the labeled alphabet \(\Sigma_q^n\), with \(|\Sigma_q|=q\). Write \(D_2(X)\) for the **set** of distinct length-\(n-2\) words obtained by deleting exactly two coordinates, and \(B_{n,q}=|D_2(X)|\). With \(m=n-1\), the exact first two moments are
\[
\mathbb E B_{n,q}=\frac{m^2(q-1)^2+m(q^2-1)+2q}{2q^2}
\]
and
\[
\boxed{\operatorname{Var}(B_{n,q})=\frac{(m-1)(q-1)}{2q^4}\left[2m^2(q-1)^2+m(-2q^2+5q-3)+2q^2-4q\right].}
\]
For every fixed \(q\ge3\), this gives \(\operatorname{Var}(B_{n,q})=(q-1)^3n^3/q^4+O_q(n^2)\). The binary specialization \(q=2\) agrees with an already published result; **novelty is claimed only for the nonbinary range**.

## Assumptions and scope
The input is a uniformly random, independent-symbol linear word, not a cyclic word. The channel deletes exactly two coordinates; repeated outputs count once. The alphabet is labeled but the formulas depend only on its size. The zero-length descendant is included when \(n=2\), so \(B_{2,q}=1\) deterministically. The formula is a second-moment result, not a complete distributional description and not an assertion about the probability of any particular deletion pattern.

## Proof
### 1. A pointwise two-deletion identity
For a nonempty word \(w\), let \(r(w)\) be the number of maximal constant runs, \(h(w)\) the number of those runs having length at least two, and \(t(w)\) the number of internal singleton runs whose two neighboring runs have the **same symbol**. Then
\[
|D_2(w)|=\binom{r(w)}2+h(w)-t(w). \tag{1}
\]
Here \(D_2(w)=\varnothing\) if \(|w|<2\). We give a direct induction, so equation (1) need not be taken on faith from prior run enumerations. For \(w=ua\), with nonempty \(u\) and appended letter \(a\), the decomposition
\[
D_2(ua)=D_1(u)\ \cup\ \{va:v\in D_2(u)\}
\]
expresses the possible last-coordinate deletion. There are \(r(u)\) distinct one-deletion descendants. If \(a\) is the final letter of \(u\), exactly \(r(u)-\mathbf1_{\{\text{last run of }u\text{ is singleton}\}}\) of them end in \(a\), and each belongs to \(D_2(u)a\). Indeed, any deletion that retains the terminal \(a\) also permits a two-deletion embedding with that terminal copy retained; a final singleton deleted as a whole gives the sole exception. Thus adjoining the same letter increases \(|D_2|\) by one precisely when the old final run was a singleton.

If \(a\) differs from the final letter of \(u\), at most one one-deletion descendant of \(u\) can end in \(a\): it must delete the final letter, and the penultimate letter must be \(a\). When that happens the descendant is also in \(D_2(u)a\), using the deletion of the last two letters for its shorter prefix. Hence adjoining a different letter increases \(|D_2|\) by \(r(u)-\mathbf1_{\{\text{the penultimate letter of }u\text{ is }a\}}\). These two increments agree with the right side of (1): in the first case a singleton run becomes nonsingleton, and in the second case a new singleton run appears while the old final run becomes an internal singleton counted by \(t\) exactly in the stated configuration. Both sides vanish on a one-letter word, proving (1) for every length and alphabet.

### 2. Independent increments and conditional law
Fix an identification of the alphabet with the additive group \(\mathbb Z/q\mathbb Z\). Define \(\Delta_i=X_{i+1}-X_i\pmod q\), \(1\le i\le m\). The map \((X_1,\Delta_1,\ldots,\Delta_m)\mapsto X\) is bijective, so the increments are independent uniform group elements. Define \(A_i=\mathbf1_{\{\Delta_i\ne0\}}\), \(S=\sum_i A_i\), and \(J=\sum_{i=1}^{m-1}A_iA_{i+1}\). The \(A_i\) are independent Bernoulli variables with
\[
p=\frac{q-1}{q},\qquad v=p(1-p)=\frac{q-1}{q^2},\qquad \alpha=\frac1{q-1}.
\]
Run boundaries occur at the nonzero increments, and hence \(r=1+S\). The number of nonsingleton runs is the number of maximal zero-runs among the \(A_i\); for \(m\ge2\),
\[
h=(1-A_1)+\sum_{i=2}^m A_{i-1}(1-A_i)=1+S-A_1-A_m-J. \tag{2}
\]
An internal singleton run with equal flanking letters is exactly an adjacent pair of nonzero increments satisfying \(\Delta_i+\Delta_{i+1}=0\) modulo \(q\). Therefore, conditional on the binary pattern \(A=(A_1,\ldots,A_m)\),
\[
t\mid A\ \sim\ \operatorname{Binomial}(J,\alpha). \tag{3}
\]
To justify independence in (3), within any maximal block of nonzero increments the first increment may be chosen in \(q-1\) ways. At each subsequent position exactly one of the \(q-1\) choices is the negative of its predecessor. Thus any prescribed pattern of adjacent return/nonreturn indicators has the corresponding product probability, and separate nonzero blocks are independent. This includes even \(q\), when some nonzero increments can be self-inverse.

Combining (1) and (2),
\[
B_{n,q}=\tfrac12S(S+1)+1+S-A_1-A_m-J-t. \tag{4}
\]
The conditional variance of (4) is \(\alpha(1-\alpha)J\), while its conditional expectation is
\[
G(A)=\tfrac12S(S+1)+1+S-A_1-A_m-(1+\alpha)J. \tag{5}
\]

### 3. Orthogonal second-moment calculation
Assume \(m\ge2\), and let \(Y_i=A_i-p\). The \(Y_i\) are independent, centered, and have variance \(v\). Since \(Y_i^2=v+(1-2p)Y_i\) and \((1+\alpha)p=1\), expanding (5) yields the exact orthogonal decomposition
\[
G-\mathbb E G=(m-1)p\sum_{i=1}^mY_i
 +\sum_{\substack{1\le i<j\le m\\j\ge i+2}}Y_iY_j
 -\alpha\sum_{i=1}^{m-1}Y_iY_{i+1}. \tag{6}
\]
To check its uniform linear coefficient, let \(e_i=1\) at an endpoint and zero elsewhere, and let \(d_i\) be the degree of vertex \(i\) in the length-\(m\) path. The coefficient of \(Y_i\) before simplification is \(mp+2-p-e_i-(1+\alpha)p d_i\). Since \(e_i+d_i=2\) at every vertex and \((1+\alpha)p=1\), it equals \((m-1)p\). A nonadjacent pair has coefficient \(+1\); an adjacent pair has \(1-(1+\alpha)=-\alpha\).

Distinct square-free centered monomials in (6) are orthogonal. There are \((m-1)(m-2)/2\) nonadjacent pairs and \(m-1\) adjacent pairs. Consequently
\[
\operatorname{Var}(G)=m(m-1)^2p^2v+(m-1)v^2\left(\frac{m-2}{2}+\alpha^2\right). \tag{7}
\]
The law of total variance, (3), and \(\mathbb E J=(m-1)p^2\) give
\[
\operatorname{Var}(B_{n,q})=m(m-1)^2p^2v+(m-1)v^2\left(\frac{m-2}{2}+\alpha^2\right)+(m-1)p^2\alpha(1-\alpha). \tag{8}
\]
Substituting \(p,v,\alpha\) and collecting terms proves the boxed variance. Taking expectations in (4), using \(\mathbb ES=mp\), \(\mathbb ES^2=m^2p^2+mv\), \(\mathbb EJ=(m-1)p^2\), and \(\mathbb Et=\alpha(m-1)p^2\), gives the displayed mean. The case \(m=1\) is deterministic, and both formulas yield mean one and variance zero. This finishes the proof for every integer \(q\ge3\), \(n\ge2\).

## Verification
The standalone `verify_deletion_moments.py` reconstructs the sets \(D_2(w)\) directly from all coordinate pairs, rather than using the proof's recurrence. It checks the pointwise run formula for every word and compares exact rational means and variances against both closed forms for \(2\le n\le11\) when \(q=2\), \(2\le n\le8\) when \(q=3\), \(2\le n\le7\) when \(q=4\), and \(2\le n\le6\) when \(q=5\). All tests pass. The separate `verify_conditional.py` checks the return-event binomial law on every binary boundary pattern at small nonbinary parameters, and the algebraic coefficients of the orthogonal decomposition with exact fractions. The computational tests are finite corroboration, not a replacement for the all-parameter induction and conditional-probability proof.

For example at \(q=4\), \(n=5\), the formulas give \(\mathbb EB_{5,4}=53/8\) and \(\operatorname{Var}(B_{5,4})=549/128\); all \(4^5\) words verify both values. At \(q=2\), (8) specializes to \((n-1)(n-2)(2n-3)/32\), providing an external consistency anchor without claiming that binary case as new.

## Relationship to prior work
Swart and Ferreira (2003) give the binary run-based double-deletion count. Mercier, Khabbazian and Bhargava (2008) develop exact deterministic subsequence counting, including nonbinary alphabets and small deletion radii. Liron and Langberg (arXiv:1202.1644, first public version 2012-02-08) analyze extremal sizes of deletion sets for binary strings. Li, Wang and Fu (arXiv:2601.06493) give nonbinary extremal run-structured bounds. These works supply motivation and pre-existing deterministic information; the pointwise cardinality is not claimed as a new invariant. A separate public 2026 result explicitly gives the binary variance \((n-1)(n-2)(2n-3)/32\), and the present claim deliberately excludes the binary alphabet. The contribution is the evaluated, uniform-input, **nonbinary** variance formula, including its exact \(q\)-dependence and leading constant. Accessible primary full texts and research-record comparisons did not establish previous coverage of that formula. An older or unindexed derivation cannot be excluded.

## Limitations
Mercier et al. (2008) was identified as highly relevant, but its complete publisher text could not be inspected through available access; historical-priority confirmation is particularly important. No claim is made for biased independent symbols, correlated sources, three or more deletions, full distributions, or deletion-ball intersections. Its value is an exact nonbinary second moment for a natural channel parameter; no coding-rate improvement or downstream theorem is asserted.

## References
1. Y. Liron and M. Langberg, *A characterization of the number of subsequences obtained via the deletion channel*, arXiv:1202.1644, first posted 2012-02-08. https://arxiv.org/abs/1202.1644
2. H. Mercier, M. Khabbazian and V. K. Bhargava, *On the number of subsequences when deleting symbols from a string*, IEEE Trans. Inf. Theory 54 (2008), 3279–3285. https://doi.org/10.1109/TIT.2008.924730
3. T. G. Swart and H. C. Ferreira, *A note on double insertion/deletion correcting codes*, IEEE Trans. Inf. Theory 49 (2003), 269–273. https://doi.org/10.1109/TIT.2002.806155
4. H. Li, X. Wang and F.-W. Fu, *On the number of subsequences in the nonbinary deletion channel*, arXiv:2601.06493, 2026. https://arxiv.org/abs/2601.06493
5. *Exact variance of binary two-deletion sphere size*, public mathematical research record (2026); binary-case antecedent. https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-variance-of-binary-two-deletion-sphere-size--6c9fe70986cc/RESULT.md
