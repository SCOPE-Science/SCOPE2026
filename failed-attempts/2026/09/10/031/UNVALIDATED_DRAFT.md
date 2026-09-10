# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharp Elliott-invariant obstruction witness for the Giol–Kerr perforated
minimal crossed product (TARGET draft)

## 1. Claim (target route)

**Pinned object.** Let $Z=S^{2}$, $Y=Z\times Z=S^{2}\times S^{2}$, and let
$(X_{GK},T)$ be the Giol–Kerr Section-3 minimal free subshift
$X_{GK}=\bigcap_{n}X_{n}\subset Y^{\mathbf Z}$ built by recursive blocking
$B_{n}=D_{n,1}\times\cdots\times D_{n,l_{n}}$ with lower $Y$-density
$d>1/2$ pinned e.g. at $d=3/5$ (any $d>1/2$ works; the construction allows
any $0<d<1$, and §3 explicitly assumes $d>1/2$ for the perforation step,
so $|\{i:D_{n,i}=Y\}|>l_{n}/2$ for all $n$).
Put $A_{GK}=C(X_{GK})\rtimes_{T}{\mathbf Z}$ (full$=$reduced for
${\mathbf Z}$). Then $A_{GK}$ is simple, unital, separable, nuclear,
stably finite and exact. (The word "Cantor" in the lane title is loose:
$X_{GK}$ is infinite compact metrizable minimal, not zero-dimensional.)

**Theorem (explicit witness + boundary lemma).**
Let $\xi\to Z$ be the Hopf line bundle, $\xi^{\times2}=\pi_{1}^{*}\xi\oplus
\pi_{2}^{*}\xi\to Y$ (rank $2$), $\theta_{r}$ the trivial rank-$r$ bundle,
$g=[\xi^{\times2}]-[\theta_{1}]\in K^{0}(Y)$, $\psi_{\infty}:C(Y)\to A_{GK}$
the $0$th-coordinate projection followed by the canonical embedding, and
$[w]=\psi_{\infty*}(g)\in K_{0}(A_{GK})$. Then:

- (a) **Certified pairing.** $\tau_{*}([w])=c=1$ for **every** tracial state
  $\tau$ on $A_{GK}$ (trace simplex is infinite-dimensional; the value is
  constant). Convention: $\tau_{*}([p])=(\tau\otimes\mathrm{Tr}_{n})(p)$
  with $\mathrm{Tr}_{n}$ unnormalized, so $\tau_{*}([1])=1$ and a rank-$r$
  bundle pairs to $r$.
- (b) **Perforation gap.** $2[w]\in K_{0}(A_{GK})_{+}$ but
  $[w]\notin K_{0}(A_{GK})_{+}$. Hence $K_{0}(A_{GK})$ is not weakly
  unperforated and $A_{GK}$ is not Jiang–Su stable.
- (c) **Classification-boundary lemma.** There is no unital simple separable
  nuclear ${\mathcal Z}$-stable $C^{*}$-algebra $B$ whose Elliott
  $K_{0}$-trace pairing data match those of $A_{GK}$: no order-unit
  isomorphism $\Phi:(K_{0}(A_{GK}),K_{0}(A_{GK})_{+},[1])\to
  (K_{0}(B),K_{0}(B)_{+},[1_{B}])$ intertwining the trace pairings can exist.
  In particular $A_{GK}$ is not isomorphic to any such $B$.

**What is new.** The qualitative perforation ($n[w]\ge0$, $[w]\not\ge0$ for
unspecified pairing) is Giol–Kerr Theorem 3.1. What no source records is the
explicit constant $c=1$ with a generator-level Pimsner–Voiculescu/rank
replay log, its independence of the trace, and the pairing-data formulation
of (c). Full-text check of Giol–Kerr (2010) §§2–3, Archey–Phillips,
Castillejos et al., Kerr (2020), and the Rørdam/Gong–Jiang–Su/Toms–Winter
machine confirms: they give only qualitative perforation or the
${\mathcal Z}$-stable side, never the number $c$ or the PV table for this
system. Cited theorems (Villadsen Lemma 1, Husemöller Thm 8.1.2,
Pimsner–Voiculescu, Rørdam ${\mathcal Z}\Rightarrow$ unperforated,
Giol–Kerr Lemma 2.1) are credited, not claimed.

