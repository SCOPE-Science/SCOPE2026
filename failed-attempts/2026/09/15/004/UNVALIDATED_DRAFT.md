# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Pressure gap and uniqueness of equilibrium states for geometric potentials
# on the Zorich suspension coding the Teichmüller flow
# (Repaired submission — auditor points (1)–(4) addressed, pressure-gap core intact)

## Abstract
Fix a Rauzy class / stratum component H (genus g >= 2) with the
Bufetov–Gurevich countable Markov coding (Sigma,sigma) of Zorich
induction and roof r suspending to the Teichmüller flow (Sigma_r,Phi^t).
Let phi_geom be the geometric unstable-Jacobian potential on the
suspension and J(x)=int_0^{r(x)} phi_geom dt its induced base increment.
We prove there is delta>0 such that for |t|<delta, t != 0, with s(t)
the unique root of p(t,s)=P_G(tJ-sr)=0,
P_infty(tJ-s(t)r) <= -kappa < 0 = P_G(tJ-s(t)r)
(i.e. P_bad < P_full), and hence t*phi_geom has a unique equilibrium
state, distinct from the Masur–Veech / Bufetov–Gurevich MME.
Repair vs prior draft: (1) the SPR/conformal/IFT machinery is now run
explicitly on an induced Bernoulli (full) Young base Y_w with stated
distortion/summable-variation bounds, while the tail upper bound stays
on the full shift where no BIP is needed; (2) the h>1 claim is proved in
the roof normalization via F(1)=infinity; (3) continuity/IFT for p(t,s)
is justified by uniform tail summability for s-prime>1; (4) distinctness
uses two explicit periodic-loop matrices with computed J/r ratios.

## 1. Full shift vs induced Bernoulli shift (addresses auditor point 1)

**Full BG shift.** (Sigma,sigma) is a topologically mixing countable
Markov shift; alphabet A indexes maximal Zorich blocks; roof
r: Sigma -> (0,infty) satisfies inf r = r_min > 0, r unbounded, and
Lemma 1 below. We do NOT assume BIP or summable variations on the full
shift, and nothing in Sections 2–3 needs them.

**Induced Bernoulli base.** Fix a good bounded Zorich symbol w0 (small
Rauzy length, in the mixing finite core F={n(a)<=N0}) and put
Y=[w0] (a 1-cylinder). Let tau>=1 be the first return time to Y and
(Sigma_hat,sigma_hat) the induced countable full shift (Bernoulli) over
return words e; fullness (= BIP with constant 1) holds by construction
(Young tower base, Marmi–Moussa–Yoccoz / Bufetov–Gurevich inducing;
called Y_w in the literature). Write
  R = S_tau r (induced roof),  Jbar = S_tau J (induced increment),
sums over the excursion. Return words that ever visit large symbols
correspond to cusp excursions; words staying in F are the compact core.

**Regularity on the induced shift (explicit bounds).** The only
properties of (J,r) used are, with constants depending only on the
Rauzy class and w0:
  (a) |J| <= K r on Sigma, osc_{[a]}(r) <= C0, osc_{[a]}(J) <= C_J
      per full-shift 1-cylinder (bounded phi_geom + BG distortion,
      BG Lemma 3);
  (b) inherited: |Jbar| <= K R, and sup_e osc_e(R) <= C_dist,
      sup_e osc_e(Jbar) <= C_dist' (telescoped BG distortion; each
      excursion branch of the Zorich projective map has uniformly
      bounded Jacobian distortion on Y);
  (c) summable variations: Var_k(R), Var_k(Jbar) <= C_1 theta^k for
      some C_1<infty, theta in (0,1) (uniform expansion of Zorich
      induction on the compact core in the Hilbert projective metric;
      contraction factor theta=tanh(Delta/4)<1; cite BG + Avila–
      Gouëzel–Yoccoz). Hence sum_k Var_k < infty, uniformly for
      (t,s) in compacts via Var_k(tJbar-sR) <= |t|Var_k(Jbar)+|s|Var_k(R).
All SPR/conformal/pressure-analyticity arguments (Sections 5–6) run on
(Sigma_hat,sigma_hat), where Sarig's BIP theory applies verbatim.
Results transfer to (Sigma,sigma) and the flow by Kac/Abramov +
Jaerisch–Takahashi / Climenhaga–Thompson inducing criteria ( давления
at infinity and SPR are preserved under inducing with exponential-tail
return times, which SPR itself gives; see Section 6).

