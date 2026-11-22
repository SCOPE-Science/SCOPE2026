# A sharp flip and Gaussian-tail resilience law for a probit-feedback interval map

## Finding

Let \(\Phi\) and \(\varphi\) be the standard normal cumulative distribution function and density. For each real \(a>0\), define a smooth map of the open unit interval by
\[
 F_a(x)=\Phi\!\left(\Phi^{-1}(x)-a(x-\tfrac12)\right),\qquad 0<x<1.
\]
Write \(a_c=2\sqrt{2\pi}\). The following classification holds.

1. When \(0<a\le a_c\), every orbit in \((0,1)\) converges to the unique fixed point \(1/2\). At the critical gain \(a=a_c\), for every initial point not in the complete backward orbit of \(1/2\),
\[
 \lim_{n\to\infty}n\left(\Phi^{-1}(x_n)\right)^2=\frac32,
 \qquad \lim_{n\to\infty}n(x_n-\tfrac12)^2=\frac3{4\pi}.
\]
The excluded initial points instead reach \(1/2\) in finitely many iterates.

2. When \(a>a_c\), exactly one primitive period-two orbit exists in \((0,1)\). It is the pair \(\Phi(-u_a),\Phi(u_a)\), where \(u_a>0\) is the unique positive solution of
\[
 a\left(\Phi(u_a)-\tfrac12\right)=2u_a.
\]
It attracts a neighborhood of each point for every finite \(a>a_c\). Its two-step multiplier is
\[
 M(a)=\left(1-a\varphi(u_a)\right)^2\in[0,1).
\]

3. There is exactly one superattracting gain \(a_s>a_c\). If \(u_s\) is the unique positive root of
\[
 \Phi(u_s)-\tfrac12=2u_s\varphi(u_s),
\]
then \(a_s=1/\varphi(u_s)\), numerically \(u_s=1.3999852768782042\ldots\), \(a_s=6.678663688751935\ldots\). The multiplier decreases strictly from one to zero as \(a\) increases from \(a_c\) to \(a_s\), and then increases strictly toward one.

4. The two-cycle is born on the exact square-root scale
\[
 u_a^2\sim\frac{6(a-a_c)}{a_c}\quad(a\downarrow a_c).
\]
For \(a\to\infty\), its endpoint location and its almost-neutral attraction have the sharp laws
\[
 u_a=\frac a4-2\varphi(a/4)(1+o(1)),
\]
\[
 \Phi(-u_a)\sim\frac4{a\sqrt{2\pi}}e^{-a^2/32},
 \qquad 1-M(a)\sim\sqrt{\frac2\pi}\,a e^{-a^2/32}.
\]
The last two expressions quantify a Gaussian-in-gain, rather than exponential-in-gain, approach to the boundary and to neutral two-cycle stability.

## Assumptions and scope

The gain \(a\) is an arbitrary finite positive real number; the state space is the entire open interval \((0,1)\). The map is never extended by assigning a finite Gaussian quantile at the endpoints. The standard normal distribution is normalized by \(\varphi(z)=(2\pi)^{-1/2}e^{-z^2/2}\). A primitive two-cycle means an unordered pair of distinct interior points interchanged by one iterate. Local attraction refers to the two-step return map near either cycle point, not to a claim about every orbit for supercritical gains. The backwards orbit of \(1/2\) means \(\bigcup_{k\ge0}F_{a_c}^{-k}(\{1/2\})\).

This map is a decreasing-quantile specialization of the general shift construction \(f=h^{-1}(h(x)+a(x-b))\), with \(h=-\Phi^{-1}\) and \(b=1/2\), from Kryzhevich and Zhang (2026). That general construction, including its telescoping periodic-orbit mean, is prior work and is not claimed as new. The specific all-gain dynamics and sharp Gaussian-tail rates above are the assessed contribution.

## Proof

**Conjugacy.** Let \(z=\Phi^{-1}(x)\) and \(g(z)=\Phi(z)-1/2=\int_0^z\varphi(t)\,dt\). The conjugate map is exactly
\[
 G_a(z)=z-ag(z).
\]
The function \(g\) is odd, is strictly increasing on \(\mathbb R\), and for \(z>0\) its quotient satisfies
\[
 q(z)=\frac{g(z)}z=\int_0^1\varphi(sz)\,ds.
\]
Consequently \(q\) decreases strictly from \(\varphi(0)\) to zero on \((0,\infty)\). It is also true that \(g(z)>z\varphi(z)\) for every \(z>0\), since the density decreases strictly on positive arguments.

