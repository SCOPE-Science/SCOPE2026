# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Attained lattice-width-1 table and hollow witness for centrally symmetric lattice 3-polytopes (even volumes 4–48)

## 1. Objects and normalizations

A **lattice polytope** is $P=\mathrm{conv}(v_1,\dots,v_n)$ with $v_i\in\mathbb Z^3$,
full-dimensional. Its **normalized volume** is $\mathrm{Vol}(P)=3!\,\mathrm{vol}(P)\in\mathbb Z_{\ge 1}$.
$P$ is **centrally symmetric** if there is $c\in \tfrac12\mathbb Z^3$ with
$x\mapsto 2c-x$ permuting the vertex set (hence preserving $P$).
The lattice width in direction $0\ne u\in\mathbb Z^3$ is
$w_u(P)=\max_P u-\min_P u$, and the **lattice width** is
$w(P)=\min_{0\ne u\in\mathbb Z^3} w_u(P)$.
$P$ is **hollow** if $\mathrm{int}(P)\cap\mathbb Z^3=\varnothing$.
$L_P(t)=|tP\cap\mathbb Z^3|$ is the Ehrhart count.

**General-center convention.** The claim below allows half-integer centers
$c\in\tfrac12\mathbb Z^3$ (not only $c=0$). This is the standard meaning of
"centrally symmetric lattice polytope" and is what makes small volumes such as
$V=6$ attainable (the unit cube $[0,1]^3$, $V=6$, center $(1/2,1/2,1/2)$).
Origin-symmetric-only would exclude $V\equiv 2\pmod 4$ in some subfamilies;
the wider (standard) convention is used throughout, and every row's center is
committed explicitly.

## 2. Theorem (attained-width-1 table + hollow witness)

**Theorem.** For every even integer $V\in\{4,6,\dots,48\}$ there exists an
explicit full-dimensional centrally symmetric lattice $3$-polytope $P_V$ with
$\mathrm{Vol}(P_V)=V$, lattice width $w(P_V)=1$ (attained at $u^*=(0,0,1)$),
and $P_V$ hollow. In particular the minimum attained lattice width over this
class at each such volume is $1$ (it cannot be $0$ for a full-dimensional body).
The largest-volume witness $P_{48}$ has $22$ lattice points, none interior,
with dilate counts $L(0..3)=(1,22,111,316)$.

The witnesses are two explicit twisted-prism families (vertices in §4, machine
table in `artifacts/polytope_table.json`, human table in
`artifacts/width_table.csv`):

- **Family T** ($V\equiv 0\pmod 4$ plus 28, 44): for a lattice triangle
  $T\subset\mathbb Z^2$ put
  $$P = \mathrm{conv}\bigl(T\times\{0\}\;\cup\;(-T)\times\{1\}\bigr),$$
  symmetric about $c=(0,0,1/2)$ (committed $2c=(0,0,1)$).
  Since $P$ lies between the planes $z=0$ and $z=1$, $w_{(0,0,1)}(P)=1$, so
  $w(P)=1$ (a full-dimensional lattice polytope always has $w\ge 1$ since some
  integer functional is non-constant on it).
