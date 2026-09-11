# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Toric capacity deficit versus Mahler deficit on the \(B_p^4\) curve: explicit one-sided \(C=1\) transfer and impossibility of any two-sided comparison

## 1. Statement

Work in \(\mathbb R^4\) (so symplectic space \(\mathbb R^8=\mathbb C^4\)).
For \(p\in[2,\infty]\) let \(B_p^4=\{x\in\mathbb R^4:\|x\|_p<1\}\) (open unit
\(l_p\)-ball; \(B_\infty^4=(-1,1)^4\)).
Its polar is \((B_p^4)^\circ=B_q^4\) with \(1/p+1/q=1\).
Mahler product \(P(p)=\lvert B_p^4\rvert\,\lvert(B_p^4)^\circ\rvert\).

Define the moment domain
\[
\Omega_p = 4\,\lvert B_p^4\rvert
  =\{(4\lvert x_1\rvert,\dots,4\lvert x_4\rvert):x\in B_p^4\}
  =\{u_i\ge 0:\textstyle\sum (u_i/4)^p<1\},
\]
with the obvious modification \(\max u_i<4\) at \(p=\infty\),
and the toric domain \(X_p=X_{\Omega_p}=\mu^{-1}(\Omega_p)\) where
\(\mu(z)=(\pi\lvert z_1\rvert^2,\dots,\pi\lvert z_4\rvert^2)\).
Let \(c\) be any normalized symplectic capacity.

**Theorem.**
(a) Each \(X_p\) is a convex toric domain and
\[
c(X_p)=4\qquad\forall\,p\in[2,\infty],
\]
hence with the toric-cube baseline the absolute capacity deficit
\(D_{\mathrm{cap}}(p)=c(X_p)-4\) is identically \(0\)
(and so is the relative deficit \((c(X_p)-4)/4\)).
(b) The Mahler deficits \(D_M(p)=P(p)-32/3\ge 0\) for all \(p\), with
\[
P(\infty)=32/3,\quad P(2)=\pi^4/4\approx 24.3523,\quad
P(4)=\lvert B_4^4\rvert\,\lvert B_{4/3}^4\rvert\approx 20.5472,
\]
\[
D_M(2)\approx 13.6856,\qquad D_M(4)\approx 9.8806,
\]
both strictly positive (analytic lower bounds in §3).
(c) Explicit one-sided transfer with named constant \(C=1\):
\[
0=D_{\mathrm{cap}}(p)\le 1\cdot D_M(p)\quad\forall p\in[2,\infty],
\]
in both absolute and relative normalizations.
(d) No finite \(C>0\) gives the reverse
\(D_M(p)\le C\,D_{\mathrm{cap}}(p)\) or the two-sided
\((1/C)D_M\le D_{\mathrm{cap}}\le C D_M\) on \([2,\infty]\):
at \(p=2\) (and \(p=4\)) the left side is \(>0\) while the right side is \(0\).

In particular the stated one-sided branch of the target holds with \(C=1\)
and calibration points \(p=2,4,\infty\), while the two-sided branch is
rigorously impossible on this curve: normalized toric capacity is blind to
Mahler distance along \(B_p^4\).

## 2. Toric construction and capacity evaluation

\(B_p^4\) is a convex balanced (1-unconditional) region.
Its symmetrization satisfies
\(\widehat{\Omega_p}=4B_p^4\), which is convex; hence \(X_p\) is a convex
toric domain in the sense of Shi–Lu [arXiv:2008.04000, §1].
By Theorem 1.4 there, every normalized capacity coincides on \(X_p\) with value
\[
c(X_p)=\min_{i=1,\dots,4}\|e_i\|_{\Omega_p}^*,\qquad
\|v\|_{\Omega_p}^*=\sup_{w\in\Omega_p}\langle v,w\rangle.
\]
For \(v=e_i\),
\(\|e_i\|_{\Omega_p}^*=\sup\{u_i:u\in\Omega_p\}=4\sup\{y_i:y\in\lvert B_p^4\rvert\}\).
Since \(y_i\le\|y\|_p<1\) for \(y\in B_p^4\) and \(e_i\) lies in the closure,
the supremum equals \(1\); over \(\Omega_p\) it equals \(4\).
Hence \(\|e_i\|_{\Omega_p}^*=4\) for each \(i\) and
\[
c(X_p)=\min_i 4 = 4.
\]
The argument uses only \(\|y\|_\infty\le\|y\|_p\) and \(e_i\in\overline{B_p^4}\);
it is uniform in \(p\), including \(p=\infty\).
Thus \(D_{\mathrm{cap}}(p)\equiv 0\).
Remark: via [24, Thm 7] cited in Shi–Lu Cor 1.6,
\(X_p\) is symplectomorphic to \(B_\infty^4\times_L B_p^4\) up to the harmless
factor \(4\) absorbed in \(\Omega_p\); the capacity computation above is the
same as Cor 1.6's \(4\min_i\|e_i\|^*_{|B_p|}=4\).

## 3. Mahler evaluation

