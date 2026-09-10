# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Validated May–Steenrod window at p=3 to stem 40 with a certified
# V(1)-twist obstruction (machine-checked, stdlib-only)

## Abstract
We build from scratch a machine-checked mod-3 Steenrod-algebra engine
(admissible basis, Adem relations $P^aP^b$ / $P^a\beta P^b$, $\beta^2=0$),
verify the $H^*V(1)$ module structure, compute a validated May spectral
sequence E1/d1/E2 window for the sphere at $p=3$ ($s\le 8$, $t\le 41$,
517 E1 monomials, $d_1^2=0$ on all generators, textbook anchors
$E_2^{1,1}=a_0$, $E_2^{1,4}=h_{10}$, $E_2^{2,12}(\beta_1)$ all of dimension 1),
tabulate the full E2 page in the window (in particular sphere
$\dim E_2^{6,40}=5$, $\dim E_2^{8,41}=6$), and certify a structural
obstruction: the naive $V(1)$-twisted May differential fails $d^2=0$ with
nonzero residue $-a_0h_{10}e_5$ (the class $[a_0h_{10}]$ is nonzero in
May-E2 at $(s,t)=(2,5)$, and $E_1^{1,5}=\{a_1\}$ with $d_1(a_1)=0$, so no
canceling source exists). A measured census (1,552,353 admissible monomials
$\le 41$; $\dim A_{40}=328{,}962$, $\dim A_{41}=473{,}119$) quantifies why
naive full-Steenrod resolution to the $(34,6)$ cell is infeasible and
redirects future $V(1)$ attacks to chart-anchored twists. We do NOT decide
the classical $d_2(x)$ at $(34,6)$ and do NOT certify motivic E3 survival:
this report states exactly what is proved, what is computed, and what is
blocked.

## 1. Conventions (logged; everything keyed to these)
- Prime $p=3$. Graded mod-3 Steenrod algebra with generators $\beta$
  ($|\beta|=1$) and $P^i$ ($|P^i|=4i$); Adem relations as in the code
  (`adem_PP`, `adem_PbP` in `check_ext.py`); $\beta^2=0$.
- Monomial degree = sum of factor degrees; admissibility = standard
  ($P^aP^b$ with $a<3b$ inadmissible; $P^a\beta P^b$ with $1\le a\le 3b$
  inadmissible).
- $H^*V(1)=\mathrm{span}\{e_0,e_1,e_5,e_6\}$, $|e_i|=i$, with
  $\beta(e_0)=e_1$, $\beta(e_5)=e_6$, $P^1(e_1)=e_5$, all else 0 on generators.
- May E1 (sphere): $|a_n|=(s,t)=(1,2(3^n-1)+1)$; $|h_{ij}|=(1,2(3^i-1)3^j)$;
  $|b_{ij}|=(2,2(3^i-1)3^{j+1})$; $d_1(a)=d_1(b)=0$ (verified on generators);
  $d_1(h_{ij})=\sum_{k=1}^{i-1}h_{k,j}h_{i-k,j+k}$ with ordered-squarefree
  $h$-products and Koszul signs (all $h$ odd, all $a$/$b$ even).
  Truncation: products landing outside $s\le 8$, $t\le 41$ are dropped
  (logged in `mul`).

## 2. What is PROVED vs COMPUTED (separation)
- PROVED (by machine-checked certificate, rerunnable):
  (a) Poincare-series check: computed admissible dims 0–9 =
  1,1,0,0,1,2,1,0,1,2 (matches hand product
  $(1+t)(1+t^4+t^8)(1+t^5)$ to degree 8 and the listed deg-9 census
  $\{\beta P^2, P^2\beta\}$ giving 2).
  (b) 40/40 random associativity identities $(xy)z=x(yz)$ in the truncated
  algebra.
  (c) Every tested Adem-relation instance ($\beta^2$, $P^aP^b$ for
  $1\le a<3b$, $P^a\beta P^b$ for $1\le a\le 3b$ in range) acts as 0 on all
  four $H^*V(1)$ basis elements — i.e. the encoded $H^*V(1)$ satisfies the
  module axioms over the tested relations.
  (d) $d_1^2=0$ on every E1 generator in the window.
  (e) Twist obstruction: for the derived cobar twist
  $d_{tw}(e_0)=a_0e_1$, $d_{tw}(e_5)=a_0e_6$, $d_{tw}(e_1)=h_{10}e_5$,
  $d_{tw}(e_6)=0$ (with $d_{May}(a_0)=d_{May}(h_{10})=0$), one has
  $d^2(e_0)=-a_0h_{10}e_5\ne 0$ in E1, and $a_0h_{10}$ is not a $d_{May}$
  boundary (sole possible source bidegree $(1,5)$ contains only $a_1$ with
  $d_1(a_1)=0$; $[a_0h_{10}]\ne 0$ in May-E2 at $(2,5)$, dim 1).
