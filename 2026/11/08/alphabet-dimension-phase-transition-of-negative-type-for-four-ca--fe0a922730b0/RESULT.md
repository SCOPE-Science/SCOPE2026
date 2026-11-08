# Alphabet–dimension phase transition of negative type for four-capped Hamming metrics

## Finding
Fix integers \(n\ge5\) and \(q\ge3\). On \(G=(\mathbb Z/q\mathbb Z)^n\), let \(w(x)\) be the number of nonzero coordinates and define the metric
\[
 d_{n,q}(x,y)=\min\{w(x-y),4\}.
\]
Let \(\beta_{n,q}\) be the supremum of \(p>0\) for which \(d_{n,q}^p\) is conditionally negative definite. Put \(L=\log(4/3)\). The following three asymptotic laws hold, with the stated order of limits.

**Fixed alphabet.** For each fixed integer \(q\ge3\),
\[
 \boxed{\lim_{n\to\infty} n^3\beta_{n,q}=\frac{6}{L}.}
\]

**Alphabet proportional to dimension.** For every integer sequence \(q_n\ge3\) with \(q_n/n\to c\in(0,\infty)\), define the degree-three discrete Charlier-limit polynomial
\[
 P_c(s)=-\frac16+\frac{cs}{2}-\frac{c^2s(s-1)}2+\frac{c^3s(s-1)(s-2)}6,\qquad s=0,1,2,\ldots,
\]
with \(\mu(c)=-\min_{s\in\mathbb Z_{\ge0}}P_c(s)>0\). Then
\[
 \boxed{\lim_{n\to\infty}n^3\beta_{n,q_n}=\frac{1}{L\mu(c)}.}
\]
There is a sharp transition at the alphabet-to-dimension ratio \(c=1/2\): \(\mu(c)=1/6\) for every \(0<c\le1/2\), whereas \(\mu(c)>1/6\) for every \(c>1/2\). For \(0<c<1/2\), the unique minimizing codimension is \(s=0\), and this asymptotic localization strengthens to **exact finite-dimensional stabilization**: for every sequence \(q_n/n\to c\in(0,1/2)\), the sole null layer at \(p=\beta_{n,q_n}\) is eventually \(k=n\), of dimension \((q_n-1)^n\). Moreover, the critical exponent is then exactly the alphabet-independent root \(b_n\sim6/(Ln^3)\) of
\[
 -4^{b_n}+n(4^{b_n}-1)+\binom n2(2^{b_n}-4^{b_n})+\binom n3(4^{b_n}-3^{b_n})=0.
\]
Here \(b_n\) means the unique root in a fixed sufficiently small multiple-of-\(n^{-3}\) window around \(6/(Ln^3)\), as established below; no global uniqueness for the scalar equation is asserted. At \(c=1/2\), the limiting minimizing codimensions are exactly \(\{0,4,5\}\). For every \(c>1/2\), the full-weight layer \(k=n\) is eventually *not* critical. For any \(c>0\), if a nonconstant Fourier mode is null at \(p=\beta_{n,q_n}\), every subsequential limit of its codimension \(s=n-k\), where \(k\) is the number of nontrivial character coordinates, lies in the finite set \(\operatorname*{argmin}_{s\ge0}P_c(s)\). For instance, the unique limiting critical codimension is \(3\) when \(c=1\) and \(2\) when \(c=2\).

**Fixed dimension, growing alphabet.** For every fixed \(n\ge5\),
\[
 \boxed{\lim_{q\to\infty}q^2\beta_{n,q}=\frac{1}{(n-2)L-\log2}.}
\]
For all sufficiently large integer \(q\) at each fixed \(n\), the only critical Fourier layer is \(k=n-2\); its multiplicity is \(\binom n2(q-1)^{n-2}\). The constant in the denominator is strictly positive because \(n\ge5\). At \(n=4\) the cap does nothing, so \(\beta_{4,q}=1\) for all \(q\); the large-alphabet collapse begins sharply at dimension five.

These statements concern conditional negative definiteness of powered **distances**, equivalently the property that every Gaussian kernel \(\exp(-t d_{n,q}^p)\) is positive definite for every \(t>0\). They do not assert a closed finite-parameter formula for \(\beta_{n,q}\) at arbitrary \((n,q)\).

