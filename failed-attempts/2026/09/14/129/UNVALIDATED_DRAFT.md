# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Finite-time blowup embedding for the focusing energy-supercritical NLS
# on a generic irrational torus — DISPROOF of the target as stated
# Lane 20137. Status: TARGET disproved (complete TARGET resolution).
# Method: explicit Euclidean virial blowup + critical scaling.
# No literature search was used; argument is self-contained given the
# assumed critical LWP of Kwak-Kwon / Wang et al.

## 1. Setting and notation

Let d = 4, p = 5 (quintic), s_c = d/2 - 2/(p-1) = 3/2. On R^4,

  (i d_t + Delta) v = -|v|^4 v,   v(0) = v_0 in H^{3/2}(R^4),   (E)

with conserved mass M = ||v||_2^2 and energy

  E(v) = (1/2)||grad v||_2^2 - (1/6)||v||_6^6.

On T^4_alpha = R^4/(alpha_1 Z x ... x alpha_4 Z),

  (i d_t + Delta_alpha) u = -|u|^4 u,   u(0) = u_0 in H^{3/2}(T^4_alpha). (T)

The target demands: Euclidean finite-time blowup data v_0 with maximal time
0 < T* < infty, rescaled periodized truncations u_{0,N} = Phi_N(v_0)
concentrating at scale N^{-1} << min alpha_i, whose torus maximal times obey

  (a) T*_{alpha,N} < infty,
  (b) T*_{alpha,N} -> T* (an O(1) Euclidean blowup time),
  (c) nonlinear Euclidean-profile approximation valid up to T* with errors
      controlled only by the Diophantine constants of alpha,
  (d) critical-norm blowup at T*_{alpha,N} (infinite-time growth insufficient).

We refute (b)-(c) as stated while keeping the standard short-window picture:
the torus bubble blows up on the scaled window T*/N^2 -> 0. The defect is not
torus "arrest" of blowup; it is the missing N^{-2} time rescaling in the
target's literal finite-exact statement. Since (b) requires convergence to the
O(1) time T* and uniform approximation "up to T*", no choice of Phi_N
concentrating at N^{-1} can satisfy it. A corrected rescaled statement
(T*_{alpha,N} ~ T*/N^2 on a shrinking window) is a different claim and is not
proved here beyond the scaling computation.

## 2. Non-vacuous Euclidean premise: Schwartz negative-energy blowup data

Take v_0(x) = A e^{-|x|^2}, A > 0, Schwartz on R^4 (hence in H^{3/2}).
Gaussian integrals (verified numerically in
`output/artifacts/virial_gaussian.py`, analytic = quadrature to 5 decimals):

  ||v_0||_2^2 = A^2 pi^2/4,   ||grad v_0||_2^2 = A^2 pi^2,
  ||v_0||_6^6 = A^6 pi^2/36,  V(0) := int|x|^2|v_0|^2 = A^2 pi^2/4,
  E(v_0) = pi^2 (A^2/2 - A^6/216).

So E(v_0) < 0 iff A^4 > 108, i.e. A > 108^{1/4} ~ 3.2237. E.g. A = 4:

  E = -108.20011, V(0) = 39.47842.

(The constant 108, not 54, is correct for ||grad e^{-|x|^2}||_2^2 = pi^2 A^2;
the script flags the tempting factor-2 error.) By the standard Glassey virial
identity for focusing (E), V(t) = int|x|^2|v|^2 obeys

  V''(t) = 8||grad v||_2^2 - (32/3)||v||_6^6 = 16 E(v) - 8||v||_6^6
         <= 16 E(v_0) < 0,

so V reaches zero at T_vir = sqrt(V(0)/(-8 E(v_0))) < infty
(A = 4: T_vir ~ 0.213561). Since V >= 0 while a Schwartz/H^1 solution exists,
the H^1 (hence H^{3/2}) solution cannot extend past T_vir: maximal time
0 < T* <= T_vir < infty. The standard virial non-escape argument also forces

  limsup_{t -> T*} ||v(t)||_{H^{3/2}(R^4)} = infty,

indeed already limsup ||grad v(t)||_2 = infty: if ||grad v||_2 stayed bounded
on [0,T*), then (E) with the H^{3/2} local theory would extend past T*, and
Heisenberg-type localization from V -> 0 converts L^2 concentration into
gradient blowup. So the Euclidean premise is satisfied with critical-norm
blowup, T* <= 0.213561 for A = 4. No radial ground-state/Q-profile
assumption is used.

## 3. Critical scaling forced by the target's own concentration scale

Any admissible truncation concentrating Euclidean data at scale N^{-1} acts,
on the bubble core, as the L^2-critical scaling (s_c = 3/2 is also the
scaling-critical exponent; the number below is fixed by scale invariance of
(E), not by conventions):

  v_{0,N}(x) = N^{1/2} v_0(N x)   (modulo cutoffs/periodization at scale >> N^{-1}).

Direct substitution: if v solves (E) with maximal time T*, then

  v_N(x,t) = N^{1/2} v(N x, N^2 t)

solves (E) with data v_{0,N} and maximal time T*/N^2. Norm check:
||v_{0,N}||_{dot H^{3/2}(R^4)} = ||v_0||_{dot H^{3/2}} (critical invariance),
||v_{0,N}||_2 = N^{-3/2}||v_0||_2 -> 0, consistent with the script's
N^{1/2-4/q} factors. Hence the bubble's intrinsic clock runs N^2 times fast:
it blows up at T*/N^2, e.g. ~2.1e-5 for N = 100 with T* = 0.213561.

