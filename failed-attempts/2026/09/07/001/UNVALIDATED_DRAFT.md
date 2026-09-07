# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Explicit Pólya–Vinogradov error term for quadratic residues in a short interval intersected with a residue class

## 1. Statement

Let $p$ be an odd prime, $\chi(n)=(\frac{n}{p})$ the Legendre symbol (Dirichlet character mod $p$, $\chi(n)=0$ if $p\mid n$).
Let $m\ge 1$, $(m,p)=1$, $(a,m)=1$, $I=(N,N+H]$ with $N\ge 0$, $H\ge 1$. Put

$$Q=\#\{n\in I:n\equiv a\bmod m,\ p\nmid n\},\qquad
R=\#\{n\in I:n\equiv a\bmod m,\ \chi(n)=1\},$$
$$S=\sum_{\substack{n\in I\\n\equiv a(m)}}\chi(n).$$

Since $\chi(n)\in\{+1,-1\}$ when $p\nmid n$ and $0$ when $p\mid n$,
writing $R_{-}=\#\{\chi=-1\}$ gives $Q=R+R_{-}$, $S=R-R_{-}$, hence

$$|R-Q/2|=|S|/2\tag{1}$$
for every $N,H$ (including $p\mid n$ terms, which contribute $0$ to $S$ and are excluded from $Q$).

**Corrected Theorem.** *With notation below, for $(m,p)=1$, $(a,m)=1$,*

$$|R-Q/2|\le \frac{1}{2\phi(m)}\sum_{\psi\bmod m}\kappa_\psi\,B^{*}(q_\psi),\tag{2}$$
*where the sum is over the $\phi(m)$ Dirichlet characters $\psi\bmod m$,
$q_\psi$ is the conductor of $\chi\psi$ (so $q_\psi\mid pm$, $q_\psi=p$ if $\psi$ is principal,
$q_\psi=p\cdot\mathrm{cond}(\psi)$ otherwise), $B^{*}$ is the explicit Frolenkov primitive
bound of Lemma 1, and $\kappa_\psi=2^{\omega(m)-\omega(f)}\le 2^{\omega(m)}$ with
$f=\mathrm{cond}(\psi)$ $(f=1$ for principal$)$. In particular with uniform
$\kappa(m)=2^{\omega(m)}$ and single-term $B^{*}(q)\le 19\sqrt q\log q$ $(q\ge 3)$,*

$$|R-Q/2|\le \frac{19\cdot 2^{\omega(m)}}{2\phi(m)}\sum_{\psi}\sqrt{q_\psi}\log q_\psi.\tag{3}$$

*Corollary ($H_0$). Let $E(p,m)$ denote the right side of (2) and*

$$H_0(p,m)=\frac{m\,(2E(p,m)+2)}{1-1/p}.\tag{4}$$
*If $H>H_0(p,m)$ then every $I$ of length $H$ contains in class $a\bmod m$
both a quadratic residue and a nonresidue (i.e. $0<R<Q$).*

Remarks on the assigned target. The target as written omits $\kappa_\psi$ and states
$H/m-1>\cdots$. Both are slightly inaccurate: (i) the inner sum is over an *imprimitive*
character, so the pure primitive bound $B^{*}(q_\psi)$ without $\kappa$ is false in general
($m=2$ principal example below); (ii) the $Q$ lower bound loses an extra $1$ from
$p$-divisibility plus a factor $(1-1/p)$. Our (2)–(4) is the corrected honest version.
Up to this explicit $m$-factor it is the claimed doubly-filtered inequality.

## 2. Frozen explicit Pólya–Vinogradov lemma

**Lemma 1 (Frolenkov, arXiv:1107.0381 Thm 1).** *Let $\xi\bmod q$ be primitive nonprincipal.
With $C_0=4\pi^{5/2}+5$, $\gamma$ Euler,*

