# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact Cayley diameters and spectral gaps for explicit two-generated
# nonabelian groups of orders 48--64, with an extremal witness and a
# gap--diameter decoupling certificate

## 1. Claim

We certify an exact-diameter plus spectral-gap table for **25 Cayley graphs**
arising from **23 explicit two-generated nonabelian groups** whose orders cover
**every nonabelian order in the band 48--64** (48, 50, 52, 54, 55, 56, 57, 58,
60, 62, 63, 64). For each row, with symmetric generating set
$S=\{a,b,a^{-1},b^{-1}\}$ and degree $d=|S|$:

- (a) the **exact diameter** $D$ by all-pairs breadth-first search over the
  stored multiplication table (pure integer arithmetic), with a shortest word
  over $\{a,b,A,B\}$ for **every** group element, each re-evaluated to its
  element, plus a diameter-witness word of length $D$;
- (b) the **spectral gap** $d-\lambda_2$ with two-sided interval
  $[\mathrm{gap}_{lo},\mathrm{gap}_{hi}]$ of half-width $10^{-9}$, cross-checked
  by two independent eigensolvers (`eigh` and `eig`) agreeing to $<2.5\times
  10^{-14}$, Ritz residuals $<10^{-13}$, exact top eigenvalue $d$ (constant
  vector), and trace checks $\sum\mu_i=0$, $\sum\mu_i^2=nd$;
- (c) the **extremal row**: two-reflection generators of the order-64 dihedral
  group give the 2-regular cycle $C_{64}$ with diameter **32**, the largest in
  the table;
- (d) a **gap--diameter decoupling**: e.g. UT$_3(\mathbf{Z}_4)$ at order 64 has
  diameter $6$ and gap $\approx 1.17157$, while the Frobenius group
  $C_{11}\rtimes C_5$ at order 55 has diameter $4$ and gap $\approx 1.00829$:
  larger diameter coexists with a (disjoint-interval) larger gap, so neither
  invariant orders the other. Five such strict pairs are certified.

Lemma (proved). The order-64 semidihedral and modular 2-groups with their
canonical generators have **isomorphic** Cayley graphs (explicit intertwiner
$f(e,k)=(e,(-1)^e k)$, machine-checked on the stored tables), hence rigorously
equal diameters ($9$) and spectra (gap $\approx 0.152241$).

## 2. Scope and generating-pair rule (read before auditing)

No GAP/SmallGroups library exists in this environment (Python stdlib + numpy
only), so the full SmallGroups transversal of the original audit plan is
replaced by the following fully documented rule, and the claim is adjusted
accordingly (this matches the topic's own fallback: certified exact diameters
with two-sided gap intervals):

- Each group is constructed from scratch (presentations in Section 3) as an
  explicit element list with identity first and a multiplication function;
  the builder verifies **full associativity** $O(n^3)$, identity, inverses,
  a noncommuting pair, and closure-from-generators $= n$ (order/generation
  check, equivalent to Schreier--Sims at this scale).
- **Canonical pair**: the lexicographically first ordered pair of non-identity
  indices $(i,j)$, $i\ne j$, whose closure is the whole group (complete search
  over all $n^2$ pairs; logged in `census.py`). Two extra rows are documented
  **alternate** bireflection pairs. This is one canonical pair per group, not
  a full $\mathrm{Aut}(G)$-orbit transversal -- see Limitations.
- $D8\times C_8$ (order 64) was tested and **certified not 2-generated**
  (all 4096 ordered pairs fail closure; abelianization $C_2^2\times C_8$ needs
  three generators) and is excluded. Orders 49, 51, 53, 59, 61 admit no
  nonabelian groups and are correctly absent.

## 3. Groups (presentations; `*` = alternate pair row)

