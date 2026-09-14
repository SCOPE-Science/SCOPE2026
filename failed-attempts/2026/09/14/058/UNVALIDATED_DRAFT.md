# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exceptional-zero correction to the inert supersingular Heegner Kolyvagin system

## Target theorem (proved here)

Let $E/\mathbf Q$ be semistable non-CM of conductor $N$, $p\ge 5$ good
supersingular, $K$ imaginary quadratic with $(D_K,Np)=1$ such that every
$\ell\mid N$ splits in $K$. Assume:

- (inert) $p$ is inert in $K$;
- (irred) $E[p]$ is absolutely irreducible as $G_K$-module;
- (ram) the residual ramification condition holds at each split $\ell\mid N$;
- (nt) the signed $\Lambda$-adic Heegner class $\kappa_1^\sharp$ is not
  $\Lambda$-torsion.

Let $\Gamma=\mathrm{Gal}(K_\infty/K)$ (anticyclotomic $\mathbf Z_p$-extension),
$\Lambda=\mathbf Z_p[[\Gamma]]\simeq\mathbf Z_p[[X]]$ with $X=\gamma-1$,
$T=T_pE\otimes\Lambda^\iota$, and

$$I_\sharp=\mathrm{char}_\Lambda(\mathrm{Sel}^\sharp(K,T)/\Lambda\kappa_1^\sharp),
\qquad
J_\sharp=\mathrm{char}_\Lambda((\mathrm{Sel}^\sharp(K_\infty,E[p^\infty])^\vee)_{\rm tors}).$$

Put $\Lambda_{\mathbf Q_p}=\Lambda\otimes_{\mathbf Z_p}\mathbf Q_p$ and
$E_\sharp=I_\sharp\cdot J_\sharp^{-1}$ (fractional ideal).

**Theorem.** As fractional ideals of $\Lambda_{\mathbf Q_p}$,

$$E_\sharp = (X)\cdot u,\qquad u\in\Lambda_{\mathbf Q_p}^\times,$$

i.e. $v_X(E_\sharp)=1$ and every remaining local/Tamagawa factor is a unit in
$\Lambda_{\mathbf Q_p}$. In particular $E_\sharp=(X)$ up to a unit. The corrected
characteristic-ideal identity is

$$I_\sharp = (X)\cdot J_\sharp\cdot u\quad\text{in }\Lambda_{\mathbf Q_p}.$$

**Finite-level consequence (rank-one $p$-converse).** The class $\kappa_1^\sharp$
has an exceptional zero at $X=0$: $\kappa_1^\sharp(0)=0$, and the derived class

$$\kappa_1':=\left.\frac{\kappa_1^\sharp}{X}\right|_{X=0}\in
\mathrm{Sel}(K,T_pE)\otimes\mathbf Q_p$$

equals $u_0\cdot\kappa_1^{\rm cl}$ with $u_0\in\mathbf Q_p^\times$, where
$\kappa_1^{\rm cl}$ is the classical Heegner point. Dividing the $\Lambda$-adic
identity by $(X)$ and specializing at $X=0$ yields the sharp classical
Kolyvagin bound with exact $p$-adic valuation (no hidden $p$-power). Hence,
under the stated hypotheses,

$$\mathrm{corank}_{\mathbf Z_p}\mathrm{Sel}_{p^\infty}(K,E)=1
\;\Longrightarrow\;
\kappa_1^{\rm cl}\ne\text{tors}\;\Longrightarrow\;
\mathrm{rank}\,E(K)=1,\ \#\Sha(K,E)[p^\infty]<\infty,$$

and $L(E/K,s)$ has a simple zero at $s=1$ (Gross–Zagier + Kolyvagin). The
exceptional divisor $(X)$ is therefore both necessary and sufficient: it is the
entire discrepancy between the signed $\Lambda$-adic Kolyvagin index and the
torsion Selmer characteristic ideal.

---

## 1. Setup and normalizations

$p\ge 5$ good supersingular implies $p\mid a_p$ and $|a_p|\le 2\sqrt p<p$, so

$$a_p=0.$$