*even $\xi(-1)=1$:*
$$M(\xi):=\max_{M<N}\Bigl|\sum_{M<n\le N}\xi(n)\Bigr|
\le \frac{2}{\pi^2}\sqrt q\log q+\frac{4}{\pi^2}(1+\gamma+\log C_0)\sqrt q+\psi_1(q),$$
$$\psi_1(q)=1+\frac{24}{\pi^2C_0}+\frac{8}{\pi^2}\frac{\sqrt q}{e^{2\sqrt q/C_0}-1};$$
*odd $\xi(-1)=-1$:*
$$M(\xi)\le \frac{1}{2\pi}\sqrt q\log q+\frac1\pi\Bigl(1+\gamma+\log\frac{2C_0}{\pi}\Bigr)\sqrt q+\psi_2(q),$$
$$\psi_2(q)=1+\frac{3}{C_0}+\frac{2}{\pi}\frac{\sqrt q}{e^{\pi\sqrt q/C_0}-1}.$$

Numerics: $C_0=74.97367331\ldots$, $2/\pi^2=0.20264236\ldots$,
$4/\pi^2(1+\gamma+\log C_0)=2.38889116\ldots$,
$1/(2\pi)=0.15915494\ldots$, $1/\pi(1+\gamma+\log(2C_0/\pi))=1.73248749\ldots$.
Define $B_{\rm even}(q)$, $B_{\rm odd}(q)$ as the two right sides and
$B^{*}(q)=B_{\rm even}(q)$.

*Majorant.* For $q\ge 3$, $B^{*}$ bounds both parities. Indeed
$x/(e^{bx}-1)$ is decreasing in $x>0$, so $\psi_{1,2}$ are decreasing in $q$ and
$\psi_1(q)-\psi_2(q)\ge\lim_\infty=\frac{24/\pi^2-3}{C_0}=-0.0076\ldots$.
Since $c_{1,e}-c_{1,o}=0.0435>0$, $c_{2,e}-c_{2,o}=0.6564>0$,
$B_{\rm even}-B_{\rm odd}\ge 0.0435\sqrt q\log q+0.6564\sqrt q-0.0076$,
increasing for $q\ge 3$ and $\ge 1.21>0$ at $q=3$. So $B^{*}\ge B_{\rm odd}$.

*Single-term.* For $q\ge 3$, $B^{*}(q)\le 19\sqrt q\log q$.
Proof: $\psi_1$ decreasing, $\psi_1(q)\le\psi_1(3)=30.7216\ldots$
(computed; crude uniform $\psi_1\le 1+24/(\pi^2C_0)+4C_0/\pi^2<31.5$ via $e^y-1\ge y$).
Hence ratio $B^{*}/(\sqrt q\log q)=c_1+c_2/\log q+\psi_1/(\sqrt q\log q)$
is decreasing in $q$ and max $18.5221$ at $q=3<19$ (margin $\gg$ fp error).
All our conductors satisfy $q_\psi\ge p\ge 3$, so logs are positive.

We use only the primitive case of Frolenkov; imprimitive sums are reduced by Lemma 4.

## 3. Orthogonality

**Lemma 2.** *Assume $(a,m)=1$. For every integer $n$, with $\psi(n)=0$ if $(n,m)>1$,*
$${\bf 1}_{\{n\equiv a(m)\}}=\frac1{\phi(m)}\sum_{\psi\bmod m}\bar\psi(a)\psi(n).\tag{5}$$
*Proof.* If $n\equiv a$ then $(n,m)=1$ and (5) is usual orthogonality on $(\mathbf Z/m)^\times$.
If $n\not\equiv a$ but $(n,m)=1$, both sides are $0$ by orthogonality.
If $(n,m)>1$, RHS is $0$ (all $\psi(n)=0$) and LHS is $0$ since $(a,m)=1$. ∎

Hence with $(\chi\psi)(n)=\chi(n)\psi(n)$,
$$S=\frac1{\phi(m)}\sum_{\psi}\bar\psi(a)\,T_\psi,\qquad
T_\psi=\sum_{n\in I}(\chi\psi)(n).\tag{6}$$
So $|S|\le\phi(m)^{-1}\sum|T_\psi|$ and $|R-Q/2|\le(2\phi(m))^{-1}\sum|T_\psi|$.

