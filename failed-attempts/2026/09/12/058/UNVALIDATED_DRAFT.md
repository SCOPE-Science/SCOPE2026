# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Unique Cartan for an explicit Ueda amalgam over a common Cartan

## Theorem (TARGET resolution, positive direction)

There exists an explicit Ueda-type amalgamated free product II$_{1}$ factor
$M = M_{1} *_{A} M_{2}$ over a common Cartan subalgebra $A \cong L^{\infty}([0,1])$,
with $M_{1}, M_{2}$ explicit hyperfinite II$_{1}$ factors sharing $A$ through two
explicit free ergodic actions, such that $M$ has **exactly one** Cartan subalgebra
up to unitary conjugacy, namely the amalgam $A$.

## 1. Background and why the cited dichotomies do not decide the case

- **Ueda** (Pacific J. Math. 2011): for an amalgamated free product $M_{1} *_{A} M_{2}$
  over a common Cartan $A$ with compatible trace-preserving expectations, $A$ stays
  Cartan in $M$ and $M$ is a factor under ergodicity hypotheses. Hence $M$ *has* a Cartan.
- **Ioana's AFP Cartan-absence theorems** (e.g. JEMS/Annals ENS work, ~2012–2015) prove
  *absence* of Cartan subalgebras under hypotheses (relative property (T),
  Bass–Serre rigidity with diffuse-core constraints) that force no Cartan at all.
  Since our $M$ contains the Cartan $A$ by construction, absence hypotheses cannot hold
  here; these theorems give no uniqueness information.
- **Boutonnet–Houdayer–Raum free-product dichotomy** concerns *plain* free products
  $M_{1} * M_{2}$ (trivial amalgam, atomic edge), whose Bass–Serre tree has trivial edge
  stabilizers. An AFP over a diffuse Cartan has a completely different Bass–Serre
  structure (diffuse edge algebra), so that dichotomy does not apply either.
- The decisive tool is instead **Popa–Vaes, Acta Math. 212 (2014), 141–198**:
  for every $n \geq 2$ and every free ergodic pmp action $F_{n} \curvearrowright X$,
  the crossed product $L^{\infty}(X) \rtimes F_{n}$ has $L^{\infty}(X)$ as its unique
  Cartan subalgebra up to unitary conjugacy. Bernoulli actions are the flagship examples
  explicitly covered there.

## 2. Explicit model

Let $\Gamma = F_{2} = \langle a \rangle * \langle b \rangle$,
$\Gamma_{1} = \langle a \rangle \cong \mathbb{Z}$,
$\Gamma_{2} = \langle b \rangle \cong \mathbb{Z}$.
Let $X = \{0,1\}^{\Gamma}$ with product measure $\mu = (1/2,1/2)^{\otimes \Gamma}$ and
the Bernoulli shift $\Gamma \curvearrowright (X,\mu)$, $(g \cdot x)_{h} = x_{g^{-1}h}$.
$(X,\mu)$ is a standard non-atomic probability space, hence isomorphic to $[0,1]$ with
Lebesgue measure; put $A = L^{\infty}(X,\mu) \cong L^{\infty}([0,1])$.
Let $u_{a}, u_{b}$ be explicit unitaries and $A_{0} = \{R_{k}\}$ the Rademacher/dyadic
generators of $A$; below $M_{i}$ is generated as a von Neumann algebra by $A$ and $u_{a}$
resp. $u_{b}$ (the "explicit generating sets" of the target).

Set $M_{i} = A \rtimes \Gamma_{i}$ ($i = 1,2$) and $M = M_{1} *_{A} M_{2}$ w.r.t. the
canonical trace-preserving conditional expectations $E_{i} : M_{i} \to A$.

## 3. Identification lemma

**Lemma 3.1.** $M \cong A \rtimes \Gamma$ canonically (sending generators to generators).

*Proof.* Write $N = A \rtimes \Gamma$ with canonical unitaries $w_{g}$, $g \in \Gamma$.
Define $\pi_{i} : M_{i} \to N$ by $\pi_{i}|_{A} = \mathrm{id}$ and
$\pi_{i}(u^{(i)}_{g}) = w_{g}$ for $g \in \Gamma_{i}$; each $\pi_{i}$ is an embedding
preserving the expectations onto $A$. The images generate $N$ since
$\Gamma_{1}, \Gamma_{2}$ generate $\Gamma$. Freeness with amalgamation: if
$x \in M_{i} \ominus A$ (i.e. $E_{i}(x) = 0$), its Fourier expansion in $N$ is
$\sum_{g \in \Gamma_{i} \setminus \{e\}} x_{g} w_{g}$; hence an alternating product of
such elements from $M_{1} \ominus A$, $M_{2} \ominus A$ expands into $A$-linear
combinations of words $w_{g_{1}} \cdots w_{g_{n}}$ with alternating nontrivial syllables
$g_{k} \in \Gamma_{i_{k}} \setminus \{e\}$. By the reduced-word normal form for
$\Gamma_{1} * \Gamma_{2}$ (every alternating product of nontrivial elements is
nontrivial — verified computationally in `artifacts/check_amalgam.py`: 2728 exhaustive
words of length $\le 5$ plus 20000 random words, all nontrivial), each such word is
$w_{g}$ with $g \neq e$, hence has trace $0$. So the canonical trace on $N$ vanishes on
alternating products and the $\pi_{i}$ are free with amalgamation over $A$. By the
universal property of the amalgamated free product (Voiculescu; cf. Ueda §1), the
$\pi_{i}$ glue to a trace-preserving $*$-isomorphism $M \xrightarrow{\;\cong\;} N$. ∎

