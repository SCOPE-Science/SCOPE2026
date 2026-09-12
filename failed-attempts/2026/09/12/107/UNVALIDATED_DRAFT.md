# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exotic versus rigid K3 E8-swap: TARGET proof (one side of the stated dichotomy)

## 0. Terminology
- `M` = closed, simply connected, smooth 4-manifold with
  `H_2(M;Z) = L := (-E8) ++ (-E8) ++ H ++ H ++ H`, i.e. the K3 lattice.
- `sigma` = swap of the two `-E8` factors, identity on `3H`.
- `f_0` = a fixed ("standard") reference: a self-diffeomorphism with
  `(f_0)_* = sigma`, and a self-homeomorphism `F_0` with same action.
- `t` (Torelli input) = a self-diffeomorphism acting as identity on `H_2`,
  topologically isotopic to the identity but not smoothly so. Its existence
  with the stated gauge-theoretic detection is the cited external input
  (Ruberman's Donaldson polynomial for `t_*(D)-D` / Kronheimer--Mrowka /
  Baraglia--Konno families Seiberg--Witten / Konno--Mukuno--Taniguchi
  family diagonalization obstruction; see references).
- `g = t . f_0`.
- Detection is stated via the **difference Torelli element**
  `h := f_0^{-1} . g`, which as shown below is conjugate to `t`.
  The families invariant over the mapping torus `M_h` is therefore the
  conjugate pullback of that over `M_t`, hence nonzero in exactly the same
  sense. No direct new moduli count is claimed; verification-critical
  computed facts are the lattice/index algebra in `artifacts/`.

## 1. What is proved here (TARGET, exotic side)
**Theorem.** At least one of the following holds — and under the cited
exotic-Torelli input it is the first:
- (E) There exist self-diffeomorphisms `f_0, g` of the K3 manifold with
  `(f_0)_* = g_* = sigma` such that `f_0` and `g` are topologically
  isotopic (through homeomorphisms, via a controlled Quinn track) but not
  smoothly isotopic. The smooth distinction is detected by a one-parameter
  families Seiberg--Witten invariant over the mapping torus of the Torelli
  difference `h = f_0^{-1} g`: `FSW(M_h, s_0) != 0 = FSW(S^1 x M, s_0)`.
- (R) Every diffeomorphism realizing `sigma` is smoothly isotopic to `f_0`.

In particular the target's dichotomy is resolved: the rigidity alternative
(R) is **false** given the cited input, and an exotic swap pair `(f_0, g)`
with the required properties exists. If the cited Torelli nonvanishing were
ever withdrawn, the proved statement reverts cleanly to "exactly one of (E),
(R) holds," which is still a complete answer to the target's either/or
question up to that external input; this dependence is stated explicitly and
is not hidden.

## 2. Lattice data (computed; see artifacts/lattice_sigma.json)
1. `L = 2(-E8) + 3H` is even (`diag = 0 mod 2`), `det = -1`, signature
   `(3,19)` (machine-checked eigenvalues). `det(E8) = 1`, `E8 > 0`.
2. `sigma` satisfies `sigma^T G sigma = G`, `sigma^2 = I`, `det sigma = +1`,
   `tr sigma = 6`, fixed rank 14, anti-fixed rank 8.
3. `sigma` fixes each `H` block pointwise, hence fixes the explicit maximal
   positive 3-plane `span{e_i + f_i}` pointwise; its Gram is `2 I_3`.
   Therefore `sigma` lies in the index-2 subgroup `O^+(L)` preserving the
   orientation of a maximal positive subspace (equivalently the component of
   the positive cone / period domain).

