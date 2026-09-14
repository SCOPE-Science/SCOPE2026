# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Weight–monodromy purity for the exceptional G₂ central functor

## Self-contained proof (target claim)

**Theorem (target).** Let $F/\mathbf Q_p$ be finite with residue field
$k=\mathbf F_q$, $q$ a power of $p\ne\ell$. Let $G/F$ be split adjoint of
type $G_2$, $I\subset G(F)$ Iwahori. For every finite-dimensional
$\overline{\mathbf Q}_\ell$-representation $V$ of
${}^LG^\circ\simeq G_2$, let

$$Z^{IW}(V)=R\Psi^{IW}(\mathrm{Sat}(V))$$

be the (normalized, perverse t-exact) nearby-cycles image of the geometric
Satake sheaf on the special-fiber Iwahori Hecke stack. Then the weight
filtration $\mathrm{Fil}^W_\bullet$ on $Z^{IW}(V)$ equals the monodromy
filtration $\mathrm{Fil}^M_\bullet$ centered at weight $0$.

### 1. Normalizations and definitions

(1a) *Coefficients.* Work with $\overline{\mathbf Q}_\ell$-Weil perverse
sheaves, $\ell\ne p$. "Pure of weight $w$" is in Deligne's sense (Weil II).
Tate twist $(1)$ has weight $-2$; $N:\mathrm{Gr}^M_k\to\mathrm{Gr}^M_{k-2}(-1)$.

(1b) *Monodromy filtration centered at $0$.* For a perverse sheaf $P$ with
nilpotent $N:P\to P(-1)$ (log of tame monodromy), $\mathrm{Fil}^M_\bullet$ is
the unique finite filtration with $N(M_k)\subset M_{k-2}$ and
$N^r:\mathrm{Gr}^M_r \xrightarrow{\sim} \mathrm{Gr}^M_{-r}(-r)$ for all
$r\ge 0$ (Deligne). Uniqueness implies strict functoriality.

(1c) *Weight filtration.* $\mathrm{Fil}^W_\bullet$ is Deligne's weight
filtration on mixed perverse sheaves over the finite field $k$; strictly
functorial; $\mathrm{Gr}^W_k$ is pure of weight $k$ when defined.

(1d) *The functor.* Fix a henselian trait $S=\mathrm{Spec}\,R$ with closed
point $s=\mathrm{Spec}\,k$ ($k$ finite, $\mathrm{char}\ne\ell$) and generic
point $\eta$; e.g. the henselization of $\mathbf A^1_{\mathcal O_F}$ at the
origin. Let $\mathfrak X\to S$ be Gaitsgory's central degeneration:
$\mathfrak X_\eta\simeq \mathrm{Gr}_G$ (affine Grassmannian) and
$\mathfrak X_s\simeq \mathrm{Fl}_{I}$ (affine flag variety), with the Iwahori
Hecke stack as quotient; the family is $I$-equivariant of relative dimension
one. Define $R\Psi^{IW}= {}^{p}\!R\Psi[-1]^{\mathrm{un}}$ with the standard
normalization making it perverse t-exact (Gaitsgory; Arkhipov–Bezrukavnikov).
Set $Z^{IW}(V)=R\Psi^{IW}(\mathrm{Sat}(V))$, a perverse sheaf on the
special-fiber Iwahori Hecke stack with nilpotent monodromy $N$.

### 2. Input sheaves are pure of weight 0

**Lemma 1 (Satake purity; $G_2$-normalization).** For every $V$,
$\mathrm{Sat}(V)$ is $L^+G$-equivariant perverse on $\mathrm{Gr}_{G,\bar\eta}$,
pure of weight $0$.

*Proof.* Geometric Satake in mixed characteristic (Zhu; Richarz) identifies
$\mathrm{Rep}({}^LG^\circ)$ with $L^+G$-equivariant perverse Weil sheaves via
normalized intersection cohomology:
$$\mathrm{Sat}(V_\mu) = \mathrm{IC}_\mu
  = j_{!*}(\overline{\mathbf Q}_\ell[\dim][(\dim)/2]),\qquad
  \dim = \dim\mathrm{Gr}_{\le\mu}=\langle 2\rho,\mu\rangle.$$
Purity of $\mathrm{IC}$ of a Schubert variety over a finite field is Weil II
/ BBD: the normalized complex is pure of weight $0$ provided the Tate twist
is integral. For $G_2$ this is automatic: $G$ adjoint has coweight lattice
equal to the coroot lattice $Q^\vee$, and
$\langle\rho,\alpha_i^\vee\rangle=1$ gives
$\langle 2\rho, m\alpha_1^\vee+n\alpha_2^\vee\rangle = 2m+2n\in 2\mathbf Z$.
Hence every $\langle 2\rho,\mu\rangle$ is even, the half-twist is an integral
Tate twist, and $\mathrm{IC}_\mu$ is pure of weight $0$ with no sign
ambiguity. Semisimplicity of $\mathrm{Rep}(G_2)$ extends this to all $V$.
The $G_2$ root datum ($\det A = 1$, $|W|=12$, $\dim G_2=14$, dual dimensions
$7$ and $14$) is verified in `output/artifacts/g2_combinatorics.py`. ∎

