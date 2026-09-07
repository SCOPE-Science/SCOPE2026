# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact spectral gaps for 4-regular dicyclic Cayley graphs and their Schreier quotients via two-dimensional interlacing and trace checks

**Lane-03 draft — self-contained note. Status: claimed partial/complete theorem with machine audit.**

## Abstract

Let `Dic_n = Q_{4n} = < a,x | a^{2n}=1, x^2=a^n, x^{-1}ax=a^{-1} >` of order `4n`
(`n>=3`) and `S={a,a^{-1},x,x^{-1}}`. Let `Gamma_n=Cay(Dic_n,S)` (right Cayley,
4-regular simple, `4n` vertices) and `Sigma_n=Sch(Dic_n/<x>,S)` on right cosets
of `H=<x>` (order 4, index `n`; 4-regular with loops/multi-edges, `n` vertices).
Using only explicit `2×2` irreps, elementary trig, permutation-vs-regular
inclusion, trace identities and the discrete Cheeger inequality, we prove:

- `lambda_2(Gamma_n)=2+2cos(2π/n)`, gap `4-lambda_2=2-2cos(2π/n)=4sin^2(π/n)>=16/n^2`;
- `Spec(Sigma_n) ⊂ Spec(Gamma_n)` as sets (with multiplicities dominated), hence
  `gap(Sigma_n)>=gap(Gamma_n)`, in fact equality for all `n>=3`;
- `Tr(A_{Gamma_n}^2)=16n`, `Tr(A_{Gamma_n}^4)=152n` (38 closed 4-walks per vertex),
  verified combinatorially and spectrally;
- edge-expansion `h>=2sin^2(π/n)>=8/n^2` for both families.

Numerics for `3<=n<=30` (pure-Python group model + `numpy.linalg.eigvalsh`) agree
to `<1e-8` and audit the proof; the proof itself is exact and does not depend on
floating point. The `2×2` eigenvalue inputs are classical (Babai; dicyclic
representation theory); the conversion to a sharp gap, the `n`-vertex Schreier
family with inclusion, the uniform `38` trace count and Cheeger data are the new
packaging. This is **not** a uniform expander claim (gap `~1/n^2`).

## 1. Prior work and originality

- Babai (1979) spectra of Cayley graphs via irreps; Hoory–Linial–Wigderson
  expander survey (Cheeger inequalities). We invoke these, prove nothing new there.
- Integral Cayley graphs over dicyclic groups (e.g. Lin. Alg. Appl. 2019): eigenvalue
  formulas, integrality criteria. No gap, no Cheeger, no Schreier quotient.
- Random walks on Heisenberg/unitriangular groups (cutoff, coupling, many random
  generators). Disjoint: we use 4 fixed generators, deterministic `2×2` blocks,
  no coupling.
- Searches for "dicyclic spectral gap" return zero title hits. The delta is therefore
  packaging known formulas into a certified gap + quotient + trace audit, not discovery
  of the irreps.

## 2. The group and the graphs

Write elements in normal form `x^e a^k` with `e∈{0,1}`, `k∈Z_{2n}`:
`(0,k)=a^k`, `(1,k)=xa^k`. Multiplication (from `a^ix=xa^{-i}`, `x^2=a^n`):

- `(0,k1)(0,k2)=(0,k1+k2)`,
- `(0,k1)(1,k2)=(1,k2-k1)`,
- `(1,k1)(0,k2)=(1,k1+k2)`,
- `(1,k1)(1,k2)=(0,n+k2-k1)`, all mod `2n`.

Identity `(0,0)`. Inverses: `(0,k)^{-1}=(0,-k)`, `(1,k)^{-1}=(1,k+n)` since
`-n≡n mod 2n`. In particular `x=(1,0)` has order 4, `x^{-1}=(1,n)=xa^n`,
`a=(0,1)` has order `2n`. `a^n=(0,n)` is the unique central involution.

For `n>=3`: `a≠a^{-1}` (order `>=6`), `x≠x^{-1}` (order 4), and
`<a> ∩ x<a>=∅`, so `|S|=4` with `S={a,a^{-1},x,x^{-1}}={(0,1),(0,-1),(1,0),(1,n)}`
symmetric (`S=S^{-1}`).

