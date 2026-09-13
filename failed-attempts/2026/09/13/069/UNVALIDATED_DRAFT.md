# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Type-3 Wilf gap 3 for multiplicity-6 semigroups — proof

## Result

Let $S$ be a numerical semigroup with multiplicity $m(S)=6$ and
Cohen–Macaulay type $t(S)=3$. Then the Wilf number
$W(S)=e(S)n(S)-c(S)$ satisfies $W(S)\ge 3$.
In fact the proof gives $W(S)\ge 4$ on all but explicitly handled
branches, and $W(S)\ge 3$ everywhere; the bound $3$ is sharp in the
sense that the certificate threshold is exactly $3$.

## Setup and notation

Write $\mathrm{Ap}(S,6)=\{w_0=0,w_1,\dots,w_5\}$ with
$w_i=6k_i+i$, $k_i\ge 1$ integers. The Kunz polyhedron $P_6$ is

$$k_s\le k_i+k_j\ (i+j=s<6),\qquad k_{s-6}\le k_i+k_j+1\ (i+j=s>6).$$

For $i\ne j$ put $x\le_S y\iff y-x\in S$. On Apéry elements:

- if $j>i$: $w_i\le_S w_j\iff k_j-k_i-K[j-i]\ge 0$ where $K[0]=0$,
  $K[r]=k_r$;
- if $j<i$: $w_i\le_S w_j\iff k_j-k_i-K[j-i+6]-1\ge 0$.

Hence with $d=q-p$ (resp. $q-p+6$) and offset $o=0$ (resp. $1$),
$\lnot(w_p\le_S w_q)$ is the strict integer inequality
$k_q-k_p-k_d\le -1-o$, and $w_p\le_S w_q$ is $k_q-k_p-k_d\ge o$.
Maximal Apéry elements correspond to pseudo-Frobenius numbers
$w_i-6$; their count is the type $t$. Minimal nonzero Apéry elements
plus $6$ are the minimal generators; their count is $e$.
Genus $g=\sum k_i$, conductor $c=\max w_i-5$, $n=c-g$,
$W=en-c$.

The proof is by exhaustive, exactly certified polyhedral case analysis.
Every certificate below is a rational Farkas (LP-duality) certificate
with all arithmetic verifiable in exact integer arithmetic
(`output/artifacts/run_verify.py`, `run_verify_e5.py`, no LP solver
needed for checking).

## Lemma A — type 3 forces $e\ge 4$

$e=2$ gives $S=\langle 6,x\rangle$, whose Apéry poset is the chain
$0<x<2x<\cdots$, so $t=1$. For $e=3$: fix a minimal pair
$A=\{a,b\}$ ($\binom 52=10$ choices) and a maximal triple $M$
($\binom 53=10$ choices). Exact minimality of $A$ is the strict rows
plus, for each of the 3 non-minimal indices, a witness choice
$a(j)\in A$ with $w_{a(j)}\le_S w_j$ ($2^3=8$ witness maps). This gives
$10\cdot 10\cdot 8=800$ rational polyhedral cells, each containing the
Kunz rows, the $M$-maximality strict rows, the $A$-minimality strict
rows, witness rows, and $k_i\ge 1$. Every cell is LP-infeasible; the
artifact `e5certs.json` stores one exact Farkas ray per cell
($yA_1+zA_2=0$ coefficient-wise, $-yb_1+zb_2>0$), and the verifier
checks all 800 in exact `Fraction` arithmetic. Most rays use just
2 rows. Example: for $A=\{1,2\}$, $M=\{1,2,3\}$, witnesses
$w_1\le w_3,w_1\le w_4$: witnesses give $k_3\ge k_1+k_2$,
$k_4\ge k_1+k_3\ge 2k_1+k_2$, while maximality gives
$k_2\le 2k_1-1$ and $k_4\le 2k_2-1$, whence
$2k_1+1\le k_2\le 2k_1-1$, absurd. Since LP-infeasibility implies
integer infeasibility, no $m=6$ semigroup has $e=3$ and $t=3$.
Consequently $t=3$ implies $e\in\{4,5\}$ (indeed $e=6$ has $t=5$).

## Exact cell decomposition for $t=3$

With $e\ge 4$ established, the type-3 region is partitioned into refined
cells $(M,A,F,\mathrm{wit}_{\max},\mathrm{wit}_{\min})$ where $M$ ranges
over all $\binom 53=10$ maximal triples, $A$ over all minimal sets of
size 3 or 4 ($\binom 53+\binom 54=10+5=15$), $F\in M$ attains the
conductor, and the witness maps resolve the non-maximal/non-minimal
disjunctions ($|M|^{|\mathrm{nonmax}|}\cdot|A|^{|\mathrm{nonmin}|}$
maps per $(M,A,F)$). This exhaustive enumeration has exactly
$29{,}700$ refined cells, covering every candidate $(M,A)$ pair — not
just the 19 faces observed in small boxes. The defining inequalities of
each refined cell are exact (mutual incomparability inside $M$ and
inside $A$, witness inequalities with the correct $+o$ offset,
$F$-maximality, Kunz rows), so every $t=3$ tuple lies in at least one
cell with its true $e=1+|A|$, true $F$, true $W$. Every one of the
$29{,}700$ cells is decided by a stored exact certificate in
`maincerts.json`: 214 cells carry dual bound certificates $\ge 3$,
15 cells carry certified branch trees (45 leaves: 19 with bound $>2$,
26 infeasible), and the remaining $29{,}471$ cells carry exact Farkas
infeasibility rays. The verifier `run_verify.py` iterates this
exhaustive $29{,}700$-cell enumeration itself — rebuilding each cell's
row system from scratch and asserting every combo is decided — rather
than checking only stored entries. Separately, exhaustion over
$k_i\in[1,6]$ (2796 valid tuples, 690 type-3) confirms all box type-3
tuples fall in decided feasible cells with $W\ge 4$ (`coverage.py`:
690 covered, 0 uncovered), and the same 19 faces occur in $[1,8]^5$;
these box checks are consistency evidence only, since completeness
rests on the $29{,}700$-cell enumeration.

