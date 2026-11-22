# Unique transient-norm peak and exponentially small angular overshoot for affine Fock composition semigroups

## Finding

On the classical Bargmann–Fock space, fix a nonzero point \(c\in\mathbb C\), a decay rate \(\alpha>0\), and an angular rate \(\beta\in\mathbb R\). The unweighted affine composition semigroup
\[
(T_t f)(z)=f\!\left(c+e^{-(\alpha+i\beta)t}(z-c)\right),\qquad t\ge0,
\]
converges in operator norm to \(P_cf=f(c)\), whose norm is \(e^{|c|^2/2}\). Put \(\kappa=|\beta|/\alpha\), \(\tau=\alpha t\), and
\[
R_\kappa(\tau)=\frac{\cosh\tau-\cos(\kappa\tau)}{\sinh\tau}\quad(\tau>0).
\]
Then \(\log\|T_t\|=|c|^2R_\kappa(\alpha t)/2\). If \(\beta=0\), this norm increases strictly to \(\|P_c\|\), without attaining its supremum. If \(\beta\ne0\), there is a **unique finite-time global maximizer** \(t_*=\tau_*/\alpha\) and \(\|T_{t_*}\|>\|P_c\|\). Here \(\tau_*\) is the unique solution in \((\pi/(2\kappa),3\pi/(2\kappa))\) of
\[
\cosh\tau\cos(\kappa\tau)+\kappa\sinh\tau\sin(\kappa\tau)=1.
\]
There is exactly one additional local extremum in each consecutive angular half-period, the extrema alternate between maxima and minima, and \(\|T_t\|\) crosses its limiting value infinitely often.

For fixed \(\kappa>0\), let \(\tau_m\), \(m=0,1,2,\dots\), enumerate the critical times; \(\tau_0=\tau_*\). With
\[
\tau_m^{(0)}=\frac{\pi/2+\arctan\kappa+m\pi}{\kappa},
\]
one has, as \(m\to\infty\),
\[
\tau_m=\tau_m^{(0)}+O_\kappa(e^{-\tau_m^{(0)}}),\qquad
R_\kappa(\tau_m)-1=\frac{2(-1)^m\kappa}{\sqrt{1+\kappa^2}}e^{-\tau_m^{(0)}}\bigl(1+O_\kappa(e^{-\tau_m^{(0)}})\bigr).
\]
In the singular small-angular-speed limit \(\kappa\downarrow0\), the global peak occurs at
\[
\alpha t_* =\frac{\pi}{2\kappa}+1+O(\kappa^2)
\]
and the sharp maximum amplification beyond the limiting projection is
\[
\boxed{\frac{\sup_{t\ge0}\|T_t\|}{\|P_c\|}-1
\sim\frac{|c|^2}{e}\,\kappa\,\exp\!\left(-\frac{\pi}{2\kappa}\right).}
\]
In particular, every nonzero angular rate produces a genuine positive overshoot, even though its magnitude tends to zero faster than every algebraic power of \(\kappa\).

## Assumptions and scope

The Hilbert space is \(\mathcal F^2=\{f(z)=\sum_{n\ge0}a_n z^n/\sqrt{n!}:\sum |a_n|^2<\infty\}\), with the indicated orthonormal basis and kernel \(K_w(z)=e^{z\overline w}\). The parameters satisfy \(\alpha>0\), \(c\in\mathbb C\setminus\{0\}\), \(\beta\in\mathbb R\). All norms are operator norms on this specific Hilbert space; time is real and nonnegative. The estimates \(O_\kappa\) are for fixed \(\kappa>0\) as \(m\to\infty\), whereas the final asymptotic is for fixed \(\alpha,c\) and \(\kappa\downarrow0\). No assertion is made for weighted composition semigroups or other Fock normalizations.

## Proof

