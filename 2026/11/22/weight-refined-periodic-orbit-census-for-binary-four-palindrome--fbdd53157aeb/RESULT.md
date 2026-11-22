# Weight-refined periodic-orbit census for binary four-palindrome avoidance

## Finding

For every positive integer \(n\), let \(X_n\) be the set of binary words \(w=w_0\cdots w_{n-1}\) whose periodic extension contains no factor in \(\{0000,0110,1001,1111\}\). Define the composition polynomial \(C_n(u)=\sum_{w\in X_n}u^{|w|_1}\), where \(|w|_1\) counts ones in one indexed circumference. The complete weight-refined periodic-orbit zeta function is

\[
\exp\!\left(\sum_{n\ge1}\frac{C_n(u)}{n}z^n\right)
=\frac{1}{1-uz^2-(u+u^3)z^4-u^3z^6}.
\]

Every odd circumference has no admissible word. At each even circumference \(n\ge2\), the set of achievable numbers of ones is exactly
\[
\{k\in\mathbb Z:\lceil n/4\rceil\le k\le\lfloor3n/4\rfloor\}.
\]
Moreover the primitive-period spectrum is precisely \(\{2,4,6,\ldots\}\): for every even \(n\) some admissible circle has least period \(n\), and no such circle has odd least period. The formulas for primitive orbit and total necklace composition-polynomials, respectively, are
\[
P_n(u)=\frac{1}{n}\sum_{d\mid n}\mu(d)C_{n/d}(u^d),\qquad
N_n(u)=\frac{1}{n}\sum_{d\mid n}\varphi(d)C_{n/d}(u^d).
\]
Here \(P_n\) counts primitive necklaces of length \(n\), \(N_n\) counts all necklaces of length \(n\), and \(\mu\), \(\varphi\) are the Möbius and Euler-totient functions. The exponential growth rate of admissible indexed circles is \(\sqrt{\rho}\) where \(\rho\approx2.1478990357\) is the unique real root exceeding one of \(\rho^3-\rho^2-2\rho-1=0\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). A forbidden factor is an **ordinary** palindrome of contiguous length four; its factors may cross the circular boundary. A circular word is represented by all indexed binary words of length \(n\), not by necklaces. For \(n<4\), the forbidden factor test is applied to the **infinite periodic extension**, with repeated positions allowed. Weight counts the number of ones in one circumference; it is not a density normalization. The zeta identity holds as a formal power series in \(z\) with coefficients in \(\mathbb Z[u]\).

## Proof

**Transfer graph.** Label the eight binary length-three states by their binary integer values \(0,\ldots,7\). Put an edge from state \(v\) to state \((2v+b)\bmod8\), for \(b\in\{0,1\}\), precisely when the length-four word encoded by \(2v+b\) is not a palindrome. Assign that edge monomial weight \(u^b\). Write \(A(u)\) for the resulting \(8\times8\) weighted adjacency matrix. Length-\(n\) closed walks beginning at a fixed state correspond bijectively to admissible indexed length-\(n\) binary periodic words; the transition labels recover the word, including the cases \(n<4\). Thus \(C_n(u)=\operatorname{tr}(A(u)^n)\).

**Exact determinant.** The six simple directed cycles of the graph, listed by state sequence and pair (length, number of ones), are:

- \((0,1,2,4)\): \((4,1)\);
- \((0,1,2,5,3,7,6,4)\): \((8,4)\);
- \((0,1,3,7,6,4)\): \((6,3)\);
- \((0,1,3,7,6,5,2,4)\): \((8,4)\);
- \((2,5)\): \((2,1)\);
- \((3,7,6,5)\): \((4,3)\).

The only pairs of vertex-disjoint simple cycles are the length-four cycles together, and the length-six and length-two cycles together. Each such pair has total length eight and total number of ones four. The signed vertex-disjoint cycle expansion of the determinant therefore gives
\[
\begin{split}
\det(I-zA(u))&=1-uz^2-u z^4-u^3z^4-u^3z^6\\
&\quad-2u^4z^8+2u^4z^8\\
&=1-uz^2-(u+u^3)z^4-u^3z^6.
\end{split}
\]
The formal determinant-trace identity \(-\log\det(I-zA)=\sum_{n\ge1}\operatorname{tr}(A^n)z^n/n\) now proves the claimed zeta identity. As an alternative explicit coefficient formula, for \(m\ge1\),
\[
C_{2m}(u)=2m\!\sum_{\substack{a,b,c\ge0\\a+2b+3c=m}}
\frac{(a+b+c-1)!}{a!b!c!}\,u^{a+3c}(u+u^3)^b,
\qquad C_{2m+1}(u)=0.
\]
The expression has an integer interpretation by expanding the remaining binomial power; \(m\ge1\) ensures the factorial numerator is defined for every summand.