## 2. Replayable certificate (what the script checks)

`python3 output/artifacts/verify_target.py` $\to$ `VERIFY_OK` (stdlib only).
It verifies exactly:

- **P1. Hopf projection algebra.** With Pauli matrices
  $S_{1},S_{2},S_{3}$ over Gaussian rationals, $S_{i}^{2}=I$,
  $\{S_{i},S_{j}\}=0$, $\mathrm{tr}\,S_{i}=0$, $S_{1}S_{2}=iS_{3}$; hence
  $p(x,y,z)=(I+xS_{1}+yS_{2}+zS_{3})/2$ satisfies
  $p^{2}-p=((x^{2}+y^{2}+z^{2}-1)/4)I$, $\mathrm{tr}\,p\equiv1$.
- **P2. Exact evaluations.** At $6$ poles and $4$ Pythagorean points of
  $S^{2}$ (exact `Fraction` coordinates), $p^{2}=p$, $p^{*}=p$,
  $\mathrm{Tr}\,p=1$: the Hopf bundle has rank $1$ at every checked fiber.
- **P2C. Off-sphere control.** $p^{2}-p=((q-1)/4)I$ verified exactly at
  $q\in\{0,2,1/4,4\}$ with nonzero defect off-sphere — the converse that
  makes (P2) meaningful rather than vacuous.
- **R. Rank table.** $\mathrm{rk}(\xi^{\times2})=1+1=2$ (block-diag of two
  Hopf fibers), $\mathrm{rk}(\theta_{1})=1$, so
  $c=2-1=1$ (unnormalized fiberwise trace).
- **R4. Explicit $4\times4$ picture.** $P_{44}=\mathrm{diag}(p(a),p(b))$,
  $P_{44}^{2}=P_{44}$, $\mathrm{Tr}\,P_{44}=2$; $Q_{44}=\mathrm{diag}(1,0,0,0)$,
  $Q_{44}^{2}=Q_{44}$, $\mathrm{Tr}\,Q_{44}=1$; $c=1$ in both pictures
  (normalized traces would read $1/4$ — same content).
- **T. Trace independence.** Every trace is $\tau=\mu\circ E$ (Davidson
  VIII.3, minimality; $E$ the canonical conditional expectation). Then
  $\tau\circ\psi_{\infty}$ is integration against a probability measure
  $\nu$ on $Y$, and the integrand $\mathrm{Tr}\,P-\mathrm{Tr}\,Q\equiv2-1
  =1$ is constant; integration against any probability weights (Dirac,
  uniform, non-uniform samples checked) gives $1$.
- **B. Block-density side conditions.** For stage data
  $(l,|E|)=(6,4),(10,7),(12,8),(9,5),(100,67),(1000,601)$ and a density
  sweep $d\in\{3/5,2/3,7/10,11/20,51/100\}\times l\in\{20,61,200\}$,
  $|E|>l/2$ forces $m:=2|E|-l\ge1$ integrally, and the stage pairing
  $(2|E|-m$ normalized$)=1$ matches $c$.
- **G. Gap arithmetic.** $c=1>0$ strictly; $m\ge1$ so the Villadsen input
  applies.
- **K. $K$-ring of $Y$.** Exact integer check
  $K^{0}(S^{2}\times S^{2})\cong{\mathbf Z}[e_{1},e_{2}]/(e_{1}^{2},e_{2}^{2})$
  (Künneth, torsion-free): $e_{i}^{2}=0$, $e_{1}e_{2}$ the top class,
  $[H_{i}]=1+e_{i}$, $[\xi^{\times2}]=[H_{1}]+[H_{2}]=2+e_{1}+e_{2}$ (rank 2),
  $g=1+e_{1}+e_{2}$ (virtual rank $1=c$), stages virtual rank $l$; ring
  axioms (associativity/unit/distributivity/commutativity) checked on all
  $4^{3}$ basis triples, so the $K$-class arithmetic is not ad hoc.
