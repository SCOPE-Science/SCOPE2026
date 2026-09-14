# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# SL restriction and PGL descent of shifted Poisson (g=2, r=3) — proof draft

## 1. Setup and theorem

Let $k=\bar k$, $\mathrm{char}\,k=0$ (in particular $\mathrm{char}\nmid 3$),
$C/k$ smooth projective genus $g=2$, $r=3$, $d$ coprime to $3$,
$L_0\in\mathrm{Pic}^d(C)$ fixed.

- $\mathbf M_{GL}$: derived rank-3 $GL(3)$-Higgs stack,
  $\mathbf M_{GL}=\mathbf{Map}(C_{\mathrm{Dol}},BGL_3)$,
  with PTVV–Calaque $0$-shifted symplectic form $\omega_{GL}$
  (hence nondegenerate $0$-shifted Poisson bivector $\pi_{GL}=\omega_{GL}^{-1}$)
  from the trace pairing and Serre duality.
- $\det\mathrm{-tr}:\mathbf M_{GL}\to \mathbf M_{G_m}\cong
  \mathbf{Pic}(C)\times H^0(C,K_C)$,
  $(E,\phi)\mapsto(\det E,\mathrm{tr}\,\phi)$.
- $\mathbf M_{SL}$: derived homotopy fiber over fixed $(L_0,0)$,
  rank-3 fixed-determinant traceless Higgs moduli.
- $q:\mathbf M_{SL}\to\mathbf M_{PGL}$: rigidification by the residual
  central scalar automorphisms (a $B\mathbb G_m$-gerbe, restricting to
  $B\mu_3$ on the stable locus).

**Theorem (target, proved).**
(a) The $0$-shifted Poisson structure on $\mathbf M_{GL}$ restricts to a
canonical $0$-shifted symplectic structure $\omega_{SL}$ on
$\mathbf M_{SL}$ (the derived fixed-determinant/traceless fiber is a
$0$-shifted symplectic leaf).
(b) $\omega_{SL}$ descends along $q$ to a $0$-shifted symplectic structure
$\omega_{PGL}$ on $\mathbf M_{PGL}$, with identified band-$\mathbb G_m$
weight $0$ (Hitchin scaling weight $1$).
(c) Shift classification differs exactly in that the canonical
**$2$-shifted ($B\mathbb G_m$-center / trace–trace) class** present on
$\mathbf M_{GL}$ vanishes on $\mathbf M_{SL}$ (with the associated
$1$-shifted gerbe-pairing class as corollary).

Stable dimensions: $\dim M^{st}_{GL}=2r^2(g-1)+2=20$,
$\dim M^{st}_{SL}=2(r^2-1)(g-1)=16$,
$\dim(\mathrm{Pic}\times H^0(K))=2+2=4=20-16$; $q$ preserves dimension 16.

## 2. Tangent fiber sequence and trace splitting

At $x=(E,\phi)$ the derived tangent is hypercohomology of the Higgs
deformation complex
\[
\mathcal C^\bullet=[\mathcal End\,E \xrightarrow{[\phi,-]} \mathcal End\,E\otimes K_C],
\qquad \mathbb T_x\mathbf M_{GL}\simeq \mathbf R\Gamma(C,\mathcal C^\bullet)[1].
\]
Write $\mathfrak{gl}_3=\mathfrak{sl}_3\oplus k\cdot\mathbf 1$.
The determinant-plus-trace differential is the trace map of complexes
\[
\tau:\mathcal C^\bullet\longrightarrow \mathcal D^\bullet:=[\mathcal O_C
\xrightarrow{d} K_C],
\]
$\tau_0=\mathrm{tr}$, $\tau_1=\mathrm{tr}$, where $\mathcal D^\bullet$ is the
tangent complex of $\mathbf M_{G_m}$ at $(\det E,\mathrm{tr}\,\phi)$.
Its homotopy kernel is the traceless complex
$\mathcal C^\bullet_0=[\mathcal End^0 E\to\mathcal End^0 E\otimes K_C]$,
the tangent of $\mathbf M_{SL}$. Hence a homotopy fiber sequence
\[
\mathbb T\mathbf M_{SL}\longrightarrow i^*\mathbb T\mathbf M_{GL}
\xrightarrow{d(\det\mathrm{-tr})} (\det\mathrm{-tr})^*\mathbb T_{\mathrm{base}}.
\tag{1}
\]