**Fixed point and its global critical basin.** The identity \(G_a(z)=z\) gives \(z=0\) as the only fixed point. For every nonzero \(z\), the signed quotient \(ag(z)/z\) lies strictly between zero and \(a\varphi(0)\). When \(a\le a_c=2/\varphi(0)\), this gives \(\lvert G_a(z)\rvert<\lvert z\rvert\). Therefore the absolute values along each orbit decrease strictly. If their limit were positive, continuity and compactness of the visited amplitude range would force a uniform positive decrease; this is impossible. Thus \(z_n\to0\), equivalently \(x_n\to1/2\).

At \(a=a_c\), the Taylor expansion around zero gives
\[
 G_{a_c}(z)=-z+\frac{z^3}{3}+O(z^5).
\]
For each orbit that never equals zero, set \(v_n=z_n^2>0\). Then
\[
 v_{n+1}=v_n-\frac23v_n^2+O(v_n^3),
\quad
\frac1{v_{n+1}}-\frac1{v_n}=\frac23+O(v_n)\to\frac23.
\]
Telescoping and Cesàro averaging yield \(1/(nv_n)\to2/3\), so \(nv_n\to3/2\). Since \(\Phi(z)=1/2+\varphi(0)z+O(z^3)\), the state-coordinate coefficient is \((3/2)\varphi(0)^2=3/(4\pi)\). A finite-time hit of zero is the only exception, and then all subsequent iterates remain zero. Such exceptional nonzero points do exist, because for \(a=a_c\), \(G_a(z)\) changes sign on the positive half-line.

**Two-cycle exhaustion.** If distinct real \(z,w\) satisfy \(G_a(z)=w\) and \(G_a(w)=z\), adding the displacement identities gives \(g(z)+g(w)=0\); strict monotonicity and oddness of \(g\) force \(w=-z\). With \(u=|z|>0\), the orbit equation is exactly \(a q(u)=2\). Since \(q\) is strictly decreasing, this has exactly one positive solution precisely when \(a\varphi(0)>2\), or \(a>a_c\). Hence the primitive period-two orbit is globally unique as a periodic *pair*, with no assumption of local or global attraction needed for uniqueness.

