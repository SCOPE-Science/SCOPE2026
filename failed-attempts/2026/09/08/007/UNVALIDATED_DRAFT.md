# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact Molien degrees, exponents, coexponents and reflection fake degrees
# for G(m,p,n), n = 2..4, m <= 6 — with a certified non-Coxeter witness at G(4,2,2)

## 1. What was proved and computed (42/42 groups, exact arithmetic)

For every triple $(m,p,n)$ with $2\le n\le 4$, $1\le m\le 6$, $p\mid m$
(42 triples), the imprimitive reflection representation of $G(m,p,n)$ was
constructed as monomial matrices over the exact cyclotomic ring
$\mathbf Z[\zeta_m]\cong \mathbf Z[x]/(\Phi_m)$ (no floating point anywhere),
fully enumerated (orders $2$ through $31104$), and the following were verified
exactly (see `artifacts/replay.py`, stdlib only; rerun prints `ALL_GATES: True`):

1. **Order.** Enumerated $|G| = m^n n!/p$ for all 42 groups.
2. **Degrees / Molien match to order 30.** With
   $M(t) = |G|^{-1}\sum_{g}\!1/\det(1-tg)$ computed by exact type-aggregated
   cyclotomic series inversion, $M(t) = 1/\prod_i(1-t^{d_i})$ through $t^{30}$
   for $d = (m,2m,\dots,(n-1)m,mn/p)$, all 42 groups.
3. **Degree product.** $\prod_i d_i = |G|$, all 42 groups.
4. **Reflection count.** $N_{\mathrm{ref}} := \#\{g : \operatorname{fix}(g)
   \text{ is a hyperplane}\} = \sum_i(d_i-1) =: N$, all 42 groups; reflection
   orders per group recorded (e.g. $G(4,1,2)$: six order-2, four order-4).
5. **Hyperplane count.** Enumerated reflecting hyperplanes (coordinate type
   $x_i=0$ and transposition type $x_i=\zeta^k x_j$ with correct phase-ratio
   keys) match $n_{\mathrm{hyp}} = c + f\binom n2$ with $c = n$ if $p<m$
   else $0$ and fibre $f \in \{1,2,3,5\}$ ($m=2{:}1$, $m=4{:}2$, $m=6{:}3$,
   else $f=m$), all 42 groups.
6. **Reflection fake degrees.** The $V$-isotypic series
   $A_V(t) = |G|^{-1}\sum_g \overline{\chi_V(g)}/\det(1-tg)$ times
   $\prod_i(1-t^{d_i})$ is a polynomial $F_V(t)$ with $F_V(1) = n$
   (42/42), supported on the exponent list below; likewise $F_{V^*}(t)$ with
   $F_{V^*}(1) = n$ supported on the coexponent list (42/42). All outputs are
   Galois-real (conjugation-deviation $0$) nonneg integers.
7. **Character Gram on $\{1,\chi_V,\bar\chi_V\}$.**
   $\langle 1,1\rangle = 1$; $\langle 1,\chi_V\rangle = 1$ for $m=1$
   (permutation representation) else $0$; $\langle\chi_V,\chi_V\rangle = 1$
   except $m=1$ (value $2$) and $G(2,2,2)$ (value $2$, abelian — $V$ splits as
   two distinct linear characters); $\langle\chi_V,\bar\chi_V\rangle = 1$ for
   real $V$ ($m \le 2$, plus the dihedral groups $G(m,m,2)$) else $0$.
   All 42 exact.
8. **Independent lattice cross-check.** Molien coefficients at selected degrees
   recomputed by counting invariant monomials $e_1^{a_1}\cdots z^b$ in the
   known generator multidegrees — no determinants — agreeing with both the
   determinant route and $1/\prod(1-t^{d_i})$ (5 spot groups).

### Closed tables verified on all 42 groups

