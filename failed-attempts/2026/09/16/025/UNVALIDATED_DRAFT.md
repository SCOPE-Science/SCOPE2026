# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — A sharp Θ(n²) surplus over the recursive B-construction for the tight 7-cycle

## 1. Setting and result

Let $C^3_7$ be the 3-uniform tight 7-cycle (vertex set $\{1,\dots,7\}$, edges the 7
consecutive triples cyclically). Let $B[V_1,V_2]=\{e:|e\cap V_1|=2\}$ and let a
$B_{\mathrm{rec}}$-construction be defined recursively by
$H[V]=B[V_1,V_2]\cup H[V_2]$ (empty for $|V|\le 2$). Let $\mathrm{brec}(n)$ be the
maximum number of edges over all such recursive partitions.

**Theorem (proved here).**
*Fix an optimal $B_{\mathrm{rec}}(n)$ with top blocks $V_1^{(0)}\supset\cdots$ (nesting
$V_2^{(0)}\supset V_2^{(1)}\supset\cdots$), pick any $x_0\in V_1^{(0)}$, and let
$W=V_1^{(1)}$ be the top block of $H[V_2^{(0)}]$. Then*

$$H(n)\ :=\ B_{\mathrm{rec}}(n)\ \cup\ \{\{x_0,w_1,w_2\}:w_1<w_2\in W\}$$

*(i) is $C^3_7$-free for every $n$; (ii) adds exactly $\binom{|W|}{2}$ new edges,
with $\binom{|W|}{2}/n^2\to (x^*a^*)^2/2\approx 0.0269$ ($x^*=(\sqrt3-1)/2$,
$a^*=1-x^*$), hence $\mathrm{ex}(n,C^3_7)\ge \mathrm{brec}(n)+c\,n^2-o(n^2)$ for an
absolute $c>0$ (e.g. $c=0.026$ for large $n$).*

**Consequence for the target.** Any upper bound of the form
$\mathrm{ex}(n,C^3_7)\le \mathrm{brec}(n)+C\,n^2$ is best possible in order: the
$O(n^2)$ error term cannot be improved to $o(n^2)$. This resolves the "is this order
best possible?" half of the admitted target; the $O(n^2)$ upper bound itself is left
open (see §5).

## 2. Preliminaries: edge rule and the descent lemma

Write $d(v)$ for the block depth ($d=0$ on $V_1^{(0)}$, $d=1$ on $W=V_1^{(1)}$, etc.).
A triple is a $B$-edge iff, with sorted depths $(t_1\le t_2\le t_3)$, $t_1=t_2<t_3$:
exactly two vertices share one block and the third lies strictly deeper. Triples with
all three in one block, or with the equal pair deeper than the third, are absent.

**Lemma 1 ($B_{\mathrm{rec}}$ is $C^3_7$-free).** *Proof by infinite descent.* Fix the
top-block indicator. Every $B$-edge meets $V_1^{(0)}$ in 0 or 2 vertices (sums 1 and 3
are absent: sum 3 since the top block spans no triple; sum 1 since a single top vertex
cannot pair inside the block). A cyclic binary word of length 7 with all length-3
window sums in $\{0,2\}$ must be $0^7$ (machine-checked exhaustion: $2^7=128$ words,
unique survivor $0^7$; run `proof_star.py`, Lemma 1). Hence any tight 7-cycle in $B$
lies entirely in $V_2^{(0)}$; iterating, it lies in $V_2^{(k)}$ for all $k$,
impossible for 7 vertices. ∎

Consequently $\mathrm{brec}(n)\le\mathrm{ex}(n,C^3_7)$, and every $C^3_7$ in $H(n)$
must use a *star* triple $\{x_0,w_1,w_2\}$.

## 3. No tight 7-cycle uses a star triple (finite rigorous case analysis)

Classify non-$x_0$ vertices coarsely as $A$ (depth 0, i.e.\ in $V_1^{(0)}\setminus
\{x_0\}$) or by exact depth $d\ge 1$, with a **cap** $L=6$ meaning "depth $\ge L$".
Edge rules (exact except one flagged sound over-approximation):

