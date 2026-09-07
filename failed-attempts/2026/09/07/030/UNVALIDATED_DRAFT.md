# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Weight-32 level-one Galois-orbit certificate: exact Hecke polynomials, q-expansions, and trace-formula cross-check

## Abstract
For $S_{32}(SL_2(\mathbf Z))$ we prove $\dim=2$ and a single Galois orbit of
degree $2$ (Maeda holds at $k=32$). Exact characteristic polynomials over
$\mathbf Z$ for $T_2,T_3,T_5$, the quadratic coefficient field
$\mathbf Q(\sqrt{18295489})$ with $18295489=67\cdot 273067$ squarefree, one
normalized eigenform $q$-expansion per orbit to $O(q^{50})$, and an independent
Eichler–Selberg trace cross-check for $n=1,2,3,5$ are produced by a single
stdlib-only Python script rerunnable in seconds. No floating point is used.

This is not a new proof of Maeda's conjecture in general; $T_2$-irreducibility
to weight $<12000$ is due to Ghitza–McAndrew, and the same polynomials appear
in the LMFDB (1.32.a.a). The contribution is a single-weight replayable exact
bundle (polynomials $+$ $O(q^{50})$ eigenforms $+$ trace certificate) with two
independent legs (Hecke linear algebra vs.\ trace formula) and congruence
witness, checkable without Sage/Magma/PARI.

## 1. Theorem

Let $k=32$, $S_k=S_k(SL_2(\mathbf Z))$.

1. $\dim M_{32}=3$, $\dim S_{32}=2$.
2. On $S_{32}$, with respect to the integral cusp basis below,
   $$M_2=\begin{pmatrix}1321176&1280664\\-1320000&-1281216\end{pmatrix},\quad
     M_3=\begin{pmatrix}570798252&553246848\\-570240000&-553435092\end{pmatrix},$$
   $$M_5=\begin{pmatrix}-1855520206770&-1816698723840\\1872499200000&1836128988750\end{pmatrix}.$$
   Hence
   $$\chi_{T_2}(T)=T^2-39960T-2235350016,$$
   $$\chi_{T_3}(T)=T^2-17363160T-416300505539184,$$
   $$\chi_{T_5}(T)=T^2+19391218020T-5207533830370075837500.$$
3. $D_2=10538201664=576\cdot18295489$, $18295489=67\cdot273067$ squarefree,
   $D_2$ non-square. $\chi_{T_2}$ is irreducible over $\mathbf Q$ (hence over
   $\mathbf Z$); it has no root mod $29$ ($D_2$ is a non-residue mod $29$).
   So $T_2$ has distinct eigenvalues and $S_{32}$ is a single Galois orbit of
   degree $2$. $D_3/D_2=432^2$, $D_5/D_2=1418560^2$, so $T_3,T_5$ have the same
   splitting field $\mathbf Q(\sqrt{18295489})$, discriminant $18295489\equiv1(4)$.
4. Let $s=\sqrt{18295489}$. Up to Galois conjugacy the normalized eigenform is
   $f^-=q+\sum_{n\ge2}a_n^-q^n$, $a_n^-=A_n+B_ns$ with $A_n,B_n\in\mathbf Z$,
   $f^+= \bar f^-$ ($s\mapsto -s$). First values $(A_n,B_n^-)$:
   $$(2:19980,-12),\ (3:8681580,-5184),\ (4:886267168,-479520),$$
   $$(5:-9695609010,17022720),\ (6:1311583748112,-207755280),\ (7:15128763788600,863146368).$$
   Full table to $n\le50$ is in `artifacts/qexp_Oq50.txt`. Trace form
   $t_n=a_n^-+a_n^+=2A_n$ begins
   $2,39960,17363160,1772534336,-19391218020,2623167496224,\dots$
   matching $\mathrm{Tr}(T_n)$.
5. Independent Eichler–Selberg values for $k=32$ agree:
   $\mathrm{Tr}(T_1)=2$, $\mathrm{Tr}(T_2)=39960$, $\mathrm{Tr}(T_3)=17363160$,
   $\mathrm{Tr}(T_5)=-19391218020$.