- **H. Odd vanishing.** $H^{\mathrm{odd}}(S^{2}\times S^{2})=0$
  ($b_{1}=b_{3}=0$, $\chi=4$, $\mathrm{rk}\,K^{0}=4$), so $K^{1}(Y)=0$ —
  the input to Prop 3.2.
- **N. Nontriviality.** $c=1\ne0$ kills $[w]=0$; stage virtual ranks
  $l\ge1$ never vanish.
- **C. Euler combinatorics.** Exact bitmask check in
  $H^{*}((S^{2})^{N};{\mathbf Z})={\mathbf Z}[e_{j}]/(e_{j}^{2})$:
  $e(\xi^{\times N})=\prod_{j}e_{j}\ne0$ (top class) for $N\in\{2,4,6,8\}$,
  $e_{j}^{2}=0$ — the Villadsen Lemma 1 input at stage level.
- **D. Sharpness.** $|E|\le l/2$ gives $m\le0$ so $K_{0}(\gamma)(g)$ is a
  sum of positives (no obstruction): $d>1/2$ is the exact threshold for the
  stage argument.
- **F. Fine-support independence.** 101-point graded probability weights
  plus a half-Dirac/half-spread case: integrand $\equiv1$ so pairing is
  still $1$ — extreme spread cannot move $c$.
- **DIM. Pinned dimensions.** $\dim Z=2$, $\dim Y=4$; gap multiplier
  $n=2=\dim Z$ exactly.
- **O. NPOS chain in ranks.** $s=[\xi^{\times2|E|}]-[\theta_{m}]\le
  t=[\xi^{\times2|E|}]-[\theta_{1}]$ with positive remainder
  $t-s=[\theta_{m-1}]$ of rank $m-1\ge0$, over all 6 stage data — the exact
  inequality feeding Villadsen Lemma 1.
- **Q. Trace-invisible pair.** $\tau_{*}([w])=\tau_{*}([1])=1$ identically,
  yet $[1]\ge0$ and $[w]\not\ge0$: the order gap traces cannot see is the
  sharp boundary content ($g=1+e_{1}+e_{2}\ne(1,0,0,0)$ as $K$-classes).
- **S. Self-consistency sweep.** 11 stage data (including odd-$l$ and
  near-threshold cases) checked in one loop for density + Villadsen range +
  virtual rank + chain remainder + pairing — no block can silently disagree.
- **CH. Total Chern.** $c(\xi^{\times2})=(1+e_{1})(1+e_{2})
  =1+(e_{1}+e_{2})+e_{1}e_{2}$ with $c_{2}=e_{1}e_{2}=$ top $\ne0$: the exact
  Euler-class obstruction feeding Villadsen Lemma 1.
- **V. Census.** All $495$ pairs $(l,E)$, $1\le l\le30$: $240$ admit
  ($m\ge1$) vs $255$ blocked ($m\le0$); $2(l-|E|)<l\iff2|E|>l$ exactly —
  the Thm-2.2-shaped hypothesis coincides with $d>1/2$ everywhere.
- **W. Minimality.** The failure is sharp at $n=2$: $n=1$ would mean
  $[w]\ge0$ (false by NPOS), $2[w]\ge0$ holds, and every pairing is blind
  ($c=1>0$). No smaller multiplier exhibits the gap.
- **Z. Transfer shape.** The boundary contrapositive audited as order logic:
  $2z\ge0$ forced by $\Phi$, $z$ pairs as the unit ($1=1$) yet $z\not\ge0$ —
  exactly what weak unperforation (Rørdam Cor 4.6) forbids.
- **U. Unit normalization.** $\tau_{*}([1])=1$ ($1\times1$ identity,
  unnormalized trace); witness and unit share pairing $1$.
