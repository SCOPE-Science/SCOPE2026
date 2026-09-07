# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# L-membrane first Dirichlet eigenvalue: rigorous wide enclosure, sharp conforming upper bound, and a self-contained Kato flux lemma
## lane-20 technical note (partial result; NO tightening claimed)

### 1. Normalization and references
Let `Omega_L` be the L-polygon with CCW vertices
`(0,0),(2,0),(2,1),(1,1),(1,2),(0,2)`, area `|Omega_L|=3`,
one re-entrant corner of angle `3pi/2` at `(1,1)`.
Let `lambda1` be the lowest eigenvalue of `-Delta` on `H0^1(Omega_L)`.
Non-rigorous MPS reference (Betcke–Trefethen, SIAM Rev. 2005):
`lambda1 ~ 9.63972384402` (12 digits quoted, no enclosure).
Faber–Krahn disk floor (area 3): `lambda1 >= pi*j01^2/3 ~= 6.05` (made explicit below).

Prior rigorous context (survey, offline): Fox–Henrici–Moler (1967) two-sided
inclusions for the L-membrane of width `O(1e-02..1e-01)`; Carstensen–Gedicke
(Math. Comp. 2014) guaranteed lower bounds (one-sided, not a tight two-sided
enclosure at `5e-04`); Liu–Oishi frameworks give verified bounds but no published
`<=5e-04` closed interval for this size-2 normalization was found in triage.
**This note does NOT tighten any of these**: its closed interval has width
`~3.59`. It records a sharp rigorous conforming upper bound, an exact-rational
Faber–Krahn floor, a reusable Kato lemma, and a rerunnable benchmark.

### 2. What is proved vs computed (separation)
- **PROVED (rigorous):** Theorem U (conforming upper bound `lambda1 <= 9.643856`);
  Theorem L0 (Faber–Krahn floor `lambda1 >= 6.0561` with exact-rational Bessel/pi
  bounds); Lemma GAP (square monotonicity `lambda2(Omega_L) >= 5pi^2/4 > 12.33`);
  Lemma KATO (flux-based lower bound from `H^{-1}` residual + gap, self-contained proof).
- **COMPUTED (non-rigorous approximations, clearly labeled):** P1 Ritz values
  `9.96597665 (N=16), 9.74081708 (N=32), 9.67295071 (N=64), 9.65120311 (N=128),
  9.64600950 (N=192), 9.64385398 (N=256)`; averaged-flux residuals
  (`eta ~ 2.3..3.3`, bound vacuous — reported as a negative result).
- **CONJECTURE (not proved):** `lambda1 = 9.63972384402...` (MPS, quoted).
- **UNCERTAINTY:** none in U/L0 beyond stated rounding margins (explicit);
  Kato lemma is valid but not usefully tight with the tested flux.

### 3. Theorem U (rigorous conforming upper bound)
**Theorem.** `lambda1(Omega_L) <= U := 9.643856`.
*Proof.* Min-max: for any nonzero `v in H0^1`, `lambda1 <= R(v)=||grad v||^2/||v||^2`.
Take `v_h` = P1 conforming FEM function on the uniform `N=256` triangulation
(`h=2/256`, `49665` nodes, `98304` triangles, `48641` free dofs), coefficients `x`
from inverse iteration (any `x` works; convergence is irrelevant to validity).
The mesh is exact: `N` even so element edges align with `x=1`, `y=1`; every
triangle lies wholly inside or outside `Omega_L`; no variational crime.
Stiffness entries are dyadic-exact in binary64: nodes are multiples of
`2^-7`, `b,c` differences exact, `b_i b_j+c_i c_j` and `4A` are dyadic with
`4A=2^-13` so division is an exact exponent shift. Mass entries `A/12*{2,1,1}`
incur at most `0.5 ulp` each. Let `Nhat,Dhat` be float64 evaluations of
`x^T A x`, `x^T M x`: `Nhat=9.6438539766`, `Dhat=1.0`.
Higham forward bounds with `eps=2^-52`, row `nnz<=7`, `n=48641`:
`dN=(gamma7+gamman+...)*SA=1.42e-06` (`SA=131076.55`),
`dD=(eps/2)*SM+...=1.08e-11` (`SM=1.0`).
Hence true `R <= (Nhat+dN)/(Dhat-dD) = 9.643855393 < 9.643856 =: U`. ∎
Rerun: `output/artifacts/verify_bounds.py` recomputes assembly from
`mesh_N256.npz` + `P1_N256_rayleigh.npz` in `~1 s` (numpy 1.26.4, python 3.12.3).