`Gamma_n`: right Cayley graph, vertices `Dic_n`, edges `g—gs` for `s∈S`.
Since `1∉S` there are no loops; since `gs1=gs2⇒s1=s2` no multi-edges; symmetry of
`S` makes it undirected 4-regular simple on `4n` vertices. Connected since
`a∈S` generates `<a>` and `x∈S` joins the two cosets. Largest eigenvalue 4 (simple).

`H=<x>={(0,0),(1,0),(0,n),(1,n)}`, order 4. Right cosets `Hg`:
`H(0,k)={(0,k),(1,k),(0,k+n),(1,k+n)}`, indexed by `k mod n`. Similarly
`H(1,k)` is the same set. Hence index `n`; representatives `r_i=(0,i)`, `0<=i<n`.

`Sigma_n`: Schreier graph on these `n` cosets, `B[i,j]=#{s∈S: Hr_is∈Hr_j}`
(counting multiplicity; loops counted). Row sums 4 by construction.
Explicit action (`rep_i=(0,i)`):

- `·a: (0,i)(0,1)=(0,i+1)` → `i↦i+1 mod n`;
- `·a^{-1}: i↦i-1 mod n`;
- `·x: (0,i)(1,0)=(1,-i)` → coset `-i mod n`;
- `·x^{-1}: (0,i)(1,n)=(1,n-i)` → coset `-i mod n`.

So from `i` neighbours are `i+1, i-1, -i, -i` (two parallel edges to `-i`).
Loops iff `-i≡i mod n`, i.e. `i=0` (always, 2 loops) and additionally `i=n/2`
if `n` even (2 loops). All other vertices have one double edge. `B` symmetric:
`a/a^{-1}` pair symmetrically, `x`-double-edges symmetrically. `a`-edges alone form
an `n`-cycle, so connected; top eigenvalue 4 (all-ones vector), simple for `n>=3`
(checked numerically; follows from inclusion + simplicity of 4 in Gamma, see §4).

## 3. Cayley spectrum and gap

### Lemma 1 (2-dim irreps).
For `z=exp(πi/n)` and `1<=k<=n-1`, define
`ρ_k(a)=diag(z^k,z^{-k})`, `ρ_k(x)=[[0,1],[(-1)^k,0]]`.
Then `ρ_k` extends to a representation of `Dic_n`.

*Proof.* Direct: `ρ_k(a)^{2n}=I` since `z^{2nk}=exp(2πik)=1`;
`ρ_k(x)^2=(-1)^kI=ρ_k(a)^n=diag((-1)^k,(-1)^k)`; with `M=ρ_k(x)`,
`M^{-1}=[[0,(-1)^k],[1,0]]` and `M^{-1}diag(d,d^{-1})M=diag(d^{-1},d)`,
so `x^{-1}ax=a^{-1}` holds. ∎

These plus 4 linears exhaust irreps (dimension count `4·1+(n-1)·4=4n`).

### Lemma 2 (blocks).
Let `ρ_k(S)=∑_{s∈S}ρ_k(s)`. Then:

- `k` even: `ρ_k(a)+ρ_k(a^{-1})=2cos(πk/n)I`,
  `ρ_k(x)+ρ_k(x^{-1})=[[0,2],[2,0]]`, so
  `ρ_k(S)=[[2c,2],[2,2c]]`, `c=cos(πk/n)`, eigenvalues `2c+2, 2c-2`;
- `k` odd: `ρ_k(x)+ρ_k(x^{-1})=0`, so `ρ_k(S)=2cI`, eigenvalue `2c` (double),
  `c=cos(πk/n)`.

*Proof.* `ρ_k(a)+ρ_k(a^{-1})=diag(z^k+z^{-k},same)=2cos(πk/n)I`.
`X+X^{-1}` with `X=[[0,1],[e,0]]`, `X^{-1}=[[0,e],[1,0]]`, `e=(-1)^k`:
sum `=[[0,1+e],[1+e,0]]`, i.e. `2[[0,1],[1,0]]` if `e=1`, `0` if `e=-1`. ∎

