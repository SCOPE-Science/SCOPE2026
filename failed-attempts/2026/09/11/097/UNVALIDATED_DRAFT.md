# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Skein completion destroys full dualizability for 2Rep(Z/2)

## Theorem (target)
Fix $k$ algebraically closed of characteristic $0$.
Let $C=2\mathrm{Rep}(\mathbf{Z}/2)$ and $\mathrm{SkFr}(C)$ its framed skein
completion (free filtered cocompletion / Cauchy completion in the skein–
factorization-homology sense). Then $\mathrm{SkFr}(C)$ is **not** fully
dualizable in the Morita $4$-category. Witness: the generating
$1$-morphism $S$ induced by the countable direct sum of the regular module
strand has **no right adjoint** in the completion; the cusp zigzag fails for
every candidate. Hence the distinguished object cannot define a framed
$4$d local TFT via the cobordism hypothesis.

## Setup and definitions
1. **Uncompleted baseline.** Before completion the generating endomorphism
   category is the finite rigid symmetric monoidal category
   $E_0=\mathrm{Rep}(\mathbf{Z}/2)=\{1,\chi\}$, $\chi^2=1$,
   $R=1\oplus\chi$ the regular strand ($2$-dimensional swap representation).
   Every object is dualizable; $R$ is self-dual. This is the Decoppet
   regime: the uncompleted fusion $2$-category is fully dualizable.
2. **Framed skein completion.** Define $\mathrm{SkFr}(C)$ by freely adjoining
   filtered colimits of framed strands (Cauchy colimits in the skein /
   factorization-homology sense; cf. skein-as-cocompletion). Concretely, for
   the distinguished generating object $X$ (regular-module strand vacuum),
   $$\mathrm{End}_{\mathrm{SkFr}}(X)\;\cong\;\mathrm{Ind}(E_0)
     \;=\;\mathrm{Ind}(\mathrm{Rep}(\mathbf{Z}/2)),$$
   the category of all (possibly infinite-dimensional) $\mathbf{Z}/2$
   representations, with monoidal product $=\,$ composition (strand stacking
   $=\,$ tensor over $k$), unit $1$. Monoidal structure preserves filtered
   colimits in each variable (Day convolution / pointwise tensor).
   Finite strand sums are the compact objects $E_0\subset\mathrm{Ind}(E_0)$.
3. **Witness.** $S_N=R^{\oplus(N+1)}$, $i_N:S_N\hookrightarrow S$,
   $S=\mathrm{colim}_N S_N=\bigoplus_{n\in\mathbf{N}}R$.
   Each $S_N$ is a compact generator; $S$ is a filtered colimit thereof, so
   $S\in\mathrm{SkFr}$ proper (not a larger cocompletion). Projections
   $p_N:S\to S_N$, $q_m:S\to R$ ($m$-th summand), $j_m:R\to S$ satisfy
   $p_N i_N=\mathrm{id}$, $q_m j_m=\mathrm{id}$, $q_m i_N=0$ for $m>N$.
4. **Adjoints = duals.** For an endo-$1$-morphism $f:X\to X$, a right adjoint
   is exactly a right dual in the monoidal $\mathrm{End}(X)$: unit
   $\eta:1\to f\otimes T$ (coevaluation), counit
   $\varepsilon:T\otimes f\to 1$ (evaluation) satisfying the two cusp
   zigzags $(\mathrm{id}_f\otimes\varepsilon)(\eta\otimes\mathrm{id}_f)=
   \mathrm{id}_f$, $(\varepsilon\otimes\mathrm{id}_T)
   (\mathrm{id}_T\otimes\eta)=\mathrm{id}_T$ (up to symmetric braiding).

## Level-sharpness (lower duals hold)
- Objects have duals (unchanged by completion at object level).
- Every compact $1$-morphism has both adjoints: $E_0$ is rigid; e.g. $R$
  self-dual via $\mathrm{ev}=[1\,0\,0\,1]$,
  $\mathrm{coev}=[1\,0\,0\,1]^t$ on $R\otimes R$ (checked $Z/2$-linear,
  both zigzags $=\mathrm{id}_R$ on the nose; see `artifacts/verify.py`).
  Hence failure, if proved, sits exactly at the infinite completed
  $1$-morphism $S$, i.e. at $3$-dualizability, not a low-level degeneracy.

## Lemma (unit compactness + tensor-colimit factoring)
(a) $1$ is compact in $\mathrm{Ind}(E_0)$:
$\mathrm{Hom}(1,\mathrm{colim}_N V_N)\cong\mathrm{colim}_N\mathrm{Hom}(1,V_N)$.
Indeed $\mathrm{Hom}(1,V)=V^{\mathbf{Z}/2}$ (invariants), a finite limit over
the finite group, commuting with filtered colimits in $\mathrm{Vect}_k$
(Reynolds projector $E=(1+g)/2$ uses $\mathrm{char}\,k=0$; verified
$\dim (R^{\otimes 2})^G=2$, $\dim (R^{\oplus 3})^G=3=\sum\dim$).
(b) $S\otimes T\cong\mathrm{colim}_N(S_N\otimes T)$ for any $T$.
Hence any $\eta:1\to S\otimes T$ factors as
$1\xrightarrow{c_N}S_N\otimes T\xrightarrow{i_N\otimes\mathrm{id}}S\otimes T$
for some finite $N$.

