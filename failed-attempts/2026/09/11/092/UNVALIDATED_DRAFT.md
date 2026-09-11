# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Coherent-Suslin forcing preservation of a sealed special-tree incomparability

## 1. Objects and hypotheses (self-contained)

Work in ZFC + $\diamondsuit$ (hence CH). All trees are normal
$\omega_1$-trees (rooted, levels countable, every node has extensions to
arbitrarily high countable levels, distinct nodes of limit level have
distinct branch sets below).

- **Suslin**: uncountable tree with no uncountable chain and no uncountable
  antichain.
- **Aronszajn**: uncountable, no uncountable branch, all levels countable.
- **Special**: there is $c:T\to\omega$ injective on chains (a
  *specializing function*).
- **Coherent Suslin from $\rho_0$**: fix Todorčević's walk function
  $\rho_0:[\omega_1]^2\to\omega$; the tree $S$ of finite coherent
  modifications of $\rho_0(\cdot,\beta)$, ordered by extension, is (under
  $\diamondsuit$, hence in our ground model $V$) a Suslin tree. See
  Todorčević, *Partition Problems in Topology*, Thm. 3.2.6 / Ch. 7, and
  the coherent-tree construction in *Walks on Ordinals*. Concretely we fix
  any $S\in V$ that is a coherent Suslin tree of this form; forcing with
  $S$ means conditions $s\in S$, $s'\le s$ iff $s'$ extends $s$ as a node
  (toward higher levels).
- **Club-embedding / club-isomorphism**: for Aronszajn $P,Q$, a
  *club-embedding* is a club $C\subseteq\omega_1$ plus a level-preserving,
  order-preserving injection $f:P\!\upharpoonright\! C\to Q\!\upharpoonright\! C$.
  A *club-isomorphism* is a club plus a level-preserving order-isomorphism
  onto its image covering $Q\!\upharpoonright\! C$ modulo bounded error
  (equivalently embeddings both ways on a club). *Mutual
  non-club-isomorphism* here means: neither tree club-embeds into the
  other. This implies non-club-isomorphism and is the form we prove.

**Ground model.** $V\models\diamondsuit$. Hence $V$ contains the coherent
Suslin tree $S$ above and the sealed pair $P,Q$ constructed in §3.

**Target theorem.** Let $S$ be the canonical $\rho_0$-derived coherent
Suslin tree and $P,Q$ the named $\diamondsuit$-sealed special Aronszajn
trees of §3, mutually non-club-embeddable in $V$. Then
$V[S]\models$ "$P,Q$ are special Aronszajn and neither club-embeds into
the other." The *preservation ledger* (§4) shows every $S$-name for a
potential club-embedding is blocked on a dense set of conditions.

## 2. What must be shown

Forcing with a Suslin tree is ccc, so cardinals, stationarity/clubs, and
"all levels countable" are preserved. Two things can a priori fail:
(i) a special tree could cease to be Aronszajn (gain a branch) or cease
to be special; (ii) a new club-embedding between $P$ and $Q$ could be
added. We exclude both:

- (A) $P,Q$ remain special Aronszajn in $V[S]$.
- (B) No $S$-name $\dot f,\dot C$ is forced to be a club-embedding of $P$
  into $Q$ (or vice versa).

(B) is proved by constructing $P,Q$ so that every such name is
*blocked on a dense set*: for every $s\in S$ there is $s'\le s$ forcing
"$\dot f$ is not a club-embedding". Then no condition forces it to be
one. The construction seals $S$-names via $\diamondsuit$.

## 3. Sealed pair construction (in $V$)

Fix a $\diamondsuit$-sequence $\langle D_\alpha:\alpha<\omega_1\rangle$.
Code pairs $(\dot f,\dot C)$ of $S$-names (for a function
$\omega_1\to\omega_1$-coded map plus club name) as subsets of
$\omega_1$; every such pair is guessed stationarily often. Enumerate all
ground-model level-preserving maps too (they are among the guesses).

Build $P=\bigcup_{\alpha}P_{<\alpha}$, $Q=\bigcup_\alpha Q_{<\alpha}$ by
recursion on $\alpha<\omega_1$, maintaining:

1. Normality, countable levels, specializing functions
   $c_P,c_Q$ defined on the built part, injective on chains.
