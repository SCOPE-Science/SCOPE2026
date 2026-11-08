# Sharp progression packing and polynomial arithmetic complexity for power-support words

## Finding
Fix an integer base \(b\ge2\). Let \(w_b\) be the binary automatic word with \(w_b(t)=1\) exactly when \(t=b^e\) for some integer \(e\ge0\), and zero otherwise, for \(t\ge0\). Let \(\mathcal A_b(n)\) be the set of length-\(n\) binary words \((w_b(a+jd))_{0\le j<n}\) for all integers \(a\ge0\) and \(d\ge1\). Write \(P_b(n)=|\mathcal A_b(n)|\), and let \(H_b(n)\) be the largest number of ones in one such word.

**Theorem.** For every integer \(b\ge2\) and \(n\ge1\),
\[
H_b(n)=1+\left\lfloor\log_b\bigl(1+(b-1)(n-1)\bigr)\right\rfloor.
\]
Equivalently, the least window length containing at least \(r\ge1\) ones along an arithmetic progression is
\[
L_b(r)=1+\frac{b^{r-1}-1}{b-1}.
\]
For every \(r\ge3\), the **unique** binary arithmetic-progression factor of length \(L_b(r)\) with \(r\) ones has its ones at the zero-based positions
\[
0,\quad 1,\quad 1+b,\quad\ldots,\quad 1+b+\cdots+b^{r-2}.
\]
Every arithmetic progression giving this extremal factor has initial value \(b^e\) and step \(b^e(b-1)\) for some integer \(e\ge0\). For \(r=1,2\), the shortest factors are respectively `1` and `11`, without the claimed rigidity of progressions for \(r=2\).

In addition, for every \(n\ge2\),
\[
P_b(n)\le 1+n+\binom n2\left(1+2\left\lfloor\log_b(n-1)\right\rfloor\right).
\]
In particular, \(P_b(n)=O_b(n^2\log(n+1))\), an explicit polynomial bound for the arithmetic-subword complexity of this sparse automatic family.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). The indexing starts at zero; the support consists of the positive powers \(1,b,b^2,\ldots\), excluding zero. Sampling is along an arithmetic progression \(a,a+d,\ldots,a+(n-1)d\) with unrestricted nonnegative integer origin and strictly positive integer step. The count \(P_b(n)\) counts **distinct binary sampled words**, not progressions or occurrences. The upper bound on \(P_b(n)\) is not claimed sharp, and no exact formula for \(P_b(n)\) is asserted.

## Proof
Let a sampled word contain \(r\ge2\) ones, coming from selected distinct powers \(b^{e_0}<b^{e_1}<\cdots<b^{e_{r-1}}\). Put \(E=e_{r-1}-e_0\) and
\[
g=\gcd(e_1-e_0,\ldots,e_{r-1}-e_0)\ge1.
\]
The elementary identity \(\gcd(b^u-1,b^v-1)=b^{\gcd(u,v)}-1\) (obtained by the Euclidean algorithm) implies
\[
\gcd_{1\le i<r}(b^{e_i}-b^{e_0})=b^{e_0}(b^g-1).
\]
If the progression step is \(d\), all the differences on the left are multiples of \(d\). Therefore, writing \(j_0<j_{r-1}\) for the first and last sampled-one positions,
\[
j_{r-1}-j_0=\frac{b^{e_{r-1}}-b^{e_0}}{d}
\ge \frac{b^E-1}{b^g-1}
=\sum_{t=0}^{E/g-1}b^{tg}
\ge\sum_{t=0}^{r-2}b^t.
\]
The last inequality uses the fact that the \(r\) exponent differences are distinct multiples of \(g\), so \(E/g\ge r-1\); also \(g\ge1\). Since \(j_{r-1}-j_0\le n-1\), the proposed lower bound on \(L_b(r)\) follows. It is attained by \(a=b^e\) and \(d=b^e(b-1)\), for the sampled positions of consecutive powers \(b^e,\ldots,b^{e+r-1}\). The displayed exact formula for \(H_b(n)\) follows by inverting these sharp thresholds, including \(r=1\).

If \(r\ge3\), equality in the lower bound forces both \(E/g=r-1\) and \(g=1\): for \(r-1\ge2\), either an extra term or a larger exponent strictly raises the positive sum. Hence the selected exponents are consecutive and the step must equal their difference gcd \(b^{e_0}(b-1)\). At the minimum possible window length, the first and last ones must occupy its endpoints. This proves both uniqueness of the binary pattern and rigidity of the realizing progressions.

