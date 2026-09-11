# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Diamond-sealed three-way far family in the ρ₁-coherent special cell

## 1. Theorem (target claim)

**Theorem.** Assume $\diamondsuit_{\omega_1}$ (diamond on $\omega_1$).
Then there exist three $\rho_1$-coherent special Aronszajn trees
$R_0,R_1,R_2$ (as trees of functions ordered by extension, with countable
levels, height $\omega_1$, no uncountable branch, each with a strictly
increasing specializing map into $\mathbb Q$) which are **pairwise far**:
for distinct $i,j$, no uncountable downward-closed subtree of $R_i$ is
club-isomorphic to an uncountable downward-closed subtree of $R_j$
(level-preserving isomorphism on a club of levels).

**Corollary A (no member-universal).** No $R_i$ is club-universal for the
cell: for each $i$ there is $j\ne i$ with $R_j$ not club-embedding
(whole-tree, on a club) into $R_i$.

**Corollary B (lower-basis number $\ge 3$).** No family
$\mathcal B\subseteq\mathrm{cell}$ with $|\mathcal B|\le 2$ is a
whole-tree lower basis (every cell member hosts some $\mathcal B$-member
by whole-tree club-embedding). In particular there is no single
lower-universal member for $\{R_0,R_1,R_2\}$, so the lower-basis number
of the cell is at least $3$.

*Terminology.* "Club-embedding" = level-preserving order-embedding whose
level set contains a club. "Club-isomorphic subtrees" = uncountable
downward-closed $S\subseteq R_i$, $T\subseteq R_j$ with a level-preserving
bijection $S\!\upharpoonright\! C\to T\!\upharpoonright\! C$ for some club $C$.
"Lower basis" is in the sense of the Todorcevic/Moore basis problem
(basis members embed *into* arbitrary members). Both corollaries are stated
with these explicit meanings; no claim is made about upper-universals
outside the triple.

## 2. Background ingredients (cited, not re-proved)

1. **$\rho_1$ walk and coherence class.** Fix a $C$-sequence
   $\langle C_\alpha:\alpha<\omega_1\rangle$. Let $\rho_1$ be Todorcevic's
   walk function. Call $f:\alpha\to\omega$, $g:\beta\to\omega$
   *coherent mod-finite* if $\{\xi<\min(\alpha,\beta):f(\xi)\ne g(\xi)\}$
   is finite. Let $\mathcal F$ be the $\rho_1$-coherence class: all
   $f$ with domain $<\omega_1$ coherent mod-finite with some
   $\rho_1(\cdot,\gamma)\!\upharpoonright\!\mathrm{dom}(f)$.
   Facts used (Todorcevic, *Walks on Ordinals*): $\mathcal F$ is closed
   under finite modifications and under countable unions of chains
   (the union of a chain of pairwise mod-finite functions is mod-finite
   with each member); each $f\in\mathcal F$ has extensions at arbitrarily
   high domains in $\mathcal F$ with prescribed finite modifications.
2. **Specializing criterion.** A tree of functions ordered by extension
   with a strictly increasing map $f:T\to\mathbb Q$ along branches is
   special (fibres $f^{-1}\{q\}$ are antichains; $\mathbb Q$ countable)
   and Aronszajn (an uncountable branch would carry an uncountable
   strictly increasing $\mathbb Q$-sequence, impossible).
3. **Diamond coding.** $\diamondsuit_{\omega_1}$ implies CH. Fix a pairing
   function so every tuple $Q=(i,j,S,T,\varphi,C)$ (indices, subsets of
   $\omega_1$ coding subtrees, a function $\omega_1\to\omega_1$ coding a
   partial isomorphism, a club) is coded as a subset of $\omega_1$.
   For the true $Q$, the set
   $\{\alpha: D_\alpha = Q\cap\alpha\ \wedge\ \alpha\in C\ \wedge\ \text{$\alpha$ limit $>0$}\}$
   is stationary (standard $\diamondsuit$ capture plus club intersection).

Prior far-family theorems (Abraham–Shelah; Krueger/Chavez via proxy;
MA weak-embedding no-universal theorems) are recorded as motivation only;
no implication from them is used.

## 3. Construction

We build increasing continuous chains
$(T^i_\alpha, f^i_\alpha)_{\alpha<\omega_1}$, $i<3$, satisfying:

- (H1) $T^i_\alpha$ is a countable pruned tree of height $\alpha$ with all
  nodes in $\mathcal F$, ordered by extension; levels countable.
