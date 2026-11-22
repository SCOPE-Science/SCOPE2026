# Exact all-prime nearest-neighbor gap laws for the nonzero Pascal fractal

## Finding

For any prime \(p\) and integer \(r\ge1\), consider every row \(0\le n<p^r\) of Pascal's triangle and retain exactly the positions \(k\) for which \(p\nmid\binom nk\). In each row, list these positions increasingly and record every **gap between successive retained positions**. We pool all such gaps over all the rows, with multiplicities. Write \(C_{p,r}(d)\) for the number of pooled gaps of size \(d\), where \(d\) is a positive integer. Let
\[
 A=\frac{p(p+1)}2,\qquad B=\frac{p(p-1)}2,\qquad
 i_p(d)=\min\{i\ge0:d\le p^i\}.
\]
Then the **entire nearest-neighbor spacing spectrum**, for every prime and every depth, is
\[
 \boxed{C_{p,r}(d)=\begin{cases}
 \displaystyle\frac{B}{A-1}\bigl(A^{r-i_p(d)}-1\bigr),&1\le d\le p^{r-1},\\
 0,&d>p^{r-1}.
 \end{cases}}
\]
The fraction is an integer because it is a finite geometric sum: equivalently, \(C_{p,r}(d)=B\sum_{i=i_p(d)}^{r-1}A^{r-1-i}\).

The exact number of pooled gaps is \(A^r-p^r\). As \(r\to\infty\), the distribution obtained by sampling **a uniformly chosen pooled gap, not a uniformly chosen row**, converges at every positive integer \(d\) to
\[
 \boxed{\pi_p(d)=\frac{B}{A-1}A^{-i_p(d)}.}
\]
This is a probability distribution on the positive integers. Its tail is exactly self-similar at prime-power thresholds: for every integer \(j\ge0\),
\[
 \boxed{\mathbb P_{\pi_p}(D>p^j)
 =\frac{p-1}{A-1}\left(\frac pA\right)^j
 =\frac{p-1}{A-1}(p^j)^{-\alpha_p},\qquad
 \alpha_p=\log_p\!\left(\frac{p+1}{2}\right).}
\]
In particular \(0<\alpha_p<1\), and the \(s\)-th moment of \(\pi_p\) is finite **if and only if** \(0\le s<\alpha_p\). The limiting mean is infinite, despite each finite-depth distribution having finite mean. At finite depth the exact mean is
\[
 \frac{p^r(p^r-1)}{2(A^r-p^r)}.
\]

## Assumptions and scope