- **Family Q** ($V\equiv 2\pmod 4$): for $A_k=\mathrm{conv}\{(0,0),(k,0),(0,1),(1,1)\}$
  put
  $$P_k = \mathrm{conv}\bigl(A_k\times\{0\}\;\cup\;A_k'\times\{1\}\bigr),
    \qquad A_k'=(1,1)-A_k,$$
  symmetric about $c=(1/2,1/2,1/2)$ (committed $2c=(1,1,1)$).
  Again $0\le z\le 1$ on $P_k$, so $w_{(0,0,1)}(P_k)=1$ and $w(P_k)=1$.

**Volume computation (by hand-checkable formulas).**
For $T_{b,h}=\mathrm{conv}\{(0,0),(b,0),(0,h)\}$ the prism has
$\mathrm{Vol}=2\cdot b\cdot h$ (normalized area of $T$ is $bh$, doubled because
the convex hull of the two opposite triangles has normalized volume
$2\,\mathrm{area}_2(T)$; verified row-wise by the fan computation).
This gives $4,8,12,16,20,24,32,36,40,48$ for the $(b,h)$ choices
$(1,1),(2,1),(3,1),(4,1),(5,1),(3,2),(4,2),(3,3),(5,2),(4,3)$.
For $A_k$ ($k\ge 2$; normalized area $k+1$ by decomposition into the
$k\times 1$ rectangle of area $2k$ minus two unit half-triangles... directly:
shoelace $=k+1$) the twisted prism has $\mathrm{Vol}=4k+2$; explicitly
$k=1,\dots,11$ give $6,10,14,\dots,46$ (row-wise fan-verified).
The two non-right triangles give $V=28$ (triangle $(0,0),(1,2),(4,1)$,
normalized area $7$, doubled) and $V=44$ (triangle $(0,0),(1,3),(4,1)$,
normalized area $11$, doubled).

*Remark on "doubling".* For the origin-symmetric construction
$P=\mathrm{conv}(T\times0\cup(-T)\times1)$, $\mathrm{Vol}(P)=2\,\mathrm{area}_2(T)$
holds because $P$ is the union (up to measure zero) of two copies of the
prism-over-$T$ construction glued along $T\times\{0\}$-type sections; the
verifier independently recomputes every volume by the hull-fan determinant sum,
so the closed form is a guide and the certificate is the exact determinant sum.

**Hollowness (no enumeration needed for the proof).** Every witness lies in the
slab $0\le z\le 1$. The only integer planes meeting $P$ are $z=0$ and $z=1$;
both are boundary planes of $P$ (each contains a full facet: the bottom/top
triangle or quadrilateral). Hence every lattice point of $P$ lies on the
boundary: $\mathrm{int}(P)\cap\mathbb Z^3=\varnothing$. The machine check
additionally enumerates the bounding box and confirms $n_{\mathrm{int}}=0$
row-wise.

**Width exactly 1.** $w\le 1$ via $u^*=(0,0,1)$; $w\ge 1$ because $P$ is a
full-dimensional lattice polytope (any nonzero integer functional taking two
distinct integer values differs by at least 1). The verifier additionally
exhausts all primitive directions with $\|u\|_\infty\le 8$ and finds minimum
$1$ in every row (recorded search bound $B=8$).

## 3. What is proved vs computed vs open

- **Proved (by the argument above from the committed vertices):** for each even
  $V\in[4,48]$ the committed $P_V$ is a centrally symmetric lattice
  3-polytope of normalized volume $V$, width exactly $1$, hollow.
  Consequently the per-volume *attained minimum* width over this class is $1$.
- **Computed evidence (machine replay):** exact volumes by merged-facet hull
  fan determinant sums; central-symmetry pairing checks; lattice-point and
  strict-interior enumerations; dilate counts $t=0..3$; exhaustive
  primitive-direction width search in box $B=8$. Replay with
  `python3 artifacts/verify.py` → `VERIFY_OK` (stdlib only, seconds).
- **Conjecture / explicitly open:** the per-volume *maximum* width side of the
  target claim (exact min–max table) is NOT established here — no extremal-max
  witnesses and no classification/obstruction certificates are supplied.
  The hollow witness is the maximal-volume ($V=48$) member of this width-1
  table, not a maximal-volume hollow polytope in any global sense.

## 4. Committed witnesses (exact vertices)

Family T (center $2c=(0,0,1)$; $u^*=(0,0,1)$; $w=1$):

| vol | bottom triangle $T$ (at $z=0$) | top $=-T$ (at $z=1$) |
|---|---|---|
| 4 | $(0,0),(1,0),(0,1)$ | $(0,0),(-1,0),(0,-1)$ |
| 8 | $(0,0),(2,0),(0,1)$ | $(0,0),(-2,0),(0,-1)$ |
| 12 | $(0,0),(3,0),(0,1)$ | $(0,0),(-3,0),(0,-1)$ |
| 16 | $(0,0),(4,0),(0,1)$ | $(0,0),(-4,0),(0,-1)$ |
| 20 | $(0,0),(5,0),(0,1)$ | $(0,0),(-5,0),(0,-1)$ |
| 24 | $(0,0),(3,0),(0,2)$ | $(0,0),(-3,0),(0,-2)$ |
| 28 | $(0,0),(1,2),(4,1)$ | $(0,0),(-1,-2),(-4,-1)$ |
| 32 | $(0,0),(4,0),(0,2)$ | $(0,0),(-4,0),(0,-2)$ |
| 36 | $(0,0),(3,0),(0,3)$ | $(0,0),(-3,0),(0,-3)$ |
| 40 | $(0,0),(5,0),(0,2)$ | $(0,0),(-5,0),(0,-2)$ |
| 44 | $(0,0),(1,3),(4,1)$ | $(0,0),(-1,-3),(-4,-1)$ |
| 48 | $(0,0),(4,0),(0,3)$ | $(0,0),(-4,0),(0,-3)$ |

Family Q (center $2c=(1,1,1)$; $u^*=(0,0,1)$; $w=1$;
bottom $A_k=\{(0,0),(k,0),(0,1),(1,1)\}$ at $z=0$,
top $(1,1)-A_k$ at $z=1$, i.e. $\{(1,1),(1-k,1),(1,0),(0,0)\}$):

| vol | $k$ | volume formula |
|---|---|---|
| 6 | 1 | unit cube $[0,1]^3$ |
| 10 | 2 | $4k+2$ |
| 14 | 3 | $4k+2$ |
| 18 | 4 | $4k+2$ |
| 22 | 5 | $4k+2$ |
| 26 | 6 | $4k+2$ |
| 30 | 7 | $4k+2$ |
| 34 | 8 | $4k+2$ |
| 38 | 9 | $4k+2$ |
| 42 | 10 | $4k+2$ |
| 46 | 11 | $4k+2$ |

Ehrhart/dilate data $(L(0),L(1),L(2),L(3))$ per row and lattice-point totals are
in `artifacts/width_table.csv` (23 rows); all rows hollow ($n_{\mathrm{int}}=0$).

## 5. Reproduction

```
cd output
python3 artifacts/verify.py
# VERIFY_OK: 23/23 rows (vols 4..48 even), symmetry+volume+width(B=8)+lattice/hollow+dilates all agree
```

Method: merged-facet convex-hull via coplanar grouping of all lattice triangles
(sign-canonicalized), normalized-volume fan determinant sum from vertex 0,
bounding-box lattice enumeration against exact facet half-spaces (strict for
interior), exhaustive primitive-direction width search in $|u|_\infty\le 8$.
SHA-256: see `research_report.json` artifact inventory.

## 6. Prior-art separation

Parametric classifications of empty 4-simplices (Iglesias-Valiño–Santos) and
flatness-threshold results (Codenotti et al.; Averkov et al.) give infinite
families and structural bounds, not a per-volume attained-width table with
replayed Ehrhart vectors for centrally symmetric 3-polytopes; the width-1
attained-minimum table and its certificates here are new as a finite checkable
artifact (no novelty is claimed for the width-$\ge$1 lemma or the fan-volume
method).