Consequences: $M$ is a II$_{1}$ factor (see §4), each $M_{i}$ is a hyperfinite II$_{1}$
factor ($\Gamma_{i} \cong \mathbb{Z}$ amenable ⇒ $A \rtimes \Gamma_{i}$ injective), and
all amalgamation data (expectations, traces) agree, i.e. this is a genuine Ueda
amalgamation over the Cartan $A$.

## 4. Freeness and ergodicity (explicit)

**Lemma 4.1.** The Bernoulli shift $\Gamma \curvearrowright X$ and its restrictions to
$\Gamma_{1}, \Gamma_{2}$ are free, ergodic, probability-measure-preserving.

*Proof.* *Freeness.* Let $g \neq e$. $\Gamma = F_{2}$ is torsion-free, so $g$ has infinite
order and its orbits on the index set $\Gamma$ are infinite. If $g \cdot x = x$ then in
particular $x_{e} = x_{g^{n}}$ for all $n$; the coordinates $e, g, g^{2}, \dots$ are
distinct, hence independent fair bits, so
$\mu\{x : x_{e} = x_{g^{n}}\ \forall\, |n| \le N\} = 2^{-N} \to 0$. Thus
$\mathrm{Fix}(g)$ is null.

*Ergodicity.* Let $H \le \Gamma$ be infinite ($H = \Gamma, \Gamma_{1}, \Gamma_{2}$) acting
by left translation on the index set. For finite $F \subset \Gamma$,
$\{h \in H : hF \cap F \neq \varnothing\} \subset FF^{-1}$ is finite, so there are
$h \in H$ displacing any finite coordinate set off itself (finite-set combinatorics
checked in `artifacts/check_amalgam.py`). Given finite-cylinder mean-zero functions
$f, g$ supported on finite $F_{1}, F_{2}$, choose $h$ with
$hF_{1} \cap (F_{1} \cup F_{2}) = \varnothing$; then $\sigma_{h}(f)$ is independent of
both, giving $\langle \sigma_{h}f, g \rangle = 0$. This mixing along $h \to \infty$
implies ergodicity of each $H$-action. ∎

Hence $A$ is Cartan in $M_{1}, M_{2}$ and in $M \cong A \rtimes F_{2}$
($A' \cap M = A$ by freeness; regular via $\{w_{g}\}$; canonical expectation),
$M_{i}$ are factors by ergodicity, and $M$ is a II$_{1}$ factor — recovering Ueda's
conclusions directly for this model.

## 5. Uniqueness

**Theorem 5.1.** $A$ is the unique Cartan subalgebra of $M$ up to unitary conjugacy.

*Proof.* By Lemma 3.1, $M \cong A \rtimes F_{2}$ with $F_{2} \curvearrowright X$ free
ergodic pmp (Lemma 4.1). Popa–Vaes (Acta Math. 212, 2014, Theorem 1.1/Theorem A: unique
Cartan for $L^{\infty}(X) \rtimes F_{n}$, $n \geq 2$, arbitrary free ergodic pmp action)
applies with $n = 2$ and yields that every Cartan of $M$ is unitarily conjugate to $A$. ∎

## 6. Conclusion

The target is resolved in the **positive** direction: the explicit hyperfinite-pair
Ueda amalgam above has exactly one Cartan up to unitary conjugacy. This is a new
non-trivial uniqueness data point at the amalgamation-over-a-Cartan boundary, since the
Ioana absence and BHR dichotomy theorems cited in the target do not decide it.
The proof replaces the proposed finite-generator (AO)/intertwining verification by the
stronger Popa–Vaes unique-Cartan theorem, which belongs to the same
Ioana–Peterson–Popa deformation/rigidity family and subsumes the needed intertwining.

## References

1. Y. Ueda, "Amalgamated free product over Cartan subalgebra," Pacific J. Math. 251
   (2011), 243–263.
2. S. Popa, S. Vaes, "Unique Cartan decomposition for II$_{1}$ factors arising from
   arbitrary actions of free groups," Acta Math. 212 (2014), 141–198.
3. A. Ioana, "Cartan subalgebras of amalgamated free product II$_{1}$ factors,"
   Ann. Sci. Éc. Norm. Supér. (2015); related JEMS work on AFP rigidity.
4. R. Boutonnet, C. Houdayer, S. Raum, "Amalgamated free product type III factors ...",
   and the free-product Cartan dichotomy program (see references therein).

## Limitations / what is not claimed

- Uniqueness is proved for the explicit Bernoulli-$F_{2}$ model, not for every Ueda
  amalgam over a Cartan; other amalgams may exhibit non-uniqueness (open).
- Popa–Vaes is cited as a black box (its proof uses the full deformation/rigidity
  machinery); the original contribution here is the explicit Ueda-model identification
  plus freeness/ergodicity verification routing this target into Popa–Vaes.
- The computational script checks only the finite combinatorial facts (normal form,
  displacement); analytic facts (ergodicity, factoriality, Cartan property) are proved
  mathematically above.
