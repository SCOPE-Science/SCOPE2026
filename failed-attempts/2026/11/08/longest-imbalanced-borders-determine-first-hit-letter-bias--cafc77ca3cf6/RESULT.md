# Longest imbalanced borders determine first-hit letter bias

## Finding

Let \(w\) be any nonempty binary pattern. Sample independent, fair binary letters until the first completed occurrence of \(w\), and let \(\tau_w\) be that stopping time. Write \(N_w\) for the number of ones sampled up to and including time \(\tau_w\), and define
\[
q(w)=\mathbb E\!\left[\frac{N_w}{\tau_w}\right].
\]
A nonempty border of \(w\) is a prefix that is also a suffix; the full word is included. For a border of length \(b\), put \(d_b=2|w_1\cdots w_b|_1-b\). If all \(d_b=0\), then \(q(w)=1/2\). Otherwise, let \(k\) be the **largest** border length with \(d_k\ne0\). The exact strict-sign law is
\[
\operatorname{sgn}\!\left(q(w)-\tfrac12\right)=\operatorname{sgn}(d_k).
\]
In particular, \(q(w)=1/2\) if and only if every nonempty border is balanced. This settles the first-hit proportion clause of the half-frequency conjecture in [1], without asserting a new result about the separate asymptotic shift frequency.

## Assumptions and scope

The sample letters are independent Bernoulli(\(1/2\)); the forbidden/target word \(w\) has positive length. Occurrence means a contiguous factor, overlaps are allowed, and \(\tau_w\) is the index of the final letter of the first occurrence. Every finite word appears almost surely: inspection of disjoint blocks of length \(|w|\) gives geometric tail bounds, so \(\tau_w\) is finite almost surely and has all moments. The statistic is the expectation of the *random fraction* \(N_w/\tau_w\), not the ratio \(\mathbb E[N_w]/\mathbb E[\tau_w]\), not a typical long-word frequency, and not a density conditioned on survival.

## Proof

Write \(\mathcal B(w)\) for the set of nonempty border lengths, including \(n=|w|\), and define, for positive \(t\),
\[
C(t)=\sum_{b\in\mathcal B(w)}t^b,\qquad H(t)=\sum_{b\in\mathcal B(w)}d_b t^b.
\]
The first-hit bivariate generating function proved in [1, Fact 2.9, Eq. (2.12)] is
\[
\Phi(x,y)=\mathbb E[x^{\tau_w}y^{N_w}]
=\frac1{1+[1-x(1+y)/2]\sum_{b\in\mathcal B(w)}(2/x)^b y^{-|w_1\cdots w_b|_1}}.
\tag{1}
\]
The expression is interpreted initially at positive \(x,y\) near \((1,1)\), or by clearing Laurent denominators as a rational power series. The normalization agrees with the first-hit convention above. In particular \(\Phi(1,1)=1\).

Substitute \(x=z e^{-u}\) and \(y=e^{2u}\) for fixed \(0<z<1\). The denominator of (1) becomes
\[
D(u,z)=1+(1-z\cosh u)\sum_{b\in\mathcal B(w)}(2/z)^b e^{-d_bu}.
\]
Consequently, at \(u=0\),
\[
\left.\partial_u\Phi(ze^{-u},e^{2u})\right|_{u=0}
=\mathbb E[(2N_w-\tau_w)z^{\tau_w}]
=\frac{(1-z)H(2/z)}{[1+(1-z)C(2/z)]^2}.
\tag{2}
\]
For integer \(\tau_w\ge1\), \(1/\tau_w=\int_0^1z^{\tau_w-1}\,dz\). Absolute integrability follows from
\[
\mathbb E\left[\int_0^1 |2N_w-\tau_w|z^{\tau_w-1}\,dz\right]
=\mathbb E\left[\frac{|2N_w-\tau_w|}{\tau_w}\right]\le1.
\]
Thus Fubini and (2) give the **exact integral identity**
\[
q(w)-\frac12=\frac12\int_0^1
\frac{(1-z)H(2/z)}{z[1+(1-z)C(2/z)]^2}\,dz.
\tag{3}
\]
The kernel outside \(H\) is strictly positive for \(0<z<1\). The integral converges absolutely by the preceding argument; the displayed rational expression is evaluated only on \((0,1)\).

