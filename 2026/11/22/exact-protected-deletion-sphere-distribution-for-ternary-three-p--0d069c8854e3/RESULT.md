# Exact protected-deletion sphere distribution for ternary three-palindrome-avoiding words

## Finding

Let \(\Sigma=\{0,1,2\}\), and let \(\mathcal P_n\) be the set of length-\(n\) words \(w=w_1\cdots w_n\) with \(w_i\ne w_{i+2}\) for every \(1\le i\le n-2\). Thus no contiguous three-letter palindrome is permitted. Let \(D(w)\) be the **set of distinct** words produced by deleting exactly one coordinate of \(w\) for which the remaining word is also three-palindrome-avoiding, and put \(d(w)=|D(w)|\). This is a constrained-output single-deletion sphere, not an unrestricted deletion sphere.

For the polynomial \(P_n(u)=\sum_{w\in\mathcal P_n}u^{d(w)}\), with \(n\ge1\), define \(G(z,u)=\sum_{n\ge1}P_n(u)z^n\). Then

\[
G(z,u)=\frac{3uz(1+z)R(z,u)}{Q(z,u)},
\]

where

\[
\begin{aligned}
Q(z,u)&=1-z-(1+u)z^2+(1-u^2)z^3+(u^2-1)z^4,\\
R(z,u)&=1-z-z^2+z^3-z^4+u(2z-z^2+2z^4)\\
&\qquad+u^2(2z^2-z^3-z^4).
\end{aligned}
\]

In particular, for every \(n\ge1\),

\[
\max_{w\in\mathcal P_n}d(w)=\left\lceil\frac{2n+1}{3}\right\rceil.
\]

The number \(A_n\) of words attaining this maximum is exactly

\[
A_1=3,\qquad
A_{3h}=6\ (h\ge1),\qquad
A_{3h+1}=3h(h+1)+12\ (h\ge1),\qquad
A_{3h+2}=6(h+1)\ (h\ge0).
\]

Thus the complete sphere-size distribution, the sharp maximum and the exact number of extremizers are all explicit for every blocklength, without restricting to a finite sample.

## Assumptions and scope

Words are linear, not circular; alphabet symbols are labeled; each deletion produces a length-\(n-1\) word and equal results from different deletion positions are counted once. At \(n=1\), deletion yields the empty word, regarded as admissible. Both source and received word must obey the identical length-three palindrome restriction. Only the three-symbol alphabet and exactly one deletion are asserted here.

## Proof

**Local deletion test.** Two single-position deletions of a word yield identical words exactly when the positions belong to the same maximal constant run. Consequently a distinct descendant can be represented by deletion at the first position of each run. Deleting position \(i\) can introduce forbidden length-three factors only across the new junction. When the relevant indices exist, the two potential new palindromes have equal outer letters precisely when \(w_{i-2}=w_{i+1}\) or \(w_{i-1}=w_{i+2}\). Accordingly the deletion of the first run position \(i\) contributes one exactly when its junction passes these two tests. The first position contributes one unconditionally; the initial and final positions have only the available tests. All original, non-junction factors were already admissible.

**Six-state enumeration.** For length-four source windows, relabel the letters by the order in which they first appear. The six possible equality-pattern states are, in this order,

\[
0011,\quad0012,\quad0110,\quad0112,\quad0120,\quad0122.
\]

Each has exactly six realizations over \(\Sigma\). Let \(u\) mark the number of admissible distinct deletion outputs. The initial-weight row, final-weight column and one-symbol transition matrix are

\[
V=6\begin{pmatrix}u&u&u&u^2&u&u^2\end{pmatrix},\qquad
T=\begin{pmatrix}u&u^2&u&u&u&u\end{pmatrix}^{\!\mathsf T},
\]

\[
M=\begin{pmatrix}
0&0&1&u&0&0\\
0&0&0&0&1&u\\
1&1&0&0&0&0\\
1&1&0&0&0&0\\
0&0&0&0&1&1\\
0&0&1&u&0&0
\end{pmatrix}.
\]

The initial row marks deletions at the first two positions, and \(T\) marks those at the final two positions. On each appended symbol the transition marks the now-settled deletion at the middle of the previous four-symbol window. For example, in state \(0011\), append \(0\) to obtain \(0110\) with weight \(1\), or append the third color \(2\) to obtain \(0112\) with weight \(u\). Every other entry follows by the same junction test. Since transitions preserve the no-palindrome condition, each word is counted once. Therefore

