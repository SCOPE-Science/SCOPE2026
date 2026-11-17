# Sharp sixth-moment staircase for sparse symmetric three-point first chaos

## Finding

Fix an integer \(n\ge 2\) and a real \(t\ge 1\). Let \(X_1,\ldots,X_n\) be independent, each having the symmetric three-point law
\[
\mathbb P(X_j=\sqrt t)=\mathbb P(X_j=-\sqrt t)=\frac1{2t},
\qquad \mathbb P(X_j=0)=1-\frac1t.
\]
These variables are centered and have variance one. On their real linear span in \(L^6\), the exact sixth power of the identity-embedding norm from \(L^2\) into \(L^6\) is
\[
\boxed{C_n(t)^6=\max_{1\le k\le n}F_k(t),\qquad
F_k(t)=15+\frac{15(t-3)}k+\frac{t^2-15t+30}{k^2}.}\tag{1}
\]
Here \(C_n(t)=\sup_{a\ne0}\|\sum_j a_jX_j\|_6/\|\sum_j a_jX_j\|_2\).

All equality cases can be classified. If \(1\le t<5\) and \(t\) is not one of the crossing parameters defined below, every maximizing real coefficient vector \(a\), after normalization \(\sum_j a_j^2=1\), has exactly \(k\) nonzero entries, each of magnitude \(1/\sqrt k\), where \(k\) is the unique maximizer of (1). Signs and support locations are arbitrary. At a crossing \(t=\tau_k\) with \(k\ge2\), the only maximizers are these flat vectors of support sizes \(k\) and \(k+1\). At the special crossing \(t=5=\tau_1\), *every* coefficient vector supported on at most two coordinates is maximizing, regardless of the two nonzero magnitudes. For \(t>5\), precisely the one-coordinate vectors maximize. At \(t=1\), the same flat full-support characterization holds.

For each integer \(k\ge1\), let \(\tau_k\) denote the unique real solution greater than \(3\) of
\[
15(\tau_k-3)k(k+1)+(2k+1)(\tau_k^2-15\tau_k+30)=0.\tag{2}
\]
Then
\[
5=\tau_1>\tau_2>\tau_3>\cdots>3,
\qquad \lim_{k\to\infty}k(\tau_k-3)=\frac45.
\]
For fixed \(n\), the maximizing support decreases through \(n,n-1,\ldots,1\) as \(t\) increases, crossing from \(k+1\) to \(k\) exactly at \(\tau_k\), for \(1\le k<n\). Thus *every* intermediate support size occurs, and the number of transitions grows without bound with the dimension.

As a consequence, the best dimension-free sixth-moment constant is Gaussian for \(1\le t\le3\), and strictly exceeds the Gaussian value for \(t>3\):
\[
C_\infty(t)^6:=\sup_{n\ge2}C_n(t)^6=
\begin{cases}
15,&1\le t\le3,\\
\max_{k\ge1}F_k(t)>15,&t>3.
\end{cases}\tag{3}
\]
For \(t\ge5\), (3) equals \(t^2\). For \(t\downarrow3\), the optimal finite support size is asymptotic to \(4/[5(t-3)]\) and
\[
C_\infty(t)^6=15+\frac{75}{8}(t-3)^2+O((t-3)^3).
\]
At and below \(t=3\), the dimension-free supremum \(15\) is approached with growing equal support but not attained in a finite dimension.

## Assumptions and scope

All random variables are independent, identically distributed, real and supported on precisely the stated three-point law (at \(t=1\), the zero atom has mass zero). All expectations use its product probability law. The normalized coefficient simplex is \(x_j=a_j^2\ge0\), \(\sum_jx_j=1\). The parameter \(t\) is real, not restricted to integers. Only the sixth-to-second norm comparison is asserted; no other exponents, complex coefficients, nonidentical laws or dependent coordinates are included.

## Proof