**Division of labour (stated once).** Tail upper bounds (Lemma 2):
full shift, no BIP. Existence/uniqueness/analyticity/IFT (Sections 5–6):
induced Bernoulli shift, then lifted. This fixes the BIP/regularity gap.

## 2. Combinatorial tail lemma (pressure-gap core, unchanged)

**Lemma 1 (Zorich tail).** There are D>=1, C0 with: full-shift
1-cylinders partitioned by Rauzy length n(a)>=1, at most D letters per
n, and |r|_{[a]} - log(n(a)+1)| <= C0. Moreover for each n>=1 there is
at least one letter with Rauzy length exactly n. (Upper bound: finitely
many winner/loser/combinatorial types, Dehn-twist matrix I+nE, Zorich
time = log mass growth; BG Lemma 3 for distortion/roof asymptotics.
Lower bound: n-fold repeat of a fixed winner on a balanced permutation
before switching, realized in every Rauzy class; Zorich/Rauzy.)
Hence for s>1, c real,
  T_N(s,c) := sum_{n(a)>=N} exp(sup_{[a]}(-sr+c))
           <= D e^{c+sC0} sum_{n>=N} n^{-s} -> 0.
Mechanism: r~log n turns Gibbs weights e^{-sr} into p-series weights
n^{-s}; s>1 gives arbitrarily small tail mass.

**Lemma 2 (cusp pressure upper bound; no BIP needed).** For
Sigma_N = subshift with n(a)>=N and any potential Phi,
  P_G(Sigma_N,Phi) <= log sum_{n(a)>=N} e^{sup_{[a]} Phi}.
Proof: period-k points are admissible words; sup S_k Phi <= sum sup Phi
(up to distortion absorbed in sup); Z_k <= (sum e^{sup Phi})^k;
(1/k)log Z_k gives the bound; inadmissibility only lowers Z_k. ∎

## 3. Roof-normalized proof that h > 1 (addresses auditor point 2)

Let p(t,s)=P_G(tJ-sr) (full shift) and F(s)=sum_a exp(-s inf_{[a]} r).
By Lemma 1 lower bound + BG Lemma 3,
  F(1) >= sum_{n>=1} e^{-(log(n+1)+C0)} = e^{-C0} sum_n 1/(n+1) = infty.
So the first partition sum diverges at s=1. Transfer to the induced
Bernoulli shift: fix base symbol w0; two-step induced loops w0->a->w0
range over all large a with uniformly bounded connector cost (mixing),
so the induced return partition sum Zbar_1(0,1)=infty as well; for a
countable full shift Sarig's Z_2 argument gives induced pressure
p_hat(0,1)=+infty (the sum over middle symbols diverges). By
Jaerisch–Takahashi pressure preservation under inducing,
p(0,1)=+infty on the full shift too. In particular p(0,1)>0.

Black boxes used in the same roof normalization r (no rescaling):
(i) the Teichmüller flow on H has finite topological entropy
H_flow<infty (Eskin–Masur; same Zorich-time normalization as BG roof);
(ii) Barreira–Schmeling / Jaerisch et al.: s -> p(0,s) is continuous
strictly decreasing on {p<infty}, and its unique zero is H_flow, i.e.
p(0,H_flow)=0. Since p(0,1)=+infty>0=p(0,H_flow) and p is strictly
decreasing where finite, the zero satisfies h := H_flow > 1.
We set h=h_top(Phi^t|_H)>1 in this normalization, so P_G(-hr)=0.
This replaces the prior scale-dependent Lyapunov-sum claim entirely.

Finiteness for s>1 (needed for continuity domain): at t=0,
Z_1(0,s) <= D e^{sC0} zeta(s) < infty for s>1 by Lemma 1; on the BIP
induced shift finite Z_1 + summable variations => p_hat(0,s)<infty
(Sarig), transferred to p(0,s)<infty. So [1+eps,infty) lies in the
finite-pressure domain for every eps>0.

## 4. Pressure gap at t = 0

Apply Lemma 2 with Phi=-hr, h>1:
  P_G(Sigma_N,-hr) <= log T_N(h,0) -> -infty (N->infty).
