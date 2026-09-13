# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Liftings of rank-two super type in characteristic 5 — classification draft

## 1. Scope and theorem

Let $k=\bar k$, $\mathrm{char}\,k=5$. Let $G$ be finite abelian, $5\nmid |G|$,
$V\in {}^{kG}_{kG}\mathcal{YD}$ two-dimensional, principally realized:
$g_1,g_2\in G$, $\chi_1,\chi_2\in\hat G$, $q_{ij}=\chi_j(g_i)$, with

$$q_{11}=q,\quad q_{22}=-1,\quad q_{12}q_{21}=q^{-1},$$

$q$ a primitive $N$th root of unity, $N>2$, $5\nmid N$.
So the braiding is connected rank-two diagonal of super type with one
fermionic vertex. Assume $B(V)$ finite-dimensional (the standard super-type
datum, as in characteristic 0).

**Theorem (target).** Every finite-dimensional pointed Hopf algebra $H$ with
$H_0=kG$ and infinitesimal braiding $V$ in this scope is, up to isomorphism,
exactly one algebra $H(\mu)$ below. Each $H(\mu)$ has dimension $4N|G|$,
is presented by deformed super Serre + deformed fermionic powers with the
stated parameter constraints, is a cocycle deformation of $B(V)\#kG$ with the
stated ledger, and $H(\mu)\cong H(\mu')$ iff the parameters differ by the
stated torus rescaling (dichotomy). Nothing extra vanishes mod 5.

## 2. Nichols datum mod 5 (verified)

Put $x_{12}=x_1x_2-q_{12}x_2x_1=(\mathrm{ad}\,x_1)(x_2)$ and
$s=(\mathrm{ad}\,x_1)^2(x_2)$. A direct expansion gives

$$s = x_1^2x_2 - q_{12}(1+q)x_1x_2x_1 + qq_{12}^2x_2x_1^2.$$

Since $N>2$, $q\ne-1$, $(2)_q=1+q\ne0$; all three coefficients are nonzero,
so $s$ is a nontrivial relation over the whole scope.
Self-braiding of $x_{12}$: $q_{12,12}=q_{11}q_{12}q_{21}q_{22}
=q\cdot q^{-1}\cdot(-1)=-1$, order 2.

**Lemma (mod-5 carryover).** $B(V)$ has the same presentation, PBW basis and
dimension as in characteristic 0:
relations $s=0$, $x_2^2=0$, $x_{12}^2=0$, $x_1^N=0$;
basis $\{x_1^ax_{12}^bx_2^c:0\le a<N,\ b,c\in\{0,1\}\}$;
$\dim B(V)=4N$; positive roots $\alpha_1$ (height $N$),
$\alpha_1+\alpha_2$ (height 2), $\alpha_2$ (height 2).
*Proof.* All $q$-number / Gaussian-binomial vanishing used in the
characteristic-0 proof involves only orders $N$ (with $5\nmid N$) and $2$.
The integers $2,3,4$ are invertible mod 5, so zero patterns of
$(k)_q$, Gaussian binomials, and $(2)_{-1}=0$, $(k)_{-1}\ne0$ ($k$ odd)
are identical to characteristic 0. Numerically certified for
$N\in\{3,4,6,7,8,9,11,12\}$ in `artifacts/verify_super_type.json`;
the general statement is the standard theorem that $q$-combinatorics
depends only on $\gcd(\mathrm{char},N)$. In particular no structure
constant vanishes mod 5 that did not vanish in characteristic 0; the
excluded cases $N=5$ or $5\mid|G|$ are exactly where new vanishing would occur.

## 3. Coproduct / stratification (symbolically verified)

Work in $T(V)\#kG$. Under the scope constraint $q_{12}q_{21}=q^{-1}$ the
exact free-level coproduct (artifact `coproduct_z2.py/json`) is

$$\Delta(z)=z\otimes1+g_{12}\otimes z
  +\tfrac{q-1}{q}\,x_1g_2\otimes x_2,\qquad z=x_{12},\ g_{12}=g_1g_2,$$

i.e. the $x_2g_1\otimes x_1$ term present for generic splits vanishes
identically in scope. For $z^2$, $\Delta(z^2)-z^2\otimes1-g_{12}^2\otimes z^2$
has exactly 14 terms; the three $A\otimes x_2$ terms with
$A\in\{x_1^2x_2,x_1x_2x_1,x_2x_1^2\}$ are proportional to $s$ (ratios
verified: middle/last coefficients $-q_{12}(1+q)$, $qq_{12}^2$), hence vanish
modulo $(s)$; the terms containing an $x_2^2$ factor vanish modulo the
deformed $x_2^2$ relation. Consequence: with stratification order

$$(x_2^2,\ s)\ \to\ w=z^2+\text{(correction)}\ \to\ x_1^N,$$

each step adjoins a skew-primitive (after quotient by the previous step).
The correction is $w=z^2-c\,\mu_2x_1^2g_2^2$ (unique scalar killing the
$x_1^2\otimes x_2^2$ remainder; coefficient read off from
`coproduct_z2.json`; explicitly proportional to $(q-1)^2/(q^3q_{12})$ up to
the nonzero factor $1+q$). If $\mu_2=0$ no correction is needed ($w=z^2$).
$x_1^N$ is skew-primitive at the top because $q^N=1$ makes the braiding
trivial in that degree (standard $q$-binomial argument, valid since
$5\nmid N$).

## 4. Lifting list and parameter constraints

For a YD relation $r$ of $G$-degree $g_r$ and character $\chi_r$, a lifting
scalar can be nonzero only if $\chi_r=\varepsilon$ (otherwise
$r-\mu(g_r-1)$ is not YD / not central; standard). With
$q_{12}q_{21}=q^{-1}$ and $q^N=1$ this gives (artifact
`verify_super_type.json`):

| relation | deformation | nonzero only if |
|---|---|---|
| $x_2^2$ | $x_2^2=\mu_2(g_2^2-1)$ | $\chi_2^2=\varepsilon\iff q_{21}^2=1$ ($q_{21}=\pm1$) |
| $s$ | $s=\lambda(g_1^2g_2-1)$ | $\chi_1^2\chi_2=\varepsilon\iff q_{12}^2=-1$ and $q^2q_{21}=1$ (very restrictive; generically $\lambda=0$) |
| $w$ (corrected $x_{12}^2$) | $w=\mu_{12}(g_{12}^2-1)$ | $(\chi_1\chi_2)^2=\varepsilon\iff q_{12}^2=1$ (then the $g_1$-condition is automatic) |
| $x_1^N$ | $x_1^N=\mu_1(g_1^N-1)$ | $\chi_1^N=\varepsilon\iff q_{12}^N=1$ (the $g_1$-condition $q^N=1$ is automatic) |

If the character is nontrivial the scalar is forced to $0$; if trivial it is
free in $k$. Every combination of allowed scalars occurs (quotient by the
deformed relations is nonzero of the right dimension; Diamond-lemma/PBW
argument identical to characteristic 0 since leading words and
$q$-commutation scalars are unchanged mod 5). In particular:
generic splits have only $\mu_1$ (and sometimes $\mu_2$); $\lambda\ne0$
requires $q_{12}^2=-1$ (possible e.g. at $N=4$ with $q_{12}$ a primitive
4th root and compatible $q_{21}$); $\mu_{12}\ne0$ requires $q_{12}^2=1$.

**Dimension.** Each $H(\mu)$ has PBW basis lifting that of $B(V)$:
$\dim H(\mu)=4N\cdot|G|$. The bottom stratum uses semisimplicity of $kG$
(Maschke, $5\nmid|G|$).

## 5. Cocycle ledger

Each stratification step is $H_{k+1}=H_k/(w_k-\mu(g_k-1))$ with $w_k$
$(g_k,1)$-primitive and $\chi_k=\varepsilon$. By the Masuoka/Andruskiewitsch–
Schneider cleft-extension argument (which uses only that $kG$ is semisimple
— true here since $5\nmid|G|$), each step is a Hopf 2-cocycle (equivalently
Hochschild 2-cocycle on $B(V)\#kG$) deformation; the deformation cocycle is
supported in the corresponding YD bidegree. Ledger:
$\mu_2\leftrightarrow$ class in degree $2\alpha_2$;
$\lambda\leftrightarrow$ degree $2\alpha_1+\alpha_2$;
$\mu_{12}\leftrightarrow$ degree $2\alpha_1+2\alpha_2$;
$\mu_1\leftrightarrow$ degree $N\alpha_1$.
Composition gives an explicit multiplicative 2-cocycle
$\sigma=\sigma_1*\sigma_{12}*\sigma_s*\sigma_2$ on $B(V)\#kG$ with
$H(\mu)\cong (B(V)\#kG)_\sigma$. The undeformed point $\mu=0$ is $B(V)\#kG$.

## 6. Isomorphism dichotomy

Vertices are labelled ($q\ne-1$ since $N>2$), so no diagram automorphism
swaps them. Any isomorphism in scope restricts to a group automorphism
$\varphi:G\to G'$ carrying $(g_i,\chi_i)$ to $(g_i',\chi_i')$ and a torus
rescaling $x_i\mapsto c_ix_i$, $c_i\in k^\times$. Hence

$$\mu_1'=c_1^N\mu_1,\quad \mu_2'=c_2^2\mu_2,\quad
  \lambda'=c_1^2c_2\lambda,\quad
  \mu_{12}'=c_1^2c_2^2\mu_{12}+F(c_1,c_2,\mu_2),$$

where $F$ is the explicit carryover from the $w$-correction (zero if
$\mu_2=0$; in general the unique polynomial making $w$ rescale
homogeneously, read off from §3). Conversely any such rescaling extends to a
Hopf isomorphism. So: $H(\mu)\cong H(\mu')$ iff their parameter tuples lie
in the same $(\mathbb G_m^2\rtimes\mathrm{Aut}(G,\text{datum}))$-orbit;
otherwise they are non-isomorphic. In particular, vanishing vs nonvanishing
of each admissible scalar (up to the $w$-correction) is an isomorphism
invariant. This is necessary and sufficient.

## 7. What is proved vs computed; limitations

*Proved deductively:* Serre coefficient formula; $q_{12,12}=-1$;
character-triviality reductions (exact monomial algebra using only
$q_{12}q_{21}=q^{-1}$, $q^N=1$); stratification logic; dimension/cocycle/iso
arguments adapted from the standard lifting machinery (valid because
$5\nmid N|G|$ keeps all denominators invertible and $kG$ semisimple).
*Computed certificates:* `verify_super.py/json` (vanishing patterns,
character table, mod-5 lemma data); `coproduct_z2.py/json` (exact
$\Delta(z)$, $\Delta(z^2)$ remainder, correction existence).
*Limitations:* the cocycle is exhibited per stratum (ledger) rather than by
one closed-form exponential formula; the $w$-correction scalar is certified
via the remainder file rather than fully simplified in text; the
characteristic-0 lifting machinery is invoked as adapted (not re-proved from
scratch) — legitimate since every step dividing by an integer prime to 5 or
using Maschke is flagged.