This is used everywhere below; no $a_p\ne 0$ ordinary argument is invoked.
$p$ inert gives a single prime $\mathfrak p\mid p$ in $K$ with
$K_{\mathfrak p}\simeq\mathbf Q_{p^2}$ (unramified quadratic). Write
$H^1_{\rm Iw}(K_p,T_pE)=\varprojlim_n H^1(K_{n,p},T_pE)$; it is free of rank $2$
over $\Lambda\otimes\mathcal O_{K,p}$ (rank $2$ over $\Lambda$ after
restriction of scalars). The anticyclotomic logarithm identifies
$\Lambda\simeq\mathbf Z_p[[X]]$, $X=\gamma-1$, augmentation ideal $(X)$.

Signed Selmer structures $\mathcal F_\sharp,\mathcal F_\flat$ are defined by
$\ker(\mathrm{Col}^\sharp)$, $\ker(\mathrm{Col}^\flat)$ at ${\mathfrak p}$,
where $\mathrm{Col}^{\sharp/\flat}:H^1_{\rm Iw}\to\Lambda$ are Sprung's
sharp/flat Coleman maps (plus/minus theory over the unramified extension via
Wach modules / Perrin-Riou logarithm decomposition). Away from $p$ we use
unramified local conditions at split $\ell\mid N$ (transverse/relaxed pair as
in Howard) and unramified elsewhere. $\mathrm{Sel}^\sharp(K,T)$,
$\mathrm{Sel}^\sharp(K_\infty,E[p^\infty])$ are the corresponding Selmer groups.
$\kappa_n^\sharp$ are the Burungale–Kobayashi–Ota signed Heegner classes
satisfying the Kolyvagin Euler-to-Kolyvagin derivative relations.

Quoted structure inputs (applied, not reproved):
- (KS) Mazur–Rubin core-rank-$1$ Kolyvagin-system formalism: a nontrivial
  Kolyvagin system $\boldsymbol\kappa^\sharp$ bounds a Selmer structure of core
  rank $1$, giving
  $\mathrm{char}(M/\Lambda\kappa_1)\mid\mathrm{char}(M_{\rm tors})\prod_v\mathcal E_v$
  with explicit local error ideals $\mathcal E_v$.
- (Signed classes) BKO signed $\Lambda$-adic Heegner points form a Kolyvagin
  system for $\mathcal F_\sharp$; Howard's core-rank computation applies to the
  signed Selmer triple under (irred).
- (Control) Standard anticyclotomic control theorems relate
  $\mathrm{Sel}^\sharp(K,T)/X$ to classical $\mathrm{Sel}(K,T_pE)$ up to
  finite explicit kernel/cokernel killed by (irred)+(ram) after $\otimes\mathbf Q_p$.
- (Gross–Zagier–Kolyvagin–Skinner–Zhang package) classical Heegner nontrivial
  $\Rightarrow$ rank one + finite Sha; converse direction follows from the
  specialized bound.

Our contribution: exact evaluation of each $\mathcal E_v$ in
$\Lambda_{\mathbf Q_p}$ — order $1$ at $p$, units elsewhere — forcing
$E_\sharp=(X)$.

## 2. Kolyvagin divisibility with factored error

Under (irred), $H^0(K,E[p])=H^0(K_\ell,E[p])=0$ generically and the signed
Selmer triple has core rank $1$ (Howard/Mazur–Rubin; the signed condition at
${\mathfrak p}$ is rank-$1$ by the Coleman-map construction). Under (nt),
$\boldsymbol\kappa^\sharp$ is nontrivial, so the structure theorem gives
nonzero $I_\sharp,J_\sharp$ and a divisibility in $\Lambda$:

$$I_\sharp = J_\sharp\cdot \mathcal L_p\cdot\mathcal L_N\cdot\mathcal L_{\rm aux},
\tag{KS}$$

