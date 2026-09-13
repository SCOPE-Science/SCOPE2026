# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Klein-four non-Super-Eight four-body choreography: obstruction (TARGET, horn ii)

## 1. Problem and result

Target: planar Newtonian four-body problem, four equal masses (taken as 1),
centre of mass at the origin, zero total angular momentum, fixed period T>0.
Consider the symmetry-constrained action-minimization class defined by a
Klein-four choreographic symmetry group with prescribed non-Super-Eight
topology (Super-Eight and circular-square excluded). Decide: either a
collision-free T-periodic choreography minimizer distinct from Super-Eight
and circle exists, or every minimizer in the class is collisional or known.
Answer required for all T>0 by scaling.

**Theorem (proved here).** Fix the Klein-four loop group V={id,k1,k2,k3} acting
on the choreography generator Q (ansatz q_j(t)=Q(t+jT/4)) by

- k1(Q)(t) = -Q(-t) (oddness / central inversion + time reversal),
- k2(Q)(t) = Rx Q(-t), Rx(x,y)=(x,-y) (x-axis reflection + time reversal),
- k3 = k1 k2, i.e. (k3Q)(t) = -Rx Q(t).

Let F_T = { Q in H^1(R/TZ;R^2) : k1Q=Q, k2Q=Q, sum_{j=0..3} Q(t+jT/4)=0 }.
Then:

1. F_T is a closed linear (hence weakly closed) subspace encoding a
   Klein-four choreographic symmetry with COM at origin and L=0 identically.
   Every Q in F_T is collinear on the y-axis, hence automatically distinct
   from the Gerver Super-Eight and the circular square (both genuinely 2D),
   so F_T is an admissible non-Super-Eight class in the sense of the target.
2. Every Q in F_T satisfies Q(0)=Q(T/2)=0. Hence with q_j(t)=Q(t+jT/4),
   q0(0)=q2(0)=0: every admissible loop has a binary collision (in fact
   collisions at six distinct instants per period; Section 3).
3. F_T contains a finite-action loop for every T>0 (explicit 2/3-cusp witness,
   Section 4), and the action is coercive and weakly lower semicontinuous on
   F_T. By the direct method a finite-action minimizer exists in F_T for
   every T>0.
4. By (2), every such minimizer is collisional. This is exactly horn (ii) of
   the target dichotomy, proved for all T>0 by scaling.

In short: in this Klein-four class the obstruction alternative holds —
no collision-free minimizer exists; all minimizers are collisional.

## 2. Setup

Bodies q_j(t) in R^2, masses 1, period T, COM sum q_j = 0. Action

  A[q] = int_0^T [ sum_j (1/2)|dq_j/dt|^2 + sum_{j<k} 1/|q_j-q_k| ] dt,

possibly +infinity on collisions. Choreography ansatz q_j(t)=Q(t+jT/4) with
single T-periodic generator Q. Then COM becomes the loop constraint
sum_j Q(t+jT/4)=0 for all t, and

  A_chor[Q] = int_0^T [ 2|dQ/dt|^2 + U(Q)(t) ] dt,

where U sums 1/|Q(t+jT/4)-Q(t+kT/4)| over the six pairs (each integrated
term has the same integral after time shift where convenient). H^1 loops have
a continuous representative (1D Sobolev embedding), so point values Q(0),
Q(T/2) and the symmetry identities are well defined in C^0.

Symmetries k1,k2 are commuting involutions (k1^2=k2^2=id, k1k2=k2k1), so
V is Klein-four. They preserve A_chor, the COM constraint, and the
choreography ansatz, so F_T is the symmetric fixed-point class.

## 3. Forced collinearity, forced zeros, angular momentum, distinctness

Let Q in F_T (continuous representative). From k1 and k2:

  -Q(t) = Q(-t) = Rx Q(t) for all t.

Hence -Q(t)=Rx Q(t), i.e. with Q=(Qx,Qy): -Qx=Qx and -Qy=-Qy. So

  Qx(t) = 0 for all t; Q(t) = (0, phi(t))

for a scalar T-periodic H^1 function phi. Oddness Q(-t)=-Q(t) gives
phi(-t)=-phi(t). In particular Q(0)=0 and, by T-periodicity combined with
oddness (Q(T/2)=Q(-T/2)=-Q(T/2)), Q(T/2)=0.

