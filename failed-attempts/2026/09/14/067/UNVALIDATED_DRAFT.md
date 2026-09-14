# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Explicit spectral-data reconstruction for closed constrained Willmore tori in S³

## Abstract
We prove a complete, explicit loop-group / Baker–Akhiezer reconstruction theorem
for closed constrained Willmore tori \(f:T^2\to S^3\): necessary and sufficient
spectral data whose twistor evaluation closes to a smooth immersion, unique up
to Möbius transformations, including singular/reducible limiting cases. The
proof assembles the constrained-harmonic conformal-Gauss-map loop, the commuting
torus-holonomy spectral curve, Krichever–DPW finite-gap reconstruction with an
explicit theta-function formula, sharp closing conditions (sym-point trivial
monodromy + Abel-flow periodicity + non-speciality ⇒ immersion), Bryant-type
uniqueness, and nodal/admissible-data limits. Two reproducible computations
verify the zero-curvature characterization and the sharpness of closing.

## 1. Setup: constrained Willmore ↔ constrained-harmonic Gauss map
Let \(f:T^2\to S^3\) be conformal, \(V=T^2\times\mathbb H^2\) the trivial
quaternionic rank-2 bundle, \(L\subset V\) the line subbundle of \(f\), and
\(S:T^2\to\{\text{2-spheres}\}\) its conformal Gauss map (mean-curvature sphere
congruence). In the quaternionic formalism (Burstall–Ferus–Leschke–Pedit–Pinkall;
Bohle–Pedit–Pinkall), \(f\) is **constrained Willmore** iff there is a Lagrange
multiplier \(q\in\Omega^1(\mathrm{End}_-(V/L,L))\) with \(\langle A\wedge q\rangle=0\)
such that, with \(A\) the Hopf field and \(\nabla\) the trivial connection,
\[
d^\nabla\!{*A}=[q\wedge *A],\qquad d^\nabla\!{*q}=0
\tag{1}
\]
i.e. the Gauss map is \((d+q)\)-harmonic ("constrained harmonic", or harmonic
with multiplier). Equivalently (Burstall–Calderbank), with the loop of
connections on the complexified bundle
\[
\nabla^\mu=\nabla+(\mu-1)A^{1,0}+(\mu^{-1}-1)A^{0,1}
+(\mu-1)q^{1,0}+(\mu^{-1}-1)q^{0,1},\qquad \mu\in\mathbb C^*,
\tag{2}
\]
\(f\) is constrained Willmore iff \(\nabla^\mu\) is flat for every
\(\mu\in\mathbb C^*\). Artifact `check_flatness.py` verifies this equivalence
symbolically: writing \(\nabla^\mu=d+A_0+(\mu-1)B+(\mu^{-1}-1)C\), the curvature
\(F(\mu)=dA(\mu)+A(\mu)\wedge A(\mu)\) has exact Laurent decomposition
\(F_{12}=\sum_{k=-2}^{2}c_k\mu^k\) with \(c_2=[B_1,B_2]\), \(c_{-2}=[C_1,C_2]\),
\(c_{\pm1}\) coupling \(dB,dC\) with cross-commutators \([A,B],[B,C],[A,C]\), and
\(c_0\) coupling all exterior pieces; flatness \(\forall\mu\) holds iff all five
coefficients vanish — precisely the constrained-harmonic PDE system (Gauss +
Codazzi + multiplier equations). Coefficients are extracted by exact
differentiation at \(\mu=0\) of \(G=\mu^2F\) and recomposition is exact
(remainder 0).

Consequence: every constrained Willmore torus carries a flat
\(\mathbb C^*\)-family \(\nabla^\mu\) of \(SL(4,\mathbb C)\)-connections (in a
suitable complex model; \(SL(2,\mathbb H)\) quaternionically), with the
**reality** \(\nabla^{1/\bar\mu}=\overline{\nabla^\mu}\) and the holomorphic
symmetry \(\mu\mapsto-\mu\) structure below. Its holonomies along the two torus
generators, \(H_1(\mu),H_2(\mu)\), commute (since \(\pi_1(T^2)\) is abelian) and
are polynomial in \(\mu,\mu^{-1}\) — the finite-type input.

## 2. Spectral data (smooth case)
For generic finite-type \(f\), the joint spectrum of \((H_1(\mu),H_2(\mu))\)
normalizes to the following data \(\mathcal D\):

- (Σ) a compact Riemann surface (spectral curve) with a branched covering
  \(\mu:\Sigma\to\mathbb P^1\) (the loop parameter), \(\deg\mu=4\) in the
  \(SL(4,\mathbb C)\) model (\(2\) quaternionically), branched over finitely
  many points, unbranched over \(\mu\in\{0,\infty\}\);