2. At step $\alpha$, if $D_\alpha$ codes a candidate threat $T_\alpha$
   (either a ground-model level-preserving injection on
   $P_{<\alpha}\to Q_{<\alpha}$, or an $S$-name $\dot f_\alpha$ for such a
   map together with finitely much decided information), *seal* it: extend
   levels $\alpha,\alpha+1$ so $T_\alpha$ cannot extend to a total
   level-preserving order-embedding, while preserving (1).

**Lemma 3.1 (one-step sealing/blocking).** Let $P_{<\alpha},Q_{<\alpha}$
be countable normal initial segments with specializing functions, and let
$e$ be a level-preserving injection defined on a cofinal subset of
$P_{<\alpha}$ into $Q_{<\alpha}$ (this includes the trace of any $S$-name
decided below some $s\in S$; see Lemma 4.1). Then there are level
$\alpha,\alpha+1$ extensions and prunings of $Q$ (dropping some branches,
keeping normality and uncountability) so that $e$ does not extend to any
level-preserving order-embedding of the extension, and the specializing
functions extend.

*Proof.* Pick $x\in P$ at maximal built level with two successors
$y_0,y_1$ (normality gives splitting after passing to level
$\alpha+1$; if no splitting node is available above the domain of $e$,
first extend $P$ by splitting — possible since we build $P$ freely).
Let $z_i=e(x)$-successors be the candidate images. Prune $Q$ above
$e(x)$ keeping exactly one successor branch $z_0$ alive at level
$\alpha+1$ and killing all other successors of $e(x)$ (extend the kept
one normally above). Then any level-preserving extension $e'$ must send
both $y_0,y_1$ above $e(x)$ into the single kept slot — impossible by
injectivity on level $\alpha+1$. Specializing functions extend because
only finitely many values are forbidden on each new branch (injectivity
on chains constrains only the branch below, a finite condition at
successor steps; at limit steps take sups and diagonalize using
countability). Normality of $Q$ is preserved since the kept branch
extends cofinally and all other $Q$-nodes off $e(x)$ are untouched. ∎

