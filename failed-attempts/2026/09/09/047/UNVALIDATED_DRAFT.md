# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified route-separation for the base-15 symmetric Cantor product:
# axial spike law + digit-energy obstruction to the vanilla transfer

## 1. Objects

Let $b=15$, $D=\\{0,1,2,13,14\\}=\\{0,\\pm 1,\\pm 2\\}\\bmod 15$,
$C\\subset[0,1]$ the attractor of $x\\mapsto(x+d)/15$, $d\\in D$,
$\\nu$ the uniform self-similar probability measure on $C$
(weights $1/5$), $\\mu=\\nu\\times\\nu$ on $E=C\\times C\\subset\\mathbb R^2$.
The five first-generation intervals are disjoint, so by Hutchinson/Moran
$\\dim_H C=\\log 5/\\log 15\\approx 0.59432$ and
$\\dim_H E=s_0=2\\log 5/\\log 15\\approx 1.18863<5/4$.
Write $A(R)=\\int_{S^1}|\\hat\\mu(R\\omega)|^2\\,d\\sigma(\\omega)$
(normalised circular mean) and
$M_1=\\int_0^\\infty A(R)^2 R\\,dR$ for the Liu--Mattila integral whose
finiteness is equivalent (Liu 2018, $L^2$-identity) to finiteness of
$\\int\\|d^x_\\*\\mu\\|_{L^2(dr)}^2\\,d\\mu(x)$.

The Fourier multiplier is exact:
$$m(\\xi)=\\tfrac15\\sum_{d\\in D}e^{-2\\pi i d\\xi}
=\\tfrac15\\bigl(1+2\\cos2\\pi\\xi+2\\cos4\\pi\\xi\\bigr),\\qquad
\\hat\\nu(\\xi)=\\prod_{j\\ge 1}m(\\xi/15^j),\\qquad
\\hat\\mu(\\xi_1,\\xi_2)=\\hat\\nu(\\xi_1)\\hat\\nu(\\xi_2).$$

## 2. Theorem (route separation, certified)

**(i) Axial spike law.** With $c_0=|\\hat\\nu(1)|^2\\approx 0.67356406$
(computed; rationally certified $c_0>0.4576$),
exact self-similarity gives $\\hat\\nu(15n)=\\hat\\nu(n)$ for all
$n\\in\\mathbb Z$, hence $|\\hat\\nu(15^k)|^2=c_0$ for every $k\\ge 0$.
A $2\\pi$-Lipschitz argument ($\\operatorname{supp}\\nu\\subset[0,1]$)
then certifies
$$A(15^k)\\ \\ge\\ 0.003/15^k\\qquad\\forall k\\ge 0.$$
Numerically $A(15^k)\\approx 15^{-0.93k}$ (effective exponent
$\\gamma_{\\mathrm{eff}}\\approx 0.93<1$), while Liu's averaged-decay
conditional needs $\\gamma>1$. The vanilla averaged-decay route is
therefore provably unclosable on the spike sequence, at every scale.

**(ii) Digit-energy obstruction.** Let $N(p)=\\#\\{(x,y)\\in D^2:x+y=p\\}$
and $E_1=\\sum_p N(p)^2$ (additive energy of one digit). Exact integer
count gives $E_1=65$, versus the random-heuristic closure budget
$5^4/15=125/3\\approx 41.67$:
$$E_1=65>125/3,\\qquad E_1/(125/3)=39/25=1.56.$$
The excess is caused by the AP $\\{0,1,2\\}\\subset D$ and the symmetric
pair. At deeper levels $E_2=5265$ (budget $(125/3)^2$, excess $3.03$)
and $E_3=438945$ (budget $(125/3)^3$, excess $6.07$): the shortfall
GROWS with $k$, so no multiscale vanilla Bourgain--Demeter + Liu--Pham
closure can recover — the obstruction is structural, not a one-level
accident.

**(iii) No-atom lemma.** $\\mu$ is Ahlfors $s_0$-regular
($s_0>0$; crude Frostman constant $C=625$), so
$d^x_\\*\\mu(\\{0\\})=\\mu(\\{x\\})=0$ for every pin $x$. The
obstruction bites on $(0,\\infty)$, i.e. inside the pinned-$L^2$ regime,
not at a removable atom.

**Interpretation.** (i)--(iii) jointly certify WHY the vanilla
full-partition Bourgain--Demeter + Liu--Pham transfer provably breaks on
this product's axial/arithmetic structure, redirecting future attacks to
genuinely digit-restricted (fractal) decoupling. This is a route-separation
result, not a bound on $\\dim\\Delta_x(E)$ itself.

## 3. Proof sketches (full details + certificates in artifacts)

*Resonance.* $m(n)=1$ for $n\\in\\mathbb Z$ since all $d\\in D$ are
integers; the product for $\\hat\\nu(15n)$ shifts by one factor
$m(n)=1$. Verified numerically to 8 digits for $n\\in\\{1,2,7,100\\}$.

*Rational $c_0$ bound.* $m(1/15)\\ge 0.8245$ via
$\\cos t\\ge 1-t^2/2$ with $\\pi\\le 3.1416$; tail
$\\prod_{j\\ge 2}(1-12\\pi 15^{-j})>0.82$ via $|m(u)-1|\\le 12\\pi|u|$
(mean digit $\\le 6$) and $\\prod(1-a_j)\\ge 1-\\sum a_j$.
Hence $|\\hat\\nu(1)|>0.676$, $c_0>0.4576$ (machine value $0.67356$).

*Spike width.* On $|\\theta|\\le\\delta/R$,
$|R-R\\cos\\theta|\\le\\delta^2/(2R)\\le\\delta^2/2$ and
$|R\\sin\\theta|\\le\\delta$; Lipschitz bounds give both factors
$\\approx c_0$, $\\approx 1$. Angular fraction $2\\delta/(2\\pi R)$
times the peak product yields $A\\ge c_\\*/R$ with
$c_\\*=0.003$ at $\\delta=0.05$ (all rational; see `proofs_cert.py`).

*Energy counts.* Direct $25$-pair enumeration (exact integers);
$E_2,E_3$ by deterministic brute force over $25^2,125^2$ pairs.

*Frostman constant.* Generation-$k$ squares: side $15^{-k}$, mass
$25^{-k}=15^{-ks_0}$; a ball of radius $r$ meets $\\le 25$ squares with
$15^{-k}\\le 15r$, giving $\\mu(B)\\le 25(15r)^{s_0}=625\\,r^{s_0}$.

## 4. Reproduction

- `proofs_cert.py` (stdlib only): prints all exact counts, rational
  bounds, and `ALL CERTIFICATES PASS`. Asserts: $E_1=65$,
  $E_2=5265$, $E_3=438945$, $c_\\*>0.003$.
- `numerics.py` (needs numpy): recomputes $c_0$ and $A(15^k)$,
  $k=0..3$: $0.252611$, $0.061708$, $0.006722$, $0.000990$;
  $R\\cdot A$ grows $0.25\\to 3.34 ($\\gamma_{\\mathrm{eff}}<1$).

## 5. What is NOT claimed

Finiteness or infinitude of $M_1$ (hence the target pinned-$L^2$ bound
and its negation) is NOT proved: log-block masses
$I_0..I_3=0.150/0.186/0.344/0.807$ grow but spike widths $w_k$ are
unresolved, and $M_1(1..60000)\\approx 0.49$ looks convergent. The claim
is exactly the route separation above. All prior sources (Liu; Du et
al.; 5/4 repair; Fraser--Pham; Li--Liang--Shen) state only upper bounds
or thresholds and contain no such lower-bound certificate for this
window (admission scan).