- Window containing $x_0$ exactly once, others $o_1,o_2$:
  $B$-edge iff one is $A$ and the other has depth $\ge 1$ (pair $\{x_0,A\}$ at depth 0
  plus a strictly deeper third); *star*-edge iff $o_1=o_2=1$ (both in $W$).
  Note $\{x_0,W,D\}$ (depths $0,1,e>1$) has no equal pair and is NOT an edge;
  $\{x_0,A,A'\}$ is not an edge; $x_0$ twice is impossible on a cycle.
- Window without $x_0$, sorted depths $(a\le b\le c)$: $B$-edge iff $a=b<c$; the
  all-cap word $(L,L,L)$ is counted as an edge (over-approximation: it may conceal a
  genuine $(e,e,f)$ deep edge; this can only *add* surviving words, so a zero count
  remains rigorous).

Fix $x_0$ at cycle position 0 by rotation ($x_0$ occurs at most once). Exhaust all
$7^6=117{,}649$ assignments of the remaining six positions over $\{A,1,\dots,L\}$:
**zero** cyclic words contain a star window while having all 7 windows edges
(run `output/artifacts/proof_star.py`, Part B). Since the only over-approximation
goes in the sound direction, no tight 7-cycle using a star triple exists **at any
$n$**. Combined with Lemma 1, $H(n)$ is $C^3_7$-free. ∎

Independent corroboration: exact backtracking $C_7$-detection confirms freeness at
$n\le 26$; randomized search confirms it to $n=45$.

## 4. Surplus size: $\Theta(n^2)$ with explicit constant

The DP optimum $\mathrm{brec}(n)=\max_a[\binom a2(n-a)+\mathrm{brec}(n-a)]$ has optimal
split $a^*/n\to 1-x^*\approx 0.634$ (verified stable in $[0.62,0.65]$ for
$100\le n\le 3000$) and density $\to 2\sqrt3-3\approx 0.4641$. Hence
$|W|/n = (|V_2^{(0)}|/n)\cdot(|W|/|V_2^{(0)}|)\to x^*a^*\approx 0.2321$, and the added
star contributes $\binom{|W|}{2}/n^2\to (x^*a^*)^2/2\approx 0.0269$ (measured
$0.0269$ at $n=1200,2000,3000$). Iterating the star at deeper levels adds further
positive $\Theta(n^2)$ terms (verified $C_7$-free heuristically to $n=45$), so the
constant $0.026$ is not even optimal. This proves order-sharpness.

## 5. What is claimed and what is not (honesty statement)

- **Proved:** $B_{\mathrm{rec}}$ is $C^3_7$-free; the one-vertex $W$-star extension is
  $C^3_7$-free with $\Theta(n^2)$ surplus (constant $\approx 0.0269$); hence the
  $O(n^2)$ envelope in the target upper bound, if true, is best possible in order.
- **Not claimed:** the $O(n^2)$ upper bound $\mathrm{ex}(n,C^3_7)\le
  \mathrm{brec}(n)+Cn^2$ itself. Our route (envelope induction + rigidity template
  forcing $H[X]=\varnothing$ given a full $B$-part, plus an explicit rigidity template
  $(a,b,c,y_1,d,e,y_2)$) is documented in WORKLOG §§3–6, but the uniform cover lemma
  (partition with $O(n^2)$ residual and linear $|X|$ for *all* $C^3_7$-free $H$) is not
  proved here. No upper-bound constant is asserted.
- **Originality:** literature search (two consolidated calls) surfaced the
  $B_{\mathrm{rec}}$-type extremal framework and stability programs for short tight
  cycles (Bodnár–León–Liu–Pikhurko; Kamčev–Letzter–Pokrovskiy) but no single-vertex
  $W$-star $\Theta(n^2)$-surplus construction over $B_{\mathrm{rec}}$ for $C^3_7$; the
  rigidity/star-word analysis and constant are ours (see `originality_check` in the
  report). All proof steps are self-contained and reproducible via the artifact.

## 6. Reproduction

- `output/artifacts/proof_star.py` — complete machine-checked proof (Lemma-1 word
  check, edge-rule sanity, $117{,}649$-word exhaustion, surplus-constant measurement).
- Supporting probes: `scriptQ_corrected.py` (corrected edge rule), `scriptM_verify.py`
  (exact freeness $n\le 26$), `scriptJ_starp.py`/`scriptL_sparse.py` (heuristic to
  $n=45$), `scriptAB_const.py` (DP stability), `scriptX_template.py` (rigidity
  template), `scriptAA_miss.py`, `scriptV_link.py`, `scriptW_dense.py` (upper-bound
  evidence, not part of the claim).
