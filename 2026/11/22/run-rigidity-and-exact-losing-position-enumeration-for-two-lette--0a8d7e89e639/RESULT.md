# Run-rigidity and exact losing-position enumeration for two-letter two-sided word subtraction

## Finding
Let \(\Sigma=\{a,b\}\). Consider the impartial normal-play game on finite binary words in which a move may either (i) remove a nonempty **prefix ending in the contiguous pair** \(ab\), or (ii) remove a nonempty **suffix beginning in the contiguous pair** \(ba\). Equivalently, the two-sided word-subtraction languages are \(S=\Sigma^*ab\) and \(T=ba\Sigma^*\).

**Theorem.** The set of losing positions, including the empty word, is exactly the regular language
\[
\mathcal P=b^*\ \cup\ a^+(b^{\ge2}a^+)^*.
\]
Thus a nonunary losing word starts and ends in \(a\), and each of its maximal \(b\)-runs has length at least two. If \(p_n=|\mathcal P\cap\Sigma^n|\), then \(p_0=1\) and, for every \(n\ge1\),
\[
p_n=1+\sum_{j=0}^{\lfloor(n-1)/3\rfloor}\binom{n-j-1}{2j},
\qquad
\sum_{n\ge0}p_nz^n
=\frac{1}{1-z}+\frac{z(1-z)}{1-2z+z^2-z^3}
=\frac{1-z-z^2}{1-3z+3z^2-2z^3+z^4}.
\]
In addition, if \(G(w)\) is the Sprague–Grundy value, then
\[
\max_{w\in\Sigma^n}G(w)=\left\lfloor\frac n2\right\rfloor\qquad(n\ge0),
\]
with equality for the alternating word beginning in \(a\) of each length \(n\). In particular the losing-position density among uniformly sampled length-\(n\) binary words decays exponentially: \(p_n/2^n\to0\). More precisely, \(p_n\sim C\lambda^n\), where \(\lambda\approx1.7548776662\) is the positive root of \(\lambda^3-2\lambda^2+\lambda-1=0\), and \(C=(1-\lambda^{-1})/(2-2\lambda^{-1}+3\lambda^{-2})\approx0.234486766\).

## Assumptions and scope
Words are finite, including \(\varepsilon\); deletion is always from an *end*, never from the middle. The deleted prefix is any word in \(\Sigma^*ab\), and the deleted suffix any word in \(ba\Sigma^*\). Both deleted portions have length at least two. In normal play a position with no legal move is losing; \(G(w)=\operatorname{mex}\{G(v):w\to v\}\). The theorem is exact for all \(n\), without a length cutoff. The structural result does not assert a closed formula for \(G(w)\) at every individual word.

## Proof
**(1) No move between proposed losing words.** Pure \(b\)-words have no occurrences of \(ab\) or \(ba\), hence are terminal. Suppose \(w\in a^+(b^{\ge2}a^+)^*\). Each occurrence of \(ab\) crosses from an \(a\)-run to the first letter of a \(b\)-run. Deleting a prefix ending at such an occurrence leaves a word beginning in \(b\) and ending in \(a\), hence outside \(\mathcal P\). Each occurrence of \(ba\) crosses from the last letter of a \(b\)-run to the following \(a\)-run. Deleting a suffix beginning at this occurrence leaves a word starting in \(a\) and ending in \(b\), again outside \(\mathcal P\). Thus no proposed losing position moves to another.

**(2) Every other word moves into the proposed set.** Fix \(w\notin\mathcal P\). If \(w\) begins in \(b\), then it contains an \(a\) (otherwise it would belong to \(b^*\)). Let \(ba\) straddle the beginning of its first \(a\)-run. Deleting the suffix beginning at that \(b\) leaves a pure \(b\)-word. If instead \(w\) begins in \(a\) and ends in \(b\), delete the prefix ending at the \(ab\) transition into the final \(b\)-run; the remainder is pure \(b\). In the remaining case \(w\) begins and ends in \(a\), but is not in \(a^+(b^{\ge2}a^+)^*\), so it has a singleton maximal \(b\)-run. Choose the *leftmost* such run, and delete the suffix starting with the \(ba\) at that singleton and the next \(a\). The remaining prefix starts and ends in \(a\), and every earlier \(b\)-run is of length at least two, so it lies in \(\mathcal P\). This exhausts the complement. By the standard normal-play recursive P/N characterization and induction on length, \(\mathcal P\) is exactly the losing language.