Hence P_infty(-hr) = lim_N P_{n>=N} <= lim_N log T_N = -infty
< 0 = P_G(-hr). Fix N large with P_{outside F}(-hr) <= -2kappa<0,
F={n<N} (finite union of cylinders = compact). "Bad segments with
r>=log N" are {n>=N}; their pressure is -infty by the convergent
p-series. No BIP used.

## 5. Persistence, continuity and IFT (addresses auditor point 3)

With |J|<=Kr and per-cylinder oscillation <=C_J,
  sup_{[a]}(tJ-sr) <= -(s-|t|K) inf_{[a]}r + |t|C_J' ,
so with s':=s-|t|K,
  sum_{n(a)>=N} e^{sup(tJ-sr)} <= e^{|t|C_J'} T_N(s',0)
    <= D e^{|t|C_J'+s'C0} sum_{n>=N} n^{-s'}.
Uniform tail summability: for Rect = {|t|<=t0, s in [s_-,s_+]} with
s'_- := s_- - t0 K > 1, Weierstrass M-test with M_n = const*n^{-s'_-}
gives uniform convergence and
  sup_{Rect} tail_N -> 0 (N->infty),
with an explicit majorant D e^{t0 C_J'+s_+ C0} sum_{n>=N} n^{-s'_-}.
Fix the N from Section 4; shrinking t0,|s-h| gives, for the same F,
  P_{Sigma\F}(tJ-sr) <= -kappa  on Rect (upper bound needs no BIP;
  same estimate holds for induced return words with (C0,C_J) replaced
  by (C_dist,C_dist') and an extra bounded-connector factor).

Continuity/analyticity: on the induced Bernoulli shift, (t,s) in Rect
satisfies uniform summable variations (Section 1(c)) + uniform Z_1 bound
+ uniform tail bound with s'_->1 (equi-SPR). Sarig's perturbation
theorem + Jaerisch–Munday–Takahashi analyticity for SPR potentials give
that (t,s) -> p_hat(t,s) is continuous (indeed analytic) on Rect, with
Ruelle derivative d/ds p_hat = -int R d mu_{t,s} <= -r_min < 0
(SPR Gibbs state mu_{t,s}; derivative formula of Sarig–Jaerisch).
Transfer to full-shift p(t,s) preserves continuity and the sign of the
s-derivative (Kac: int R d mu_hat = int r d mu / mu(Y) form).
Since p(0,h)=0, the implicit function theorem yields unique analytic
s(t) near h with p(t,s(t))=0 for |t|<delta1, and with the F from above,
  P_infty(tJ-s(t)r) <= -kappa < 0 = P_G(tJ-s(t)r),
i.e. P_bad < P_full for |t|<delta (also at t=0). Finiteness near (0,h)
is Z_1(t,s) <= const*zeta(s')<infty. delta depends only on
h-1, K, D, C0, C_J (resp. induced constants). This justifies
continuity/IFT under |J|<=Kr.

## 6. Unique equilibrium via SPR + suspension (on Y_w, then lifted)

For |t|<delta, Phi_t := tJ-s(t)r (resp. induced tJbar-s(t)R) satisfies
P_infty < P_G = 0 < infty: strong positive recurrence on the BIP
induced shift. By Sarig / Buzzi–Sarig, the induced potential has a
unique Gibbs/equilibrium measure mu_hat_t (conservative conformal +
invariant; exponential tails for R, so int R d mu_hat_t < infty);
every equilibrium is Gibbs. Kac/Abramov lifts mu_hat_t to a base
equilibrium mu_t on Sigma with int r d mu_t < infty, then to a
flow-invariant nu_t on Sigma_r with
  h_{nu_t}+t int phi_geom d nu_t = s(t) = P_flow(t phi_geom),
and any flow equilibrium projects ( muro(Y)>0 by SPR) to an induced
equilibrium, hence equals nu_t. This is the Climenhaga–Thompson /
Jaerisch flow criterion (P_bad<P_full => unique lift). Existence uses
BIP + finite pressure on the induced shift only. No Dolgopyat estimate
needed for uniqueness.

## 7. Distinctness: explicit periodic witnesses (addresses auditor point 4)

Livsic criterion: J is cohomologous to c*r (Hölder coboundary) iff all
periodic orbits have J(gamma)/r(gamma)=c. We give two periodic orbits
with different ratios, as return words on the induced Bernoulli shift
(fullness => every concatenation admissible; primitivity certifies the
pseudo-Anosov periodic Teichmüller geodesic; BG roof = log PF
eigenvalue, geometric increment = sum of expanding logs of the total
Rauzy matrix = periodic KZ/unstable-Jacobian data, Forni/KZ/AGY; for
exact closed loops there is no O(1) ambiguity).

Fixed connectors (in the finite BIP core):
  Lp = [[1,0,0,1],[1,1,0,1],[0,1,1,0],[0,0,1,1]],
  Rp = [[1,1,1,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]],
B(n) = I + n E_{14} (n-fold top-winner Dehn twist), M(n) = Lp B(n) Rp.
Both M(1), M(200) have det 1 and M^8 strictly positive
(min M(1)^8 = 1628, min M(200)^8 = 19140), hence Perron–Frobenius
primitive (admissible periodic loops e_1, e_200; e_1 bounded, e_200
with one deep Dehn-twist block + bounded connectors, legal by
full-shift property). Matrices:
  M(1)   = [[1,1,1,2],[1,2,2,2],[0,1,2,0],[0,0,1,1]],
  M(200) = [[1,1,1,201],[1,2,2,201],[0,1,2,0],[0,0,1,1]].
Eigenvalue moduli (numpy, artifact periodic_witnesses.py):
  n=1:   |eigs| = [3.974449, 1.290944, 1.290944, 0.150976],
         R_1 = log PF = 1.379886, S_1 = sum_{|mu|>1} log|mu| = 1.890633,
         rho_1 = S_1/R_1 = 1.370137;
  n=200: |eigs| = [7.989366, 5.089539, 5.089539, 0.004832],
         R_200 = 2.078111, S_200 = 5.332486, rho_200 = 2.566025.
Hence rho_200 - rho_1 = 1.195888 >> 0 (numerical error <1e-6; eigenvalue
separation from 1 exceeds 0.29, so the expanding count k=3 is robust).
So J/r takes two distinct periodic values; J is not cohomologous to
c*r for any c (for each c at least one witness differs by >0.5).

Consequences (Gouëzel–Sarig variance criterion + Ruelle formula):
sigma^2 := lim_n (1/n) Var_{mu_0}(S_n(J-c r)) > 0 (zero variance iff
coboundary), s''(0) = sigma^2 / int r d mu_0 > 0: s(t) strictly convex
near 0. If nu_t = nu_0 for arbitrarily small t != 0, the free energy
t -> h_{nu_0}+t int phi d nu_0 - s(t) would vanish to second order,
contradicting sigma^2>0. Thus nu_t != nu_0 (= MME of Bufetov–
Gurevich) for small t != 0. The new equilibrium is distinct from MME.

Recomputation: output/artifacts/periodic_witnesses.py prints the above
matrices, dets, primitivity minima, eigs, R/S/rho. Intermediate n
(2,5,10,20,50) show monotone rho growth 1.46→2.27, confirming the
mechanism (shear eigenvalue growth) rather than a one-off accident.

## 8. Conclusion

There is delta>0 (through D,C0/C_dist,K,h-1) with, for |t|<delta,
t != 0: P_bad(overline{phi}_t) < P_full(overline{phi}_t) (P_infty<P_G
with margin -kappa), and t phi_geom has exactly one equilibrium state
for the suspension (hence Teichmüller flow on H), distinct from MME. ∎

## References (black-box citations, not re-proved)
Bufetov–Gurevich (coding, mixing, BG Lemma 3 distortion/roof);
Sarig, Buzzi–Sarig, Ruette (Gurevich pressure, SPR, Gibbs);
Barreira–Schmeling, Jaerisch–Munday–Takahashi, Jaerisch et al.,
Climenhaga–Thompson (suspension reduction, inducing preservation,
flow criterion); Avila–Gouëzel–Yoccoz, Avila–Gouëzel, Forni,
Kontsevich–Zorich, Eskin–Masur (uniform hyperbolicity on compacta,
Hilbert contraction, finite flow entropy, KZ periodic data);
Veech, Zorich, Rauzy, Marmi–Moussa–Yoccoz (induction combinatorics,
Young/Bernoulli inducing); Gouëzel–Sarig (variance/coboundary),
Ruelle (pressure derivatives), Livsic (periodic cohomology).
