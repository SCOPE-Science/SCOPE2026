# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Vacuity diagnosis and scale-invariant repair for uniform Diophantine Lazutkin thresholds

## 1. What is proved here (and what is not)

This note proves exactly two things:

**(A) Vacuity theorem.** Under the literal absolute homogeneous reading of the
Diophantine class in the admitted target, the uniform horn is empty for every
large threshold, so the dichotomy can only be satisfied vacuously.

**(B) Repair lemma with explicit witnesses.** Under the scale-invariant relative
Diophantine definition standard in small-twist KAM theory, every shrinking
interval $(0,\eta]$ contains explicit admissible rotation numbers; an infinite
family $w_M=g/M$ ($g$ the golden-ratio conjugate) is proved to lie in the
relative class with an explicit constant.

The conditional closed-form $Q^\*$ majorant chain developed during target work
is described in Section 5 as an explicitly **conditional** framework (two
constants flagged as assumed), and is **not** part of the claimed theorem. No
uniform KAM existence theorem and no converse-KAM counterexample is claimed.

## 2. Vacuity theorem (absolute reading)

**Definition (absolute).** For $c>0$, $\tau\ge 0$,
$$D(c,\tau)=\{\omega\in(0,1]:|k\omega-l|\ge c/|k|^\tau\ \forall k\ge 1,\ l\in\mathbb Z\}.$$

**Theorem 1.** Every $\omega\in D(c,\tau)$ satisfies $\omega\ge c$. Hence for any
threshold $Q^\*>1/c$,
$$(0,1/Q^\*]\cap D(c,\tau)=\varnothing,$$
and the universal statement "every curve has a KAM caustic for every
$\omega\in D(c,\tau)$ with $\omega\le 1/Q^\*$" holds vacuously.

**Proof.** Take $k=1$, $l=0$ in the definition: $|\omega-0|=\omega\ge c/1^\tau=c$.
If $Q^\*>1/c$ then $1/Q^\*<c$, so no $\omega\le 1/Q^\*$ can satisfy
$\omega\ge c$. The universal quantification is over the empty set. ∎

**Remark.** For the concrete instance $c=0.01$, any $Q^\*>100$ — including the
computed conditional value $Q^\*\approx 5.77\times 10^{48}$ — empties the horn.
A proof that "discharges" the target by exhibiting such a $Q^\*$ under the
absolute reading would exercise no KAM construction at all. This note
deliberately does **not** take that vacuous route; it diagnoses it as a defect
in the problem wording and repairs the definition instead.

## 3. Repair lemma (relative / scale-invariant reading)

**Definition (relative).** For $0<c\le 1$, $\tau\ge 0$,
$$D_{\mathrm{rel}}(c,\tau)=\{\omega\in(0,1]:|k\omega-l|\ge c\,\omega/|k|^\tau\
\ \forall k\ge 1,\ l\in\mathbb Z\}.$$
Equivalently $|\omega-l/k|\ge c\,\omega/|k|^{\tau+1}$. For $l=0$ the condition is
$|\omega|\ge c\omega/k^\tau$, automatic for $c\le 1$, $k\ge 1$; the content lies
in $l\ge 1$, i.e.\ approximants near $0$. This scaling is the standard
small-twist adaptation: the twist (hence the effective Diophantine margin)
degenerates linearly with the action, so the admissible margin must scale with
$\omega$ itself.

**Theorem 2.** Let $g=(\sqrt5-1)/2$.
Let $0<c\le 1/2$ (in particular the concrete target-instance value $c=0.01$
qualifies). Then for every integer $M\ge 1$,
$$w_M:=g/M\in D_{\mathrm{rel}}(c,1).$$
Hence every interval $(0,\eta]$, $\eta>0$, contains admissible rotation numbers
(take $M> g/\eta$), and $\{w_M\}$ is an explicit infinite witness family
accumulating at $0$.

