# Divergence Theorem for the Crepant E8 Singular Torus-Orbibundle Resolution

## Context

Let S_0 be an elliptic K3 orbisurface with a single E8 rational double point
(Kodaira type II* fiber) and otherwise smooth Ricci-flat orbifold metric,
equipped with orbifold anti-self-dual integral classes omega_1, omega_2 whose
local binary-icosahedral (2I) actions are nontrivial. The Goldstein-Prokushkin
T2-orbibundle X_0 -> S_0 is then singular along the T2 fiber over the E8
point, outside the smooth-total-space hypothesis of Fino-Grantcharov-Vezzoni
Theorem A and outside the cyclic A_n hypersurfaces of Fino-Grantcharov-Medel.
Let rho: S~ -> S_0 be the minimal crepant resolution (det C_E8 = 1) and
X~ the resolved GP bundle with Euler classes e_j = rho*omega_j != 0 and
exceptional set E = union_j (D_j x T2), D_i.D_j = -C_ij.
Balanced classes [omega_eps,alpha] = rho*[omega_S0]
+ eps sum a_j [D_j] + alpha [fiber] with
a = (46,91,135,110,84,57,29,68), C_E8 a = 1, are balanced-positive for small
eps, alpha > 0. The target asked either for a gluing existence with HYM
tangent connection or for a nonzero exceptional (-2)-curve / Futaki
obstruction. Both literal horns fail for structural reasons; their
conjunction is the result.

## Definitions

Vertical extension: 0 -> O_X~ -> T_X~ -> pi*T_S~ -> 0 with vertical (1,0)
field V, connection form theta, omega_C = omega_1 + i omega_2.
Slope in a balanced class: mu(F) = int c1(F) ^ omega^2 / rk(F).
Exceptional cycles: E_j = D_j x T2. Link of C^2/2I is S^3/2I.
Stringy/balanced Futaki density against a holomorphic field xi:
m_xi = L_xi(log ||Omega||_omega).

## Result (Divergence Theorem)

In the certified classes [omega_eps,alpha]:
(i) The vertical sequence is nonsplit for general smooth (1,0)-forms, so
T_X~ is strictly semistable and admits no Hermitian-Yang-Mills Chern
connection in any balanced class; hence no Hull-Strominger solution with HYM
tangent connection exists in [omega_eps,alpha].
(ii) All exceptional anomaly residues int_Ej (c2(T)-c2(V)) vanish, and the
stringy Futaki invariant vanishes identically with explicit pointwise-zero
density; the stated exceptional/Futaki obstruction mechanism is absent.
(iii) The scalar weighted-edge gap (-2,0) at weight delta=-1 is certified
(first 2I link eigenvalue 168); the full bundle uniform invertibility and
O(eps^{2/3}+alpha^2) contraction are explicit conditional hypotheses, not
proved estimates.

## Proof / Evidence

Nonsplit: a holomorphic retraction would give dbar-closed eta with eta(V)=1.
The T2-action is holomorphic so averaging Av commutes with dbar and fixes V;
Av(eta) is T2-invariant, dbar-closed, still with value 1 on V. Invariant
(1,0)-forms are f theta + pi*beta; i_V contraction gives i_V dbar eta =
-dbar f, so dbar-closed forces f = c constant. If c=0 then eta(V)=0,
impossible; if c!=0 then dbar beta = -omega_C, i.e. [omega_C]=0, contrary to
e_j != 0 integral with e_j^2 <= -2. Leray (R^0=O, R^1=O^2, R^2=O and
H^0(S~,Omega)=0 for K3) identifies H^1(X~,pi*Omega_S~) with H^1(S~,Omega_S~)
sending the class to [omega_C] != 0. Since c1(O)=c1(T)=0, both slopes are 0
in every balanced class; O is stable rank-1, so polystability of T would
split it off, contrary to nonsplit. Li-Yau/DUY for balanced classes forbids
HYM. No stability of pi*T_S~ is asserted or used.
Vanishing: c2(T) and c2(pi*E) are pullbacks of base 4-forms, hence restrict
to 0 over curves x T2 by degree; all eight residues are 0. The only
holomorphic fields are the fiber generators (K3 base has h^0(T)=0); for
T2-invariant data xi(f)=0 pointwise, so m_xi = 0 identically and F(xi)=0.
Edge: 120-element 2I Molien enumeration gives no invariants in degrees 1-11,
first at degree 12; link eigenvalues k(k+2) give lambda_1 = 168; scalar
indicial roots avoid (-2,0); gap_is_free true; delta=-1. Recomputed via
output/artifacts scripts. Bundle operator bounds are stated as hypotheses
(Proposition 4.2); the divergence does not depend on them.

## Limitations

No-HYM-tangent scope is the certified classes (no-HYM step itself is
class-independent); non-HYM-tangent or large-fiber heterotic solutions are
not ruled out. Proposition 4.2 bundle gluing is conditional. No claim about
stability of pi*T_S~ is made.

## Reproducibility

Run output/artifacts/e8_topology.py (det, inverse positivity, a, Ca=1),
molien_2I.py (120 elements, dims 0-12), edge_analysis.py (spectrum, roots,
free gap), slope_anomaly.py v4 (general nonsplit, slopes, Futaki, conditional
status). Full argument in inputs/DRAFT.md sections 2-4.

## References

Fino-Grantcharov-Vezzoni, Solutions with Torus Symmetry, CMP 2021;
Fino-Grantcharov-Medel, Fibrations Over Singular K3 Surfaces, arXiv:2501.03384v2;
Garcia-Fernandez, T-dual HS solutions, Crelle 2019;
Garcia-Fernandez-Gonzalez Molina, Futaki invariants and Yau conjecture, Crelle 2025;
Collins-Picard-Yau, Stability through conifold transitions, 2021/2024.