## 4. Conductors

**Lemma 3.** *Let $(p,m)=1$. Then $\chi\psi$ (character mod $pm$) is nonprincipal.
Let $f=\mathrm{cond}(\psi)$ ($f=1$ if principal, $f\mid m$), $\psi^{*}$ the primitive
inducing $\psi$. Then $\chi^{*}:=\chi\psi^{*}$ is primitive mod $q:=pf$,
induces $\chi\psi$, so $q_\psi=q\mid pm$. If $\psi$ principal, $q=p$.*

*Proof.* Nonprincipal: pick $u$ with $\chi(u)=-1$; by CRT choose $n\equiv u(p)$,
$n\equiv 1(m)$; then $\psi(n)=1$, $(\chi\psi)(n)=-1$.
For primitivity use coprimality: if $\xi_1,\xi_2$ are primitive of coprime moduli
$q_1,q_2$, $\xi_1\xi_2$ is primitive mod $q_1q_2$. Indeed if it were induced from
$d\mid q_1q_2$, $d<q_1q_2$, write $d=d_1d_2$, $d_i\mid q_i$; taking
$n\equiv 1(d)$, $n\equiv g(q_1)$ with $\xi_1(g)\ne1$ (possible by primitivity)
and $n\equiv1(q_2)$ via CRT forces $d_1=q_1$, similarly $d_2=q_2$.
Apply with $q_1=p$, $q_2=f$. The lift $\psi(n)=\psi^{*}(n)$ when $(n,m)=1$,
$0$ else, and $\chi(n)=0\iff p\mid n$, matches induction from $q$ to $pm$. ∎

Conductor census: number of $\psi\bmod m$ with $\mathrm{cond}=f$ is
$N_f=\#\{\text{primitive mod }f\}$, $N_1=1$, $N_f=\sum_{d\mid f}\mu(f/d)\phi(d)$ for $f>1$,
$\sum_{f\mid m}N_f=\phi(m)$. E.g. $N_2=N_6=N_{10}=0$ (no primitive mod 2,6,10).
Thus $\sum_\psi F(q_\psi)=\sum_{f\mid m}N_fF(pf)$.

## 5. Imprimitive-to-primitive reduction (the $\kappa$ correction)

**Lemma 4.** *Let $Q_0=pm$, $q\mid Q_0$ the conductor, $\chi^{*}$ the primitive.
Let $T=\sum_{n\in I}(\chi\psi)(n)$. Then $|T|\le\kappa B^{*}(q)$ where
$\kappa=\#\{d\mid Q_0:(d,q)=1,\ \mu(d)\ne0\}=2^{t}$,
$t=\#\{\ell\mid Q_0:\ell\nmid q\}$. Since $p\mid q$,
$t=\#\{\ell\mid m:\ell\nmid f\}\le\omega(m)$.*

*Proof.* $(\chi\psi)(n)=\chi^{*}(n)$ if $(n,Q_0)=1$, else $0$; both are $0$ if
$(n,q)>1$ (as $q\mid Q_0$). So $T=\sum_{n\in I}\chi^{*}(n){\bf1}_{(n,Q_0)=1}$.
Möbius: ${\bf1}_{(n,Q_0)=1}=\sum_{d\mid n,\,d\mid Q_0}\mu(d)$. Hence
$T=\sum_{d\mid Q_0}\mu(d)\sum_{n\in I,\,d\mid n}\chi^{*}(n)$.
If $(d,q)>1$, $\chi^{*}(d)=0$ kills the term; else writing $n=dk$,
$\chi^{*}(n)=\chi^{*}(d)\chi^{*}(k)$, inner sum is $\chi^{*}(d)\sum_{k:dk\in I}\chi^{*}(k)$,
an interval of length $H/d$, bounded by $B^{*}(q)$ via Lemma 1.
Triangle gives $|T|\le B^{*}(q)\sum_{d\mid Q_0,(d,q)=1}1=\kappa B^{*}(q)$. ∎