- **Degrees:** $d = (m, 2m, \ldots, (n-1)m, mn/p)$ sorted.
- **$V$-exponents** (support of $F_V$, i.e. $V$-isotypic degrees in the
  coinvariant algebra): $m=1{:}\ (0,\dots,n-1)$; $p<m{:}\
  (1, 1+m, \ldots, 1+(n-1)m)$; $p=m$, $n=2{:}\ (1,m-1)$;
  $p=m$, $n\ge 3{:}\ (1,\ 1+m,\ \ldots,\ 1+(n-2)m$ with the top entry replaced
  by $(n-1)m-n+1)$.
- **Coexponents** (support of $F_{V^*}$): $m=1{:}\ (0,\dots,n-1)$;
  $p<m$, generic: $(m-1, 2m-1, \ldots, nm-1)$; non-generic fibres:
  $G(4,2,2){:}\ (3,3)$; $G(6,2,2){:}\ (5,5)$; $G(6,3,2){:}\ (3,5)$;
  $G(4,2,3){:}\ (3,5,7)$; $G(6,2,3){:}\ (5,8,11)$; $G(6,3,3){:}\ (5,5,11)$;
  $G(4,2,4){:}\ (3,7,7,11)$; $G(6,2,4){:}\ (5,11,11,17)$;
  $G(6,3,4){:}\ (5,7,11,17)$; $p=m{:}\ n=2{:}\ (1,m-1)$ ($m>2$), $(1,1)$ for
  $G(2,2,2)$; $n=3{:}\ (1,2,3), (2,2,5), (2,3,7), (2,4,9), (2,5,11)$ for
  $m=2,3,4,5,6$; $n=4{:}\ (1,3,3,5), (2,3,5,8), (3,3,7,11), (3,4,9,14),
  (3,5,11,17)$ for $m=2,3,4,5,6$.

### The G(4,2,2) non-Coxeter splitting witness (certified)

$G(4,2,2)$: $|G| = 16$, degrees $(4,4)$,
$M(t) = 1/(1-t^4)^2 = \sum_{k\ge 0}(k+1)t^{4k}$
(first 8 Molien coefficients `1,0,0,0,2,0,0,0`, matching the lattice count),
$F_V(t) = t+t^5$ (exponents $(1,5)$), $F_{V^*}(t) = 2t^3$ (coexponents
$(3,3)$), $F_V(1) = F_{V^*}(1) = 2$, Gram $(1,0,1,0)$, 6 reflections (all
order 2), 4 hyperplanes. Contrast $S_4$ (degrees $(1,2,3,4)$,
$F_V = 1+t+t^2+t^3$): no symmetric group has a repeated degree, and none has
a multiplicity-2 coexponent $2t^3$; the repeated-degree splitting is a
non-Coxeter phenomenon. Full record in `artifacts/witness.json`.

## 2. Full 42-group table

Columns: group; $|G|$; degrees; coexponents; $F_V$; $F_{V^*}$; $F(1)$.
(Molien-to-$t^{30}$, product, reflection/hyperplane, Gram gates all pass;
see `artifacts/table.csv` / `table_full.json`.)

