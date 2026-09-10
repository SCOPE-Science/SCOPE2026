# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# QF-vacuity and horn-necessity for twisted sum-product in Frobenius difference fields

## 1. Setting

Let $p$ be prime, $l\geq 2$, $q=p^l$, $K=\mathbf{F}_q$,
$\sigma(x)=x^p$ (Frobenius). Let $N(x)=x^{(q-1)/(p-1)}$ (norm to
$\mathbf{F}_p^\times$) and $\mathrm{Tr}(x)=\sum_{i=0}^{l-1}\sigma^i(x)$
(trace to $\mathbf{F}_p$). Consider the sequence
$K_n=\mathbf{F}_{p_n^{l_n}}$, $\sigma_n=\mathrm{Frob}_{p_n}$ with distinct
primes $p_n\to\infty$, $l_n\to\infty$, and $(K,\sigma)=\prod_U K_n$.

A **quantifier-free order-$\leq 1$ atom** is $\{x:F(x,\sigma(x))=0\}$ where
$F\in K[X,Y]$ has total degree $\leq D$. A **qf formula** with $m$ atoms is
any Boolean combination of $m$ such atoms. Write $S_F=\{x:F(x,\sigma x)=0\}$.

## 2. Theorem (qf size-gap + window vacuity)

**Lemma 2.1 (per-atom gap).** Assume $p>D$. Let $F\neq 0$ of total degree
$\leq D$. Then either $|S_F|\leq Dp$ or $S_F=K$ (the latter iff $F=0$ as a
polynomial, see proof).

*Proof.* Write $F(X,Y)=\sum_{a+b\leq D}c_{a,b}X^aY^b$. On $K$,
$\sigma(x)=x^p$, so $S_F$ is the zero set of the univariate polynomial
$G(X)=\sum c_{a,b}X^{a+bp}$. Claim: $(a,b)\mapsto a+bp$ is injective on
$\{a+b\leq D\}$ when $p>D$. Indeed if $a_1+b_1p=a_2+b_2p$ with, say,
$b_1\geq b_2$, then $a_1-a_2=(b_2-b_1)p$; $|a_1-a_2|\leq D<p$ forces
$a_1=a_2$, $b_1=b_2$. Hence distinct monomials give distinct exponents, so
$F\neq 0\Rightarrow G\neq 0$ as a polynomial, of degree
$\max(a+bp)\leq Dp$ (attained at $(0,D)$). A nonzero univariate polynomial
of degree $\leq Dp$ has at most $Dp$ roots. If $F=0$, $S_F=K$. ∎

**Lemma 2.2 (Boolean closure).** Let $\varphi$ use $m$ atoms of degree
$\leq D$, $p>D$. Then $|A|\leq 2^mDp$ or $|K\setminus A|\leq 2^mDp$,
where $A=\varphi(K)$.

*Proof.* Each atom is $\leq Dp$-small or whole ($=K$) by Lemma 2.1.
Write $\varphi$ in DNF: $A=\bigcup_{j\leq 2^m}C_j$, each $C_j$ an
intersection of literals. A literal is small ($\subseteq$ a $\leq Dp$ atom
or empty) or co-small (complement of a $\leq Dp$ atom, with complement
$\leq Dp$). A clause containing a small literal is small ($\leq Dp$);
a clause of only co-small literals has complement $\leq mDp$ by union
bound. If some clause is co-small, $K\setminus A\subseteq K\setminus C_j$
gives $|K\setminus A|\leq mDp\leq 2^mDp$. Else all clauses are small and
$|A|\leq 2^mDp$. ∎

**Corollary 2.3 (window vacuity).** Fix $m,D,\delta>0$. For the sequence
$(p_n,l_n)$ with $p_n\to\infty$, $l_n\to\infty$, for all large $n$ no
qf-definable $A_n\subseteq K_n$ with $\leq m$ atoms of degree $\leq D$
lies in the intermediate window $q_n^\delta\leq|A_n|\leq q_n^{1-\delta}$.

*Proof.* Let $B_n=2^mDp_n$, $q_n=p_n^{l_n}$. Small-avoids:
$B_n<q_n^\delta\iff 2^mD<p_n^{l_n\delta-1}$; since $l_n\to\infty$,
$l_n\delta-1>1$ eventually and $p_n\to\infty$, holds eventually.
Co-small-avoids: $q_n-B_n>q_n^{1-\delta}\iff q_n-q_n^{1-\delta}>B_n$;
$q_n-q_n^{1-\delta}=q_n^{1-\delta}(q_n^\delta-1)\geq q_n^{1-\delta}\geq
q_n/ q_n^\delta$ grows faster than $B_n=O(p_n)$; precisely,
$q_n^\delta\to\infty$ gives $q_n-B_n\geq q_n/2>q_n^{1-\delta}\iff
q_n^\delta>2$, eventually true. Combined with Lemma 2.2, $A_n$ is
$B_n$-small ($<q_n^\delta$) or $B_n$-co-small ($>q_n^{1-\delta}$). ∎