**Proof.** We use an elementary Liouville argument for $g$, avoiding any sharp
approximation constant. Let $f(x)=x^2+x-1$, so $f(g)=0$ with
$g=(\sqrt5-1)/2\approx 0.618$ and $g+1=\varphi=(1+\sqrt5)/2$.
For integers $k\ge 1$, $p\in\mathbb Z$, $f(p/k)=(p^2+pk-k^2)/k^2=N/k^2$ with
$N\in\mathbb Z$. Since the roots of $f$ are irrational, $N\ne 0$, hence
$|f(p/k)|\ge 1/k^2$. Factoring,
$$|f(p/k)|=|p/k-g|\cdot|p/k+g+1|,$$
so
$$|g-p/k|=\frac{|f(p/k)|}{|p/k+g+1|}\ge\frac{1}{k^2\,|p/k+g+1|}.$$
If $|p/k-g|\ge 1$ then $|g-p/k|\ge 1\ge 1/(2\varphi k^2)$ trivially (as
$2\varphi k^2\ge 1$). Otherwise $|p/k|\le g+1=\varphi$, so
$|p/k+g+1|\le\varphi+g+1=2\varphi$, giving in all cases
$$|g-p/k|\ge\frac{1}{2\varphi\,k^2},\qquad\text{i.e.}\qquad
|kg-p|\ge\frac{1}{2\varphi\,k}=\frac{g}{2k},$$
since $1/(2\varphi)=g/2\approx 0.309$ (using $g\varphi=1$).
Now fix $M\ge 1$, $w=g/M$, and integers $k\ge 1$, $l\in\mathbb Z$.
Put $p=Ml\in\mathbb Z$. Then
$$|kw-l|=\Bigl|\frac{kg}{M}-l\Bigr|=\frac{1}{M}\,|kg-Ml|
\ge \frac{1}{M}\cdot\frac{g}{2k}.$$
The required relative bound is $|kw-l|\ge c\,w/k=cg/(Mk)$. It suffices that
$g/2\ge cg$, i.e.\ $c\le 1/2$, which holds by hypothesis. The
case $kw-l=0$ cannot occur since $g$ is irrational. For $l=0$ the same
computation applies ($p=0$). Thus $w_M$ satisfies every constraint, so
$w_M\in D_{\mathrm{rel}}(c,1)$. Since $w_M\to 0$, each $(0,\eta]$ contains such
points. ∎

**Numerical corroboration (not part of the proof).**
`output/artifacts/verify_witness.py` checks the elementary bound and membership:
(i) $\min_{k\le 20000} k\,|kg-l|\ge g/2$;
(ii) zero violations of $|kw-l|\ge c\,w/k$ with $c=0.5$ over $M\le 200$,
$k\le 3000$; (iii) the vacuity inequality $1/Q^\*<c$ for the computed
conditional $Q^\*$. These runs corroborate but do not replace the proofs above.

## 4. Why this matters

1. **Blocks scope evasion.** Theorem 1 shows the admitted wording, read
literally, admits a degenerate "proof by empty horn." Publishing such a vacuous
resolution as a TARGET success would misrepresent the mathematics. The diagnosis
forces any honest attempt to amend the Diophantine class first.
2. **Supplies the corrected object.** Theorem 2 gives the minimal corrected
definition together with certified members — the missing starting point for any
future uniform-threshold program. Any subsequent KAM argument must target
$D_{\mathrm{rel}}$, where the horn is provably nonempty.
3. **Separates scales honestly.** The relative form makes explicit the
mechanism ($\gamma\sim c\omega$ twist margin vs.\ $\varepsilon\sim\omega^3$
perturbation) that any future quantitative $Q^\*$ must exploit.

## 5. Conditional framework (explicitly not claimed)

For orientation only: with curvature bounds
$\kappa\in[2\pi/(LK),2\pi K/L]$ from total curvature $2\pi$ plus ratio $K$,
$C=\int\kappa^{2/3}$ bounds, derivative majorants
$B_j=(j+1)!(1+N)^{j+1}$, and a Lazutkin remainder majorant
$M_0=200(1+B_5)^3\kappa_{\min}^{-8}(C_{\max}/C_{\min})^3(1+L)^2$, the formal KAM
reduction $\varepsilon=M_0\omega^3\le\delta_H(c\omega)^2$ with assumed universal
twist-KAM constant $\delta_H=10^{-8}$ and $\tau$-factor $(1+\tau)^{-4}$ yields
$Q^\*=1/\min(y_{\mathrm{geo}}/2,\ \delta_Hc^2/(4M_0(1+\tau)^4))$, evaluated in
`output/artifacts/compute_Qstar.py` ($5.77\times10^{48}$ for
$L=2\pi,K=2,N=10,c=0.01,\tau=1$). The prefactor $200$ and $\delta_H$ are
**assumed, not derived**; certifying them (plus the circle-to-caustic step)
remains open. This chain is recorded for reuse, not claimed as a theorem.

## References (qualitative, for context)

Lazutkin's normal form near the boundary; Douady and De Simoi–Kaloshin–Wei
uniform versions; Herman–Rüssmann–Moser quantitative twist-map KAM theorem;
Lazutkin/Mather invariant-circle-to-caustic correspondence. No explicit-constant
certification is drawn from these here; they motivate the conditional framework
only.
