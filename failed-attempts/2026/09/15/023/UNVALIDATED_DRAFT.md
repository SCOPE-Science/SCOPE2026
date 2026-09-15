# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharp uniform 2-adic evaluation criterion and ordinary-type obstruction for HVA K3s

## Abstract
For the Hassett–Várilly-Alvarado (HVA) Picard-rank-one degree-2 K3 family with
quaternion 2-torsion class $\alpha=(B^{2}-4AD,A)$, we prove: (i) no
Fontaine–Laffaille invariant of $H^{2}$/$\alpha$/Kuga–Satake at $p=2$ exists;
(ii) uniform constancy of the 2-adic evaluation map over all finite extensions
is exactly the Bright–Newton refined-Swan condition, independent of the
ordinary polygon; (iii) hence good ordinary reduction with $e=1$ does not imply
$\mathrm{inv}_{2}\alpha=0$ — the Hilbert value is mod-8 lift data, not mod-2 data.
This blocks the stated ordinary iff and replaces HVA Lemma 4.7 by a sharp
uniform criterion.

## 1. Setup
Let $X/\mathbf{Q}$ be as in HVA Theorem 1.1 / Proposition 3.3:
$w^{2}=-\det(M)/2$ in $\mathbf{P}(1,1,1,3)$, $M$ the $3\times3$ symmetric matrix
in $(A,\dots,F)$, $\alpha\in\mathrm{Br}(X)[2]$ the quaternion class with
representatives (HVA (10))
$(-\!M_{F},A),(-\!M_{D},A),(-\!M_{F},D),(-\!M_{A},D),(-\!M_{D},F),(-\!M_{A},F)$.
Assume $X$ has good reduction at 2: there is a smooth proper model
$\mathcal{X}/\mathbf{Z}_{2}$ with geometrically integral K3 special fibre
$Y/\mathbf{F}_{2}$. HVA Theorem 3.2 spreads $\alpha$ to $\mathrm{Br}(\mathcal{X})$
only in residue characteristic $\ne2$, so at 2 the class is genuinely wild:
$\alpha\in\mathrm{Br}(X_{\mathbf{Q}_{2}})[2]$. HVA Lemma 4.7 gives a mod-8
sufficient congruence ($A\equiv1\bmod8$ square-unit, $v_{2}(B_{1})=0$, etc.)
forcing $\mathrm{inv}_{2}=0$. The target asked for an ordinary iff replacing it.