- (H2) $f^i_\alpha:T^i_\alpha\to\mathbb Q_{\ge 0}$ strictly increasing
  along branches; every successor step increases values by $<2^{-\ell}$
  where $\ell$ is the level (summable increments), so every countable
  branch has finite supremum in $\mathbb Q_{\ge 0}$.
- (H3) $T^i_{\alpha+1}$ end-extends $T^i_\alpha$; at limits take unions
  then add level-$\alpha$ nodes as below.

**Successor step** $\alpha\to\alpha+1$. For each $x\in T^i_\alpha$ at top
level pick two distinct coherent extensions $x^\frown n_0,x^\frown n_1$
in $\mathcal F$ (possible by ingredient 1) and assign
$f$-values in $(f(x),f(x)+2^{-\alpha})$ distinct. Nodes not at top keep
(H2). Countability preserved.

**Limit step** $\alpha$ limit. Let $U^i=\bigcup_{\xi<\alpha}T^i_\xi$
(countable). For each node $p\in U^i$ pick one cofinal branch
$b_p$ through $U^i$ above $p$ (possible since each $T^i_\xi$ pruned and
$\alpha$ countable; enumerate nodes and diagonalize — concretely fix an
enumeration and extend greedily). Let $u_p=\bigcup b_p\in\mathcal F$
(ingredient 1). The set $\{u_p:p\in U^i\}$ is countable; put all of them
(resp. all but one, see sealing) as level-$\alpha$ nodes. Assign
$f(u_p)$: let $s_p=\sup f[b_p]$ (finite by (H2) summability); choose
rational $f(u_p)\in(s_p,s_p+2^{-\alpha})$ with distinct values across
$p$ (possible as $\mathbb Q$ dense). Then (H2) persists: future suprema
stay finite because tail increments remain summable.

**Sealing step.** Suppose at limit $\alpha$ the diamond guess $D_\alpha$
codes $Q=(i,j,S,T,\varphi,C)$ with $i\ne j$, $\alpha\in C$,
$\varphi:S\!\upharpoonright\!(C\cap\alpha)\to T\!\upharpoonright\!(C\cap\alpha)$
a level-preserving bijection agreeing with the approximations built so
far (i.e., $S\!\upharpoonright\!\alpha\subseteq T^i_{<\alpha}$,
$T\!\upharpoonright\!\alpha\subseteq T^j_{<\alpha}$ uncountable
downward-closed in the approximations, $\varphi$ order- and
level-preserving). Then:

1. Pick a cofinal chain $b=\{s_\xi:\xi\in C\cap\alpha\}\subseteq S$
   with $s_\xi$ at level $\xi$ (possible: $S$ uncountable
   downward-closed meets every level of $C\cap\alpha$ cofinally;
   thin to a chain using prunedness).
2. Let $u=\bigcup b$ (domain $\alpha$, in $\mathcal F$) and
   $v=\bigcup\varphi[b]$ (domain $\alpha$, in $\mathcal F$).
3. Put $u$ as a level-$\alpha$ node of $T^i_\alpha$ (among the $\{u_p\}$;
   ensure $b$ is one of the chosen $b_p$, replacing one if needed).
