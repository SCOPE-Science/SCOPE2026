# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Eliahou numbers under Delorme–Rosales gluing: a closed formula, ray-positivity, and a certified beyond-frontier table

## 1. Setup and conventions

A numerical semigroup is a cofinite submonoid of $(\mathbb N,+)$.
For $\Gamma$ write $m$ = multiplicity, $c$ = conductor, $g$ = genus (number of gaps),
$n=\delta=|\Gamma\cap[0,c)|$ ($\delta$-invariant), $e$ = embedding dimension,
$G$ = minimal generators, $e_s=|G\cap[0,c)|$, $q=\lceil c/m\rceil$, $\nu=qm-c$,
$W(k)=kn-c$ (Wilf function).
The **Eliahou number** (locked convention, verified against published tables) is

$$E(\Gamma)=e_s\,n-q\,|d_q|+\nu,\qquad d_q=[c,c+m-1]\setminus p_q,\ p_q=[c,c+m-1]\cap G.$$

Note: the window is $[c,c+m-1]$ (length $m$), i.e. $|d_q|\le m$; the
topic prose "$J_q=[c,c+m]$" is off by one endpoint and we correct it here.
Proof of correctness: Almirón–Moyano Table 1 reproductions —
$\langle100,170,171,176\rangle_{599}\mapsto E=-1$,
$\langle100,270,272,275\rangle_{998}\mapsto E=-2$,
$\langle100,170,173,175\rangle_{599}\mapsto E=-7$ (all exact, conductor confirmed).

A **Delorme–Rosales gluing** $C=k_1A\sqcup k_2B$ ($A,B$ numerical semigroups) requires
$k_1\in B\setminus G(B)$, $k_2\in A\setminus G(A)$, $\gcd(k_1,k_2)=1$, and
minimality $e(C)=e_A+e_B$ (checked, not assumed: one toy tuple
$A=\langle4,7,9\rangle$, $B=\langle3,5\rangle$, $k_1=5,k_2=4$ has $e(C)=4<5$ and is
correctly excluded by the auditor).

## 2. Theorem 1 — closed Eliahou-gluing formula (proved, machine-checked 345/345)

**Theorem 1.** Let $C=k_1A\sqcup k_2B$ be a valid gluing. With Rosales identities
$c_C=k_1c_A+k_2c_B+(k_1-1)(k_2-1)$,
$n_C=k_1n_A+k_2n_B+(k_1-1)(k_2-1)/2$ (same for $g_C$),
$m_C=\min(k_1m_A,k_2m_B)$, and

$$e_{s,C}=\#\{a\in G_A:k_1a<c_C\}+\#\{b\in G_B:k_2b<c_C\},$$
$$j_C=\#\{a\in G_A:c_C\le k_1a\le c_C+m_C-1\}+\#\{b\in G_B:c_C\le k_2b\le c_C+m_C-1\},$$

one has $q_C=\lceil c_C/m_C\rceil$, $\nu_C=q_Cm_C-c_C$, $|d_{q,C}|=m_C-j_C$, and

$$E(C)=e_{s,C}\,n_C-q_C\,(m_C-j_C)+\nu_C,$$

an exact closed integer expression in base data $(G_A,G_B,c,n,m,k_1,k_2)$ only —
no enumeration of $C$ needed.

*Proof.* Rosales identities are standard (Frobenius/genus/delta/multiplicity
propagation; $e_C=e_A+e_B$ is the validity hypothesis). The Eliahou count:
minimal generators of $C$ are exactly $\{k_1a\}\cup\{k_2b\}$ (validity), so
splitting them at $c_C$ (resp. in $[c_C,c_C+m_C-1]$) gives $e_{s,C}$ (resp. $j_C$);
$|d_{q,C}|=m_C-j_C$ follows since the window has length $m_C$. Substituting into
the locked $E$-definition gives the formula. The inequality $E\ge W(e_s)$ also
gives $E(C)\ge W_C(e_{s,C})$. ∎