### 4. Theorem L0 (exact-rational Faber–Krahn floor)
**Theorem.** `lambda1(Omega_L) >= 6.0561`.
*Proof.* Quote Faber–Krahn: `lambda1(Omega) >= pi*j01^2/|Omega|` (`|Omega|=3`).
It remains to show `j01 > 2.40482` and `pi > 3.14159` by exact rational arithmetic.
(a) `J1(x)>0` on `(0,2.41]`: `J1(x)=sum (-1)^k t^{2k+1}/(k!(k+1)!)`, `t=x/2<=1.205`;
ratios `t^2/((k+1)(k+2)) <= 1.4521/2 < 1` for all `k>=0`, so Leibniz applies and
`J1(x) >= t-t^3/2 = t(1-t^2/2) > 0` (as `t^2<2`). Hence `J0'=-J1<0`, `J0`
strictly decreasing there, at most one zero.
(b) `J0(2.40482)>0`: `J0=sum (-1)^k a_k`, `a_k=(x0^2/4)^k/(k!)^2`,
`x0=120241/50000`, `q=x0^2/4=1.4457898081<1.46`; ratios `q/(k+1)^2<1` for `k>=1`,
Leibniz from `k>=1` gives `J0 >= S12-a13 = 2.8852671851e-06 > 0` (exact
`Fraction` arithmetic, remainder `3.1e-18`). Thus no zero in `[0,2.40482]`,
`j01>2.40482`.
(c) `pi>3.14159` by Machin `pi=16 arctan(1/5)-4 arctan(1/239)` with alternating
bounds (12 and 4 terms; ratios `<1` since `x<=1/5`); exact `Fraction` check gives
`pi_lo=3.14159265...>3.14159`.
Hence `lambda1 >= 3.14159*2.40482^2/3 = 6.05610507... >= 6.0561`. ∎
Script: `work/fk_exact.py` (pure `Fraction`, no floats).

### 5. Lemma GAP (verified spectral gap for Kato condition)
**Lemma.** `lambda2(Omega_L) >= 5pi^2/4 > 12.33`.
*Proof.* `Omega_L subset [0,2]^2`; extension by zero embeds
`H0^1(Omega_L) hookrightarrow H0^1(Box)` isometrically, so min-max gives
`lambda_k(Omega_L) >= lambda_k(Box)` for all `k`. Box eigenvalues
`(pi^2/4)(m^2+n^2)`: `lambda2(Box)=5pi^2/4`. With `pi>3.14159`,
`5pi^2/4 > 12.336 > 12.33 =: nu`. Since `U=9.643856 < nu`, `mu<nu` holds for our
trial functions. ∎

### 6. Lemma KATO (self-contained H^{-1} lower bound) + honest negative test
**Lemma.** Let `||v||_{L2}=1`, `mu=||grad v||^2`, `r(phi)=(grad v,grad phi)-mu(v,phi)`,
`||r||_{-1} <= eta`. Let `nu<=lambda2`, `mu<nu`, `eta<(nu-mu)/sqrt(nu)`. Then
`(mu-lambda1)^2/lambda1 <= eta^2`, i.e. `lambda1 >= mu-eta*sqrt(mu)`
(tighter quadratic root available).
*Proof.* Eigen-expand `v=sum c_k u_k`, `sum c_k^2=1`, `mu=sum c_k^2 lambda_k`.
Dual norm: `||r||_{-1}^2 = sum (lambda_k-mu)^2 c_k^2/lambda_k =: sum g(lambda_k)c_k^2`
(Cauchy–Schwarz on `(lambda_k-mu)c_k/sqrt(lambda_k)` against `sqrt(lambda_k)d_k`).
`g(l)=(l-mu)^2/l` increases for `l>mu` (`g'=(l-mu)(l+mu)/l^2>0`), so for `k>=2`,
`g(lambda_k)>=g(nu)=:B`. Hence `eta^2 >= A t + B(1-t)` with `A=(mu-lambda1)^2/lambda1`,
`t=c_1^2`. If `eta^2<B` then `min(A,B)<=eta^2<B`, forcing `A<=eta^2`. ∎
Flux majorant: for any `q in H(div)`, `eta := ||grad v-q|| + C_P||div q+mu v||`
with `C_P=1/sqrt(L0)` bounds `||r||_{-1}` (integrate by parts; boundary term
vanishes as test functions are in `H0^1`).
*Negative result (honest):* with P1 Ritz `v` + area-weighted averaged `q`,
`e1=0.59,0.33,0.19,0.11` but `e2=4.2,5.0,6.2,7.8` (`N=16..128`), `eta~2.3..3.3`,
bound vacuous (`mu-eta sqrt(mu)` negative). Simple averaging is NOT equilibrated
(`div q` far from `-mu v`); an RT-equilibrated flux is needed (roadmap). The lemma
stands; its hypothesis is not met tightly by this flux.