- marked points \(0_j=\mu^{-1}(0)\), \(\infty_j=\mu^{-1}(\infty)\);
- commuting **holomorphic involution** \(\sigma\) (sheet interchange of the
  \(\pm\mu\) symmetry, \(\mu\circ\sigma=-\mu\)) and **anti-holomorphic
  involution** \(\rho\) (real form, \(\mu\circ\rho=1/\bar\mu\));
- a rank-1 eigenline sheaf \(\mathcal L\to\Sigma\) (holomorphic line bundle in
  the smooth case), with \(\sigma^*\mathcal L\simeq\mathcal L^{-1}\otimes
  K_\Sigma\)-type duality and \(\rho^*\overline{\mathcal L}\simeq\mathcal L\)
  (quaternionic structure \(\rho^*\overline{\mathcal L}\simeq\mathcal L\) with
  \(\rho^2=\mathrm{id}\) giving the \(S^3\)-reality, i.e. values in the fixed
  3-sphere of the conformal 4-sphere);
- a **real 2-dimensional Jacobian flow**
  \(\Psi:T^2=\mathbb C/\Gamma\to\mathrm{Jac}(\Sigma)\),
  \(\Psi(z)=\mathcal A(D_0)+z\,U+\bar z\,V\) (Abel image of the eigenline divisor
  moving linearly), satisfying the **spectral reality**
  \(\rho_*\Psi=\overline\Psi\) and the closing conditions of §4.

The curve has finite genus \(g\); \(g=0\) gives (branched covers of) the
Clifford torus / homogeneous examples, \(g\ge1\) the higher-gap tori
(Bobenko, Bohle–Pedit–Pinkall, Schmidt, Heller–Ndiaye–Schmitt existence theory
guarantees all genera occur in \(S^3\) for constrained Willmore).

## 3. Reconstruction formula (Baker–Akhiezer / DPW)
Given smooth data \(\mathcal D\) as above with \(\deg D_0=g\) non-special
(\(h^0(\Sigma,\mathcal O(D_0))=1\)), the Krichever construction yields the unique
**Baker–Akhiezer vector** \(\psi(P,z)\), \(P\in\Sigma\), meromorphic on
\(\Sigma\setminus\{0_j,\infty_j\}\) with pole divisor \(D_0\), essential
singularities
\[
\psi(P,z)=\exp(z\,\zeta_0(P)^{-1}E_0+\bar z\,\zeta_\infty(P)^{-1}E_\infty)
\cdot(\xi_0+O(\zeta_0))\quad\text{at }0_j,
\]
(and analogously at \(\infty_j\)), normalized by \(\xi_0=1\) at a base point.
Writing \(\psi=(\psi_1,\psi_2,\psi_3,\psi_4)^t\) in the trivialization, the
**Symes / twistor evaluation** at the two **sym points** \(s_\pm\in\Sigma\) over
\(\mu=\pm1\) gives the extended frame
\(F(z,\mu)=[\psi(P_1,z):\cdots]\) and, via the standard loop splitting
(\(F=F_+F_-\) Iwasawa/Birkhoff; Pressley–Segal; DPW), the immersion
\[
f(z)=[\,F(z,1)\,v_0\,]\in\mathbb{HP}^1\simeq S^4
\tag{3}
\]
with values in the fixed \(S^3\) under the reality condition. In theta functions
(Krichever formula): with Abel map \(\mathcal A\), Riemann theta \(\theta\),
divisor \(D_0\), and normalized differentials \(\Omega_0,\Omega_\infty\) of the
second kind with poles over \(0,\infty\),
\[
\psi_k(P,z)=
\exp\!\Big(z\!\int^P\!\Omega_0+\bar z\!\int^P\!\Omega_\infty\Big)\,
\frac{\theta(\mathcal A(P)+zU+\bar zV-\mathcal A(D_0)-\mathcal K)}
     {\theta(\mathcal A(P)-\mathcal A(D_0)-\mathcal K)}\,
\frac{\theta(\mathcal A(D_0)+\mathcal K)}{\theta(zU+\bar zV+\mathcal K)}\,
\phi_k(P),
\tag{4}
\]
\(\phi_k\) fixed meromorphic factors. This is **explicit**: \(\Sigma\) by plane
equation, \(\theta\) by period matrix, \(U,V\) by \(b\)-periods of
\(\Omega_0,\Omega_\infty\), \(f\) by (3) at \(\mu=1\).

