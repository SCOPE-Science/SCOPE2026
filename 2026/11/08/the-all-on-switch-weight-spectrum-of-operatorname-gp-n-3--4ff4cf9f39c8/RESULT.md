# All-on switch-weight spectra for generalized Petersen graphs with inner step three

## Finding and precise novelty

Let \(G=\operatorname{GP}(n,3)\), \(n\ge7\), with vertices \(u_i,v_i\) and edges \(u_iu_{i+1},u_iv_i,v_iv_{i+3}\) (indices modulo \(n\)). An all-on Lights Out strategy is a vertex subset \(S\) whose intersection with each **closed** neighbourhood is odd. Its labelled cardinality enumerator is
\[
 W_n(z)=\sum_{S:\,|S\cap N[x]|\equiv1\pmod2\ \forall x}z^{|S|}.
\]
Write \(g=\gcd(n,20)\). Then \(W_n(z)=R_g(z^{n/g})\), where
\[
\begin{aligned}
R_1(t)&=2t,&R_2(t)&=4t^2,\\
R_4(t)&=4t^2+8t^4+4t^6,&R_5(t)&=10t^3+12t^5+10t^7,\\
R_{10}(t)&=10t^6+44t^{10}+10t^{14},\\
R_{20}(t)&=4t^{10}+10t^{12}+60t^{18}+108t^{20}
 +60t^{22}+10t^{28}+4t^{30}.
\end{aligned}
\]
These are exact integer polynomials for every specified order, not empirical fits.

**Prior coverage and surviving contribution.** An earlier general theorem, *Exact two-colour closed-neighbourhood conflict-free census of generalized Petersen graphs* (October 2026 research record, public Git commit dated November 8, 2026, 20:01:35 UTC), establishes the **identical set of admissible binary configurations** through its polynomial-kernel criterion for arbitrary \(\operatorname{GP}(n,k)\), and hence supplies their total numbers for \(k=3\). It does not give their individual Hamming weights. This theorem's kernel/period factorization and the fact that step-three contains step-two solutions are consequently **not claimed as new**. The previously published full \(k=2\) inhomogeneous weight spectrum supplies every coefficient when \(4\nmid n\); the perfect-code classification of Wang and Zhang already supplies the four minimum solutions of size \(n/2\) when \(4\mid n\). The remaining independent exact finding is the full **weight splitting** at orders \(4\mid n\), particularly \(R_{20}\): at \(20\mid n\), it accounts for 256 solutions, with 192 strategies beyond the known step-two set. The result gives every nonminimum cost as well as the minimum.

In particular, at \(4\mid n\) and \(5\nmid n\), the three weights \(n/2,n,3n/2\) have multiplicities \(4,8,4\). At \(20\mid n\), the seven distinct weights \(n/2,3n/5,9n/10,n,11n/10,7n/5,3n/2\) have multiplicities \(4,10,60,108,60,10,4\). For all other \(n\), the old step-two enumerator applies unchanged.

## Proof

Put \(a_i,b_i\in\mathbb F_2\) for pressing \(u_i,v_i\). The equations for the all-on game are
\[
 a_{i-1}+a_i+a_{i+1}+b_i=1,\quad
 a_i+b_{i-3}+b_i+b_{i+3}=1.
\]
Eliminating \(b_i=1+a_{i-1}+a_i+a_{i+1}\) gives the reversible recurrence
\[
 a_{i-4}+a_{i-3}+a_{i-2}+a_{i-1}+a_{i+1}+a_{i+2}+a_{i+3}+a_{i+4}=0.
\]
Multiplication by the fourth power of the cyclic shift yields \(P_3(T)a=0\), with
\[
P_3(t)=1+t+t^2+t^3+t^5+t^6+t^7+t^8
=(t+1)^4(t^4+t^3+t^2+t+1).
\]
Because \(P_3(t)\mid t^{20}+1\) in \(\mathbb F_2[t]\), every solution is twenty-periodic; its given \(n\)-periodicity reduces this to \(g=\gcd(n,20)\). Conversely every \(g\)-periodic recurrence solution, with the uniquely determined \(b\), solves both original equations.