**Step 1: exact moment polynomial.** Directly, \(\mathbb EX_j^2=1\), \(\mathbb EX_j^4=t\), and \(\mathbb EX_j^6=t^2\). Expanding the sixth moment by independence and symmetry, with \(s_r=\sum_jx_j^r\), gives
\[
\mathbb E\left(\sum_j a_jX_j\right)^6
=15+15(t-3)s_2+(t^2-15t+30)s_3.\tag{4}
\]
Indeed, the monomial types are one exponent \(6\), one exponent \(4\) and another \(2\), or three exponents \(2\); their multinomial factors are respectively \(1\), \(15\) and \(90\). The \(L^2\) norm is \((\sum_j a_j^2)^{1/2}\), so maximizing (4) on the simplex suffices.

**Step 2: pair-smoothing lemma and complete equality cases.** Put \(A=15(t-3)\), \(B=t^2-15t+30\), and \(\phi(z)=Az^2+Bz^3\). For any pair of nonnegative coordinates \(u,v\), with fixed sum \(s=u+v>0\), the identity
\[
\phi(u)+\phi(v)=As^2+Bs^3+uv[-2A-3Bs]\tag{5}
\]
shows that the pair contribution depends *affinely* on \(uv\). If \(D(s):=-2A-3Bs>0\), the unique maximizing pair is \((s/2,s/2)\); if \(D(s)<0\), only \((s,0)\) and \((0,s)\) maximize. If \(D(s)=0\), all pairs with that sum tie.

For \(1\le t\le3\), \(D(s)>0\) for every \(0<s\le1\): when \(B\le0\) this follows from \(A\le0\), and when \(B>0\), \(D(s)\ge D(1)=3t(5-t)>0\). Repeated pair-smoothing, including pairs of positive and zero coordinates, forces all \(n\) weights to be \(1/n\), hence the unique support size is \(n\).

For \(3<t<5\), \(A>0\) and \(B<0\), so \(D(s)\) has exactly one positive zero. At any global maximum, two *unequal positive* weights \(u,v\) would require \(D(u+v)=0\), since otherwise the pair could be strictly improved by equalization or by deletion. If a third positive weight \(w\) exists, comparison of unequal pairs forces any such \(w\) to equal either \(u\) or \(v\). Thus two coordinates of one value are repeated. Perturb an unequal pair slightly while keeping its sum fixed: (5) leaves the objective unchanged, but the repeated pair becomes unequal with a generically different sum. Applying (5) to this new unequal pair strictly improves the purported maximum, a contradiction. Hence every maximizer with three or more nonzero weights is flat. For precisely two nonzero weights, \(D(1)=3t(5-t)>0\) forces equality. Consequently every maximizer is flat on its support, and substituting \(x_j=1/k\) into (4) proves (1) and the equality classification away from the crossings.

At \(t=5\), (5) has \(D(s)=60(s-1)\). If at least three weights are positive, some pair has sum less than one and can be strictly improved by deletion. For support one or two, the objective is identically \(25\), proving the exceptional continuum. For \(t>5\), \(D(s)<0\) for all \(0<s\le1\): if \(B<0\), use \(D(s)\le D(1)=-3t(t-5)<0\), and if \(B\ge0\), use \(D(s)\le-2A<0\). Thus only singleton supports survive, with value \(F_1(t)=t^2\).

**Step 3: phase staircase.** For \(3<t\le5\), set \(R(t)=-B/A\). Direct algebra yields
\[
R(t)=\frac{12-t}{15}+\frac{2}{5(t-3)},\qquad
R'(t)=-\frac1{15}-\frac{2}{5(t-3)^2}<0.
\]
Moreover, for each \(k\ge1\),
\[
F_{k+1}(t)-F_k(t)=\frac{A(2k+1)}{k^2(k+1)^2}
\left(R(t)-\frac{k(k+1)}{2k+1}\right).\tag{6}
\]
The quantities \(k(k+1)/(2k+1)\) are strictly increasing with \(k\), while \(R(t)\) strictly decreases from \(+\infty\) to \(2/3\) as \(t\) increases from \(3\) to \(5\). Equation (6) gives a single adjacent crossing for each \(k\), its defining equation (2), strict ordering, and no nonadjacent ties. In particular the support increases monotonically with \(R(t)\). The asymptotic estimate \(k(\tau_k-3)\to4/5\) follows by comparing \(R(3+\varepsilon)\sim2/(5\varepsilon)\) with \(k(k+1)/(2k+1)\sim k/2\).

