# Exact palindrome-pair complexity of binary two-run periodic words

## Finding

Let \(a,b\geq1\) and \(W=(0^a1^b)^\omega\), and write \(L=a+b\). The palindromic length \(\operatorname{PL}(u)\) is the minimum number of nonempty palindromes whose concatenation is the nonempty word \(u\). For each \(n\geq1\), let \(Q_{a,b}(n)\) be the number of **distinct** length-\(n\) contiguous factors \(u\) of \(W\) for which \(\operatorname{PL}(u)=3\). Then every factor of \(W\) has palindromic length at most three, and

\[
Q_{a,b}(n)=
\begin{cases}
0,&1\leq n\leq L+1,\\
2\displaystyle\sum_{s=1}^{a-1}\sum_{t=1}^{b-1}\mathbf{1}_{\{s+t\equiv n\pmod L\}},&n\geq L+2.
\end{cases}
\]

(The sum is empty when either upper limit is zero.) Equivalently, with \(z\) a formal variable,

\[
\sum_{n\geq1}Q_{a,b}(n)z^n
=\frac{2z^L}{1-z^L}
\left(\sum_{s=1}^{a-1}z^s\right)
\left(\sum_{t=1}^{b-1}z^t\right).
\]

For \(n\geq L\), the word \(W\) has exactly \(L\) distinct factors of length \(n\); consequently its exact palindrome-pair complexity (the number of distinct length-\(n\) factors with palindromic length at most two) is \(L-Q_{a,b}(n)\). All its factors are palindrome pairs **if and only if** \(\min(a,b)=1\); otherwise length \(L+2\) already has factors of palindromic length three. Over one complete period of factor lengths in the stable regime, the total number of length/starting-phase pairs requiring three palindromes is \(2(a-1)(b-1)\).

## Assumptions and scope

Letters \(0\) and \(1\) are distinct; \(a,b\) range over positive integers without bounds. Factors are ordinary contiguous strings, not scattered subsequences. Starting positions are considered modulo the primitive period \(L\). A palindrome is equal to its reversal and each part in a factorization is nonempty. We do not count different factorizations of the same word separately. For \(n\geq L\), period phases give distinct words; the formula for shorter lengths is zero independently of possible repetition among phase words.

## Proof

**1. Palindromic-length classification by run endpoints.** Fix a factor \(u\) and put \(x\in\{0,1\}\) for its initial letter and \(y\) for the other letter. Let \(A\) and \(B\) be the respective full run lengths of \(x\) and \(y\) in \(W\), so \(\{A,B\}=\{a,b\}\). If \(u\) has at most two maximal constant-letter runs, it is a concatenation of at most two constant palindromes.

If it has at least three runs and begins and ends in \(x\), it has the unique form
\[
u=x^s y^B(x^A y^B)^j x^t,
\qquad j\geq0,\quad1\leq s,t\leq A.
\]
If \(t\geq s\), factor it as the palindrome \(x^s y^B(x^A y^B)^j x^s\) followed by \(x^{t-s}\) (omit an empty second part). If \(s>t\), factor it as \(x^{s-t}\) followed by the palindrome \(x^t y^B(x^A y^B)^j x^t\). Thus it is a palindrome pair.

If \(u\) begins in \(x\), ends in \(y\), and has at least four runs, then
\[
u=x^s y^B(x^A y^B)^j x^A y^t,
\qquad j\geq0,\quad1\leq s\leq A,\quad1\leq t\leq B.
\]
If \(s=A\), the prefix \(x^A y^B(x^A y^B)^j x^A\) is a palindrome and the remaining \(y^t\) is another. If \(t=B\), the initial \(x^s\) is a palindrome and the suffix \(y^B(x^A y^B)^j x^A y^B\) is another.

When \(s<A\) and \(t<B\), there is nevertheless a three-palindrome factorization:
\[
u=\underbrace{x^s}_{\rm pal}\,
\underbrace{y^{B-t}}_{\rm pal}\,
\underbrace{y^t(x^A y^B)^j x^A y^t}_{\rm pal}.
\]
It cannot be a palindrome pair. Indeed, any nonempty palindrome prefix starts and ends in \(x\). It either ends inside the first \(x^s\) run or, after crossing the first \(y^B\) run, it must end exactly \(s\) letters into a complete \(x^A\) run (matching its initial \(x^s y\)). In the first case, the remaining suffix starts in \(x\) and ends in \(y\) unless the entire initial \(x\)-run was removed; in that latter subcase its initial complete \(y^B\) run has different length from its final \(y^t\) run, so it is not a palindrome. In the second case, the remaining suffix starts in the nonempty \(x^{A-s}\) and ends in \(y\), again not a palindrome. This excludes every possible cut into two nonempty palindromes.