**Sharp weight support.** Every simple directed cycle has even length, hence every closed walk has even length and all odd-length counts vanish. Conversely, in any admissible circle each four-window is neither \(0000\) nor \(1111\), so its one-count lies between one and three. Summing these inequalities over all \(n\) windows counts every symbol exactly four times, giving \(n\le4|w|_1\le3n\). For sufficiency write \(n=2m\). The two-cycle \((2,5)\) has length two and weight one; the four-cycle \((0,1,2,4)\) has length four and weight one, sharing state two; the four-cycle \((3,7,6,5)\) has length four and weight three, sharing state five. Concatenating \(a\) repetitions of one of these four-cycles with \(m-2a\) repetitions of the two-cycle, for each \(0\le a\le\lfloor m/2\rfloor\), yields admissible words of respective weights \(m-a\) and \(m+a\). Their union realizes every weight in the claimed interval.

**Primitive periods.** The two-cycle gives primitive circumference two. For each even \(n\ge4\), traverse the four-cycle \((0,1,2,4)\) exactly once and insert \((n-4)/2\) traversals of the two-cycle \((2,5)\) at shared state two. The resulting closed walk passes through state \(0\) exactly once. A circular word with a proper period would pass through every state encountered at least twice, contradicting this uniqueness. Thus its primitive period is exactly \(n\). No odd primitive period is possible. The necklace formulas follow from orbit division and Möbius inversion. Finally, at \(u=1\), the denominator \(1-z^2-2z^4-z^6\) has dominant positive singularity \(z=\rho^{-1/2}\), giving the stated rate.

## Verification

`check_cycles.py` enumerates all elementary directed cycles and all vertex-disjoint families, recomputing the determinant polynomial exactly over integers and symbolic monomials without numerical approximation. `check_direct.py` independently enumerates every binary word at each length from one through sixteen, tests every cyclic forbidden window, counts compositions and primitive periods, and compares against a separate formal-series coefficient recurrence. Both scripts use only the Python standard library; run `python3 check_cycles.py` and `python3 check_direct.py` from the extracted package directory. Independent enumerations agree at every tested length. For example, \(C_2(u)=2u\), \(C_4(u)=4u+2u^2+4u^3\) and \(C_6(u)=6u^2+8u^3+6u^4\). The infinite result rests on the determinant proof and explicit constructions, not on the finite tests.

## Relationship to prior work

Fici and Zamboni examine palindromic-factor scarcity in infinite words, including periodic words; Guo, Shallit and Shur examine combinatorics of palindromes and antipalindromes; Fleischer and Shallit obtain rational generating functions for different bounded-palindrome languages using automata. These results motivate the local palindromic exclusion but do not state the present evaluated *binary four-palindrome, circular, composition-refined* zeta, full weight-support interval, and exact primitive-period spectrum. The transfer-matrix and determinant-trace methods themselves are standard and are not claimed as new.

## Limitations

This is a constraint on contiguous palindromes of **exact length four**, not avoidance of all palindromes or reverse-complementary DNA palindromes. It does not imply a result for arbitrary alphabets or multiple forbidden lengths. Indexed counts and orbit counts use different normalizations as specified. The literature comparison is limited to the inspected studies and indexed records, so unnoticed equivalent historical computations remain possible. No independent mathematical audit has been performed.

## References

1. G. Fici and L. Q. Zamboni, *On the least number of palindromes contained in an infinite word*, arXiv:1301.3376, first version 2013-01-15, https://arxiv.org/abs/1301.3376 .
2. J. Guo, J. Shallit and A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, arXiv:1503.09112, 2015-03-31, https://arxiv.org/abs/1503.09112 .
3. L. Fleischer and J. Shallit, *Words with Few Palindromes, Revisited*, arXiv:1911.12464, 2019-11-27, https://arxiv.org/abs/1911.12464 .