Consequence for the target: the quantifier-free fragment can never meet
the hypothesis of the twisted dichotomy; any proof or refutation must use
quantified formulas. Ring-level uniformity fails because
$\sigma(x)=x^{p_n}$ has ring degree $p_n\to\infty$ (so BGT-type
$\varepsilon$ cannot come from ring complexity); the replacement input
must be difference complexity via Zou coarse dimension.

## 3. Horn-necessity identities

Let $T=\{x:N(x)=1\}$ (norm-1 torus, $|T|=(q-1)/(p-1)$),
$V=\{x:\mathrm{Tr}(x)=0\}$ ($|V|=q/p$).

**Lemma 3.1.** $\sigma(T)=T$ and $T\cdot\sigma(T)=T$ as sets; hence the
twisted product never grows on $T$ and the sum horn is indispensable.
$\sigma(V)=V$ and $V+V=V$; hence the sum never grows on $V$ and the twist
horn is indispensable.

*Proof.* $N(\sigma x)=N(x)^p=N(x)$ since $N(x)\in\mathbf{F}_p^\times$ is
fixed by $t\mapsto t^p$; so $\sigma(T)=T$, and $T$ a subgroup gives
$T\cdot\sigma(T)=T$. $\mathrm{Tr}(\sigma x)=\mathrm{Tr}(x)$ by cyclic shift
of the sum; so $\sigma(V)=V$, and $V$ an additive subgroup gives
$V+V=V$. ∎

Thus neither $|A+A|$ nor $|A\cdot\sigma(A)|$ alone suffices; the target's
sum-of-two-terms growth is the correct shape. $T,V,\mathrm{Fix}(\sigma)$
and subfields are $\sigma$-invariant; $\mathrm{Fix}$/subfields sit in the
STRUCT horn by definition.

## 4. Computational verification (replayable, stdlib only)

`python3 output/artifacts/verify_emergent.py → VERIFY_OK` checks:
- **E1** distinct-exponent injectivity at $(D,p)=(2,5),(3,5),(2,101)$.
- **E2** exhaustive qf gap, $\mathbf{F}_p$-coeff slice, $D=2$:
  $(3,2)$: 728 polys, BAD=0; $(5,2)$: 15624 polys, BAD=0 (every nonzero
  $F$ has $|\{x:F(x,\sigma x)=0\}|\leq 2p$ or whole field).
- **E3** exact-integer window-avoidance spots
  $(p,l)=(5,30),(101,10),(7,20)$: $B^5<q$, $(q-B)^5>q^4$
  ($\delta=1/5$), via integer arithmetic.
- **E4** horn identities at $(3,2),(5,2)$: $T\cdot\sigma(T)=T$,
  $V+V=V$ as exact set equalities.

Supporting target-shape evidence (not part of the claim):
exhaustive/randomized existential-projection censuses
(`phase1f_census.py`, `phase1g_widen.py`) found VIOL=0 in-window escapes
at $(2,2),(3,2),(5,2),(2,3),(3,3)$; random $\mathbf{F}_q$-coefficient gap
probes (`phase1e_exotic.py`) found BAD=0. These illustrate but do not prove
the quantified case.

## 5. Limitations and scope

- Covers **quantifier-free** formulas only; says nothing about
  $\exists y\,F(x,y,\sigma x,\sigma y)=0$ or deeper quantifiers, where the
  target lives.
- Gives no growth exponents $\varepsilon,\eta$; does not prove the
  fallback ($25/24$, $11/12$) or target dichotomy.
- Exhaustive machine checks are small-field illustrations
  ($\mathbf{F}_p$-slice); the general-coefficient proof is Lemma 2.1
  (needs $p>D$), not the scripts.
- Originality: proof ingredients (injectivity + Schwartz–Zippel + DNF
  union bound) are standard; novelty is the difference-field formulation,
  the window-vacuity corollary forcing the quantified case, and the paired
  horn-necessity pinning the exact target shape. No source was found
  stating this qf-vacuity for Frobenius difference fields (live-checked:
  Zou = SOP/TP2 + coarse dimension only; Hrushovski = untwisted
  stabilizer; BGT = linear approximate subgroups; Chernikov–Starchenko =
  distal regularity).
