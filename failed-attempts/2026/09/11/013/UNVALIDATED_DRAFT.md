# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Impossibility of the literal symmetric (2,2) target cell: handle-count obstruction

## Claim (TARGET disproof)
The object presupposed by the target claim does not exist. Precisely:

**Theorem.** There is no compact oriented 4-manifold $W$ with a handle
decomposition having $n_0=1$, $n_1=1$, $n_2=2$, $n_3=n_4=0$ that is
contractible (equivalently, an integral homology ball). In particular there is
no compact Stein Mazur-type contractible handlebody with one 1-handle and two
2-handles, with any framings, twists, or Legendrian front data, and hence no
triple $(W^{sym}_{2,2},Y_{2,2},\tau)$ satisfying all clauses of the target
hypothesis simultaneously. The target claim as stated is false by void
presupposition.

## Proof
Let $W$ be compact, oriented, connected with exactly one 0-handle, one
1-handle, two 2-handles, and no 3- or 4-handles.

**Euler characteristic.** For any finite handle decomposition,
$\chi(W)=\sum_i(-1)^i n_i$. Hence
$$\chi(W)=1-1+2=2.$$
A contractible space has $\chi=1$ (homotopy equivalent to a point). Since
$2\ne 1$, $W$ is not contractible and not even an integral homology ball
(which also has $\chi=1$). This uses only the handle counts, no contact
geometry. ∎

**Rank-nullity cross-check (independent).** The cellular chain complex is
$$0\to C_2=\mathbb{Z}^2 \xrightarrow{d_2} C_1=\mathbb{Z}
 \xrightarrow{d_1} C_0=\mathbb{Z}\to 0.$$
$\operatorname{rank}\ker d_2 = 2-\operatorname{rank}\operatorname{im}d_2
\ge 2-1=1$ since $\operatorname{rank}C_1=1$. Case split on
$r=\operatorname{rank}\operatorname{im}d_2\in\{0,1\}$:
- $r=0$: $\operatorname{rk}H_1=1$, $\operatorname{rk}H_2=2$.
- $r=1$: $\operatorname{rk}H_1=0$, $\operatorname{rk}H_2=1$.
In every case $H_1(W)$ and $H_2(W)$ are not both zero (one always has positive
rank), so $W$ is never acyclic, never contractible. ∎

**No repair stays inside the literal target.** The target fixes the handle list
of $D_{sym}$ (one 1-handle, two 2-handles, no 3-handles listed) and the
Mazur-type clause (one 0-, one 1-, one 2-handle; Mazur 1961). The only
$\chi$-repair, adding one 3-handle ($1-1+2-1=1$), goes beyond the stated
diagram: an abstract acyclic chain exists (e.g.\ $d_3(1)=(1,0)$,
$d_2(a,b)=b$, giving $H_2=H_1=0$ at rank level), but realizing it requires a
3-handle outside $D_{sym}$, and counts $(1,2)$ are plug-type, not Mazur-type
(cf.\ Akbulut–Yasui 0806.3010: $W_n$ corks vs.\ $W_{m,n}$ plugs). Whether some
*other* diagram with a 3-handle could independently carry a Stein structure
is a separate question not decided here; every repair violates at least one
literal target clause (the fixed handle list of $D_{sym}$ or Mazur-type).

**Consequence for the target.** The target asserts, of this $W$,
that $\tau$ extends, $d_3(\xi_1)=d_3(\xi_0)$, and cap twists are standard.
Since no $W$ satisfies the joint hypotheses (contractible + Stein +
Mazur-type + counts $1+2$ + homology-sphere boundary), the "Let $W\ldots$
Then $\ldots$" statement has no model: the presupposed diagram $D_{sym}$
with all stated properties does not exist. The universal conclusions
($\tau$-extension, $d_3$-equality, cap standardness for that pattern) are
unestablished and the existence-loaded rigidity lemma is refuted as stated.

## Remarks (context, not claimed)
- A nearby Stein-preserving repair (one 0-, one 1-, one 2-handle with two
  $(2,2)$ boxes on a single 2-handle circle, if realizable with the right
  winding) would be a *different* object from the literal 1+2 target and is
  not decided here.
- This disproof says nothing about exoticity of any actually existing cork;
  it only closes the literal 1+2 symmetric-contractible-Stein combination.

## Limitations
- Proves non-existence of the hypothesized configuration, not non-existence
  of exoticity elsewhere.
- Uses Mazur-type terminology in the standard sense (one 0-, one 1-, one 2-handle);
  if "Mazur-type" were redefined to allow extra 2-handles, the Euler proof
  still rules out contractibility with counts $1+2$ and no other handles.
- No Floer, Seiberg–Witten, or contact computation is needed or claimed.

## Reproducibility
`output/artifacts/verify_target.py` (stdlib only) replays: $\chi(1+2)=2\ne1$,
both rank cases, Stein index bound, 3-handle repair arithmetic, and the
Mazur/plug terminology check. Result: `VERIFY_OK` (10/10).
