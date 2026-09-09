# Finite Hjorth-shadow data for odometer conjugacy on minimal Cantor
# homeomorphisms (lane-403)

## Theorem L1 (Local transitivity / finite Hjorth shadow — PROVED)
Let s_m(a) = a+1 mod 2^m (binary odometer pattern at level m),
V_m = {g in Sym(2^{m+1}) : g preserves mod-2^m blocks}
(fiber-swaps, |V_m| = 2^{2^m}). Then the V_m-conjugacy orbit of s_{m+1}
EQUALS the set of all single-cycle lifts of s_m to level m+1; both have
cardinality 2^{2^m - 1}.

Proof. Write atoms (c,e), c in Z_{2^m}, e in {0,1}, s_{m+1}(c,e) =
(c+1 mod 2^m, e + 1_{c = 2^m - 1}).
(Orbit size.) Stab_{V_m}(s_{m+1}): g in V_m determined by bits f(c) with
g(c,e) = (c, e + f(c)); g s = s g forces f constant (check c = 2^m - 1
carry), and constants commute with everything; the nontrivial constant
is s_{m+1}^{2^m}. So Stab = {id, s^{2^m}}, size 2, orbit = 2^{2^m}/2.
(Lifts.) A lift psi(c,e) = (s_m(c), e + f(c)) is bijective iff
e -> e + f(c) is bijective per c (always true) AND images across the two
preimage classes... (full detail in DRAFT.md): psi^{2^m}(c,e) =
(c, e + sum_b f(b)); single 2^{m+1}-cycle iff sum f is odd (else two
2^m-cycles). Exactly half of the 2^{2^m} lifts: 2^{2^m - 1}.
V_m-conjugates of the single cycle s_{m+1} are single cycles lifting s_m
(conjugation preserves cycle type and block quotient); equal finite sizes
give equality. QED.

Exact verification (replay: lane403_attack{6,8,10}.py):
- m=2: 8 U-cyclic lifts, V-orbit 8 distinct, equality (log6 B3).
- m=3: 128 lifts, V-orbit 128 distinct, lifts == orbit (log8).
- m=4: 32768 lifts = 2^15, V-orbit 32768 distinct, equality (log10).

## Lemma L2 (Twisted-product lift — PROVED, constructive)
Let M | N, K = N/M, tau a single M-cycle. Atoms (b,j), b in Z_M, j in Z_K.
psi(b,j) = (tau(b), j + 1_{b == b0}) (fixed b0). Then psi is a single
N-cycle with M-quotient tau.
Proof: psi^M(b,j) = (b, j+1) (each tau-step advances block; the fiber
+1 fires exactly once per M-block-tour since b0 is visited once); so
psi^M is the K-cycle on fibers x identity on blocks, psi permutes the M
blocks cyclically: order of psi is M*K = N, single cycle. Quotient is tau
by construction.
Verification (replay: lane403_attack12.py, finite_level_log12.json):
exhaustive all taus for M <= 6 (1, 2, 24, 120, 6 taus), sampled 12/12 for
M in {10, 15, 8}; 12/12 divisor pairs (M,N) incl. 8|32: ALL OK.
Corollary: the pure-odometer N-pattern (any single N-cycle) is S_N-
conjugate to psi, so some g in Homeo(2^N) sends the odometer pattern to a
pattern with prescribed cyclic M-quotient: the odometer H-orbit meets every
cyclic-factor basic open at divisor levels (finite density shadow).

## Proposition P3 (Eigenvalue density obstruction — PROVED mod standard facts)
(a) A p-cyclic clopen partition (B_j, psi(B_j) = B_{j+1}) gives Koopman
eigenvalue zeta_p = e^{2pi i/p} via f = sum_j zeta_p^{-j} 1_{B_j};
eigenvalues are conjugacy invariants.
(b) The binary odometer has eigenvalue group {2-power roots of unity} only:
finite shadow — a cyclic quotient of a single 2^n-cycle has order | 2^n
(divisor table log6), and 2^n mod 3 != 0 for all n (log4).
(c) Hence no binary-odometer-type point can be the dense-orbit turbulent
witness: its H-orbit is constrained in eigenvalue data. The target's phi*
must be eigenvalue-universal yet non-odometer (e.g. Toeplitz almost-1-1
extension of the universal odometer). Naive coherent twists fail: all 60
same-fiber single-swaps break the 30-cycle (log9) — recorded constraint.

## What is NOT claimed
- NOT Hjorth turbulence of any point; NOT density of any H-orbit in M;
  NOT generic E0-ergodicity; NOT non-Borel-reducibility. Finite-level
  shadows only; the infinite-level transfers are open.
- U_3 "missed basic open" claims from v4/v5 are WITHDRAWN (fiber-swap
  error); corrected enumeration (log7) shows level-2 reach complete (6/6).

## Replay
python3 lane403_attack6.py lane403_attack8.py lane403_attack10.py
lane403_attack12.py (stdlib only) from output/artifacts/.
Logs: finite_level_log{6,8,10,12}.json (+{3,4,7,9,11} exploratory).