Items 2–5 are computed exactly over $\mathbf Z/\mathbf Q$; §3–§4 give the
verification steps. The script also checks $[M_i,M_j]=0$,
$a_{p^2}=a_p^2-p^{31}$ for $p=2,3,5$, and $a_6=a_2a_3$ on both eigenforms.

## 2. Method (exact, Sage-independent)

**Eisenstein monomials.** $M(SL_2(\mathbf Z))=\mathbf C[E_4,E_6]$,
$E_4=1+240\sum\sigma_3(n)q^n$, $E_6=1-504\sum\sigma_5(n)q^n$.
Weight $32$: $4a+6b=32$ gives $(a,b)=(8,0),(5,2),(2,4)$, so
$m_1=E_4^8$, $m_2=E_4^5E_6^2$, $m_3=E_4^2E_6^4$ span $M_{32}$.
Computed truncated to $O(q^{70})$ by exact integer convolution.
Determinant of $(m_i)$ at $q^0,q^1,q^2$ is $-5159780352\ne0$, so they are
independent and $\dim M_{32}=3$. Each has $a_0=1$, so
$S_{32}=\{c_1+c_2+c_3=0\}$ has dim $2$ with integral basis
$b_0=m_1-m_2$, $b_1=m_2-m_3$ ($a_1=1728$ each, det at $1,2$ is $-5159780352$).

**Hecke action.** Level-one $T_n$ on $q$-expansions ($k=32$):
$$b_m(T_nf)=\sum_{d\mid\gcd(n,m)}d^{31}a_{mn/d^2}(f),\quad
  b_0=\sigma_{31}(n)a_0.$$
Applied to $b_0,b_1$ (needs $a$ up to index $10\cdot5=50<70$).
Write $T_n(b_i)=\sum_k(M_n)_{ki}b_k$; solved from $m=1,2$
($B^{-1}T$ over $\mathbf Q$) and verified for $m=0,\dots,11$.
Matrices are integral. Characteristic polynomials and $D=\mathrm{Tr}^2-4\det$
follow. This leg uses only divisor sums and rational linear algebra.

**Field and irreducibility.** $D_2=10538201664$,
$102655^2=10538049025<D_2<10538254336=102656^2$, so non-square, non-zero:
quadratic irreducible. Trial division to $5000$ (sieve) gives
$18295489=67\cdot273067$; $\sqrt{273067}<523$, all prime divisors $\le522$
tested, so both prime; exponents $1$ so squarefree. $67^2\nmid$ it.
$D_2=24^2\cdot18295489$, $D_3=D_2\cdot432^2$, $D_5=D_2\cdot1418560^2$
(exact division + isqrt check), same field. Mod $29$:
$\chi_{T_2}$ has zero roots among $0,\dots,28$ (brute force) and
$D_2^{(29-1)/2}\equiv28\pmod{29}$, non-residue, so irreducible mod $29$.
For $p<29$, $p=3$ ramifies, others are residues — $29$ is the first witness.

**Eigenforms.** $T_2$-eigenvalues $\lambda^\pm=19980\pm12s$.
Eigenvectors $v^\pm=(1280664,\lambda^\pm-1321176)$ in
$\mathbf Q(s)^2$. $M_3,M_5$ commute with $M_2$ (checked), preserve the
one-dimensional eigenspaces; eigenvalues
$\mu_3^\pm=8681580\pm5184s$, $\mu_5^\pm=-9695609010\mp17022720s$
(the sign convention matches $v^\pm$) verified by $Mv=\mu v$ in exact
$(p,q)$ arithmetic and $\mathrm{Tr}=\mu+\bar\mu$, $\det=\mu\bar\mu$.
Normalization $a_1=1$ gives $\alpha+\beta=1/1728$,
$t=1/(1728(b+\lambda-a))$, $f=\alpha b_0+\beta b_1$.
All $a_n$, $n\le50$, lie in $\mathbf Z[s]$ (denominators cancel, checked).
Conjugacy $f^+=\bar f^-$ is immediate, so one orbit.
Relations $a_{p^2}=a_p^2-p^{31}$, $a_6=a_2a_3$ checked.