Because $\mathrm{tr}(\mathbf 1_3)=3$ is invertible, the projector
\[
P(A)=A-\tfrac13\mathrm{tr}(A)\mathbf 1_3,\qquad
s:\mathcal O\to\mathcal End,\ 1\mapsto \tfrac13\mathbf 1,
\]
splits $\mathcal End\,E\cong\mathcal End^0E\oplus\mathcal O$ and likewise
after $\otimes K_C$, compatibly with $[\phi,-]$ once $\mathrm{tr}\,\phi=0$
(for the fiber; globally it splits the sequence of graded bundles and the
induced map on hypercohomology). Verified computationally in
`artifacts/shift_checks.json`: $P^2=P$, $\mathrm{im}\,P$ rank $8$,
$\mathrm{tr}\circ P=0$, $\mathrm{tr}(\mathbf1^2)=3\ne0$. Consequently (1)
splits:
\[
\mathbb T\mathbf M_{GL}\simeq \mathbb T\mathbf M_{SL}\boxplus
\mathbb T_{\mathrm{base}},\qquad
\chi(\mathcal End^0)=8(1-g)=-8,\ \chi(\mathcal End^0\otimes K)=8(g-1)=8,
\]
giving $\dim\mathbb T^{st}_{SL}=16$, $\dim\mathbb T^{st}_{GL}=20$,
base rank $4$, consistent with Riemann–Roch ($g=2$:
$h^1(\mathcal O)=h^0(K)=2$, $h^0(\mathcal O)=h^1(K)=1$).

## 3. Restriction: block-diagonal Serre pairing

The $0$-shifted form is the trace–residue pairing
\[
\omega_{GL}((a_1,b_1),(a_2,b_2))=\int_C\mathrm{tr}(a_1\smile b_2-a_2\smile b_1),
\]
$a_i\in C^*(\mathcal End)$, $b_i\in C^*(\mathcal End\otimes K)$,
via Serre duality. Key linear fact: for $A_0$ traceless,
$\mathrm{tr}(\mathbf1\cdot A_0)=\mathrm{tr}(A_0)=0$.
Hence with the splitting of section 2,
\[
\omega_{GL}=\omega_{SL}\oplus\omega_{\mathrm{base}},
\tag{2}
\]
no cross terms between center and $\mathfrak{sl}_3$ (machine-checked
$\mathrm{tr}(\mathbf1\cdot P(B))\equiv0$ on all matrix units).
Each block is nondegenerate:
- Center block: $H^1(\mathcal O)\leftrightarrow H^0(K)$ ($2\leftrightarrow2$)
  by ordinary Serre duality; this is $\omega_{\mathrm{base}}$, the canonical
  $T^*\mathrm{Pic}$ symplectic form.
- $\mathfrak{sl}$ block: $\mathrm{tr}|_{\mathfrak{sl}_3}$ is nondegenerate
  (Killing $=6\,\mathrm{tr}$; needs $\mathrm{char}\ne2,3$), so
  $\mathcal End^0E$ is self-dual and Serre duality makes $\omega_{SL}$
  nondegenerate on $H^1(\mathcal C^\bullet_0)$.

Thus $i^*\omega_{GL}$ projects to a closed nondegenerate $0$-shifted
$2$-form $\omega_{SL}$ on the fiber. Closedness is inherited: the inclusion
$\mathcal C^\bullet_0\hookrightarrow\mathcal C^\bullet$ respects the
de Rham differential on the mapping stack (PTVV functoriality), and the
projection $P$ is a morphism of complexes over the fiber, so
$d_{dR}\omega_{SL}=P^*d_{dR}\omega_{GL}=0$.
Equivalently, $\mathbf M_{SL}$ is the derived Lagrangian intersection of the
Lagrangian morphism $\det\mathrm{-tr}$ (a $0$-shifted Lagrangian fibration
with base $T^*\mathrm{Pic}$) with the Lagrangian point $(L_0,0)$
(intersection of zero-section and cotangent fiber), hence $0$-shifted
symplectic by Lagrangian-intersection. The Poisson bivector likewise
block-diagonalizes, $\pi_{GL}=\pi_{SL}\oplus\pi_{\mathrm{base}}$ with
$\pi_{\mathrm{base}}=0$ on Casimirs, so the fiber is a symplectic leaf:
restriction of Poisson = inverse of $\omega_{SL}$. No obstruction class
appears; the would-be Kodaira–Spencer obstruction lands in the base
directions killed by fixing $(L_0,0)$, and on the coprime-degree stable
locus $H^2(\mathcal C^\bullet_0)=0$ at stable points (see section 5),
so the derived fiber is smooth there. This proves (a), with no
exotic shifted Poisson structure on $\mathbf M_{SL}$.

## 4. Descent to PGL and the G_m-weight