*Why $\kappa$ cannot be omitted.* Take $m=2$, $\psi$ principal. Then
$T=\sum_{n\in I,\,n\,{\rm odd}}\chi(n)=S(I)-\chi(2)S(I/2)$, two primitive sums;
$|T|\le 2B^{*}(p)$. No primitive mod $2p$ with this $p$-part exists ($N_2=0$),
so $B^{*}(p)$ alone is false in general. Our $\kappa=2$ is sharp for this method.

Combining (6) and Lemmas 3–4 gives (2), and with $B^{*}\le19\sqrt q\log q$ gives (3).
For $m=1$ this is $|R-Q/2|\le B^{*}(p)/2$, the pure short-interval case.

## 6. $Q$ lower bound and $H_0$

**Lemma 5.** *Let $K=\#\{n\in I:n\equiv a(m)\}$, $Q_0=\#\{n\in I:n\equiv a(m),p\mid n\}$.
Then $K\ge H/m-1$ (indeed $K\ge\lfloor H/m\rfloor$) and $Q_0<H/(pm)+1$.
Hence with $Q=K-Q_0$,*
$$Q>\frac{H}{m}\Bigl(1-\frac1p\Bigr)-2.\tag{7}$$
*Proof.* $K$ is $\lfloor(H+r)/m\rfloor$-type; an interval of length $H$ meets each
residue at least $\lfloor H/m\rfloor>H/m-1$ times. The $Q_0$ points lie in one
residue mod $pm$ (CRT, as $(m,p)=1$); $k$ such points span $\ge(k-1)pm<H$,
so $k<H/(pm)+1$. ∎

*Corollary proof.* If $E<Q/2$ then $|R-Q/2|<Q/2$, so $0<R<Q$: both signs occur.
By (7) it suffices that $E\le L(H)/2$ with $L(H)=H(1-1/p)/m-2>0$,
i.e. $H>m(2E+2)/(1-1/p)=H_0$. If $H\ge pm$ the claim is also elementary:
$H\ge pm$ gives $K\ge p$ consecutive progression terms covering all of
$\mathbf F_p$, hence both Legendre values (plus at most one $0$). So $H>H_0$
always forces mixed signs, whether $H_0<pm$ (via the bound) or $H_0\ge pm$
(via the period). ∎

The target's "$H/m-1$" omits the $-H/(pm)-1$ $p$-correction; (4) is the honest form.

## 7. Tables

$E(p,m)=(2\phi(m))^{-1}\sum_{f\mid m}N_f\kappa_fB^{*}(pf)$,
$\kappa_f=2^{\omega(m)-\omega(f)}$, $H_0$ by (4). Values (two-term $B^{*}$):

| $m$ | $H_0(101,m)$ | $H_0(1009,m)$ | $H_0(4999,m)$ |
|---|---|---|---|
| 1 | 63.6 | 142.9 | 304.3 |
| 2 | 250.2 | 567.5 | 1213.1 |
| 3 | 322.0 | 781.8 | 1717.2 |
| 4 | 449.1 | 1114.6 | 2468.0 |
| 5 | 562.6 | 1501.9 | 3410.2 |
| 6 | 1275.7 | 3115.1 | 6856.7 |
| 8 | 973.5 | 2671.1 | 6112.5 |
| 10 | 2230.1 | 5987.7 | 13620.6 |
| 12 | 2335.1 | 6193.4 | 14019.4 |
| 20 | 4202.7 | 12083.1 | 27976.0 |

Full CSV for $m\le20$, $p\in\{3,5,7,11,101,1009,4999\}$ in `artifacts/h0_table.csv`
(column `note` flags $H_0\ge pm$ trivial-regime, common for tiny $p$).
Single-term (3) is looser by factor $\approx 19/0.2/\log q$; we tabulate the tight two-term version.

## 8. Computational verification (reproducible)

Scripts: `artifacts/verify_main.py`, `artifacts/check_h0.py`
(summary `verification_summary.csv`, table `h0_table.csv`).
Legendre via Euler `pow(r,(p-1)//2,p)`; numpy vectorized.