Dihedral $D_{2m}=\langle r,s\mid r^m=s^2=1,\ srs=r^{-1}\rangle$, $m=24,\dots,32$
(orders 48--64, canonical pair $(r,s)$, degree 3; alternates $(s,rs)$, degree 2,
for $m=24,32$). Frobenius $C_{11}\rtimes C_5$ ($yxy^{-1}=x^3$),
$C_{19}\rtimes C_3$ ($x\mapsto x^7$), $C_7\rtimes C_9$ via the $C_3$ quotient
($x\mapsto x^2$), $C_{13}\rtimes C_4$ ($x\mapsto x^5$). Dicyclic
$\mathrm{Dic}(M)=\langle a,x\mid a^M=1,x^2=a^{M/2},x^{-1}ax=a^{-1}\rangle$,
$M=24,28,32$ (last is generalized quaternion $Q_{64}$).
$GL(2,3)$ ($2\times2$ matrices over $\mathbf{F}_3$, $\det\ne0$, order 48).
$S_3\times C_8$ (order 48). $\mathrm{Heis}(\mathbf{F}_3)\times C_2$ (order 54).
$A_5$ (even permutations of 5, order 60). $UT_3(\mathbf{Z}_4)$ upper-triangular
ones-on-diagonal $3\times3$ over $\mathbf{Z}_4$ (order 64). Semidihedral
$\langle r,s\mid r^{32}=s^2=1,srs=r^{15}\rangle$ and modular
$\langle a,b\mid a^{32}=b^2=1,bab=a^{17}\rangle$ (order 64).

## 4. Results table (exact $D$; gaps to 6dp with $\pm10^{-9}$ intervals)

```text
id   order  structure            d   D  lambda2    gap       witness word (len D)
R00  48     Dihedral_2x24        3  13  2.931852  0.068148  (see words.json)
R01  50     Dihedral_2x25        3  13  2.937166  0.062834  ...
R02  52     Dihedral_2x26        3  14  2.941884  0.058116  ...
R03  54     Dihedral_2x27        3  14  2.946090  0.053910  ...
R04  56     Dihedral_2x28        3  15  2.949856  0.050144  ...
R05  58     Dihedral_2x29        3  15  2.953241  0.046759  ...
R06  60     Dihedral_2x30        3  16  2.956295  0.043705  ...
R07  62     Dihedral_2x31        3  16  2.959060  0.040940  ...
R08  64     Dihedral_2x32        3  17  2.961571  0.038429  ...
R09  55     Frob_C11_C5          4   4  2.618034  1.381966  ...
R10  57     Frob_C19_C3          4   4  2.991715  1.008285  ...
R11  63     Frob_C7_C9           4   5  3.532089  0.467911  ...
R12  52     Frob_C13_C4          4   4  2.738060  1.261940  ...
R13  48     Dic12                4   7  3.732051  0.267949  ...
R14  56     Dic14                4   8  3.801938  0.198062  ...
R15  48     GL(2,3)              3   6  2.414214  0.585786  ...
R16  48     S3xC8                3   7  2.645751  0.354249  ...
R17  54     Heis(F3)xC2          4   5  3.000000  1.000000  ...
R18  60     A5                   4   6  3.236068  0.763932  ...
R19  64     UT3(Z4)              4   6  2.828427  1.171573  ...
R20  64     Semidihedral         3   9  2.847759  0.152241  ...
R21  64     Modular              3   9  2.847759  0.152241  ...
R22  64     Q64 (Dic16)          4   9  3.847759  0.152241  ...
R23* 48     Dihedral_2x24 alt    2  24  1.982890  0.017110  ...
R24* 64     Dihedral_2x32 alt    2  32  1.990369  0.009631  ...
```

Full precision, per-element words, distance distributions, spectra, generator
labels, and presentations are in `artifacts/cayley_table.csv` and
`artifacts/words.json`. Pearson correlation of $(D,\mathrm{gap})$ over the 25
rows is $-0.69$: negative trend with certified exceptions.

Diameter-vs-gap scatter (each `*` a row; gaps on log-ish scale):

```text
gap  1.4 | * (R09 D4)
     1.2 | * (R12 D4)  * (R19 D6)
     1.0 | * (R10 D4)  * (R17 D5)
     0.7 |             * (R18 D6)
     0.5 | * (R15 D6)    * (R11 D5)
     0.3 |   * (R13/R16 D7)
     0.15|         * (R14 D8)  * (R20/21/22 D9)
     0.06|                       * (dihedrals D13-14)
     0.04|                                 * (dihedrals D15-17)
     0.01|                                                 * (R23 D24, R24 D32)
         +--------------------------------------------------------
           4  5  6  7  8  9      13  14  15  16  17      24  32  (D)
```

## 5. Proofs and computed evidence (separated)