### Lemma 3 (linears ≤0 apart from trivial).
Abelianization: imposing `a=a^{-1}` gives `2a=0`; with `2x=na` (additive).
If `n` even, `na=0`, abelianization `C2×C2`, characters `χ(a),χ(x)∈{±1}`,
`χ(S)=2χ(a)+2χ(x)∈{4,0,0,-4}`.
If `n` odd, abelianization `C4=⟨x⟩`, `a=2x`, `χ_j(x)=i^j`, `χ_j(a)=(-1)^j`,
`χ_j(S)=2Reχ_j(a)+2Reχ_j(x)∈{4,-2,0,-2}` for `j=0,1,2,3`.
In both cases non-trivial values `≤0`.

*Proof.* Computation above; uses only that 1-dim characters factor through
abelianization. ∎

### Theorem 1 (sharp Cayley gap).
For `n>=3`, `Spec(Gamma_n)` consists of Lemma 2–3 values (each `2×2` eigenvalue
with multiplicity `dim=2`, each linear with multiplicity 1). Hence
`λ_2(Gamma_n)=2+2cos(2π/n)` and gap `4-λ_2=2-2cos(2π/n)=4sin^2(π/n)>=16/n^2`.

*Proof.* General Cayley spectral theorem: eigenvalues are those of `ρ(S)` over
all irreps with multiplicity `dimρ` (regular representation contains `dimρ`
copies of each `ρ`). So it suffices to maximize over Lemmas 2–3 excluding the
trivial `4`. Linears contribute `≤0<2+2cos(2π/n)` (the latter is `>=1` for
`n>=3` since `cos(2π/n)>=-1/2`). Negative branches `-2+2cos<=0` similarly
dominated. Odd `k`: values `2cos(πk/n)`, max at `k=1`: `2cos(π/n)`.
Even `k`: values `2+2cos(πk/n)`, max over even `k>=2` at smallest `k=2`
(`cos` decreasing on `[0,π]`, `πk/n<π` for `k<n`): `2+2cos(2π/n)`.
Compare: with `θ=π/n`, `c=cosθ>=1/2` (`n>=3⇒θ<=π/3`),
`(2+2cos2θ)-2cosθ=4c^2-2c=2c(2c-1)>=0`, equality only at `n=3`
(`c=1/2`, both equal 1; tie noted, formula still holds).
Thus global second maximum is `2+2cos(2π/n)` from `k=2` (shared with `k=1` when
`n=3`). No other irrep attains 4 (`2+2cos<4` for `k>=2`, `2cos<=2<4`,
linears `≤0`). Gap identity via `1-cos2θ=2sin^2θ`. Trig bound:
for `x∈[0,π/2]`, `sin x>=2x/π` by concavity (`sin''<0`, chord below graph);
`π/n∈(0,π/3]`, so `sin(π/n)>=2/n`, gap `>=16/n^2`. ∎

*Remark.* The case `n=3` tie means `λ_2` has higher multiplicity but identical
value; no edge-case failure.

## 4. Schreier quotient and inclusion

### Lemma 4 (Schreier structure).
`Sigma_n` has vertices `Z_n`, adjacency
`(Tf)(i)=f(i+1)+f(i-1)+2f(-i)`. Loops/multi-edges as in §2.

*Proof.* Computation of `Hr_is` in §2. ∎

### Theorem 2 (inclusion and Schreier gap).
`Spec(Sigma_n)⊂Spec(Gamma_n)` as sets, with each Schreier multiplicity
`≤` Cayley multiplicity. Consequently
`gap(Sigma_n)>=gap(Gamma_n)=4sin^2(π/n)>=16/n^2`, and in fact equality holds
for all `n>=3` (verified analytically below and numerically to `n=30`).

*Proof.* Two arguments (either suffices; both recorded).

(i) Abstract: `C[G/H]=Ind_H^G 1` embeds in `C[G]=Reg_G` (induction is exact;
`1_H↪Reg_H` induces to `Ind_H^G1↪Ind_H^GReg_H≅Reg_G`). The Schreier adjacency
is the image of `∑_{s∈S}s` under the permutation representation, the Cayley
adjacency under the regular representation; subrepresentation implies
eigenvalue multiset inclusion.

