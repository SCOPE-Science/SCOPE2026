# Exact extreme-edge sensitivity trichotomy for left-permutive binary cellular automata

## Finding
For **all** left-permutive elementary binary cellular automata and all integer times \(t\ge1\), the fair-Bernoulli influence of the initial coordinate at the *rightmost* edge of the backward light cone takes exactly one of the three values \(0\), \(2^{-t}\), and \(1\). The case is completely determined by the two values of the local right Boolean derivative, independently of \(t\). Of the 16 left-permutive elementary rules, precisely 4 fall in the zero class, 8 in the exponential class, and 4 in the unit class. In particular, Rule 30 has right-edge influence exactly \(2^{-t}\) and left-edge influence \(1\) for every \(t\ge1\).

## Assumptions and scope
Use the two-sided full binary shift with coordinatewise independent fair initial bits \(X_i\), \(i\in\mathbb Z\). A left-permutive elementary local rule has the unique form
\[
g(a,b,c)=a\oplus h(b,c),\qquad h:\{0,1\}^2\to\{0,1\},
\]
with \(\oplus\) denoting XOR. Write \(F(X)_i=g(X_{i-1},X_i,X_{i+1})\), and let \(X^{(j)}\) denote the configuration obtained by toggling \(X_j\). For each integer \(t\ge1\), the influence at location \(j\) is
\[
I_t(j)=\Pr\!\big[(F^tX)_0\ne(F^tX^{(j)})_0\big].
\]
Only the extreme coordinates \(j=-t\) and \(j=t\) are considered. Define the right Boolean derivative
\[
\delta(b)=h(b,0)\oplus h(b,1),\qquad b\in\{0,1\}.
\]
Then the exact **right-edge trichotomy** is
\[
I_t(t)=
\begin{cases}
0,&(\delta(0),\delta(1))=(0,0),\\
1,&(\delta(0),\delta(1))=(1,1),\\
2^{-t},&(\delta(0),\delta(1))\in\{(0,1),(1,0)\}.
\end{cases}
\]
The familiar left-permutivity consequence \(I_t(-t)=1\) serves as comparison and is **not** claimed as new. The statement is restricted to fair iid input and radius-one binary rules, and makes no claim about inner-cone influences or biased initial measures.

## Proof
**1. Unique fastest path.** Consider toggling the initial bit at site \(t\) and observing site \(0\) after exactly \(t\) updates. At each update its effect can move left at most one site. Therefore any influence reaching the observation travels through the unique left-moving fastest path. A toggle arriving as the right input of \(g(a,b,c)\) propagates precisely when \(\delta(b)=1\), regardless of the left input. Define the unperturbed center bits along that path by
\[
Z_s=(F^sX)_{t-1-s},\qquad 0\le s\le t-1.
\]
Each \(Z_s\) depends only on initial coordinates through \(t-1\), so it is unchanged when the site \(t\) is flipped. The Boolean chain rule along the unique path gives the **pointwise identity**
\[
\mathbf1\!\{(F^tX)_0\ne(F^tX^{(t)})_0\}
=\prod_{s=0}^{t-1}\delta(Z_s).
\]
This does not assume independence of nearby space-time cells.

**2. Fairness and independence of boundary inputs.** Left-permutivity implies, by induction on \(s\), that for every site \(i\) there is a Boolean function \(R_{s,i}\) such that
\[
(F^sX)_i=X_{i-s}\oplus R_{s,i}(X_{i-s+1},\ldots,X_{i+s}).
\]
In particular,
\[
Z_s=X_{t-1-2s}\oplus R_s(X_{t-2s},\ldots,X_{t-1}).
\]
The first bit on the right is independent and fair, conditional on all the coordinates having index at least \(t-2s\). Earlier \(Z_0,\ldots,Z_{s-1}\) are measurable with respect to these latter coordinates, because \(Z_r\) uses only indices \(t-1-2r\) through \(t-1\). Hence \(Z_s\) is conditionally fair and independent of all earlier \(Z_r\). Inductively, \(Z_0,\ldots,Z_{t-1}\) are independent Bernoulli\((1/2)\) variables.

**3. Exact influence.** Take expectations in the pointwise product. If both \(\delta\) values vanish, the influence vanishes. If both are one, the influence is one. Otherwise \(\delta\) is the indicator of exactly one bit value, and the independence just proved yields probability \(2^{-t}\).

**4. Complete rule census.** There are exactly \(2^4=16\) choices for the four truth-table entries of \(h\). For any prescribed ordered pair \((\delta(0),\delta(1))\), the values \(h(0,0)\) and \(h(1,0)\) can be chosen independently, after which the two remaining entries are forced. Thus every derivative pair occurs for exactly four rules: four zero, four unit and eight exponential. For Rule 30, \(h(b,c)=b\lor c\), so \(\delta(0)=1\) and \(\delta(1)=0\). Its left-edge influence is one by left-permutivity (along the unique right-moving fastest path), as already known.

## Verification
The standalone `check_edge_influence.py` enumerates all \(16\) left-permutive elementary binary rules and all \(2^{2t}\) assignments of the other input bits for each \(1\le t\le6\), comparing the exact observed right-edge influence with the three predicted counts. All \(96\) full rule/time comparisons and \(80\) boundary-factorization and fair-independence comparisons passed. The code checks that Rule 30 corresponds to the specified truth table. Its finite tests do not prove the statement for unbounded \(t\); Steps 1–4 do. Run `python check_edge_influence.py` with Python 3; no third-party package is required.

## Relationship to prior work
Chan-López and Martín-Ruiz, arXiv:2604.00165, define the very same Boolean-influence observable and prove unit influence for the leftmost cone coordinate (their Proposition 4). Their Section 8.2 gives Monte Carlo evidence for right-side decay but **no all-time right-edge formula or complete 16-rule classification**. The present statement resolves the extreme right edge of that empirical profile, not the full profile or the deterministic single-seed problem. The standard preimage theory for permutive cellular automata concerns reachability, not the probability that a far-edge bit flip survives. Wolfram's Rule 30 discussion establishes one-sided propagation qualitatively but not this fair-coin trichotomy.

## Limitations
The exact formula is for the outermost light-cone coordinate only, not for the broad interior right-side sensitivity shown in numerical plots. For biased or correlated initial inputs, the boundary sequence need not be independent fair bits, and the exponential coefficient need not equal \(1/2\). This proof does not resolve any computational universality or single-seed randomness conjecture. The novelty assessment is based on inspected material and literature searches, not a proof that no earlier equivalent Boolean-derivative identity exists. Independent external audit has not been performed.

## References
1. E. Chan-López and A. Martín-Ruiz, *Symmetric Nonlinear Cellular Automata as Algebraic References for Rule 30*, arXiv:2604.00165 (first posted 2026-03-31), especially Section 8.2 and Proposition 4. https://arxiv.org/abs/2604.00165
2. S. Wolfram, *A New Kind of Science*, Chapter 10 notes on Rule 30's one-sided additivity and right-neighbor irrelevance. https://www.wolframscience.com/nks/notes-10-10--cryptographic-properties-of-rule-30/
3. *Combinatorial designs and cellular automata: A survey*, *Discrete Applied Mathematics*, doi:10.1016/j.dam.2025.10.014 (preimage/permutivity background; full text not inspected).