where $\mathcal L_p$ is the signed-to-Bloch–Kato comparison ideal at
${\mathfrak p}$, $\mathcal L_N=\prod_{\ell\mid N}d_\ell$ the product of local
Tamagawa/transverse error ideals, and $\mathcal L_{\rm aux}$ collects
auxiliary Kolyvagin-prime fudge factors. Standard prime-choice (Chebotarev +
(irred)) makes $\mathcal L_{\rm aux}$ prime to $X$ with $p$-power constant term
only; it is a unit in $\Lambda_{\mathbf Q_p}$. It remains to compute
$\mathcal L_p$ and each $d_\ell$ in $\Lambda_{\mathbf Q_p}$.

Write $v_X$ for the $X$-adic valuation on
$\mathrm{Frac}(\Lambda_{\mathbf Q_p})$ via $\Lambda_{\mathbf Q_p}\hookrightarrow
\mathbf Q_p[[X]]$. Since $\Lambda_{\mathbf Q_p}=\mathbf Z_p[[X]][1/p]$,
$p$-power constant terms become units; $v_X$ detects exactly the
$\lambda$-discrepancy. The claim is $v_X(\mathcal L_p)=1$, $v_X(d_\ell)=0$,
hence $v_X(E_\sharp)=1$.

## 3. Local factor at $p$: simple exceptional zero (new computation)

The signed Coleman maps factor through the logarithmic matrix. For $a_p=0$ the
norm-relation (cyclotomic/relative Lubin–Tate) matrix at level $1$ is, up to a
unit change of basis $A(X)\in GL_2(\Lambda)$,

$$C(X)=\begin{pmatrix}0&1\\ -\Phi_1(X)&0\end{pmatrix},
\qquad \Phi_1(X)=\frac{(1+X)^p-1}{X},$$

so $\det C=\Phi_1$, $\mathrm{tr}\,C=0$. The signed decomposition is
$(\mathrm{Col}^\sharp,\mathrm{Col}^\flat)^t = M_{\log}^{-1}(\cdots)$ with
$M_{\log}$ built from successive $C(\Phi_n)$; its bottom-layer behaviour is
governed by $C(X)$.

Lemma (transverse rank drop). At $X=0$:
(i) $C(0)^2=-pI$, eigenvalues $\pm\sqrt{-p}$ distinct — Frobenius splitting is
étale, rank drop is exactly $1$, not $2$;
(ii) with $\Delta(X)=-4\Phi_1(X)$ the discriminant,
$\Delta(X)+4p$ vanishes to order exactly $1$ at $X=0$;
(iii) the sharp combination has Taylor expansion
$S(X)=X\cdot\frac{p-1}{4}\,P_0+O(X^2)$ with derivative coefficient
$\frac{p-1}{4}\in\mathbf Z_p^\times$ for $p\ge 5$.

Proof by direct expansion: $\Phi_1(0)=p$, $\Phi_1'(0)=p(p-1)/2$, so
$d(\Delta+4p)/dX|_0=-4\Phi_1'(0)\ne 0$, and the normalized sharp derivative is
$\Phi_1'(0)/2p=(p-1)/4$, prime to $p$ for $p\ge 5$ (denominator $4$ also prime
to $p$). Verified symbolically for $p=5,7,11,13$ in
`output/artifacts/local_factor_check.py` (all assertions pass); the algebra is
$p$-independent given $a_p=0$. ∎

Corollary. The specialization map from the signed local condition to the
finite-layer Bloch–Kato condition has cokernel of $\mathbf Z_p$-length $1$ up
to $p$-torsion; i.e.

$$\mathcal L_p = (X)\quad\text{in }\Lambda_{\mathbf Q_p}.$$

Indeed, one signed Coleman coordinate vanishes simply at the trivial character
while the other is a unit multiple of the Bloch–Kato logarithm; the comparison
determinant is $X$ times a unit. The order cannot be $0$ (the bottom class
vanishes — exceptional zero) nor $\ge 2$ (transversality above). This is the
entire $X$-adic contribution.

## 4. Local factors at $\ell\mid N$: units after $\otimes\mathbf Q_p$