**Local multiplier and uniquely optimal gain.** Differentiation yields \(G_a'(z)=1-a\varphi(z)\). At both members of the pair the derivative is the same. The period-two equation and \(g(u)>u\varphi(u)\) imply
\[
 0<a\varphi(u_a)=\frac{2u_a\varphi(u_a)}{g(u_a)}<2.
\]
Therefore \(M(a)=(1-a\varphi(u_a))^2<1\), establishing local attraction and excluding a subsequent flip of this pair for every finite gain.

Define \(r(u)=u\varphi(u)/g(u)\). An exact integral representation is
\[
 \frac1{r(u)}=\frac{g(u)}{u\varphi(u)}
 =\int_0^1\exp\!\left(\frac{u^2}{2}(1-s^2)\right)ds.
\]
This quantity increases strictly from one to infinity as \(u\) increases from zero to infinity, so \(2r(u)=a\varphi(u)\) decreases strictly from two to zero along the two-cycle branch. It passes one exactly once, proving the existence and uniqueness of the superattracting gain and strict monotonicity of the multiplier on the two sides. Equivalently the crossing is the unique positive solution of \(H(u)=g(u)-2u\varphi(u)=0\). Indeed \(H(0)=0\), \(H'(u)=(2u^2-1)\varphi(u)\), and \(H(u)\to1/2\). This also uniquely defines the reported numerical constant and shows \(u_s>1/\sqrt2\).

**Birth and large-gain laws.** Gaussian Taylor expansion gives
\[
 q(u)=\varphi(0)\left(1-\frac{u^2}{6}+O(u^4)\right).
\]
Combining \(a q(u_a)=2\) with \(a_c\varphi(0)=2\) proves \(u_a^2=6(a-a_c)/a_c+O((a-a_c)^2)\).

For large gain let \(Q(u)=1-\Phi(u)\). The same orbit equation can be rearranged **exactly** as
\[
 u_a=\frac a4-\frac a2Q(u_a).
\]
Since \(g(u_a)/u_a=2/a\to0\), strict monotonicity of \(q\) implies \(u_a\to\infty\). Since \(Q(u_a)\to0\), the exact identity then gives \(u_a/a\to1/4\). The Gaussian Mills asymptotic \(Q(u)=\varphi(u)u^{-1}(1+O(u^{-2}))\) implies \(aQ(u_a)/2=O(\varphi(u_a))\) and thus \(u_a=a/4+O(\varphi(u_a))\). This makes \((a/4)^2-u_a^2=o(1)\), so \(\varphi(u_a)/\varphi(a/4)\to1\). Substitute Mills' relation once more to get the stated sharpened displacement \(a/4-u_a\sim2\varphi(a/4)\), the lower endpoint \(\Phi(-u_a)=Q(u_a)\sim4\varphi(a/4)/a\), and
\[
 1-M(a)=2a\varphi(u_a)-a^2\varphi(u_a)^2
 \sim 2a\varphi(a/4)=\sqrt{\frac2\pi}\,a e^{-a^2/32}.
\]
Every asymptotic is along the unique positive branch; no finite numerical enumeration is used as proof.

## Verification

A standalone standard-library checker, \(\texttt{check_probit.py}\), evaluates the defining root and derivative identities by bracketing, checks the unique superattracting root, tests exact return identities at several gains, and numerically compares the critical and large-gain asymptotic constants. Its finite computations corroborate but do not replace the arguments above. The full proof uses the monotone Gaussian quotient, strict integral inequalities, Taylor expansions and Mills' asymptotic, and is valid at all stated real parameters.

## Relationship to prior work

Kryzhevich and Zhang (2026), Proposition 4.2 and Remark 4.3, give the general quantile-shift construction and explicitly mention normal quantiles, but their later theorems concern the *logit* replicator map and not the present anti-quantile probit feedback's exact period-two gain diagram. They already establish the periodic-mean property, which the present theorem does not reclaim. The 2024 full-text study by Kryzhevich, Zhang and Chmara establishes global two-cycle attraction in the **logit** symmetric replicator and an exponential-in-gain endpoint law. A change of distribution is not a formal conjugacy preserving the gain or its Floquet multiplier: in probit coordinates the force is the Gaussian CDF, not the logistic sigmoid. Our gain threshold, unique superstable gain, critical amplitude, and Gaussian-in-gain asymptotics therefore do not follow merely by substituting symbols into their statements. Searches of related dynamical literature and available mathematical research records did not identify an exact, dominating probit result; this is an evidence-bounded priority assessment, not a proof of worldwide uniqueness.

## Limitations

The global convergence assertion is confined to gains at or below \(a_c\). For larger gains this result proves uniqueness and local attraction of the primitive two-cycle but does **not** classify other possible recurrent or attracting sets, nor the global basin of the two-cycle. The critical \(n^{-1/2}\) law explicitly excludes initial points whose orbit hits the fixed point in finite time. The endpoint asymptotics concern the open interval and do not assign finite values to \(\Phi^{-1}(0)\) or \(\Phi^{-1}(1)\). An independent audit has not been performed; historically obscure equivalent results may exist.

## References

1. S. Kryzhevich and Y. Zhang, *Shift maps and statistical invariants for some dynamical systems*, arXiv:2603.20685, first publicly posted March 21, 2026. https://arxiv.org/abs/2603.20685 . Relevant parts: Section 4 Proposition 4.2 and Remark 4.3; Section 5 onward treats the logit map.
2. S. Kryzhevich, Y. Zhang and M. Chmara, *Bifurcations and invariant sets for a family of replicator maps from evolutionary games*, arXiv:2412.16379, first publicly posted December 20, 2024. https://arxiv.org/abs/2412.16379 . Relevant parts: Section 3.1, symmetry and period-two asymptotics in the distinct logit family.
3. NIST Digital Library of Mathematical Functions, Chapter 7, *Error Functions, Dawson's and Fresnel Integrals*, Gaussian-tail/error-function asymptotics. https://dlmf.nist.gov/7.12