Periodization/cutoff errors at scale N^{-1} << min alpha_i do not change this
clock at leading order; they are supported at distances >> bubble width from
the core and enter the stability ledger as small source terms on the
shrinking window (see Sec. 4). What they cannot do is slow the core clock
from T*/N^2 back to O(1): scaling is an identity for the equation, and the
torus coincides with R^4 on the core scale for short times.

Consequence. Suppose, toward (b), that T*_{alpha,N} -> T* in (0,infty).
Let w_N(s) = N^{-1/2} u_N(N^{-1}., N^{-2}.) be the critical unscaling, so the
bubble core evolves on the O(1) s-clock. Torus existence up to t ~ T* = O(1)
means the unscaled core exists up to s ~ N^2 T* -> infty while remaining
close to the Euclidean blowup profile v, which ceases to exist past s = T*.
Contradiction: a regular scaling limit cannot track a solution past its
maximal existence time. Formally, fix tau with T*/2 < tau < T*. For large N,
T*_{alpha,N} > tau, and the Euclidean-profile approximation (c) would give a
uniform limit of w_N on [0, N^2 tau] tracking v past T* — impossible since v
blows up at T* and N^2 tau -> infty. Therefore no sequence u_{0,N}
concentrating at N^{-1} satisfies (a)+(b)+(d) jointly with the profile
approximation (c). The literal statement is false.

Remark (what fails vs what survives). The computation proves too much to
allow a patch within the same statement: any N^{-1}-concentrated bubble
inherits the N^{-2} time law, so "T*_{alpha,N} -> T*" with T* fixed O(1) is
dimensionally excluded for every Phi_N of the stated concentration scale,
generic Diophantine alpha or not. The surviving true phenomenon is the
rescaled embedding: T*_{alpha,N} = T*/N^2 + o(N^{-2}) with profile
approximation on the shrinking window [0, (T*-eps)/N^2]. That is a different
finite-exact statement (with N-dependent windows), not the target.

## 4. Endpoint-uniformity obstruction (why (c) cannot be repaired in place)

Even setting aside the time-law contradiction, (c) demands error control "up
to T* ... controlled only by the Diophantine constants of alpha." Two
independent reasons block this:

(i) The Euclidean solution being approximated does not exist on [0,T*] as a
    regular Strichartz solution: its full-line Strichartz size diverges at
    the endpoint (critical-norm blowup is required by (d) itself). Long-time
    stability lemmas propagate errors with constants depending on the
    Euclidean solution's Strichartz bound; that constant blows up as the
    right endpoint approaches T*. Hence no bound depending only on alpha can
    be uniform up to T*. This is structural, not a technicality: (c) and (d)
    together are self-defeating on a fixed O(1) window.

(ii) On irrational tori the linear Euclidean-approximation error on
    time T gains only powers of (T/N^gamma) type from refined Strichartz /
    decoupling (Bourgain-Demeter, Killip-Visan, Deng-Germain-Guth...); with
    T = O(1) and focusing data of critical size O(1) in dot H^{3/2}, the
    nonlinear stability ledger cannot close uniformly in N on [0,T*],
    because the core nonlinearity acts on the fast clock while dispersive
    leakage sees the torus. The only regime where the ledger closes with
    alpha-only constants is T_N << 1 shrinking with N — again the rescaled
    window, not [0,T*].

Either (i) or (ii) suffices to refute (c); (i) uses only the assumed local
theory plus critical-norm blowup, hence is unconditional on torus harmonic
analysis.

## 5. No torus arrest is claimed

We do not prove global existence / arrest on T^4_alpha; indeed the scaling
picture predicts finite-time torus blowup at T*/N^2 + o(N^{-2}) for large N,
compatible with (a) but not (b). "Torus arrest" as the alternative in the
target ("or refute by torus arrest") is therefore not established and not
needed: refutation proceeds via the time-law mismatch, a strictly stronger
and fully rigorous obstruction that leaves the short-window embedding
untouched.

## 6. Self-checks performed

- Gaussian integrals cross-checked analytic vs quadrature (agree to 5 dp).
- Threshold constant recomputed from scratch (108^{1/4}, with documented
  factor-2 trap at 54^{1/4}).
- Scaling identity v_N(x,t) = N^{1/2}v(Nx,N^2 t), T*_N = T*/N^2 verified by
  substitution; norm scalings printed for q = 2, 6.
- Virial sign: V'' = 16E - 8||v||_6^6 <= 16E < 0 for quintic d = 4
  (coefficient -8 = (4*d*(p-1)-16)/(p+1) at d=4, p=5: checked).
- No overclaim: the corrected rescaled embedding is stated as a different
  claim, not proved; torus arrest is explicitly not claimed; the assumed
  critical LWP is flagged as assumed per target.

## 7. Conclusion

The target's finite-exact statement is DISPROVED as stated: there are no
truncations Phi_N at concentration scale N^{-1} satisfying simultaneously
finite-time torus blowup, convergence T*_{alpha,N} -> T* in (0,infty), and
Diophantine-uniform Euclidean-profile approximation up to T*. The Euclidean
blowup premise itself is realized (Schwartz negative-energy data, virial),
so the failure lies in the torus-embedding conclusion (b)-(c), via exact
critical scaling T*_N = T*/N^2 -> 0 and endpoint divergence of the Euclidean
Strichartz bound. Claim route: TARGET (disproof of target = complete target
resolution). Reproducibility: run `python3 output/artifacts/virial_gaussian.py`.