Therefore \(\operatorname{PL}(u)=3\) **exactly** when \(u\) has at least four runs, begins and ends in opposite letters, and its first and last runs are both strict partial runs: \(1\leq s<A\), \(1\leq t<B\).

**2. Counting actual distinct factors.** Such a factor that begins in the \(0\)-run has initial length \(s\in\{1,\ldots,a-1\}\) and terminal length \(t\in\{1,\ldots,b-1\}\), so its length is \(n=kL+s+t\) for a unique integer \(k\geq1\). Conversely, each such \((k,s,t)\) gives exactly one starting phase and a three-palindrome factor. The same argument after interchanging the letters supplies another one for every pair. Since \(2\leq s+t\leq L-2\), the exponent \(k\) is uniquely determined by \(n\), and no such factors exist for \(n\leq L+1\). This proves both the coefficient formula and the formal generating function.

Finally, \(0^a1^b\) is primitive: a smaller repeating cyclic period would force at least four changes of letter per full word, whereas this word has exactly two cyclic changes. Therefore its \(L\) cyclic phases yield distinct length-\(L\) factors, hence distinct length-\(n\) factors for all \(n\geq L\). Counting starting phases is thus counting distinct factors. The threshold \(\min(a,b)=1\), the palindrome-pair complexity, and the period-sum statement follow immediately from the formula.

## Verification

The accompanying standalone `verify.py` independently enumerates phase factors, constructs a palindrome table and performs exact dynamic programming for minimum palindromic length. It checks \(a,b\in\{1,\ldots,9\}\) and all \(1\leq n\leq4(a+b)\): 3,240 parameter-length cases, 36,720 phase equivalences, and 36,720 checked words. It separately checks the predicted coefficient counts and distinctness of the \(L\) phases when \(n\geq L\). Command: `python3 verify.py`. These finite checks are a reproducibility cross-check; the preceding run decomposition proves the assertion for all parameters and lengths.

## Relationship to prior work

Borchert and Rampersad [1] study palindrome pairs, give a complete characterization of binary minimal non-palindrome pairs (Theorem 18), show any word with at most three runs is a palindrome pair (Lemma 13), and explicitly introduce palindrome-pair factor complexity (Section 6). Their classification of minimal obstructions is structurally stronger on arbitrary binary words, so it is relevant prior coverage for membership questions. However, that classification does not state the exact two-parameter, length-by-length **factor count** for the periodic sources considered here, or the convolution formula and sharp run-length threshold. Our proof derives these independently by run endpoints, rather than asserting a new global classification of minimal obstructions. Frid–Laborde–Peltomäki [2] and Bulgakova–Frid–Scanvic [3] analyze prefix palindromic length in automatic words, whereas the result here enumerates palindromic lengths of **all distinct factors** of a periodic two-run word.

## Limitations

The theorem is for exactly one constant run of each binary letter per primitive period. It does not yield a corresponding formula for arbitrary periodic words, aperiodic automatic words, or counts of individual optimal palindrome factorizations. The originality comparison does not rule out an obscure specialization of the general minimal-non-palindrome-pair theory. No claim is made to settle the broader conjectures or open problems in [1]–[3].

## References

1. Adam Borchert and Narad Rampersad, *Words with many palindrome pair factors*, arXiv:1509.05396 (first posted 2015-09-17), https://arxiv.org/abs/1509.05396. Especially Lemma 1, Lemma 13, Theorem 18, and Section 6.
2. Anna E. Frid, Enzo Laborde, and Jarkko Peltomäki, *On prefix palindromic length of automatic words*, arXiv:2009.02934 (first posted 2020-09-07), https://arxiv.org/abs/2009.02934.
3. Dora V. Bulgakova, Anna E. Frid, and Jérémy Scanvic, *Prefix palindromic length of the Sierpinski word*, arXiv:2201.09556 (first posted 2022-01-24), https://arxiv.org/abs/2201.09556.
