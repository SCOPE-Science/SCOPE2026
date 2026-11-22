# Gaussian factorial moments for alternating scattered patterns in binary Parikh fibres

## Finding

For integers \(A\ge1\), \(B\ge0\), and \(0\le C\le AB\), let \(\mathcal L_{A,B,C}\) be the binary words with \(A\) letters \(a\), \(B\) letters \(b\), and exactly \(C\) scattered \(ab\) pairs. Each word has the unique gap representation
\[
w=b^{g_0}a b^{g_1}a\cdots a b^{g_{A-1}}a b^{g_A},
\qquad g_i\in\mathbb Z_{\ge0},\quad\sum_{i=0}^{A}g_i=B.
\]
Set \(H(w)=|\{i:1\le i\le A-1,\ g_i>0\}|\), the number of *occupied interior* \(b\)-gaps. For \(q,u\) formal variables, the complete joint enumerator is
\[
\begin{aligned}
G_{A,B}(q,u)
&=\sum_{|w|_a=A,\ |w|_b=B}q^{\binom{w}{ab}}u^{H(w)}\\
&=[t^B]\frac{\prod_{i=1}^{A-1}(1+(u-1)tq^i)}{\prod_{i=0}^{A}(1-tq^i)}\\
&=\sum_{r=0}^{\min(A-1,B)}(u-1)^r q^{r(r+1)/2}
\begin{bmatrix}A-1\\r\end{bmatrix}_{q}
\begin{bmatrix}A+B-r\\A\end{bmatrix}_{q}.
\end{aligned}
\tag{1}
\]
Its factorial-moment polynomials have the factored formula
\[
\boxed{\sum_{|w|_a=A,\ |w|_b=B}q^{\binom{w}{ab}}\binom{H(w)}r
=q^{r(r+1)/2}\begin{bmatrix}A-1\\r\end{bmatrix}_q
\begin{bmatrix}A+B-r\\A\end{bmatrix}_q}
\tag{2}
\]
for every integer \(0\le r\le\min(A-1,B)\), and vanish for larger \(r\). Here \(\begin{bmatrix}n\\j\end{bmatrix}_q\) is the Gaussian binomial polynomial, and \(\binom{w}{ab}\) counts increasing-position scattered \(ab\) pairs.

For *every* integer \(k\ge1\), the scattered alternating pattern \((ab)^k a\) occurs in \(w\) if and only if \(H(w)\ge k\). Consequently the exact number of its avoiders in **every** binary Parikh fibre is
\[
\boxed{N_k(A,B,C)=[q^C]\sum_{h=0}^{k-1}[u^h]G_{A,B}(q,u),}
\tag{3}
\]
with exact conditional containment probability
\[
\Pr((ab)^k a\preceq w\mid w\in\mathcal L_{A,B,C})
=1-\frac{N_k(A,B,C)}{[q^C]\begin{bmatrix}A+B\\A\end{bmatrix}_q}.
\tag{4}
\]
The denominator is strictly positive for \(0\le C\le AB\). In particular, this gives a closed finite Gaussian-binomial coefficient expression, without enumerating the fibre, for arbitrarily long alternating patterns.

Summing over the pair count gives the additional exact composition-level spectrum
\[
\boxed{\#\{w:|w|_a=A,\ |w|_b=B,\H(w)=h\}
=\binom{A-1}{h}\binom{B+1}{h+1}}
\tag{5}
\]
for \(0\le h\le\min(A-1,B)\). Hence the total number avoiding \((ab)^k a\) is \(\sum_{h=0}^{k-1}\binom{A-1}{h}\binom{B+1}{h+1}\), with binomial coefficients outside their usual ranges interpreted as zero. For any fixed \(k\ge1\) and balanced content \(A=B=m\to\infty\), their avoidance probability among all \(\binom{2m}{m}\) binary words has the sharp equivalent
\[
\Pr((ab)^k a\not\preceq w\mid |w|_a=|w|_b=m)
\sim\frac{\sqrt\pi}{(k-1)!k!}\frac{m^{2k-1/2}}{4^m}.
\tag{6}
\]

## Assumptions and scope

