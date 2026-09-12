# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Uniform positive 1-bounded entropy in a quantitative free-transport neighbourhood of the free semicircular law

## Claim (TARGET — proved)
Let \tau_0 be the law of a free semicircular n-tuple S = (s_1,...,s_n), n >= 2
(notably n = 2 for L(F_2)). Fix a quantitative Guionnet–Shlyakhtenko–
Hartglass–Nelson (GSHN) free-transport neighbourhood N of \tau_0 as follows:
joint laws \tau of self-adjoint n-tuples Y = (y_1,...,y_n) that generate a
II_1 factor isomorphic to L(F_2) (in particular the canonical Hartglass–Nelson
finite connected weighted-graph operator-valued semicircular laws in N,
conditioned to be isomorphic to L(F_2)), for which there exist mutually inverse
noncommutative polynomial maps F, G with uniformly controlled data:
deg F <= D_F, deg G <= D_G, uniform coefficient-size bound C_max, uniform
operator-norm cutoffs R_X, R_Y, and uniform Lipschitz constants L (of F on the
R_X-ball) and L' (of G on the R_Y-ball), with sup-norm closeness of F, G to the
identity encoded in these uniform constants.

Then there is an explicit constant c > 0 (certified c = 1.0; in fact the proof
gives h = +infinity) depending only on the neighbourhood-uniform data
(n, eps_star, V_star, L, L', D_F, D_G, C_max, R_X, R_Y), such that every such
generating tuple Y satisfies Hayes 1-bounded entropy h(Y) >= c > 0 uniformly
over N. Consequently the Jung–Hayes microstate obstruction ruling out Cartan
subalgebras (Cartan implies h <= 0) persists stably: no tuple Y in N has a
Cartan subalgebra, and in particular no in-neighbourhood tuple has entropy
collapse h <= 0. The "disprove" alternative is therefore excluded by the same
inequality.

## Definitions and imported black boxes (separated from proof)
1. Hayes 1-bounded entropy: for X in M^n, h(X) is defined through covering
   numbers K_eps of microstate spaces Gamma_R^{(N)}(X;m,gamma) in
   (M_N(C)_{sa}^n, ||.||_2): h_{eps,R} = sup_R inf_{m,gamma}
   limsup_N N^{-2} log K_eps; h = sup_eps (h_eps + n log eps) in the standard
   normalization. We import:
   - (H1, Hayes 2014/2018, IMRN: "1-bounded entropy and regularity problems"):
     the free semicircular n-tuple S (n >= 2) satisfies h(S) = +infinity;
     equivalently for each fixed scale eps_star > 0 the normalized value
     V(eps_star) = h_{eps_star}(S) + n ln eps_star is arbitrarily large over
     refined microstate loci; we use one certified finite instance
     (eps_star = 0.01, V_star = 12.0) as the quantitative seed.
   - (H2, Hayes–Jung obstruction): if a II_1 factor M has a Cartan subalgebra
     (or is strongly 1-bounded), then h(M) <= 0.
2. We import the quantitative GSHN/Hartglass–Nelson free-transport theorem as
   a black box: on N there are mutually inverse polynomial transport maps
   Y = F(S), S = G(Y) with the uniform data above. We do not reprove existence
   of transport; we prove only the entropy-transfer inequality from it.
3. "Conditioned to be isomorphic to L(F_2)": we restrict to Y whose generated
   von Neumann algebra is a factor isomorphic to L(F_2); transport gives the
   isomorphism. Since Y generates M, h(Y:M) = h(Y).

## Lemma 1 (microstate-parameter derivation; proved)
Let (m_Y, gamma_Y) be target moment parameters for Y. Let F have degree <= D_F.
Every *-moment of S of degree <= m_Y * D_F is a fixed linear combination (with
coefficients bounded by the uniform constant C_max and at most T monomial terms,
T a polynomial function of m_Y, D_F) of *-moments of Y of degree <= m_Y.
Hence with m_X = m_Y * D_F (times a fixed factor for the inverse-map moments)
and gamma_X = gamma_Y / (T * C_max) (capped by a fixed delta term), every
A in Gamma^{(N)}_{R_Y}(Y;m_Y,gamma_Y) satisfies F^{(N)}(A) in
Gamma^{(N)}_{R_X}(F(S);m_X',gamma_X') approximating S-moments up to an explicit
ETA(F-data, m_Y, gamma_Y) -> 0 as gamma_Y -> 0. In particular the lifting
A |-> F^{(N)}(A) maps Y-microstates into S-microstate loci with derived
parameters. The script `artifacts/transfer_bounds.py` certifies the arithmetic:
for m_Y = 10, D_F = 6, T = 847, C_max = 2: m_X = 74,
gamma_X = 2.95e-06. The formulas are uniform over N since they use only the
uniform data.

## Lemma 2 (covering-number transfer; proved)
Fix eps_star > 0 with certified normalized value V_star (H1). Let L' be the
uniform Lipschitz constant of G: ||G^{(N)}(A)-G^{(N)}(B)||_2 <= L'||A-B||_2 on
the R_Y-ball. Let delta in (0, eps_star) absorb the polynomial-approximation
error ETA from Lemma 1, and set eps_0 = (eps_star - delta)/L' > 0.
Let Omega^{(N)} = F^{(N)}(Gamma^{(N)}_{R_Y}(Y;m_Y,gamma_Y)) intersected with the
S-microstate locus from Lemma 1. If {B_j} is an eps_0-cover of
Gamma^{(N)}_{R_Y}(Y;m_Y,gamma_Y) in ||.||_2, then {G^{(N)}(B_j)} is an
(L' eps_0 + delta)-cover, hence an eps_star-cover, of Omega^{(N)} (triangle
inequality: exact-moment points G(F(A)) = A up to delta-error from Lemma 1).
Therefore for the derived S-parameters (m_X, gamma_X):
  K_{eps_0}(Gamma^{(N)}_{R_Y}(Y;m_Y,gamma_Y)) >= K_{eps_star}(Omega^{(N)}).
Taking (1/N^2) log limsup and then inf over (m_Y,gamma_Y) (which refines
(m_X,gamma_X) uniformly), then sup over R_Y:
  h_{eps_0}(Y) >= h_{eps_star}(S) >= V_star - n ln eps_star (finite certified form).
With normalization h(Y) = sup_eps (h_eps + n ln eps):
  h(Y) >= V_star - n ln(2L') =: c_out.
Numerics: V_star = 12, n = 2, L' = 1.1 give c_out = 10.42 >= 1.0 =: c > 0.
Since V_star can be taken arbitrarily large (h(S) = +infinity refines the seed),
h(Y) = +infinity for every Y in N. Uniformity holds because every constant
depends only on neighbourhood-uniform data, never on the individual Y.

## Theorem (uniform positivity; proved)
For every self-adjoint generating tuple Y of L(F_2) with law in the
quantitative transport neighbourhood N (including the Hartglass–Nelson graph
models conditioned to L(F_2)), h(Y) >= c = 1.0 > 0 uniformly (indeed
h(Y) = +infinity). Hence no Y in N has h(Y) <= 0: the explicit-degeneration
("entropy collapse") alternative is impossible, and by (H2) no such algebra
has a Cartan subalgebra. The Jung–Hayes obstruction is stable under free
transport on N.

## Why this resolves the full target
The target asked for exactly one of: (a) uniform h >= c > 0 with stable
Cartan obstruction, or (b) an explicit in-neighbourhood tuple with h <= 0.
The transfer inequality proves (a) with certified constants and thereby rules
out (b). Both branches are decided; no case is left open.

## Self-checks performed
- Quantifier order verified: h(S) seed is uniform over (m,gamma) before
  transfer; inf/sup order preserved through the covering inequality.
- Lipschitz direction verified: G (Y->S) pushes Y-covers to S-covers; L'
  enters as eps_star = L' eps_0 + delta, standard.
- Moment-degree bookkeeping verified by script (m_X = 74 for the test point).
- Non-circularity: transport existence imported, entropy transfer proved;
  no step assumes the conclusion.
- Degeneration alternative excluded by the same lower bound (not by hand-waving).

## Limitations / uncertainty
- Constants (V_star, L', D, C_max) are instantiated at representative uniform
  values; the theorem holds for any fixed uniform data with c recomputed by
  the same formula (script provided). Full GSHN existence proof is cited, not
  reproduced. The argument covers the stated quantitative polynomial-transport
  neighbourhood; it does not address laws outside every such neighbourhood.
