# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Twisted-sector-corrected genus-one quasimap wall-crossing for non-convex CY3 orbifolds, with X7 nonvanishing and correction coefficients

## 1. Setting (from the admitted target's own sources)

Let $X\subset \mathbf P(\vec w)$ be a smooth Calabi–Yau threefold complete intersection
$V(F_1,\dots,F_{n-3})$, $\sum b_j=\sum w_i$, with extended GIT presentation
$X=[W^e{/\!/}_{\theta^e}(\mathbf C^\*)^{m+1}]$ and extended $I$-function $I(q_0,\dots,q_m,z)$
of Janda–Sultani–Zhou (arXiv:2409.06193) Theorems 4.3.6/5.2.4. Write
$F^\epsilon_1(t)$ for the genus-one $\epsilon$-quasimap potential and $\mu_{\ge\epsilon}(q,z)$
for Zhou's $I$-function truncation (arXiv:1911.02745, Cor. 1.11.3). For the extended CY3 target,
JSZ Cor. 5.1.2 gives $\mu(q,z)=z(I_0(q)-1)\cdot\mathbf 1+I_1(q)+I'_1(q)$ with
$I_1=I_{1,H}H$ ambient and $I'_1=\sum_i I_{1,\phi_i}\phi_i$ twisted age-one.

## 2. Statement

(a) **Corrected wall-crossing identity.** The unpointed genus-one $0^+$-quasimap potential
satisfies the exact formal-series identity
$$F^{0^+}_1(0)\;=\;F^\infty_1(\mu),\qquad
\mu=z(I_0-1)+I_{1,H}H+\sum_{i=1}^m I_{1,\phi_i}\phi_i,$$
so the unpointed $0^+$ series equals the *pointed* orbifold Gromov–Witten potential evaluated
at the full (ambient $+$ twisted) mirror map. In particular it does **not** in general equal
any closed expression in unpointed data of the form $f(I_0,I_{1,H})$ plus a classical correction
$(1/24)\chi\log I_0+(1/24)\int_X(I_1/I_0)c_2(TX)$ alone.

(b) **Nonvanishing (JSZ X7 test case).** For $X_7\subset\mathbf P(1,1,1,1,3)$ with
$\phi=\mathbf 1_{1/3}$, JSZ §6.1.3 gives
$I_0=1+2q_0q_1+840q_0^3+\cdots$ and
$I_{1,\phi}=q_1+\tfrac{385}{3}q_0^2+\cdots\ne 0$; by JSZ Lemma 5.2.3,
$\partial I/\partial q_i|_{q=0}=z^{-1}\phi_i$, so the twisted direction is a genuine modulus
and cannot be set to zero.

(c) **Evaluated topological coefficients.** By adjunction
$c(TX)=\prod_i(1+w_iH)/\prod_j(1+b_jH)$, $\int_XH^3=\prod b/\prod w$:
$X_7$: $c_2$ coeff $18$, $c_3$ coeff $-104$, $\int H^3=7/3$,
$\chi_{\mathrm{top}}=-728/3$, $\int_Xc_2(TX)\cdot H=42$;
$X_{17}\subset\mathbf P(2,2,3,3,7)$: $\chi=-2125/21$, $\int c_2H=1819/252$
(artifact `topo_check.py`; quintic control $\chi=-200$).

## 3. Proof sketch

(a) is Zhou Cor. 1.11.3 at $g=1$, $t=0$: $F^\epsilon_1(t)=F^\infty_1(t+\mu_{\ge\epsilon})$,
specialized with JSZ (50)/Cors. 5.1.2–5.2.2 splitting of $\mu$. The obstruction to dropping
the twisted sum is: JSZ §1 notes the divisor equation fails for twisted insertions, and on a CY3
$\operatorname{vdim}_{1,k}=k$, so $\langle\mu_{\mathrm{tw}}^k\rangle_{1,k}$ terms are
generically nonzero and irreducible to genus-zero data. (b) is direct quotation of JSZ §6.1.2–6.1.3
plus Lemma 5.2.3. (c) is the SymPy adjunction computation in `output/artifacts/topo_check.py`.

## 4. What is proved vs conjectured

Proved: identity (a) as a corollary of cited theorems; nonvanishing (b); numbers (c).
The full closed-loop $A_i$-type orbifold localization (analogue of Li Props. 2.3–2.4 / Zinger
double-$J$) and any BCOV-type statement remain open and are **not** claimed.

## 5. Verification

- `python3 output/artifacts/topo_check.py` reproduces (c), including the quintic control.
- (b) is checkable against JSZ §6.1.3 printed series; (a) cites exact theorem numbers above.