**Step 4: dimension-free transition.** For \(t\le3\), the finite maximum is \(F_n(t)\), which increases to \(15\) as \(n\to\infty\) and is strictly below it for each finite \(n\). For \(t>3\), choose sufficiently large finite \(k\) so that \(A/k+B/k^2>0\); the maximum therefore exceeds \(15\). The finite-support staircase makes that maximum attained at some \(k\). As \(t=3+\varepsilon\downarrow3\), the continuous quadratic \(A/k+B/k^2\), viewed as a function of \(1/k\), has maximum \(A^2/(-4B)=75\varepsilon^2/8+O(\varepsilon^3)\). Rounding the optimal \(k\) to an integer changes the value only by \(O(\varepsilon^4)\), proving the stated expansion and support asymptotic.

## Verification

Run `python checker.py` with Python 3.9 or later and SymPy installed. The self-contained checker computes the sixth moment independently by multinomial compositions; checks the pair identity and crossing derivatives symbolically; verifies the first 100 ordered transition roots; checks every squared-coefficient grid point of denominator twelve in dimensions two through four at eight rational parameter values; and verifies the exceptional two-support family at \(t=5\). Its final output is `ALL_SPARSE_SIXTH_MOMENT_DIAGNOSTICS_PASSED`. The exact universal statements follow from Steps 1–4, not from finite enumeration or numerical root comparisons.

## Relationship to prior work

Nayar and Oleszkiewicz (first public online June 15, 2011) establish general optimal even-moment Gaussian comparisons for ultra-sub-Gaussian summands. Their theory covers the dimension-free Gaussian regime here, since the normalized sparse law is ultra-sub-Gaussian for \(t\le3\), but does not state the finite-dimensional sharp values, the sparse optimizers for \(t>3\), or the sequence of support transitions. Havrilla and Tkocz (arXiv submission December 31, 2019) treat symmetric discrete laws and prove Schur concavity of the relevant moment norm for three-atom laws with zero mass at most one half (here \(t\le2\)); their main theorem does not cover the complete high-zero-mass phase diagram. These are credited ingredients and partial precedents, not novel subclaims.

Whittle's 1960 paper gives broad moment bounds for linear and quadratic forms, but its accessible bibliographic abstract does not permit a full implication comparison. A prior exact sixth-moment finding for *exactly two activated signed coordinates* (sampling without replacement) concerns a different, dependent distribution, and its one/two-support regimes do not imply this independent-thinning result with arbitrary optimal support sizes. The present claim should not be treated as a proof of publication priority; an equivalent result in older or poorly indexed moment-inequality literature remains possible.

## Limitations

Only the real sixth-to-second norm, the specified independent symmetric three-point family, and its finite and dimension-free extremizers are resolved. The proof does not establish analogous formulas for non-even exponents, arbitrary discrete laws, nonidentical thinning parameters, dependent sampling, or complex coefficients. The citations support comparison with inspected results; they do not certify exhaustive historical novelty.

## References

1. P. Nayar and K. Oleszkiewicz, *Khinchine type inequalities with optimal constants via ultra log-concavity*, Positivity 16 (2012), 359–371; publicly online June 15, 2011. DOI: 10.1007/s11117-011-0130-z. Open-access full text: https://link.springer.com/content/pdf/10.1007/s11117-011-0130-z.pdf
2. A. Havrilla and T. Tkocz, *Sharp Khinchin-type inequalities for symmetric discrete uniform random variables*, arXiv:1912.13345 (first submitted December 31, 2019). Full text: https://arxiv.org/abs/1912.13345
3. P. Whittle, *Bounds for the Moments of Linear and Quadratic Forms in Independent Variables*, Theory Probab. Appl. 5 (1960), 302–305. DOI: 10.1137/1105028; accessible bibliographic abstract: https://www.mathnet.ru/eng/tvp4838
