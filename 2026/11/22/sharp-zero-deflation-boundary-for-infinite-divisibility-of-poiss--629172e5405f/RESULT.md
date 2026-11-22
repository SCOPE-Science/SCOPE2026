# Sharp zero-deflation boundary for infinite divisibility of Poisson–Bilal counts

## Finding
Consider the one-parameter Poisson–Bilal count law of Eliwa and collaborators (2023), with Bilal mixing scale \(\beta>0\), and modify its zero mass by multiplying every strictly positive count probability by a common factor \(t>0\) and choosing the mass at zero to normalize the distribution. The modified law is valid exactly when
\[
0<t\le \frac1{1-c_\beta},\qquad
c_\beta=\frac6{(\beta+2)(\beta+3)},
\]
where the rightmost equality allows zero mass at the upper endpoint. Within the nondegenerate, positive-zero-mass range \(0<t<1/(1-c_\beta)\), the modified law is infinitely divisible on the nonnegative integers **if and only if**
\[
\boxed{t\le t_*(\beta):=1+\frac3{(\beta+1)(2\beta+7)}.}
\]
For \(0<t\le1\), every genuine zero inflation preserves infinite divisibility. For \(1<t\le t_*(\beta)\), a nonempty interval of zero *deflation* also preserves infinite divisibility, including equality. For \(t_*(\beta)<t<1/(1-c_\beta)\), infinitely many even-order coefficients in the logarithm of the probability-generating function are strictly negative, hence no compound-Poisson representation exists. At the upper endpoint \(t=1/(1-c_\beta)\), the law has positive mass at \(1\) but zero mass at \(0\), and is not infinitely divisible on the nonnegative integers. The special modification \(t=0\) is the degenerate law at zero and is infinitely divisible.

## Assumptions and scope
Use zero-based geometric variables \(\operatorname{Geom}_0(q)\) with \(\Pr(G=k)=(1-q)q^k\) for integers \(k\ge0\). The parent Poisson–Bilal law is the mixed Poisson distribution with Bilal mixing density
\[
f_\beta(\lambda)=\frac6\beta\left(e^{-2\lambda/\beta}-e^{-3\lambda/\beta}\right),\quad\lambda>0,
\]
with \(\beta>0\). Let
\[
a=\frac\beta{\beta+2},\quad b=\frac\beta{\beta+3},\quad c=(1-a)(1-b)=c_\beta.
\]
Then \(0<b<a<1\). Its probability-generating function is
\[
G(z)=\frac{c}{(1-az)(1-bz)}.
\]
Consequently this parent has the *already known* form of a convolution of two nonidentically parameterized geometric variables, a member of the Newton convolution class studied by Hürlimann (2015). This identification is only an input to the new zero-modification theorem, not itself asserted as an original distribution class.

The zero-modified generating function is
\[
F_t(z)=1-t+tG(z),\quad p_0=1-t(1-c),\quad
p_k=t\Pr(X=k)\ (k\ge1).
\]
Ordinary infinite divisibility here means that, for every positive integer \(m\), the count law is the convolution of \(m\) identical nonnegative-integer laws. For a nondegenerate such law with \(p_0>0\), this is equivalent to having a compound-Poisson representation with nonnegative canonical intensities of every positive integer order.

## Proof
**Step 1 (parent decomposition).** Conditioned on the Bilal mixing variable \(\Lambda\), the count is \(\operatorname{Poisson}(\Lambda)\). Integrating its conditional generating function gives
\[
\begin{aligned}
G(z)&=\frac6\beta\left(\frac1{1+2/\beta-z}-\frac1{1+3/\beta-z}\right)\\
&=\frac{(1-a)(1-b)}{(1-az)(1-bz)}.
\end{aligned}
\]
In particular \(G(0)=c\) and its two geometric factors are independent. This establishes all formulas in the assumptions.

**Step 2 (canonical coefficients).** For \(0<t<1/(1-c)\), put \(d=1-t(1-c)>0\), \(u=1-t\), and write
\[
F_t(z)=\frac{d-u(a+b)z+uabz^2}{(1-az)(1-bz)}.
\]
Let \(\rho_1,\rho_2\) be the two (possibly complex) roots of the *root-parameter* quadratic
\[
w^2-\frac{u(a+b)}d\,w+\frac{uab}d=0.
\]
The numerator of \(F_t(z)\) is then \(d(1-\rho_1z)(1-\rho_2z)\). Expanding \(\log F_t(z)-\log F_t(0)\) as a power series at zero yields the unique formal canonical coefficients
\[
\nu_n=\frac{a^n+b^n-\rho_1^n-\rho_2^n}{n},\qquad n\ge1.
\]
Any compound-Poisson representation forces \(\nu_n\ge0\) for every \(n\), and if all \(\nu_n\ge0\) with \(\sum_n\nu_n=-\log d<\infty\), then \(F_t(z)=\exp(\sum_n\nu_n(z^n-1))\), establishing infinite divisibility.