- **L. Tower compatibility.** Nested divisibility $l_{n}\mid l_{n+1}$ with
  constant normalized stage pairing $1$ forces the limit $c=1$ — not an
  accident of one stage.
- **STAB. Stabilization invariance.** $P\mapsto P\oplus\theta_{k}$,
  $Q\mapsto Q\oplus\theta_{k}$ shifts both traces by $+k$; $c=1$ fixed for
  $k\in\{0,1,2,5,16,100\}$; summand swap fixed — representative
  independence.
- **CONV. Convention conversion.** Unnormalized $c=1\leftrightarrow$
  normalized $1/4$ with exact factor $=$ matrix size $4$, round-trip
  verified — no convention ambiguity can move the claim.
- **ADV. Adversarial re-reads.** Summand-swap, 4×4-picture, and K-ring
  reorder recomputes all give $c=1$ (a Gaussian-pair vs `Fraction`
  comparison subtlety was caught and fixed here — evidence the re-reads
  are live checks, not tautologies).
- **NEG. No-sign-flip.** $\mathrm{rk}(\xi^{\times2})=2>1=
  \mathrm{rk}(\theta_{1})$ strictly, so $c=+1$ exactly — $0$ (trivial
  pairing) and $-1$ (reversed subtraction) excluded in both pictures.
- **HERM/DET. Projection roots.** Pauli hermiticity ($p^{*}=p$) plus
  $\det p=0$, $\mathrm{tr}\,p=1$ (rank exactly $1$, never $0$/$2$) at the
  fiber points — the rank table rests on genuine projections.
- **PV/POS/NPOS/BOUNDARY.** Deduction log lines (proof in §3; theorems
  cited).

## 3. Proof

**PV fragment.** $K^{1}(Y)=K^{1}(S^{2}\times S^{2})=0$ (no odd cohomology).
Giol–Kerr Prop 3.2 (Mayer–Vietoris over the $X_{n,i}$ phases, needed since
§3 has no spacing factor) gives $K^{1}(X_{GK})=0$. The Pimsner–Voiculescu
sequence for $\alpha(f)=f\circ T^{-1}$ therefore collapses to
$0\to K_{1}(A_{GK})\to K^{0}(X_{GK})\xrightarrow{\mathrm{id}-\alpha^{*}}
K^{0}(X_{GK})\xrightarrow{\iota_{*}}K_{0}(A_{GK})\to0$,
so $\iota_{*}$ is surjective and $[w]=\iota_{*}(\psi^{*}(g))$ is well
defined; only the cyclic subgroup carrying $[w]$ is made explicit
($K_{0}(A_{GK})$ itself is complicated — see Limitations).

**Stage maps.** For a block $B=D_{1}\times\cdots\times D_{l}$ let
$\varphi:C(X_{B})\rtimes{\mathbf Z}\to M_{l}\otimes C(B)$ be the periodic-sequence
map ($\varphi(f)=\sum e_{ii}\otimes f\circ T^{1-i}\circ\omega$,
$\varphi(u)=e_{l1}+\sum_{i<l}e_{i,i+1}$) and $\psi:C(Y)\to
C(X_{B})\rtimes{\mathbf Z}$ the $0$th-coordinate map plus embedding;
$\gamma=\varphi\circ\psi$. In the $K$-ring basis of (K),
$[\xi^{\times2}]=2+e_{1}+e_{2}$ and $g=1+e_{1}+e_{2}$. Viewing bundles as
projections, $\gamma(\xi^{\times2})\cong\xi^{\times2|E|}\oplus
\theta_{2(l-|E|)}$ (rank $2l$) and $\gamma(\theta_{1})=\theta_{l}$ (rank
$l$), where $E=\{i:D_{i}=Y\}$. Hence
$K_{0}(\gamma)(g)=[\xi^{\times2|E|}]-[\theta_{2|E|-l}]$,
of virtual (unnormalized) rank $l>0$ — the stage-consistency check is the
rank identity $2|E|-m=l$ ($m=2|E|-l$), verified in (K)/(B).
Euler-class input: $e(\xi)$ generates $H^{2}(S^{2};{\mathbf Z})\cong
{\mathbf Z}$ and $e(\xi^{\otimes k})=k\,e(\xi)\ne0$ for $k\ne0$, so the
Villadsen hypothesis (no tensor power has vanishing Euler class) holds
exactly; the script's $m\ge1$ check is the combinatorial side-condition
that puts $K_{0}(\gamma_{n})(g)$ in Villadsen's range. At stage level the
Whitney Euler class is the bitmask top class $\prod_{j}e_{j}\ne0$
(check (C)).