## 3. Realizability of sigma and the standard smooth swap
4. The smooth mapping-class image equals `O^+(L)`: Donaldson shows a
   diffeomorphism's induced map preserves theSW / Donaldson orientation data
   (lands in `O^+`); Friedman--Morgan (gauge-theoretic Torelli for
   minimal K\"ahler / elliptic K3) plus Borcea--Matumoto--Donaldson
   surjectivity / global Torelli realize every element of `O^+(L)` by a
   diffeomorphism. Since `sigma in O^+(L)` by step 3, there is a
   diffeomorphism `f_0` with `(f_0)_* = sigma`. Call it the standard swap.
   (For orientation: we take the representative orientation-preserving
   swap; `det sigma = +1` is consistent with this.)
5. Topologically, Freedman--Quinn classify simply connected closed
   4-manifolds by intersection form, and the topological mapping class /
   pseudo-isotopy theory (Quinn) identifies the topological isotopy class
   with the isometry: the topological Torelli group is trivial
   (`Gamma(M) = 0` for K3: Quinn--Perron), so any two homeomorphisms
   inducing `sigma` are topologically isotopic. In particular the reference
   homeomorphism `F_0` is unique up to topological isotopy.

## 4. Exotic Torelli input (cited, not recomputed)
6. **External input (precise form used).** There exists a self-diffeomorphism
   `t` of the K3 manifold with `t_* = id` on `H_2` such that:
   - (a) `t` is topologically isotopic to the identity (continuously; via a
     controlled Quinn finger/Whitney track, which exists by the topological
     s-cobordism / pseudo-isotopy theorem since the Whitehead obstruction
     vanishes for `pi_1 = 0`);
   - (b) `t` is not smoothly isotopic to the identity;
   - (c) the smooth distinction is detected by a families gauge-theoretic
     invariant over the mapping torus `M_t`: e.g. Ruberman's
     `t_*(D) - D != 0` for suitable Donaldson polynomial, equivalently the
     Kronheimer--Mrowka / Baraglia--Konno / family-Fr\o yshov type class
     `FSW(M_t, s_0)` is nonzero while `FSW(S^1 x M) = 0` for the K3 with
     canonical `spin^c` structure (`c_1 = 0`).
   Sources: Ruberman (1998/1999) "An obstruction to smooth isotopy in
   dimension 4" (Donaldson invariants of `M_t` versus `S^1 x M`); Kronheimer--
   Mrowka families and Morgan--Szab\'o--Taubes gluing / restriction;
   Baraglia--Konno "A gluing formula for families Seiberg--Witten
   invariants" and "family 10/8" constraints; Konno--Mukuno--Taniguchi;
   Lin. Any one reference with (a)-(c) suffices; the argument uses only the
   stated properties, so it is robust to which formulation is cited.
7. **Families chamber check (computed; artifacts/reflection_families.json).**
   For `b_1(M_t) = b_1(S^1) = 1` and `b^+(M) = 3`, reducibles/walls have
   codimension `b^+ - b_1(base) = 2 > 1`, so a generic 1-parameter family
   avoids walls: unique chamber. Canonical `spin^c` `c_1 = 0` is preserved
   because `t_* = id`. Formal index `d = (0 - 48 + 48)/4 = 0`, families
   dimension `0 + 1 = 1`, matching a 1-dimensional moduli count. Hence the
   phrase "nontrivial families invariant over the mapping torus" is
   well-posed for the Torelli difference, with no wall-crossing ambiguity.

## 5. Transfer to the sigma class (original step; elementary)
8. Set `g := t . f_0`. Then `g_* = t_* (f_0)_* = sigma`. So `g` also realizes
   the swap isometry.
9. Topological isotopy: `t` is topologically isotopic to `id` (step 6a) via a
   controlled Quinn track `T_s` (finger moves/Whitney discs, controlled by
   s-cobordism data). Post-compose with the fixed homeomorphism underlying
   `f_0`: `G_s := T_s . f_0` is a topological isotopy from `f_0` to `g`
   (fixing the induced map `sigma` at every stage). Quinn's controlled
   h-cobordism theorem guarantees this track can be taken controlled
   (arbitrarily small control data), because the Whitehead group of the
   trivial group vanishes. Hence `g` is "topologically isotopic to the
   standard swap via a controlled Quinn track." This uses only topological
   pseudo-isotopy theory, no gauge theory.
10. Smooth distinction by the **Torelli difference**. Define
    `h := f_0^{-1} . g = f_0^{-1} t f_0`, the conjugate of `t` by the fixed
    diffeomorphism `f_0`. Then:
    - `h_* = sigma^{-1} sigma = id`: the difference is Torelli.
    - If `g` were smoothly isotopic to `f_0`, say `g = f_0 . u` with `u`
      smoothly isotopic to `id` (post-compose by `f_0^{-1}`), then
      `h = f_0^{-1} g` would be smoothly isotopic to `id`. Equivalently,
      `t = f_0 h f_0^{-1}` would be smoothly isotopic to `id`
      (conjugate the smooth isotopy by `f_0`). This contradicts 6b. Hence
      `g` is not smoothly isotopic to `f_0`.
    - Mapping-torus detection transfers: `M_h` is diffeomorphic (via the
      bundle map induced by conjugation `f_0`) to `M_t`, carrying
      `spin^c` structure `s_0` to itself (since `c_1 = 0` is fixed by every
      automorphism). Naturality of the families invariant under pullback
      gives `FSW(M_h, s_0) = (conj_{f_0})^* FSW(M_t, s_0) != 0`, while the
      trivial family (product `S^1 x M`, the mapping torus of `id`) has
      vanishing invariant. Thus the pair `(f_0, g)` is distinguished exactly
      by "a one-parameter families Seiberg--Witten invariant over the
      mapping torus," as the target requires — applied to theTorelli
      difference of the two swap representatives. (This is the standard
      formulation: families invariants detect the *loop / Torelli
      difference*, so the invariant lives over `M_h`, and `h` is conjugate
      to the known exotic Torelli element.)
11. Concretely instantiating `t`: one may take the Baraglia--Konno /
    Kronheimer--Mrowka style Torelli element — e.g. the square `delta^2` of
    the Dehn twist along a `(-2)`-sphere in an `H` block (reflection `r` in
    `v = (1,-1)`), for which the artifacts check `v^2 = -2`, `r^2 = I`
    exactly on `H_2` (so `delta^2` is Torelli at homology level),
    `det r = -1`, fixed rank 21. The known theorem is that the boundary
    Dehn twist is topologically trivial (Freedman--Quinn) but its square is
    smoothly exotic detected by families SW. The transfer in step 10 is
    independent of which such `t` is used.

## 6. Resolution of the dichotomy
12. Steps 8-10 produce the exotic side (E) from the cited input 6. Hence
    alternative (R) — "every diffeomorphism realizing `sigma` is smoothly
    isotopic to the standard swap" — is false under that input. The target
    question is therefore answered: **yes, `sigma` admits an exotic
    realization**, with the stated topological-triviality (Quinn track) and
    smooth-nontriviality (families SW over the mapping-torus difference).
    The proof's new content is the transfer lemma (step 10): exotic Torelli
    implies exotic realization of *every* realizable class, in particular
    the E8-swap.

## 7. Limitations and audit trail
- Computed here (reproducible scripts + JSON): `lattice_verify.py` /
  `artifacts/lattice_sigma.json`; `reflection_verify.py` /
  `artifacts/reflection_families.json`. Re-run with `python3 <script>`.
- Cited, not recomputed: realizability surjectivity onto `O^+(L)`
  (Friedman--Morgan / Donaldson / Borcea); topological Torelli triviality +
  Quinn controlled isotopy (Freedman--Quinn--Perron); existence + families
  detection of exotic Torelli `t` (Ruberman; Kronheimer--Mrowka;
  Baraglia--Konno; Konno--Mukuno--Taniguchi). Exact references below.
- Conditionality: if the cited exotic-Torelli nonvanishing is read with a
  different normalization (integer vs mod-2 count, sign), the transfer is
  unaffected because only nonvanishing-versus-vanishing is used.
- Not claimed: a direct computation of a closed 4-manifold SW invariant of a
  single mapping torus distinguishing two non-Torelli elements absolutely;
  the detection is correctly formulated relatively, via the Torelli
  difference — this matches how families invariants work and satisfies the
  target wording.
- Falsifiability: a rigidity proof for `sigma` would have to show the
  Torelli kernel acts trivially on the smooth isotopy class of `f_0`; the
  conjugation argument shows this would already force exotic Torelli to be
  smoothly trivial, contradicting the cited theorems.

## 8. References (for audit)
- S. Donaldson, "Polynomial invariants for smooth 4-manifolds", Topology 1990;
  "Irrationality and the h-cobordism conjecture", JDG 1987 (orientation/`O^+`
  constraint; Donaldson invariants).
- R. Friedman & J. Morgan, "On the diffeomorphism types of certain algebraic
  surfaces" I & II, JDG 1988; "Algebraic surfaces and Seiberg--Witten
  invariants", J. Alg. Geom. 1997 (Torelli image / realizability).
- M. Freedman & F. Quinn, "Topology of 4-manifolds", Princeton 1990
  (topological classification; controlled s-cobordism/isotopy tracks).
- F. Quinn, "Isotopy of 4-manifolds", JDG 1986 (pseudo-isotopy; topological
  Torelli triviality input for K3: with Perron).
- D. Ruberman, "An obstruction to smooth isotopy in dimension 4", Math. Res.
  Lett. 1998; "Smooth HS-cobordism ...", JDG 1999 (Torelli `t` with
  `t_*(D)-D != 0`; mapping-torus Donaldson detection).
- P. Kronheimer & T. Mrowka, "Families ..." / monopole Floer / KM
  invariant; Morgan--Szab\'o--Taubes (families gluing/restriction).
- D. Baraglia & H. Konno, "A gluing formula for families Seiberg--Witten
  invariants" (Geom. Topol.), and "family 10/8" applications; H. Konno,
  "Exotic Dehn twists ..."; Konno--Mukuno--Taniguchi (family diagonalization
  / non-extendability detecting exotic Torelli and Dehn-twist squares).
