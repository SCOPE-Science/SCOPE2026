# Complete censuses and largest-size witnesses for simultaneous (4,5,7)-cores and (5,6,7)-cores

## Context

A partition is a $t$-core if no hook length in its Young diagram is a multiple of $t$,
and an $(s,t,u)$-core if it is simultaneously an $s$-, $t$-, and $u$-core.
For coprime pairs, Anderson enumerated $(s,t)$-cores and Olsson–Stanton/Johnson
determined the maximal size; for consecutive triples $(s,s+1,s+2)$,
Yang–Zhong–Zhou gave count/maximum/average formulas and Xiong gave largest-size
formulas, but no source recorded full size distributions, Durfee data, every
beta-set, or explicit witness partitions for the triples $(4,5,7)$ (non-interval)
and $(5,6,7)$.

## Definitions

For a partition $\lambda=(\lambda_1,\dots,\lambda_\ell)$ let
$B(\lambda)=\{\lambda_i+\ell-i:1\le i\le\ell\}\subset \mathbb{N}_{>0}$
be its beta-set (first-column hook lengths).
$\lambda$ is a $t$-core iff $B(\lambda)$ is $t$-flush:
$b\in B,\ b\ge t \Rightarrow b-t\in B$.
$|\lambda|=\sum B-\ell(\ell-1)/2$.
The Durfee size is $\max\{k:\lambda_k\ge k\}$.
The hook multiset is computed from the Young diagram in the usual way.

## Result (census)

(a) **$(4,5,7)$-cores.** There are exactly **10** simultaneous $(4,5,7)$-cores.
Size distribution (size: count): $0{:}1,\ 1{:}1,\ 2{:}2,\ 3{:}3,\ 4{:}1,\ 6{:}2$
(no core of size $5$ or $\ge 7$).
Maximum size is **6**, attained by exactly two partitions:
$\lambda=(4,1,1)$ with beta-set $\{1,2,6\}$ and
$\lambda=(3,1,1,1)$ with beta-set $\{1,2,3,6\}$
(both Durfee size $1$, hook multiset $\{1,1,2,2,3,6\}$).

Full list (size, partition, beta-set, Durfee):
$(0,[],[],0)$, $(1,[1],[1],1)$,
$(2,[1,1],[1,2],1)$, $(2,[2],[2],1)$,
$(3,[1,1,1],[1,2,3],1)$, $(3,[2,1],[1,3],1)$, $(3,[3],[3],1)$,
$(4,[2,2],[2,3],2)$,
$(6,[3,1,1,1],[1,2,3,6],1)$, $(6,[4,1,1],[1,2,6],1)$.

(b) **$(5,6,7)$-cores.** There are exactly **21** simultaneous $(5,6,7)$-cores.
Size distribution: $0{:}1,\ 1{:}1,\ 2{:}2,\ 3{:}3,\ 4{:}5,\ 5{:}2,\ 6{:}2,\ 8{:}2,\ 9{:}1,\ 12{:}2$
(no core of size $7,10,11$ or $\ge 13$).
Maximum size is **12**, attained by exactly two partitions:
$\lambda=(6,2,2,2)$ with beta-set $\{2,3,4,9\}$ and
$\lambda=(4,4,1,1,1,1)$ with beta-set $\{1,2,3,4,8,9\}$
(both Durfee size $2$, hook multiset $\{1,1,2,2,2,3,3,3,4,4,8,9\}$).

Full list (size, partition, beta-set, Durfee):
$(0,[],[],0)$, $(1,[1],[1],1)$,
$(2,[1,1],[1,2],1)$, $(2,[2],[2],1)$,
$(3,[1,1,1],[1,2,3],1)$, $(3,[2,1],[1,3],1)$, $(3,[3],[3],1)$,
$(4,[1,1,1,1],[1,2,3,4],1)$, $(4,[2,1,1],[1,2,4],1)$, $(4,[2,2],[2,3],2)$,
$(4,[3,1],[1,4],1)$, $(4,[4],[4],1)$,
$(5,[2,2,1],[1,3,4],2)$, $(5,[3,2],[2,4],2)$,
$(6,[2,2,2],[2,3,4],2)$, $(6,[3,3],[3,4],2)$,
$(8,[4,1,1,1,1],[1,2,3,4,8],1)$, $(8,[5,1,1,1],[1,2,3,8],1)$,
$(9,[5,1,1,1,1],[1,2,3,4,9],1)$,
$(12,[4,4,1,1,1,1],[1,2,3,4,8,9],2)$, $(12,[6,2,2,2],[2,3,4,9],2)$.

Pair cross-checks: $(4,5)$-cores: 14; $(5,6)$-cores: 42,
matching Anderson's formula $\binom{s+t}{s}/(s+t)$.

## Proof / evidence

Beta-set criterion is the classical James/Anderson abacus fact, machine-checked
here on all partitions to size 12 (flush $\Leftrightarrow$ hook-free for
$t\in\{4,5,6,7\}$). Depth-first search over $[1,st-1]$ imposing
$b\in B\Rightarrow b-s,b-t\in B$ enumerates exactly the Anderson numbers
14 for $(4,5)$ and 42 for $(5,6)$; filtering by $7$-flushness yields 10 and
21 sets. Each surviving beta-set is inverted to a partition and its size,
Durfee square, and full hook multiset recomputed from scratch; every hook
multiset is verified free of multiples of the triple. Maxima are read off the
complete finite lists; the headline hook multisets above certify core status
by hand-checkable arithmetic. An independent exhaustive partition hook-scan to
the classical pair max-size bounds $(4,5)$: 15 and $(5,6)$: 35 finds exactly
the same 10 and 21 partitions, proving completeness independently of the
abacus-bound argument.

## Limitations

Completeness rests on the finite abacus-ideal search plus replayable code, not
on hand case analysis. The beta-flush lemma is cited as classical with a machine
check on the needed range. No asymptotic or general-$n$ claims are made.
For $(5,6,7)$ the bare aggregates (count 21, max value 12, two maximizers) are
implied by the Yang–Zhong–Zhou/Xiong interval formulas and are not claimed as
new; the new content is the full distributions, Durfee data, beta-sets, and
named witnesses.

## Reproducibility

Stdlib-only `verify_cores.py` replays counts, hooks, flush conditions,
beta-partition round-trips, sizes, and Anderson numbers from `census_data.json`
and prints `VERIFY_OK` in seconds:
`python3 verify_cores.py` run in the directory containing `census_data.json`.

## References

- Anderson (2002), Partition identities and the number of $(s,t)$-core partitions.
- Yang–Zhong–Zhou (2014), On the Enumeration of $(s,s+1,s+2)$-Core Partitions, arXiv:1406.2583.
- Xiong (2014), On the largest size of $(t,t+1,\dots,t+p)$-core partitions, arXiv:1410.2061.
- Baek–Nam–Yu (2017), Johnson's bijections and counting simultaneous cores, arXiv:1711.01469.
- Yan–Yu–Zhou (2019), On self-conjugate $(s,\dots,s+k)$-cores, arXiv:1905.00570.
- Li–Sha–Xiong (2024), Asymptotic normality of core statistics, arXiv:2410.18596.
