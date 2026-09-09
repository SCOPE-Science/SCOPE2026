# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# S3-on-O2 Rokhlin boundary collapses positively: no pointwise-outer finite-dimensional non-absorbing example (corollary of Szabo)

## 1. Statement

**Lemma (verified corollary).** Let $G=S_3$ and $A=\mathcal O_2$.
Let $\delta\colon G\curvearrowright\mathcal O_2$ be the Szabo model action
(Notation below). Then:

1. Every pointwise outer action $\alpha\colon S_3\curvearrowright\mathcal O_2$
   has Rokhlin dimension $\dim_{\mathrm{Rok}}(\alpha)\le 1$
   (hence in particular $\le 2$, finite, with no commuting-tower hypothesis).
2. For every action $\alpha\colon S_3\curvearrowright A$ on a unital Kirchberg
   algebra, $\alpha\otimes\delta$ is strongly cocycle conjugate to $\delta$.
   If $\alpha$ is pointwise outer, $\alpha\otimes\mathrm{id}_{\mathcal O_2}$
   is strongly cocycle conjugate to $\delta$ (actions on
   $A\otimes\mathcal O_2\cong\mathcal O_2$ identified via Kirchberg–Phillips).
3. In particular, there is **no** pointwise-outer (for finite $G$, equivalently
   outer) $S_3$-action on $\mathcal O_2$ with finite Rokhlin dimension that
   fails to absorb $\delta$ in the stabilized sense above. The conjectured
   target counterexample does not exist relative to Szabo's model $\delta$.
   Any hypothetical non-absorption example must lie outside the
   pointwise-outer class.

This is **fallback (c)** of the admitted plan (subclass absorption lemma),
pre-approved as independently valuable. It decides the assigned boundary
instance in the positive direction instead of by counterexample.

## 2. Definitions and model (all standard, cited)

- $\mathcal O_2$: Cuntz algebra on two generators; unital, separable, simple,
  purely infinite, nuclear — i.e. a unital Kirchberg algebra.
- Pointwise outer: $\alpha_g$ is an outer automorphism for every $g\ne 1$.
  For finite $G$ this coincides with outerness of the action.
- Strong cocycle conjugacy ($\simeq_{\mathrm{scc}}$): conjugacy up to
  $\alpha$-cocycle perturbation with approximately inner correction;
  Szabo's classification equivalence (see Szabo arXiv:1610.05939 §1).
- Model $\delta$: fix a unitary representation
  $v\colon G\to\mathcal U(\mathcal O_2)$ inducing an embedding
  $C^*(G)\hookrightarrow\mathcal O_2$, and put
  $\delta=\bigotimes_{\mathbb N}\mathrm{Ad}(v)$ on
  $\bigotimes_{\mathbb N}\mathcal O_2\cong\mathcal O_2$
  (Szabo Example “$\gamma$/$\delta$”, Introduction; §5, Example 5.6).
  Up to $\simeq_{\mathrm{scc}}$, $\delta$ is independent of the choice of $v$
  (Theorem A / Cor. 3.8 analogue for $\mathcal O_2$).
- Rokhlin dimension $\dim_{\mathrm{Rok}}$: Hirshberg–Winter–Zacharias /
  Gardella–Szabo tower formulation; commuting towers NOT assumed here.

## 3. Proof (by citation + hypothesis check; no new analysis claimed)

**Source theorems** (G. Szabo, arXiv:1610.05939, published
Comm. Math. Phys. 361 (2018), 1115–1154; statements verified against the
full text/HTML, not from memory):

- **Theorem C (Thm 5.5).** For every action $\alpha\colon G\curvearrowright A$
  of a countable discrete amenable $G$ on a unital Kirchberg algebra,
  $\alpha\otimes\delta\simeq_{\mathrm{scc}}\delta$.
  If $\alpha$ is pointwise outer, $\alpha\otimes\mathrm{id}_{\mathcal O_2}
  \simeq_{\mathrm{scc}}\delta$.
- **§7.** Every pointwise outer action of an amenable **residually finite**
  group on a Kirchberg algebra has Rokhlin dimension $\le 1$.