(ii) Elementary Fourier: on basis `e_k(i)=exp(2πiki/n)`, reflection sends
`e_k↦e_{-k}`, and `T e_k=(ω^k+ω^{-k})e_k+2e_{-k}`, `ω=exp(2πi/n)`.
For `0<k<n/2`, `span{e_k,e_{-k}}` is invariant with matrix
`[[2cos(2πk/n),2],[2,2cos(2πk/n)]]`, eigenvalues `2cos(2πk/n)±2`.
For `k=0`: eigenvalue 4. For `n` even, `k=n/2`: `e_{n/2}` fixed by reflection,
`Te=-2e+2e=0` (the `+` branch `2cosπ+2=0`; the `-` branch `-4` absent due to
dimension collapse). Hence
`Spec(Sigma_n)={2cos(2πk/n)+2, 2cos(2πk/n)-2}` over `k`, with the stated
collapses. With `k'=2k`, these are exactly the even-`k'` branches of Lemma 2
(`2+2cos(πk'/n)`, `-2+2cos(πk'/n)`), hence contained in `Spec(Gamma_n)`.
Multiplicities: each Schreier pair contributes 1 each vs 2 each in Cayley,
so dominated; collapsed cases similarly dominated.

Gap: `k=1` block (present for all `n>2`) gives `2+2cos(2π/n)`, i.e. the Cayley
`λ_2`, and no Schreier eigenvalue exceeds it except 4 (same maximization as
Theorem 1 restricted to this subset; odd-`k'` branches absent here). The only
subtlety is whether 4 is simple in Sigma (else gap=0). It is: Fourier shows 4
only from `k=0` (for `k>0`, `2cos+2<4`). Hence `λ_2(Sigma_n)=2+2cos(2π/n)`,
same gap. A fortiori `gap(Sigma)>=gap(Gamma)`. ∎

*Numerical check.* For `3<=n<=30`, `max_{μ∈SpecB}min_{λ∈SpecA}|μ-λ|<1e-8`
(worst `7.5e-15`) and `gapB==gapA==4sin^2` to `<1e-14`.

## 5. Trace-moment audit

Let `A` be Cayley adjacency (`4n×4n`, symmetric 0/1, no loops).

`Tr(A^2)=16n`: `(A^2)_{vv}=deg(v)=4`, sum over `4n` vertices. Equivalently 4
closed 2-walks per vertex (`ss^{-1}`).

### Lemma 5 (uniform fourth moment).
For all `n>=3`, each vertex has exactly 38 closed 4-walks, so
`Tr(A^4)=4n·38=152n`, split as 6 (zero `x`-letters) + 24 (two) + 8 (four).
Odd numbers of `x`-letters contribute 0 (wrong coset).

*Proof.* Words `w1…w4∈S^4` with product 1 (vertex-transitivity reduces to
identity). Write `a`-letters as `a^{±1}`, `x`-letters as `xa^t`, `t∈{0,n}`.

- 0 `x`'s: exponents `e_i=±1`, sum `≡0 mod 2n`. Since `|sum|<=4<2n` (`n>=3`),
  sum=0 exactly: `C(4,2)=6`.
- 4 `x`'s: `(xa^{t1})…(xa^{t4})=a^{t4-t3+t2-t1}` (pairwise
  `(xa^{s})(xa^{t})=a^{n+t-s}`, `a^{2n}=1` kills `2n`). Exponent is a multiple
  of `n`, equals 0 mod `2n` iff `(b4-b3+b2-b1)∈{-2,0,2}` where `bi=ti/n∈{0,1}`,
  iff total parity even: 8 of 16 assignments.
- 2 `x`'s: 6 position patterns. E.g. pattern `(0,1)`:
  `x_{t1}x_{t2}a^{e3}a^{e4}=a^{n+t2-t1+e3+e4}`; equals 1 iff
  `(t2-t1)+(e3+e4)≡n mod 2n`. With `t2-t1∈{-n,0,n}`, `e3+e4∈{-2,0,2}` and
  `2n>4`, the `0` difference never works (`±2,0≠n mod 2n` for `n>=3`), while
  `±n` works iff `e`-sum `=0` (2 choices). Hence `2·2=4` per pattern. The other
  five patterns reduce to the same congruence:
  `(2,3)`: same; `(0,3)`: `a^{n+t4-t1-(e2+e3)}`; `(1,2)`:
  `a^{e1+e4+n+t3-t2}`; `(0,2)`: `a^{n+(t3-t1)+(-e2+e4)}`; `(1,3)`:
  `a^{n+(t4-t2)+(e1-e3)}`; each gives 4. Total `6·4=24`.
  The bound `2n>4` (i.e. `n>=3`) is exactly what excludes extra small-`n`
  coincidences (`n=2` would add solutions). ∎