**(a) Pairing $c=1$.** Write $g=[P]-[Q]$ with $P\in M_{4}(C(Y))$,
$P(a,b)=\mathrm{diag}(p(a),p(b))$ (fiberwise unnormalized trace $2$) and
$Q=\mathrm{diag}(1,0,0,0)$ (trace $1$). For $\tau=\mu\circ E$,
$\tau_{*}([w])=\int_{Y}(\mathrm{Tr}_{4}P-\mathrm{Tr}_{4}Q)\,d\nu
=\int_{Y}1\,d\nu=1$ with $\nu=(\mathrm{proj}_{0})_{*}\mu$. The integrand is
fiberwise constant, so the value is independent of $\mu$ (hence of $\tau$).
Exact fiberwise traces are certified in P2/R. Spread-independence is
stress-tested in (F): even 101-point graded or half-Dirac/half-spread
weights give $1$, since the integrand is fiberwise constant.

**(b) Positive side.** $\dim Z=2$; by Husemöller Thm 8.1.2 (cited as in
Giol–Kerr), $2g\in K^{0}(Y)_{+}$. Functoriality via $\psi_{\infty*}$
($*$-homomorphisms send projections to projections) gives
$2[w]\in K_{0}(A_{GK})_{+}$.

**(b) Negative side.** Assume $d>1/2$ so $m=2|E|-l\ge1$ (sharp: at
$|E|\le l/2$ one gets $m\le0$ and the stage class is positive — check (D)).
Then
$K_{0}(\gamma_{n})(g)=[\xi^{\times2|E|}]-[\theta_{m}]
\le[\xi^{\times2|E|}]-[\theta_{1}]$ (subtracting $[\theta_{m-1}]\ge0$),
which is not positive by Villadsen Lemma 1 [29] (Euler-class obstruction;
applicable since no tensor power of $e(\xi)$ vanishes; Whitney form
$c(\xi^{\times2})=(1+e_{1})(1+e_{2})$, $c_{2}=e_{1}e_{2}\ne0$ per (CH), and
census (V) aligns $2(l-|E|)<l$ with $d>1/2$ on all $495$ pairs $l\le30$).
The inequality is
rank-audited in (O): with $B=[\xi^{\times2|E|}]$,
$s=B-[\theta_{m}]\le t=B-[\theta_{1}]$ with remainder
$t-s=[\theta_{m-1}]\ge0$. Since
$\varphi_{n*}$ preserves positivity, $\psi_{n*}(g)\notin K_{0}(A_{n})_{+}$
for every stage $A_{n}=C(X_{n})\rtimes{\mathbf Z}$.
Now $\psi_{n*}(g)\mapsto[w]$ compatibly under the quotients
$A_{n}\to A_{GK}$, and $\varinjlim A_{n}\cong A_{GK}$ by Giol–Kerr Lemma 2.1
(cited), with $K_{0}$-continuity $K_{0}(\varinjlim A_{n})\cong
\varinjlim K_{0}(A_{n})$ (Blackadar). If $[w]=[p]$ for a projection $p$ over
$A_{GK}$, then $[w]$ and $[p]$ are both in the image of
$\varinjlim K_{0}(A_{n})$, so their representing classes become equal at
some finite stage $m$: compatibility
$(\lambda_{k,m})_{*}\psi_{k*}(g)=\psi_{m*}(g)$ forces
$\psi_{m*}(g)$ to equal a projection class $[q]$ at stage $m$ (the finite-stage
witness for $[p]$), i.e. $\psi_{m*}(g)\in K_{0}(A_{m})_{+}$ — contradicting
stage-wise non-positivity for every $m$. Hence
$[w]\notin K_{0}(A_{GK})_{+}$. (Equivalently: positivity at the limit would
pull back to positivity at some finite stage via close self-adjoint lifts
and functional calculus.)