Words are finite and linear over \(\{a,b\}\), and subsequences need not be contiguous. The polynomial variable \(q\) is formal, not an alphabet size; exponent \(\binom{w}{ab}\) is the count of scattered occurrences. In (1)–(6), \(A\ge1\) and \(B\ge0\). The degenerate case \(A=0\) consists of the single word \(b^B\), with \(C=H=0\), generating polynomial one, and all patterns \((ab)^k a\) absent. If \(k>A-1\), occurrence is impossible and (3) counts every word in the fibre. Gaussian binomials are polynomials defined by the recurrence \(\begin{bmatrix}n\\j\end{bmatrix}_q=\begin{bmatrix}n-1\\j\end{bmatrix}_q+q^{n-j}\begin{bmatrix}n-1\\j-1\end{bmatrix}_q\), with boundary values one and invalid-index values zero. Formula (6) is only for fixed \(k\), not for \(k\) increasing with \(m\).

## Proof

**Gap representation and pair statistic.** The unique gap vector records how many \(b\)'s occur before the first \(a\), between successive \(a\)'s, and after the last \(a\). A \(b\) in gap \(i\) has exactly \(i\) earlier \(a\)'s; therefore
\[
\binom{w}{ab}=\sum_{i=1}^{A}i g_i.
\tag{7}
\]
All nonnegative gap vectors with sum \(B\) are bijective with binary words of composition \((A,B)\).

**Alternating-pattern equivalence.** A scattered \((ab)^k a\) embedding selects \(k\) distinct \(b\)'s with an \(a\) preceding and following each selected \(b\), and at least one selected \(a\) between successive selected \(b\)'s. Thus their \(b\)'s lie in \(k\) strictly increasing nonempty interior gaps. Conversely, given such gaps \(1\le i_1<\cdots<i_k\le A-1\), select the \(a\) preceding gap \(i_1\), one \(b\) from each selected gap, and the \(a\) immediately following each chosen gap. These indices form \((ab)^k a\). This proves the equivalence without an assumption about unselected runs.

**Product and Gaussian expansion.** By (7), the contributions of exterior gaps \(0,A\) are \((1-t)^{-1}\) and \((1-tq^A)^{-1}\). For each interior gap \(i\), a zero gap contributes one and a positive gap \(v\ge1\) contributes \(u t^v q^{iv}\); hence its series is
\[
1+\frac{utq^i}{1-tq^i}=\frac{1+(u-1)tq^i}{1-tq^i}.
\]
Multiplying these independent gap series and extracting \([t^B]\) proves the first expression in (1). The elementary-symmetric identity
\[
\sum_{\substack{S\subseteq\{1,\ldots,A-1\}\\|S|=r}}q^{\sum_{i\in S}i}
=q^{r(r+1)/2}\begin{bmatrix}A-1\\r\end{bmatrix}_q
\]
and the weak-composition identity
\[
[t^d]\prod_{i=0}^{A}(1-tq^i)^{-1}=\begin{bmatrix}A+d\\A\end{bmatrix}_q
\]
then give the second expression in (1), with \(d=B-r\). Expanding \(u^{H}=(1+(u-1))^H\), the coefficient of \((u-1)^r\) in the joint enumerator is precisely the left side of (2), proving the factored factorial-moment identity.

**Exact fibres and unrefined spectrum.** Selecting the coefficients \(q^C u^h\) counts words with precisely those statistics by construction; summing over \(h<k\) and using the equivalence yields (3). Setting \(u=1\) in (1) yields \(\begin{bmatrix}A+B\\A\end{bmatrix}_q\), the usual positive rectangle-partition polynomial whose coefficient at every integer \(C\) from zero to \(AB\) is nonzero; this proves (4). For (5), choose the \(h\) occupied interior gaps from \(A-1\), place one \(b\) in each, then distribute the remaining \(B-h\) letters among the \(h\) selected interior gaps and both exterior gaps by stars and bars. The latter count is \(\binom{B+1}{h+1}\), so (5) follows.

**Asymptotic.** For fixed \(k\), as \(m\to\infty\), the largest-degree summand in \(\sum_{h=0}^{k-1}\binom{m-1}{h}\binom{m+1}{h+1}\) is the \(h=k-1\) term, asymptotic to \(m^{2k-1}/((k-1)!k!)\); all earlier terms have lower powers of \(m\). Dividing by \(\binom{2m}{m}\sim4^m/\sqrt{\pi m}\) proves (6). No asymptotic statement about a fixed \(C\) is asserted.

