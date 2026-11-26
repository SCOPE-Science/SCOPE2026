# All positive moments of regular-overpartition excludants

## Finding and scope

Fix an integer \(\ell\ge2\). An \(\ell\)-regular overpartition of \(n\) uses only positive sizes not divisible by \(\ell\); each admissible size has unrestricted nonoverlined multiplicity and may also occur once overlined. Under the uniform measure on these overpartitions, let \(M_{\ell,n}\) be the least admissible size with **zero nonoverlined multiplicity**. Write \(\bar p_\ell(n)\) for the number of these overpartitions, extended by zero to negative integers, and set
\[
\rho=1-\frac1\ell,\qquad \mu=\frac{\pi^2\rho}4,\qquad a=\frac{\pi\rho^{3/2}}4.
\]
The result is convergence of **every fixed positive real moment** at the known Rayleigh scale:
\[
n^{-s/4}\mathbb E M_{\ell,n}^s\longrightarrow \Gamma(1+s/2)a^{-s/2}.
\]
Consequently \(\mathbb E M_{\ell,n}\sim\rho^{-3/4}n^{1/4}\), and
\(\operatorname{Var}(M_{\ell,n})\sim(4/\pi-1)\rho^{-3/2}n^{1/2}\). In particular, the aggregate first moment is
\[
\sum_{\pi\in\overline{\mathcal P}_\ell(n)}M(\pi)\sim
\frac{e^{\pi\sqrt{\rho n}}}{2\sqrt{2(\ell-1)n}}.
\]
The survivor \(\Pr(M_{\ell,n}>xn^{1/4})\to e^{-ax^2}\) for fixed \(x\ge0\) is already the marginal of the joint law in [4, Eq. (1)]; it is recalled below for context. No result here assumes or asserts uniformity for growing \(\ell,x,s\), a local limit, or a convergence rate.

## Proof

**Exact survivor (cf. [4, Eq. (3)] on the diagonal).** For integers \(t,n\ge0\), put \(u=\lfloor t/\ell\rfloor\) and
\[
 S_\ell(t)=\frac{t(t+1)}2-\frac{\ell u(u+1)}2.
\]
The event \(M_{\ell,n}>t\) is equivalent to having at least one nonoverlined copy of each admissible size up to \(t\). Removing one such copy of each (and leaving overlines untouched) is a bijection onto the regular overpartitions of \(n-S_\ell(t)\). In particular,
\[
\Pr(M_{\ell,n}>t)=\frac{\bar p_\ell(n-S_\ell(t))}{\bar p_\ell(n)}.
\]
The empty overpartition has excludant 1.

**Counting series and its sector estimate.** Write \(E_b(z)=(e^{-bz};e^{-bz})_\infty\) for \(b>0\), \(\Re z>0\), and \(\bar P_\ell(q)=\sum_{n\ge0}\bar p_\ell(n)q^n\). The local factor \((1+q^j)/(1-q^j)\) at an admissible size gives
\[
\bar P_\ell(e^{-z})=\frac{E_2(z)E_\ell(z)^2}{E_1(z)^2 E_{2\ell}(z)}.
\]
The Dedekind eta transformation, with the principal square root, gives
\[
 E_b(z)=\sqrt{\frac{2\pi}{bz}}\exp\!\left(-\frac{\pi^2}{6bz}+\frac{bz}{24}\right)
 \bigl(e^{-4\pi^2/(bz)};e^{-4\pi^2/(bz)}\bigr)_\infty.
\]
In each fixed sector \(|\Im z|\le\Delta\Re z\), one has \(\Re(1/z)\ge(1+\Delta^2)^{-1/2}/|z|\). The last product is therefore \(1+O_{b,\Delta}(e^{-c_{b,\Delta}/|z|})\) for a positive constant \(c_{b,\Delta}\). Taking the ratio yields
\[
 \bar P_\ell(e^{-z})=\ell^{-1/2}\exp(\mu/z)
 \left(1+O_{\ell,\Delta}(e^{-c_{\ell,\Delta}/|z|})\right).
\]
In particular the real-axis equivalent holds, as does \(|\bar P_\ell(e^{-z})|\ll_{\ell,\Delta}e^{\mu/|z|}\) in every such sector. The coefficients are nonnegative and nondecreasing (adjoin one nonoverlined 1) and the series is analytic for \(|q|<1\). The coefficient form of Ingham's theorem [3, Theorem 1.1] now gives
\[
\bar p_\ell(n)\sim \frac{\mu^{1/4}}{2\sqrt{\pi\ell}}n^{-3/4}e^{2\sqrt{\mu n}}.\tag{1}
\]
For integer \(D_n=O(\sqrt n)\) with \(D_n/\sqrt n\to d\ge0\), (1) implies \(\bar p_\ell(n-D_n)/\bar p_\ell(n)\to e^{-\sqrt\mu\,d}\) by expanding the difference of square roots. Taking \(t=\lfloor xn^{1/4}\rfloor\) gives \(S_\ell(t)/\sqrt n\to\rho x^2/2\). Since \(\rho\sqrt\mu/2=a\), this proves the stated survivor, including \(x=0\).