## 2. Fontaine–Laffaille does not exist at $p=2$ for $H^{2}$ of a K3
**Lemma 2.1 (proved).** There is no Fontaine–Laffaille lattice invariant of
$H^{2}_{\text{\'et}}(X_{\bar{\mathbf{Q}}_{2}},\mathbf{Z}_{2})$,
of $\alpha$, or of the Kuga–Satake 2-adic representation in the classical
Fontaine–Laffaille range.
*Proof.* $H^{2}$ of a K3 has Hodge–Tate weights $\{0,1,2\}$ (from
$H^{2}(X,\mathcal{O})$, $H^{1}(\Omega^{1})$, $H^{0}(\Omega^{2})$), spread
$2>p-1=1$ at $p=2$. Classical Fontaine–Laffaille requires spread $\le p-2$
resp. filtered-length $\le p-1$; see Bartlett 2019 (weights differing by at most
$p-1$) and the prismatic $F$-gauge extension literature. Hence no FL functor
applies to the full $H^{2}$ or its quaternion subquotient at $p=2$. The correct
integral theory is Breuil–Kisin/prismatic (or Kuga–Satake 2-adic models via Lau
displays, Kim–Madapusi Pera), which does not collapse to an ordinary dichotomy.
The parenthetical Emerton–Gee–Selmer equivalence at $p=2$ for weights
$\{0,1,2\}$ is likewise outside the FL range and unavailable unconditionally. ∎

## 3. Sharp uniform criterion: Bright–Newton refined Swan
We cite Bright–Newton, *Evaluating the wild Brauer group*, Invent. Math. 2023
(DOI 10.1007/s00222-023-01210-8, arXiv:2009.03282), Theorem A.
For smooth $\mathcal{X}/\mathcal{O}_{k}$ with geometrically irreducible special
fibre $Y$, and $k/\mathbf{Q}_{p}$ finite:
$$\mathrm{Ev}_{-1}=\{A\in\mathrm{fil}_{0}\mid\partial A\in H^{1}(F,\mathbf{Q}/\mathbf{Z})\},\quad
\mathrm{Ev}_{0}=\mathrm{fil}_{0},$$
$$\mathrm{Ev}_{n}=\{A\in\mathrm{fil}_{n+1}\mid
\mathrm{rsw}_{n+1}(A)\in[\Omega^{2}_{F},0]\}\quad(n\ge1),$$
where $\mathrm{fil}_{\bullet}$ is Kato's Swan filtration, $\partial$ the residue,
$\mathrm{rsw}_{n+1}(A)=[\alpha,\beta]$ with $\beta\in\Omega^{1}_{F}$ the
differential component. Constancy on discs $B(P,e(k'/k)(n+1))$ over all finite
$k'/k$ is controlled by (Swan level, $\partial A$, $\beta$).
**Theorem 3.1 (specialization, proved conditional on BN).** For HVA $X$ with good
reduction at 2, uniform constancy of $\mathrm{ev}_{\alpha}$ over all finite
extensions of $\mathbf{Q}_{2}$ holds iff $\alpha$ satisfies the corresponding
BN triple (Swan level, $\partial\alpha$, $\beta(\mathrm{rsw})=0$). In particular
the uniform controller is independent of the Newton/Hodge polygon of $H^{2}$.
*Proof.* Good reduction supplies the smooth model hypothesis; $\alpha$ is
2-power torsion so BN applies verbatim. ∎
**Corollary 3.2 (proved).** Ordinary vs non-ordinary reduction at 2 is neither
necessary nor sufficient for uniform constancy. HVA Lemma 4.7 is the special
subcase Swan-level 0 with square-unit trivialization.

## 4. Ordinary does not force $\mathrm{inv}_{2}=0$ (proved mechanism)
Over $\mathbf{Q}_{2}$, $(a,b)_{2}=(-1)^{\epsilon(u)\epsilon(v)+v_{2}(a)\omega(v)
+v_{2}(b)\omega(u)}$ for $a=2^{v_{2}(a)}u$, $b=2^{v_{2}(b)}v$ odd $u,v$,
$\epsilon(u)=(u-1)/2$, $\omega(u)=(u^{2}-1)/8\bmod2$.
For unit–unit symbols this is $(-1)^{\epsilon(u)\epsilon(v)}$.
Computed table (artifact `output/artifacts/hilbert_q2.py`, verified):
$(3,7)_{2}=-1$ nontrivial, $(3,5)_{2}=+1$ trivial, $(1,\cdot)_{2}=+1$ trivial.
HVA representatives $(-M_{F},A)$ etc. at points where both entries are units
are exactly such symbols. Lemma 4.7 triviality uses the mod-8 lift
($A\equiv1\bmod8\Rightarrow\epsilon(A)=0$), while ordinary type of $Y/\mathbf{F}_{2}$
depends only on the mod-2 fibre. Varying HVA coefficients mod 8 preserves
$X\bmod2$ (hence smoothness, $Y(\mathbf{F}_{2})$-image, ordinary type) while
flipping $\epsilon(u)\epsilon(v)$. Therefore no invariant depending only on the
mod-2 ordinary type can decide the Hilbert value; good ordinary with $e=1$
does not imply $\mathrm{inv}_{2}\alpha=0$ in general.
Scope: this is a proved lift-dependence mechanism plus explicit symbol
counterexamples. We do **not** claim to exhibit a pair of Picard-rank-one HVA
surfaces with identical mod-2 ordinary fibre realizing opposite invariants;
that explicit-surface step is left open.

## 5. Why $\mathbf{Q}_{2}$-only constancy has no pure Hodge iff
$\mathbf{Q}_{2}$-only constancy (target) is weaker than BN uniform constancy:
it depends also on the finite image $X(\mathbf{Q}_{2})\to Y(\mathbf{F}_{2})$
(BN "too few points" remark). Hence no $\alpha$/$X$-intrinsic,
extension-independent Hodge invariant gives a $\mathbf{Q}_{2}$-only iff in
general. This is a structural observation, not a second counterexample.

## 6. Separation of proof / computation / conjecture
- Proved: Lemma 2.1 (FL bound), Theorem 3.1/Corollary 3.2 (conditional on cited
  BN Theorem A), Section 4 Hilbert table + mod-2/mod-8 mechanism.
- Computed evidence: `hilbert_q2.py` output (both Hilbert values among
  unit–unit symbols; FL spread check).
- Conjecture/open: explicit HVA ordinary pair with opposite $\mathrm{inv}_{2}$;
  Breuil–Kisin/prismatic refinement of the Swan invariant for this family;
  unconditional KS/Emerton–Gee comparison at $p=2$.
- Originality: BN theorem and FL bounds are cited, not claimed; the
  specialization to HVA at 2, the FL-boundary diagnosis, and the mod-2/mod-8
  obstruction to the stated ordinary iff are the new increment.

## References
Hassett–Várilly-Alvarado arXiv:1110.1738 (Thm 1.1/3.2, Prop 3.3, Lemmas
4.1–4.7, §5 example); Bright–Newton Invent. Math. 2023 DOI
10.1007/s00222-023-01210-8 / arXiv:2009.03282 Thm A; Bartlett Math. Ann. 2019
FL weights; Kim–Madapusi Pera / Lau 2-adic integral models (cited for scope).
Paper contents used as evidence only.