**Hypothesis verification for $S_3$ / $\mathcal O_2$:**
- $S_3$ is finite of order $6$ with presentation
  $\langle r,s\mid r^3=s^2=1,\ srs=r^{-1}\rangle$; replay-verified in
  `output/artifacts/verify_s3_inputs.py` (permutation model, relation check,
  generation, VERIFY_OK).
- Finite $\Rightarrow$ countable discrete amenable (Følner set $F=G$) and
  residually finite (regular representation separates points); both checked
  in the same script. Hence $S_3$ meets the hypotheses of Theorem C and §7.
- $\mathcal O_2$ is a unital Kirchberg algebra (standard; e.g. Kirchberg–Phillips;
  used identically in Szabo's statements for $\mathcal O_2$).
- $C^*(S_3)$ data used by the model construction: irreps of degrees
  $1,1,2$, $\sum d_i^2=6=\lvert S_3\rvert$; exact, hence embeds in
  $\mathcal O_2$ (Kirchberg). Degrees checked in the script.

Applying Theorem C and §7 under these verified hypotheses yields (1)–(2)
directly; (3) is the contrapositive for the target alternative.

## 4. What is proved vs computed vs conjectured

- **Proved (as corollary):** the Lemma above, conditional on the cited
  Szabo theorems. The deduction itself is elementary hypothesis-checking.
- **Computed evidence:** `verify_s3_inputs.py` (stdlib only) replays the
  finite-group inputs: order $6$, dihedral relation, generation, amenability,
  residual finiteness, $C^*(S_3)$ degree data. All VERIFY_OK.
- **Not computed / not claimed:** no new equivariant $K$-theory mismatch is
  claimed (none exists in this subclass by (2); moreover $K_*(\mathcal O_2)=0$
  makes fixed-point $K_*$ a weak invariant here). No explicit Rokhlin towers
  are exhibited; the bound comes from §7, not from an ansatz.
- **Conjecture / open:** the original “finite-dim non-absorbing” alternative
  in full generality (non-pointwise-outer actions, other models) is untouched.

## 5. Identification caveat (uncertainty, not hidden)

The Lemma is relative to **Szabo's model $\delta$**. Its identification with
the topic's phrase “Rokhlin model $S_3$-action” is: $\delta$ is the
finite-group equivariant $\mathcal O_2$-absorbing model (Szabo §5 and
[76] §5: it reproduces the Izumi/Goldstein–Izumi finite-group models up to
$\simeq_{\mathrm{scc}}$). A from-scratch re-proof of that identification, or
of Szabo's Theorems C/§7, is explicitly **not** attempted and is cited as
literature. If “Rokhlin model” is meant in a narrower sense (e.g. a specific
Izumi Rokhlin-property representative), the Lemma should be read as stated
for $\delta$, with the transfer to that representative via the cited
uniqueness results.

## 6. Why this matters

The admitted target asked whether dropping commuting towers opens a
finite-dimensional non-absorbing $S_3$-on-$\mathcal O_2$ example.
The Lemma shows the answer is **no** inside the natural (pointwise-outer)
class: finite Rokhlin dimension is automatic ($\le 1$) there and absorption
of $\delta$ holds. Classification hypotheses for nonabelian finite groups on
Kirchberg algebras therefore cannot use such a counterexample; any
separation must come from outside pointwise-outer actions. This is exactly
the pre-registered fallback value: an auditable boundary update reusable in
classification.

## References (checked live)

- G. Szabo, *Equivariant Kirchberg–Phillips-type absorption for amenable group
  actions*, arXiv:1610.05939 (v3); Comm. Math. Phys. 361 (2018).
  Theorems B/C/D/E/F, §5 (model $\delta$, Ex. 5.6), §7 (Rokhlin dim $\le1$).
- J. Szabo, *Rokhlin dimension: absorption of model actions*, arXiv:1804.04411
  (commuting-tower regime; shows why the noncommuting instance was open).
- Hirshberg–Phillips, arXiv:1410.6581 (commuting-tower obstructions only).
- Gardella, arXiv:1407.1277 (commuting vs noncommuting separation).
- Girón Pacheco–Szabo, arXiv:2608.09517 (anomalous Rokhlin $G$-kernels;
  distinct setting, no $S_3$-on-$\mathcal O_2$ alternative recorded).
