# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of a dilated Capparelli-type companion at modulus 12 with a mod-7 family

## 1. Statement

Let $D(n)$ count partitions of $n$ into distinct parts with no part equal to $1$,
successive gaps $\lambda_i-\lambda_{i+1}\ge 2$, and gap $\ge 4$ whenever the larger
part $\lambda_i$ is even (with $D(0)=1$). Let

$$P(q)=(-q;q)_\infty\,\frac{(q^{12};q^{12})_\infty}
{(q^2;q^{12})_\infty\,(q^{10};q^{12})_\infty}=\sum_{n\ge 0}P(n)q^n.$$

**Theorem.** (i) $\sum_n D(n)q^n \ne P(q)$: the identity fails at the first
possible coefficient, $D(1)=0\ne 1=P(1)$, while $D(0)=P(0)=1$ rules out any
monomial prefactor rescue $q^c$. (ii) The congruence $d(7n+3)\equiv 0\pmod 7$
is false at its first term: $D(3)=1$. (iii) Certifying the obstructed residue:
no residue class mod 7 vanishes identically — each class $r\in\{0,\dots,6\}$
has a failing witness $m\equiv r\pmod 7$ with $m\le 8$ and $D(m)\not\equiv 0
\pmod 7$ (witnesses $0,8,2,3,4,5,6$ with values $1,3,1,1,1,1,1$).

Hence neither the product identity (up to prefactor) nor any mod-7 residue
congruence family holds; the obstruction log above is sharp.

## 2. The partition side

Define $G(r,L)$ = number of admissible partitions of $r$ whose parts are all
$< $ bound determined by largest part $L$ ($L=0$ means no constraint yet):
$G(0,L)=1$, and for $r>0$, $G(r,0)=\sum_{k=2}^{r}G(r-k,k)$,
$G(r,L)=\sum_{k=2}^{\min(r,\,L-4\text{ or }L-2)}G(r-k,k)$ with $L-4$ if $L$
even else $L-2$. Then $D(n)=G(n,0)$. Two independent implementations
(memoized recursion; bottom-up iterative table) agree to $n=300$, and
brute-force subset enumeration agrees for $n\le 10$.

Hand-checkable seed: $D(0..8)=1,0,1,1,1,1,1,2,3$. E.g. $D(1)=0$ (part 1
forbidden); $D(3)=1$ (only $[3]$, since $[2{+}1]$ uses a forbidden 1);
$D(8)=3$ ($[8]$, $[6,2]$ with even gap $4$, $[5,3]$ with odd gap $2$;
$[7,?]$ and $[4{+}3{+}1]$-type options excluded by gap/no-1 rules).

## 3. The product side

Two independent expansions of $P(q)$ agree to $n=300$: (a) incremental
multiplication by $(1+q^k)$, $(1-q^{12k})$, and prefix-sum multiplication by
$1/(1-q^{12k+2})$, $1/(1-q^{12k+10})$; (b) separate numerator/denominator
polynomials followed by series division. Both give
$P(0..8)=1,1,2,3,4,6,8,11,14$.

Analytically, $P(1)=1$: $(-q;q)_\infty=1+q+O(q^2)$ while every mod-12 factor
is $1+O(q^2)$, so the linear term can only come from $(-q;q)_\infty$.

## 4. Disproof

(i) $D(1)=0\ne 1=P(1)$ with $D(0)=P(0)=1$: any monomial prefactor $q^cP$
forces $c=0$ from the constant term, hence fails at $n=1$. Natural binomial
rescues fail concretely: $P(1-q)$ matches $D$ only to $n=4$ (fails at $n=5$:
$2$ vs $1$); $P/(1+q)$ already fails at $n=2$ ($2$ vs $1$); the ratio series
$D/P$ is densely nonzero (295 of 301 coefficients to $n=300$), excluding any
sparse-prefactor rescue.

(ii) $D(3)=1\not\equiv 0\pmod 7$ kills $d(7n+3)\equiv 0$ at $n=0$.

(iii) Residue census (dual-DP verified to $n=150$): first $m\equiv r\pmod 7$
with $D(m)\not\equiv 0\pmod 7$ is $m=0,8,2,3,4,5,6$ for $r=0,\dots,6$.
So every residue class is obstructed by a hand-checkable witness ($m\le 8$).

## 5. Reproduction

Run `python3 output/artifacts/verify.py` (stdlib only) → `VERIFY_OK`.
It checks dual-DP agreement, brute force to $n=10$, dual-product agreement,
both first-coefficient failures, the prefactor-rescue failures, and the full
seven-residue witness table.

## 6. Scope

This disproves the stated product and mod-7 family for the exact predicate
(distinct, no 1, gap $\ge 2$, $\ge 4$ above an even part) and the exact
product $(-q;q)_\infty(q^{12};q^{12})_\infty/((q^2;q^{12})_\infty
(q^{10};q^{12})_\infty)$. It does not rule out other dilations, other gap
predicates, or congruences at other moduli.
