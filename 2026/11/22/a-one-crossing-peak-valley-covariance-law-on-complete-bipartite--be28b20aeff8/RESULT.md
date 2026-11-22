# A one-crossing peak–valley covariance law on complete bipartite graphs

## Finding

Let \(a,b\) be integers with \(1\le a\le b\). Independently assign continuously distributed identically distributed heights to the vertices of the complete bipartite graph \(K_{a,b}\). Let \(P\) and \(V\) be its respective numbers of strict local maxima and strict local minima. Then

\[
\begin{aligned}
\operatorname{Cov}(P,V)={}&\frac{a(a-1)}{(b+1)(b+2)}+\frac{b(b-1)}{(a+1)(a+2)}\\
&+2-\frac{2}{\binom{a+b}{a}}-\left(\frac{a}{b+1}+\frac{b}{a+1}\right)^2. \tag{1}
\end{aligned}
\]

For \(a=b=1\), the covariance is zero. For \(a=1<b\), it is strictly negative. For each fixed \(a\ge2\), the value in (1) is **strictly decreasing as the integer \(b\) increases from \(a\)**, is positive at \(b=a\), and becomes negative for large \(b\). Consequently, the sign passes from positive through at most one zero to negative: there is a unique positive-to-nonpositive transition in part-size imbalance, with no reentry. Writing \(b_*(a)=\max\{b\ge a:\operatorname{Cov}(P,V)>0\}\), the positive part is precisely \(a\le b\le b_*(a)\), with at most one zero immediately afterward. The exact formula (1) resolves any boundary equality.

The transition has the sharp square-root scale

\[
 b_*(a)-a\sim\sqrt a \qquad (a\to\infty).
\]

More precisely, if \((b-a)/\sqrt a\to c\ge0\) as \(a\to\infty\), then \(a^2\operatorname{Cov}(P,V)\to 8(1-c^2)\). At \(c=1\), this limiting statement alone does not determine the finite-size sign.

## Assumptions and scope

The graph is finite, simple and has both bipartition classes nonempty. Heights are iid from any atomless common distribution, so their ranking is uniform. A vertex is a strict local maximum or minimum if its height exceeds or is below, respectively, all of its neighbors. Isolated vertices do not occur. The assertion is only about complete bipartite graphs; no monotonicity across arbitrary graph additions is claimed.

## Proof

**Ranking reduction.** Sort vertices by increasing height and write their bipartition classes as a uniformly random word containing \(a\) letters \(A\) and \(b\) letters \(B\). Exactly the vertices in its last monochromatic run are local maxima, and exactly those in its first run are local minima. Write these two run lengths \(T\) and \(H\), respectively; then \((P,V)=(T,H)\) in law.

Let \(H_A\) denote the number of initial \(A\) letters before the first \(B\), and \(H_B\) the number of initial \(B\) letters before the first \(A\). Define \(T_A,T_B\) analogously at the word's end. Thus \(H=H_A+H_B\) and \(T=T_A+T_B\). Elementary gap enumeration gives

\[
 \mathbb EH=\mathbb ET=\frac{a}{b+1}+\frac{b}{a+1},\qquad
 \mathbb E(H_AT_A)=\frac{a(a-1)}{(b+1)(b+2)},\quad
 \mathbb E(H_BT_B)=\frac{b(b-1)}{(a+1)(a+2)}.
\]

For the cross-color term, independently uniformize all heights to the interval \((0,1)\). Sum over the \(ab\) ordered \(A,B\) vertex pairs. An \(A\) vertex at value \(x\) contributes to \(H_A\) exactly if every \(B\) value exceeds \(x\); a \(B\) vertex at \(y\) contributes to \(T_B\) exactly if every \(A\) value is below \(y\). Hence

\[
\mathbb E(H_AT_B)=ab\int_{0<x<y<1}y^{a-1}(1-x)^{b-1}\,dx\,dy
=1-\frac{a!b!}{(a+b)!}=1-\binom{a+b}{a}^{-1}.
\]

The same holds for \(\mathbb E(H_BT_A)\); expanding \(\mathbb E(HT)-(\mathbb EH)^2\) proves (1).

**One-crossing certificate.** Define the rational function

\[
F(a,b)=\frac{a(a-1)}{(b+1)(b+2)}+\frac{b(b-1)}{(a+1)(a+2)}+2-\left(\frac{a}{b+1}+\frac{b}{a+1}\right)^2.
\]

Thus the covariance equals \(F(a,b)-2/\binom{a+b}{a}\). Direct rational simplification yields

