# Two-term logarithmic growth of the semi-Pell sequence at odd indices

## Finding
Let \(s(0)=0\), \(s(1)=1\), and for every integer \(t\ge1\) define
\[
s(2t)=s(t),\qquad s(2t+1)=2s(2t)+s(2t-1).
\]
As the positive odd integer \(n\) tends to infinity,
\[
\boxed{\log_2 s(n)=\frac{(\log_2 n)^2}{2}-(\log_2 n)\log_2(\log_2 n)+O(\log n).}
\]
In particular, the second-order term is \(- (\log_2 n)\log_2(\log_2 n)\), with coefficient exactly \(-1\). Equivalently, for every sufficiently large integer \(k\), the last odd term in the dyadic interval satisfies
\[
\log_2 s(2^k-1)=\frac{k^2}{2}-k\log_2 k+O(k).
\]
The constants implicit in the error terms are absolute. All logarithms without an explicit base are natural logarithms.

## Assumptions and scope
Only the recursion above and elementary counting are used. The estimate concerns positive **odd** arguments: for every \(r\ge0\), \(s(2^r n)=s(n)\), so a uniform assertion over all positive indices would be false. Every asymptotic quantifier refers to odd positive integers increasing without bound. The associated combinatorial objects are binary overpartitions, meaning partitions into powers of two in which each occupied size occurs an odd positive number of times, with each occupied size optionally marked at most once; the largest occupied size is required to be marked.

## Proof
**Step 1 (exact overpartition model).** Let \(f(n)\) count the overpartitions just defined; put \(f(0)=0\). There is one object of weight one. At even weight \(2t\), size one cannot occur because its multiplicity, if present, would be odd. Dividing every part by two gives a bijection with objects of weight \(t\), so \(f(2t)=f(t)\). At odd weight \(2t+1>1\), the number of unit parts is odd. If it is one, deleting the unit yields an object of weight \(2t\); the deleted unit had two possible marking statuses, since the largest size was greater than one. If it is at least three, deleting two units preserves all marking statuses and yields an object of weight \(2t-1\). Both operations are reversible and have disjoint images. Consequently
\[
f(2t+1)=2f(2t)+f(2t-1).
\]
The initial values and recurrences agree, hence \(f(n)=s(n)\) for all nonnegative \(n\). In addition,
\[
s(2t+1)-s(2t-1)=2s(t)>0,
\]
so the odd-index subsequence is strictly increasing.

**Step 2 (sharp logarithmic upper bound).** Let \(p_2(n)\) count the unrestricted partitions of \(n\) into powers of two. For \(0<n<2^k\), forgetting the optional markings maps the objects counted by \(s(n)\) into partitions counted by \(p_2(n)\), and at most \(k\) sizes can be occupied. Thus \(s(n)\le2^k p_2(n)\). For any \(u>0\), coefficient positivity in the product generating function gives
\[
p_2(n)\le e^{un}\prod_{i\ge0}(1-e^{-u2^i})^{-1}.
\]
Take \(u=k/2^k\) and \(J=k-\lceil\log_2 k\rceil\) for integers \(k\ge2\). The quantities \(u2^{J+j}\) are between \(2^{j-1}\) and \(2^j\). Hence the product over \(i\ge J\) is bounded above by the absolute convergent constant
\[
C=\prod_{j\ge0}(1-e^{-2^{j-1}})^{-1}<\infty.
\]
For \(i<J\), \(u2^i\le1\), and concavity gives \(1-e^{-x}\ge(1-e^{-1})x\) for \(0\le x\le1\). It follows that
\[
\begin{aligned}
\log_2 s(n)
&\le k+\frac{k}{\log 2}+\log_2 C
 +\sum_{i=0}^{J-1}\big(k-i-\log_2 k-\log_2(1-e^{-1})\big)\\
&=\frac{k^2}{2}-k\log_2 k+O(k),
\end{aligned}
\]
uniformly for \(0<n<2^k\). The equality follows from \(J=k-\log_2 k+O(1)\); terms of size \((\log k)^2\) are absorbed into \(O(k)\).