## Verification

Two standalone programs are included. `verify_direct.py` enumerates **all 8,191 binary words** of lengths zero through twelve, computes \(C\) from ordered letter pairs, computes \(H\) by scanning the input, directly tests every relevant scattered alternating pattern by a greedy subsequence matcher, and compares the joint histogram to a separately enumerated gap-composition model. Expected output: `PASS: all binary words of length <=12, 8191 words; pattern equivalence and bivariate spectrum`.

`verify_gaussian.py` derives Gaussian binomials by a polynomial recurrence and expands the right side of (1) by signed binomial coefficients, separately computes the entire joint distribution by independent coefficient convolution of all gap series, and verifies agreement for 175 content pairs with \(0\le A,B\le13\), \(A+B\le20\). It also checks (2), reflection symmetry, (5), and total population. Expected output: `PASS: 175 (A,B) pairs; independent Gaussian and slot-product coefficient calculations`. Both programs require only the Python standard library. These finite checks corroborate the symbolic, unbounded proof; they are not a substitute for it.

## Relationship to prior work

Fazekas, Huang and Mercaş (October 5, 2026) define conditional fixed-subsequence occurrence probabilities inside binary Parikh-matrix languages, characterize existence and universal subsequence indices, and give an additive approximation scheme for arbitrary fixed patterns. Their visible abstract and accessible material do not state the exact all-parameter occupancy distribution (1), the Gaussian factorial moments (2), or the resulting exact family of alternating-pattern probabilities. Their full text was not completely retrievable in this examination, so a hidden special case in that source remains a specific priority originality risk.

Menon and Singh (2023) determine the classical **unrestricted length-only** number of words avoiding a given scattered pattern. Their theorem concerns the marginal after summing over compositions and scattered \(ab\)-pair counts; it does not provide the joint distribution \((C,H)\), and those unrestricted avoidance totals are expressly not claimed as discoveries here.

Previously published binary Parikh-fibre results include *Exact sandwich-subsequence profiles within binary Parikh-matrix classes* (2026), which counts the **total** number of interior \(b\)'s and the scattered sandwich patterns \(ab^t a\), and *Inversion-refined avoidance spectra for all balanced four-letter scattered patterns* (2026), which gives exact avoidance distributions for the six balanced four-letter patterns. The present \(H\) records the number of **nonempty** interior gaps, not their total occupancy; these two statistics differ even at equal interior total, and the prior sandwich distribution does not imply (1). The four-letter classifications do not extend to the varying lengths \(2k+1\) for \(k\ge2\). The simple existence of some alternating-pattern avoider in a fibre and the unrefined count are **not** asserted as new; the new result is the joint Gaussian factorial-moment factorization and all-length, inversion-refined occurrence law.

Bilotta and collaborators (2012) treat binary strings avoiding **contiguous** alternating factors. Such factor avoidance and scattered-subsequence avoidance are different mathematical conditions. Classical Gaussian-binomial coefficient and gap-composition identities are used as ingredients, not advertised as individually original.

## Limitations

The claim addresses alternating scattered patterns beginning and ending in \(a\), over the binary alphabet. It does not solve the fixed-fibre probability problem for arbitrary patterns, optimize numerical bit-complexity, or establish an asymptotic for a fixed noncentral \(C\). The coefficient formulas specify exact integer counts, potentially requiring large polynomials when parameters are large. The closely related 2026 primary paper could not be read in full, and an unindexed equivalent joint-occupancy law is an explicit residual risk. The argument and computations have not undergone independent scientific audit.

## References

1. S. Z. Fazekas, X. Huang and R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717v1, first public October 5, 2026. https://arxiv.org/abs/2610.06717 .
2. R. Menon and S. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870, June 2023. https://arxiv.org/abs/2306.07870 .
3. *Exact sandwich-subsequence profiles within binary Parikh-matrix classes*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-sandwich-subsequence-profiles-within-binary-parikh-matrix--b40371a80999 .
4. *Inversion-refined avoidance spectra for all balanced four-letter scattered patterns*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-inversion-refined-avoidance-spectra-for-all-balanced-four-letter--e75590ea1e11 .
5. S. Bilotta et al., *Generation of binary words avoiding alternating patterns*, arXiv:1210.7620, 2012, https://arxiv.org/abs/1210.7620 .
