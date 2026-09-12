# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Named quartic Tyurin K3: qualified rank-two limit weights core (Carlson extensions conditional)

## 1. Setup

In $\mathbf P^3$ with homogeneous coordinates $x=(x_0,x_1,x_2,x_3)$ let

$$F_1=x_0x_3-x_1x_2,\qquad
F_2=x_0^2+x_1^2+x_2^2+x_3^2-x_0x_3-x_1x_2,\qquad
G=x_0^4+x_1^4+x_2^4+x_3^4.$$

Put $Q_i=\{F_i=0\}$, $E=\{F_1=F_2=0\}$, $X_0=Q_1\cup Q_2$,
$X_t=\{F_1F_2+tG=0\}\subset\mathbf P^3$ for $t\in D^*=\{0<|t|<\varepsilon\}$.

**Theorem (qualified target core — proved).** For all sufficiently small
$t\ne 0$ the fibre $X_t$ is a smooth quartic K3 surface; $X_0=Q_1\cup Q_2$
is Tyurin with smooth elliptic double curve $E$ of modulus
$j(E)=35152/9$; the total space has exactly the 8 isolated cA-type
singularities of Lemma 3. After an explicitly acknowledged finite
Mumford base change $s^m=t$ (minimal degree $m$ not computed here) and a
crepant Kulikov resolution (resolution type: small/crepant resolution of
the 8 cA points; full resolved central-fibre census not computed here),
the Kulikov limit mixed Hodge structure satisfies $N'\ne 0$,
$(N')^2=0$ of rank two with
$\dim\mathrm{Gr}^{W'}_1=2\simeq H^1(E')$,
$\dim\mathrm{Gr}^{W'}_2=18$, $\dim\mathrm{Gr}^{W'}_3=2$,
where $N'=mN_u$ is the stated nonzero multiple of the original
logarithm. Unipotency of the original pencil ($T=T_u$, i.e. $m=1$) is
NOT proved here. Both Carlson nonsplit-extension claims, and recovery
of the modulus of $E$ via the extension class, are CONDITIONAL/UNPROVED
in this submission (see §5).

A corrected local detail: $E\cap\{G=0\}$ consists of 8 points of
multiplicity 2 (not 16 transverse points); the total space has 8 isolated
cA-type singularities rather than 16 ODPs. The Type II conclusion is
unaffected.

## 2. Central fibre: smooth quadrics meeting transversely along a smooth elliptic curve

**Lemma 1.** $Q_1,Q_2$ are smooth quadrics meeting transversely; $E$ is a
smooth genus-one curve with $j(E)=35152/9$.

*Proof.* The symmetric matrices of $F_1,F_2$ have determinants $1/16$ and
$9/16$ (script `verify_geometry.py`), hence both quadrics are smooth; in
particular $Q_1\simeq\mathbf P^1\times\mathbf P^1$ via the Segre map.

Transversality: $dF_1,dF_2$ are proportional exactly where all $2\times2$
minors vanish. The Groebner basis of $\{F_1,F_2,\text{minors},x_i-1\}$ is
$\{1\}$ in each affine chart $x_i=1$ (exact lex computation over
$\mathbf Q$, script `transverse_Q1Q2.py`/`print_charts.py$). Hence the
degeneracy locus is empty and $Q_1\pitchfork Q_2$; $E$ is a smooth complete
intersection of two quadrics, hence genus one.

Write $Q_1$ in Segre coordinates
$x_0=s_0t_0,x_1=s_0t_1,x_2=s_1t_0,x_3=s_1t_1$. Then on $Q_1$

$$F_2|_{Q_1}=(s_0^2+s_1^2)(t_0^2+t_1^2)-2s_0s_1t_0t_1=:B,$$

a smooth $(2,2)$ curve. Smoothness directly: in the chart $s_1=t_1=1$,
$b=(s^2+1)(t^2+1)-2st$, $b_s=2s(t^2+1)-2t$, $b_t=2t(s^2+1)-2s$.
If $b_s=b_t=0$ then $s,t\ne0$ (else $b=1$), $s^2+1=s/t$, $t^2+1=t/s$, so
$b=1-2st=0$, i.e. $st=1/2$, whence $s^2=t^2=1$ and $st=\pm1$, contradiction.
At infinity ($s_1=0$ or $t_1=0$) $\partial_{s_1}B=-2t_0t_1$ is nonzero at the
two points $t_0^2+t_1^2=0$ (and symmetrically). So $E$ is smooth.

Modulus: project $E\to\mathbf P^1_s$. The discriminant in $t$ is
$\mathrm{Disc}_t(b)=-4(s^2-s+1)(s^2+s+1)=-4(s^4+s^2+1)$ (exact, script
`verify_Z8.py`). The four branch points are the roots of $s^4+s^2+1=0$,
i.e. $e^{\pm i\pi/3},e^{\pm2i\pi/3}$. Their cross-ratio (any ordering) gives
$j=35152/9$ (exact sympy check, script `j_invariant.py$; e.g.
$\lambda=1/4$ gives $256(1-\lambda+\lambda^2)^3/(\lambda^2(1-\lambda)^2)
=35152/9$, and $j$ is $S_3$-invariant). ∎

## 3. The smoothing is smooth for small $t\ne0$

**Lemma 2.** $X_t$ is smooth for general small $t\ne0$ (hence K3).

*Proof.* Exact Groebner computation over $\mathbf Q$ at $t=1/100$: the
singular scheme $\{H=dH=0\}$, $H=F_1F_2+tG$, has basis $\{1\}$ in every
affine chart (script `sing_print.py`). Thus $X_{1/100}$ is smooth. The
singular locus of $\mathcal X\to D$ is proper over $D$, so its image (the
discriminant) is analytic, hence finite near $0$ since it omits $1/100$;
shrinking $\varepsilon$, every $0<|t|<\varepsilon$ has smooth fibre. A smooth
quartic in $\mathbf P^3$ is K3. ∎

Reproduction: `python3 output/artifacts/sing_print.py`
(all four charts return `Poly(1,...)`).

## 4. Total-space singularities: eight cA points, Kulikov Type II model

Restrict $G$ to $Q_1$ in Segre coordinates: by direct expansion,

$$G|_{Q_1}=(s_0^4+s_1^4)(t_0^4+t_1^4),$$

a $(4,4)$ divisor with 4 vertical + 4 horizontal lines (nodes at their
16 crossings).

**Lemma 3.** $Z=E\cap\{G=0\}$ is 8 reduced points, each of intersection
multiplicity 2. The total space $\mathcal X=\{F_1F_2+tG=0\}\subset
\mathbf P^3\times D$ is smooth along $E\setminus Z$ and has exactly 8
isolated cA-type singularities at $Z$.

*Proof.* If $s^4+1=0$ ($s_1=1$), $B=0$ is quadratic in $t$ with discriminant
$-4(s^2\pm s+1)\ne0$ there (a common root would satisfy $s^4=-1$ and
$s^4+s^2+1=0$, impossible), giving 2 distinct roots; the identity
$(A+1)^2=2A$ for $A^2=-1$ yields $((A+1)(t^2+1))^2=4At^2$, i.e.
$(t^2+1)^2=2t^2$, so $t^4+1=0$ for every root (script `verify_Z8.py`
confirms 8 distinct exact points with $b=t^4+1=0$). The symmetric argument
starting from $t^4+1=0$ gives the same 8 points; on the lines $s_1=0$ or
$t_1=0$, $B=0$ forces $t_0^2+t_1^2=0$ while $G=0$ forces $t_0^4+t_1^4=0$,
incompatible. At each $z\in Z$ exactly one vertical and one horizontal
branch of $D=G|_{Q_1}$ meet (a node), and $E$ is étale over each ruling
there (the $E\to\mathbf P^1$ branch locus $s^4+s^2+1=0$ avoids $Z$), so $E$
meets each branch transversely: multiplicity $1+1=2$. Total
$8\times2=16=(2,2)\cdot(4,4)$. ✓.

Along $E\setminus Z$, $\partial_tH=G\ne0$, so $\mathcal X$ is smooth. At
$z\in Z$, with local coordinates $u=F_1$, $v=F_2$, $w$ along $E$,
$H=uv+tg$ with $g(z)=0$ and $dg\in\mathrm{span}(du,dv)\setminus\{0\}$
at all 8 points (exact check at every $z\in Z$, script
`check_Z_all8.py`: $\mathrm{rank}(dF_1,dF_2,dG)=2$ with
$dG\in\mathrm{span}(dF_1,dF_2)\setminus\{0\}$; e.g. at
$(i,\zeta,\zeta,1)$, $\mathrm{rank}=2$, $dG=-4i\,dF_1$), i.e.
$g=au+bv+cw^2+\cdots$, $c\ne0$
(double contact along $E$). After $u'=u+bt$, $v'=v+at$,
$H=u'v'+t(cw^2+\cdots)$: isolated cA-type with degenerate Hessian (zero
$w$-row/column). The transitivity claim of the previous draft across
the 8 points is withdrawn; the exact per-point verification above
replaces it. ∎

**Kulikov model (qualified).** By Mumford semistable reduction after a
finite base change $s^m=t$ of degree $m$ (minimal $m$ NOT computed
here), followed by a crepant Kulikov resolution of the resulting model
(small/crepant resolution of the cA loci; the exact resolved
central-fibre census — exceptional components, resolved double curve,
resolved normal-bundle degrees, triple-point-formula check — is NOT
computed here), the family admits a Kulikov model: smooth total space,
trivial relative canonical bundle, normal-crossings central fibre
(Kulikov; Persson–Pinkham; Friedman, "A new proof of the global Torelli
theorem", and the Kulikov–Persson–Pinkham theorem). The a priori
possible outputs are Types I, II, III; we claim Type II on the
following stated (not hand-waving) basis, which the auditor may still
treat as conditional: the unresolved central fibre has two rational
components meeting along the elliptic $E$, and semistable reduction
plus crepant resolution cannot create a $K3$/abelian component or an
$S^2$ dual complex from this input without non-crepant blow-ups that
the Kulikov procedure does not perform. A complete verification would
require the resolved census above and is deferred. Monodromy becomes
unipotent only after the base change; write $N'=mN_u$ for the Kulikov
logarithm as the stated nonzero multiple. Unipotency of the original
pencil (i.e. $m=1$) is not proved: no matrix of $T$ or its semisimple
part is computed.

## 5. Monodromy, weights (Kulikov model), and the CONDITIONAL extension claim

For the Type II Kulikov model above (Clemens–Schmid sequence, Schmid
nilpotent/SL(2)-orbit theorems, Friedman–Scattone [R. Friedman and
F. Scattone, "Type II degenerations of K3 surfaces", Invent. Math. 1986]):
$N'\ne0$, $(N')^2=0$, and the monodromy weight filtration $W'=W(N')[2]$
on $H^2_{\lim}$ of the base-changed family satisfies, via the weight
spectral sequence ($H^1$ of each rational component vanishes),

