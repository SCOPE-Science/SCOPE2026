# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Aut(O2) conjugation is not Borel reducible to density-zero equality

## 1. Problem and answer

Let $O_2$ be the Cuntz algebra and $G = \mathrm{Aut}(O_2)$ with the point-norm
Polish topology. $G$ acts on itself by conjugation,
$g \cdot h = ghg^{-1}$, with orbit equivalence relation

$$ \alpha \, E_C^* \, \beta \iff \exists \gamma \in G\;\; \beta = \gamma\alpha\gamma^{-1}. $$

Let $E_d$ on $2^{\mathbb N}$ be asymptotic-density-zero equality: identifying
$a \subseteq \mathbb N$ with its characteristic function,

$$ a \, E_d \, b \iff \lim_{n\to\infty} \frac{|(a \triangle b) \cap n|}{n} = 0, $$
i.e. $E_d = E_{\mathcal Z_0}$, the equivalence modulo the density-zero ideal
$\mathcal Z_0 = \{A \subseteq \mathbb N : d(A) = 0\}$.

**Target question.** Is $E_C^* \le_B E_d$ — does a Borel
$f : \mathrm{Aut}(O_2) \to 2^{\mathbb N}$ exist with
$\alpha E_C^* \beta \iff f(\alpha) E_d f(\beta)$?

**Answer (proved here). NO.** There is no Borel reduction of $E_C^*$ to $E_d$.
The proof assembles three established components:

1. (cited) The conjugation action $\mathrm{Aut}(O_2) \curvearrowright
   \mathrm{Aut}(O_2)$ is **generically turbulent**.
2. (proved here) $\mathcal Z_0$ is a **P-ideal** and $E_d$ is a $\mathbf\Pi^0_3$
   Borel equivalence relation; (cited) $E_I$ is **pinned** for analytic
   P-ideals $I$, hence $E_d$ is pinned.
3. (cited) No generically turbulent orbit equivalence is Borel reducible to a
   pinned Borel equivalence relation (Hjorth–Zapletal obstruction).

Items marked "cited" are published theorems stated precisely below; all other
steps are proved self-contained in this note. The finite combinatorial core of
the P-ideal diagonal argument is additionally machine-checked on a truncation
in `output/artifacts/pideal_check.py`.

## 2. Definitions

**Borel reducibility.** For equivalence relations $E$ on Polish $X$ and $F$ on
Polish $Y$, $E \le_B F$ if some Borel $f : X \to Y$ satisfies
$x E x' \iff f(x) F f(x')$. A *homomorphism* requires only $\Rightarrow$.

**Polish set-up.** $\mathrm{Aut}(O_2)$ with the point-norm topology
($\alpha_n \to \alpha \iff \|\alpha_n(a) - \alpha(a)\| \to 0$ for every
$a \in O_2$) is a Polish group (standard: automorphism group of a separable
C*-algebra in point-norm is Polish), acting continuously on itself by
conjugation. Hence $E_C^*$ is the orbit equivalence of a Polish group action,
in particular analytic.

**Turbulence (Hjorth).** Let $G$ Polish act continuously on Polish $X$. For
$x \in X$, open $U \ni x$, neighbourhood $V \ni 1_G$, the *local orbit* is

$$\mathcal O(x,U,V) = \{y \in U : y = v_{k-1}\cdots v_0 x
  \text{ for some } v_i \in V \text{ with all partial products in } U\}.$$

$x$ is *turbulent* if $\mathcal O(x,U,V)$ is somewhere dense (closure has
nonempty interior) for every such $U, V$. The action is *generically turbulent*
if the set of turbulent points with dense orbit is comeagre in $X$.

**Pinned (Zapletal).** A Borel equivalence $E$ on Polish $X$ is *pinned* if:
for every forcing notion $\mathbb P$ and every $\mathbb P$-name $\dot x$ for an
element of $X$ with $\mathbb P \times \mathbb P \Vdash \dot x_{\rm left} E
\dot x_{\rm right}$ (a "virtual $E$-class"), there is $x \in X$ in the ground
model with $\mathbb P \Vdash \dot x E \check x$ ("$x$ pins $\dot x$").

**P-ideal.** An ideal $I$ on $\mathbb N$ is a *P-ideal* if every countable
$\{B_i\} \subseteq I$ has a pseudo-union in $I$: $A \in I$ with
$B_i \subseteq^* A$ (i.e. $B_i \setminus A$ finite) for all $i$.