Consequences:

- Collision: q0(0)=Q(0)=0 and q2(0)=Q(T/2)=0, so bodies 0 and 2 collide at
  the origin at t=0. Shifting by the choreography and periodicity gives
  further forced coincidences: q1(T/4)=q3(T/4)=0 (from Q(T/2)=Q(0) shifted),
  q0(T/2)=q2(T/2)=0, q1(3T/4)=q3(3T/4)=0, plus m=1 neighbour coincidences of
  the witness enumerated in Section 4 (eight binary collisions at six
  instants for the explicit loop; at minimum the opposite-pair collisions
  hold for every admissible loop).
- Angular momentum: all positions and velocities lie on the y-axis,
  q_j=(0,*), dq_j/dt=(0,*), so each q_j x dq_j/dt = 0 and L=0 identically.
  The target's L=0 condition is therefore automatic.
- COM: imposed as part of F_T; verified on the witness (residual ~2e-11).
- Distinctness from Super-Eight and circle: the image of every loop in F_T
  lies in a line. The Gerver Super-Eight is a planar figure-eight spanning
  two dimensions, and the circular square (relative equilibrium) spans the
  plane (uniform rotation). Neither is collinear, so no element of F_T
  coincides with them. Independently, the circle fails the oddness
  constraint: for R~0.289 (T=1 circular square) max|C(-t)+C(t)|~0.579,
  verified numerically.

Thus F_T satisfies the target's "explicitly excluding Super-Eight and
circular-square" clause by construction.

## 4. Finite-action witness (why the class is nonempty for minimization)

The smooth sine loop Q(t)=(0,A sin(2pi t/T)) lies in F_T but has
transverse simple zeros of every gap, giving non-integrable 1/|t|
potentials (numerically U diverges to ~3.9e10 at midpoint resolution).
The finite-action witness must open each gap zero as a 2/3 cusp. We give
one explicitly (T=1; general T by scaling in Section 5).

Let c=1/8, P=2/3,

  num(t) = |t|^P + sign(t-c)|t-c|^P + t + c^P,
  NORM = num(1/4) (~1.14685),
  s(t) = num(t)/NORM on [0,1/4].

Then num(0)=0 (since -c^P+c^P=0), s(0)=0, s(1/4)=1,
s'(t) = [(2/3)|t|^{-1/3}+(2/3)|t-c|^{-1/3}+1]/NORM > 0 on (0,1/4)\{c},
so s is continuous strictly increasing from 0 to 1 with integrable
singular slopes s'^2 ~ |t|^{-2/3}, |t-c|^{-2/3}. Define phi by mirror,
oddness, half-antisymmetry:

  phi(u)=s(u) on [0,1/4]; phi(u)=s(1/2-u) on [1/4,1/2];
  phi(u)=-s(u-1/2) on [1/2,3/4]; phi(u)=-s(1-u) on [3/4,1],

extended 1-periodically, Q*(t)=(0,phi(t)).

Properties: phi is odd, phi(u+1/2)=-phi(u), phi(1/2-u)=phi(u); hence
Q* satisfies k1,k2. phi>0 on (0,1/2) (minimum ~1.7e-4 on grid interior
away from endpoints), phi<0 on (1/2,1). COM sum vanishes identically by
half-antisymmetry. phi in H^1: at u=0,1/2 cusps ~|u|^{2/3} with
phi'^2 ~ |u|^{-2/3} integrable; at u=1/8,3/8,5/8,7/8 interior cusps
~|u-c|^{2/3}; at u=1/4,3/4 Lipschitz corners (finite left/right
derivatives). Kinetic integral is finite (K~34.6 at T=1).

Gap analysis. Write p_j(t)=phi(t+j/4). Gaps:
- m=2 (opposite): phi(t)-phi(t+1/2)=2phi(t) (by half-antisymmetry).
  Zeros iff phi(t)=0 iff t in {0,1/2} mod 1. Near 0,
  num(t)=t^{2/3}+O(t) (smooth in the second and third terms at t=0), so
  |gap| ~ 2 NORM^{-1}|t|^{2/3}. Similarly at 1/2. Hence 1/|gap| and
  phi'^2 ~ |t|^{-2/3}, integrable.
