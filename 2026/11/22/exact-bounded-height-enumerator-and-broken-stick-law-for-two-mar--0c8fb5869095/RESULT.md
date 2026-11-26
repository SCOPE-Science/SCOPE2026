# Exact bounded-height enumerator and broken-stick law for two-marker binary words

## Finding
Let \(h(w)\) be the least integer \(H\) for which the **set** of scattered subsequences of \(w\) of lengths at most \(H\) identifies \(w\) uniquely among all binary words of arbitrary length. Let \(S_j(z)=z+z^2+\cdots+z^j\) for \(j\ge1\), and \(S_j(z)=0\) for \(j\le0\). For every integer \(H\ge3\), the exact length-generating polynomial for binary words with **exactly two** occurrences of \(1\) and \(h(w)\le H\) is

\[
\boxed{G_H(z)=1+3S_{H-1}(z)+S_{H-2}(z)^2+2zS_{H-2}(z)+2(S_{H-2}(z)-z)S_{H-3}(z)+S_{H-3}(z)^3.}
\]
Here the exponent of \(z\) counts **zeros**, so the coefficient of \(z^{n-2}\) counts length-\(n\) words. The exact-height enumerator is \(G_H-G_{H-1}\) for \(H\ge4\), and \(G_3\) at height three. In particular the full cumulative number of two-marker words of all lengths with height at most \(H\) is \(G_H(1)=H^3-6H^2+16H-11\), an exact cubic polynomial.

For \(W_n\) uniform among length-\(n\) binary words with exactly two ones, the normalized complexity \(h(W_n)/n\) converges in distribution to \(M\), the maximum of three uniform-simplex coordinates. Its distribution function is

\[
\boxed{\Pr(M\le x)=\sum_{j=0}^3(-1)^j\binom3j(1-jx)_+^2,\qquad 0\le x\le1,}
\]
where \(t_+=\max(t,0)\). The limiting mean and variance are respectively \(11/18\) and \(13/648\). This provides an exact all-height finite census and a nondegenerate asymptotic law for a natural sparse family of singleton-language descriptive complexities.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). A scattered subsequence retains selected letters in their original order, without requiring contiguity; existence, not embedding multiplicity, is considered. Every word considered has the unique decomposition \(w(a,b,c)=0^a1\,0^b1\,0^c\), where \(a,b,c\) are nonnegative integers. The polynomial counts each indexed word once; it does not identify cyclic rotations or complements. The empty subsequence affects no distinction. All comparisons in the definition of \(h\) allow competing binary words of any length and Hamming weight.

## Proof
**1. From singleton height to deleted-symbol witnesses.** For a binary word \(w\), let \(\lambda_i(w)\) be the shortest length of a scattered subsequence present in \(w\) but absent after deleting the symbol at position \(i\). The published deletion characterization of the piecewise minimality index \(\rho\), together with the binary identity \(h=\rho+1\) [1, Proposition 3.4 and Theorem 3.11], yields
\[
h(w)=1+\max_i\lambda_i(w).\tag{1}
\]
Indeed the maximum Simon-congruence level preserved under each deletion is \(\lambda_i-1\), so \(\rho=\max_i\lambda_i\). Equation (1) is credited to the published characterization, not claimed as new.

**2. Exact witness lengths for two markers.** Set \(N=a+b+c\). Deleting either \(1\) always has \(\lambda=2\), witnessed by the scattered pattern `11`. If the relevant zero run is nonempty, deleting any zero in the first, middle, or last run has respectively the witness length
\[
\begin{aligned}
\lambda_a&=\min\{N,\ a+1\text{ if }b=0\text{ else }a+2\},\quad(a>0),\\
\lambda_b&=\min\{N,\ b+1\text{ if }a=0\text{ or }c=0\text{ else }b+2\},\quad(b>0),\\
\lambda_c&=\min\{N,\ c+1\text{ if }b=0\text{ else }c+2\},\quad(c>0).
\end{aligned}\tag{2}
\]
Missing zero runs contribute no candidate. To prove these identities, every scattered pattern has zero, one, or two occurrences of \(1\). The all-zero patterns first distinguish at length \(N\). Patterns with two ones are precisely \(0^u1\,0^v1\,0^t\), present exactly when \(u\le a,v\le b,t\le c\); decreasing the relevant gap by one makes the shortest such missing pattern have length \(a+2,b+2,c+2\), respectively. Patterns with one one are \(0^u1\,0^v\), supported by the union of rectangles
\[
([0,a]\times[0,b+c])\ \cup\ ([0,a+b]\times[0,c])
\]
in the \((u,v)\) lattice. Decreasing \(a\) can only uncover points with \(u=a\) in the first rectangle or \(u=a+b\) in the second. The point \((a,0)\) is uncovered exactly when \(b=0\), and if \(b>0\) no point of total pattern length at most \(a+1\) is uncovered. Decreasing \(c\) is symmetric. Decreasing \(b>0\) can only uncover points with \(v=b+c\) in the first rectangle or \(u=a+b\) in the second. The axis points \((0,b+c)\) and \((a+b,0)\) are both uncovered, so the exact shortest one-marker witness has length \(b+1+\min\{a,c\}\). In particular its length is \(b+1\) if either outer gap is zero and is at least \(b+2\) otherwise; the two-marker witness of length \(b+2\) supplies the upper bound in the latter case. Taking the minimum over the zero-, one-, and two-marker witnesses proves (2), including zero-sized boundary cases.