**Step 3 (matching constructive lower bound).** For any integer \(k\ge8\), put \(r=k-\lceil\log_2 k\rceil-2\), so \(r\ge1\). Independently choose integers
\[
0\le j_i\le\left\lfloor\frac{2^{k-i}}{8k}\right\rfloor,
\qquad 1\le i\le r.
\]
Use exactly \(2j_i+1\) copies of \(2^i\), for each chosen \(i\), and fill the remainder of \(2^k-1\) with units. The number used before adding units is at most
\[
\sum_{i=1}^{r}(2j_i+1)2^i
\le 2^{r+1}+\frac{r2^k}{4k}
\le\frac{2^k}{2k}+\frac{2^k}{4}<2^k-1.
\]
The remaining number of units is therefore positive and odd. Mark the largest occupied size \(2^r\) and no smaller sizes. Each choice gives a distinct legal overpartition of \(2^k-1\); no general asymptotic theorem for unrestricted binary partitions is used for this lower bound. Therefore
\[
\begin{aligned}
\log_2 s(2^k-1)
&\ge\sum_{i=1}^r\log_2\left(1+\left\lfloor\frac{2^{k-i}}{8k}\right\rfloor\right)\\
&\ge rk-\frac{r(r+1)}2-r\log_2(8k)\\
&=\frac{k^2}{2}-k\log_2 k-O(k).
\end{aligned}
\]
The second inequality uses \(1+\lfloor x\rfloor\ge x\) for every positive real \(x\).

**Step 4 (all odd arguments).** If \(2^{k-1}\le n<2^k\) and \(n\) is odd, monotonicity implies \(s(2^{k-1}-1)\le s(n)\le s(2^k-1)\). Apply Steps 2 and 3 with indices \(k\) and \(k-1\). Both endpoints have logarithm \(k^2/2-k\log_2 k+O(k)\), because their leading expressions differ by \(O(k)\). Finally, since \(\log_2 n=k+O(1)\), substitution changes the expression by only \(O(k)\), proving the claim.

## Verification
The standalone Python 3 file `semi_pell_growth_verify.py` uses only the standard library. It independently counts the marked odd-multiplicity binary partitions through weight 512 and checks equality with the defining recurrence at every weight. It verifies strict odd-index monotonicity in this range. At dyadic endpoints for \(8\le k\le19\), it checks the explicit constructive lower count and a coarse unconditional upper count directly against the recurrence values. Run with `python3 semi_pell_growth_verify.py`. These finite tests do **not** establish an infinite asymptotic. Steps 1–4 above provide that proof.

## Relationship to prior work
Keith and Munagi's 2019 semi-Pell composition paper defines the same recurrence and gives its composition interpretation. Ballantine and Beck (2023, Section 6) establish a marked odd-binary-overpartition interpretation; their concluding discussion explicitly raises comparison of the growth rates of odd-index self-similar sequences. Keith and Munagi's later account of power compositions gives further generating functions and congruences, not the displayed two-term logarithmic estimate. Classical Mahler–de Bruijn asymptotics for unrestricted binary partitions furnish bounds on \(p_2(n)\), but an upper bound for a superset alone cannot give the required sharp lower bound for the restricted semi-Pell family. The construction in Step 3 closes that gap. The second-order coefficient is not determined by a first-order estimate with error \(O(k\log k)\).

## Limitations
The formula leaves an error \(O(\log n)\); it does not identify the constant multiplying \(\log n\), any bounded oscillatory correction, or the asymptotic ratios among all the different self-similar sequences. Ordinary even indices are excluded for the stated divisibility reason. No claim of exhaustive literature priority or independently certified proof is made.

## References
1. W. J. Keith and A. O. Munagi, *Binary Compositions and Semi-Pell Compositions*, arXiv:1912.11148v1 (first posted 2019-12-23), https://arxiv.org/abs/1912.11148.
2. C. Ballantine and G. Beck, *Partitions Enumerated by Self-Similar Sequences*, arXiv:2303.11493v1 (2023-03-20), Section 6 and concluding remarks, https://arxiv.org/html/2303.11493.
3. W. J. Keith and A. O. Munagi, *Power Compositions and Semi-Pell Compositions*, *Online Journal of Analytic Combinatorics* 18 (2023), paper 2, https://combinatorialpress.com/article/ojac/vol18/276.pdf.
4. N. G. de Bruijn, *On Mahler's Partition Problem*, *Indagationes Mathematicae* 10 (1948), 210–220; classical asymptotics for unrestricted binary partitions (comparison only).
