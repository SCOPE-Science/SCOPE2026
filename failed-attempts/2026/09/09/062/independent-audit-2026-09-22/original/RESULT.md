# No Liouvillian solution at Heun accessory point q*=7/5 — certified Kovacic elimination with replayable log

## Context
Heun functions are the recognized next transcendental tier above the hypergeometric family. Deciding Liouvillian (non-)existence for a named Heun equation is the standard progress unit for symbolic-solver testing (Kovacic's algorithm is the decision procedure, DLMF 31.14(ii)) and for anchoring irreducibility in Heun application models (DLMF 31.17). The target was a full SL(2,C) density certificate plus a Liouvillian neighbor; investigation proved the neighbor clause impossible (all Kovacic local data q-independent), so the claimed result is the admitted preset fallback: the exact non-Liouvillian certificate at q*=7/5.

## Definitions
Operative equation (as written, by explicit coefficients):
y'' + (1/x + (1/2)/(x-1) + (1/2)/(x-2)) y' + ((x/3 - q)/(x(x-1)(x-2))) y = 0,
i.e. singularities {0,1,2,infinity}, a=2, gamma=1, delta=epsilon=1/2, accessory parameter q, named point q*=7/5. SL(2) normal form u''=r u with r=P'/2+P^2/4-Q, P=1/x+(1/2)/(x-1)+(1/2)/(x-2), Q=(x/3-q)/(x(x-1)(x-2)), u=rho y, rho=exp(int P/2). "Liouvillian solution" means expressible in finite terms (Kovacic 1986 sense). Kovacic cases 1/2/3 = reducible-Borel / dihedral / finite-primitive (A4/S4/A5) necessary-condition stages.

## Result
At q*=7/5, Kovacic cases 1, 2, and 3 each terminate with no admissible solution. Hence the equation has no Liouvillian solution over C(x). The complete exact-rational elimination log replays with binary pass/fail (artifacts/fallback_replay.py -> FALLBACK_REPLAY_OK, exit 0).

## Proof / evidence
Normal form, exact over Q: r=N/D, D=48x^2(x-1)^2(x-2)^2, N=-16x^4+(48+48q)x^3+(-65-144q)x^2+(72+96q)x-48; q-dependent part 48q x(x-1)(x-2) (symbolically verified). At q*=7/5: N(0)=-48, N(1)=-9, N(2)=-36 (all nonzero, poles 0,1,2 exact order 2); deg N=4 with q-free lead -16, so ord_inf(r)=6-4=2. Local data (coeffs of (x-c)^{-2}): b0=-1/4, b1=b2=-3/16, b_inf=-1/3, i.e. sqrt(1+4b) in {0,1/2,1/2,i/sqrt3}. Case 1: alpha0=1/2; alpha1,2 in {3/4,1/4}; alpha_inf=(1+-i/sqrt3)/2 nonreal; every d=alpha_inf-S (S real, 8 branches) has Im(d)=+-1/(2sqrt3)!=0, never in Z>=0. Case 2: E0={2}, E1=E2={1,2,3}, E_inf={2}; all 9 tuples give d=(2-2-e1-e2)/2<=-1<0. Case 3 (Kovacic-1986 E={(6+k rho)/n,|k|<=n/2} cap Z): n=4: E0={3/2} empty; n=12: E0={1/2} empty; n=6: E={1} at every point, d=(6/12)(1-3)=-1<0. A generous |k|<=12 sweep admits one extra n=6 tuple (1,0,0,1), d=0, killed exactly by the degree-0 P-recurrence (P6+1 = nonzero degree-14 polynomial) — robustness only. Kovacic's algorithm being a complete decision procedure (Kovacic 1986; DLMF 31.14(ii)), and rho^4=x^2(x-1)(x-2) in C(x) (algebraic, Liouvillian-preserving twist), the y-equation has no Liouvillian solution at q*=7/5. Cross-checks: DLMF 31.2 E3-E4 coefficients A=13/40,B=-113/120,C=37/60,D,E,F=(-1/4,-3/16,-3/16) coincide identically with direct partial fractions; full branch enumeration; Frobenius log-witness at x=0. Full suite: replay_all.sh -> REPLAY_ALL_OK.

## Limitations
Fallback only: no SL(2,C) Zariski-density upgrade and no reducible neighbor q_red (the latter proved impossible in this family — all Kovacic local data are q-independent since the q-part vanishes at 0,1,2 and is O(x^{-3}) at infinity, so cases 1/2/3 die for every q). The computation uses the written numerator x/3-q (true infinity-exponents (1+-i/sqrt3)/2); the topic's (1/3,2/3) labels would require 2x/9. The true-Heun 2x/9 variant was checked separately and dies identically (b_inf=-2/9, rho=1/3; case 1 six d's inadmissible, case 2 d<0, case 3 n=4 empty / n=12 empty / n=6 d=-1). No automated Kovacic oracle in installed sympy; elimination hand-checked against Kovacic-1986 E-set formulas with generous-k sweep.

## Reproducibility
stdlib-only (plus sympy for the exotic-kill robustness script): python3 artifacts/fallback_replay.py -> FALLBACK_REPLAY_OK; python3 artifacts/case12_enumeration.py -> CASE12_ENUM_OK; python3 artifacts/kovacic_uniform.py -> KOVACIC_UNIFORM_OK; python3 artifacts/dlmf_crosscheck.py -> DLMF_CROSSCHECK_OK; python3 artifacts/kovacic_trueheun_check.py -> TRUE_HEUN_UNIFORM_OK; python3 artifacts/case3_exotic_kill.py -> EXOTIC_KILL_OK.

## References
Kovacic, J. Symb. Comp. 2 (1986) 3-43; DLMF sections 31.2, 31.5, 31.8, 31.14; Ronveaux (ed.), Heun's Differential Equations (1995); Maier, Math. Comp. 76 (2007) (192 solutions); Acosta-Humanez et al., arXiv:1104.0312 (different Heun equation, method precedent only); van der Put-Singer, Galois Theory of Linear Differential Equations (2003).
