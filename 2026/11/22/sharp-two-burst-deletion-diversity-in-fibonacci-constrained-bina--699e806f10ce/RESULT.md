# Sharp two-burst deletion diversity in Fibonacci-constrained binary words

## Finding
For each integer \(n\ge2\), let \(\mathcal F_n\) be the set of indexed binary words of length \(n\) containing no factor `11`. For \(w\in\mathcal F_n\), let \(\mathcal D_2(w)\) be the set of **distinct** length-\(n-2\) words obtained by deleting exactly one pair of adjacent symbols, and put
\[
F_n(u)=\sum_{w\in\mathcal F_n}u^{|\mathcal D_2(w)|-1}.
\]
The entire deletion-diversity spectrum has the rational generating function
\[
\boxed{\sum_{n\ge2}F_n(u)z^{n-2}
=\frac{3+2uz+(u^2+2u-3)z^2}{1-z-z^2-(u^2-1)z^3}.}
\]
In particular, the maximum number of different burst-deletion outcomes is
\[
\boxed{\max_{w\in\mathcal F_n}|\mathcal D_2(w)|=1+\left\lfloor\frac{2(n-1)}3\right\rfloor.}
\]
The exact number \(E_n\) of maximizing indexed words is
\[
\boxed{E_{3h}=2\ (h\ge1),\qquad E_{3h+1}=1\ (h\ge1),\qquad E_{3h+2}=h+3\ (h\ge0).}
\]
For uniformly sampled \(W_n\in\mathcal F_n\), a corresponding typical-source result is
\[
\mathbb E[|\mathcal D_2(W_n)|]
=\left(\frac{3\sqrt5}{5}-1\right)n+O(1).
\]

## Assumptions and scope
Words are linear and indexed (not necklaces); the alphabet is exactly \(\{0,1\}\). The forbidden factor `11` may not occur anywhere in the source. A deletion removes **exactly two consecutive** source symbols and leaves the remaining order intact. All possible deletion positions are allowed, and coincident resulting strings are counted once. All statements hold for every integer \(n\ge2\), including the empty received word at \(n=2\). No claim is made about correcting arbitrary two deletions, codebook capacity, or other alphabets.

## Proof
**Collision lemma.** Write \(w=w_1\cdots w_n\) and \(y_i=w_1\cdots w_{i-1}w_{i+2}\cdots w_n\) for deleting positions \(i,i+1\), with \(1\le i\le n-1\). For \(1\le i<j\le n-1\), comparison of the output coordinates between the two deletion locations gives
\[
y_i=y_j\quad\Longleftrightarrow\quad
w_s=w_{s+2}\ \text{for every }i\le s<j.
\]
Consequently, equal outputs are exactly the constant intervals in the ordered deletion-location list; outputs cannot reappear after an intervening change. Thus
\[
|\mathcal D_2(w)|-1=\sum_{i=1}^{n-2}[w_i\ne w_{i+2}]. \tag{1}
\]
This identity also follows from the interleaved-run formula for burst-deletion balls and is **not** claimed as a new general identity.

**Exact spectrum.** Encode each admissible length-two suffix by one of `00`, `01`, and `10`. When appending a bit \(c\) to a suffix \(ab\), the no-`11` constraint allows the transition \(ab\to bc\) exactly if \(bc\ne11\), and formula (1) adds one to the exponent precisely if \(a\ne c\). With the states ordered (`00`,`01`,`10`), the weighted transition matrix is
\[
T(u)=\begin{pmatrix}1&u&0\\0&0&1\\u&1&0\end{pmatrix},\qquad
F_n(u)=(1,1,1)T(u)^{n-2}(1,1,1)^\mathsf T.
\]
The characteristic polynomial of \(T(u)\) is \(x^3-x^2-x-u^2+1\). Cayley--Hamilton yields
\[
F_{n+3}(u)=F_{n+2}(u)+F_{n+1}(u)+(u^2-1)F_n(u)
\quad(n\ge2).
\]
Directly evaluating the three initial cases gives \(F_2=3\), \(F_3=3+2u\), and \(F_4=3+4u+u^2\). Solving the recurrence as an ordinary generating function establishes the displayed rational fraction.

**Sharp maximum and its multiplicity.** Write \(d_n=\deg F_n\) and \(a_n=[u^{d_n}]F_n\). The recurrence and the three initial cases give by induction
\[
\begin{array}{c|c|c}
 n& d_n&a_n\\\hline
3h\ (h\ge1)&2h-1&2\\
3h+1\ (h\ge1)&2h&1\\
3h+2\ (h\ge0)&2h&h+3.
\end{array}
\]
Indeed, in residue classes \(n\equiv0,1\pmod3\), the highest-degree contribution to \(F_{n+3}\) comes solely from \(u^2F_n\); in residue class \(n\equiv2\pmod3\), it comes from both \(u^2F_n\) and \(F_{n+2}\), increasing the top coefficient by one. The negative term \(-F_n\) is always strictly below the resulting top degree. Formula (1) then shows that the maximum deletion-ball cardinality is \(1+d_n\), and that the number of extremizers is \(a_n\).