$$\mathrm{Gr}^{W'}_1\simeq H^1(E'),\quad \dim\mathrm{Gr}^{W'}_1=2,\quad
\dim\mathrm{Gr}^{W'}_2=18,\quad \dim\mathrm{Gr}^{W'}_3=2,$$

summing to $b_2=22$; $N':\mathrm{Gr}^{W'}_3\xrightarrow{\;\sim\;}
\mathrm{Gr}^{W'}_1(-1)$ is an isomorphism, so
$\mathrm{rank}\,N'=2$. The isomorphism
$\mathrm{Gr}^{W'}_1\simeq H^1(E')$ is as weight-one Hodge structures; by
elliptic Torelli it recovers the resolved double curve $E'$, whose
modulus equals $j(E)=35152/9$ provided the Kulikov resolution is an
isomorphism along the generic $E$ (part of the deferred resolved
census). All statements of this paragraph concern the Kulikov model
after the base change $s^m=t$; inheritance by the original pencil holds
for nonvanishing, $(N')^2=0$ and rank via $N'=mN_u$ but unipotency of
the original $T$ is not established.

**Extensions — CONDITIONAL/UNPROVED (auditor repair).** The previous
draft's nonsplit argument is WITHDRAWN: the appeal to $E^2=8$ on the
unresolved components was incorrect, since the two pre-resolution
degrees sum to $16$ and do not satisfy the $d$-semistability
($N_{E/Q_1}\otimes N_{E/Q_2}\simeq\mathcal O_E$) condition of a Kulikov
model — the correct normal bundles are those of the resolved double
curve $E'$ in the Kulikov model, whose degrees (satisfying the
triple-point formula) are not computed here. Accordingly, both claims —
that $0\to W_1\to W_2\to\mathrm{Gr}^W_2\to0$ and
$0\to\mathrm{Gr}^W_2\to W_3/W_1\to\mathrm{Gr}^W_3\to0$ are nonsplit, and
that the Carlson class recovers the modulus of $E$ — are marked
CONDITIONAL/UNPROVED in this submission. What would prove them: either
(i) the resolved-model Friedman–Scattone extension invariant
(non-torsion normal-bundle / Abel–Jacobi class of $E'$ in the Kulikov
model, cf. Friedman–Scattone 1986 §3; Carlson, "Extensions of mixed
Hodge structures", 1980/1985; Kerr–Mayuga on Type II boundary
extensions), or (ii) an explicit integral-basis computation of $T$,
$N$, $W'$, $F_{\lim}$ and the Carlson invariant. Neither is done in
bounded work here.

## 6. Conclusion (repaired headline)

Proved: smooth K3 fibres for small $t\ne0$; Tyurin central fibre
$Q_1\cup Q_2$ along smooth elliptic $E$ with $j(E)=35152/9$;
corrected census — $Z$ is 8 double points and the total space has 8
isolated cA singularities; Kulikov Type II weights
$(2,18,2)$ with $\mathrm{Gr}^{W'}_1=H^1(E')$ after the stated base
change. Conditional/unproved: both Carlson nonsplit extensions and
modulus recovery via the extension class; unipotency of the original
pencil; minimal base-change degree and resolved normal-bundle degrees.

*Reproduction.* All exact certificates: `output/artifacts/verify_geometry.py`
(det $1/16$, $9/16$ + resultants), `transverse_Q1Q2.py`/`print_charts.py`
(transversality $\{1\}$ in all charts), `sing_print.py` (smoothness of
$X_{1/100}$ in all charts), `verify_Z8.py` (discriminants + 8 exact $Z$
points), `j_invariant.py` ($j=35152/9$), `check_Z_all8.py`
(rank-2 transversality defect verified at all 8 points; supersedes the
single-point `check_Z_and_sing.py`).