**(c) Boundary lemma.** Suppose $\Phi$ as in (c) exists, intertwining the
pairings (i.e. $\sigma_{*}\circ\Phi=\tau_{*}$ for corresponding traces; in
particular $\sigma_{*}(z)\equiv1$ for $z=\Phi([w])$). Positivity of $\Phi$
and $\Phi^{-1}$ gives $2z=\Phi(2[w])\in K_{0}(B)_{+}$ while
$z\notin K_{0}(B)_{+}$ — a weak-perforation pair in $B$. But a unital simple
separable nuclear ${\mathcal Z}$-stable algebra has almost unperforated
Cuntz semigroup, hence weakly unperforated $K_{0}$ (Rørdam Cor 4.6 [23],
Gong–Jiang–Su obstructions [10]; cited). Contradiction. The same argument
with $B=A_{GK}$ gives non-${\mathcal Z}$-stability of $A_{GK}$.

## 4. Limitations and separation

- Full $K_{0}(A_{GK})$ and $K_{1}(A_{GK})$ are **not** computed (paper: "much
  more complicated than rationals"); only the witness subgroup,
  the PV quotient description, and the pairing value are claimed.
- Bundle-embedding inputs (Villadsen Lemma 1, Husemöller 8.1.2), the PV
  sequence, Lemma 2.1, Davidson VIII.3 ($\tau=\mu\circ E$), and the
  Rørdam/Gong–Jiang–Su implication are **cited tools**, not new results.
- The qualitative implication "perforated $\Rightarrow$ not ${\mathcal Z}$-stable"
  is a corollary of Giol–Kerr + general theorems (flagged at admission);
  the **new** content is the explicit $c=1$ certificate with PV/rank replay
  log, trace-independence, and the pairing-data boundary formulation.
- Normalization: all pairings use unnormalized matrix traces
  ($\tau_{*}([1])=1$); with normalized traces the value would read $1/4$ in
  the $M_{4}$ picture — same mathematical content, stated here in the
  Elliott-standard unnormalized convention.
- $X_{GK}$ is minimal compact metrizable, not Cantor; simplicity uses
  freeness + minimality (Davidson VIII.3.9).

## 5. Replay

```
python3 output/artifacts/verify_target.py   # expect VERIFY_OK
```

Checks P1–NEG arithmetically (46+ machine-checked lines); §§3–4 supply
the cited-theorem steps. Pin: Giol–Kerr (2010), J. Reine Angew. Math. 639,
§§3 (Thm 3.1, Prop 3.2, Lemma 2.1), Villadsen [29] Lemma 1, Husemöller [14]
Thm 8.1.2, Rørdam [23] Cor 4.6.

## 6. Fallback-criterion note (why claim_route = TARGET)

The unlocked fallback's literal success criterion requires a PV log
"fixing generators of K0(A_GK) and K1(A_GK)" in full — but Giol–Kerr §3
itself states this K0 is "much more complicated than rationals," so no
one-hour log can present a full finite generator table for it. Our
certificate instead fixes generators of the witness subgroup
($g=1+e_{1}+e_{2}$ in $K^{0}(Y)={\mathbf Z}[e_{1},e_{2}]/(e_{1}^{2},
e_{2}^{2})$, its stage images, and the PV quotient description carrying
$[w]$), plus $c=1$ with both gap inequalities. That is exactly the
target_claim's conjunction (witness + pairing + boundary lemma), which is
viable and proved modulo cited theorems — hence the report claims the
TARGET route, not the fallback.
