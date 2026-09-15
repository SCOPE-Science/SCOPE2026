# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Odd-dimensional Chekanov-type tori: divisor-bulk no-go theorem

## 1. Statement

Let $n = 2m+1 \geq 3$ be odd, $X = (\mathbf{CP}^1)^n$ with each factor of area $1$,
and $\Theta^n_s \subset X$, $s \in (1/2,1)$, the Chekanov-type torus of Vianna
(arXiv:1603.02006, Definition 4.2). Let the spin structure be the one for which
every Maslov-2 holomorphic disk counts positively (Proposition 4.5), and let
$b = T^{\rho}\sum_{i=1}^n l_i h_i \in H^2(X,\Lambda_+)$, $\rho > 0$, be any
uniform-valuation divisor bulk ($h_i$ Poincar\'e dual to $\{y_i = 0\}$).
Write the bulk-deformed disk potential as in Vianna Proposition 5.1.
Then:

**Theorem (odd-$n$ divisor-bulk no-go).** Every critical point
$(u,w_1,\dots,w_{n-1}) \in (\Lambda_0^\times)^n$ of the bulk-deformed potential
$PO^{b}_{\Theta^n_s}$ satisfies $\mathrm{val}(u) = 1/2$. In particular there is
no critical point with $\mathrm{val}(u) = s > 1/2$, i.e.\ no weak bounding
cochain $b_{\mathrm{vec}} \in H^1(\Theta^n_s,\Lambda_0)$ with $z_\beta = T^s\times
\mathrm{unit}$ critical for $PO^b$, for any choice of $\rho > 0$ and any
integers (indeed any scalars) $l_i$. Hence the Fukaya–Oh–Ohta–Ono
bulk-plus-$H^1$-cochain route of Vianna Sections 2/5 (Corollary 2.8) cannot
produce $HF(\Theta^n_s,(b,b_{\mathrm{vec}});\Lambda_{0,nov}) \cong
H^*(\Theta^n_s)$ for any $s \in (1/2,1)$.

## 2. Potential and bulk family

With $u = z_\beta$, $w_i = z_{\alpha_i}$, $z_{H_i} = T$, Vianna Proposition 4.5 gives
$$PO = u + \frac{T}{u}(1+w_1+\cdots+w_{n-1})(1+w_1^{-1}+\cdots+w_{n-1}^{-1}).$$
The relative classes $\beta,\alpha_j$ do not meet $\{y_k = 0\}$, while
$H_i - \beta - \alpha_i + \alpha_j$ meets $\{y_k = 0\}$ iff $k = i$ with
multiplicity one. Hence a divisor bulk $b = T^\rho\sum l_i h_i$ multiplies the
monomial $T w_j/(u w_i)$ (convention $w_n = 1$) by the unit
$\exp(l_i T^\rho) = 1 \bmod \Lambda_+$. Every uniform-valuation divisor bulk is
covered by Vianna's parametrization
$b = T^\rho[(k_1+k_n)h_1+\cdots+(k_{n-1}+k_n)h_{n-1}+k_n h_n]$
(take $k_n = l_n$, $k_i = l_i - l_n$). The bulk-deformed potential is
$$PO^b = u + \frac{T}{u}\sum_{i,j} c_{ij}\frac{w_j}{w_i},\quad
c_{ij} = e^{(k_i\text{-type})T^\rho} = 1 \bmod \Lambda_+,$$
in factored form
$$PO^b = u + \frac{T}{u}(1+w_1+\cdots+w_{n-1})
  \left(b_n + \frac{b_1}{w_1} + \cdots + \frac{b_{n-1}}{w_{n-1}}\right)$$
up to the harmless overall unit, with $b_i = e^{k_i T^\rho}$.

## 3. Critical points (Vianna Lemma 5.2)

Write $b_i = e^{k_iT^\rho}$. Differentiating in $w_i$ and multiplying by $w_i$,
$$ (i):\quad w_i + \sum_{j\ne i}\frac{b_j w_i}{w_j}
   - b_i\left(\frac{1}{w_i}+\sum_{j\ne i}\frac{w_j}{w_i}\right)\cdot
   (\text{common }u\text{-independent factor}) = 0,$$
i.e.\ equation (5.1) of Vianna. Summing and setting
$L = \sum_{i=1}^{n-1} w_i = \sum b_i/w_i$ at a critical point, Vianna derives
$$w_i - \frac{b_i}{w_i}(1+L) = 0,\qquad
  1 - \frac{b_n T}{u^2}(1+L)^2 = 0.$$
Hence every critical point has the form
$$w_i = \epsilon_i e^{k_iT^\rho/2},\qquad
  u = \epsilon_n e^{k_nT^\rho/2}T^{1/2}\Bigl(1+\sum_{i=1}^{n-1}
      \epsilon_i e^{k_iT^\rho/2}\Bigr),\quad \epsilon_i = \pm 1.$$
The derivation uses only the factored form and holds for every $\rho > 0$ and
every choice of parameters.

## 4. Parity forces valuation $1/2$

Put $S = \sum_{i=1}^{n-1}\epsilon_i e^{k_iT^\rho/2}$.
Since $e^{k_iT^\rho/2} = 1 \bmod \Lambda_+$,
$$S = \Bigl(\sum_{i=1}^{n-1}\epsilon_i\Bigr) \bmod \Lambda_+.$$
Because $n = 2m+1$ is odd, $n-1 = 2m$ is even, so $\sum_{i=1}^{n-1}\epsilon_i$
is an even integer (between $-2m$ and $2m$). Therefore
$$1 + S = \bigl(1 + \text{even integer}\bigr) \bmod \Lambda_+
        = \text{odd integer} \bmod \Lambda_+,$$
in particular a nonzero integer plus positive-valuation terms: a unit of
$\Lambda_0$ (valuation $0$). Consequently
$$\mathrm{val}(u) = \tfrac12 + \mathrm{val}(1+S) = \tfrac12$$
for every one of the $2^{\,n-1}$ sign patterns, every $\rho > 0$, every
parameter tuple. Exhaustive check for $n=3,5,7$ in
`output/artifacts/no_go_odd.py` (all $2^{n-1}$ patterns) and the refined
leading-order check in `output/artifacts/leading_order_no_go.py` confirm this.

A weak bounding cochain with $u = z_\beta = T^s\times\mathrm{unit}$ requires
$\mathrm{val}(u) = s > 1/2$ — impossible. By Vianna Corollary 2.8, vanishing of
$m_1^{b,b}|_{H^1}$ (hence $HF \cong H^*$) is equivalent to criticality, so no
pair $(b,b_{\mathrm{vec}})$ in this family yields non-vanishing Floer
cohomology. Higher-Maslov disks do not affect the criterion: $m_1^{b,b}$ on
$H^1$ counts only Maslov-2 disks for degree reasons (proof of Corollary 2.8),
and Proposition 4.10 confirms higher-Maslov disks have area $\geq 1-s$ with
equality only at Maslov 2.

## 5. Scope and remarks

* Strictly $s \in (1/2,1)$: at the monotone point $s = 1/2$ one has
  $\mathrm{val}(u) = 1/2 = s$, so critical points do exist — the no-go is
  specific to the non-monotone range of the target.
* Fixed $+1$ spin structure of Proposition 4.5 and uniform-valuation divisor
  bulks (the full family of Vianna Section 5). This is exactly the route that
  proves the even-dimensional theorem; the parity argument shows it cannot
  extend to odd $n$.
* This does not resolve displaceability of $\Theta^n_s$ (either horn); it is a
  proved obstruction for one natural proof family, explaining why Vianna's
  Question 1.2 remains open and forcing future attacks toward displacement
  constructions or non-FOOO methods.

## 6. Verification

* `output/artifacts/no_go_odd.py`: all sign patterns for $n=3,5,7$ give
  $1+S$ odd/nonzero, i.e.\ $\mathrm{val}(u) = 1/2$; spin-flip variant checked.
* `output/artifacts/leading_order_no_go.py`: leading-order unit analysis.
* Sources: Vianna arXiv:1603.02006 Proposition 4.5, Lemma 5.2, Lemma 5.3,
  Proposition 4.10, Corollary 2.8; FOOO Theorem 2.4/2.5 cited therein.
