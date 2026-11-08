# Two-imbalance rigidity for unbiased single-pattern shifts

## Finding
Let \(w\) be a binary word containing at least two zeros and at least two ones. A *border* is a nonempty prefix that is also a suffix, including the full word. A border is *balanced* if it contains equally many zeros and ones. Let \(\rho(w)\) be the limiting proportion of ones when all finite binary words avoiding \(w\) are counted uniformly and their length tends to infinity. **If at most two borders of \(w\) are unbalanced, then**
\[
\rho(w)=\tfrac12\quad\Longleftrightarrow\quad\text{every border of }w\text{ is balanced}.
\]
This includes the first mixed-sign case not covered by the existing one-sided border-imbalance criterion. In particular, forbidding \(10001\) gives \(\rho\approx0.517189436751863\), while forbidding \(100011110001\) gives \(\rho\approx0.500000885746181\); both values are strictly larger than one half.

## Assumptions and scope
The alphabet is \(\{0,1\}\). The word \(w\) has length \(k\ge4\), with at least two occurrences of each letter. Put
\[
\mathcal B=\{j\in\{1,\ldots,k\}:w_1\cdots w_j=w_{k-j+1}\cdots w_k\},\qquad c_j=|w_1\cdots w_j|_1.
\]
Write \(a_n\) for the number of binary words of length \(n\) that avoid \(w\), and define
\[
\rho(w)=\lim_{n\to\infty}\frac{\sum_{u\in\{0,1\}^n,\,u\text{ avoids }w}|u|_1}{n a_n}.
\]
The assumption on both letter multiplicities avoids the four reducible exceptional words and ensures a primitive one-word-avoidance transition matrix, hence the existence of the limit, a simple dominant growth eigenvalue \(1<\lambda<2\), and analytic dependence on a positive letter weight near one. This is the standard single-pattern shift construction in [1,2]. Define the *imbalance polynomial*
\[
P_w(x)=\sum_{j\in\mathcal B}(j-2c_j)x^j.
\]
The assumption is that \(P_w\) has at most two nonzero monomials. No finite-length bound is asserted; the theorem holds for all words satisfying the stated hypotheses.

