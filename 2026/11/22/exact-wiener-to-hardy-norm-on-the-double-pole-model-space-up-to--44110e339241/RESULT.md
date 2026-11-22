# Exact Wiener-to-Hardy norm on the double-pole model space up to half radius

## Finding

For every real \(0\le r\le 1/2\), let
\[
E_r=\left\{f(z)=\frac{a+bz}{(1-rz)^2}:a,b\in\mathbb C\right\}.
\]
With \(f(z)=\sum_{k\ge0}c_kz^k\), the Wiener and Hardy norms are
\[\|f\|_W=\sum_{k\ge0}|c_k|,\qquad
\|f\|_{H^2}=\left(\sum_{k\ge0}|c_k|^2\right)^{1/2}.\]
Then the exact embedding norm is
\[
\boxed{\sup_{0\ne f\in E_r}\frac{\|f\|_W}{\|f\|_{H^2}}
=\left[\frac{2(1+r)}{1-r}\big(1+2r^2(1-r)^2\big)\right]^{1/2}.}
\]
When \(0<r\le 1/2\), equality holds precisely for nonzero complex multiples of
\[
\boxed{f_r(z)=\frac{(1+2r^2)-(1+4r)z}{(1-rz)^2}.}
\]
At \(r=0\), equality holds precisely when \(|a|=|b|>0\). In particular, the endpoint sharp norm at \(r=1/2\) is \(3\sqrt3/2\).

## Assumptions and scope

The parameter \(r\) is real, and the denominator has a double zero-free pole factor inside the unit disk. The space \(E_r\) is the two-dimensional Hardy model space associated with the double Blaschke zero \(r\), equivalently the analytic functions with numerator degree at most one over the fixed denominator \((1-rz)^2\). Coefficients and norms are measured with respect to the Taylor expansion at the origin and the normalized unit-circle Hardy norm. The theorem optimizes only this fixed, coalesced-pole subspace: it is not an exact norm assertion for arbitrary rational functions with two distinct poles.

## Proof

**Step 1: an exact three-functional majorant.** Put \(u=(a,b)^\mathsf{T}\). Direct expansion gives
\[
c_0=a,\qquad c_k=r^{k-1}\big((2ra+b)+(k-1)(ra+b)\big)\quad(k\ge1).
\]
Since \(0\le r<1\), summing the geometric series and applying the triangle inequality proves
\[
\|f\|_W\le |a|+\frac{|2ra+b|}{1-r}
+\frac{r|ra+b|}{(1-r)^2}=:T_r(u).
\]
This is exact when the two complex quantities \(2ra+b\) and \(ra+b\) lie on the same ray. Define the real covectors
\[
v_0=(1,0)^\mathsf{T},\quad
v_1=(2r,1)^\mathsf{T}/(1-r),\quad
v_2=(r^2,r)^\mathsf{T}/(1-r)^2.
\]
Thus \(T_r(u)=\sum_{j=0}^2|v_j^\mathsf{T}u|\).

**Step 2: exact Hardy Gram matrix.** The coefficient identity and the sums \(\sum_{k\ge0}(k+1)^2r^{2k}=(1+r^2)/(1-r^2)^3\) and \(\sum_{k\ge1}k(k+1)r^{2k-1}=2r/(1-r^2)^3\) give
\[
\|f\|_{H^2}^2=u^*M_ru,\quad
M_r=\frac1{(1-r^2)^3}
\begin{pmatrix}1+r^2&2r\\2r&1+r^2\end{pmatrix},
\]
and
\[
M_r^{-1}=\begin{pmatrix}
1-r^4&-2r(1-r^2)\\-2r(1-r^2)&1-r^4
\end{pmatrix}.
\]
The duality formula for a map from a Hilbert space to \(\ell^1_3\) reads
\[
\max_{u\ne0}\frac{T_r(u)^2}{u^*M_ru}
=\max_{|\varepsilon_j|=1}
\left(\sum_j\varepsilon_jv_j\right)^*M_r^{-1}
\left(\sum_j\varepsilon_jv_j\right).
\]

