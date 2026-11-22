# Full joint limit rectangle for Goldring prime-factor quotients on squarefree three-prime inputs

## Finding

Let \(P(a)\) be the largest prime divisor of \(a\ge2\). Let \(\mathcal C_3\) be the set of products \(n=pqr\) of three *distinct* primes and define
\[
w(pqr)=P(p+q)P(p+r)P(q+r),\qquad
R(n)=\frac{P(w(n))}{P(n)},\qquad S(n)=\frac{w(n)}n.
\]
The set of all finite simultaneous accumulation points of \((R(n),S(n))\) as \(n\to\infty\) through \(\mathcal C_3\) is **exactly**
\[
\boxed{\mathcal L_{\mathcal C_3}=[0,1]\times[0,\infty).}
\]
The same conclusion holds under the additional requirement \(w(n)\in\mathcal C_3\), and with the three input primes odd. More quantitatively, for **every** point \((\alpha,\beta)\) of this closed rectangle and every open neighborhood \(U\subset\mathbb R^2\) of the point, a positive constant \(c_U\) exists such that, for all sufficiently large real \(X\),
\[
\#\{n\le X:n,w(n)\in\mathcal C_3,\ (R(n),S(n))\in U\}
\ge c_U\frac{X}{(\log X)^6}.
\]
This is a joint statement: prescribing the two quotients simultaneously is substantially stronger than prescribing either marginal limit separately.

## Assumptions and scope

All prime variables used in the prime-pattern construction tend to infinity. Prime patterns are obtained from the unconditional, finite-complexity-six-form case of the Green–Tao theorem, with local solubility and complexity verified in Yang–Zhao's Lemma 5. The construction makes no unproved prime-tuple conjecture. The lower bound's constant may depend on \(U\); it is not uniform as \(U\) shrinks or approaches an axis. The statement concerns accumulation points and not natural density among all members of \(\mathcal C_3\).

## Proof

**1. Upper containment.** If \(p,q,r\) are all odd primes, each pair sum is even; hence \(P(p+q)\le(p+q)/2\le P(pqr)\), and similarly for the other two sums. Therefore \(0<R(n)\le1\) and \(S(n)>0\). If one input prime is 2, the same argument for the odd-odd pair and \(P(2+t)\le t+2\) for each odd input \(t\) give \(R(n)\le1+2/P(n)\). As \(n\to\infty\) in \(\mathcal C_3\), necessarily \(P(n)\to\infty\). Thus every finite joint accumulation point lies in the asserted rectangle.

**2. Simultaneously prime linear forms.** Fix an integer \(m\ge1\). Yang–Zhao establish that
\[
x,\quad y,\quad z,\quad mx+my-z,\quad mx-my+z,\quad-mx+my+z
\]
form a locally admissible system of Green–Tao complexity at most two. Write the final three forms \(p,q,r\). The identities
\[
p+q=2mx,\qquad p+r=2my,\qquad q+r=2z
\]
show that, whenever all six forms are prime and \(x,y,z>P(2m)\), one has \(w(pqr)=xyz\) and
\[
(R(pqr),S(pqr))=\left(\frac{\max(x,y,z)}{\max(p,q,r)},\frac{xyz}{pqr}\right).
\]
For each fixed positive real triple \((p,q,r)\) satisfying these relations, choose the corresponding positive \((x,y,z)\) as a center, then a sufficiently small *fixed* positive closed three-dimensional box around it. The Green–Tao theorem gives \(\gg N^3/(\log N)^6\) simultaneous prime points in the dilated box. Equalities among the three input or output primes lie on finitely many proper hyperplanes with only \(O(N^2)\) integer points, so may be removed. The unordered integer \(n=pqr\) has at most six representations. All six primes are \(\asymp N\), so \(n\asymp N^3\), and the resulting pair of quotients lies in any fixed neighborhood of its real center with \(\gg X/(\log X)^6\) distinct squarefree input and output products \(n\le X\). If the edges with multiplier \(2m\) are \(p+r,q+r\) rather than \(p+q,p+r\), a permutation of the three input primes reduces the system to the same six forms; the conclusion is unchanged.

**3. Every interior pair is attainable.** Fix \(0<\alpha\le1\) and \(\beta>0\), and normalize the prospective three positive input-prime sizes as \((p,q,r)=(1,u,v)\).

If \(0<\alpha\le1/2\), take \(u=2\alpha-v\) with \(0<v\le\alpha\), so \(1\ge u\ge v>0\), and place the two multiplier-\(m\) edges at \(p+q,p+r\):
\[
x=\frac{1+u}{2m},\qquad y=\frac{1+v}{2m},\qquad z=\frac{u+v}2=\alpha.
\]
Choose integer \(m\) large enough that \((1+2\alpha)/(2m)<\alpha\) and \((1+\alpha)^2/(4m^2\alpha)<\beta\). Then \(\max(x,y,z)=\alpha\), so \(R=\alpha\) for every \(v\) in the indicated range; meanwhile
\[
S(v)=\frac{\alpha(1+u)(1+v)}{4m^2uv}.
\]
At \(v=\alpha\), this is \((1+\alpha)^2/(4m^2\alpha)<\beta\), whereas \(S(v)\to\infty\) as \(v\downarrow0\). Continuity supplies a strictly positive \(v\) with \(S(v)=\beta\).