4. **Omit** $v$ from $T^j_\alpha$: do not include $v$ among level-$\alpha$
   nodes of $T^j$, including no finite modification coinciding with $v$
   on a tail (omit the finitely many $\mathcal F$-representatives equal
   mod-finite to $v$ at domain $\alpha$ — there are only countably many,
   and omitting them keeps levels countable; every node below $\alpha$
   still has another limit above it because we include all other
   $u_p$'s, so prunedness is preserved).
5. Assign $f$ as in the limit step for included nodes.

If $D_\alpha$ codes no such live guess, do the plain limit step.
Since $D_\alpha$ codes at most one tuple, at most one directed pair is
sealed per $\alpha$; all six directed pairs $(i,j)$ are handled whenever
guessed.

Let $R_i=\bigcup_\alpha T^i_\alpha$, $f_i=\bigcup_\birthmark$.
Levels are countable by construction; height $\omega_1$ since each level
is nonempty (prunedness); every node lies in $\mathcal F$
($\rho_1$-coherent); $f_i$ strictly increasing into $\mathbb Q$, hence
each $R_i$ special Aronszajn by ingredient 2.

*Why omission preserves prunedness.* The omitted $v$ extends a unique
chain $\varphi[b]$; every proper initial segment of that chain is also
extended by other branches $b_p$ whose limits are included (at each
$\xi<\alpha$ the node $\varphi(s_\xi)$ has $\ge 2$ successors in the
approximation by the successor step, and at most one successor-chain is
killed). Hence every node below $\alpha$ retains an extension at level
$\alpha$. A routine induction shows levels stay nonempty.

## 4. Sealing verification (far)

Suppose for contradiction $i\ne j$ and $Q=(i,j,S,T,\varphi,C)$ is a
genuine club-isomorphism between uncountable downward-closed
$S\subseteq R_i$, $T\subseteq R_j$ on club $C$. By ingredient 3, the
capture set is stationary; pick $\alpha$ in it above all parameters
where the approximations already contain $S\!\upharpoonright\!\alpha$,
$T\!\upharpoonright\!\alpha$, $\varphi\!\upharpoonright\!\alpha$ (possible
since capture is stationary hence unbounded, and approximations are
continuous). At that $\alpha$ the construction sealed $Q$: $u\in R_i$
at level $\alpha$ lies in $S$ (as $S$ downward-closed uncountable
contains the chain $b$ and its limit — $S$ contains limits of its
$\alpha$-chains present in $R_i$; if $S$ missed $u$ we instead choose
$b$ inside $S$ whose limit the construction includes, forcing
$S$ to meet level $\alpha$ at $u$), while the corresponding
$v=\varphi$-image is absent from $R_j$, hence absent from $T$.
But $\varphi$ level-preserving on $C\ni\alpha$ would have to send the
level-$\alpha$ node of $S$ on $b$ to a level-$\alpha$ node of $T$ on
$\varphi[b]$, namely $v$ — contradiction. Thus no such $Q$ exists.
Since $Q$ was arbitrary, $R_i,R_j$ are far. All three pairs likewise.

*Remark on $S$ containing the limit.* If the particular $b$ chosen were
not eventually in $S$, replace it: because $S\!\upharpoonright\!\alpha$
is uncountable-in-$\alpha$ and the construction's menu $\{b_p\}$ covers
every node, some $b_p\subseteq S$ cofinal exists; seal along that one.
The diamond guess tells us $S\!\upharpoonright\!\alpha$ exactly, so the
choice is well-defined at stage $\alpha$.

## 5. Corollaries

*Corollary A.* Fix $i$. For $j\ne i$, $R_j$ does not whole-tree
club-embed into $R_i$: such an embedding's image would be an uncountable
subtree of $R_i$ club-isomorphic to (a subtree of) $R_j$, contradicting
farness. Hence no $R_i$ hosts the whole cell.

*Corollary B.* Let $\mathcal B\subseteq\mathrm{cell}$,
$|\mathcal B|\le 2$, and suppose every cell member hosts some
$B\in\mathcal B$ by whole-tree club-embedding. Then each of
$R_0,R_1,R_2$ hosts some $B_k$; by pigeonhole some $B\in\mathcal B$
whole-tree embeds into two distinct $R_i,R_j$ on clubs $C_0,C_1$.
On $C=C_0\cap C_1$ the two images are club-isomorphic subtrees
(both isomorphic to $B\!\upharpoonright\! C$), contradicting farness.
Hence no such $\mathcal B$ exists; the whole-tree lower-basis number is
$\ge 3$.

## 6. Finite sealing shadow (computed evidence, not the proof)

A finite mock (`output/artifacts/verify.py`, stdlib only) builds three
binary trees of depth $10$ and performs four scheduled directed seals:
at the scheduled level keep a source cone but delete the guessed target
cone. It checks: (C1) all levels nonempty; (C2) a mock specializing
label strictly increases along surviving edges; (C3) coherence labels
stay in $\{0,1,2\}$; (C4) every sealed guess is blocked (source retains a
top descendant, target has none). Result `VERIFY_OK`
(`output/artifacts/seal_ledger.json`), top counts $[960,768,1004]$,
$4$ seals. This validates the *combinatorial shape* of sealing
(keep-source/kill-target while preserving height and labels), not any
uncountable statement; the theorem rests on §§3–5.

## 7. Limitations and honesty

- The proof uses $\diamondsuit_{\omega_1}$ essentially (capture + CH for
  countable levels). No ZFC claim is made.
- Standard walk/coherence facts are cited to Todorcevic; the
  successor-branching and chain-union closure are used as black boxes
  with explicit references, not re-derived.
- The finite script is an analogy at depth $10$ (delete-cone sealing);
  transfinite details (choice of $b_p$ covering all nodes, omission of
  the mod-finite class of $v$, prunedness induction) are proved
  mathematically, not machine-checked.
- Corollaries use the explicit whole-tree club-embedding / lower-basis
  definitions above; "basis $\ge 3$" is exactly Corollary B, not a claim
  about upper-universals outside the triple.