The prime \(p\) ranges over all rational primes, including two; \(r\) ranges over positive integers; \(n\) ranges over \(\{0,\ldots,p^r-1\}\); and gaps are positive *differences of consecutive admissible column indices inside the same row*. Endpoints \(k=0,n\) are always retained. If a row contains only one retained position (only possible at \(n=0\)), it contributes no gaps. No inter-row, cyclic, wraparound, or duplicate gaps are inserted. Multiplicities count the ordered adjacent pairs \((k,k')\) with \(k<k'\). The limiting law is formed by first pooling all such pairs, then choosing one uniformly; weighting rows equally gives a different statistic.

## Proof

**Step 1: Lucas support as a digital box.** Write the \(r\) base-\(p\) digits of the row index as \(n=\sum_{j=0}^{r-1}a_jp^j\), where \(0\le a_j<p\). By Lucas's theorem, the retained column indices are exactly
\[
 K_p(n)=\left\{\sum_{j=0}^{r-1}b_jp^j:0\le b_j\le a_j\right\}.
\]
Consequently the size of the support is \(\prod_j(a_j+1)\), and summing over all rows gives \(A^r\), as in Fine's digit-product count.

**Step 2: Classify every adjacent pair with one pivot digit.** In increasing numeric order, every nonterminal \(b\in K_p(n)\) has a unique least position \(i\) for which \(b_i<a_i\). All lower digits are saturated, \(b_j=a_j\) for \(j<i\). The immediate successor replaces \(b_i\) by \(b_i+1\), sets all lower digits to zero, and leaves higher digits untouched. (There is no admissible value between them, by the ordinary radix order.) Therefore its gap is
\[
 d=p^i-\sum_{j=0}^{i-1}a_jp^j.
\]
For any fixed row digits \(a\) and pivot \(i\), the number of such pairs is exactly
\[
 a_i\prod_{j=i+1}^{r-1}(a_j+1),
\]
because the pivot digit \(b_i\) has \(a_i\) choices, the higher digits have their independent allowed choices, and the lower digits are fixed at their maxima. The terminal support element has no successor and no pivot, so the classification is exhaustive without overcounting.

**Step 3: Pool rows for a fixed pivot and gap.** Fix \(0\le i<r\). The lower-digit number \(L=\sum_{j<i}a_jp^j\) ranges bijectively over all \(0,\ldots,p^i-1\). Thus the gap \(d=p^i-L\) occurs for exactly one lower-digit vector for each \(d\in\{1,\ldots,p^i\}\), and for no other \(d\). Summing the pivot multiplicity over every pivot digit gives
\[
 \sum_{a_i=0}^{p-1}a_i=B,
\]
and independently summing over all higher row digits gives
\[
 \prod_{j=i+1}^{r-1}\sum_{a_j=0}^{p-1}(a_j+1)=A^{r-1-i}.
\]
So every \(d\) from one through \(p^i\) occurs exactly \(BA^{r-1-i}\) times at pivot \(i\). Summing over every possible pivot \(i\ge i_p(d)\) proves the displayed complete gap formula, including its sharp support cutoff.

**Step 4: Exact finite totals.** Each row contributes \(|K_p(n)|-1\) gaps because it contains the endpoints; \(|K_p(0)|=1\) also satisfies this. Thus the total number of gaps is
\[
 \sum_{n<p^r}\left(\prod_j(a_j+1)-1\right)=A^r-p^r.
\]
The sum of all gap lengths within any row telescopes from first retained index zero to final retained index \(n\). Therefore the total gap-length sum is \(\sum_{n=0}^{p^r-1}n=p^r(p^r-1)/2\), proving the finite mean.

**Step 5: Limit and exact tail.** For fixed \(d\), divide the finite formula by \(A^r-p^r\), then let \(r\to\infty\). Since \(p<A\), this gives \(\pi_p(d)\) above. For \(i\ge1\), exactly \((p-1)p^{i-1}\) positive integers have \(i_p(d)=i\); the shell \(i=0\) contains only \(d=1\). Summing these geometric shells, using \(A-p=B\), gives \(\sum_{d\ge1}\pi_p(d)=1\) and, for any \(j\ge0\),
\[
 \begin{aligned}
 \sum_{d>p^j}\pi_p(d)
 &=\frac{B}{A-1}\sum_{i=j+1}^{\infty}(p-1)p^{i-1}A^{-i}\\
 &=\frac{p-1}{A-1}\left(\frac pA\right)^j.
 \end{aligned}
\]
Since \(A/p=(p+1)/2\), this is the stated power-tail formula. For any real \(s\ge0\), the contribution from shell \(i\) to the \(s\)-th moment is bounded above and below by positive \(p,s\)-dependent constants times \((p^{s+1}/A)^i\) (with the lower bound for \(i\ge1\) obtained from the upper half of each shell). This geometric series converges exactly when \(p^{s+1}<A\), equivalently \(s<\log_p(A/p)=\alpha_p\). Equality gives divergence as well. This proves the entire theorem.

## Verification

The standalone file `verify_gap.py` constructs successive Pascal rows using integer addition reduced modulo \(p\), determines admissible positions without invoking the proof's digital pivot construction, enumerates all adjacent gaps, and compares each complete histogram against the theorem. It also independently checks binomial coefficients from `math.comb` on initial rows; checks the total number and sum of gap lengths; and checks exact counts beyond prime-power thresholds at finite depth. Execute `python3 verify_gap.py` from the extracted directory. The observed output ends in `CHECK_OK`: 25 prime/depth cases covering \(p\in\{2,3,5,7,11\}\), with up to nine binary digits and six ternary digits. The finite checks corroborate, but do not establish, the infinite statement; the Lucas pivot argument above supplies the universal proof.

## Relationship to prior work

Lucas's classical congruence theorem (1878) identifies the exact digitwise support; Fine's theorem (1947) determines its **cardinality per row**. Rowland's 2010 preprint (arXiv:1001.1783v1) and Spiegelhofer–Wallner's 2016 preprint (arXiv:1604.07089v1) classify **counts** of binomial coefficients meeting various prime-power divisibility thresholds and their digit-word statistics. Neither the inspected statements nor the relevant arguments provide the distance between consecutive surviving positions, the complete **pooled nearest-neighbor histogram**, or its heavy-tail moment threshold. A published sharp theorem about the longest contiguous *run of retained positions* in each row also concerns a different extremal invariant; its own scope explicitly excludes complete run distributions. Its maximal run length does not yield the spacing spectrum here, which includes arbitrarily large distances across excluded blocks. The present counting uses Lucas directly but evaluates a different statistic involving ordering and all prime-power-length row ensembles.

## Limitations

The law is for nondivisibility modulo \(p\), not a higher power \(p^\alpha\) with \(\alpha>1\), nor for the values or signs of the nonzero binomial coefficients. Its limiting probability measure weighs each gap equally and rows according to their number of gaps. This is not a stationary infinite-row gap process or a uniformly weighted row limit. Elementary digit methods establish the law, but historical priority remains conditional on finding no implicit equivalent in older work on Pascal-triangle fractal spacing; a literature search is not a proof of novelty. No independent mathematical audit has been performed.

## References

1. É. Lucas, *Théorie des fonctions numériques simplement périodiques*, American Journal of Mathematics **1** (1878), 184–196, 197–240, 289–321 (digitwise binomial congruences).
2. N. J. Fine, *Binomial coefficients modulo a prime*, American Mathematical Monthly **54** (1947), 589–592.
3. E. Rowland, *The number of nonzero binomial coefficients modulo \(p^\alpha\)*, arXiv:1001.1783v1, publicly posted 2010-01-12; https://arxiv.org/abs/1001.1783.
4. L. Spiegelhofer and M. Wallner, *An explicit generating function arising in counting binomial coefficients divisible by powers of primes*, arXiv:1604.07089v1, publicly posted 2016-04-24; https://arxiv.org/abs/1604.07089.
5. *Sharp longest nondivisibility runs in Pascal rows modulo prime powers*, public result at https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-longest-nondivisibility-runs-in-pascal-rows-modulo-prime-p--e9c9cfbae1e4 (comparison source for a distinct extremal invariant).