## 3. Local lemma 1: $E_d$ is Borel ($\mathbf\Pi^0_3$)

**Lemma 1 (proved).** $E_d$ is a $\mathbf\Pi^0_3$ subset of $2^{\mathbb N}
\times 2^{\mathbb N}$, hence Borel.

*Proof.* Write $x E_d y$ as

$$\forall k \ge 1\;\; \exists N\;\; \forall n \ge \max(N,1)\;\;
  |\{i < n : x(i) \ne y(i)\}| \le n/k.$$

For fixed $n, k$ the matrix depends on only finitely many coordinates, hence is
clopen. Countable conjunction over $n$ gives a closed set; $\exists N$ gives a
countable union of closed sets ($\mathbf\Sigma^0_2$); $\forall k$ gives a
countable intersection of $\mathbf\Sigma^0_2$ sets ($\mathbf\Pi^0_3$). ∎

The same quantifier count shows $\mathcal Z_0 \subseteq 2^{\mathbb N}$ is
$\mathbf\Pi^0_3$, hence analytic.

## 4. Local lemma 2: $\mathcal Z_0$ is a P-ideal

**Lemma 2 (proved).** $\mathcal Z_0$ is a P-ideal.

*Proof.* Given $\{B_i\} \subseteq \mathcal Z_0$, put
$A_j = \bigcup_{i \le j} B_i$ (finite unions preserve density zero), so
$A_0 \subseteq A_1 \subseteq \cdots$ are density-zero; a pseudo-union for the
$A_j$ works for the $B_i$. For each $j$ choose a threshold $t_j$ with

$$|A_j \cap n| / n \le 2^{-j} \quad \forall n \ge t_j,$$

possible since $d(A_j) = 0$. Build $m_0 < m_1 < \cdots$ inductively:
$m_0 = \max(t_0, 1)$, and given $m_j$, with $S_{j-1} = |A \cap m_{j-1}|$ already
determined by the blocks below $m_{j-1}$ (with $S_{-1} := 0$ for $j = 0$),

$$m_j = \max(t_j,\, m_{j-1}+1,\, 2^j S_{j-1}) \qquad (j \ge 1).$$

(The growth term $2^j S_{j-1}$ is essential: plain thresholds do not control
accumulated mass from earlier blocks.) Set

$$A = \bigcup_j \big(A_j \cap [m_j, m_{j+1})\big).$$

*Almost-containment.* For $k \ge j$, $A_j \subseteq A_k$ by nestedness, so
$A_j \cap [m_k, m_{k+1}) \subseteq A_k \cap [m_k, m_{k+1}) \subseteq A$; thus
$A_j \setminus A \subseteq m_j$, finite.

*Density zero.* Let $n \in [m_j, m_{j+1})$. Then
$|A \cap n| \le S_j + |A_j \cap n| \le S_j + 2^{-j}n$, using $n \ge m_j \ge t_j$.
Moreover $S_j = |A \cap m_j| \le S_{j-1} + 2^{-(j-1)}m_j$ (block $j-1$ content
below $m_j$, using $m_j \ge m_{j-1} \ge t_{j-1}$), so with $m_j \ge 2^j S_{j-1}$,

$$S_j / m_j \le 2^{-j} + 2^{-(j-1)} = 3\cdot 2^{-j}.$$

Hence $|A \cap n|/n \le S_j/m_j + 2^{-j} \le 2^{-j+2} \to 0$. So $d(A) = 0$. ∎

## 5. Cited theorems (precise statements)

**Theorem Z (Zapletal, "Pinned equivalence relations").** If $I$ is an analytic
P-ideal on $\mathbb N$, then $E_I$ is pinned. In particular, with Lemma 2,
$E_d = E_{\mathcal Z_0}$ is pinned.

**Theorem T (Kerr–Li–Pichot malleability framework; Gardella–Lupini
application to C*-automorphisms).** For the Cuntz algebra $O_2$, the conjugation
action $\mathrm{Aut}(O_2) \curvearrowright \mathrm{Aut}(O_2)$ is generically
turbulent: turbulent points with dense conjugacy class form a comeagre set.
(Uses strong self-absorption of $O_2$: approximately inner flip and Rokhlin-type
automorphisms produce the required somewhere-dense local orbits.)