*Remark.* $G_2$ has trivial center, so $G$ is both adjoint and simply
connected; $\mathrm{Gr}_G$ is connected and there is no component-group
subtlety. $G_2$ has no nonzero minuscule coweight, so every nontrivial
$\mathrm{Gr}_{\le\mu}$ is singular — the proof cannot avoid singular nearby
cycles, which is why Gabber's theorem (not a smooth computation) is needed.

### 3. Reduction to finite type and unipotent monodromy

**Lemma 2 (finite-type support).** Fix $V$. Then $\mathrm{Sat}(V)$ is supported
on a finite union of $L^+G$-orbits $\mathrm{Gr}_{\le\mu}$, and the degeneration
restricts to a finite-type family $\mathfrak X_{\le\mu}\to S$. So Gabber's
finite-type hypothesis applies.

*Proof.* $V$ has finitely many highest weights; Satake sheaves have
Schubert-stratified finite support. ∎

**Lemma 3 (unipotent monodromy).** The inertia action on $Z^{IW}(V)$ is
unipotent; i.e. $R\Psi = R\Psi^{\mathrm{un}}$ on Satake inputs.

*Proof.* This is Gaitsgory's theorem on the central degeneration: the family
is $\mathbf G_m$-equivariant (loop rotation), and $L^+G$-equivariant Satake
sheaves are $\mathbf G_m$-monodromic, forcing the tame monodromy to be
unipotent (Gaitsgory, Invent. 2001, §1–2; see also Arkhipov–Bezrukavnikov on
perversity and $I$-equivariance of the output). Hence the logarithm $N$ is
nilpotent and the unipotent nearby cycles capture everything. ∎

### 4. Gabber's theorem gives the equality

**Theorem (Gabber; see Illusie, Astérisque 223, exposé of Gabber's
monodromy theorem).** Let $\mathfrak X/S$ be separated of finite type over a
henselian trait with finite residue field of characteristic $\ne\ell$.
Let $\mathcal F$ on $\mathfrak X_\eta$ be perverse, pure of weight $w$, with
unipotent monodromy. Then on $\Psi^{\mathrm{un}}(\mathcal F)$ (normalized to be
perverse), the weight filtration coincides with the monodromy filtration
shifted by $w$: $\mathrm{Gr}^M_r$ is pure of weight $w+r$.

Apply with $w=0$: by Lemmas 1–3, $\mathcal F=\mathrm{Sat}(V)$ is pure of
weight $0$ with unipotent monodromy on a finite-type family. Hence
$\mathrm{Gr}^M_r(Z^{IW}(V))$ is pure of weight $r$, i.e. the monodromy
filtration centered at $0$ is a weight filtration. By uniqueness of the
weight filtration,
$$\mathrm{Fil}^W_k Z^{IW}(V) = \mathrm{Fil}^M_k Z^{IW}(V)\quad\forall k,$$
with both graded pieces pure of weight $k$. Functoriality/strictness of both
filtrations extends the irreducible case to arbitrary finite-dimensional $V$
(direct sums and subquotients). This is exactly the target claim. ∎

### 5. What was checked computationally

`output/artifacts/g2_combinatorics.py` (all assertions pass) verifies:
- $\det A(G_2)=1$ (adjoint = simply connected);
- $|W(G_2)|=12$ by explicit reflection-group computation;
- $\langle 2\rho,\mu\rangle\in 2\mathbf Z$ on the coroot lattice (integral
  normalization, Lemma 1);
- Weyl dimension formula gives dual-$G_2$ dimensions $7$ ($L(\omega_1)$) and
  $14$ ($L(\omega_2)$, adjoint), confirming the Satake parameterization;
- an explicit Deligne monodromy filtration (Jordan type $3+1$,
  $\dim\mathrm{Gr}^M=(1,2,1)$, $N^2:\mathrm{Gr}^M_2\cong\mathrm{Gr}^M_{-2}$),
  illustrating the characterizing property used in §4.

### 6. References (results used, not reproved)

- P. Deligne, *Weil II* (1980): weights, monodromy filtration, strictness.
- O. Gabber / L. Illusie, *Autour du théorème de monodromie locale*,
  Astérisque 223 (1994): weight = monodromy for unipotent nearby cycles of a
  pure perverse sheaf.
- D. Gaitsgory, *Construction of central elements via nearby cycles*,
  Invent. Math. 144 (2001): central degeneration, perversity,
  $\mathbf G_m$-equivariance ⇒ unipotent monodromy.
- S. Arkhipov–R. Bezrukavnikov: perversity/$I$-equivariance refinements.
- Mirković–Vilonen; X. Zhu (*Affine Grassmannians and geometric Satake in
  mixed characteristic*, Ann. Math. 2017); T. Richarz: Satake + IC purity.

### 7. Limitations and scope

- The proof is a specialization of general theorems (Gabber, Weil II,
  Gaitsgory, mixed-characteristic Satake) to $G_2$; it verifies all
  hypotheses in the $G_2$ case but does not give new proofs of those inputs.
- Requires $\ell\ne p$ and finite residue field (used for weights and tame
  nearby cycles); says nothing about $\ell=p$.
- The computation supports normalizations/combinatorics only; the sheaf
  identity is deductive, not machine-checked.