**1. Exact operator norm.** Let \(\phi(z)=az+b\) with \(|a|<1\), \(d=1-|a|^2\). The coherent-displacement operator \((U_u f)(z)=e^{-|u|^2/2+z\overline u}f(z-u)\) is unitary on \(\mathcal F^2\). Choose \(u=-b/d\) and \(v=\overline a b/d\). Direct substitution gives
\[
U_v C_{az}U_u=e^{-|b|^2/(2d)}C_{az+b}.
\]
Since \(C_{az}\) is diagonal on the monomial orthonormal basis with norm one,
\[
\|C_{az+b}\|=\exp\!\left(\frac{|b|^2}{2(1-|a|^2)}\right).
\]
The factor \(1/2\) follows from the explicitly stated kernel normalization; in particular \(\|C_b\|=\|K_b\|=e^{|b|^2/2}\). For the semigroup \(a=e^{-(\alpha+i\beta)t}\) and \(b=c(1-a)\), so
\[
\log\|T_t\|=\frac{|c|^2}{2}\frac{1+e^{-2\tau}-2e^{-\tau}\cos(\kappa\tau)}{1-e^{-2\tau}}
=\frac{|c|^2}{2}R_\kappa(\tau).
\]
At \(t=0\), \(T_0=I\). The limit \(P_c\) is rank one with norm \(e^{|c|^2/2}\). Operator-norm convergence of affine strict-contraction Fock composition semigroups is established in [1, Theorem 2.3]; it also follows from [1, Theorem 2.2] by taking integer steps and then using boundedness on a compact time interval.

**2. All stationary times.** Differentiation yields
\[
R_\kappa'(\tau)=\frac{F_\kappa(\tau)}{\sinh^2\tau},\qquad
F_\kappa(\tau)=\cosh\tau\cos(\kappa\tau)+\kappa\sinh\tau\sin(\kappa\tau)-1,
\]
\[
F_\kappa'(\tau)=(1+\kappa^2)\sinh\tau\cos(\kappa\tau).
\]
When \(\kappa=0\), \(R_0(\tau)=\tanh(\tau/2)\), strictly increasing. For \(\kappa>0\), \(F_\kappa(0)=0\) and \(F_\kappa>0\) on \((0,\pi/(2\kappa))\). At the endpoints of the intervals
\[
J_m=\left(\frac{(m+1/2)\pi}{\kappa},\frac{(m+3/2)\pi}{\kappa}\right),\qquad m=0,1,2,\ldots,
\]
its values are \((-1)^m\kappa\sinh((m+1/2)\pi/\kappa)-1\) and \((-1)^{m+1}\kappa\sinh((m+3/2)\pi/\kappa)-1\). Since \(\kappa\sinh(\pi/(2\kappa))>\pi/2>1\), these have opposite signs. The displayed derivative shows that \(F_\kappa\) is strictly monotone in each \(J_m\), proving exactly one zero \(\tau_m\) per interval, with alternating maximum/minimum type.

**3. Global maximum and infinitely many crossings.** Write \(q=e^{-\tau}\), \(h=\cos(\kappa\tau)\). Then
\[
R_\kappa(\tau)-1=G(q,h):=\frac{2q(q-h)}{1-q^2}.
\]
If \(G(q,h)>0\), then \(h<q\), and
\[
\frac{\partial G}{\partial q}=
\frac{2(2q-h(1+q^2))}{(1-q^2)^2}>0.
\]
For \(\tau>2\pi/\kappa\) with \(R_\kappa(\tau)>1\), shifting time backward by \(2\pi/\kappa\) preserves \(h\), increases \(q\) and strictly raises \(R_\kappa\). Hence any global maximum above one must occur in the first period. In \((0,2\pi/\kappa)\), the first stationary point \(\tau_0\in J_0\) is a strict maximum, the second is a minimum, and \(R_\kappa(2\pi/\kappa)<1\). Since \(R_\kappa(\pi/\kappa)>1\), the first maximum is above one and is the unique global maximum. Further, at \(\tau=2m\pi/\kappa\) for \(m\ge1\), \(R_\kappa<1\), whereas at \(\tau=(2m+1)\pi/\kappa\), \(R_\kappa>1\). Continuity proves infinitely many crossings.