Key trick (exact, not heuristic): $b_n={\bf1}_{n\equiv a}\chi(n)$ is $pm$-periodic
with period sum $0$ (progression of length $p$ covers all $\mathbf F_p$,
$\sum_{\mathbf F_p}\chi=0$). Hence prefix $P$ is $pm$-periodic and
$\max_{N,H\le pm}|S(N,H)|=\max P-\min P$ over one period; longer $H$ reduces to
remainder plus zero-mean full periods. So $O(pm)$ per $(p,m,a)$ suffices; no
$O((pm)^2)$ scan needed.

Results:
- Main inequality (2): all odd $p\le5000$ (668 primes), $1\le m\le10$, $(m,p)=1$,
  all $(a,m)=1$: **21352 cases, 0 failures**. Worst ratio
  $(\max|S|/2)/E=0.465245$ at $(p,m,a)=(4957,1,1)$ ($\max|S|=140$, $E=150.46$).
  Per-$m$ worst ratios $0.10$–$0.47$ (see `verification_summary.csv`). Bound is loose
  for small $p$ (PV weak there) and tightens relatively at large $p$ — expected.
- $H_0$ forcing: for $H_1=\lfloor H_0\rfloor+1<pm$, sliding-window check of all
  $N\bmod pm$ that $(N,N+H_1]$ has $R>0$ and $R<Q$: **20154 combos, 0 failures**;
  361 combos have $H_1\ge pm$ (trivial full-period regime, verified by covering argument).
- $Q$ bound (7) spot-checked against brute counts; period-sum-zero asserted in code.

## 9. Limitations, conjecture, uncertainty

- PROVED: corrected (2)–(4) with $\kappa$, $Q$ bound, $H_0$, single-term $19$,
  plus exhaustive check $p\le5000$, $m\le10$.
- COMPUTED (not proved analytically): numeric values $C_0$, $B^{*}(3)$, ratio max;
  floating error $\ll$ margins ($0.48$ for $C=19$, $\ge1.2$ for even-majorant);
  verification outputs.
- NOT proved (and false as stated): verbatim target without $\kappa$; $H/m-1$ threshold
  without $p$-correction. We flag, correct, and do not claim the stronger form.
- Uncertainty: Frolenkov constants taken from ar5iv HTML rendering; cross-checked
  against Pomerance-type shape but not re-derived from scratch. Verification covers
  $m\le10$ only; $m\le20$ table is analytic extrapolation (same formula, not brute-forced
  for $11\le m\le20$). Asymptotic originality is nil — this is textbook orthogonality +
  bookkeeping; the delta is making it fully explicit with exact conductor/Möbius counts
  and a runnable check, which to our knowledge is absent from Frolenkov/McGown–Trifonov/
  Treviño/Wright in this joint form.
- Small-$H$ regime: for $H\le H_0$ the theorem says nothing; brute data show mixed signs
  often occur much earlier. Improving $H_0$ needs Burgess/smaller PV constants, out of scope.

## References

- D. A. Frolenkov, Numerically explicit version of the Pólya–Vinogradov inequality,
  arXiv:1107.0381 (2011), Thm 1 (our Lemma 1; $C_0=4\pi^{5/2}+5$).
- C. Pomerance, Remarks on the Pólya–Vinogradov inequality, Integers 11A (2011)
  (prior explicit form $2/\pi^2\sqrt q\log q+\cdots$ improved by Frolenkov).
- E. Dobrowolski–K. Williams; G. Bachman–L. Rachakonda (explicit PV predecessors).
- L. Goldmakher; A. Granville–K. Soundararajan (asymptotic/pretentious improvements, not explicit here).
- Iwaniec–Kowalski, Analytic Number Theory, Ch. 12 (PV + imprimitive reduction background).
- K. McGown; T. Trifonov; T. Treviño (explicit Burgess/least-nonresidue, interval-only).
- S. Wright, Quadratic residues/nonresidues in arithmetic progression, arXiv:1111.2236
  (inexplicit AP-pattern asymptotics, no finite-$p$ $H_0$).
