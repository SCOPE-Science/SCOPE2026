# A sharp Fibonacci-partition doubling dichotomy across Lucas intervals

## Finding
Let \(F_0=0,F_1=1\), and let \(R(t)\) count subsets of \(\{F_2,F_3,\ldots\}\) whose sum equals the nonnegative integer \(t\); the Fibonacci entries are distinct and the index \(2\) is the unique copy of \(1\). Let \(\varphi=(1+\sqrt5)/2\). For each integer \(N\ge3\), let \(\beta(N)\) be its Bergman (no adjacent ones) base-\(\varphi\) expansion. Its lowest occupied exponent is \(-r(N)\). Write \(L_0=2,L_1=1,L_{j+2}=L_{j+1}+L_j\).

**Theorem.** For every integer \(N\ge3\),
\[
 R(F_{r(N)+4}N)\ge2R(F_{r(N)+2}N).
\]
Equality holds **if and only if** \(N\) lies in an odd Lucas interval \([L_{2j+1}+1,L_{2j+2}-1]\) for some \(j\ge1\). Strict inequality holds throughout every even interval \([L_{2j},L_{2j+1}]\). In fact, if \(K(N)\) and \(V(N)\) are the Knott and natural base-\(\varphi\) expansion counts, respectively, then
\[
 R(F_{r(N)+4}N)=K(N)+V(N),\qquad R(F_{r(N)+2}N)=V(N).
\]
The ratio can be arbitrarily large: for every \(j\ge1\),
\[
 R(F_{2j+4}L_{2j+1})=2j+2,\qquad R(F_{2j+2}L_{2j+1})=1.
\]

## Assumptions and scope
All expansions use only binary digits and finite support. A Fibonacci representation uses each Fibonacci index at most once; there is a single allowed \(1=F_2\), not two copies. A Knott expansion is a finite base-\(\varphi\) representation that does not terminate in the pattern \(011\); a natural expansion has the same lowest occupied exponent as its Bergman expansion. The exponent \(-r(N)\) is negative for \(N\ge3\) and is always even. Neither \(r(N)\) nor the Fibonacci multipliers are chosen freely: \(r(N)=2j\) on the even Lucas interval \([L_{2j},L_{2j+1}]\), and \(r(N)=2j+2\) on the succeeding odd interval.

## Proof
**1. The natural-count identity (published input).** Dekking and van Loon prove a bijection between natural expansions of \(N\) and distinct-Fibonacci partitions of \(F_{-R(N)+2}N\), where \(R(N)\) in their notation is the lowest Bergman exponent. Here \(-R(N)=r(N)\), so
\[
 V(N)=R(F_{r(N)+2}N).
\]
This is their Theorem 4.4; it is explicitly an input, not a new assertion.

**2. A two-step tail-extension lemma.** Let \(w=10^{s_h}\cdots10^{s_1}1\) be a no-adjacent-ones word encoding the Bergman expansion, with \(s_i\ge1\). Append two zeros on the right and interpret the resulting binary word as a Zeckendorf representation with its last occupied position at Fibonacci index \(4\). The represented Fibonacci integer is \(F_{r(N)+4}N\): indeed, from the identity \(\varphi^i=F_i\varphi+F_{i-1}\), shifting the exponents of any representation by \(r(N)+4\) and comparing coefficients of \(\varphi\) gives \(\sum a_iF_{i+r(N)+4}=NF_{r(N)+4}\).

For clarity, let \(C_h\) be the number of Fibonacci partitions encoded by that word, truncating the left portion after its \((h+1)\)-st one, with the same final \(100\). The standard Fibonacci binary-flip block decomposition (the split/overlap argument in Dekking--van Loon, Section 2, and the Fibonacci counterpart of Robbins) gives
\[
 C_h=\begin{cases}
 (s_h/2+1)C_{h-1},&s_h\text{ even},\
 ((s_h+3)/2)C_{h-1}-C_{h-2},&s_h\text{ odd},
 \end{cases}\qquad(h\ge2).
\]
This recursion depends on interior zero gaps, not the terminal condition. It can also be obtained by splitting at the leftmost block \(10^{s_h}\): even gaps admit only independent prefix and suffix flips, while odd gaps admit an additional overlap state; subtracting the doubly counted preceding-tail state gives the displayed second term. The boundary values here are \(C_0=R(F_4)=R(3)=2\) and \(C_1=R(F_{s_1+5}+3)=s_1+2\). We verify the latter rather than assuming it: for \(j\ge8\), every representation of \(F_j+3\) either contains \(F_j\) (two choices to make \(3\)) or omits it, in which case it must contain \(F_{j-1}\), leaving \(F_{j-2}+3<F_{j-1}\). Hence \(R(F_j+3)=2+R(F_{j-2}+3)\); the bases \(R(F_6+3)=3\) and \(R(F_7+3)=4\) give \(R(F_j+3)=j-3\).