The recurrence is monic with nonzero constant term and has degree eight. Therefore each of its 256 possible eight-bit initial words extends uniquely to a bi-infinite periodic sequence. For each divisor \(g\) of twenty, retain exactly those sequences invariant under shift by \(g\), reconstruct \(b\) from the displayed formula, and tally the integer weight \(\sum_{i=0}^{g-1}(a_i+b_i)\). The resulting exhaustive census is

| \(g\) | \(w\!:\!\text{number of period-}g\text{ strategies}\) |
|---|---|
| 1 | \(1:2\) |
| 2 | \(2:4\) |
| 4 | \(2:4,\ 4:8,\ 6:4\) |
| 5 | \(3:10,\ 5:12,\ 7:10\) |
| 10 | \(6:10,\ 10:44,\ 14:10\) |
| 20 | \(10:4,\ 12:10,\ 18:60,\ 20:108,\ 22:60,\ 28:10,\ 30:4\) |

This is a complete 256-word finite certificate, not an infinite extrapolation: every unrestricted solution has already been proved to have period dividing twenty. The original bundled `periodic_check.py` implements the exact eight-bit census; the independent direct-neighbourhood linear algebra in `gauss_check.cpp` supplies a second verification for specified finite orders. Both files are preserved unchanged. Repetition of a period-\(g\) strategy exactly \(n/g\) times multiplies its weight by \(n/g\), proving \(W_n(z)=R_g(z^{n/g})\).

For comparison, the corresponding step-two elimination gives \(P_2(t)=(t+1)^2(t^4+t^3+t^2+t+1)\). Consequently \(P_2\mid P_3\), and the quotient of cyclic-solution-space sizes is four precisely when \(4\mid n\) and otherwise one. This numerical comparison also follows from the earlier general kernel theorem; it is included to identify the new **weight refinement**, not as a priority claim. At \(20\mid n\), subtraction of the previously known step-two polynomial gives the excess
\[
4z^{n/2}+60z^{9n/10}+64z^n+60z^{11n/10}+4z^{3n/2}.
\]

## Scope, interpretation and limitations

The graph is finite, simple and three-regular with \(n\ge7\). Strategies are labelled vertex subsets, not dihedral-orbit classes; double presses cancel over \(\mathbb F_2\). The polynomials for small formal periods are periodic-word counts, not the Lights Out polynomials of independent small graphs with invalid parameters. This result does not determine arbitrary starting configurations or arbitrary inner step \(k\), and the weights off multiples of four and the known perfect-code optimum are not newly established here. An unindexed earlier full weight-enumerator could still cover the surviving statement; originality remains best-of-knowledge.

## Relevant prior results

1. *Exact two-colour closed-neighbourhood conflict-free census of generalized Petersen graphs*, public scientific result: https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-exact-two-colour-closed-neighbourhood-conflict-free-census-of-ge--31f03994e1a6/RESULT.md . Its all-\(k\) kernel criterion describes precisely the odd-neighbourhood configurations and already yields their number.
2. *Complete odd-domination weight spectra of \(\operatorname{GP}(n,2)\)*: https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-complete-odd-domination-weight-spectra-of-operatorname-gp-n-2--7b458bdb223f/RESULT.md . Exact older weight spectrum for step two.
3. B. Torrence and R. Torrence, *An iterative strategy for Lights Out on Petersen graphs*, **Involve** 9 (2016), 721–732, DOI: 10.2140/involve.2016.9.721. The linear formulation and finite nullity table precede the weight refinement.
4. X. Wang and J. Zhang, *Classification of perfect and total perfect codes in generalized Petersen graphs*, arXiv:2603.20722v1 (March 21, 2026), Theorem 1.1, https://arxiv.org/html/2603.20722v1 . The four minimum perfect-code patterns are prior work.
5. H. Karami, *Perfect 2-colorings of the generalized Petersen graph GP(n,3)*, **EJGTA** 10 (2022), 239–245, DOI: 10.5614/ejgta.2022.10.1.16. These are equitable-neighbour counts, not the complete odd-neighbourhood weight spectrum.
6. Fu Xueliang, Yang Yuansheng and Jiang Baoqi, *On the domination number of generalized Petersen graphs P(n,3)*, **Ars Combinatoria** 84 (2007), 373–383. Its ordinary domination condition is weaker than parity-domination.