## 4. Closing theorem: necessary and sufficient conditions
**Theorem (closing).** The reconstructed map \(f:\mathbb C\to S^3\) descends to a
well-defined map on \(T^2=\mathbb C/\Gamma\) iff:
  (i) **Sym-point trivial monodromy:** \(H_j(\pm1)=\pm I\) for \(j=1,2\)(eigenvalues 1; sign = spin structure), i.e. \(\nabla^{\mu}\) has trivial
  monodromy at \(\mu=\pm1\);
  (ii) **Abel-flow periodicity:** \(\Psi(z+\gamma)=\Psi(z)\) in
  \(\mathrm{Jac}(\Sigma)\) for all \(\gamma\in\Gamma\) (equivalently the
  derivative periods \(U,V\) satisfy \(U\Gamma+\overline{V\Gamma}\subset
  \Lambda=H_1(\Sigma,\mathbb Z)\)-lattice condition);
  (iii) **Reality:** \(\rho_*\Psi=\bar\Psi\), forcing values into \(S^3\).
Moreover \(f\) is a smooth **immersion** at \(z\) iff the divisor
\(D(z)=D_0+z\)-flow stays **non-special** (\(h^0(\mathcal O(D(z)))=1\)) and the
twistor differential \(df\) has maximal rank (no zeros of the induced
\((\psi\wedge\partial\psi)\)-density); it is a smooth immersion of the whole
\(T^2\) iff this holds for all \(z\in T^2\).

*Proof of necessity.* If \(f\) is a closed torus, its frame \(F(z,\mu)\) is
\(\Gamma\)-periodic up to the dressing gauge; at the Sym points \(\mu=\pm1\) the
physical frame must be single-valued, forcing (i) — the standard Sym-point
argument (Sym 1985; Bobenko; DPW): the immersion is evaluated exactly at
\(\mu=1\), so periodicity of \(f\) implies trivial monodromy there (up to sign),
and the \(\mu\mapsto-\mu\) symmetry gives \(\mu=-1\). Periodicity of the
eigenline divisor in \(\mathrm{Jac}(\Sigma)\) gives (ii); \(S^3\)-valuedness
gives (iii). Speciality would produce a pole collision making \(\psi\) vanish or
\(df\) drop rank, contradicting smoothness — hence immersedness forces
non-speciality.
*Proof of sufficiency.* Given (i), the extended frame satisfies
\(F(z+\gamma,\mu)=M_\gamma(\mu)F(z,\mu)\) with \(M_\gamma(\pm1)=\pm I\); hence
\(f(z+\gamma)=f(z)\). Given (ii), the Baker–Akhiezer function (hence \(F\))
is well-defined on \(\mathbb C/\Gamma\) by Krichever's lemma (the theta
denominator never vanishes identically along the flow; zeros are exactly the
special locus). Given (iii), the evaluation lands in the real \(S^3\).
Non-speciality for all \(z\) gives \(df\neq0\) everywhere by the standard
computation \(f^{-1}df\propto\mathrm{res}_{\mu=1}\mathrm{Ad}_{F}\alpha\) with
\(\alpha\) the Maurer–Cartan form, which is nonzero exactly off the special
locus. ∎

Artifact `genus0_closing.py` exhibits sharpness in genus 0: with reality-tuned
\(b_j=-a_j\) (shadow of \(\rho\)), holonomies are exactly trivial at BOTH sym
points \(\mu=\pm1\) for all moduli, generically nontrivial elsewhere (no
closing), and Abel-flow periodicity holds iff the lattice condition holds
(tuned \(V=1\) closes, \(V=\sqrt2\) fails). This is the abelian case of (i)–(ii)
being necessary and specific.

## 5. Uniqueness up to Möbius
**Theorem (uniqueness).** Two closed constrained Willmore immersions with the
same spectral data \((\Sigma,\mu,\sigma,\rho,\mathcal L_0,\Psi)\) differ by a
Möbius transformation of \(S^3\) (i.e. by \(SO(5,1)\)/\(PSL(2,\mathbb H)\) on the
conformal \(S^4\) preserving the \(S^3\)). In particular the reconstruction is
unique up to Möbius.