The published Knott and natural recurrences (Theorems 2.3 and 4.1 in the cited paper) have **exactly the same coefficient matrices** as this Fibonacci block recursion. Their initial values sum to \(K_0+V_0=2\) and \(K_1+V_1=s_1+2\), whether \(s_1\) is even or odd. Induction on \(h\), including the single-one base case, therefore yields
\[
 R(F_{r(N)+4}N)=C_h=K(N)+V(N).
\]
This is the new two-scale bridge.

**3. Exact inequality and equality.** Subtracting the natural recurrence from the Knott recurrence gives a difference sequence \(D_h\) with \(D_0=0\), initial \(D_1=0\) if \(s_1\) is even and \(D_1=1\) if \(s_1\) is odd, and the same gap matrices as above. When \(s_1\) is odd, the coefficients are at least \(2\), and the recurrence preserves \(D_h\ge D_{h-1}>0\) from \(D_1=1,D_0=0\). Thus \(K(N)>V(N)\) exactly when \(s_1\) is odd, and equality holds exactly when it is even. Proposition 5.1 of the source identifies the odd-gap case with even Lucas intervals and even-gap case with odd Lucas intervals. Combining this with Step 2 gives the sharp claimed dichotomy.

**4. Unbounded ratio.** At \(N=L_{2j+1}\), the source's Theorem 3.3 and its Lucas examples give \(K(N)=2j+1\) and \(V(N)=1\). The interval is even and \(r(N)=2j\). The bridge gives \(R(F_{2j+4}N)=2j+2\) and \(R(F_{2j+2}N)=1\), proving unboundedness.

## Verification
The separate file `verify.py` uses an independent subset-decomposition dynamic program for the distinct-Fibonacci partition function and compares both multipliers with the published word recurrences. It also checks the interval-dependent equality/strictness of the doubling law, and the Lucas endpoint family. Run `python verify.py`. The finite checks corroborate rather than establish the theorem. The infinite claim is established by the block recurrence, its verified boundary conditions, and the published expansion correspondences.

## Relationship to prior work
Dekking and van Loon, *Counting base phi representations* (arXiv:2304.11387, first posted 22 April 2023; Fibonacci Quarterly 62(2), May 2024), establish the Knott and natural recurrences and the one-scale identity \(V(N)=R(F_{r(N)+2}N)\). The two-scale bridge, the sharp Fibonacci-partition doubling inequality with an exact Lucas-interval equality locus, and its unbounded ratio are additional statements. Earlier literature on Fibonacci partitions, especially Robbins and Klarner, supplies the standard flip-counting framework. Shallit (arXiv:2305.02672) provides a separate automata perspective on base-\(\varphi\) representations; his accessible abstract does not settle this counting comparison, but the full paper has not been conclusively excluded.

## Limitations
The theorem uses the digit-dependent canonical multiplier \(F_{r(N)+2}\); it does not assert doubling for arbitrary Fibonacci multipliers or all integers at a fixed scale. The recurrence-based proof assumes the standard binary-flip enumeration for Fibonacci partitions and cites its primary source. Novelty is assessed within inspected literature, not certified by an independent reviewer. Numerical checks are finite and do not establish the infinite result.

## References
1. M. Dekking and A. van Loon, *Counting base phi representations*, arXiv:2304.11387v1 (22 April 2023); *Fibonacci Quarterly* 62(2), 2024, 114–123. https://arxiv.org/html/2304.11387v1
2. N. Robbins, *Fibonacci partitions*, *Fibonacci Quarterly* 34(4), 1996, 306–313.
3. D. A. Klarner, *Partitions of N into distinct Fibonacci numbers*, *Fibonacci Quarterly* 6(4), 1968, 235–243.
4. J. Shallit, *Proving properties of phi-representations with the Walnut theorem-prover*, arXiv:2305.02672 (4 May 2023).