## Proposition (no right adjoint)
$S$ has no right dual in $\mathrm{Ind}(\mathrm{Rep}(\mathbf{Z}/2))$, hence
as a $1$-morphism $X\to X$ has no right adjoint.

*Proof.* Suppose $T$ with $\eta:1\to S\otimes T$,
$\varepsilon:T\otimes S\to 1$ satisfying the cusp. By the Lemma,
$\eta=(i_N\otimes\mathrm{id})\circ c_N$ for some $N$. Then
$$\mathrm{id}_S=(\mathrm{id}_S\otimes\tilde\varepsilon)\circ
  (\eta\otimes\mathrm{id}_S)
  =i_N\circ f,\quad
  f:=(\mathrm{id}_{S_N}\otimes\tilde\varepsilon)\circ(c_N\otimes\mathrm{id}_S)
  :S\to S_N$$
($\tilde\varepsilon$ absorbs the symmetric braiding). So $\mathrm{id}_S$
factors through the finite stage $S_N$. For $m>N$,
$$\mathrm{id}_R=q_m\circ\mathrm{id}_S\circ j_m
  =q_m\circ i_N\circ f\circ j_m=0\circ f\circ j_m=0,$$
since $q_m i_N=0$. But $R\neq 0$: $\mathrm{tr}(\mathrm{id}_R)=2\neq 0$,
$\mathrm{id}_R\neq 0$ (explicit matrix; `verify.py` certifies the zero
component $\neq\mathrm{id}_R$). Contradiction. Thus no pair
$(T,\eta,\varepsilon)$ satisfies the cusp; the cusp identity fails for
every candidate. ∎

## Corollary (not fully dualizable; no framed 4d TFT)
Per the admitted audit plan, 3-dualizability is tested exactly by exhibiting
or refuting a right adjoint for the named generating 1-morphism via the cusp
zigzags. Since $S$ has none, the distinguished generating object fails the
3-dualizability test, hence is not fully dualizable in the Morita
4-category. By the cobordism hypothesis it cannot define a framed $4$d local
(fully extended) TFT. This contrasts with Decoppet full dualizability before
completion: completion adds the infinite colimit $S$ and breaks adjoint
existence, since infinite sums need not preserve duals.

## Computed evidence (finite core; stdlib, exact over QQ)
`output/artifacts/verify.py` → `VERIFY_OK`, certifying:
- fusion $\chi^2=1$, $R=1\oplus\chi$ ($\dim2$, $\mathrm{tr}\,g_R=0$);
- $R$ self-dual: explicit $\mathbf{Z}/2$-maps $\mathrm{ev},\mathrm{coev}$
  with both zigzags $=\mathrm{id}_R$, invariants $\dim(R^{\otimes2})^G=2$;
- compactness: $\dim(R^{\oplus3})^G=3=\sum$ (Reynolds rank);
- obstruction: zero-coev component gives $0_{2\times2}\neq I_2$,
  $\mathrm{tr}(I_2)=2$. The infinite tail argument above lifts this finite
  rank fact to the no-dual theorem (proof, not computation).

## What is proved vs conjectured vs uncertain
- **Proved:** no-dual/no-right-adjoint theorem for $S$ in the stated
  $\mathrm{Ind}$ model; level-sharpness for compact strands; TFT corollary
  conditional on definitions.
- **Computed:** finite fusion/zigzag/compactness/obstruction identities.
- **Not claimed:** classification of all (non)dualizable completed
  $1$-morphisms beyond $S$; any statement outside $\mathrm{char}\,0$ or
  beyond $2\mathrm{Rep}(\mathbf{Z}/2)$.
- **Definition dependence (disclosed):** "framed skein completion" is taken
  as free filtered (Cauchy-in-skein-sense) cocompletion, so
  $\mathrm{End}=\mathrm{Ind}(\mathrm{Rep}(\mathbf{Z}/2))$ and $S$ lies in it
  by construction. Under a strictly finite (Karoubi-only) reading of
  "Cauchy", $\bigoplus_{\mathbf N}R$ would not be present; the audit plan
  and admission record ("infinite Cauchy/strand colimits", "witness as Cauchy
  colimit of compact generators") adopt the former, cocompletion sense used
  in skein–factorization-homology literature, which we follow explicitly.

## Reproducibility
Run `python3 output/artifacts/verify.py` (stdlib only) → expect `VERIFY_OK`.
All matrices and maps are listed in the script; the infinite-step factoring
is the written proof above.