\[
G(z,u)=3uz+(3u+6u^2)z^2+(12u^2+6u^3)z^3
+z^4V(I-zM)^{-1}T.
\]

All matrices here have entries in \(\mathbb Z[u]\) and the inverse is formal at \(z=0\). Exact polynomial elimination of this six-dimensional rational expression yields the displayed \(R/Q\). The supplied checker independently assembles \(M,V,T\) from the local rules and verifies the exact symbolic identity.

**Sharp degree and extremizers.** The initial polynomials, which also fix every boundary case, are

\[
\begin{aligned}
P_1&=3u,\\
P_2&=3u+6u^2,\\
P_3&=12u^2+6u^3,\\
P_4&=18u^2+18u^3,\\
P_5&=30u^2+30u^3+12u^4,\\
P_6&=48u^2+54u^3+36u^4+6u^5.
\end{aligned}
\]

As the numerator of \(G\) has \(z\)-degree six, the denominator yields for \(n\ge7\)

\[
P_n=P_{n-1}+(1+u)P_{n-2}+(u^2-1)P_{n-3}+(1-u^2)P_{n-4}.
\]

Set \(m_n=\lceil(2n+1)/3\rceil\). Induction in this recurrence shows \(\deg P_n\le m_n\), because every term on the right has degree at most \(m_n\) when earlier terms satisfy these bounds. Let \(a_n\) be the coefficient of \(u^{m_n}\). Comparing the top-degree terms in the three congruence classes gives, for the indices where the recurrence applies,

\[
\begin{aligned}
a_{3h}&=a_{3h-3},\\
a_{3h+1}&=a_{3h}+a_{3h-1}+a_{3h-2}-a_{3h-3},\\
a_{3h+2}&=a_{3h}+a_{3h-1}.
\end{aligned}
\]

Together with the six initial polynomials these solve to \(a_1=3\), \(a_{3h}=6\), \(a_{3h+1}=3h(h+1)+12\), and \(a_{3h+2}=6(h+1)\), in the stated ranges. Every top coefficient is strictly positive, so the upper degree bound is attained, completing the all-length proof.

## Verification

The standalone `verify.py` reconstructs the local six-state automaton and performs an exact symbolic equality check against \(G(z,u)\). It independently enumerates source words and distinct legal deletion results through length thirteen, checks the six-state spectra and both extremal laws through length sixteen, and checks polynomial recurrence coefficients through length twenty-six. The symbolic matrix identity and the algebraic induction, not finite enumeration alone, establish the infinite parameter range. Python 3 and SymPy are needed to run the verifier.

## Relationship to prior work

Shen, Shangguan, Lin and Ge (2024) explicitly identify fixed-length palindrome avoidance as a finite-type coding constraint and give general methods to count constrained words. Their one-variable length enumerator is recovered here upon setting \(u=1\), but their results do not specify the retained-valid-deletion statistic or its sharp extremizers. Bar-Lev, Kobovich, Leitersdorf and Yaakobi (2023) provide general constructions for parametric constraints including palindrome avoidance; these are encoder constructions, not conditional deletion-sphere enumerations. Bar-Lev, Etzion and Yaakobi (2022) study unrestricted deletion and fixed-length Levenshtein spheres. Their unrestricted deletion operation does not impose legality of the received word, and the equal-length edit metric is different. A run-two deletion-survivor formula that only forbids constant triples does not give the present statistic: avoiding all three-letter palindromes is strictly stronger at both the source and the receiver. The present result imposes that stricter restriction on both ends of the deletion channel.

## Limitations

No claim is made for other alphabets, cyclic boundary conventions, two or more deletions, code capacity or optimal codebooks. The result concerns exact output cardinality, not deletion probabilities. The comparison to prior literature cannot rule out an earlier unindexed equivalent formula. No independent mathematical audit has been performed.

## References

1. Y. Shen, C. Shangguan, Z. Lin, G. Ge, *Constrained coding upper bounds via Goulden-Jackson cluster theorem*, arXiv:2407.16449, first posted 2024-07-23. https://arxiv.org/abs/2407.16449
2. D. Bar-Lev, A. Kobovich, O. Leitersdorf, E. Yaakobi, *Universal Framework for Parametric Constrained Coding*, arXiv:2304.01317, first posted 2023-04-03. https://arxiv.org/abs/2304.01317
3. D. Bar-Lev, T. Etzion, E. Yaakobi, *On the Size of Balls and Anticodes of Small Diameter under the Fixed-Length Levenshtein Metric*, arXiv:2206.07995, first posted 2022-06-16. https://arxiv.org/abs/2206.07995