## Assumptions and scope
The alphabet \(\mathbb Z/q\mathbb Z\) need not be a field and may have composite order. The metric is the minimum of ordinary Hamming distance with four, not a distance in a graph power. For a translation-invariant real symmetric kernel on a finite abelian group, conditional negative definiteness is equivalent to nonpositivity of every nontrivial Fourier eigenvalue. The nontrivial characters split into layers according to the number \(k\in\{1,\ldots,n\}\) of nonzero frequency coordinates, with multiplicity \(\binom nk(q-1)^k\).

For integers \(0\le j\le3\), use the q-ary Krawtchouk numbers
\[
 K_j(k;n,q)=[z^j](1+(q-1)z)^{n-k}(1-z)^k.
\]
Their normalization is not probability-normalized: \(K_0=1\). The exact Fourier eigenvalue of the powered distance for every nontrivial layer \(k\) is
\[
 \lambda_k(p)=-4^p+(1-4^p)K_1(k)+(2^p-4^p)K_2(k)+(3^p-4^p)K_3(k).
\]
Thus \(\beta_{n,q}=\sup\{p>0:\lambda_k(p)\le0\text{ for every }1\le k\le n\}\). In all three limiting regimes proved here, this supremum is finite and positive for sufficiently large parameters; the endpoint belongs to the negative-type interval.

## Proof
**1. Fourier criterion.** The spherical Fourier sum on the shell of Hamming weight \(j\) is \(K_j(k;n,q)\), by multiplying the one-coordinate character sums \(q-1\) and \(-1\). For a nontrivial character \(k\ge1\), summing the generating polynomial at \(z=1\) shows \(\sum_{j=0}^{n}K_j(k)=0\). The diagonal contributes zero for \(p>0\); therefore the shell coefficients \(1^p,2^p,3^p,4^p\) produce the displayed exact \(\lambda_k(p)\). At \(p=0\), interpreting all nonzero distances to the zeroth power as one, \(\lambda_k(0)=-1\). The classical negative-type interval property allows the threshold to be bounded by testing a single larger exponent and a single smaller exponent.

**2. Proportional alphabet: finite critical codimensions.** Write \(s=n-k\) and \(Q=q-1\). The exact coefficient formulas are
\[
 \begin{aligned}
 K_1&=sQ-(n-s),\\
 K_2&=\binom s2Q^2-s(n-s)Q+\binom{n-s}2,\\
 K_3&=\binom s3Q^3-\binom s2(n-s)Q^2+s\binom{n-s}2Q-\binom{n-s}3.
 \end{aligned}
\]
If \(q_n/n\to c>0\), choose any constant \(a\in(0,c)\). For all sufficiently large \(n\), \(Q\ge an\). For every integer \(s\) larger than a constant \(S(a)\), these three coefficients are nonnegative simultaneously, *uniformly over* \(s\le n\). Indeed,
\[
 K_1\ge n(as-1),\qquad
 K_2\ge sQn\bigl(a(s-1)/2-1\bigr),
\]
and
\[
 K_3\ge nQ^2\binom s2\bigl(a(s-2)/3-1\bigr)-n^3/6.
\]
Choosing \(S(a)\) large makes all right-hand sides nonnegative. Since each coefficient \(j^p-4^p\) is strictly negative for \(1\le j\le3\) and \(p>0\), all such layers have \(\lambda_k(p)<0\) at *every* positive exponent. Hence only the fixed finite set \(0\le s<S(a)\) can obstruct negative type.

For each fixed \(s\), direct comparison of coefficients gives
\[
 \frac{K_3(n-s;n,q_n)}{n^3}\longrightarrow P_c(s),\qquad K_2/n^3\to0,\quad K_1/n^3\to0.
\]
Therefore, for each fixed \(t\ge0\), uniformly across that finite candidate set,
\[
 \lambda_{n-s}(t/n^3)\longrightarrow -1-tL P_c(s).
\]
The cubic \(P_c(s)\) tends to positive infinity as \(s\to\infty\), and \(P_c(0)=-1/6\). Consequently \(\mu(c)\) is finite and positive. For \(t<1/(L\mu(c))\), every nontrivial eigenvalue is eventually negative. For \(t>1/(L\mu(c))\), a minimizing codimension has an eventually positive eigenvalue. The negative-type interval property gives the claimed limit. The same uniform finite-set argument forces the limiting codimensions of all critical zero eigenvalues into the minimizer set of \(P_c\).

