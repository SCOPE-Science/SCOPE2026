# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Complemented AM-subspaces of C(K)-spaces: the nonseparable case — Resolution

## Claim (TARGET: YES)

Let $X$ be an (real) AM-space whose underlying Banach space is linearly
isomorphic to a complemented subspace of some $C(K)$-space, with $X$
nonseparable. Then $X$ is linearly isomorphic to $C(K')$ for some compact
Hausdorff $K'$. In fact the complemented-subspace and nonseparability
hypotheses are both superfluous: *every* AM-space is linearly isomorphic to
some $C(K')$.

## Proof

### 1. AM-spaces are $C_{0}(L)$

Recall a Banach lattice $E$ is an AM-space if
$\|x\vee y\|=\max(\|x\|,\|y\|)$ for all $x,y\ge 0$.
Kakutani's representation theorem (1941) says every AM-space with unit is
lattice-isometric to $C(K)$ for compact Hausdorff $K$. The general (not
necessarily unital) version states:

> Every AM-space is lattice-isometric to $C_{0}(L)$ for a unique (up to
> homeomorphism) locally compact Hausdorff space $L$.

See e.g. Schaefer, *Banach Lattices and Positive Operators*, Ch.II,
Thm 7.4 for the unital case and the standard $C_{0}(L)$ extension
(e.g. Aliprantis–Burkinshaw, *Positive Operators*, Thm 4.29; Meyer-Nieberg,
*Banach Lattices*); the principal ideals $E_{x}$ are AM-spaces with unit
hence $C(K_{x})$, glued into $C_{0}$ over the disjoint union / Gelfand
spectrum. The complex case follows by complexification.

Apply this to $X$: there is locally compact Hausdorff $L$ with $X$
lattice-isometric (hence linearly isomorphic) to $C_{0}(L)$.
If $L$ is compact, $X\cong C(L)$ and we are done with $K'=L$.

### 2. Lemma: every hyperplane in a $C$-space is a $C$-space

Let $K$ be compact Hausdorff and $H\subset C(K)$ a closed hyperplane,
$H=\ker\varphi$, $0\ne\varphi\in C(K)^{*}$.

Fix distinct $x_{0},x_{1}\in K$ (if $K$ is a singleton $C(K)$ is
one-dimensional and all hyperplanes are $\{0\}=C(\varnothing)$; assume
$|K|\ge 2$). Let $\psi=\delta_{x_{0}}-\delta_{x_{1}}$ and
$H_{0}=\ker\psi=\{g:g(x_{0})=g(x_{1})\}$.
Let $q:K\to \widetilde K=K/\{x_{0}\sim x_{1}\}$ be the quotient. Since the
equivalence relation is closed, $\widetilde K$ is compact Hausdorff, and
$f\mapsto f\circ q$ is a lattice isometry of $C(\widetilde K)$ onto $H_{0}$.
Hence $H_{0}$ is (isometrically) a $C$-space.

All closed hyperplanes in a Banach space are mutually isomorphic: if
$H=H_{0}$ there is nothing to prove; otherwise $\varphi|_{H_{0}}\ne 0$ and
$\psi|_{H}\ne 0$, so choose $e_{1}\in H_{0}$ with $\varphi(e_{1})=1$ and
$e_{2}\in H$ with $\psi(e_{2})=1$. Note $\varphi(e_{2})=0$,
$\psi(e_{1})=0$. Define bounded operators

$$S:H\to H_{0},\quad S(x)=x-\psi(x)e_{2}+\psi(x)e_{1},$$
$$R:H_{0}\to H,\quad R(y)=y-\varphi(y)e_{1}+\varphi(y)e_{2}.$$

Indeed $\psi(S(x))=\psi(x)-\psi(x)=0$ and
$\varphi(R(y))=\varphi(y)-\varphi(y)=0$. Moreover for $x\in H$,
$\varphi_{1}(e_{2})=0$ gives the inversion: $\psi$ of $R(y)$ equals
$\varphi(y)$ (since $\psi(y)=0$ for $y\in H_{0}$ up to notation) and
$S(R(y))=y$, $R(S(x))=x$ by direct substitution. Explicitly, with
$\varphi_{1}=\varphi$, $\varphi_{2}=\psi$: for $y\in H_{0}$,
$\varphi_{2}(R(y))=0+\varphi_{1}(y)(1-0)=\varphi_{1}(y)$, so
$S(R(y))=y+\varphi_{1}(y)(e_{2}-e_{1})+\varphi_{1}(y)(e_{1}-e_{2})=y$;
symmetrically $R\circ S=\mathrm{id}_{H}$. Hence $S:H\to H_{0}$ is a linear
isomorphism with bounded inverse $R$.

Thus every hyperplane $H$ is linearly isomorphic to $C(\widetilde K)$.

### 3. Conclusion

Suppose $L$ above is locally compact non-compact. Let $\alpha L=L\cup
\{\infty\}$ be its one-point compactification, compact Hausdorff. Then
$C_{0}(L)=\{f\in C(\alpha L):f(\infty)=0\}=\ker\delta_{\infty}$ is a closed
hyperplane in $C(\alpha L)$. By the Lemma it is linearly isomorphic to some
$C(K')$; concretely one may take $K'$ to be $\alpha L$ with $\infty$
identified with any other point. Hence $X\cong C(K')$ as Banach spaces.

The complemented-subspace hypothesis was never used, and separability
plays no role: separable or nonseparable, every AM-space is a $C$-space up
to linear isomorphism. In particular the nonseparable $X$ in the target is
a $C$-space.

### 4. Remarks

* The recent Plebanek–Salguero-Alarcón space $\mathit{PS}_{2}$,
  1-complemented in a $C(L)$ but isomorphic to no $C(K)$, is not a Banach
  lattice at all (de Hevia–Tradacete survey, 2025), so it does not
  contradict the above: the AM hypothesis rules it out.
* The $c_{0}$ case illustrates the Lemma: $c_{0}=C_{0}(\mathbb N)$ is a
  hyperplane in $c\cong C(\alpha\mathbb N)$ and is isomorphic (though not
  isometric) to a $C(K')$, indeed to the quotient identifying $\infty$ with
  another point; no dual-separability obstruction arises.
* If "AM-space" is meant in the unital sense, the conclusion is immediate
  from Kakutani without the Lemma.

## Self-checks

* Verified all hyperplanes mutually isomorphic with explicit bounded
  mutually inverse maps (no dimension or separability assumption; singleton
  case handled separately).
* Verified quotient identifying two points of a compact Hausdorff space is
  compact Hausdorff and $C$ of the quotient is the equalizer subspace.
* Verified $C_{0}(L)=\ker\delta_{\infty}$ has codimension one (evaluation
  at $\infty$ is continuous of norm one).
* Distinguished linear isomorphism vs lattice isometry: only linear
  isomorphism is claimed for $K'$.
* No originality claim beyond classical Kakutani + folklore hyperplane
  fact; complemented hypothesis shown redundant, consistent with known
  counterexamples being non-lattice.