## Proof
The weighted avoidance generating function [1, Eq. (2.11)] is
\[
G(z,y)=\left(1-(1+y)z+\Big(\sum_{j\in\mathcal B}z^{-j}y^{-c_j}\Big)^{-1}\right)^{-1}.
\]
Its simple dominant positive singularity equals \(z=1/\lambda(y)\). By transfer-matrix Perron theory or differentiation of its simple pole,
\(\rho(w)=\lambda'(1)/\lambda(1)\).
Put \(F(x,y)=\big(1-(1+y)/x\big)\sum_{j\in\mathcal B}x^jy^{-c_j}+1\), so \(F(\lambda(y),y)=0\). At \(y=1\), the polynomial equation is
\[
H_w(x)=F(x,1)=(x-2)\sum_{j\in\mathcal B}x^{j-1}+1=0.
\]
Because \(k\in\mathcal B\), \(H_w\) is monic of degree \(k\). It has integer coefficients, and its constant coefficient is \(1\) if \(1\notin\mathcal B\), or \(-1\) if \(1\in\mathcal B\). Hence \(\lambda\), a zero of this monic polynomial, is an algebraic integer and an algebraic unit. As \(\lambda>1\), **no positive integral power of \(\lambda\) is rational**: otherwise that power and its inverse would both be rational algebraic integers, hence ordinary integers, forcing the power to be one.

Differentiate \(F\) at \((\lambda,1)\) in the direction \(\partial_y+(\lambda/2)\partial_x\). This direction annihilates the prefactor \(1-(1+y)/x\), while it sends the monomial \(x^jy^{-c_j}\) to \((j/2-c_j)\lambda^j\). Thus
\[
\Big(\partial_y+\tfrac\lambda2\partial_x\Big)F(\lambda,1)
=\frac{1-2/\lambda}{2}P_w(\lambda).
\]
The growth root is simple, so \(F_x(\lambda,1)=H'_w(\lambda)\ne0\). Implicit differentiation therefore yields
\[
\rho(w)=\tfrac12\quad\Longleftrightarrow\quad P_w(\lambda)=0.
\]
If there are no unbalanced borders, \(P_w\) vanishes identically. If there is exactly one, \(P_w(\lambda)\ne0\) because \(\lambda>0\). If there are exactly two, cancellation would give \(\lambda^{\ell-j}=-a/b\in\mathbb Q\), where \(j<\ell\) are distinct border lengths and \(a,b\) are their nonzero integer imbalances. This contradicts the algebraic-unit observation. These cases exhaust the hypotheses and prove both implications.

For completeness, differentiating the same implicit identity gives an exact signed formula. With \(T(x)=\sum_{j\in\mathcal B}x^j\),
\[
\rho(w)-\tfrac12=\frac{P_w(\lambda)}{2\lambda T(\lambda)H'_w(\lambda)}.
\]
The dominant root is the largest positive simple root of the monic entropy polynomial \(H_w\), so \(H'_w(\lambda)>0\), and the sign is the sign of \(P_w(\lambda)\).

For \(w=10001\), the borders have lengths \(1,5\) and one-counts \(1,2\). For \(w=100011110001\), they have lengths \(1,5,12\) and one-counts \(1,2,6\). In both cases \(P_w(x)=x^5-x>0\) for \(x>1\), proving the asserted strict inequalities. Their numerical values follow from the displayed algebraic equations, not from a finite-sample limit.

## Verification
The accompanying pure-Python `verify.py` uses two independent representations: the border-polynomial implicit-derivative formula, and left/right Perron vectors of the prefix-matching automaton. Every one of the \(426\) words of lengths \(4\) through \(8\) with at least two occurrences of both digits passed the comparison, with maximum observed absolute density discrepancy \(1.67\cdot10^{-16}\). The named longer examples passed as well; see `verification_output.txt`. This finite test checks the formulas, not the algebraic-unit proof, which is given above.

## Relationship to prior work
Bóna, Maga and Richey [1] introduce the weighted border polynomial, prove the balanced-border sufficient direction, and conjecture its necessity for limiting letter density (Conjecture 6.1). Their Theorem 3.5 resolves cases where all nonzero border imbalances have the same sign. The present theorem handles the first remaining mixed-sign situation—**two** nonzero imbalances with opposite signs—by exploiting the algebraic-unit property of the growth root; neither [1] nor the earlier unweighted single-pattern shift work [2] is claimed to supply this conclusion. In fact [1, §3.2] singles out \(10001\) and \(100011110001\) as cases beyond its one-sided criterion.

## Limitations
The full balanced-border necessity conjecture remains open when at least three borders have nonzero imbalance, and no claim is made about the stopping-time statistic \(q(w)\) from [1]. The two-letter multiplicity assumption excludes reducible exceptional shifts. The priority comparison is based on the inspected primary text, related earlier single-pattern-shift work, and mathematical-record searches; independently inaccessible manuscripts or implicit earlier equivalents remain a residual risk. No independent audit or peer review has been performed.

## References
[1] M. Bóna, B. Maga and J. Richey, *Letter frequency in shifts of finite type with one forbidden word*, arXiv:2606.06655, first publicly available 2026-06-04, version of 2026-09-09; https://arxiv.org/html/2606.06655 .

[2] N. Chandgotia, B. Marcus, J. Richey and C. Wu, *Shifts of finite type obtained by forbidding a single pattern*, arXiv:2409.09024 (2024), Discrete and Continuous Dynamical Systems 48 (2026), 538–576; https://www.aimsciences.org/article/doi/10.3934/dcds.2025152 .

[3] L. Guibas and A. Odlyzko, *String overlaps, pattern matching, and nontransitive games*, Journal of Combinatorial Theory A 30 (1981), 183–208.