| group | $|G|$ | degrees | coexponents | $F_V$ | $F_{V^*}$ | $F(1)$ |
|---|---|---|---|---|---|---|
| G(1,1,2) | 2 | [1,2] | [0,1] | [1,1] | [1,1] | 2 |
| G(2,1,2) | 8 | [2,4] | [1,3] | t+t^3 | t+t^3 | 2 |
| G(2,2,2) | 4 | [2,2] | [1,1] | 2t | 2t | 2 |
| G(3,1,2) | 18 | [3,6] | [2,5] | t+t^4 | t^2+t^5 | 2 |
| G(3,3,2) | 6 | [2,3] | [1,2] | t+t^2 | t+t^2 | 2 |
| G(4,1,2) | 32 | [4,8] | [3,7] | t+t^5 | t^3+t^7 | 2 |
| G(4,2,2) | 16 | [4,4] | [3,3] | t+t^5 | 2t^3 | 2 |
| G(4,4,2) | 8 | [2,4] | [1,3] | t+t^3 | t+t^3 | 2 |
| G(5,1,2) | 50 | [5,10] | [4,9] | t+t^6 | t^4+t^9 | 2 |
| G(5,5,2) | 10 | [2,5] | [1,4] | t+t^4 | t+t^4 | 2 |
| G(6,1,2) | 72 | [6,12] | [5,11] | t+t^7 | t^5+t^11 | 2 |
| G(6,2,2) | 36 | [6,6] | [5,5] | t+t^7 | 2t^5 | 2 |
| G(6,3,2) | 24 | [4,6] | [3,5] | t+t^7 | t^3+t^5 | 2 |
| G(6,6,2) | 12 | [2,6] | [1,5] | t+t^5 | t+t^5 | 2 |
| G(1,1,3) | 6 | [1,2,3] | [0,1,2] | 1+t+t^2 | 1+t+t^2 | 3 |
| G(2,1,3) | 48 | [2,4,6] | [1,3,5] | t+t^3+t^5 | t+t^3+t^5 | 3 |
| G(2,2,3) | 24 | [2,3,4] | [1,2,3] | t+t^2+t^3 | t+t^2+t^3 | 3 |
| G(3,1,3) | 162 | [3,6,9] | [2,5,8] | t+t^4+t^7 | t^2+t^5+t^8 | 3 |
| G(3,3,3) | 54 | [3,3,6] | [2,2,5] | t+2t^4 | 2t^2+t^5 | 3 |
| G(4,1,3) | 384 | [4,8,12] | [3,7,11] | t+t^5+t^9 | t^3+t^7+t^11 | 3 |
| G(4,2,3) | 192 | [4,6,8] | [3,5,7] | t+t^5+t^9 | t^3+t^5+t^7 | 3 |
| G(4,4,3) | 96 | [3,4,8] | [2,3,7] | t+t^5+t^6 | t^2+t^3+t^7 | 3 |
| G(5,1,3) | 750 | [5,10,15] | [4,9,14] | t+t^6+t^11 | t^4+t^9+t^14 | 3 |
| G(5,5,3) | 150 | [3,5,10] | [2,4,9] | t+t^6+t^8 | t^2+t^4+t^9 | 3 |
| G(6,1,3) | 1296 | [6,12,18] | [5,11,17] | t+t^7+t^13 | t^5+t^11+t^17 | 3 |
| G(6,2,3) | 648 | [6,9,12] | [5,8,11] | t+t^7+t^13 | t^5+t^8+t^11 | 3 |
| G(6,3,3) | 432 | [6,6,12] | [5,5,11] | t+t^7+t^13 | 2t^5+t^11 | 3 |
| G(6,6,3) | 216 | [3,6,12] | [2,5,11] | t+t^7+t^10 | t^2+t^5+t^11 | 3 |
| G(1,1,4) | 24 | [1,2,3,4] | [0,1,2,3] | 1+t+t^2+t^3 | 1+t+t^2+t^3 | 4 |
| G(2,1,4) | 384 | [2,4,6,8] | [1,3,5,7] | t+t^3+t^5+t^7 | t+t^3+t^5+t^7 | 4 |
| G(2,2,4) | 192 | [2,4,4,6] | [1,3,3,5] | t+2t^3+t^5 | t+2t^3+t^5 | 4 |
| G(3,1,4) | 1944 | [3,6,9,12] | [2,5,8,11] | t+t^4+t^7+t^10 | t^2+t^5+t^8+t^11 | 4 |
| G(3,3,4) | 648 | [3,4,6,9] | [2,3,5,8] | t+t^4+t^6+t^7 | t^2+t^3+t^5+t^8 | 4 |
| G(4,1,4) | 6144 | [4,8,12,16] | [3,7,11,15] | t+t^5+t^9+t^13 | t^3+t^7+t^11+t^15 | 4 |
| G(4,2,4) | 3072 | [4,8,8,12] | [3,7,7,11] | t+t^5+t^9+t^13 | t^3+2t^7+t^11 | 4 |
| G(4,4,4) | 1536 | [4,4,8,12] | [3,3,7,11] | t+t^5+2t^9 | 2t^3+t^7+t^11 | 4 |
| G(5,1,4) | 15000 | [5,10,15,20] | [4,9,14,19] | t+t^6+t^11+t^16 | t^4+t^9+t^14+t^19 | 4 |
| G(5,5,4) | 3000 | [4,5,10,15] | [3,4,9,14] | t+t^6+t^11+t^12 | t^3+t^4+t^9+t^14 | 4 |
| G(6,1,4) | 31104 | [6,12,18,24] | [5,11,17,23] | t+t^7+t^13+t^19 | t^5+t^11+t^17+t^23 | 4 |
| G(6,2,4) | 15552 | [6,12,12,18] | [5,11,11,17] | t+t^7+t^13+t^19 | t^5+2t^11+t^17 | 4 |
| G(6,3,4) | 10368 | [6,8,12,18] | [5,7,11,17] | t+t^7+t^13+t^19 | t^5+t^7+t^11+t^17 | 4 |
| G(6,6,4) | 5184 | [4,6,12,18] | [3,5,11,17] | t+t^7+t^13+t^15 | t^3+t^5+t^11+t^17 | 4 |