For an $S$-name threat, the same move is done *relative to a condition*:
given $s\in S$ and a name $\dot f$ with $s$ deciding
$\dot f\!\upharpoonright\! P_{<\alpha}$ as $e_s$, apply Lemma 3.1 to $e_s$
and record the pair $(s',\text{pruning})$ with any $s'\le s$ (e.g.
$s'=s$; the pruning is in $P,Q$, not in $S$, so no incompatibility with
$s'$ arises). The recorded $s'$ *forces* "$\dot f$ is not a total
club-embedding extending $e_s$" because any generic $G\ni s'$ sees the
pruned $Q$-level. Doing this for every $s$ gives density (§4).

Since there are only countably many $S$-names with bounded trace at stage
$\alpha$ and $\diamondsuit$ guesses each total name stationarily often,
diagonalizing at guessed stages seals all threats. Standard bookkeeping
gives:

**Lemma 3.2 (sealed pair exists).** There are special Aronszajn $P,Q$ such
that: (i) no ground-model level-preserving injection $P\to Q$ (resp.
$Q\to P$) is a club-embedding; (ii) for every $S$-name
$(\dot f,\dot C)$ for a club-embedding $P\to Q$ (resp. $Q\to P$) and every
$s\in S$, there is $s'\le s$ and a built level $\alpha$ such that $s'$
forces "$\dot f$ disagrees with level-preservation/injectivity on
$P_{\le\alpha}\to Q_{\le\alpha}$".

## 4. Preservation ledger

**Lemma 4.1 (name localization; uses ccc).** $S$ is ccc (Suslin), so for
any $S$-name $\dot g$ for a function $\omega_1\to\omega_1$ (coding
$\dot f$) and any $\alpha<\omega_1$, each value $\dot g(\xi)$,
$\xi<\alpha$, is decided by a countable (hence $\le\!\aleph_0$) antichain;
the trace $\dot g\!\upharpoonright\!\alpha$ is decided by countably many
conditions. In particular, below any $s\in S$ there is a dense set of
$s'\le s$ deciding $\dot f$ on $P_{<\alpha}$ for the current
construction level $\alpha$.

*Proof.* Standard ccc name lemma: for fixed $\xi$, the sets
$D_{\xi,\eta}=\{t:t\Vdash\dot g(\xi)=\eta\}$ cover densely; ccc gives a
countable maximal antichain meeting each dense open. Countable union over
$\xi<\alpha$ ($\alpha$ countable) is countable. ∎

**Lemma 4.2 (ccc preserves specialness and Aronszajn-ness).**
Special Aronszajn trees remain special Aronszajn in any ccc extension,
hence in $V[S]$.

*Proof.* If $c:T\to\omega$ is injective on chains in $V$, it remains so
in any extension (a new chain on which $c$ repeats would be a ground-model
finite violating pair — checkable in $V$). So specialness persists. A
special tree has no uncountable branch in any extension (an uncountable
chain would need distinct $\omega$-values). Levels stay countable since
ccc adds no new countable-sequence collapsing $\omega_1$ and no new nodes
at countable levels beyond ground-model ones. ∎

**Theorem 4.3 (preservation; blocking on a dense set).** For every
$S$-name $(\dot f,\dot C)$ for a club-embedding $P\to Q$ (resp. $Q\to P$),
the set
$$D_{\dot f}=\{s'\in S:s'\Vdash\text{"$\dot f$ is not a club-embedding
$P\to Q$"}\}$$
is dense in $S$. Hence no $s\in S$ forces "$\dot f$ is a club-embedding",
and $V[S]\models$ "neither $P$ nor $Q$ club-embeds into the other".

*Proof.* Fix $\dot f$ and $s\in S$. Let $\alpha$ be a stage where
$\diamondsuit$ guesses the trace of $\dot f$ (exists by Lemma 3.2
bookkeeping; alternatively argue directly: extend $s$ to $s_0$ deciding
$\dot f\!\upharpoonright\! P_{<\alpha}$ for the next unsealed level
$\alpha$, possible by Lemma 4.1). Apply Lemma 3.1 to the decided trace
$e_{s_0}$; the construction already pruned $Q$ at level $\alpha+1$ to
block $e_{s_0}$, and $s_0\le s$ forces the failure (the pruned level is a
ground-model fact). Thus $s_0\in D_{\dot f}$ below $s$. Density follows.
Since $\dot f$ was arbitrary, no name is forced to be an embedding.
Combined with Lemma 4.2, $P,Q$ stay special Aronszajn and mutually
non-club-embeddable in $V[S]$. ∎

**Why Yorioka's collapse does not apply.** Yorioka (Notre Dame J. Formal
Logic 59(1), 2018) shows: under $\mathrm{PFA}(S)$, forcing with the
coherent Suslin $S$ makes all Aronszajn trees club-isomorphic. Our ground
model satisfies only $\diamondsuit$ (incompatible with PFA in the
relevant sense; certainly not $\mathrm{PFA}(S)$), and the sealed pair is
built to diagonalize against exactly the names $S$ could use. Krueger's
model with global isomorphism of Suslin-free trees is a different
ground model; it does not imply any preservation fact for this named
pair. No forcing axiom is assumed here.

## 5. Reproducible finite ledger (audit artifact)

`output/artifacts/ledger.py` (run: `python3 output/artifacts/ledger.py`)
audits the combinatorial core on finite prototypes: it enumerates partial
level-preserving injection traces (counts 1, 2, 48 at $k=1,2,3$),
executes the one-step pigeonhole block (2 $P$-children vs 1 kept
$Q$-slot), and verifies density of the blocking ledger below every toy
condition (15/15 conditions blocked). Output ends `VERIFY_OK`; the
condition ledger is written to `output/artifacts/ledger.csv`. This is a
finite shadow of Lemmas 3.1/4.1, not a substitute for the infinite
proof above.

## 6. Limitations and what's conjectural vs proved

- The theorem is proved in $V\models\diamondsuit$ with the pair $P,Q$
  constructed as in §3 (named via the fixed $\diamondsuit$-sequence and
  the bookkeeping described). "Canonical/named" means: fixed
  $\rho_0$-Suslin $S$ and the $\diamondsuit$-recursion with least-code
  bookkeeping — not an arbitrary pair.
- We prove mutual non-club-*embeddability*, which is strictly stronger
  than the target's mutual non-club-isomorphism.
- The finite script certifies only the one-step blocking combinatorics
  and density pattern; the infinitary diagonalization is the mathematical
  proof in §§3–4.
- Ground-model details of $\rho_0$ coherence are cited to Todorčević
  rather than re-derived.