**Proof (Lemma).** Write $SD_{64}=\langle r,s\rangle$, $M_{64}=\langle u,v\rangle$
with $srs=r^{15}$, $vuv=u^{17}$, $17\equiv-15\pmod{32}$. Index elements
$(e,k)$, $e\in\{0,1\}$, $k\in\mathbf{Z}_{32}$ (identity $(0,0)$ first). The map
$f(e,k)=(e,(-1)^e k)$ is a bijection; rotation edges $(e,k)\sim(e,k\pm1)$ are
preserved since $k\mapsto-k$ reverses each 32-cycle (undirected: identical),
and the reflection matching $(0,k)\sim(1,15k)$ maps to
$(0,k)\sim(1,-15k)=(1,17k)$, exactly the modular matching. Hence the two
labeled Cayley graphs are isomorphic; diameters, spectra, gaps coincide.
The intertwiner is re-checked entry-by-entry from the stored tables by
`replay.py` (stdlib integer work). The groups themselves are non-isomorphic (17 vs 3
involutions: $(1,k)^2=(0,16k)$ resp.\ $(0,18k)$), so this is a genuine
Cayley-graph coincidence, not a group isomorphism.

**Computed evidence (exact part).** Diameters, words, generation, associativity,
nonabelian witnesses are exact integer computations, independently re-derived
from the stored tables by `replay.py`: 25/25 rows PASS, all-pairs diameters
recomputed, every word re-evaluated, witness lengths confirmed.

**Computed evidence (spectral part).** Two LAPACK routes agree to
$<2.5\times10^{-14}$; Ritz residuals $<10^{-13}$; $\lambda_1=d$ exact
(row sums); trace identities hold; top separation $\gg$ residuals on all rows;
reported intervals $\pm10^{-9}$ exceed all observed numeric error by
$\sim 5$ orders of magnitude, while every decoupling margin below exceeds
$0.11$. Gap values are therefore *computed with audited intervals*, not
formally proved enclosures.

**Decoupling certificate.** Strict pairs (bigger $D$, disjoint-bigger gap):
(R19 vs R10: $6>4$, $[1.171572,1.171574]>[1.008284,1.008286]$),
(R19 vs R11), (R18 vs R11), (R19 vs R17), (R15 vs R11). All margins survive the
intervals; replay re-checks gap containment.

**Numerical observations (NOT claimed).** Several $\lambda_2$ values match
algebraic integers to 6dp: A5 $\approx2\varphi$, UT$_3\approx2\sqrt2$,
GL(2,3) $\approx1+\sqrt2$, Dic12 $\approx2+\sqrt3$, Frob55 $\approx1+\varphi$,
Heis $\approx3$ exactly, SD/Mod $\approx1+2\cos(\pi/8)$,
Q64 $\approx2+2\cos(\pi/8)$. Offered as conjectures for exact follow-up, not
as results.

## 6. Reproduction

```text
python3 output/artifacts/census.py            # rebuilds table + words.json (needs numpy; ~2 min)
python3 output/artifacts/replay.py output/artifacts/words.json   # independent check (stdlib; numpy rechecks gaps if present)
```

`replay.py` shares no code with `census.py` beyond the JSON schema: it
re-verifies associativity, generation, BFS distances, all word evaluations,
the all-pairs diameter, the gap intervals, and the Lemma intertwiner.

## 7. Limitations (honest)

1. One canonical pair per group, not a full $\mathrm{Aut}(G)$ transversal, and
   23 explicit groups, not the whole SmallGroups 48--64 library (267 groups at
   order 64 alone). The extremal ($D=32$) is maximal *in this census*, not
   proven maximal over all 2-generated groups of orders 48--64.
2. Spectral gaps are dual-solver computed values with audited $\pm10^{-9}$
   intervals, not interval-arithmetic theorems; only diameters/words/lemma are
   exact proofs.
3. No claim that the observed algebraic-integer $\lambda_2$ values are exact.
4. Q64 sharing $\lambda_2$'s fractional part with SD/Mod to 12dp is an
   unexplained numerical coincidence, flagged, not explained.

## References

- H. U. Besche, B. Eick, E. A. O'Brien, A millennium project: constructing
  small groups, Int. J. Algebra Comput. 12 (2002) -- the SmallGroups library
  (enumeration infrastructure; not available in this environment).
- Standard Cayley/spectral-graph background: Godsil--Royle; Chung; Diaconis--
  Saloff-Coste (gap vs diameter bounds -- universal inequalities, disjoint
  from this computed census).