## 3. Method (reproducible)

`artifacts/replay.py` (stdlib only, pinned: Python 3.12.3; run time ~7 min
single core): exact cyclotomic arithmetic in $\mathbf Z[\zeta_m]$ as
polynomial vectors mod $\Phi_m$ with `Fraction` coefficients; group
enumeration as permutation + phase-vector pairs with the $p$-constraint;
type aggregation by cycle-phase multiset (distinct denominators cached —
at most 6 for $G(4,2,2)$); Molien series by exact series inversion of
$\prod_C(1-\zeta^{s_C}t^{\ell_C})$; fake degrees by character-weighted
isotypic series times $\prod(1-t^{d_i})$ with Galois-conjugation deviation
diagnostics (all $0$); Gram numbers by exact weighted class sums; hyperplane
keys distinguishing coordinate vs phase-ratio transposition type. Outputs:
`table.csv`, `table_full.json` (per-group: Molien vectors to $t^{30}$,
$F_V/F_{V^*}$, Gram, reflection/hyperplane data), `witness.json`
($G(4,2,2)$ vs $S_4$), `burnside.json` (lattice cross-check log).

## 4. Limitations, uncertainties, and what is NOT claimed

- **Formulas vs computation.** The degree formula, exponent/coexponent tables,
  hyperplane counts and irreducibility/Gram expectations are classical
  (Shephard–Todd / Orlik–Solomon / Steinberg); the contribution is the
  machine-checked exact census and replay certificate on this 42-group slice,
  not discovery of the formulas. The closed-form tables in §1 were fitted to
  — and then verified against — the exact series output (42/42), not derived
  inside the script from first principles.
- **Scope.** Only $n \le 4$, $m \le 6$ (max order $31104$) are enumerated; no
  claim is made outside this slice. Full character tables and all-irrep fake
  degrees are not computed — only the reflection representation $V$ and its
  dual, and only the row-Gram on $\{1, V, \bar V\}$, not full orthogonality.
- **Conventions.** $m=1$ rows are the permutation representation of $S_n$
  (reducible, contains $1$; generalized exponents $(0,\dots,n-1)$), and
  $G(2,2,2)$ is abelian with $V$ splitting into two linear characters
  ($\langle V,V\rangle = 2$); both are flagged, not hidden.
- **The "Burnside" label.** An early naive diagonal-fixed-point cross-check
  was found wrong during the run (it undercounts by the phase-torus factor)
  and was replaced by the generator-multidegree lattice count, which is the
  recorded independent check. The script retains the dead helper
  `count_fixed_monomials` (unused); it is not part of any gate.
- **No $S_n$-impossibility theorem proved.** The witness contrast is at the
  level of certified data (repeated degree $(4,4)$ and multiplicity-2
  coexponent vs distinct exponents $(0,1,2,3)$ for $S_4$), not a new
  structural theorem about symmetric groups.