If \(1/2<\alpha\le1\), take \(u=2\alpha-1>0\), allow \(0<v\le u\), and place multiplier 1 at \(p+q\) and multiplier \(m\) at both \(p+r,q+r\):
\[
x=\frac{1+u}2=\alpha,\qquad y=\frac{1+v}{2m},\qquad z=\frac{u+v}{2m}.
\]
Choose an integer \(m\ge2\) so large that \(\alpha^2/[m^2(2\alpha-1)]<\beta\). For every indicated \(v\), \(x\ge y,z\) and the largest input is 1, hence \(R=\alpha\). Also,
\[
S(v)=\frac{\alpha(1+v)(u+v)}{4m^2uv},\qquad
S(u)=\frac{\alpha^2}{m^2u}<\beta,
\]
while \(S(v)\to\infty\) as \(v\downarrow0\). The intermediate value theorem gives \(v\) with \(S(v)=\beta\).

Each constructed center has all six linear forms strictly positive. The prime-point argument in Step 2 therefore proves the quantitative joint-neighborhood bound for every pair \((\alpha,\beta)\) with \(\alpha>0,\beta>0\), including \(\alpha=1\). The centers are allowed to lie on equality hyperplanes: removing those hyperplanes from a fixed positive-volume surrounding box leaves the leading prime-point bound intact.

**4. Boundary and conclusion.** Any open neighborhood of any point of \([0,1]\times[0,\infty)\) contains a point \((\alpha',\beta')\) with \(0<\alpha'<1\) and \(\beta'>0\). Apply Step 3 in a smaller neighborhood contained in the first to obtain the same \(\gg X/(\log X)^6\) lower bound. By taking shrinking neighborhoods and increasing integers, all boundary points are accumulation points. The upper containment from Step 1 completes the proof.

## Verification

An accompanying dependency-free Python checker independently evaluates the exact six-form identities and Goldring quotients on prime configurations, verifies the full six-form complexity partitions for 25 integer multipliers, checks local admissibility at 14 primes and 25 multipliers (350 checks), checks four exact rational centers, and tests 50 numerical parameter inversions spanning both cases and extreme positive target values. Its output is `GOLDRING_JOINT_PARAM_OK rational_centres=4 local_checks=350 complexity_rows=150 real_targets=50 sample_prime_patterns>=4`. These finite checks do **not** prove the infinitude of prime configurations; that step relies on the cited unconditional theorem and verified hypotheses.

For example, the second construction at \(m=3\), \((p,q,r)=(1,1/2,1/4)\) has \((x,y,z)=(3/4,5/24,1/8)\), giving \((R,S)=(3/4,5/32)\). The latter pair lies far below the positive-region bound \(S\ge R^2/(2R-1)\) for the restricted case where *all three half-sums* are prime.

## Relationship to prior work

Yang and Zhao (2026) give the two **individual** limit sets on \(\mathcal C_3\) and a complete **joint** limit classification on the different, repeated-prime family \(\mathcal B_3\). Their already-established six-form prime-pattern lemma and counting method are indispensable here. The additional ingredient is the two-regime real parameterization showing that, in the squarefree family, those prime patterns realize **every** pair of positive target quotients at once. In contrast, the repeated-prime joint set is a countable union of curves and axes. Earlier results on the dynamics and extremal individual quotients do not supply the squarefree joint classification. The known all-half-sums-prime subfamily yields a proper restricted region; no claim of novelty is made for that earlier subfamily. The conclusion is a new theorem derived from the published prime-pattern machinery, not a new linear-forms-in-primes theorem.

## Limitations

The lower-bound constant is neighborhood-dependent and non-effective in the standard Green–Tao formulation. This work does not give a limiting joint probability distribution on \(\mathcal C_3\), a positive relative density for fixed rectangles, or uniform estimates for shrinking neighborhoods. The count \(X/(\log X)^6\) is a lower bound, not asserted to be optimal. Independent proof review and priority confirmation have not been performed. Related 2012 journal full text was not accessible in the available source inspection; its abstract and the detailed 2026 primary treatment were compared.

## References

1. Q.-H. Yang and J.-J. Zhao, *Density and distribution of quotients associated with Goldring's w-function*, arXiv:2611.02851v1, first public 2026-11-02, Theorems 1–3 and Lemma 5, https://arxiv.org/html/2611.02851v1.
2. B. Green and T. Tao, *Linear equations in primes*, Annals of Mathematics **171** (2010), 1753–1850, Corollary 1.7, https://doi.org/10.4007/annals.2010.171.1753.
3. Y.-G. Chen, Y. Shi and J. Wu, *Dynamics of Goldring's w-function*, Journal of Number Theory **132** (2012), 390–409, https://doi.org/10.1016/j.jnt.2011.07.012.