**(3) Enumeration.** The class \(b^*\) contributes \((1-z)^{-1}\). The other disjoint class has a nonempty \(a\)-run, followed by zero or more pairs consisting of a \(b\)-run of length at least two and a nonempty \(a\)-run. Hence its generating function is
\[
\frac{z/(1-z)}{1-[z^2/(1-z)] [z/(1-z)]}=
\frac{z(1-z)}{(1-z)^2-z^3}.
\]
For a word with exactly \(j\) positive \(b\)-runs in the second class, there are \(j+1\) positive \(a\)-runs and \(j\) \(b\)-runs of length at least two. After subtracting their minimum lengths, the slack \(n-(3j+1)\) is distributed among \(2j+1\) runs. Stars-and-bars gives \(\binom{n-j-1}{2j}\) when \(n\ge3j+1\), and zero otherwise. This proves the finite sum and rational identity.

**(4) Sharp maximal Grundy number.** Every legal move reduces word length by at least two. Strong induction shows \(G(w)\le\lfloor|w|/2\rfloor\), since every option has Grundy value at most \(\lfloor(|w|-2)/2\rfloor\) and the mex of such values is at most \(\lfloor|w|/2\rfloor\). Let \(u_n\) be the length-\(n\) prefix of \(ababab\cdots\). For every \(1\le j\le\lfloor n/2\rfloor\), deleting its first \(2j\) letters is legal because the removed prefix ends in \(ab\). The remaining suffix is \(u_{n-2j}\). By induction its Grundy value is \(\lfloor(n-2j)/2\rfloor\); these options realize each value from zero through \(\lfloor n/2\rfloor-1\). Together with the upper bound, the mex is exactly \(\lfloor n/2\rfloor\).

**(5) Exponential estimate.** The proper rational part of the generating function has denominator \(1-2z+z^2-z^3\), whose smallest-modulus root is the positive real \(\rho=\lambda^{-1}\approx0.569840291\). Its two other roots have greater modulus. Extracting the residue of the simple positive pole yields the displayed \(C\); the \(b^*\) contribution is just one word at each length. Since \(\lambda<2\), \(p_n/2^n\to0\).

## Verification
The included finite checker `verification/verify_outcomes.py` recursively computes every legal option and every mex, enumerates all \(262143\) binary words of lengths \(0\) through \(17\), and checks the losing-language criterion as well as the maximum nimber for every length. `verification/verify_enumerator.py` separately compares the binomial sum with the rational-series recurrence for lengths \(0\) through \(200\), and checks the alternating-word nimber formula through length \(100\). Output files `verification/verify_outcomes.txt` and `verification/verify_enumerator.txt` record the successful runs. The all-length result rests on the proof above, not on extrapolation from these checks.

## Relationship to prior work
Inoue and Inazu's *Word Subtraction Games*, arXiv:2611.09157v1 (first public arXiv posting November 6, 2026), Section 5.1 introduces the two-sided game \(\operatorname{WordSubtraction}(S,T)\). Their one-letter trigger \(S=\Sigma^*a\), \(T=b\Sigma^*\) has the **nonregular Dyck** losing language. Their open Problem 5.1 asks how to extend such a characterization to word triggers and explicitly notes overlap complications. The present result treats the first overlapping pair of two-letter opposite transitions, \(U=ab\), \(V=ba\); it gives a **regular run language**, an exact enumeration and a sharp Grundy extremum. It does not solve the arbitrary \(U,V\) problem. In particular the regularity theorem for *one-sided* regular subtraction sets cannot directly imply this two-sided classification; the same note exhibits non-context-free losing languages for some regular two-sided sets.

## Limitations
This is an exact solution for one canonical nontrivial overlapping trigger pair, not a classification of all pairs of words, all regular trigger languages, or all individual Grundy values. Source comparisons concern inspected available literature and are not a proof of global priority. The numerically checked ranges support implementation fidelity but do not substitute for the inductive argument.

## References
1. Y. Inoue and H. Inazu, *Word Subtraction Games*, arXiv:2611.09157v1, November 6, 2026; in particular Section 5.1 (two-sided subtraction, Timber/Dyck case, End-Nim counterexample, and Problem 5.1). https://arxiv.org/abs/2611.09157