**All positive moments.** Enumerate admissible sizes as \(b_1=1<b_2<\cdots\), put \(T_j=S_\ell(b_j)\), and let \(\Delta_j=b_{j+1}^s-b_j^s\). Telescoping \(M^s=1+\sum_{j\ge1}\Delta_j\mathbf1_{\{M>b_j\}}\) gives the exact generating function
\[
F_s(q):=\sum_{n\ge0}\sum_{\pi\in\overline{\mathcal P}_\ell(n)}M(\pi)^s q^n
=\bar P_\ell(q)H_s(q),\qquad H_s(q)=1+\sum_{j\ge1}\Delta_j q^{T_j}.
\]
For real \(t\downarrow0\), the nonnegative sum \(t^{s/2}(H_s(e^{-t})-1)\) is an integral sum against \(d(y^s)\) over consecutive intervals \([y_j,y_{j+1}]\), \(y_j=\sqrt t\,b_j\), with the integrand set to \(e^{-t T_j}\) on each interval. Because \(T_j=\rho b_j^2/2+O_\ell(b_j)\) and \(b_{j+1}-b_j\le2\), this integrand tends uniformly on bounded intervals above \(y_1\) to \(e^{-\rho y^2/2}\). The missing mass of \([0,y_1]\) is at most \(y_1^s\). Also \(T_j\ge c_\ell b_j^2\) for all sufficiently large \(j\), and \(y\le 2y_j\) on their intervals. Hence the tail is bounded by the integral of \(e^{-c_\ell y^2/4}\) against \(d(y^s)\), whose far tail tends to zero. This proves
\[
 H_s(e^{-t})\sim t^{-s/2}\int_0^\infty e^{-\rho y^2/2}\,d(y^s)
 = t^{-s/2}\Gamma(1+s/2)(2/\rho)^{s/2}.
\]
Nonnegative coefficients give \(|H_s(e^{-z})|\le H_s(e^{-\Re z})\ll_{\ell,s,\Delta}|z|^{-s/2}\) in the same fixed sectors. Thus the product \(F_s(e^{-z})\) has the required bound \(\ll_{\ell,s,\Delta}|z|^{-s/2}e^{\mu/|z|}\), in addition to its real-axis equivalent obtained by multiplying the equivalents above. The \(F_s\) coefficients are nonnegative and nondecreasing: adjoining a nonoverlined 1 cannot decrease the excludant and is injective. Both factors converge for \(|q|<1\). Ingham's coefficient theorem, now with real-axis power \(-s/2\), yields
\[
 [q^n]F_s\sim\frac{\Gamma(1+s/2)(2/\rho)^{s/2}}{2\sqrt{\pi\ell}}
 \mu^{(1-s)/4}n^{(s-3)/4}e^{2\sqrt{\mu n}}.
\]
Dividing by (1) proves the moment theorem. At \(s=1\) the aggregate coefficient simplifies to \(1/(2\sqrt{2(\ell-1)})\); at \(s=1,2\) the two normalized moments give the stated mean and variance.

## Verification and relation to prior work

`verify_mex.py` compares exact counts and first two moments with brute force for weights 0 through 15 at \(2\le\ell\le8\), checks monotonicity through weight 500, and compares scaled moments with the limits at weights 200 and 500. These are finite diagnostics, not the proof of the asymptotics.

Bhowmick and Meher [1] define this same nonoverlined excludant, derive its first-moment series (Theorem 1.3 and Eq. (3.21)) and give the aggregate asymptotics at \(\ell=2,3\) (Theorems 1.5–1.6). The statistic, first-moment series and those two cases are not new. Wagner's general least-gap theorem [2, Theorem 3] permits independent colors with unrestricted multiplicity. It does not describe an independent Bernoulli overline at each admissible size that is ignored by the statistic. Simply forgetting marks does not yield the uniform ordinary-partition measure. For the exact same marked model, [4] already gives the fixed-weight tail and its Rayleigh limit as diagonal specializations of its joint formulas; its moment bounds in Eq. (10) concern the Boltzmann measure, not every fixed positive real moment at fixed weight. Although the exact tail and eta-quotient estimates can also be used to control large excludants, fixed-threshold convergence alone does not justify moment convergence. The contribution here is the fixed-weight positive-real-moment theorem, including the first-moment asymptotic for every fixed \(\ell\ge4\), proved by a weighted coefficient argument. Historical priority beyond the examined sources is not asserted.

## References

1. S. Bhowmick and N. K. Meher, *The minimal excludant of \(\ell\)-regular overpartitions*, arXiv:2611.18129v1, https://arxiv.org/html/2611.18129v1.
2. S. Wagner, *Limit distributions of smallest gap and largest repeated part in integer partitions*, Ramanujan J. 25 (2011), 229–246, https://www.finanz.math.tugraz.at/~wagner/limitdist.pdf.
3. K. Bringmann, C. Jennings-Shaffer and K. Mahlburg, *On a Tauberian theorem of Ingham and Euler–Maclaurin summation*, Ramanujan J. 61 (2023), 55–86, Theorem 1.1 and its first two remarks, https://arxiv.org/abs/1910.03036.
4. *Joint support and nonoverlined gaps in regular overpartitions: a diagonal law and sharp coincidence bias*, 2026-11-22, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-joint-support-and-nonoverlined-gaps-in-regular-overpartitions-a--96650212350f/RESULT.md, Eq. (1), Eq. (3), and Steps 3–5.