**Step 3: all phases are determined.** For \(0<r\le 1/2\), the three off-diagonal real inner products are
\[
\begin{aligned}
A&=v_0^\mathsf{T}M_r^{-1}v_1=2r^3(1+r)>0,\\
-B&=v_0^\mathsf{T}M_r^{-1}v_2=-r^2(1+r)^2<0,\\
C&=v_1^\mathsf{T}M_r^{-1}v_2
=\frac{r(1+r)^2(1-2r^2)}{1-r}>0.
\end{aligned}
\]
Fixing \(\varepsilon_0=1\) and optimizing \(\varepsilon_2\) leaves, apart from diagonal terms and an overall factor two, the one-dimensional objective
\[
F(t)=At+\sqrt{B^2+C^2-2BCt},\qquad -1\le t\le1.
\]
It is strictly concave. The exact factorization
\[
BC-A(B+C)=r^3(1+r)^3(1-2r)(1+2r)\ge0
\]
implies \(F'(-1)=A-BC/(B+C)\le0\). Hence \(F\) has its unique maximum at \(t=-1\). The maximizing phases are therefore, uniquely up to common phase, \((\varepsilon_0,\varepsilon_1,\varepsilon_2)=(1,-1,-1)\). It follows that
\[
\max\frac{T_r(u)^2}{u^*M_ru}
=(v_0-v_1-v_2)^\mathsf{T}M_r^{-1}(v_0-v_1-v_2)
=\frac{2(1+r)}{1-r}\big(1+2r^2(1-r)^2\big).
\]
Moreover, the Hilbert extremal vector is proportional to
\[
M_r^{-1}(v_0-v_1-v_2)
=(1-r^2)\big(1+2r^2,-(1+4r)\big)^\mathsf{T}.
\]
This corresponds to \(f_r\) as stated. For \(0<r\le1/2\), its two combinations
\[
2ra+b=4r^3-2r-1<0,\qquad ra+b=2r^3-3r-1<0
\]
are strictly negative. Therefore the coefficient triangle inequality in Step 1 is attained, so the derived majorant is the actual Wiener norm. Uniqueness in the strict dual phase optimization and equality in Hilbert Cauchy–Schwarz give precisely the claimed extremizers.

**Step 4: the zero-pole endpoint.** At \(r=0\), the space consists of \(f(z)=a+bz\), for which ordinary two-term Cauchy–Schwarz gives \(\|f\|_W\le\sqrt2\|f\|_{H^2}\), with equality exactly when \(|a|=|b|>0\). Substitution of \(r=1/2\) in the general expression gives the claimed value \(3\sqrt3/2\).

## Verification

The accompanying standalone `checker.py` uses exact symbolic arithmetic to verify the two-by-two Gram inverse, the three pairwise inner products, the factorization controlling the phase maximum, the explicit Riesz extremizer and the closed-form constant. Five rational parameter values are additionally checked using exact Taylor-coefficient identities and the equality condition. Run using `python checker.py` with SymPy available. These finite checks are supplemental to, not substitutes for, the proof above.

## Relationship to prior work

Baranov and Zarouf (2023) proved a nonsharp general bound for the Wiener-to-Hardy embedding on rational functions with controlled poles. Auxemery, Borichev and Zarouf (2026, arXiv:2603.03908, first public March 4) established that bound's asymptotic order as rational degree grows, using powers of Blaschke factors for their test functions. Their theorems concern uniform estimates and the large-degree limit, not the exact constant and equality cases of the fixed two-dimensional double-pole model space. The present result provides a direct sharp finite-dimensional calculation, including a natural boundary in the pole-radius parameter. Earlier exact formulas for this particular subspace were not identified in the sources examined; this is not a claim of exhaustive bibliographic uniqueness.

## Limitations

The result is established only for real \(0\le r\le1/2\). Although rotations relate complex pole positions of equal modulus, no claim is made here about all distinct-pole spaces, the full degree-two rational class, or the regime \(r>1/2\), where the phase-maximizing pattern can change. All proofs and checks were performed within one review process; independent mathematical audit has not been performed.

## References

1. B. Auxemery, A. Borichev and R. Zarouf, *Asymptotic sharpness of a Nikolskii type inequality for rational functions in the Wiener algebra*, arXiv:2603.03908 (first public 2026-03-04), https://arxiv.org/abs/2603.03908.
2. A. Baranov and R. Zarouf, *H-infinity interpolation constrained by Beurling-Sobolev norms*, Moroccan Journal of Pure and Applied Analysis **9** (2023), 157–167, https://doi.org/10.2478/mjpaa-2023-0012.