### 7. Convergence table (P1 uniform, computed evidence, non-rigorous except N=256 U)
| N | h | nodes | tris | free | Ritz `lambda_h` |
|---|---|---|---|---|---|
| 16 | 0.125 | 225 | 384 | 161 | 9.96597665 |
| 32 | 0.0625 | 833 | 1536 | 705 | 9.74081708 |
| 64 | 0.03125 | 3201 | 6144 | 2945 | 9.67295071 |
| 128 | 0.015625 | 12545 | 24576 | 12033 | 9.65120311 |
| 192 | 0.010417 | 28033 | 55296 | 27265 | 9.64600950 |
| 256 | 0.0078125 | 49665 | 98304 | 48641 | 9.64385398 (-> U=9.643856 rigorous) |
Observed eigenvalue ratios `~3.2-3.5` per doubling (order `~1.7`).
Graded red-green tests (base N=16 + corner patches) gave `9.6976/9.6842` at
`1167/1836` dofs — no win over uniform at equal dofs because the base was too
coarse globally; proper `N=64`-base grading was not completed in time.

### 8. Gap-to-conjecture and prior-width comparison
`[L0,U]=[6.0561, 9.643856]`, width `3.5878`, contains MPS `9.63972384402`
(`L0<=MPS<=U` verified). `U-MPS=0.00413` (upper alone is within `5e-03` of the
conjectured value, but two-sided width is not). Prior rigorous two-sided
FHM widths `O(1e-02)` are an order of magnitude TIGHTER than `3.59`;
Carstensen–Gedicke is one-sided. Hence **no tightening is claimed**; re-check of
prior widths confirms this note does not beat them.

### 9. Limitations and roadmap
- Lower bound is the bottleneck: FK floor is far from sharp; naive-flux Kato is
  vacuous (`eta` diverges in `e2`); Lehmann–Goerisch with equilibrated RT flux
  (or CR lower bound with verified discrete eigenvalue, or Trefftz–Lehmann with
  small dense interval algebra) is the required next step, not completed.
- Corner grading did not improve on uniform in the tested regime; P2 and
  RT-equilibration were not implemented in the time budget.
- `verify_bounds.py` reruns in `~1 s`; full eigensolve (`work/sparse3.py`,
  N=256) takes `~18 s`; all within `<10 min`.

### 10. Artifact inventory (output/artifacts/)
- `mesh_N256.npz` (coords, tris; uniform N=256, exact-domain)
- `P1_N256_rayleigh.npz` (eigenvector `x`, `Nhat/Dhat/SA/SM/dN/dD/U`, `free`)
- `P1_N32.npz` (small-matrix benchmark: COO A/M, mesh, `free`, Ritz value)
- `verify_bounds.py` (self-contained rerun: assembly + Rayleigh/rounding + exact
  FK + containment/width checks; tested `0.9 s`)
Generation/assembly scripts: `work/sparse1.py`, `work/final_upper.py`,
`work/fk_exact.py`, `work/fluxtest.py`, `work/proto5.py`, `work/runB.py`.

### References
Betcke–Trefethen SIAM Rev. 2005 (MPS 9.63972384402); Fox–Henrici–Moler
SIAM J. Numer. Anal. 1967 (two-sided inclusions); Carstensen–Gedicke
Math. Comp. 2014 (guaranteed lower bounds); Liu–Oishi verified eigenvalue
frameworks (background for Lehmann–Goerisch/M_h, not directly used for the
claimed interval); Chavel/Henrot for Faber–Krahn (quoted).
