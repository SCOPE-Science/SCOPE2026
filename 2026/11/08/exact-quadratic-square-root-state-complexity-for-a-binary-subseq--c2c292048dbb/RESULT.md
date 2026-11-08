# Exact quadratic square-root state complexity for a binary subsequence ideal

## Finding
Fix any integer \(b\ge 1\), and let \(\preceq\) denote the scattered-subsequence order on binary words. Define
\[
L_b=\{v\in\{0,1\}^*:00\,1^b\preceq v\},\qquad
\sqrt{L_b}=\{w\in\{0,1\}^*:ww\in L_b\}.
\]
The exact state complexities of **complete deterministic finite automata** are
\[
\boxed{\kappa(L_b)=b+3,\quad\kappa(\sqrt{L_b})=\left\lceil\frac{b^2}{2}\right\rceil+3b+1.}
\]
Thus taking the language square root produces a quadratic number of inequivalent left quotients for an explicitly given, two-letter, principal subsequence-upward-closed language. The root means concatenating a word with itself, not interleaving or taking an algebraic square root.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). For \(b\in\mathbb Z_{\ge1}\), a word \(u\) is a scattered subsequence of \(v\) when its letters can be found in increasing, not necessarily adjacent, positions in \(v\). All machines below are complete DFAs, including their accepting sink. The state-complexity function \(\kappa\) counts states of the minimal such DFA. No nondeterministic-state claim is made.

## Proof
**1. A two-zero criterion.** A binary word without a zero is not in \(\sqrt{L_b}\). A word with exactly one zero is uniquely of the form \(1^p01^t\); the two zeros of its square are the two copies of that zero, so the condition is precisely \(t\ge b\). A word having at least two zeros is of the form \(1^p01^h0u\), with \(u\) arbitrary and \(t=|u|_1\). The first two zeros of its first copy maximize the number of ones that follow the second selected zero in its square; that number is \(p+h+2t\). Therefore
\[
1^p01^h0u\in\sqrt{L_b}\quad\Longleftrightarrow\quad p+h+2|u|_1\ge b.
\]
Any choice of later zeros leaves no more trailing ones, so the criterion is both necessary and sufficient. Note that the leading \(p\) ones reappear in the second copy and cannot be discarded.

**2. All possible left quotients.** Use the following state types (all thresholds are integers):

- \(P_p\) for \(0\le p\le b\): no zero has been read, and the number of leading ones is \(p\), capped at \(b\).
- \(Q_{\alpha,\beta}\) for \(1\le\alpha\le b\) and \(0\le\beta\le\alpha\): exactly one zero has been read, its trailing run has length \(t<b\), and \(\alpha=b-t\), \(\beta=\max(0,b-p-t)\), where \(p\) is the number of leading ones. For a suffix \(x\) with no zero, the quotient accepts \(x\) iff \(|x|_1\ge\alpha\). If \(x\) has at least one zero, write \(u\) for the number of ones preceding its first zero and \(v\) for the number of ones following that zero (including ones after any further zeros); its quotient accepts iff \(u+2v\ge\beta\).
- \(R_j\) for \(1\le j\le\lceil b/2\rceil\): at least two zeros have been read, and the quotient accepts exactly those suffixes containing at least \(j\) ones, irrespective of suffix zeros.
- \(A\): the accepting sink (all suffixes accepted).

The exact transition function, with input columns \(0,1\), is
\[
\begin{array}{c|cc}
\text{state}&0&1\\\hline
P_p&Q_{b,b-p}&P_{\min(b,p+1)}\\
Q_{\alpha,\beta}&\begin{cases} A&\beta=0\\R_{\lceil\beta/2\rceil}&\beta>0\end{cases}&\begin{cases} A&\alpha=1\\Q_{\alpha-1,\max(0,\beta-1)}&\alpha>1\end{cases}\\
R_j&R_j&\begin{cases}A&j=1\\R_{j-1}&j>1\end{cases}\\
A&A&A
\end{array}
\]
Here \(Q_{1,1}\) and \(R_1\) are identified, since both accept a suffix iff it contains at least one \(1\). The initial state is \(P_0\), and the only accepting state is \(A\). The two-zero criterion proves by induction that these transitions recognize exactly \(\sqrt{L_b}\), giving an upper bound.