**Trace formula (second leg).** For even $k\ge4$, $n\ge1$,
$$\mathrm{Tr}(T_n|S_k)=-\tfrac12\sum_{t^2<4n}P_k(t,n)H(t^2-4n)
  -\tfrac12\sum_{d\mid n}\min(d,n/d)^{k-1}
  +\tfrac{k-1}{12}n^{(k-2)/2}{\bf1}_\square(n),$$
$P_k(t,n)=S_{k-1}$, $S_0=0,S_1=1,S_m=tS_{m-1}-nS_{m-2}$,
$H$ Hurwitz–Kronecker ($H(-3)=1/3,H(-4)=1/2$, else reduced-form count with
weight $2/|\mathrm{Aut}|$: $1$ except $1/2$ for $(f,0,f)$, $1/3$ for
$(f,f,f)$). Implemented independently with `Fraction`s.
Needed $H$: $-3\!:\!1/3$, $-4\!:\!1/2$, $-7,-8,-11\!:\!1$, $-12\!:\!4/3$,
$-16\!:\!3/2$, $-19\!:\!1$, $-20\!:\!2$ (also enumerated by the code).
For $k=32$: $n=1$: $-1/12-1/2+31/12=2$; $n=2$: $39961-1=39960$;
$n=3$: $17363161-1$; $n=5$: $-19391218019-1$. Matches Hecke traces.

## 3. Reproducibility

Single file `artifacts/s32_certificate.py` (stdlib only: `fractions,math,time,os`;
no Sage, no PARI, no sympy, no numpy, no network). Run:

```
python3 artifacts/s32_certificate.py
```

writes `hecke_polys.txt`, `qexp_Oq50.txt` ($n,A_n,B_n$ to $50$),
`trace_form.txt`, `trace_check.txt`, `run_log.txt` in the same directory.
Observed $0.01$–$1$s on a standard container (PREC $70$). All asserts must pass;
any mismatch aborts (fail-closed). Coefficients $a_n=A_n+B_ns$ to $n=50$ are
listed in the artifact; head ($n\le12$) in §1. LMFDB 1.32.a.a agrees
($b=12s$ notation) as a sanity check, not as proof.

## 4. Limitations and scope

- Fixed stratum $k=32$, level $1$ only. No claim for other weights/levels or for
  Maeda in general. Reusable method for $24\le k\le36$ but not demonstrated here.
- Uses the structure theorem $M=\mathbf C[E_4,E_6]$ and the level-one Hecke
  $q$-expansion formula (textbook). Dimension counts rely on an explicit
  $3\times3$ determinant, not just $\lfloor k/12\rfloor$.
- $18295489=67\cdot273067$ primality is by trial division to $\sqrt{\ }$ (exact,
  logged); field discriminant $18295489$ uses $1\bmod4$ squarefree rule.
- Trace formula implementation covers $n\le5$ (and $n=1$); general-$n$ correctness
  relies on the quoted formula, cross-checked at four points.
- No analytic $L$-function or Galois-representation consequences are proved.

## References

- LMFDB 1.32.a.a (newform orbit, $q$-expansion, Hecke polynomials, field
  $x^2-x-4573872$, $\beta=12\sqrt{18295489}$) — ground-truth anchor.
- A. Ghitza, A. McAndrew, arXiv:1207.3480 — $T_2$-irreducibility to $<12000$
  (includes $k=32$, $T_2$-only flag).
- C. Citro, A. Ghitza, LMS J. Comput. Math. 16 (2013) — mod-$p$ level-one systems.
- F. Tsaknias, arXiv:1205.3420 — higher-level orbit-count speculation.
- W. Stein, Modular Forms: A Computational Approach (trace formula, modular symbols).
