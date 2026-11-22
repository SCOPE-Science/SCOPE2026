# Square-root Abelian sampling complexity of growing two-run periods

## Finding
For \(h\ge1\), \(q>h\), and \(k\ge1\), consider the infinite periodic binary word \(\alpha_{q,h}=(1^h0^{q-h})^\omega\). Its Abelian maximal pattern complexity \(P_{q,h}(k)\) satisfies
\[
P_{q,h}(k)\le \min\left\{q,k+1,\left\lfloor\frac{1+\sqrt{1+8hk}}2\right\rfloor\right\}.
\]
If \(k\ge h\) and \(q\ge1+\lfloor\sqrt{2hk}\rfloor\), then
\[
1+\lfloor\sqrt{2hk}\rfloor-h\ \le P_{q,h}(k)\le\left\lfloor\frac{1+\sqrt{1+8hk}}2\right\rfloor.
\]
In particular, for each fixed \(h\), in this explicitly specified regime of growing period,
\[
P_{q,h}(k)=\sqrt{2hk}+O(h+1),\qquad \lim_{k\to\infty}\frac{P_{q,h}(k)}{\sqrt k}=\sqrt{2h}.
\]
The leading constant is sharp since the lower and upper inequalities have the same leading term.

## Assumptions and scope
A \(k\)-pattern is a set \(S\subseteq\mathbb N_0\) of exactly \(k\) distinct nonnegative indices. Translating it by \(n\ge0\) samples \(\alpha_{q,h}[n+S]\). Abelian equivalence on binary sampled words means equal numbers of ones. The quantity \(P_{q,h}(k)\) maximizes the cardinality of the attained one-count set over all such \(S\). The period need not be primitive for the argument. The upper bound is unconditional. The matching leading-order bounds require the displayed relation between \(k,h,q\); no assertion of exact complexity is made in general.

## Proof
Given a pattern \(S\), let \(c_j=|\{s\in S:s\equiv j\pmod q\}|\) for \(0\le j<q\). Each \(c_j\) is a nonnegative integer and \(\sum_j c_j=k\). Conversely, any nonnegative integer vector \(c\) of length \(q\) and total \(k\) is realized by a pattern, choosing the first \(c_j\) positive or nonnegative indices in residue class \(j\). For a shift \(n\), the number of ones sampled equals a cyclic sum of \(h\) successive coordinates of \(c\); as \(n\) varies modulo \(q\), every cyclic starting coordinate occurs. Thus, writing
\[
v_i=\sum_{a=0}^{h-1} c_{(i+a)\bmod q},\quad 0\le i<q,
\]
we have \(P_{q,h}(k)=\max_{c:\sum c_j=k}|\{v_i:0\le i<q\}|\). Crucially, \(\sum_i v_i=hk\), since each coordinate appears in exactly \(h\) cyclic windows.

Suppose the windows attain \(p\) distinct nonnegative integer values. The sum over at least one occurrence of each is at least \(0+1+\cdots+(p-1)=p(p-1)/2\). All other windows contribute nonnegative values, so \(p(p-1)\le2hk\). Solving this inequality for the nonnegative integer \(p\) gives \(p\le\lfloor(1+\sqrt{1+8hk})/2\rfloor\). Clearly \(p\le q\) and \(p\le k+1\), proving the upper bound.

Now assume \(k\ge h\) and set \(t=\lfloor\sqrt{2hk}\rfloor\). The inequality \(t\ge h\) follows from \(\sqrt{2hk}\ge\sqrt 2 h\). Under \(q\ge t+1\), construct
\[
c_j=\lfloor j/h\rfloor\ (0\le j<t),\qquad c_t=k-\sum_{j=0}^{t-1}\lfloor j/h\rfloor,
\]
with all subsequent coordinates zero. The remainder is nonnegative because \(\sum_{j<t}\lfloor j/h\rfloor\le t(t-1)/(2h)\le k\). For \(0\le i\le t-h\), the length-\(h\) window beginning at \(i\) lies wholly in coordinates \(0,\ldots,t-1\), and its sum is exactly \(i\). Indeed its initial sum is \(0\), and the increment between successive windows is \(c_{i+h}-c_i=1\) whenever both starts are in this range. Therefore the distinct window sums include every integer from \(0\) through \(t-h\), giving \(P_{q,h}(k)\ge t-h+1\). As \(k\to\infty\) with fixed \(h\), the two bounds differ from \(\sqrt{2hk}\) by at most \(O(h+1)\), yielding the stated sharp asymptotics.

## Verification
A self-contained Python program enumerates all nonnegative residue-multiplicity vectors in a small finite domain and computes their exact maximum window-count spectrum. It also verifies the constructive vector over 4,995 parameter triples and the upper and lower bounds over 168 exhaustively enumerated triples. Run \(\texttt{python3 verify.py}\) after extracting the files from this finding record; the expected output is recorded in \(\texttt{verification_output.txt}\). These tests check finite cases only; the mathematical conclusion for all parameters is supplied by the preceding proof.

## Relationship to prior work
Kamae, Widmer and Zamboni introduced Abelian maximal pattern complexity in 2013 and investigated recurrent aperiodic words. Zeng, Xue and Zeng (2026) establish general complexity bounds and aperiodicity criteria; their periodicity discussion gives qualitative boundedness at each fixed period, not the uniform two-parameter sharp square-root law above. The present result studies periodic two-run words as the period grows with the sample size and establishes a sharp leading coefficient determined by the marker-run length. No claim that a negative search proves novelty is made.

## Limitations
The formula does not determine the exact maximum for finite arbitrary \((q,h,k)\), and the sharp asymptotic needs the specified period-size condition. Priority remains subject to work not indexed by the searched databases, including general results on cyclic integer sliding-window sums. All verifications are finite and the work has not undergone independent audit.

## References
1. Q. Zeng, Y. Xue, C. Zeng, *Abelian maximal pattern complexity and extremal words*, arXiv:2609.28059v1 (first posted 2026-09-23), https://arxiv.org/abs/2609.28059.
2. T. Kamae, S. Widmer, L. Q. Zamboni, *Abelian maximal pattern complexity of words*, arXiv:1301.5113v1 (2013), https://arxiv.org/html/1301.5113v1.
