# Sharp two-phase Markov–Bernstein constant for damped conjugate modes

## Finding

Let \(a,b>0\), and consider the first-derivative operator norm \(\mathcal M(a,b)\) on the real span of \(e^{-at}\cos(bt)\) and \(e^{-at}\sin(bt)\), with supremum norm on \([0,\infty)\). Put \(r=a/b\), \(R=\sqrt{1+r^2}\), and
\[
g_r(u)=e^{ru}(\cos u-r\sin u),\qquad u_1=\pi/2+\arctan r.
\]
There is a unique \(u_c\in(\arctan(1/r),\pi)\) with \(g_r(u_c)=-1\). For \(u_*=\min(u_1,u_c)\) the sharp norm is
\[
\boxed{\mathcal M(a,b)=b(1+r^2)e^{r u_*}\sin u_* .}
\]
The complex span of the two conjugate modes has the same norm. There is a unique transition ratio \(r_*=0.29908438015271477\ldots\) determined by \((2r_*/\sqrt{1+r_*^2})e^{r_*(\pi/2+\arctan r_*)}=1\). For \(r\le r_*\), \(u_*=u_1\) and \(\mathcal M(a,b)=bR e^{r u_1}\); for \(r>r_*\), \(u_*=u_c\).

**Real extremizers.** Define \(F_r(x)=g_r(u_*-x)\) for all real \(x\). Up to nonzero real scaling, all half-line derivative-norm extremizers are
\[
 f(t)=F_r(bt-d),\qquad 0\le d\le u_c-u_*.
\]
The displayed representatives have norm one; the unique representative with a positive extremal derivative *at time zero* is \(d=0\). For \(0<r<r_*\) the full derivative norm instead has a nontrivial interval of translated extremizers. There is a positive-time norm contact at \(t=(u_*+d)/b\) of value \(1\); the endpoint is a contact of value \(-1\) exactly when \(d=u_c-u_*\). For \(r\ge r_*\) the interval collapses, and the extremizer is unique up to nonzero real scaling and has both contacts.

The dimensionless norm \(C(r)=\mathcal M(br,b)/b\) is \(C^1\) but not twice differentiable at \(r_*\), with a strictly negative right-minus-left second-derivative jump given below. Moreover \(\lim_{r\downarrow 0}C(r)=1\) and \(\lim_{r\to\infty}C(r)/r=q/(q-1)=4.59112147666862\ldots\), where \(q=1+W(e^{-1})\in(1,2)\) and \(W\) is the principal Lambert function.

## Assumptions and scope

All norms are unweighted. Only the first derivative, a common positive damping rate, one positive frequency, and the nonnegative half-line are considered. The supremum of a derivative over the open half-line has the same value as over its closure by continuity. The two limiting damping statements do not classify any zero-frequency or undamped extremizers. The classification above is of real extremizers; only the constant is asserted for complex modes.

## Proof

**1. Initial derivative and real reduction.** Rescale time by \(x=bt\); this multiplies the dimensionless derivative norm by \(b\). In dimensionless time, right translation preserves the space and contracts its norm. For each \(h\ge0\), applying an initial-derivative bound to \(f(x+h)\) controls \(|f'(h)|\), and the full derivative bound in turn controls \(|f'(0)|\). Thus the two optimal constants coincide, though their equality cases need not coincide. For a complex function and any \(h\), translate by \(h\), rotate by a constant complex phase to make its initial derivative nonnegative real, and take its real part. This lies in the real space, keeps the required derivative value, and has norm at most that of the starting function. This proves equality of the real and complex constants.

**2. Phase optimization.** Up to real scaling every nonzero real function is \(e^{-rx}\cos(x-u-\phi)\) with \(\phi=\arctan r\), \(u\in[0,\pi)\). Its stationary times differ by \(\pi\), with absolute values decreasing by \(e^{-r\pi}\); the first nonnegative stationary time is \(u\). Its norm is \(R^{-1}\max\{|\cos u-r\sin u|,e^{-ru}\}\), and its initial derivative has magnitude \(R\sin u\). Therefore
\[
C(r)=\max_{0\le u\le\pi}\frac{R^2\sin u}{\max\{|\cos u-r\sin u|,e^{-ru}\}}.
\]
The endpoint phases contribute zero. Since \(g_r'(u)=-R^2e^{ru}\sin u<0\) for \(0<u<\pi\), with \(g_r(0)=1\) and \(g_r(\pi)=-e^{r\pi}\), there is one threshold \(u_c\), necessarily after the zero \(\arctan(1/r)\). Up to and including \(u_c\) the quotient is \(R^2 e^{ru}\sin u\), increasing strictly up to \(u_1\) and decreasing strictly thereafter. From \(u_c\) on it is \(R^2/(r-\cot u)\), strictly decreasing until it tends to zero at \(\pi\). The unique maximizing phase is therefore \(u_*\). At \(u=u_1\), \(-g_r(u_1)=(2r/R)e^{r u_1}\), which increases from zero to infinity (logarithmic derivative \(1/r+u_1\)). This proves the transition equation and equivalent branches. The normalized initial-derivative extremizer with positive derivative is \(F_r(x)=R e^{r u_*}e^{-rx}\cos(x-u_* -\phi)\), equivalently \(g_r(u_*-x)\). It has \(F_r(u_*)=1\), \(F_r'(0)=C(r)\), \(\|F_r\|_\infty=1\), and all later stationary absolute values are less than one.

