# Three noise scales for assortativity and stable-matching multiplicity in a Mallows market

## Finding

In a complete, strict, balanced \(3\times3\) stable-marriage market, suppose all six agents independently draw their preferences from the same Mallows distribution with dispersion \(\phi\in[0,1]\), centered on the order \(1\succ2\succ3\). Let \(N\) be the number of stable perfect matchings, and let \(I\) be the event that the perfectly assortative matching \(\mu(i)=i\) is stable. Write
\[
L(\phi)=1+\phi+\phi^2,\qquad D(\phi)=(1+\phi)^4L(\phi)^6.
\]
For a list of coefficients \(c_0,\ldots,c_d\), define the palindromic polynomial
\[
T_{2d}(\phi;c_0,\ldots,c_d)
=c_d\phi^d+\sum_{j=0}^{d-1}c_j(\phi^j+\phi^{2d-j}).
\]
The following polynomials specify the exact probabilities:
\[
\begin{aligned}
R(\phi)&=T_{12}(\phi;2,6,27,85,192,300,348),\\
S(\phi)&=T_6(\phi;6,32,58,81),\\
B(\phi)&=T_{18}(\phi;1,8,36,112,266,510,822,1142,1389,1482).
\end{aligned}
\]
Then
\[
\boxed{\begin{aligned}
\Pr(N\ge2)&=\frac{2\phi^2R(\phi)}{D(\phi)},\\
\Pr(N=3)&=\frac{\phi^5S(\phi)}{D(\phi)},\\
\Pr(I)&=\frac{B(\phi)}{(1+\phi)^6L(\phi)^6}.
\end{aligned}}
\]
For every \(0<\phi<1\), the first two probabilities are strictly increasing functions of \(\phi\), whereas \(\Pr(I)\) is strictly decreasing. Their distinct small-dispersion laws are
\[
\Pr(I^c)=4\phi+O(\phi^2),\quad
\Pr(N\ge2)=4\phi^2+O(\phi^3),\quad
\Pr(N=3)=6\phi^5+O(\phi^6).
\]
The exponents are exact: the smallest total number of preference inversions needed to produce the three respective events is \(1\), \(2\), and \(5\), with exactly \(4\), \(4\), and \(6\) labeled profiles at those minima. At \(\phi=1\), the probabilities \(\Pr(I)\), \(\Pr(N\ge2)\), and \(\Pr(N=3)\) are \(5027/23328\), \(131/486\), and \(91/3888\), respectively.

## Assumptions and scope

There are exactly three agents on each side, all partners are acceptable, and every ranking is strict. In each ranking, the six permutations \(\pi\in S_3\) occur with probabilities \(\phi^{\operatorname{inv}(\pi)}/Z(\phi)\), independently across the six agents, where
\[
Z(\phi)=\sum_{\pi\in S_3}\phi^{\operatorname{inv}(\pi)}
=1+2\phi+2\phi^2+\phi^3=(1+\phi)L(\phi).
\]
An inversion means a pair of candidate labels reversed relative to the common order. At \(\phi=0\), all six rankings equal that common order; at \(\phi=1\), all rankings are independent and uniform. The matching \(\mu(i)=i\) pairs each agent with the same-ranked opposite-side agent. A matching is stable exactly when it has no pair of unmatched agents who strictly prefer each other to their respective assigned partners.

No claim is made for more than three agents per side, non-Mallows preference models, correlated draws across agents, or differing dispersion on the two sides.

## Proof

**Exhaustive finite polynomial identity.** For each of the \(6^6=46{,}656\) labeled profiles \(P=(\pi_1,\ldots,\pi_6)\), define \(s(P)=\sum_{a=1}^{6}\operatorname{inv}(\pi_a)\). For each of the six possible matchings \(\mu\in S_3\), inspect all pairs \((i,j)\) not contained in \(\mu\). Such a pair blocks if and only if
\[
\operatorname{rank}_{m_i}(j)<\operatorname{rank}_{m_i}(\mu(i))
\quad\text{and}\quad
\operatorname{rank}_{w_j}(i)<\operatorname{rank}_{w_j}(\mu^{-1}(j)).
\]
The strict inequalities use zero-based positions in the corresponding rankings. Thus the six candidate tests determine the exact integer \(N(P)\), and the same tests determine whether \(\mu(i)=i\) is stable. The full, finite enumeration is given by the standalone files `verify.py` and `verify_independent.cpp`, the latter independently implementing the matching tests in C++. Both traverse every profile, not a statistical sample, and both reproduce every coefficient in `coefficients.json`.

In particular, the complete inversion enumerators \(H_j(\phi)=\sum_{P:N(P)=j}\phi^{s(P)}\), for \(j=1,2,3\), have the following first ten coefficients; all are degree-18 palindromic polynomials and their remaining coefficients are determined by reflection:
\[
\begin{aligned}
H_1&=T_{18}(\phi;1,12,68,266,758,1642,2821,4006,4872,5188),\\
H_2&=T_{18}(\phi;0,0,4,20,82,284,734,1410,2051,2314),\\
H_3&=T_{18}(\phi;0,0,0,0,0,6,44,128,229,278).
\end{aligned}
\]
Here \(N(P)\in\{1,2,3\}\) for every enumerated profile, with total unweighted counts \(34{,}080\), \(11{,}484\), and \(1{,}092\). The polynomial enumerator for the assortative-stability event is \(B\) as defined above. Every profile has probability \(\phi^{s(P)}/Z(\phi)^6\), so dividing the appropriate enumerators by \(Z(\phi)^6\) proves the exact probability identities upon factoring the integer polynomials \(H_2+H_3\) and \(H_3\). The denominator is positive on the stated parameter interval.

