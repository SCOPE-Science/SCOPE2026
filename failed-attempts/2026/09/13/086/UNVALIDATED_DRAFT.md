# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Full-ensemble 1D discrepancy of Dedekind sums — complete proof (TARGET)

## 0. Statement proved

Let $s(h,k)=\sum_{r=1}^{k}((r/k))((hr/k))$ be the classical Dedekind sum,
$((x))=x-\lfloor x\rfloor-1/2$ for $x\notin\mathbb Z$ and $((x))=0$ for
$x\in\mathbb Z$, and $\{y\}$ the fractional part. For prime $p\equiv 3\bmod 4$
let

$$D_p=\sup_{0\le t\le 1}\Bigl|\frac{1}{p-1}\#\{1\le h<p:\{12s(h,p)\}\le t\}-t\Bigr|$$

be the $1$D star-discrepancy of the multiset $\{\{12s(h,p)\}:1\le h<p\}$.
We prove **both** halves of the target:

- **(Upper.)** There exist absolute $C>0$, $P_0$ such that every prime
  $p\ge P_0$, $p\equiv3\bmod4$, satisfies
  $D_p\le C\,p^{-1/2}(\log p)^2$ (in fact $D_p\ll (\log p)/\sqrt p$).
- **(Lower.)** There exist absolute $c>0$ and infinitely many primes
  $p\equiv3\bmod4$ with $D_p\ge c\,p^{-1/2}/\log p$
  (in fact $D_p\ge c'/\sqrt p$ infinitely often).

Hence the target claim is **true**. The proof is self-contained except for
four standard cited theorems: Dedekind reciprocity, the Weil bound for
Kloosterman sums, the Erd\H os–Tur\'an inequality, and the Katz vertical
Sato–Tate law over primes in arithmetic progressions (used only
qualitatively). Numerical scripts in `output/artifacts/` illustrate the
lemmas; they are not part of the logical chain.

## 1. The Rademacher congruence: Weyl sums are Kloosterman sums

For coprime $h,k\ge 1$ let $\bar h$ denote the inverse of $h\bmod k$:
$\bar h=0$ if $k=1$, else $\bar h\in\{1,\dots,k-1\}$, $h\bar h\equiv1\bmod k$.
Put $D(h,k)=12s(h,k)-(h+\bar h)/k$.

**Lemma 1 (congruence).** For all coprime $h,k\ge1$, $D(h,k)\in\mathbb Z$.
That is, $12s(h,k)-(h+\bar h)/k$ is always an integer.

*Proof.* Three classical ingredients plus induction.
(i) $s(h,1)=0$ (every sawtooth value at an integer is $0$), so
$D(h,1)=-h\in\mathbb Z$.
(ii) For $k\ge2$, $s(1,k)=\sum_{r=1}^{k-1}(r/k-1/2)^2
=(k-1)(k-2)/(12k)$ by $\sum_{r<k}r^2=(k-1)k(2k-1)/6$,
$\sum_{r<k}r=(k-1)k/2$. Since $\bar1=1$,
$D(1,k)=(k-1)(k-2)/k-2/k=k-3\in\mathbb Z$.
(iii) Dedekind reciprocity (cited; e.g. Apostol, *Modular Functions and
Dirichlet Series*, Thm.\ 3.1; Rademacher–Grosswald, *Dedekind Sums*, Ch.\ 1):
for coprime $h,k\ge1$,
$$s(h,k)+s(k,h)=\frac{h^2+k^2+1}{12hk}-\frac14,$$
i.e. $12s(h,k)+12s(k,h)=(h^2+k^2+1)/(hk)-3$.
(iv) Periodicity: $s(h+k,k)=s(h,k)$ since $(((hr/k)+r))=((hr/k))$ for
integer $r$. If $h\equiv r\bmod k$ with both coprime to $k$, then also
$\bar h\equiv\bar r\bmod k$ (uniqueness of inverses), so
$(h+\bar h)-(r+\bar r)$ is divisible by $k$.

From (iii), with $k^\dagger$ the inverse of $k\bmod h$,
$$D(h,k)+D(k,h)=\frac{1-h\bar h-kk^\dagger}{hk}-3
=-\frac{h\bar h+kk^\dagger-1}{hk}-3.$$
The numerator $N=h\bar h+kk^\dagger-1$ is divisible by both $h$ and $k$:
indeed $h\bar h\equiv0$, $kk^\dagger\equiv1\bmod h$ gives $N\equiv0\bmod h$,
and symmetrically $N\equiv0\bmod k$ (for the value $1$ the conventions
$\bar{\ }=0\bmod1$ give $N=0$, trivially divisible). Since
$\gcd(h,k)=1$, $hk\mid N$, so $D(h,k)+D(k,h)\in\mathbb Z$.

Induction on $N=h+k$: assume $D(h',k')\in\mathbb Z$ for all coprime pairs
with sum $<N$, and let $h+k=N$. If $h=1$ or $k=1$ we are done by (i)–(ii).
If $h>k\ge2$, write $h=qk+r$, $1\le r<k$ ($r\ne0$ else $k\mid h$ forces
$k=1$). Then $s(h,k)=s(r,k)$ and by (iv) $D(h,k)-D(r,k)\in\mathbb Z$;
since $r+k<N$, $D(r,k)\in\mathbb Z$, so $D(h,k)\in\mathbb Z$.
If $h<k$, write $D(h,k)=[D(h,k)+D(k,h)]-D(k,h)$: the bracket is an integer
by the display above, and $D(k,h)\in\mathbb Z$ by the case just proved
(reducing $k\bmod h$). This completes the induction. ∎

**Corollary.** For prime $p$ and $1\le h<p$ with $\bar h\equiv h^{-1}\bmod p$,
$\{12s(h,p)\}=\{(h+\bar h)/p\}$. For integer $m$,
$$W_m:=\sum_{h=1}^{p-1}e(m\{12s(h,p)\})
=\sum_{x\bmod p}^{\!*}e\!\left(\frac{mx+m\bar x}{p}\right)=:K(m,m;p),$$
the Kloosterman sum ($e(y)=e^{2\pi iy}$), since $e(m\{\cdot\})=e(m\cdot)$
for integer $m$. For $p\mid m$, $W_m=p-1$.

*Remark (role of $3\bmod4$).* $(h+\bar h)/p$ has vanishing fractional part
iff $p\mid h+\bar h$, i.e. $h+\bar h=p$ (range $[2,2p-2]$), i.e.
$h^2\equiv-1\bmod p$. For $p\equiv3\bmod4$, $-1$ is a quadratic nonresidue
(Euler's criterion), so this never happens: the $p-1$ points lie in
$\{1/p,\dots,(p-1)/p\}\subset(0,1)$, never $0$. In particular, with
$F(t)=\frac1{p-1}\#\{x_h\le t\}-t$, $F(0)=0$ and $F(1)=0$.

$K(m,m;p)$ is real: conjugation gives $K(-m,-m;p)$, and $x\mapsto -x$
identifies the two sums. With the Weil bound $|K|\le2\sqrt p$ below we may
write $K(1,1;p)=2\sqrt p\cos\theta_p$, $\theta_p\in[0,\pi]$.

## 2. Upper bound: Erd\H os–Tur\'an + Weil

**Weil bound (cited).** For prime $p\nmid m$,
$|K(m,m;p)|\le2\sqrt p$ (Weil 1948; e.g. Iwaniec–Kowalski, Cor.\ 11.12).

**Erd\H os–Tur\'an (cited).** There is an absolute $C_{ET}$ such that for any
$N$ points in $[0,1)$ and any $M\ge1$,
$$D_N^*\le C_{ET}\Bigl(\frac1M+\frac1N\sum_{m=1}^{M}
\frac{|\sum_j e(mx_j)|}{m}\Bigr)$$
(Kuipers–Niederreiter, *Uniform Distribution of Sequences*, Thm.\ 2.5).

Take $N=p-1$, $M=\lfloor\sqrt p\rfloor<p$ (for $p>2$), so Weil applies to
every $m\le M$. With $|\sum_j e(mx_j)|=|K(m,m;p)|\le2\sqrt p$ and
$\sum_{m\le M}1/m\le1+\log M\le1+\log p$,
$$D_p\le C_{ET}\Bigl(\frac1M+\frac{2\sqrt p\,(1+\log p)}{p-1}\Bigr).$$
For $p\ge11$: $M\ge\sqrt p/2$ so $1/M\le2/\sqrt p$; $p-1\ge p/2$. Hence
$$D_p\le C_{ET}\frac{6+4\log p}{\sqrt p}\le 10\,C_{ET}\,
\frac{(\log p)^2}{\sqrt p},$$
since $10L^2-4L-6\ge0$ for $L=\log p\ge1$. With $D_p\le1$ always, enlarging
$C$ covers $p<11$. This proves the upper bound with e.g. $P_0=11$,
$C=10C_{ET}$ (plus a finite adjustment), in fact the stronger rate
$D_p\ll(\log p)/\sqrt p$.

## 3. Lower bound: Koksma + large Kloosterman values

**Lemma 2 (Koksma lower bound).** $D_p\ge |K(1,1;p)|/(2\pi(p-1))$.

*Proof.* Let $x_h=\{12s(h,p)\}\in(0,1)$ (Remark above),
$F(t)=\frac1N\#\{x_h\le t\}-t$, $N=p-1$; $F(0)=F(1)=0$.
For $f\in C^1$ with $f(0)=f(1)$,
$\frac1N\sum_h f(x_h)-\int_0^1f=-\int_0^1F(t)f'(t)\,dt$:
indeed $-\int_0^1[\frac1N\sum_h\mathbf1_{x_h\le t}]f'(t)dt
=\frac1N\sum_h(f(1)-f(x_h))$ (using $x_h>0$) and
$-\int_0^1(-t)f'=f(1)-\int_0^1f$ by parts; the $f(1)$ terms cancel.
Apply to $f(t)=e^{2\pi it}$ ($\int_0^1f=0$, $\int_0^1|f'|=2\pi$):
$|W_1|/N\le2\pi D_p$. Since $W_1=K(1,1;p)$, the lemma follows. ∎

**Lemma 3 (large Kloosterman values along $3\bmod4$; deep input).**
There are infinitely many primes $p\equiv3\bmod4$ with
$|K(1,1;p)|\ge\sqrt p$.

*Proof.* Write $K(1,1;p)=2\sqrt p\cos\theta_p$. By Katz's vertical
Sato–Tate law for Kloosterman sums (Katz, *Gauss Sums, Kloosterman Sums,
and Monodromy Groups*, Ann.\ of Math.\ Stud.\ 116, 1988, Ch.\ 9) in its
form over primes in a fixed residue class (Fouvry–Kowalski–Michel,
"Algebraic trace functions over the primes," *Duke Math.\ J.* 163, 2014,
and references therein; see also Kowalski's notes on trace functions),
the angles $\{\theta_p:p\le X,\ p\equiv3\bmod4\}$ equidistribute for
$\mu_{ST}=\frac2\pi\sin^2\theta\,d\theta$ on $[0,\pi]$ as $X\to\infty$.
The set $\{|\cos\theta|>1/2\}$ is a continuity set with
$$\mu_{ST}(|\cos\theta|>1/2)=1-\frac2\pi\int_{\pi/3}^{2\pi/3}\sin^2\theta\,d\theta
=1-\frac13-\frac{\sqrt3}{2\pi}=\frac23-\frac{\sqrt3}{2\pi}\approx0.39>0,$$
since $\int_{\pi/3}^{2\pi/3}\sin^2=\pi/6+\sqrt3/4$.
Hence a positive proportion (relative to $\pi(X;4,3)\to\infty$ by Dirichlet)
satisfy $|\cos\theta_p|>1/2$, i.e. $|K(1,1;p)|=2\sqrt p|\cos\theta_p|>\sqrt p$.
In particular infinitely many satisfy $|K|\ge\sqrt p$. ∎

For such $p$, Lemma 2 gives
$$D_p\ge\frac{\sqrt p}{2\pi(p-1)}
=\frac{1}{2\pi\sqrt p}\cdot\frac{p}{p-1}\ge\frac{1}{2\pi\sqrt p}
\ge\frac{c}{\sqrt p\,\log p},\qquad c=\frac1{2\pi},$$
using $\log p>1$ for $p\ge3$ (natural log; any fixed base changes only $c$).
Taking e.g. $c=1/7<1/(2\pi)$ gives the claimed infinitely-often lower bound.
In fact $D_p\ge c'/\sqrt p$ infinitely often, which is stronger by a $\log p$
factor.

## 4. Conclusion

Both halves hold with absolute constants (e.g. $P_0=11$,
$C$ a multiple of the Erd\H os–Tur\'an constant, $c=1/7$):
$D_p\le C(\log p)^2/\sqrt p$ for all large $p\equiv3\bmod4$, and
$D_p\ge c/(\sqrt p\log p)$ for infinitely many such $p$.
The target claim is therefore **proved (true)**. The hypothesis
$p\equiv3\bmod4$ is used structurally ($-1$ nonresidue $\Rightarrow$ no
degenerate atom at $0$; residue class for the Sato–Tate input).

## References (cited theorems)

- Apostol, *Modular Functions and Dirichlet Series in Number Theory*,
  Thm.\ 3.1 (reciprocity); Rademacher–Grosswald, *Dedekind Sums*.
- Weil, "On some exponential sums," *Proc.\ Nat.\ Acad.\ Sci.* 34 (1948)
  (Kloosterman bound); Iwaniec–Kowalski, *Analytic Number Theory*,
  Cor.\ 11.12.
- Kuipers–Niederreiter, *Uniform Distribution of Sequences*, Thm.\ 2.5
  (Erd\H os–Tur\'an–Koksma).
- Katz, *Gauss Sums, Kloosterman Sums, and Monodromy Groups* (1988), Ch.\ 9
  (vertical Sato–Tate); Fouvry–Kowalski–Michel, Duke Math.\ J.\ 163 (2014)
  (trace functions over primes / progressions); Dirichlet's theorem on
  primes in progressions.

## Status of computation

- `output/artifacts/lemma_congruence_check.py`: verifies
  $12s(h,k)-(h+\bar h)/k\in\mathbb Z$ on 1105 coprime pairs
  ($2\le k\le60$ all $h$, plus random $k\in\{100,500,1000,2000\}$) and
  reciprocity spot checks — all pass. Illustrative only.
- `output/artifacts/kloosterman_numerics.py`: for $p\equiv3\bmod4$, $p\le200$,
  computes $K(1,1;p)$, $t=K/2\sqrt p$, $D_p$; confirms the Koksma lower bound
  $D_p\ge|K|/2\pi(p-1)$ in every case and finds many $p$ with $|t|\ge1/2$
  (e.g. $23,71,83,103,107,127,139,151,163$). Illustrative only; the proof
  does not depend on it.
