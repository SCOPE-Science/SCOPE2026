# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Index-certified non-meridional closed-geodesic window on the triaxial
ellipsoid (1, 23/20, 27/20), beating the revolution-meridian bound

## 1. Statement

Let

$$E = \left\{(x,y,z)\in\mathbb R^3 : x^2 + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1\right\},
\qquad b=\tfrac{23}{20}=1.15,\;\; c=\tfrac{27}{20}=1.35.$$

Let $\gamma$ be the closed curve $E\cap\{z=0\}$, i.e. the ellipse with
semiaxes $(1,b)$ in the $xy$-plane, and let $M$ be the length of the ellipse
with semiaxes $(1,c)$ (the $y=0$ meridian section, equivalently the meridian
of the comparison surface of revolution obtained by rotating that section
about the $z$-axis).

**Theorem.** *$\gamma$ is a closed geodesic of $E$, it is non-meridional
with respect to the comparison meridian foliation, and:*

1. *(length window)*
   $$L(\gamma)\in [L_{\mathrm{lo}},L_{\mathrm{hi}}]
     \subset [6.762645991830,\; 6.762645991830],$$
   *with relative width $(L_{\mathrm{hi}}-L_{\mathrm{lo}})/L_{\mathrm{lo}}
   \le 2.9\times 10^{-14} \le 0.5\%$;*
2. *(Morse index)* *the (based-loop) Morse index of $\gamma$ is exactly
   $1$, and the free-loop (periodic) Morse index of $\gamma$ is exactly $1$
   (in particular $\gamma$ is unstable);*
3. *(beating margin)*
   $$M \in [7.423740780724,\; 7.423740781354],\qquad
     \frac{M_{\mathrm{lo}}-L_{\mathrm{hi}}}{M_{\mathrm{hi}}}\ge 0.08905,$$
   *so the loop beats the revolution-meridian bound by at least $8.9\%$,
   well above the $2\%$ target.*

*All bounds are rigorous: they are proved by exact rational arithmetic
(plus integer square roots) in the accompanying stdlib-only script
`artifacts/certify_window.py`, which replays in seconds and prints PASS for
each of the checks T1–T6.*

## 2. Why the loop is an exact closed geodesic (no shooting defect)

The map $\sigma(x,y,z)=(x,y,-z)$ is an isometry of $E$. Its fixed-point set
is $E\cap\{z=0\}$, a smooth embedded closed curve. A connected component of
the fixed-point set of an isometry is totally geodesic; a closed,
constant-speed parametrisation of it is therefore a closed geodesic. Hence
$\gamma$ is *exactly* closed — there is no shooting/closure defect to
enclose. The meridian foliation of the comparison surface of revolution
(rotating the $y=0$ section about the $z$-axis) is transverse to the plane
$z=0$ along $\gamma$ (except at isolated points), so $\gamma$ is
non-meridional in the sense of the target claim.

## 3. Rigorous length enclosure (exact rational arithmetic)

Ellipse perimeters are complete elliptic integrals of the second kind:
for semiaxes $0<p<q$ with $m=1-p^2/q^2$,

$$P(p,q) = 4\,q\,E(m),\qquad
  E(m)=\frac{\pi}{2}\Bigl[1-\sum_{n\ge 1}
  \frac{\binom{2n}{n}^2}{16^n}\,\frac{m^n}{2n-1}\Bigr].$$

The proof uses only the following rigorous, exactly-computed ingredients:

- $\pi$ via Machin's formula $\pi=16\arctan\frac15-4\arctan\frac1{239}$
  with Leibniz alternating-series remainders (window width $\approx
  8.8\times 10^{-14}$);
- truncation of the $E$-series at $N=25$ with the explicit tail bound
  $m^{N+1}/((2N+1)(1-m))$, valid because every coefficient satisfies
  $\binom{2n}{n}^2/16^n\le 1$ (since $\binom{2n}{n}\le 4^n$);
- all operations in exact rational arithmetic (`Fraction`), so every
  printed window rigorously contains the true value.

This gives the windows quoted in §1: $L$ for $(p,q)=(1,23/20)$ and $M$ for
$(p,q)=(1,27/20)$. Since $m_L=129/529$ and $m_M=329/729$ are well inside
$(0,1)$, the series and tail bounds apply directly. Check T6 additionally
confirms the crude circle sandwich $2\pi < L < 2\pi b$.

## 4. Morse index exactly 1 (Sturm comparison + Wirtinger)