Volume formula [Shi–Lu (4.15), standard]:
\[
\lvert B_p^4\rvert=(2\Gamma(1+1/p))^4/\Gamma(1+4/p).
\]
Duality \((B_p^4)^\circ=B_q^4\) gives \(P(p)=\lvert B_p^4\rvert\lvert B_q^4\rvert\).

- \(p=\infty\): \(\lvert B_\infty^4\rvert=2^4=16\),
  \(\lvert B_1^4\rvert=2^4/4!=2/3\), so \(P(\infty)=32/3\) exactly.
- \(p=2\): \(\lvert B_2^4\rvert=\pi^2/2\), so \(P(2)=\pi^4/4\approx24.35227\).
  Analytic positivity: \(\pi>3\) (hexagon perimeter) gives
  \(P(2)>81/4=20.25>32/3\), i.e. \(D_M(2)>81/4-32/3=115/12>9.58\).
- \(p=4\), \(q=4/3\):
  \(\lvert B_4^4\rvert=(2\Gamma(5/4))^4/\Gamma(2)=(2\Gamma(5/4))^4\approx10.79952\),
  \(\lvert B_{4/3}^4\rvert=(2\Gamma(7/4))^4/\Gamma(4)=(2\Gamma(7/4))^4/6\approx1.90261\),
  product \(P(4)\approx20.54723\), deficit \(D_M(4)\approx9.88056\).
  Analytic positivity \(D_M(4)>0\) (indeed \(D_M(p)>0\) for every
  \(p\in(1,\infty)\setminus\{2\) handled above\(\}\))
  is Theorem 4.1/Claim 4.2 of Shi–Lu: \(P\) is strictly increasing on
  \([1,2]\) via the digamma computation and symmetric under \(p\leftrightarrow q\),
  with equality to \(4^4/4!=32/3\) iff \(p=1,\infty\).
  Hence \(D_M(4)>0\) without relying on float enclosures; the displayed decimals
  are calibration values (stdlib `math.gamma` replay in `verify.py`,
  stable under \(\pm10^{-12}\) perturbations).

## 4. Comparison

Since \(D_{\mathrm{cap}}\equiv0\) and \(D_M\ge0\) (Mahler inequality on this
curve, Shi–Lu Thm 4.1),
\[
D_{\mathrm{cap}}(p)=0\le 1\cdot D_M(p)
\]
holds for all \(p\in[2,\infty]\) with \(C=1\).
The relative normalization \(D_{\mathrm{cap}}^{\mathrm{rel}}=(c-4)/4\equiv0\),
\(D_M^{\mathrm{rel}}=(P-32/3)/(32/3)\ge0\) satisfies the same inequality.

Conversely, any reverse \(D_M\le C D_{\mathrm{cap}}\) would read
\(D_M(p)\le 0\) for all \(p\), contradicted at \(p=2\) where
\(D_M(2)\ge115/12>0\) (and at \(p=4\)).
Hence no finite \(C\) works, and the two-sided comparison is impossible.

## 5. Calibration triple (benchmark)

| \(p\) | \(P(B_p^4)\) | \(D_M=P-32/3\) | \(c(X_p)\) | \(D_{\mathrm{cap}}\) |
|---|---|---|---|---|
| 2 | \(\pi^4/4\approx24.352273\) | \(\approx13.685606\) (analytic low \(115/12\)) | 4 | 0 |
| 4 | \(\approx20.547230\) | \(\approx9.880563\) (\(>0\) by Thm 4.1) | 4 | 0 |
| \(\infty\) | \(32/3\approx10.666667\) exact | 0 | 4 | 0 |

Replay: `python3 output/artifacts/verify.py` → `VERIFY_OK`.

## 6. Proof vs computation vs conjecture

- Proof (analytic): toric-domain convexity + cited capacity formula ⇒ \(c\equiv4\);
  cited Mahler theorem ⇒ \(D_M\ge0\) with strictness at \(p=2,4\);
  comparison algebra ⇒ one-sided \(C=1\) and reverse/two-sided impossibility.
- Computed evidence: closed-form numerical values of \(P(2),P(4)\) and volumes
  via stdlib gamma; rational-exact \(P(\infty)\); \(\pm10^{-12}\) stability check.
- No conjecture beyond cited theorems; no enclosure of \(\Gamma\) claimed —
  strict positivity at \(p=4\) rests on the cited analytic monotonicity, and at
  \(p=2\) on \(\pi>3\).

## 7. Interpretation and limitations

The \(B_p^4\) toric curve answers the quantitative transfer question negatively
in the capacity→Mahler direction: normalized capacity is constant while Mahler
product varies by \(>100\%\), so symplectic-capacity stability cannot control
Mahler stability here. The Mahler→capacity direction holds trivially with
\(C=1\). Scope is limited to this symmetric curve in \(\mathbb R^4\);
no universal constant or other toric families are claimed.

References: K. Shi–G. Lu, arXiv:2008.04000 §§1–4 (Thm 1.4, Cor 1.6, Thm 1.7–1.8,
Thm 4.1/Claim 4.2, volume formula (4.15), duality \((B_p)^\circ=B_q\)).