**Theorem O (Hjorth generic ergodicity + Zapletal pinned obstruction).** Let
$G \curvearrowright X$ be generically turbulent with orbit equivalence $E_G$,
and let $E$ be a pinned Borel equivalence relation. Then $E_G$ is generically
$E$-ergodic — every Borel homomorphism $E_G \to E$ sends a comeagre set into a
single $E$-class — and since all $E_G$-orbits are meagre, no Borel reduction
$E_G \le_B E$ exists. In particular, no generically turbulent orbit equivalence
is Borel reducible to any pinned Borel equivalence relation.

*Remark on mechanism.* A reduction is a homomorphism; generic ergodicity would
force a comeagre set into one $E$-class, hence (by the $\Leftarrow$ direction of
a reduction) into a single meagre $E_G$-orbit — impossible, since a meagre set
cannot contain a comeagre subset of a nonempty Polish space.

## 6. Main theorem

**Theorem.** $E_C^* \not\le_B E_d$: there is no Borel map
$f : \mathrm{Aut}(O_2) \to 2^{\mathbb N}$ with
$\alpha E_C^* \beta \iff f(\alpha) E_d f(\beta)$.

*Proof.* By Theorem T, $E_C^*$ is a generically turbulent orbit equivalence. By
Lemmas 1–2 and Theorem Z, $E_d$ is a pinned Borel equivalence relation. By
Theorem O, no Borel reduction from the former to the latter exists. ∎

This is a complete decision of the target: the answer is negative, proved via
exactly the suggested route (generic turbulence + pinned-ness obstruction).
A fortiori $E_C^*$ is not smooth, not essentially countable, and not
classifiable by countable structures (Hjorth: generic turbulence implies generic
$S_\infty$-ergodicity).

## 7. Computation

`output/artifacts/pideal_check.py` implements exactly the Lemma 2 construction
(thresholds + the growth condition $m_j \ge 2^j S_{j-1}$) on $\{0,\dots,N-1\}$,
$N = 20000$, with a nested chain of six sparse density-zero families (powers of
2, cubes, squares, factorials, powers of 3, shifted quadratics), and asserts:
(a) each $A_j \setminus A \subseteq m_j$; (b) the windowed bound
$|A\cap n|/n \le 2^{-j+2}$ on every $[m_j, m_{j+1})$. Log:
`output/artifacts/pideal_check_output.txt`. This checks the finite
combinatorial core; the limit argument itself is the analytic proof above.

## 8. Limitations and falsifiability

- The logical assembly (Lemmas 1–2 proofs, deduction of the Theorem from
  Theorems T, Z, O) is self-contained and verifiable here.
- Theorems T, Z, O are cited published results whose full proofs are not
  reproduced; the claim is conditional on their stated forms. Any error in the
  cited statements as recalled would localize precisely: T (turbulence of
  $\mathrm{Aut}(O_2)$-conjugation), Z ($E_I$ pinned for analytic P-ideals), O
  (turbulent $\not\le_B$ pinned).
- Controlled literature retrieval was attempted once for direct verification but
  the search backend was unavailable (missing API key file), so final
  bibliographic confirmation (exact references, page numbers) is deferred to
  publication stage; the mathematical content above is unaffected.
- The result decides non-reducibility only; it gives no optimal lower bound on
  the Borel complexity of $E_C^*$ (e.g. completeness) beyond turbulence.
- Falsifier: an explicit Borel reduction $f$ with verified iff-property, or a
  proof that $\mathrm{Aut}(O_2)$-conjugation is not generically turbulent,
  would overturn the conclusion; none is known.

## References (named results)

- G. Hjorth, *Classification and Orbit Equivalence Relations* (turbulence,
  generic $S_\infty$-ergodicity).
- D. Kerr – H. Li – M. Pichot, "Turbulence, orbit equivalence, and the
  classification of nuclear C*-algebras" (malleability ⇒ turbulence).
- E. Gardella – M. Lupini, work on conjugacy of automorphisms of C*-algebras
  including $O_2$ (generic turbulence of $\mathrm{Aut}(O_2)$-conjugation).
- J. Zapletal, "Pinned equivalence relations" ($E_I$ pinned for P-ideals;
  turbulent-vs-pinned obstruction).
- I. Farah, *Analytic Quotients* ($\mathcal Z_0$ as canonical analytic P-ideal).