Hence `Tr(A^4)=152n`. By the spectral theorem `Tr(A^4)=∑λ_i^4`; our numeric
`∑λ_{formula}^4` matches to `<1e-9` relative, and word-enumeration (no linear
algebra) matches matrix powers exactly as integers. This is a consistency
cross-check, **not** an independent proof of the sharp gap: the elementary bound
`λ_2<=(Tr(A^4)-256)^{1/4}=(152n-256)^{1/4}` is non-trivial (`<4`) only for
`n=3` (`≈3.76`) and exceeds 4 thereafter — recorded honestly to avoid overclaim.

## 6. Cheeger corollaries

For `d`-regular (multi)graph with loops counted in degree but not in cuts,
`h(G)=min_{|S|<=|V|/2}|E(S,∁S)|/|S|` (multi-edges with multiplicity) satisfies
`(d-λ_2)/2<=h<=√(2d(d-λ_2))` (discrete Cheeger; HLW survey; same proof works
with loops since `x^TLx=∑_{i<j}A_{ij}(x_i-x_j)^2`, loops contribute 0).
Thus:

**Corollary.** `h(Gamma_n)>=2sin^2(π/n)>=8/n^2`,
`h(Sigma_n)>=2sin^2(π/n)>=8/n^2`.

Both graphs are connected (`gap>0`). No uniform expansion claimed.

## 7. Numerical audit (corroboration, not proof)

Pure-Python group law (§2) + `numpy.linalg.eigvalsh`; scripts rerun in seconds
(`numpy` only):

- `output/artifacts/verify_dic.py`: builds both adjacencies for `3<=n<=30`,
  checks symmetry/regularity, compares `λ_2` and gap to formulas
  (worst error `9.4e-15`), compares full sorted spectra to §3 formulas
  (`<1e-8`), checks `ρ_k` relations, linears, `k=2` maximality, Schreier
  inclusion (`maxdist<1e-8`), gap equality, `Tr` identities, trig bounds.
- `output/artifacts/trace_count.py` + `trace_counts.json`: integer word
  enumeration vs matrix powers (`Tr2=16n`, `Tr4=152n` exact).
- `output/artifacts/verify_results.json`: full tables.

These audit the exact proof; floating error is irrelevant to the theorems.

## 8. Limitations and what is not claimed

- Eigenvalue formulas are classical; we claim only the gap extraction, Schreier
  family/inclusion, uniform trace count and Cheeger packaging.
- Gap `Θ(1/n^2)` is polynomial, not uniform expansion; framed as sharp solvable-group
  benchmark, not LPS-type expander.
- Numerics cover `n<=30`; theorems cover all `n>=3` analytically.
- Trace fourth moment gives only a weak independent upper bound (see §5).
- Schreier regularity is with loops/multi-edges (row-sum 4); simple-graph Cheeger
  constants would differ by loop/parallel-edge conventions — stated convention counts
  multiplicity, loops in degree only.

## References

- L. Babai, Spectra of Cayley graphs, JCT-B 1979 (character formula).
- Hoory–Linial–Wigderson, Expander graphs and their applications, Bull. AMS 2006
  (Cheeger, background).
- Integral Cayley graphs over dicyclic groups, Lin. Alg. Appl. 2019 (formulas,
  integrality; no gap).
- Cutoff for random walks on upper triangular matrices, arXiv:1911.02974
  (contrasting random-generator/coupling setting).

## Appendix: reproduction

```
python3 output/artifacts/verify_dic.py      # <10s, numpy only
python3 output/artifacts/trace_count.py     # integer checks
```

Expected: `ALL CHECKS PASSED`, worst `λ_2` error `~1e-14`.