**Strict monotonicity.** Define the following further palindromic polynomials, all of whose displayed coefficients are strictly positive:
\[
\begin{aligned}
U&=T_{14}(\phi;4,10,58,305,1001,2141,3270,3738),\\
V&=T_8(\phi;15,111,310,557,669),\\
H&=T_{18}(\phi;2,18,91,323,876,1888,3323,4872,6067,6513).
\end{aligned}
\]
Exact integer polynomial multiplication and differentiation give
\[
\begin{aligned}
\frac{d}{d\phi}\Pr(N\ge2)
&=\frac{2\phi(1-\phi)U(\phi)}{(1+\phi)^5L(\phi)^7},\\
\frac{d}{d\phi}\Pr(N=3)
&=\frac{2\phi^4(1-\phi)V(\phi)}{(1+\phi)^5L(\phi)^7},\\
\frac{d}{d\phi}\Pr(I)
&=-\frac{2(1-\phi)H(\phi)}{(1+\phi)^7L(\phi)^7}.
\end{aligned}
\]
Every denominator and every polynomial \(U,V,H\) is positive for \(0<\phi<1\), proving the three strict monotonicity assertions. The code checks these identities by exact integer convolution, without numeric differentiation.

**Sharp inversion thresholds.** The coefficient of \(\phi^s\) in an event enumerator counts exactly the labeled profiles of inversion total \(s\) realizing that event. Since \(Z(\phi)^6\) has first two coefficients \(1,12\), while \(B\) starts \(1,8\), precisely four inversion-one profiles make the assortative matching unstable. The enumerators \(H_2+H_3\) and \(H_3\) have their first nonzero terms \(4\phi^2\) and \(6\phi^5\), respectively, which proves both sharp minima and their multiplicities. Their quotients by \(Z(\phi)^6\) give the stated asymptotic expansions. Explicit examples, giving each side's three rankings in agent order, are:

- One inversion, assortative matching unstable: men \((123,123,123)\), women \((213,123,123)\).
- Two inversions, two stable matchings: men \((213,123,123)\), women \((123,213,123)\); the stable matchings are \((123)\) and \((213)\).
- Five inversions, three stable matchings: men \((123,213,132)\), women \((213,312,123)\); the stable matchings are \((123)\), \((213)\), and \((312)\).

The notation \((abc)\) for a matching means man \(1\) matches woman \(a\), man \(2\) matches woman \(b\), and man \(3\) matches woman \(c\). All displayed rankings likewise list opposite-side partners from most to least preferred. The endpoint values follow by evaluating the exact rational formulas at \(\phi=1\).

## Verification

The finite certificate is `coefficients.json`. Running `python3 verify.py` performs the complete integer enumeration of all \(46{,}656\) ranking profiles and six matchings per profile, checks the four 19-coefficient enumerators, verifies every rational-polynomial identity and its factored derivative, and checks the first-nonzero-degree assertions. Independently, `c++ -O2 -std=c++17 verify_independent.cpp -o verify_independent && ./verify_independent` recomputes the complete enumerators using an independent implementation. No sampling or floating-point arithmetic is involved. These are exhaustive finite mathematical checks, not evidence for a theorem in unrestricted market size.

## Relationship to prior work

Wang (2026) proves rank-quantile assortativity for fixed Mallows dispersion below one as market size tends to infinity, using the same independent correlated-preference model, but does not determine exact finite-market probabilities of the perfectly assortative matching being stable or of stability multiplicity. Hoffman, Levy and Mossel (2023) establish exponential growth of stable-matchings counts as market size increases under Mallows preferences; their result does not imply these fixed-three-agent rational laws or their sharp noise powers. Angel, Holroyd, Hutchcroft and Levy (2018) instead generate a Mallows-distributed *matching* from percolation of compatibility edges under common deterministic preferences; this is a different random model and has a unique finite stable matching. Borodin and coauthors (2021) enumerate precisely \(34{,}080\), \(11{,}484\), and \(1{,}092\) labeled three-by-three profiles with one, two, and three stable matchings under uniform preferences. A separate published full-symmetry orbit census refines these numbers by relabeling classes, but neither source weights rankings by total inversions about a common reference order. Their \(\phi=1\) endpoint cannot determine the interpolation, sharp low-noise exponents, or derivative signs for \(0<\phi<1\). The result distinguishes the finite-noise limit from the large-market limit.

## Limitations

The exact formulas use exactly three persons on each side, a common reference ranking, identical Mallows dispersion for all six agents, independent preference draws, and complete strict rankings. The monotonicity statements should not be extrapolated to larger markets or heterogeneous preference parameters. The probability that the perfectly assortative matching is stable is not the probability that every stable matching is perfectly assortative; the latter is a different event. The finite certificates prove the stated finite-domain identities, not an asymptotic law in market size. Unindexed equivalent finite-market calculations may exist.

## References

- Wang, B. (2026), *Random Matching Markets with Correlated Preferences*, arXiv:2603.24526, first posted 2026-03-25. https://arxiv.org/abs/2603.24526
- Hoffman, C., Levy, A., and Mossel, E. (2023), *Stable Matchings with Correlated Preferences*, arXiv:2312.14813, first posted 2023-12-22. https://arxiv.org/abs/2312.14813
- Borodin, M., et al. (2021), *Sequences of the Stable Matching Problem*, arXiv:2201.00645v1, first posted 2021-12-29. https://arxiv.org/abs/2201.00645
- Angel, O., Holroyd, A. E., Hutchcroft, T., and Levy, A. (2018), *Mallows Permutations as Stable Matchings*, arXiv:1802.07142, first posted 2018-02-20. https://arxiv.org/abs/1802.07142
