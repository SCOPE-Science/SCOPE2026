# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Generic ergodicity of rank-one mixing conjugacy — resolution

## 1. Setting and literal target

Let $X=\mathrm{MPT}$ be the Polish group of measure-preserving transformations of
$([0,1],\mathrm{Leb})$ with the weak topology. Let

$$Y = R\cap M \subset X$$

be the ergodic rank-one mixing class with the subspace topology and subspace Borel
structure, and $E$ conjugacy restricted to $Y$.
The target asks to determine whether $E$ is generically ergodic for countable-structure
invariants in the sense:

> every Borel homomorphism $f$ from $E$ to isomorphism on countable structures maps
> some relatively comeager $C\subset Y$ into a single isomorphism class,

versus exhibiting a Borel countable invariant separating a relatively non-meager set
of pairwise non-conjugate elements.

The target statement additionally calls $Y$ a "Polish subspace". We show this
presupposition is false, and that with relative Baire category the dichotomy
collapses degenerately.

## 2. Classical inputs (cited, not reproved)

We use only standard theorems:

- (a) $X$ is Polish, perfect, with no isolated points.
- (b) Halmos conjugacy lemma: the conjugacy class of any aperiodic $T$ is dense in $X$.
- (c) Halmos–Rohlin: the mixing class $M$ is dense and meager (first category) in $X$.
  Density follows from (b) since Bernoulli shifts are aperiodic mixing; meagerness is
  the classical "in general $T$ is not mixing" theorem.
- (d) Ornstein: there exists a rank-one mixing $T_0$. Hence $Y\neq\varnothing$.
  Mixing implies aperiodic, so $T_0$ is aperiodic.
- (e) Rank-one and mixing are conjugacy-invariant.
- (f) Alexandrov / Kechris 3.11: a subspace of a Polish space is Polish in the subspace
  topology iff it is $G_\delta$ in the ambient space.
- (g) Baire: a dense $G_\delta$ in a Polish space is comeager.

No literature search was needed; these are textbook facts.

## 3. $Y$ is dense meager, hence not Polish

By (d)–(e), the full conjugacy orbit $[T_0]\subset Y$. By (b) and aperiodicity of $T_0$,
$[T_0]$ is dense in $X$. Hence $Y$ is dense in $X$.

Since $Y\subset M$ and $M$ is meager by (c), $Y$ is meager in $X$
(subset of a meager set is meager: subsets of nowhere-dense sets are nowhere dense).

If $Y$ were $G_\delta$ in $X$, density plus (g) would make it comeager in $X$.
A nonempty perfect Polish $X$ cannot have a set both meager and comeager.
Hence $Y$ is not $G_\delta$, and by (f) $Y$ is not Polish in the weak subspace topology.
This refutes the "Polish subspace" presupposition as stated.
Script `output/artifacts/check_polish_obstruction.py` records this chain.

## 4. $Y$ is meager in itself

Write $M\subset\bigcup_n F_n$ with $F_n$ nowhere dense in $X$ (take closures to assume
closed). Then $Y\subset\bigcup_n (F_n\cap Y)$.
Claim: each $F_n\cap Y$ is nowhere dense in $Y$, using density of $Y$.
Indeed, let $V\subset X$ be open with $V\cap Y\subset \overline{F_n\cap Y}^X$.
Since $Y$ is dense and $V$ open, $\overline{V\cap Y}^X=\bar V$.
Taking closures gives $\bar V\subset\bar F_n$, so $V\subset\bar F_n$.
Since $F_n$ is nowhere dense, $V=\varnothing$. Thus
$\mathrm{int}_Y\overline{F_n\cap Y}^Y=\varnothing$.
So $Y$ is meager in itself. Consequently every $A\subset Y$ is meager in $Y$
(subset of a meager set is meager by the same hereditary argument).

## 5. Vacuous generic ergodicity; second horn impossible

Let $f$ be any Borel homomorphism from $E$ to isomorphism of countable structures
(in any countable language). Pick $x_0\in Y$ and $C=\{x_0\}$.
Then $Y\setminus C\subset Y$ is meager in $Y$ by §4, so $C$ is relatively comeager in $Y$.
$f(C)$ is a singleton, hence contained in a single isomorphism class.
Thus $E$ satisfies the literal generic-ergodicity clause — vacuously, for every
equivalence relation on $Y$, including smooth ones such as equality.
Script `output/artifacts/check_trivial_generic_ergodicity.py` records the chain.

Dually, there is no relatively non-meager $A\subset Y$ at all, so the second horn
(Borel countable invariant separating a non-meager set of pairwise non-conjugate
elements) is impossible.

## 6. What this does and does not show

Proved: literally, with relative Baire category, the answer is "yes, generically
ergodic", by degeneracy; the invariant horn is impossible; the Polish premise is false.
Not proved: any turbulence-based non-classification in the intended Polish sense.
The vacuous argument gives no classification obstruction (equality on $Y$ passes the
same test), so it must not be read as the intended Hjorth-turbulence result.
A non-degenerate formulation would need a different (finer) Polish topology or ambient
category reading, which the target does not supply. The result is therefore a complete
literal determination plus refutation of the presupposition, obtained by elementary
Baire reasoning from classical theorems, with no originality claimed for the
Baire observation itself.