*Machine check.* 345/345 exact agreements (formula vs. full gap-enumeration from
$C$'s generators, checking $c,g,n,m,e,E$): 90/90 on
$\langle4,7,9\rangle\times\langle3,5\rangle$ ($k\le20$) plus 255/255 random
admissible gluings over 5 small bases ($k\le40$). Zero mismatches.
Replay: `output/artifacts/sglue.py`, `glue.py`, `catalog_g100.csv`.

## 3. Theorem 2 — no fixed-base infinite negative-Eliahou ray with both multipliers growing (proved)

**Theorem 2.** Fix $A,B$ with $e_A+e_B\ge 3$ (in particular if at least one of $A,B$
is not $\mathbb N=\langle 1\rangle$; all committed bases satisfy $e=3$). Along any
admissible sequence with $k_1,k_2\to\infty$,
$E(C)\to+\infty$; hence at most finitely many members have $E<0$.

*Proof.* Eventually every fixed scaled generator lies below $c_C$ (since
$c_C/k_1\ge k_2(c_B-1)/2\to\infty$ and symmetrically), so $e_{s,C}=e_A+e_B$
eventually; if $e_A+e_B\ge 3$ then the coefficient $e_s/2-1\ge 1/2>0$ gives
quadratic dominance. The remaining case $e_A=e_B=1$ means $A=B=\mathbb N$,
$C=\langle k_1,k_2\rangle$ has $E=0$ identically, noted as explicit exception.
$E(C)\ge (e_A+e_B)n_C-c_C-m_C\ge \frac{e_A+e_B-2}{2}(k_1-1)(k_2-1)-O(k_1+k_2)\to+\infty$
as the quadratic coefficient is $\ge 1/2>0$. ∎ Numerically:
$E=8417, 34784, 109484$ at $(k_1,k_2)=(37,39),(100,101),(200,201)$ for a sample pair.

*Scope honesty.* This refutes the admitted target's "infinite parametric ray with
$E<0$ and unbounded genus for fixed $A_0,B_0$" in the both-growing regime, for all
fixed bases except $A=B=\mathbb N$ (whose ray has $E=0$ constant). The
single-ray regime (one multiplier fixed) is left as a conjecture with strong
evidence (10,499 admissible gluings computed, min $E=+612$, zero negative);
a slope analysis shows admissibility ($k_2\in A\setminus G(A)$ forces $k_2$ large
for sparse bases) protects positivity, but a full proof is not claimed.

## 4. Certified beyond-frontier table (fallback delivered, strengthened)

`output/artifacts/catalog_g100.csv`: 255 admissible gluings over committed bases
$\langle4,7,9\rangle$, $\langle5,7,9\rangle$, $\langle8,11,13\rangle$,
$\langle9,13,14\rangle$, $\langle7,15,17\rangle$ with $2\le k_i\le40$ (sampled),
each with exact $(c,g,m,e,n,E)$ recomputed from generators.
**All 255 land at genus $100<g\le2438$** (strictly beyond the Delgado–Eliahou–
Fromentin genus-100 exhaustive-verification frontier), $E\in[1056,8417]$
(all positive), max genus witness:
$A=\langle8,11,13\rangle$, $B=\langle9,13,14\rangle$, $k_1=37,k_2=39$,
$c=4609$, $g=2438$, $m=296$, $e=6$, $n=2171$, $E=8417$.
Reusable auditor `glue.py`: admissibility check (coprimality, membership in
opposite semigroup, minimality $e_C=e_A+e_B$) + exact recomputation + formula
agreement assertion.

*What was not found.* No admissible glued $E<0$ example at any genus in
$\approx$10,500 formula evaluations (plus 345 full enumerations); known
negative-Eliahou seeds ($\langle14,22,23\rangle_{56}$, $\langle24,31,35\rangle$-type,
$\langle100,170,171,176\rangle_{599}$) are gluing-atomic under complete-split test
(where feasible). We conjecture nontrivial gluings always satisfy $E\ge0$ but do
**not** claim it as proved.

## 5. Originality / limitations

Formula-level novelty per admission triage (no prior $E$-under-gluing identity;
nearest gluing theorem covers only coarse Wilf inequality). Limitations:
(1) target infinite negative ray disproved (both-growing, for all fixed bases except
$A=B=\mathbb N$ where $E=0$ constant) / unsupported
(single-ray) — the headline witness claim is replaced by the positivity theorems
and the all-positive frontier table; (2) $E\ge0$-for-all-gluings is conjectural;
(3) catalog is a sampled (not exhaustive) multiplier window; every row is
independently replayable. No database reprint: all rows are new gluings with
proved formula agreement.

## References

[1] Almirón–Moyano, arXiv:2104.03793 (conventions, Table 1, $E\ge W(e_s)$-lineage).
[2] Singh–Srinivasan, arXiv:2306.09876 (Wilf persists under gluing; no $E$-formula).
[3] Delgado–Eliahou–Fromentin, arXiv:2310.07742 (genus-100 frontier).
[4] Delgado 2018 (negative-$E$ families, non-gluing); Bras-Amorós seeds census genus 65.