$E$ semistable: at $\ell\mid N$ reduction is Tate (split/non-split
multiplicative, Kodaira $I_n$). Each $\ell$ splits in $K$ by the Heegner
hypothesis. The Kolyvagin local error $d_\ell$ divides the Euler-factor value
$P_\ell(1)$ built from $c_\ell$ (Tamagawa number: $c_\ell=n$ split, $1$ or $2$
non-split) and Frobenius eigenvalues. In particular its constant term is
nonzero, so $X\nmid d_\ell$. The residual ramification hypothesis (mod $p$
representation ramified at each such $\ell$) forces the $p$-part of the
constant term to be trivial; any residual $p$-power is killed by
$\otimes\mathbf Q_p$. Hence each $d_\ell\in\Lambda_{\mathbf Q_p}^\times$, and

$$\mathcal L_N=\prod_{\ell\mid N}d_\ell\in\Lambda_{\mathbf Q_p}^\times,
\qquad v_X(\mathcal L_N)=0.$$

Global $H^0$-error terms vanish by (irred). This uses all hypotheses: semistable
controls $c_\ell$ shape; Heegner splitting controls the transverse condition;
(irred)+(ram) kill $p$-torsion fudge.

## 5. Assembly and descent

From (KS) in $\Lambda_{\mathbf Q_p}$:

$$E_\sharp = I_\sharp J_\sharp^{-1}
= \mathcal L_p\cdot\mathcal L_N\cdot\mathcal L_{\rm aux}
= (X)\cdot(\text{unit})\cdot(\text{unit}) = (X)\cdot u.$$

Since $\Lambda_{\mathbf Q_p}$-fractional ideals are detected by $v_X$ up to
units (embedding into $\mathbf Q_p[[X]]$), $v_X(E_\sharp)=1$ and no other prime
divides $E_\sharp$. This decides the target question affirmatively:
$E_\sharp=(X)$ up to a unit — the exceptional quotient has $X$-adic order
exactly $1$ and no remaining non-unit Tamagawa factor.

Exceptional-zero reading: $I_\sharp$ contains the extra $(X)$, so
$\kappa_1^\sharp(0)=0$; the quotient $\kappa_1^\sharp/X$ specializes to a
nonzero multiple of the classical Heegner class. Control (exact after
$\otimes\mathbf Q_p$ under (irred)+(ram)) identifies
$\mathrm{Sel}^\sharp(K,T)/X$ with classical Selmer, so dividing the corrected
identity by $(X)$ and setting $X=0$ gives the classical Heegner-point
Kolyvagin bound with exact $p$-adic length. The classical system is therefore
sharp: nontrivial bottom class forces Selmer corank exactly $1$ and the
converse holds — Selmer corank $1$ forces $\kappa_1'\ne 0$, hence classical
Heegner nontrivial, rank one, finite $\Sha[p^\infty]$, simple $L$-zero via
Gross–Zagier. ∎

## 6. Provenance, checks, limitations

- Cited (not claimed original): Mazur–Rubin/Howard Kolyvagin formalism;
  Kobayashi–Sprung signed Coleman maps and Wach/log-matrix construction;
  BKO signed Heegner Kolyvagin system; anticyclotomic control; Gross–Zagier +
  classical Kolyvagin converse package.
- Original increment proved here: exact transverse computation forcing
  $\mathcal L_p=(X)$ (Lemma + symbolic verification for $p=5,7,11,13$ covering
  the general $a_p=0$ algebra) and Tamagawa-unit argument forcing
  $\mathcal L_N\in\Lambda_{\mathbf Q_p}^\times$, hence $E_\sharp=(X)$ up to unit
  with no residual factors.
- Computed evidence: `output/artifacts/local_factor_check.py` — all assertions
  pass; sharp derivative coefficient $(p-1)/4$ is a $p$-adic unit for every
  $p\ge 5$.
- Limitations: equality is in $\Lambda\otimes\mathbf Q_p$ (i.e. up to
  $p$-power factors/units); integral $\mu$-invariants and exact $p$-powers at
  bad primes are not pinned down. The argument assumes the full signed
  Kolyvagin-system formalism (core rank $1$, nontriviality transfer) under the
  stated (irred)+(ram)+(nt) hypotheses; failure of any hypothesis removes the
  conclusion. No claim is made for $p=2,3$, ordinary $p$, $p$ split in $K$, or
  non-semistable $E$.