It remains to prove that \(H(t)\) has a strict constant sign on \(t\ge2\) unless it vanishes identically. If all borders are balanced, \(H=0\), so (3) immediately gives equality. Otherwise let \(k\) be the largest imbalanced border and first suppose \(d_k>0\). As \(d_k\) is an integer, \(d_k\ge1\). For every smaller border length \(j<k\), the imbalance along the binary prefix changes by at most one per additional symbol; therefore
\[
d_j\ge d_k-(k-j)\ge1-(k-j).
\]
All border coefficients for lengths exceeding \(k\) vanish by maximality. Discarding nonnegative terms and allowing a negative contribution at *every* integer \(j\) between 1 and \(k-2\) (even when it is not a border) yields
\[
H(t)\ge t^k-\sum_{j=1}^{k-2}(k-j-1)t^j=:F_k(t).
\tag{4}
\]
For \(k=1,2\) the sum is empty. The finite geometric-arithmetic sum gives the polynomial identity
\[
(t-1)^2F_k(t)=(t-2)t^{k+1}+(k-1)t^2-(k-2)t.
\tag{5}
\]
For \(k=1\), the right side is \(t(t-1)^2>0\); for every \(k\ge2\) and \(t\ge2\), the first term is nonnegative and the remaining part is \(t[(k-1)t-(k-2)]>0\). Thus \(H(t)>0\) for all \(t\ge2\). If \(d_k<0\), interchange the two letters: every border length is unchanged and every imbalance changes sign. The same argument applied to the complemented word proves \(H(t)<0\) for every \(t\ge2\).

Since \(2/z>2\) for \(0<z<1\), equation (3) now gives the claimed strict sign. No limiting argument from finitely many words is used.

## Verification

The standalone standard-library `checker.py` first compares the rational bivariate first-hit identity with an independently constructed prefix-automaton distribution using exact fractions, for every binary pattern of lengths 1 through 6 and stopping-time coefficients through length 13 (126 patterns). It then evaluates (3) numerically and compares its sign with the final imbalanced border for every binary pattern of lengths 1 through 10 (2,046 patterns). For eleven specified examples, a separate first-hit state recurrence computes the actual expected proportion and its residual tail probability to compare with the integral. Run `python3 checker.py` beside this file. These computations test the formulas; the proof of the universal statement is (1)--(5), not enumeration.

Illustrations: \(q(0110)\approx0.497999354238\) although its full border is balanced; its longest imbalanced border has imbalance \(-1\). In contrast \(q(1001)\approx0.502000645762\). Both \(01\) and \(10\) have \(q=1/2\).

## Relationship to prior work

Bóna, Maga and Richey [1] introduce this exact first-hit proportion \(q\), supply the bivariate generating function used in (1), and explicitly conjecture that \(q=1/2\) characterizes balanced borders. Their results also address a distinct asymptotic shift-frequency statistic \(\rho\). The public balanced-border theorem discussed in [2] settles the \(\rho\) half-frequency equivalence, and its border-imbalance envelope resembles (4)--(5), but it explicitly leaves the \(q\) conjecture open. The present additional ingredient is the integral sign representation (3): positivity of the same border polynomial at **every** real \(t\ge2\) determines an expectation of random ratios, not merely a spectral-root evaluation. Asymptotic \(\rho\) results alone do not imply the \(q\) statement. Chandgotia, Marcus, Richey and Wu [3] treat one-pattern shifts and avoidance rather than this expected first-hit fraction.

## Limitations

The theorem uses a single target pattern, iid fair bits, and first occurrence including its final letter. It does not classify arbitrary biased Bernoulli sources, multiple forbidden words, higher alphabets, or the entire distribution of \(N_w/\tau_w\). The proof relies on the published first-hit generating-function identity [1]; the included independent series tests are not a replacement for that literature premise. Historical priority beyond the directly inspected sources remains open to independent review; no independent audit is claimed.

## References

[1] M. Bóna, B. Maga, and J. Richey, *Letter frequency in shifts of finite type with one forbidden word*, arXiv:2606.06655, first submitted 2026-06-04, especially Fact 2.9, equation (2.12), and Conjecture 6.1. https://arxiv.org/abs/2606.06655

[2] *Half letter frequency characterizes balanced borders*, public research dossier and linked proof record, https://www.trureturing.org/research/bona-maga-richey-2026-half-frequency-balanced-borders/ (accessed 2026-11-04 UTC). This solves the separate \(\rho\) assertion, explicitly not the \(q\) assertion.

[3] N. Chandgotia, B. Marcus, J. Richey, and C. Wu, *Shifts of Finite Type Obtained by Forbidding a Single Pattern*, arXiv:2409.09024, first released 2024-09-13. https://arxiv.org/abs/2409.09024
