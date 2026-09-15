# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Bounded t-structures and stability on the silting-free proper graded gentle algebra

## Claim (TARGET route — both conditionals resolved)

Let $A$ be the graded gentle algebra of the target: two vertices $\{0,1\}$,
arrows $a,b,c$ with $t(a)=s(b)$, $t(b)=s(c)$, relations $\{ab,bc\}$,
$|a|+|b|=1$, $|b|+|c|=1$. Then:

1. **(Bounded t-structure: YES.)** $\mathrm{per}(A)$ admits a bounded
   t-structure — the standard one, with heart the finite-dimensional graded
   $A$-modules. The graded global dimension of $A$ is $\le 3$ for every
   admissible degree assignment.
2. **(Stability: NOT empty.)** $\mathrm{Stab}(\mathrm{per}(A))\ne\varnothing$:
   an explicit Bridgeland stability condition is constructed on the standard
   heart.

Both statements are proved below; the machine-checked linear algebra is in
`artifacts/` (`verify_all.py` + `results.json`).

## 1. The algebra is unique up to isomorphism

Composability + connectedness on two vertices gives 14 quiver shapes
(`artifacts/enumerate.py`). Imposing gentle ($\le 2$ in/out at each vertex)
and properness (every oriented cycle contains a zero relation) leaves exactly
two: $a:0\to1$, $b:1\to 0$, $c:0\to1$ and its vertex swap; these are
isomorphic via $0\leftrightarrow 1$. Fix the first. Nonzero paths are
$e_0,e_1,a,b,c,ba,cb,cba$; $\dim_k A = 8$ independent of degrees. With
$d=|b|$, $|a|=|c|=1-d$. Since $|a|+|b|=1$ with integral degrees, some arrow
has strictly positive degree (max$(|a|,|b|)\ge 1$), so
$H^{>0}(A)\ne 0$ and $A$ itself is never silting — consistent with the
silting-free hypothesis, which only rules out *algebraic* (length-heart)
t-structures by Koenig–Yang, not the standard one below.

Smoothness: the quiver is bipartite ($a,c:0\to1$, $b:1\to0$), so closed walks
have even length, alternating $\{a,c\},b,\{a,c\},b,\dots$. A forbidden cycle
would need every cyclic length-2 subpath in $\{ab,bc\}$: odd–even pairs force
the $\{a,c\}$-letters to be $a$, even–odd pairs force them to be $c$ —
contradiction. Hence no forbidden cycles at any length (checked to length 10
in `verify_all.py`; the parity argument covers all lengths): $A$ is smooth,
and finite-dimensional, hence proper.

## 2. Graded global dimension $\le 3$ — explicit resolutions

Graded simples $S_0,S_1$. With $P_i=e_iA$, and convention $P_i(-s)$
denotes internal shift with generator in degree $s$ (so a path $p$ in that
summand has shifted degree $|p|+s$), the following complexes of graded
projectives (maps = left concatenation, degree $0$ with the indicated
internal shifts) are exact. For $S_1$ the shifts are $s_2=d$, $s_3=1$:

$$0 \to P_1(-s_3) \xrightarrow{\cdot c} P_0(-s_2)
  \xrightarrow{\cdot b} P_1 \to S_1 \to 0,$$

while for $S_0$ the shifts are distinct, $t_1=1-d$ (on $P_1^2$), $t_2=1$
(on $P_0$), $t_3=2-d$ (on $P_1$), i.e.

$$0 \to P_1(-(2-d)) \xrightarrow{\cdot c} P_0(-1)
  \xrightarrow{(b,0)} P_1(-(1-d))^{\oplus 2}
  \xrightarrow{(a,c)} P_0 \to S_0 \to 0.$$

Degree-$0$ check for $S_0$: the images $b,c$ have shifted degrees matching
the source generators, $d+(1-d)=1$ and $(1-d)+1=2-d$.

Exactness is a degree-independent monomial computation, verified in
`artifacts/closedform.py` and `verify_all.py`: $bc=0$, $cb\cdot b=0$ give
$d^2=0$; $\ker(\cdot b)=\mathrm{span}\{c,cb,cba\}=\mathrm{im}(\cdot c)$;
$\ker(a,c)=\mathrm{span}\{(b,0),(ba,0)\}=\mathrm{im}(b,0)$;
$\ker(b,0)=\mathrm{span}\{c,cb,cba\}$; $\ker(\cdot c)=0$.
Minimality (images in the arrow ideal) is visible. Hence
$\mathrm{pd}(S_1)=2$, $\mathrm{pd}(S_0)=3$ for every integer $d$, i.e.
graded $\mathrm{gldim}(A)\le 3$.

Consequence: every finite-dimensional graded module is perfect, so
$\mathrm{per}(A)=D^b(\mathrm{grmod}_{fd}\text{-}A)$, and the canonical
t-structure on $D(\mathrm{grmod}\text{-}A)$ restricts to a bounded
t-structure on $\mathrm{per}(A)$ with heart $\mathrm{grmod}_{fd}\text{-}A$
(noetherian and artinian: submodules stabilize by finite total dimension).
This heart has infinitely many simples $S_i(n)$, so it is not a length
category with finitely many simples — no conflict with silting-freeness.

## 3. An explicit stability condition

Use the finite-rank charge lattice $\Gamma=\mathbb Z^2$ with
$\mathrm{ch}([S_i(n)])=e_i$ (well defined since $K_0$ of the length heart is
free on the $S_i(n)$) and central charge $\bar Z(e_0)=i$, $\bar Z(e_1)=1+i$.
Every nonzero $M$ in the heart has class $(m,n)$ with $m,n\ge 0$ not both
zero, and $\bar Z(M)=n+(m+n)i$ has positive imaginary part. Harder–Narasimhan
holds for *every* such charge: a finite-dimensional graded module has only
finitely many subobject dimension vectors ($(m',n')\le(m,n)$), so a maximal
phase is attained and the standard induction on length terminates. Support
property: $\bar Z:\mathbb R^2\to\mathbb C$ is injective
($i,1+i$ are $\mathbb R$-independent), so $\ker\bar Z=0$ and $Q\equiv 0$
qualifies. Local finiteness follows from the finite-length heart. Thus
$(\bar Z\circ\mathrm{ch},\ \mathrm{grmod}_{fd}\text{-}A)$ is a Bridgeland
stability condition: $\mathrm{Stab}(\mathrm{per}(A))\ne\varnothing$.

## 4. Remarks on the literature

One consolidated search (method-blocker for Q2's Fukaya side) confirmed the
HKK picture ($M(X)\to\mathrm{Stab}(F(X))$ open/closed, arXiv:1409.8611) and
the silting-classification context for graded gentle algebras
(arXiv:2303.17474; Chang–Jin–Schroll on recollements/silting). The proof
above is independent of flat-surface existence: it works purely on the
algebra side. Notably, the resolution answers both conditionals positively
despite the suggestive framing — the obstruction is only to *algebraic*
t-structures, and stability exists via the non-algebraic standard heart.

## Limitations / what is not claimed

- Uniqueness/silting-freeness of $A$ itself is used as admitted context, not
  reproved (only the consistency check $H^{>0}(A)\ne0$ is proved).
- Only one stability condition (one component) is constructed; the full
  topology of $\mathrm{Stab}$ and the HKK comparison map are untouched.
- The graded surface identification (torus, one boundary, one stop, zero
  winding) is taken from the admission; all arguments use only the quiver
  data, which the enumeration shows is forced by it.