**3. All real equality cases for the full derivative norm.** Normalize \(f\) to norm one in dimensionless time. Its derivative is continuous and decays to zero, so its derivative norm is attained at some \(d\ge0\) on the closed half-line. If that norm equals \(C(r)\), the right translate \(f(x+d)\) must also have norm one: a smaller norm would contradict the bound for its initial derivative. By uniqueness of the maximizing phase, \(f(x+d)=\pm F_r(x)\) for \(x\ge0\). Both sides are real analytic and belong to the same two-dimensional space on the whole line, so this identity extends and determines \(f(x)=\pm F_r(x-d)\). Conversely a shift of this form remains of norm one exactly when \(|F_r|\le1\) on \([-d,0]\); it then has derivative magnitude \(C(r)\) at \(d\) and is an extremizer. On the backward interval, \(F_r(x)=g_r(u_*-x)\). Since \(g_r\) decreases strictly on \((0,\pi)\) and crosses \(-1\) at \(u_c<\pi\), the extra interval is admissible precisely up to \(d=u_c-u_*\). If \(d\) is larger, the interval includes a point with argument between \(u_c\) and \(\pi\), where \(g_r<-1\). On the admissible interval the value \(-1\) is attained only at the new endpoint and only for maximal \(d\); on the forward interval the only active positive-time contact is the first stationary point. Moreover, for \(d>0\) the initial phase \(u_*+d\) differs from the uniquely optimal initial phase \(u_*\), so it cannot attain the initial-derivative bound. Restoring \(x=bt\) gives the claimed classification.

**4. Differentiability across the switch.** Write \(W_0(r,u)=R^2 e^{ru}\sin u\). This is analytic, as are the two phase branches; implicit differentiation at the contact gives
\[
u_c'=-\frac{u_c+e^{r u_c}\sin u_c}{W_0(r,u_c)}.
\]
The composites agree at \(r_*\), where \((W_0)_u=0\) at the common phase. Thus their first derivatives agree. At the common point put \(R_*=\sqrt{1+r_*^2}\), \(U=u_1(r_*)\), and \(M=W_0(r_*,U)\). Here \(u_1'=R_*^{-2}\), \(u_c'=-R_*^{-2}-U/M\), and \((W_0)_{uu}=-R_*^2M\). Differentiating the stationary condition along \(u_1(r)\) gives \((W_0)_{ru}=-(W_0)_{uu}u_1'\) at the crossing. Consequently the second derivatives of the two composites differ by \((W_0)_{uu}(u_c'-u_1')^2\), so
\[
\boxed{C''(r_*+)-C''(r_*-)
=-R_*^2 M\left(2/R_*^2+U/M\right)^2<0 .}
\]
The analytic branches and this nonzero jump show that \(C\) is continuously differentiable but has no second derivative at the switch.

**5. Limits.** The small-\(r\) branch gives \(C(r)=1+(\pi/2)r+O(r^2)\). For large \(r\), set \(x_r=ru_c\). The increasing contact expression on the relevant phase interval becomes \(e^{x_r}(r\sin(x_r/r)-\cos(x_r/r))=1\). On \([1,2]\) its left side converges uniformly to \(e^x(x-1)\), whose endpoint values bracket one strictly. By uniqueness, for sufficiently large \(r\) the root is in that interval, and it tends to the unique \(q\) with \(e^q(q-1)=1\). Substitution in \(C(r)/r\) gives \(q e^q=q/(q-1)\).

## Verification

The analytic argument proves the continuum result and the translated equality classification. The companion standard-library `check.py` checks the numerical norm formula, transition, canonical witness \(F_r\), large-damping limit and curvature jump on finite probes (`python3 check.py`). That script does not test global uniqueness or the classification of translated extremizers.

## Relationship to prior work and limitations

Protasov's general exponential-polynomial inequalities provide the broader Markov–Bernstein setting; general constrained uniform-approximation algorithms are also known. The damped harmonic example in Kamalov and Protasov, §9.4, is described in the literature comparison as including an additional \(e^{-t}\) mode. The claim here specifically evaluates the two-mode constant and classifies its real equality cases, including the collapse of a nontrivial interval of shifts. It does not settle comparison conjectures or cover higher derivatives, additional modes, or finite time windows. Exact priority remains subject to possible earlier specialist results on maximal initial velocities of damped oscillators.

## References

1. V. Yu. Protasov, *Generalized Markov–Bernstein inequalities and stability of dynamical systems*, arXiv:2209.12250.
2. V. Yu. Protasov and R. Kamalov, *Chebyshev approximation by non-Chebyshev systems*, arXiv:2403.16330.
3. P. Borwein and T. Erdélyi, *A sharp Bernstein-type inequality for exponential sums*, J. reine angew. Math. 476 (1996), 127–141, doi:10.1515/CRLL.1996.476.127.