**3. Disjoint decomposition by positive gaps.** Equations (1)–(2) imply the following complete classification for \(H\ge3\):

- All gaps zero: the single word `11` has height \(3\).
- Exactly one gap positive, of size \(t\): the height is \(\max\{3,t+1\}\), so \(1\le t\le H-1\). There are three choices of gap.
- Exactly the first and last gaps positive (\(b=0\)): the height is \(\max\{a,c\}+2\), so \(1\le a,c\le H-2\).
- Exactly the middle and one outer gap positive: if the middle gap \(b=1\), the height equals the outer gap plus \(2\); if \(b\ge2\), the height equals \(\max\{b+2,\text{outer gap}+3\}\). There are two choices of nonzero outer gap.
- All three gaps positive: the height is \(\max\{a,b,c\}+3\), so \(1\le a,b,c\le H-3\).

The corresponding zero-count polynomials are, in order,
\[
1,\quad3S_{H-1},\quad S_{H-2}^2,\quad2\{zS_{H-2}+(S_{H-2}-z)S_{H-3}\},\quad S_{H-3}^3.
\]
Adding these disjoint classes proves the displayed formula for \(G_H\). The difference of successive cumulative polynomials gives every exact-height multiplicity, for each length.

**4. Limit law and moments.** At fixed length \(n=N+2\), the \(\binom{N+2}{2}\) allowed words correspond bijectively to nonnegative triples with sum \(N\). Only \(O(N)\) of these have a zero gap, while the total is \(\Theta(N^2)\). On the interior, Step 3 gives \(h=3+\max\{a,b,c\}\). Thus the normalized complexity differs by \(O(1/N)\) from the maximum of the three normalized gaps with probability tending to one. The uniform lattice points on \(a+b+c=N\) converge to the uniform distribution on the standard two-simplex. Inclusion–exclusion of the events that coordinate \(i\) exceeds \(x\) gives \(\Pr(M\le x)=\sum_{j=0}^3(-1)^j\binom3j(1-jx)_+^2\). Integration of the piecewise quadratic CDF yields \(\mathbb E M=11/18\), \(\mathbb E M^2=85/216\), and \(\operatorname{Var}(M)=13/648\).

## Verification
Run `python3 checker.py` using only the Python standard library. It independently constructs greedy subsequence-matching automata for each word and each one-symbol **insertion**, then breadth-first searches for the shortest distinguishing subsequence. This verifies the height formula by a different route from the deletion-gap proof for all 455 parameter triples with \(a+b+c\le12\). It also checks 368 cumulative-polynomial coefficients across sixteen height thresholds and twenty-three zero counts. Expected last line: `PASS exact_generic_insertion=455 polynomial_coefficients=368`. The finite tests are corroboration only; Steps 1–4 establish the infinite statements.

## Relationship to prior work
Praveen, Schnoebelen, Vialard and Veron [1] give the deletion and insertion formulas and the binary identity between height and minimality index. Schnoebelen and Vialard [2] give run-block methods, and Schnoebelen, Veron and Vialard [5] study tropical computation for compressed words. These results compute wordwise height; the contribution here is an explicit bounded-height census. The four-run enumerator [3] covers some boundary words of the present family, not the five-run interior. The fixed-content Simon-class census [4] restricts comparisons to words of the same composition, whereas singleton height also requires ruling out longer words. The isolated-marker result [6] states its theorem for at least three ones and all gaps positive. Its positive-gap proof extends to two ones and there gives the same interior law \(h=3+\max\{a,b,c\}\), interior term \(S_{H-3}^3\), and corresponding broken-stick limit. Neither that positive-gap argument nor the classical broken-stick distribution is a distinct contribution here. The finite census includes all vanishing-gap cases, which supply the remaining terms and change the exact counts. The shared date of this and the isolated-marker result does not determine publication priority.

## Limitations
The formula is restricted to exactly two ones over a binary alphabet. The derivation relies on established binary height characterizations, not on a new general piecewise-testability algorithm. The probabilistic limit is under uniform fixed-weight sampling, not uniform sampling of all binary words. An unindexed equivalent enumerator could exist.

## References
[1] M. Praveen, Ph. Schnoebelen, I. Vialard, J. Veron, *On the piecewise complexity of words and periodic words*, arXiv:2311.15431v1, first publicly posted 2023-11-26. https://arxiv.org/abs/2311.15431

[2] Ph. Schnoebelen and I. Vialard, *On the piecewise complexity of words*, arXiv:2412.16560v1, first publicly posted 2024-12-21. https://arxiv.org/abs/2412.16560

[3] *A perfect-square length enumerator for bounded piecewise height of four-run binary words*, https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-a-perfect-square-length-enumerator-for-bounded-piecewise-height--951e6db8c395

[4] *Exact fixed-content Simon-congruence classes for binary two-marker words*, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-exact-fixed-content-simon-congruence-classes-for-binary-two-mark--176c90a6c83d

[5] Ph. Schnoebelen, J. Veron, I. Vialard, *A Tropical Approach to the Compositional Piecewise Complexity of Words and Compressed Words*, ICALP 2025, DOI:10.4230/LIPIcs.ICALP.2025.171. https://drops.dagstuhl.de/storage/00lipics/lipics-vol334-icalp2025/html/LIPIcs.ICALP.2025.171/LIPIcs.ICALP.2025.171.html

[6] *Piecewise height and exact distribution for binary words with isolated one-markers*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-piecewise-height-and-exact-distribution-for-binary-words-with-is--688d1ac5d334