An explicit description checks the count independently. If \(n=3h\), the two maximizers are the \(h\)-fold repetitions of `001` and `100`. If \(n=3h+1\), the unique maximizer is the \(h\)-fold repetition of `100` followed by `1`. If \(n=3h+2\), three maximizers are obtained by (i) repeating `001` \(h\) times and appending `00`, (ii) repeating `100` \(h\) times and appending `10`, and (iii) prepending `0` and appending `1` to the \(h\)-fold repetition of `100`. The remaining \(h\) maximize by beginning and ending with `1` and placing \(h\) inter-one gaps, all with two zeros except one chosen gap with three zeros. These families are distinct, attain the stated top degree by (1), and exhaust the total top coefficient. For \(h=0\), the three length-two sources are obtained from the three basic families.

**Typical-source asymptotic.** Setting \(u=1\) gives \(F_n(1)=\operatorname{Fib}(n+2)\), with \(\operatorname{Fib}(0)=0\), \(\operatorname{Fib}(1)=1\). Differentiating the displayed rational generating function at \(u=1\) gives
\[
\sum_{n\ge2}F'_n(1)z^{n-2}
=\frac{2z+4z^2}{1-z-z^2}
+\frac{2z^3(3+2z)}{(1-z-z^2)^2}.
\]
The unique dominant positive pole occurs at \(\rho=(\sqrt5-1)/2\); the second summand has a double pole, and the first a simple pole. Coefficient comparison with \(\sum F_n(1)z^{n-2}=(3+2z)/(1-z-z^2)\) yields \(\mathbb E[|\mathcal D_2(W_n)|-1]=(3/\sqrt5-1)n+O(1)\), proving the final display.

## Verification
The standalone standard-library program `verify.py` enumerates every no-`11` word at lengths 2 through 18 (17,706 words in total), obtains **literal distinct** two-burst-deletion outputs, independently computes the lag-two mismatch count, and compares both with the three-state transfer polynomial. It also checks the scalar polynomial recurrence, Fibonacci total counts, maximizing degrees and multiplicities for all lengths through 250. The reproducible invocation is `python3 verify.py`, which completed with `VERIFY_OK`. These finite tests verify the implementation and boundary cases; the all-length assertions follow from the proof above, not from extrapolation of finite enumeration.

## Relationship to prior work
The general identity for the size of a binary fixed-length burst-deletion ball is credited to Levenshtein's 1967 work and is explicitly restated as equation (2) in Schoeny, Wachter-Zeh, Gabrys and Yaakobi (arXiv:1602.06820, originally public February 22, 2016). Kulkarni and Kiyavash (arXiv:1211.3128, originally public November 13, 2012) motivate constrained-source error-channel enumeration, while Cheng and collaborators (ISIT 2014) concern correction of bursts of at least three adjacent symbols. The result proved here specializes to the Fibonacci source forbidding `11` and determines its **entire two-burst deletion-ball volume distribution, sharp maximum, and exact multiplicities for every length**. The known universal ball formula alone does not state these spectrum or extremizer results.

## Limitations
This is a same-source diversity theorem, not a maximal zero-error codebook construction or an all-channel capacity theorem. The expectation is with respect to the uniform distribution over the constrained source language. General methods for finite-state weighted enumeration are well established; the contribution is the explicit closed spectrum and sharp residue-class optimization for this specific natural constrained channel. An unindexed earlier equivalent remains possible.

## References
1. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128 (initial public posting November 13, 2012), https://arxiv.org/abs/1211.3128.
2. C. Schoeny, A. Wachter-Zeh, R. Gabrys, E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, arXiv:1602.06820 (initial public posting February 22, 2016), https://arxiv.org/abs/1602.06820.
3. L. Cheng, T. G. Swart, H. C. Ferreira, K. A. S. Abdel-Ghaffar, *Codes for Correcting Three or More Adjacent Deletions or Insertions*, ISIT 2014, https://doi.org/10.1109/ISIT.2014.6875032.
4. V. I. Levenshtein, *Asymptotically optimum binary code with correction for losses of one or two adjacent bits*, Problemy Kibernetiki 19 (1967), 293–298; bibliographic details cited in References 2 and 3.