**3. Sharp threshold at the half ratio.** For every integer \(s\ge1\), factor
\[
 P_c(s)+1/6=\frac{cs}{2}\left(1-c(s-1)+\frac{c^2}{3}(s-1)(s-2)\right).
\]
For \(s\ge5\), the discriminant of the parenthesized quadratic in \(c\) is \((s-1)(5-s)/3\le0\), so this expression is nonnegative for every \(c>0\). For \(s=1,2,3,4\), elementary substitution shows nonnegativity whenever \(0<c\le1/2\); for \(s=4\), the quadratic factors as \((1-c)(1-2c)\). For \(0<c<1/2\) all these inequalities are strict; at \(c=1/2\) equality holds precisely for \(s=4,5\), in addition to \(s=0\). If \(1/2<c<1\), then \(P_c(4)+1/6=2c(1-c)(1-2c)<0\). If \(c>1\), then \(P_c(2)+1/6=c(1-c)<0\). At \(c=1\), \(P_1(3)=-2/3<-1/6\). This proves both sides of the sharp transition and the stated equality cases. At \(c=1\), the first difference is \(P_1(s+1)-P_1(s)=(s^2-3s+1)/2\), which identifies \(s=3\) as the unique global minimizer. At \(c=2\), the first difference is \(4(s-1)^2-3\), yielding the unique minimizer \(s=2\).

For the exact stabilization when \(0<c<1/2\), write \(\lambda_n(p)\) for the full-weight eigenvalue. Since \(K_j(n;n,q)=(-1)^j\binom nj\), this eigenvalue is independent of \(q\). Its derivative is \(Ln^3/6+O(n^2)\), uniformly on a bounded multiple-of-\(n^{-3}\) interval. Together with \(\lambda_n(t/n^3)\to-1+tL/6\), this produces the unique nearby root \(b_n\sim6/(Ln^3)\). For each fixed \(s\ge1\), the strict gap \(P_c(s)>P_c(0)\) implies \(\lambda_{n-s}(b_n)\to -1-(6/L)L P_c(s)<0\), while all sufficiently large codimensions are negative by Step 2. Thus at \(b_n\) only the full-weight layer is null. It is the actual negative-type endpoint, because the full-weight eigenvalue crosses zero upward and negative-type exponents form an interval. For \(c>1/2\), the limiting endpoint \(1/(L\mu(c))\) is strictly below \(6/L\), so the full-weight eigenvalue stays strictly negative at the endpoint. This proves the stated sharp change of the critical Fourier layer.

**4. Fixed alphabet.** If \(q\) is fixed while \(n\to\infty\), write \(k/n=\theta\). Uniformly for all \(0\le k\le n\),
\[
 \frac{K_3(k;n,q)}{n^3}=\frac{((q-1)-q\theta)^3}{6}+O_q(1/n),
\]
and \(K_2=O_q(n^2)\), \(K_1=O_q(n)\). Since the quantity \((q-1)-q\theta\) ranges over \([-1,q-1]\), its cubic has minimum \(-1\), attained at \(\theta=1\). For \(p=t/n^3\), the maximal nontrivial eigenvalue tends to \(-1+tL/6\), uniformly over frequency layers. Testing on either side of the unique limiting zero yields \(n^3\beta_{n,q}\to6/L\). This specialization includes the known Boolean case \(q=2\), which is not claimed as a new contribution.