- COMPUTED (evidence, convention-dependent): the full May-E2 table in the
  window (artifact stdout), anchors, cocycle representatives at
  $(6,40)$/$(8,41)$, and the admissible-basis census.
- NOT claimed: any value of classical $d_2(x)$, any motivic $d_2(\tilde x)$,
  any Moss-convergence statement, any permanent-cycle claim.

## 3. Results
1. **Validated sphere May window** (`may_window.py`): 517 E1 monomials;
   $d_1^2=0$ TRUE; anchors $E_2(1,1)=E_2(1,4)=E_2(2,12)=1$; full E2 table to
   $t=41$ (stdout), including $E_2(6,40)$ dim 5, $E_2(8,41)$ dim 6.
2. **Certified twist obstruction** (`twist_check.py` + re-verification):
   naive $V(1)$-twisted May $d_1$ fails $d^2=0$; obstruction class
   $[a_0h_{10}]$ is permanent at May-E2 $(2,5)$. Any $V(1)$ May-SS
   construction must resolve this cofiber $k$-invariant — a precise,
   checkable redirect for future work.
3. **Steenrod/$H^*V(1)$ engine certificate** (`check_ext.py`): (a)–(c) above.
4. **Infeasibility census** (`enumerate.py`): 1,552,353 admissible monomials
   of degree $\le 41$ (22 s); $\dim A_{40}=328{,}962$,
   $\dim A_{41}=473{,}119$ — naive minimal resolution to the target cells
   needs single-degree matrices of order $\sim 10^5$–$10^6$ over $\mathbf F_3$
   across 8 syzygy rounds: infeasible in-session, quantified not hand-waved.
5. **Negative probes** (`may_probe.py`, F1 in-worklog): an $h$-only May
   monomial search finds no $(6,34)$ class (consistent with the need for the
   $V(1)$-cell shift), and the motivic weight/cell-reading probe shows
   competing $(34,6,17)$ readings with no chart to select $\tilde x$ —
   documenting the exact missing datum rather than guessing it.

## 4. How to replay (verification-critical files only)
- `python3 output/artifacts/check_ext.py` → JSON (exit 0):
  `poincare_check_PASS=true`, `associativity_spot_PASS=true`,
  `HV1_module_axioms_PASS=true`, `TARGET_CELL_STATUS=OUT_OF_RANGE`.
- `python3 output/artifacts/may_window.py` → JSON (exit 0):
  `n_E1_monomials=517`, `d1_squared_zero_on_gens=true`,
  `anchor_(1,1)=anchor_(1,4)=anchor_(2,12)=1`, full E2 table.
- `python3 output/artifacts/twist_check.py` → JSON (exit 0):
  `status=TWIST_OBSTRUCTION_CERTIFIED`.
- `python3 output/artifacts/enumerate.py` → JSON (exit 0):
  `total=1552353`, dims $A_{40}$, $A_{41}$ as above.
- All scripts stdlib-only. Wall times: check_ext ~s, may_window ~s,
  twist_check instant, enumerate ~22 s.

## 5. Limitations and open data needed
- The $(34,6)$ classical pin and $(34,6,17)$ motivic pin need the published
  Ravenel/Shimomura $V(1)$ Ext chart rows (unavailable offline; one chart-PDF
  fetch returned 403) and the cofiber $k$-invariant correction to the
  twisted May $d_1$; the motivic $d_2(\tilde x)=0$ certificate and Moss check
  are downstream of that pin and are NOT supplied here.
- May-E2 dims are for the sphere with the conventions of §1; the $V(1)$
  (resp. motivic-$V(1)$) E2 pages require the twist resolution in §3.2.
- No Toda-bracket, Moss, hidden-extension, or Betti-realization claim is made.

## 6. Prior-art relation (no overclaim)
Nearest priors supply general machinery (Belmont–Kong multiplicative
Moss/Toda convergence; Dugger–Isaksen and Hu–Kriz–Ormsby motivic
construction/convergence) or a different spectral sequence (Shimomura
$L_2$-ANSS $E_{10}=E_\infty$ with $d_5$/$d_9$; Carrick–Davies synthetic
$v_2$-periodic nonvanishing). None records a from-scratch May-E2 table to
$t=41$ at $p=3$ or the $a_0h_{10}$ $V(1)$-twist obstruction certificate;
the bracket value, Moss check, and $d_2$ decision of the target remain open.