Along the $z=0$ ellipse the Gaussian curvature of $E$ is exactly

$$K(s)\in [K_{\min},K_{\max}],\qquad
  K_{\min}=\frac{a^2}{b^2c^2}=\frac{160000}{385641}\approx 0.41489,\;\;
  K_{\max}=\frac{b^2}{a^2c^2}=\frac{529}{729}\approx 0.72565.$$

Indeed, on a principal ellipse the curvature attains its extrema at the
vertices, with the stated values (verified by direct computation; the script
uses only these two endpoint values). Square roots are enclosed rigorously
by integer arithmetic: for a positive fraction $f=p/q$,
$\lfloor\sqrt{pq}\rfloor/q \le \sqrt f \le (\lfloor\sqrt{pq}\rfloor+1)/q$.

Let $d_1 < d_2$ be the first two conjugate distances along $\gamma$ (zeros
of the normal Jacobi field with $y(0)=0$, $y'(0)=1$, satisfying
$y''+K(s)y=0$). Classical Sturm comparison with the constant-coefficient
equations $y''+K_{\min}y=0$ and $y''+K_{\max}y=0$ gives

$$d_1\in\left[\tfrac{\pi}{\sqrt{K_{\max}}},\tfrac{\pi}{\sqrt{K_{\min}}}\right]
  \subset [3.682027,\,4.877323],\qquad
  d_2\in\left[\tfrac{2\pi}{\sqrt{K_{\max}}},\tfrac{2\pi}{\sqrt{K_{\min}}}\right]
  \subset [7.364055,\,9.754645].$$

Since $d_{1,\mathrm{hi}} = 4.877323\ldots < 6.762645991830 \le L_{\mathrm{lo}}$
(gap $\approx 1.885$), there is at least one conjugate point in $(0,L)$:
the based-loop index is $\ge 1$. Since
$d_{2,\mathrm{lo}} = 7.364055\ldots > L_{\mathrm{hi}}$ (gap $\approx 0.601$),
there is at most one: the based-loop index is exactly $1$. The script checks
both strict inequalities as T3 and T4.

For the free-loop (periodic) index: the constant normal test field has
negative second variation $\int (0-K\cdot 1)\,ds<0$ since $K>0$, so the
periodic index is $\ge 1$; and because $L < 2\pi/\sqrt{K_{\max}}$ (checked
as $54\pi/23 > L_{\mathrm{hi}}$, same gap $\approx 0.61$), the sharp
Wirtinger/Poincaré inequality gives nonnegativity of the index form on the
mean-zero subspace, so the periodic index is $\le 1$. Hence the free-loop
Morse index of $\gamma$ is exactly $1$: the loop is unstable, as certified.

## 5. Beating the revolution-meridian bound

The comparison value $M$ is exactly the meridian length of the revolution
spheroid generated by the $y=0$ section, hence a fortiori an upper bound
for the shortest meridian of any admissible comparison. The certified
conservative margin (check T2, strict window separation T5) is

$$\frac{M_{\mathrm{lo}}-L_{\mathrm{hi}}}{M_{\mathrm{hi}}}
  \;\ge\; 0.08905 \;>\; 0.02,$$

i.e. at least $8.9\%$, more than four times the required $2\%$.

## 6. Replay

```
python3 artifacts/certify_window.py
```

Stdlib only (`fractions`, `math`), seconds. Expected output: T1–T6 all PASS
and `ALL CHECKS PASS`, with the windows above.

## 7. Limitations and honest scope

- The certified loop is the symmetric principal ellipse $z=0$, not an
  asymmetric generic orbit; its closedness comes from the reflection
  isometry, which is exactly why the certificate is fully rigorous rather
  than a floating-point shooting log. It is non-meridional in the stated
  comparison sense, but symmetric.
- The index proof uses only scalar Sturm comparison along the loop (no
  PDE eigenvalue enclosure is needed); stability information beyond the
  index (e.g. nullity, bifurcation diagram) is not addressed.
- The certificate covers the single named ellipsoid $(1,23/20,27/20)$,
  not the full window $[1.1,1.2]\times[1.3,1.4]$; extension to the box
  would require uniform (interval) versions of the same estimates.
- Originality claim is the narrow certified datum (window + proved index +
  beating margin on this named ellipsoid, plus the exact-arithmetic
  template), not a new general theorem; prior algebraic/density theory
  (Fedorov, Abenda, Dragović–Radnović) and Jacobi numerics (Karney) contain
  no such index-certified window.