\[
F(a,b)-F(a,b+1)=\frac{(b-a+1)(a+b+2)Q(a,b)}{(a+1)^2(a+2)(b+1)^2(b+2)^2(b+3)},
\]

where

\[
\begin{aligned}
Q(a,b)={}&3a^3b+5a^3+2a^2b^2+15a^2b+19a^2\\
&+ab^3+8ab^2+23ab+20a\\
&+2b^4+14b^3+34b^2+34b+12.
\end{aligned}
\]

All its coefficients are positive. The increase in the subtracted reciprocal-binomial correction when \(b\) advances by one is exactly \(2a/[(a+b+1)\binom{a+b}{a}]\).

For \(a\ge3\) and \(b\ge a\), \(\binom{a+b}{a}\ge\binom{a+b}{3}\). Set \(D=F(a,b)-F(a,b+1)\). The exact numerator of

\[
 D-\frac{12a}{(a+b+1)(a+b)(a+b-1)(a+b-2)}
\]

under its positive common denominator is a polynomial with **65 strictly positive integer coefficients** after the substitutions \(a=u+3\), \(b=u+3+v\), with \(u,v\ge0\). The standalone exact-symbolic verification program computes the numerator from the displayed rational formula and checks all coefficients and the denominator; this is a finite coefficientwise positivity certificate, not a numerical test. Therefore the covariance strictly decreases for every \(a\ge3,b\ge a\). For \(a=2\), the numerator of the exact one-step covariance decrement, after writing \(b=2+v\), is

\[
 v^6+23v^5+219v^4+1129v^3+3188v^2+4056v+936>0.
\]

At balance, (1) is \(4(2a+1)/[(a+1)^2(a+2)]-2/\binom{2a}{a}>0\) for every \(a\ge2\) (use \(\binom{2a}{a}\ge a(2a-1)\)). For each fixed \(a\), the covariance behaves as \(-b^2/[(a+1)^2(a+2)]+O(b)\) for \(b\to\infty\), proving a negative tail. At \(a=1\), (1) simplifies to

\[
 -\frac{(b-1)(b^3+5b^2-2b-12)}{12(b+1)^2},
\]

which vanishes at \(b=1\) and is negative at every integer \(b\ge2\).

**Transition scale.** For \(b=a+c\sqrt a\), with \(c\) bounded and \(a\) growing, expansion of \(F\) gives \(F=8(1-c^2)/a^2+O(a^{-5/2})\); the reciprocal-binomial term is exponentially small. Applied to integer sequences and combined with strict one-step monotonicity, this proves \(b_*(a)-a\sim\sqrt a\).

## Verification

Run `python verify.py`. It checks direct uniform-word enumeration against (1) on all tested small configurations, checks thousands of exact rational sign/decrement identities, verifies the 65-coefficient and seven-coefficient symbolic positivity certificates, and checks the square-root asymptotic algebra. These finite tests are ancillary to the general argument; the symbolic positivity certificate covers all integer parameters in the stated domain.

## Relationship to prior work

Baldi, Rinott and Stein (1989) develop local-extremum statistics for uniformly ranked graphs, emphasizing one-type extrema counts and a normal approximation for regular graphs. Burdzy and Pal (2016) study random graph labelings conditioned on one or two peaks and do not give a joint peak–valley covariance phase diagram. Known graph-local two-point extrema formulas can recover individual covariance summands and imply the rational identity (1) after summation, but do not by themselves provide the strict all-imbalance monotonicity and square-root transition proved here. The run-word equivalence is a reduction, not a novelty claim.

## Limitations

No independent audit or external priority certification has been performed. An equivalent boundary-run covariance calculation, or a general graph covariance formula coupled with an unlocated sign theorem, could predate this result. The integer transition is not asserted to avoid exact zeros; equation (1) decides ties. The square-root law is first-order and does not specify the next correction. The conclusions do not extend automatically to non-bipartite or non-complete graphs, or to nonidentically distributed vertex heights.

## References

1. P. Baldi, Y. Rinott, C. Stein, *On the Distribution of the Number of Local Minima of a Random Function on a Graph*, Neural Information Processing Systems, 1989, https://papers.neurips.cc/paper_files/paper/1989/file/d947bf06a885db0d477d707121934ff8-Paper.pdf.
2. K. Burdzy and S. Pal, *Twin peaks*, arXiv:1606.08025v1, first posted 2016-06-26, https://arxiv.org/abs/1606.08025.