- m=1,3 (neighbours, e.g. D(t)=phi(t)-phi(t+1/4)): zeros at
  t=1/8,3/8,5/8,7/8 mod 1 (verified by monotonicity: on each of the eight
  length-1/8 subintervals D is strictly monotone — sum/difference of the
  strictly increasing s and its mirror — with endpoint values of opposite
  sign or zero, hence exactly one zero, located at the stated points; grid
  scan minima are 0 at t=0.125,0.375 for the four neighbour gaps and at
  0,0.25,0.5 for the opposite gaps). Near t=1/8, with h=t-1/8,
  s(1/8+h)-s(1/8-h) = NORM^{-1}[2(2/3)(1/8)^{-1/3}h + 2 sign(h)|h|^{2/3}]
  + O(h^2); since 2/3<1 the |h|^{2/3} term dominates, |D|~2NORM^{-1}|h|^{2/3}.
  Same at the other neighbour zeros by symmetry. Integrable as above.

Away from these points gaps are bounded away from zero and smooth, so U is
continuous there. Hence U(Q*) is integrable (U~15.7) and total action
finite: A=50.43 (N=200k midpoint, nodes avoid the measure-zero collision
set) vs 50.24 (N=80k), confirming integrability. This is the required
finite upper bound for the direct method. Log-log cusp fits give slopes
0.669 at both t=0 and t=1/8, i.e. 2/3 to 0.003.

## 5. Existence of a minimizer; obstruction for all T

F_T is a closed linear subspace of H^1 (symmetries are continuous linear
conditions on the continuous representative; COM likewise), hence weakly
closed. Oddness gives zero mean, so Poincare controls the H^1 norm by the
kinetic term: A[Q] -> +infinity as ||Q||_{H^1} -> infinity (coercive).
K is convex continuous, hence weakly lower semicontinuous; U>=0 and, under
H^1-weak convergence, uniform convergence gives pointwise convergence of
gaps a.e. (allowing +infinity at collisions), so int U <= liminf int U_n
by Fatou. Thus A_chor is weakly l.s.c. (extended-real).

Take a minimizing sequence with values approaching inf_{F_T} A <= A[Q*] < inf.
By coercivity it is H^1-bounded; extract a weakly convergent subsequence
with limit in F_T; l.s.c. gives a minimizer with finite action. This holds
for T=1 and hence every T>0: the symmetry conditions use only fractions of
the period, and the witness scales by Kepler similarity
Q_T(t)=T^{2/3}Q_1(t/T) (K and U integrals each scale as T^{1/3}, finite for
all T>0). Coercivity/l.s.c. are period-independent.

Since every Q in F_T has the forced collision q0(0)=q2(0)=0 of Section 3,
every minimizer is collisional. No collision-free minimizer exists in F_T,
and no element coincides with the Super-Eight or circle. This establishes
horn (ii) for all T>0 by scaling, completing the target dichotomy for the
stated class.

## 6. Computation (corroboration, not a substitute for proof)

Script `output/artifacts/check_obstruction.py` reproduces: symmetry
residuals (odd, Rx, half-antisymmetry) ~0 (<=2.1e-11), COM residual
~2.0e-11, gap-zero minima 0 at the six predicted instants, cusp slopes
0.669 (~2/3), finite action 50.43/50.24 at two resolutions, circle-oddness
residual 0.579 (exclusion witness). Output `check_results.json`. The proof
above is analytic; numerics only corroborate integrability and locations.

## 7. Limitations and scope

- The class F_T is one concrete admissible Klein-four non-Super-Eight class
  (collinear odd + Rx). The target's topology clause is satisfied by
  collinear exclusion; other Klein-four braid classes are not addressed.
- Only the obstruction horn is proved; no new collision-free choreography
  is claimed, and no Marchal–Chenciner-type collision exclusion is attempted
  (indeed exclusion must fail here by forced symmetry zeros).
- The minimizer's exact collision profile beyond the forced opposite-pair
  zeros is not classified; finiteness of its action follows from the upper
  bound, not from a Sundman analysis.
- Equal masses, planar motion, Newtonian potential, and zero COM/L are
  essential as stated.