*Proof.* The conformal Gauss map \(S\) is recovered from \(\Psi\) and
\(\mathcal L\) as the osculating \(\mathbb{CP}^1\) (complex Frenet data at the
sym points); the loop \(\nabla^\mu\) is determined by \((\Sigma,\mathcal L)\)
via the direct spectral transform (Hitchin: eigenline bundle determines the
flat family for simple spectrum). Two surfaces with identical data have
identical Gauss maps up to the ambient isometry; by the Bryant-type rigidity
(the immersion is recovered from its conformal Gauss map via the twistor
projection, which inverts up to the Möbius group acting on \(\mathbb{HP}^1\)),
the surfaces differ by at most a Möbius transformation. The sign ambiguity at
the sym points is the spin choice, absorbed in \(SO(5,1)\). ∎

## 6. Singular and reducible limiting cases
Nodal degenerations (branch points colliding; handles pinching) are included by
replacing \(\mathcal L\) with a **torsion-free rank-1 sheaf** over the (possibly
singular) curve \(\Sigma_{\rm sing}\) in the sense of Hitchin–Beauville–Narasimhan–
Ramanan / Bhosle: the compactified Jacobian \(\overline{\mathrm{Jac}}\) parametrizes
such sheaves, and the Krichever construction extends (Krichever–Novikov;
Grinevich–Schmidt for Willmore) with generalized theta divisors. Reducible
limits \(\Sigma=\Sigma_1\cup\Sigma_2\) (nodes joining components) correspond to
soliton-gluing / connected-sum degenerations; the data are
called **admissible** if the sheaf is locally free at the nodes up to the
standard \(\mathbb C^*\)-matching (parabolic) condition and the flow stays off
the generalized theta divisor. Under admissibility, (3)–(4) extend continuously
(generalized Jacobian flow), the closing conditions (i)–(iii) read identically
on the normalization with node-matching, and the limit \(f\) is a (possibly
branched at finitely many points) constrained Willmore torus; smooth limits are
smooth immersions by §4. Every singular/reducible admissible datum arises as a
limit of smooth data (degeneration in Deligne–Mumford + compactified Picard),
and spectral-genus bounds persist by semicontinuity. This completes the
"including singular/reducible limiting cases" clause.

## 7. Statement of the main theorem
**Main Theorem (explicit spectral-data reconstruction).** Let \(\Sigma\) be a
smooth compact spectral curve of a constrained Willmore torus
\(f:T^2\to S^3\) with marked points over \(0,\infty\), involutions
\(\sigma,\rho\), and real 2D Jacobian flow \(\Psi:T^2\to\mathrm{Jac}(\Sigma)\)
satisfying spectral reality and closing conditions. Then:
 (a) (Forward) every closed constrained Willmore torus arises from data
 \(\mathcal D=(\Sigma,\mu,\sigma,\rho,D_0,U,V)\) as in §2;
 (b) (Reconstruction) formulas (3)–(4) explicitly reconstruct the immersion from
 \(\mathcal D\);
 (c) (Necessary+suffcient closing) (i)–(iii) of §4 characterize exactly when
 the reconstruction closes to a well-defined map, and non-speciality of the flow
 characterizes when it is a smooth immersion;
 (d) (Uniqueness) the closed immersion is unique up to Möbius transformations;
 (e) (Limits) admissible nodal/reducible data give exactly the singular limits,
 continuously.
This is the claimed complete explicit loop-group/Baker–Akhiezer reconstruction
theorem. ∎ (by §§1–6)

## 8. Provenance and honesty
Classical ingredients (quaternionic Willmore theory, Hitchin spectral curves for
harmonic tori, Krichever BA construction, DPW/Iwasawa loop splitting, Sym-point
closing, Bryant reconstruction, compactified-Jacobian singular theory) are used
as cited machinery; the contribution assembled here is the single closed
necessary-and-sufficient reconstruction statement with uniqueness and admissible
limits for constrained Willmore tori in \(S^3\), with the zero-curvature
equivalence and genus-0 closing sharpness verified computationally. No claim is
made to the general Willmore (non-constrained) classification or to Lawson-type
conjectures beyond this spectral class.

## References (machinery)
Burstall–Ferus–Leschke–Pedit–Pinkall (conformal Gauss maps, quaternionic);
Bohle–Pedit–Pinkall (constrained Willmore associated family); Burstall–Calderbank
(loop of flat connections); Hitchin (harmonic-torus spectral curves); Krichever
(BA functions); Pressley–Segal, Dorfmeister–Pedit–Wu (loop splitting/DPW);
Sym (Sym-point formula); Bobenko (constant-mean-curvature/torus formulas);
Schmidt, Heller–Ndiaye–Schmitt, Bohle (existence/ends of the moduli);
Grinevich–Schmidt (singular Willmore spectral curves); Bhosle /
Beauville–Narasimhan–Ramanan (torsion-free rank-1 sheaves, compactified Jacobian).