**5. Fixed dimension and large alphabet.** Fix \(n\ge5\) and let \(q\to\infty\), again writing \(s=n-k\). For \(s\ge3\), \(K_3=\binom s3q^3+O_n(q^2)>0\); for \(s=0,1\), \(K_1,K_2,K_3=O_n(q)\). For the distinguished layer \(s=2\),
\[
 K_2=q^2+O_n(q),\qquad K_3=-(n-2)q^2+O_n(q).
\]
Putting \(p=t/q^2\) in the exact Fourier formula gives
\[
 \lambda_{n-2}(t/q^2)\longrightarrow -1+t\big((n-2)L-\log2\big).
\]
Every layer \(s=0,1\) tends to \(-1\), and every layer \(s\ge3\) tends to \(-\infty\) for fixed \(t>0\). The positive factor \((n-2)L-\log2\) exceeds \(3\log(4/3)-\log2=\log(32/27)>0\). Consequently, a positive/negative sandwich around the unique limiting root and the interval property give the large-alphabet formula. Uniformly near that root, the \(s=2\) Fourier eigenvalue is the only one capable of vanishing. Continuity at the actual finite threshold shows that for all sufficiently large \(q\), the only null Fourier layer is \(k=n-2\); its multiplicity is \(\binom n2(q-1)^{n-2}\). When \(n=4\), no pair has Hamming distance exceeding the cap; the ordinary Hamming metric has supremal negative type exponent one, proving the boundary statement.

## Verification
Run `python check.py` using Python 3 and its standard library. The script independently enumerates every input group element for four small nonprime/prime alphabet-and-dimension combinations and tests the character Fourier eigenvalues at three exponents. It separately checks the cubic minimizer transition, fifteen proportional-alphabet threshold approximations, six fixed-dimension large-alphabet cases, and nine fixed-alphabet growth cases. The direct enumeration is logically independent of the Krawtchouk formula. Successful execution prints `CAPPED_HAMMING_CHARLIER_CHECKS_PASS`. Floating numerical approximations are consistency checks, not proofs of the infinite asymptotics or uniqueness of critical layers.

## Relationship to prior work
The finite-metric negative-type interval property and a general threshold-computation framework are classical; see Sánchez (2011). The Hamming eigenmatrix is a q-ary Krawtchouk table; Brouwer, Cioabă, Ihringer and McGinnis (2017) analyze smallest eigenvalues of individual Hamming-distance graphs and, for fixed dimension with large alphabet, prove the characteristic codimension of a minimum degree-three eigenvalue. Dominici (2005) studies the classical Krawtchouk-to-Charlier limit, which motivates the proportional-alphabet scaling. These antecedents give essential polynomial ingredients but do not, in the inspected statements, determine the powered **four-capped metric**'s threshold or the half-ratio phase transition, which involve a specific logarithmic combination of degree-one through degree-three eigenvalues.

Other q-ary Hamming-harmonic results on degree-two projection endpoint norms and radius-two positive-definite Turán mass concern different operators and optimizations: their constants and equality criteria do not determine conditional negative type of this powered capped metric. The binary four-cap asymptotic is recovered on fixing \(q=2\), and the nonbinary three-cap case has distinct cap and scaling laws. This result neither replaces nor claims novelty for those known or previously recorded cases.

## Limitations
The result gives asymptotic threshold laws, not exact finite-parameter roots for every \((n,q)\). At ratios where the cubic has multiple minimizers (notably \(c=1/2\)), it localizes possible critical Fourier layers but does not determine which tie wins at a particular finite dimension. Although the checker reproduces selected limits, finite experiments alone do not establish them; the proof supplies uniform exclusion of large codimensions. The complete historical literature may contain equivalent implicit metric-transform consequences, so the bounded comparison is not an independent originality certification. No independent mathematical audit has been performed.

## References
1. D. Dominici, *Asymptotic analysis of the Askey-scheme I: from Krawtchouk to Charlier*, arXiv:math/0501072v1, first posted 2005-01-05, https://arxiv.org/abs/math/0501072, Introduction and Section 3.
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, first posted 2011-08-02, https://arxiv.org/abs/1108.0451, Sections 1–2.
3. A. E. Brouwer, S. M. Cioabă, F. Ihringer and M. McGinnis, *The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters*, arXiv:1709.09011v1, first posted 2017-09-26, https://arxiv.org/abs/1709.09011, Sections 1.1, 2.1 and 2.3.