For the complexity bound, consider a factor of length \(n\ge2\) with at least three ones. Its first and last one exponents differ by \(E\ge2\). Since at least one intermediate exponent difference is strictly between zero and \(E\), the gcd \(g\) is a proper divisor of \(E\), so \(g\le E/2\). The earlier estimate gives
\[
n-1\ge\frac{b^E-1}{b^g-1}\ge b^{E-g}\ge b^{E/2}.
\]
Thus \(E\le2\lfloor\log_b(n-1)\rfloor\). Let \(i<j\) be the first two one positions, and let their exponent difference be \(p\). The data \((i,j,p)\) determine all subsequent one positions: a power of exponent \(e_0+s\), for integer \(s\ge0\), belongs to the progression exactly at the position
\[
i+(j-i)\frac{b^s-1}{b^p-1}
\]
when this expression is an integer in the sampling window. No smaller exponent can give a one after the first, and by definition no one occurs before it. Hence a factor with at least three ones is uniquely determined by some triple \((i,j,p)\) with \(0\le i<j<n\) and \(1\le p\le2\lfloor\log_b(n-1)\rfloor\). There are at most \(\binom n2\,2\lfloor\log_b(n-1)\rfloor\) such triples. Factors with zero, one, or two ones contribute at most \(1+n+\binom n2\) further possibilities. Adding the bounds proves the formula and completes the proof.

## Verification
The standalone standard-library script `verify.py` independently enumerates selected sets of power exponents and checks sharp minimum spans, including the complete equality family, for bases \(2\) through \(9\), selected-set sizes \(3\) through \(6\), and exponents below \(12\). It additionally tests \(2{,}898{,}000\) direct arithmetic-progression windows for bases \(2\) through \(7\) and lengths \(1\) through \(25\). The observed output is:

`VERIFY_OK exponent_sets=19448 exact_minimizers=272 sample_windows=2898000 maxima_cases=150`

These are finite consistency checks only; the proof above supplies the infinite quantifiers. Reproduce with `python3 verify.py` in the directory containing this document and the script.

## Relationship to prior work
Konieczny and Müllner, *Arithmetical subword complexity of automatic sequences* (first posted September 6, 2023), develop a general classification by effective alphabet size and derive bounds on arithmetic complexity up to subexponential factors. Their Theorem A gives \(r^n\le P(n)\le r^n\exp(o(n))\) for a suitable effective-alphabet parameter, but does not explicitly evaluate the fixed-base powers-of-\(b\) characteristic word's maximal arithmetic Hamming weight, rigid shortest witnesses, or the stated quadratic-logarithmic bound. The current result is an exact fixed-family refinement, not a claim to supersede the general theorem.

The 2026 work *Abelian maximal pattern complexity and extremal words* examines a different, maximized pattern-equivalence invariant of sparse indicator words. Its binary example with support \(\{2^j-1\}\) exhibits a related logarithmic prefix bound, but does not assert an upper bound across arbitrary positive-step progressions of the fixed power-support word, nor the all-base arithmetic complexity estimate. A separate published logarithmic support-envelope result likewise concerns Abelian pattern Sturmian words, not this arithmetic sampling language.

Earlier studies of ordinary contiguous factors of power-support words do not determine the arithmetic-progression factors with arbitrary steps. The precise result could still have an unindexed equivalent; the literature comparison is best-knowledge rather than a proof of uniqueness.

## Limitations
The polynomial upper bound is not matched with a lower bound of the same order; the exact enumeration of all arithmetic factors remains open here. Nothing is claimed about polynomial samples of degree above one, arbitrary geometric sets, or bases below two. Searches for prior equivalents are incomplete in principle; independent verification of novelty and correctness has not been performed.

## References
1. J. Konieczny and C. Müllner, *Arithmetical subword complexity of automatic sequences*, arXiv:2309.03180, first version September 6, 2023, https://arxiv.org/abs/2309.03180 (primary text and Theorem A inspected).
2. Q. Zeng, Y. Xue, and C. Zeng, *Abelian maximal pattern complexity and extremal words*, arXiv:2609.28059, first version September 23, 2026, https://arxiv.org/abs/2609.28059 (different pattern-equivalence invariant).