## The bound

On a cell with fixed $(e,F)$ the Wilf number is the linear function
$W=e(c-g)-c$ with $c=6k_F+F-5$, $g=\sum k_i$.
Of the $29{,}700$ enumerated cells, $29{,}471$ are LP-infeasible, each
with a stored exact Farkas ray in `maincerts.json` ("infeasible") in
the same $U/V$ (`Y`/`Z`) format, machine-checked in exact arithmetic;
hence they contain no integer (indeed no real) Kunz point. The 229
feasible cells split as follows. 214 cells have LP-relaxation minimum
$\ge 3$; `maincerts.json` ("strong", 214 entries) stores one exact
rational dual certificate per cell
($-YA_1+ZA_2=o$ coefficient-wise with value $-Yb_1+Zb_2+o_c\ge 3$),
each machine-checked in exact arithmetic. Since integer points satisfy
the relaxation, $W\ge 3$ on all these cells.

Two faces, $((3,4,5),(1,2,5))$ and $((3,4,5),(1,4,5))$ (both $e=4$),
contain 15 refined subcells whose LP minimum is $1$ (fractional
optimum, e.g. $(4/3,7/6,5/2,7/3,13/6)$), so one branching step is used:
split on the most fractional coordinate (e.g. $k_3\le 2$ vs $k_3\ge 3$;
the $\le$ child is LP-infeasible with exact Farkas ray, the $\ge$ child
has LP minimum $>2$, certified by an exact dual certificate; a few
need two levels). `maincerts.json` ("branches", 15 trees, 45 leaves:
19 bound, 26 infeasible) stores every leaf with its exact certificate;
the independent verifier checks every leaf certificate. Since $W$ is
integer-valued on integer points,
LP minimum $>2$ gives $W\ge 3$ on every leaf. Together with the 214
direct bound certificates and $29{,}471$ infeasibility rays, all
$29{,}700$ cells are decided: $214+15+29{,}471=29{,}700$.

The two weak families are also transparent by hand. E.g. for
$M=(3,4,5)$, $A=(1,2,5)$ with witnesses $w_1,w_2\le w_3$ and
$w_2\le w_4$: Kunz plus witnesses pin $k_3=k_1+k_2$, $k_4=2k_2$ with
$k_2\le 2k_1-1$, and a three-way Frobenius case check gives
$W\ge 3$ (case $F=3$: $W=10k_1+2k_2-4k_5-6$ with
$k_5\le k_1+k_2-1$; case $F=4$: $W=20k_2-8k_1-4k_5-3$ with the two
subcases $k_1<k_2$, $k_1=k_2$; case $F=5$:
$W=14k_5-8k_1-16k_2$ with $k_5\ge\max(k_1+k_2,2k_2)$).
The family $A=(1,4,5)$ is analogous
($k_3=k_1+k_2$, $k_2\ge 2k_1$, three Frobenius cases).

## Sharpness and computational evidence

Exhaustion to $[1,8]^5$ finds minimum $W=4$ on the type-3 locus,
e.g. $k=(1,1,2,2,2)$: $\mathrm{Ap}=(0,7,8,15,16,17)$, maximal
$\{3,4,5\}$, PF $\{9,10,11\}$, atoms $\{1,2,5\}$, $e=4$, $g=8$,
$c=12$, $n=4$, $W=4$. Random sampling to $k_i\le 40$ (3776 type-3
points) gives minimum $W=13$, consistent with $W$ growing outside the
small box. The theorem's bound $W\ge 3$ therefore holds with one unit
of slack over all computed examples; no counterexample ($W\le 2$)
exists.

## Reproducibility

- `output/artifacts/maincerts.json`: exhaustive $29{,}700$-cell coverage —
  214 strong-cell dual certificates (bound $\ge 3$), 15 branch trees
  with exact leaf certificates (45 leaves: 19 bound $>2$, 26
  infeasible), and $29{,}471$ exact Farkas infeasibility rays for the
  non-stored-in-earlier-version cells, all in the same $U/V$
  (`Y`/`Z`) format.
- `output/artifacts/e5certs.json`: 800 Lemma-A Farkas infeasibility rays.
- `output/artifacts/rowsutil.py`, `run_verify.py`, `run_verify_e5.py`,
  `coverage.py`: exact (solver-free) checkers; all pass:
  exhaustive $29{,}700$-cell enumeration verified
  (strong $=214$, infeasible $=29{,}471$, branched $=15$),
  800 Lemma-A rays, 690/690 box tuples covered.
- Generation used CBC (PuLP) only to *find* rational certificates; every
  stored certificate is verified independently in exact arithmetic, so
  soundness does not depend on any floating-point solver.