**3. Reachability.** All \(P_p\) occur after \(1^p\). Every \(Q_{\alpha,\beta}\) is reached by \(1^{\alpha-\beta}01^{b-\alpha}\), except that the pair \((1,1)\) has the canonical name \(R_1\). Each \(R_j\) can be reached by \(00\) followed by enough ones to make its remaining threshold equal \(j\). The accepting state is reached by \(01^b\). Thus every listed state is reachable.

**4. Pairwise inequivalence.** State \(A\) accepts the empty suffix and no other state does. A \(P_p\) never accepts a suffix consisting entirely of ones, whereas every \(Q\) and \(R\) does when sufficiently many ones are supplied. For \(0\le p<q\le b\), the suffix \(0\,1^{b-q}0\) distinguishes \(P_p\) from \(P_q\), by the two-zero criterion. Distinct \(Q\)-states with different \(\alpha\) have different pure-one acceptance thresholds. With equal \(\alpha\) but distinct \(\beta\), a suffix \(1^{\min(\beta,\beta')}0\) distinguishes them. Different \(R_j\) have different pure-one thresholds. Finally, compare \(Q_{\alpha,\beta}\) with \(R_j\): if \(\alpha\ne j\), a pure-one suffix distinguishes them. If \(\alpha=j\) and \(\beta<j\), the suffix \(1^\beta0\) is accepted by \(Q\) and not \(R_j\). If \(\alpha=\beta=j\ge2\), the suffix \(0\,1^{\lceil j/2\rceil}\) is accepted by \(Q\) and not \(R_j\). The excluded case \(\alpha=\beta=j=1\) is exactly the identified pair. The Myhill–Nerode theorem now proves minimality.

**5. Count.** There are \(b+1\) states of type \(P\), \(\sum_{\alpha=1}^{b}(\alpha+1)-1=b(b+3)/2-1\) distinct \(Q\) states after identification, \(\lceil b/2\rceil\) states of type \(R\), and one accepting state. Their sum simplifies to \(\lceil b^2/2\rceil+3b+1\). Finally, the usual sequential subsequence-matching automaton for \(00\,1^b\) has exactly \(b+3\) states: the \(b+2\) proper-prefix matching stages and accepting sink are distinguishable by their respective remaining suffixes. This proves both formulas.

## Verification
The accompanying self-contained `checker.py` constructs these transitions, verifies their reachability and DFA minimization for every integer \(1\le b\le16\), compares direct scattered-subsequence membership with the constructed machine on 49,008 finite binary-word instances, and independently constructs and minimizes the root's transformation automaton for \(1\le b\le8\). It reports `PASS`. The finite tests are reproducibility checks, not substitutes for the general Myhill–Nerode proof.

## Relationship to prior work
Guyot [1], Section 2.1 and Appendix A, considers square roots of upward-closed languages generated by distinct-letter words with a growing alphabet, establishing exponential lower bounds; Section 2.2 concerns downward-closed language roots. Neither analysis supplies the exact fixed-binary-alphabet principal-generator formula above. Onishchenko [2] proves the general \(n^3\) worst-case **nondeterministic** state-complexity theorem; this does not determine the **deterministic** quotient count for the particular language studied here. Classical closure-language state-complexity results [3] provide background rather than this square-root specialization. These are comparisons of mathematical statements, not claims of exhaustive priority verification.

## Limitations
Only square roots (two concatenated copies) of the single pattern family \(00\,1^b\), with \(b\ge1\), are classified. The formula does not address arbitrary scattered patterns, higher roots, NFAs, or an optimal worst-case blowup over all upward-closed languages. The full text of [2] could not be inspected, and historical priority beyond the compared sources remains uncertain. No independent mathematical audit is asserted.

## References
[1] Jérôme Guyot, *On state complexity for subword-closed languages*, arXiv:2407.10355, first posted 2024-07-14. https://arxiv.org/abs/2407.10355 . The relevant Sections 2.1, 2.2 and Appendix A were inspected in the publicly available full-text presentation at https://www.researchgate.net/publication/382272084_On_state_complexity_for_subword-closed_languages .

[2] Sergey Onishchenko, *Nondeterministic state complexity of square root*, arXiv:2605.02957, first posted 2026-05-02. https://arxiv.org/abs/2605.02957 . Accessible abstract and bibliographic record; full text not confirmed read.

[3] J. Brzozowski, G. Jirásková and C. Zou, *Quotient complexity of closed languages*, arXiv:0912.1034, 2009. https://arxiv.org/abs/0912.1034 .