**4. Critical-point and peak asymptotics.** Put \(\theta=\kappa\tau\) and \(q=e^{-\tau}\). The stationary equation rearranges exactly to
\[
\cos\theta+\kappa\sin\theta
=2q-q^2(\cos\theta-\kappa\sin\theta).
\]
The simple zeros of the left side in successive intervals occur at \(\theta=\pi/2+\arctan\kappa+m\pi\), with derivative of magnitude \(\sqrt{1+\kappa^2}\). Thus the implicit zero correction is \(O_\kappa(q)\) in angle, which establishes the stated location asymptotics in \(\tau\). Substituting at the critical points gives the alternating excess formula. For the first point as \(\kappa\downarrow0\), the unperturbed time \(\tau_0^{(0)}=(\pi/2+\arctan\kappa)/\kappa\) goes to infinity, and the correction is \(O(e^{-\tau_0^{(0)}}/\kappa)\). Using \(\arctan\kappa/\kappa=1+O(\kappa^2)\) yields the claimed time. Moreover,
\[
R_\kappa(\tau_*)-1\sim\frac{2\kappa}{\sqrt{1+\kappa^2}}
\exp\!\left(-\frac{\pi/2+\arctan\kappa}{\kappa}\right)
\sim\frac{2\kappa}{e}e^{-\pi/(2\kappa)}.
\]
Exponentiating \(\log(\|T_{t_*}\|/\|P_c\|)=|c|^2(R_\kappa(\tau_*)-1)/2\) proves the sharp amplification coefficient.

## Verification

Run `python3 CHECKER.py` with the Python standard library. It independently evaluates the exact stationary equation using its exponentially rescaled form, bisects 48 stationary times, checks alternating extrema and sampled global dominance, tests small-angle peak asymptotics, and directly checks the Weyl-unitary conjugation formula on polynomial examples. The diagnostic result is **PASS: 18,295 finite checks**. The proof, not numerical sampling, establishes unique and infinitely many claims.

## Relationship to prior work

Chalendar and Partington [1] classify one-parameter Fock composition semigroups and their operator-norm limits, while the earlier Fock composition norm literature [3] determines pointwise norms. The survey [2, Section 6.2] also records these underlying facts. Those are inputs, not newly claimed results. The contribution here is the global-in-time optimization, the exact one-per-half-period stationary-point classification, infinite crossings of the limiting norm, and the singular exponentially small first-peak law. The pointwise norm formula **does imply** these conclusions after the additional elementary-but-global stationary-point and asymptotic analysis; priority should therefore be interpreted as a refinement of established explicit norm data, not an independent spectral classification.

## Limitations

The result treats only one complex variable, unweighted composition, a nonzero fixed point, and a scalar damped rotation with positive contraction rate. It does not claim that all affine weighted composition semigroups behave this way. The 2019 exact-norm paper [3] was accessible only through its metadata/abstract, so possible uninspected discussion of time optimization is an outstanding historical-priority risk. Independent validation has not been performed.

## References

[1] I. Chalendar and J. R. Partington, *Weighted composition operators on the Fock space: iteration and semigroups*, first posted 1 June 2021, https://arxiv.org/abs/2106.00427.

[2] I. Chalendar and J. R. Partington, *Semigroups of weighted composition operators on spaces of holomorphic functions*, first posted 23 January 2022, https://arxiv.org/abs/2201.09249.

[3] J. Dai, *The norm of composition operators on the Fock space*, online 4 February 2019, https://doi.org/10.1080/17476933.2018.1547284.

[4] T. Mengestie, *Resolvent growth condition for composition operators on the Fock space*, online 17 February 2020, https://link.springer.com/article/10.1007/s43034-020-00059-9.
