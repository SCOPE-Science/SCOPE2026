# Joint universality–transition census of binary words

## Finding
Let \(\Sigma=\{0,1\}\) be the **fixed ambient alphabet**. For every finite binary word \(w\), its scattered-subsequence universality index \(\iota(w)\) is the greatest integer \(k\ge0\) for which every binary word of length \(k\) occurs as a subsequence of \(w\). Let \(r(w)=|\{i:1\le i<|w|,w_i\ne w_{i+1}\}|\) be its number of symbol transitions. With \(\varepsilon\) denoting the empty word, the exact generating function is
\[
F(z,u,t):=\sum_{w\in\Sigma^*}z^{|w|}u^{\iota(w)}t^{r(w)}
=1+\frac{2z(1+ztu)}{1-z-z^2tu(1+t)}.
\]
In particular, for \(n\ge1\) and \(k\ge1\), the number \(N(n,k,r)\) of words satisfying \(|w|=n\), \(\iota(w)=k\), and \(r(w)=r\) is
\[
N(n,k,r)=2\left[\binom{n-k}{k}\binom{k-1}{r-k}+\binom{n-k-1}{k}\binom{k-1}{r-k-1}\right].
\]
A binomial coefficient is zero when its lower argument lies outside its usual nonnegative range (also when the upper argument is negative). Further, \(N(0,0,0)=1\), and for \(n\ge1\), \(N(n,0,0)=2\) while \(N(n,0,r)=0\) for \(r\ne0\).

The complete **feasibility region** at \(n\ge2k\ge2\) is \(k\le r\le\min\{2k,n-1\}\): each integer \(r\) in this interval has \(N(n,k,r)>0\), and all other transition counts are impossible. Thus any nonconstant binary word obeys the sharp structural inequalities
\[\lceil r(w)/2\rceil\le \iota(w)\le r(w).\]
Both endpoint behaviors occur for infinitely many lengths. Equivalently, for a prescribed transition budget \(r\), the universality index cannot fall below \(\lceil r/2\rceil\); the formula resolves every intermediate case, not just the extremes.

## Assumptions and scope
Words are finite ordered strings over the *fixed* binary alphabet, even if a word uses only one letter. A subsequence allows arbitrary deletions while retaining order. A transition is an adjacent change of letter, not a maximal periodic repetition (the latter is also called a run in other contexts). The empty word has index and transitions zero. The generating series is formal, so no analytic convergence assumption is required. All integer parameters \(n,k,r\) are nonnegative.

## Proof
**Greedy arches and the universality index.** Scan the word left to right. Each time both symbols have appeared since the preceding cut, cut just after the first appearance of the second symbol, and restart. Write the resulting unique decomposition as \(w=A_1\cdots A_k R\), with \(k\) complete arches and the leftover \(R\) containing at most one symbol type. Every requested length-\(k\) binary subsequence can be obtained by choosing one appropriate letter in each arch. Conversely, let \(c_j\) be the final letter of arch \(A_j\), and choose any binary symbol \(d\) absent from \(R\). The word \(c_1\cdots c_kd\) is absent as a subsequence: the *earliest* occurrence of \(c_1\) is exactly the end of \(A_1\), and, inductively, the earliest occurrence of \(c_j\) after the preceding selected arch end is exactly the end of \(A_j\). No \(d\) remains thereafter. Thus \(\iota(w)=k\). This includes the case \(k=0\).

**Two-state weighted recursion.** After at least one symbol has been read, distinguish state \(S\), in which exactly one binary symbol has appeared in the unfinished arch, from state \(E\), immediately after an arch has closed, with the most recent symbol still known. For both states the identity of that most recent letter is irrelevant by binary complementation symmetry. Mark each read letter by \(z\), each symbol change by \(t\), and each completed arch by \(u\). Let \(S(z,u,t)\) and \(E(z,u,t)\) enumerate arbitrary continuation strings from the respective states (including the empty continuation). From \(S\), stopping contributes 1, repeating the last symbol contributes \(zS\), and switching completes one arch and contributes \(ztuE\). From \(E\), stopping contributes 1, while the first symbol of the next arch may repeat or switch relative to the last symbol, contributing respectively \(zS\) or \(ztS\). Therefore
\[S=1+zS+ztuE,\qquad E=1+z(1+t)S.\]
Eliminating \(E\) yields
\[S=\frac{1+ztu}{1-z-z^2tu(1+t)}.\]
The first letter has two choices and creates no transition, so \(F=1+2zS\), which proves the stated rational series for all lengths.

**Exact coefficients and sharp region.** For \(k\ge1\), expansion as a geometric series gives
\[
[u^k]F=\frac{2z^{2k}t^k(1+t)^{k-1}(1+zt)}{(1-z)^{k+1}}.
\]
Taking coefficients of \(z^nt^r\) yields the binomial formula. For \(n\ge2k\), the first binomial contribution is positive for all \(r\in\{k,\ldots,2k-1\}\); the second additionally supplies \(r=2k\) precisely when \(n\ge2k+1\). This proves the support statement. When \(k=0\), the word has no completed arch and hence is constant (or empty), proving the boundary cases and the inequality.

## Verification
The standalone script `verify_arch_run_joint.py` builds both the greedy index and, for short words, an independent index evaluator using the definition that all length-\(k\) binary words must occur as scattered subsequences. It compares both for every binary word of length at most \(11\), exhaustively checks the coefficient formula and feasible region for every binary word of length up to \(17\), and checks total counts against \(2^n\). The actual script prints `VERIFY_OK: definition through n=11, full joint coefficient enumeration through n=17`. These finite computations verify the implementation and small cases; the state recursion and coefficient extraction establish the all-length theorem.

As a consistency check, setting \(t=1\) recovers the previously published marginal \(\frac{1+z}{1-z-2uz^2}\). Setting \(u=1\) gives the elementary transition enumeration \(1+\frac{2z}{1-z(1+t)}\). Neither marginal determines the joint coefficients.

## Relationship to prior work
Karandikar and Schnoebelen's rich-factorization framework, already publicly available in 2015, provides the historical basis for counting complete-alphabet arches. Hébrard's earlier arch factorization and Barker et al.'s scattered-factor-universality study identify the same index. Adamson gives a dynamic-programming enumeration and ranking of \(k\)-universal words without the symbol-transition refinement. A published exact *univariate-in-transition* marginal for the binary universality index is also known; the present result is the **joint distribution** of that index with adjacent symbol changes, including its sharp support. The results do not imply the joint counts from their respective marginals. Sources below are cited for their established content, not claimed as co-discoverers of the refinement.

## Limitations
The closed form is specific to the binary alphabet; for larger alphabets a partial arch cannot be encoded only by whether a letter has been seen. This does not provide a classification of words by their entire subsequence spectrum, only by the universality index and number of transitions. Earlier equivalent formulas under different terminology cannot be ruled out absolutely. The result is a symbolic counting theorem independently corroborated by finite exhaustive tests; it has not undergone independent mathematical review.

## References
1. P. Karandikar and P. Schnoebelen, *The height of piecewise-testable languages and the complexity of the logic of subwords*, arXiv:1511.01807v1, first posted 2015-11-05; see §3.2 of the lawful open full text https://arxiv.org/html/1511.01807v4 (subsequent version).
2. L. Barker, P. Fleischmann, K. Harwardt, F. Manea and D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629v1, posted 2020-03-10, https://arxiv.org/abs/2003.04629.
3. D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1, posted 2023-04-10, https://arxiv.org/html/2304.04583v1.
4. *Closed-form law for binary subsequence universality*, published published-finding corpus research record, https://github.com/Resultary/2026.