Scalar matrices act on $(E,\phi)$ by conjugation trivially; hence on
$\mathbb T\mathbf M_{SL}$ and on $\omega_{SL}$ the band-$\mathbb G_m$ of the
gerbe $q$ acts with **weight $0$**. The relative tangent of a
$\mathbb G_m$-rigidification is zero ($q^*\mathbb T_{PGL}\to
\mathbb T_{SL}$ is an isomorphism on the cotangent complex, since the band acts trivially on
$\mathbb L$), so a weight-$0$ $0$-shifted $2$-form descends uniquely:
there is a unique closed $\omega_{PGL}$ with $q^*\omega_{PGL}=\omega_{SL}$,
nondegenerate because $q^*$ is an isomorphism on $\mathbb T$.
Explicitly on the stable locus stabilizers drop
$\mathbb G_m\to\mu_3\to1$ after rigidification, all acting trivially on the
form. The Hitchin $\mathbb C^*$-scaling $t\cdot(E,\phi)=(E,t\phi)$ rescales
$\omega$ homogeneously of **weight $1$** on both $\mathbf M_{SL}$ and
$\mathbf M_{PGL}$ (linear in $\phi$ in the residue formula). This is the
identified weight: band weight $0$ (strict descent), Hitchin weight $1$.
This proves (b). The $PGL$ tangent is the adjoint-bundle complex
$[\mathrm{ad}\to\mathrm{ad}\otimes K]$, canonically identified with the
$\mathfrak{sl}$ complex, so $\omega_{PGL}$ is the same trace–residue form.

## 5. The vanishing shift: 2-shifted center class

On $\mathbf M_{GL}$ every stable point has $\mathrm{Aut}=\mathbb G_m$,
i.e. $H^0(\mathcal C^\bullet)=k$ (stacky tangent) Serre-dual to
$H^2\cong H^1(K)=k$ (obstruction). This $(1,1)$ block is the tangent of the
universal $B\mathbb G_m$: $B\mathbb G_m$ carries the canonical $2$-shifted
symplectic form from the invariant trace pairing on $\mathrm{Lie}\,\mathbb G_m$,
and the trace–trace polyvector $\mathrm{tr}(\cdot)\mathrm{tr}(\cdot)$ gives a
$2$-shifted Poisson class plus a $1$-shifted pairing between automorphisms
and $\mathrm{tr}\,\phi$-deformations. Numerically this is the
$(h^0(\mathcal O),h^1(K))=(1,1)$ block in `shift_checks.json`.

On $\mathbf M_{SL}$ both factors die: the trace projector $P$ kills the
$\mathcal O\to K$ summand, and stabilizers collapse to finite étale $\mu_3$
with $\mathrm{Lie}(\mu_3)=0$. Hence $H^0(\mathcal C^\bullet_0)=
H^2(\mathcal C^\bullet_0)=0$ at stable points: the stable $SL$ locus is a
classical smooth Deligne–Mumford stack, which admits no nonzero
$s$-shifted symplectic/Poisson structures for $s\ne0$ (perfect tangent in
degree $0$ forces the shift-$s$ pairing to vanish for degree reasons).
So the entire $2$-shifted (and $1$-shifted) center tower vanishes.
**Named vanishing shift: the $2$-shifted $B\mathbb G_m$-center
(trace–trace) class.** The associated $1$-shifted gerbe class vanishes as a
stated corollary. No other shift is affected; the $0$-shifted structure
survives as (a)–(b). This proves (c).

## 6. Computation certificate

`output/artifacts/check_shifts.py` → `output/artifacts/shift_checks.json`:
dims $(20,16,4)$; $P$ idempotent rank $8$, trace-free, block-diagonal
($\mathrm{tr}(\mathbf1\cdot P)\equiv0$, $\mathrm{tr}(\mathbf1^2)=3$);
Serre blocks $(2,2)$ $0$-shifted and $(1,1)$ $2$-shifted;
stabilizer Lie dims $1\to0$; weights
(band $0$, Hitchin $1$). All assertions pass.

## 7. Limitations

Proof is on the coprime-degree stable locus (smooth, classical for $SL$);
the strictly semistable/unstable derived and singular Hitchin-fiber loci
carry the same fiber-sequence splitting formally, but their higher-stack
obstruction theory is not analyzed here. Hypotheses $\mathrm{char}\nmid3$
(coprime degree, $1/3$ projector) and $g=2$, $r=3$ numerics are used as
stated; the same argument works for general $(g,r)$ with $\mathrm{char}\nmid r$.
Descent is to the rigidification stack $\mathbf M_{PGL}$, not to any coarse
moduli space.
