# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharp stabilization collapse for non-loose T(2,5) at tb=9 is FALSE in host d3=-1/2 — impossibility certificate

## Theorem (target refuted)
There is **no** pair — indeed, not even one — non-loose Legendrian
$(2,5)$ torus knot with $(\mathrm{tb},\mathrm{rot},\mathrm{tor})=(9,2,0)$
in the overtwisted $(S^3,\xi_{ot})$ with $d_3=-1/2$ (Gompf convention,
homotopic to tight). Hence the target claim that two such knots
$L_1,L_2$ exist, differ by one bypass arc on a convex $5/2$ torus, and are
Legendrian isotopic via that bypass with coinciding LOSS classes, is false
as stated. The bypass/LOSS clauses are moot: the objects do not exist.

## Proof
1. **Host identification.** Eliashberg classifies overtwisted $S^3$'s by
$d_3$. Etnyre–Min–Mukherjee (EMM, arXiv:2206.14848v2, §1.2.1 fn.) use
$d_3(\xi_{\rm std})=0$, differing from Gompf's original by $1/2$:
$d_{3,{\rm Gompf}}=d_{3,{\rm EMM}}-1/2$.
So target $d_{3,{\rm Gompf}}=-1/2$ = EMM $\xi_0$, homotopic to tight.
Any surgery diagram with that $d_3$ presents $\xi_0$; the diagram details
cannot change the host.

2. **Complete list in this host.** EMM Theorem 1.14 classifies non-loose
Legendrian $(2,2n+1)$ knots. For $n=2$ (i.e. $(2,5)$), hosts are only
$\xi_1,\xi_0,\xi_{1-2n}=\xi_{-3}$ (EMM notation).
In $(S^3,\xi_0)$ the non-loose $(2,5)$ knots are exactly
$L_\pm^{i,k+1/2}$ ($i\in\mathbb Z$, $k\ge 0$) with (Thm 1.14(1)):
$$\mathrm{tb}=i,\qquad \mathrm{rot}=\mp(i-2n+1)=\mp(i-3),$$
$$\mathrm{tor}=\begin{cases}k+1/2 & i>2n-1=3\\ k+1 & i\le 3.\end{cases}$$
All stabilize as $S_\pm(L_\pm^{i})=L_\pm^{i-1}$ with opposite stabilization loose.

3. **Double obstruction at $(9,2,0)$.** At $\mathrm{tb}=9>3$:
$\mathrm{rot}=\mp 6\in\{+6,-6\}$, never $2$; and $\mathrm{tor}=k+1/2\ge 1/2$,
never $0$. So no knot — hence no pair — with $(9,2,0)$ exists in $\xi_0$.
This matches EMM Theorem 1.3's exception: in $\xi_0$ with
$\mathrm{tb}>pq-p-q=10-7=3$, torsion is half-integer.

4. **Location of the triple.** For reference, $(9,2,0)$ does occur once,
elsewhere: in EMM $\xi_1$ (= Gompf $d_3=+1/2$), Thm 1.14(3) lists
$L_{2,\pm}^i$ ($8\le i\le 10$) with $\mathrm{rot}=\mp(i-7)$; at $i=9$,
$L_{2,-}^9$ uniquely has $(9,2,0)$. So the target's numerics belong to a
different contact structure. Machine check:
`output/artifacts/verify_disproof.py` → `VERIFY_DISPROOF_OK 8/8`.

∎

## Remarks
- The disproof uses only the coarse classification (existence/values of
invariants), which EMM proves completely for torus knots; no Floer
computation or isotopy movie is needed because the vertex $(9,2,0)$ is
absent from the host's mountain range.
- It does not assert anything about LOSS: with no $L_1,L_2$, coincidence
is vacuous/moot.
- A repaired claim in EMM $\xi_1$ (Gompf $+1/2$) would be trivially unique
coarsely ($L_{2,-}^9$ is the sole $(9,2,0)$ vertex), not a two-knot collapse;
upgrading coarse uniqueness to Legendrian isotopy is future work per EMM
(Vogel remark) and is not claimed here.

## Sources
- Etnyre–Min–Mukherjee, Non-loose torus knots, arXiv:2206.14848v2:
Thm 1.14 (items 1–3), Thm 1.3, §1.2.1 footnote (d3 convention),
Fig. 5 mountain ranges.