**Step 3 (all zero inflations).** For \(0<t<1\), set \(x=u/d\). Because \(d=u+tc>u>0\), we have \(0<x<1\). The roots satisfy \(\rho_1+\rho_2=x(a+b)\) and \(\rho_1\rho_2=xab\). If they are nonreal, they are conjugates with modulus \(\sqrt{xab}\). Thus, for every \(n\ge1\),
\[
\rho_1^n+\rho_2^n\le2(xab)^{n/2}\le2(ab)^{n/2}\le a^n+b^n.
\]
If the roots are real, both are nonnegative. Order them as \(\rho_1\ge\rho_2\). They satisfy \(\rho_1+\rho_2=x(a+b)\le a+b\) and \(\rho_1\le a\): indeed, the root polynomial evaluated at \(a\) is \((1-x)a^2>0\); a hypothetical root greater than \(a\) would force *both* roots to exceed \(a\), contradicting their sum being at most \(a+b\le2a\). The pair \((\rho_1,\rho_2)\) is therefore weakly majorized by \((a,b)\), so applying the increasing convex function \(r\mapsto r^n\) gives \(\rho_1^n+\rho_2^n\le a^n+b^n\) for every integer \(n\ge1\). At \(t=1\), both roots vanish and the same conclusion holds. All root moduli are less than one (the nonreal case has modulus at most \(\sqrt{ab}\)), hence the nonnegative canonical series converges at one. Infinite divisibility follows for all \(0<t\le1\).

**Step 4 (sharp zero-deflation boundary).** For \(t>1\), write \(h=t-1>0\) and \(y=h/d>0\). The root polynomial is \(w^2+y(a+b)w-yab\), so its roots are \(r>0\) and \(-s<0\), with \(s>r\). Since this polynomial is negative at zero and positive at \(b\), \(0<r<b\). The negative root magnitude \(s\) satisfies
\[
s^2-y(a+b)s-yab=0
\]
and increases strictly with \(y\), while \(y=h/[c-h(1-c)]\) increases strictly with \(h\) throughout the allowed range. The crossing \(s=a\) occurs if and only if
\[
y=\frac a{a+2b},\quad
h=\frac{c}{2(1+b/a)-c}=\frac3{(\beta+1)(2\beta+7)}.
\]
For \(1<t\le t_*(\beta)\), we have \(s\le a\) and \(r<b\). Every even-index canonical coefficient has numerator
\[
a^{2m}+b^{2m}-s^{2m}-r^{2m}\ge0,
\]
while every odd-index coefficient has numerator \(a^{2m+1}+b^{2m+1}+s^{2m+1}-r^{2m+1}>0\). All four root moduli are below one, yielding a valid compound-Poisson representation. Exactly at the crossing, the even coefficient numerator reduces to \(b^{2m}-r^{2m}>0\), so equality is included.

If \(t>t_*(\beta)\) but \(d>0\), then \(s>a>b>r\). It follows that for all sufficiently large \(m\),
\[
a^{2m}+b^{2m}-s^{2m}-r^{2m}<0.
\]
Therefore infinitely many canonical intensities are negative and the law cannot be infinitely divisible. Finally, when \(d=0\), any nontrivial nonnegative-integer infinitely divisible law must have positive mass at zero (compound-Poisson characterization); the present law has \(p_1>0\) but \(p_0=0\), excluding it. This completes the entire sharp classification.

## Verification
The standalone \(\texttt{verify.py}\) uses SymPy to verify the rational mixing identity and the exact closed-form threshold. It then separately computes canonical power sums by their two-term recurrence using exact fractions for multiple parent scales, zero inflation, the equality boundary, and parameters beyond the threshold. Those finite checks do not replace the all-index inequalities and asymptotic necessity proved above. In particular, failure may first occur at arbitrarily high even order just beyond the cutoff, so finite checking alone would be inconclusive.

## Relationship to prior work
Eliwa and collaborators (2023) introduced the mixed-Poisson–Bilal count model and studied its generating function, hazard, dispersion, and estimation. Hürlimann (2015, Section 4) already identified the arbitrary two-geometric convolution as a Newton distribution and its ordinary compound-Poisson canonical coefficients. These results are explicitly taken as background and do not give the sharp zero-deflation cutoff for the one-parameter Poisson–Bilal path. Vinogradov (2007) studied a critical *single*-geometric zero-deflation law; it is closely relevant methodologically but addresses a different object. Its full text could not be obtained, so unrecognized broader coverage remains a priority risk. The new statement is the precise all-parameter robustness boundary for zero modifying the **two-geometric Poisson–Bilal law**, including infinite-order negative coefficients beyond the boundary. This does not assert novelty of infinite divisibility for a geometric distribution or its unmodified convolution.

## Limitations
The theorem concerns the specific zero modification \(F_t=1-t+tG\) and the one-dimensional Bilal mixing path; it does not classify arbitrary zero-modified sums of more than two geometrical variables, other count laws, or other notions of thinning self-decomposability. The cutoff characterizes ordinary additive infinite divisibility, not log-concavity or monotone hazard. Available literature comparisons do not certify absolute historical priority. No independent mathematical audit has been performed.

## References
1. M. S. Eliwa, M. Ahsan-ul-Haq, A. Almohaimeed, A. Al-Bossly, M. El-Morshedy, “Discrete Extension of Poisson Distribution for Overdispersed Count Data: Theory and Applications,” *Journal of Mathematics* (2023), article 2779120, published 13 February 2023. https://doi.org/10.1155/2023/2779120.
2. W. Hürlimann, “The Concepts of Pseudo Compound Poisson and Partition Representations in Discrete Probability,” *Journal of Probability and Statistics* (2015), article 189596; especially Sections 1, 2, and 4. https://doi.org/10.1155/2015/189596.
3. V. Vinogradov, “On Structural and Asymptotic Properties of Some Classes of Distributions,” *Acta Applicandae Mathematicae* **97** (2007), 335–351. https://doi.org/10.1007/s10440-007-9117-y.
4. W. Feller, *An Introduction to Probability Theory and Its Applications*, vol. 1, 3rd ed., Wiley (1968), Chapter XII.2 (the discrete infinite-divisibility/compound-Poisson criterion).
