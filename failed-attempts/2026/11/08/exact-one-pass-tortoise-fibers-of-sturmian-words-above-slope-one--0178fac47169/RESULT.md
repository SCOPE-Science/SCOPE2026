# Exact one-pass tortoise fibers of Sturmian words above slope one-third

## Finding

Let \(\alpha\) be any irrational number strictly between \(1/3\) and \(1\), and let \(\mathcal L_\alpha(n)\) be the set of length-\(n\) factors of a binary Sturmian word of slope \(\alpha\). Set \(\tau(0^j1u)=0^ju1\) and \(\tau(0^j)=0^j\). Define the one-tortoise complexity by
\[
\rho^\tau_\alpha(n)=|\{\tau(w):w\in\mathcal L_\alpha(n)\}|.
\]
For every integer \(n\ge1\), its exact value is
\[
\rho^\tau_\alpha(n)=
\begin{cases}
2,&n=1,\\
n,&1/2<\alpha<1,\quad n\ge2,\\
2,&1/3<\alpha<1/2,\quad n\in\{2,3\},\\
n-1,&1/3<\alpha<1/2,\quad n\ge4.
\end{cases}
\]

More precisely, write \(c=c_0c_1\cdots\) for the characteristic mechanical Sturmian word of slope \(\alpha\), and \(c_{[m]}=c_0\cdots c_{m-1}\), with \(c_{[0]}\) empty. For \(\alpha>1/2\) and every \(n\ge2\), the sole nonsingleton image fiber is the pair \(\{10c_{[n-2]},01c_{[n-2]}\}\). For \(1/3<\alpha<1/2\) and every \(n\ge4\), the two and only two nonsingleton image fibers are the disjoint pairs
\[
\{10c_{[n-2]},01c_{[n-2]}\},\qquad
\{001c_{[n-3]},010c_{[n-3]}\}.
\]
At \(n=3\) in the latter regime, \(\{001,010,100\}\) is one three-element image fiber and \(\{101\}\) is a singleton. At \(n=2\), \(\{01,10\}\) is the unique two-element fiber. These conclusions hold for every intercept, since Sturmian words of one irrational slope have the same factor language.

## Assumptions and scope

The alphabet is ordered \(0<1\), and the operator is the binary Defant–Kravitz *tortoise* map applied **once**. It moves the earliest \(1\) to the right end, preserving every other symbol's relative order. A factor is contiguous, although the operation changes its internal order. Only finite positive lengths are counted. All statements quantify over irrational slopes \(1/3<\alpha<1\), excluding the rational boundary slopes and slopes not exceeding \(1/3\).

Use the two-sided mechanical coding
\[
s_{\alpha,x}(j)=\lfloor x+(j+1)\alpha\rfloor-\lfloor x+j\alpha\rfloor,
\qquad j\in\mathbb Z,
\]
with \(x\) reduced modulo one. Irrational rotation is dense, so every finite block occurring for an intercept \(x\) also occurs in the right-infinite mechanical word at any other intercept. The characteristic word is \(c_j=s_{\alpha,\alpha}(j)\) for \(j\ge0\).

## Proof

**1. Sturmian left-special uniqueness and the characteristic predecessor contexts.** A Sturmian factor language has \(n+1\) factors of length \(n\), and is recurrent. Every length-\(m\) factor therefore has at least one left extension. There are \(m+2\) distinct length-\(m+1\) factors. Consequently exactly one length-\(m\) factor has both left extensions, since the number of extensions exceeds the number of factors by one. This applies also at \(m=0\).

Fix any \(m\ge0\). Because \(\alpha\) is irrational, the forward block \(s_{\alpha,x}(0)\cdots s_{\alpha,x}(m-1)\) is constant for all \(x\) sufficiently close to \(\alpha\), on either side: none of the floors has a discontinuity at \(x=\alpha\). The backward pair at positions \(-2,-1\) is \(01\) just to the left of \(\alpha\), and \(10\) just to the right. It follows from density of the positive rotation orbit that both \(01c_{[m]}\) and \(10c_{[m]}\) occur as factors. Thus \(c_{[m]}\) is exactly the unique left-special factor of length \(m\).

In the regime \(1/3<\alpha<1/2\), the symbols at positions \(-3,-2,-1\) are respectively \(001\) just to the left of \(\alpha\) and \(010\) just to the right. Indeed, for \(x\) close to \(\alpha\), the symbol at \(-3\) is
\[
\lfloor x-2\alpha\rfloor-\lfloor x-3\alpha\rfloor=0,
\]
whereas the last two symbols switch between \(01\) and \(10\). Therefore both \(001c_{[m]}\) and \(010c_{[m]}\) occur for every \(m\ge0\).

**2. Restrictions on initial symbols.** The number of ones in any mechanical length-\(\ell\) factor is one of \(\lfloor\ell\alpha\rfloor\) and \(\lceil\ell\alpha\rceil\), by telescoping the floor differences. Hence when \(\alpha>1/2\), \(00\) is absent, so any length-\(n\) factor with \(n\ge2\) has its first one in position zero or one. When \(1/3<\alpha<1/2\), both \(11\) and \(000\) are absent, so every factor of length at least three has its first one in position zero, one, or two.

**3. Exhaustive collision equations.** For a word containing a one, \(\tau(0^j1u)=0^ju1\), and this mapping is injective when the position \(j\) of the earliest one is fixed. Equating two images with distinct first-one positions gives, for \(j=0,1\), precisely the potential pair \(\{10v,01v\}\); for \(j=1,2\), the potential pair \(\{010v,001v\}\); and for \(j=0,2\), the potential pair \(\{100v,001v\}\). The two words in each pair have the same image by direct substitution.

For either of the first two pair types, the displayed suffix \(v\) has both a zero and a one left extension and is therefore left special. Part 1 makes it the unique characteristic prefix of the appropriate length, and proves that both members of each permitted pair really occur. In the high-slope regime only the first pair type is possible. Therefore there is exactly one double fiber for every \(n\ge2\), and \(\rho^\tau_\alpha(n)=(n+1)-1=n\).

In the lower-slope regime, both the first pair with \(v=c_{[n-2]}\) and the second pair with \(v=c_{[n-3]}\) exist whenever their lengths fit. If \(n\ge4\), the third pair type is impossible: its nonempty suffix \(v\) would have to begin in \(1\) to prevent the forbidden factor \(000\) in \(100v\), but would simultaneously have to begin in \(0\) to prevent the forbidden factor \(11\) in \(001v\). Thus no fiber can include both a first-one-position-zero word and a first-one-position-two word. In particular the two existing double fibers are disjoint and cannot merge into a triple, and no other nonsingleton fibers exist. Subtracting their two independent one-unit losses from the \(n+1\) Sturmian factors gives \(n-1\) images for every \(n\ge4\).

**4. Small lengths.** For \(1/3<\alpha<1/2\), the complete factor sets at lengths two and three are \(\{00,01,10\}\) and \(\{001,010,100,101\}\), respectively; the claimed fibers follow by direct application of \(\tau\). For \(\alpha>1/2\), length two has factors \(\{01,10,11\}\). At length one the two one-letter factors are fixed by \(\tau\), giving two images. This covers every stated boundary.

## Verification

Run `python3 verify_sturmian_tortoise.py` with Python 3. The supplementary checker enumerates the complete factor language through length \(81\) at eight representative algebraic-irrational slopes using rotation-partition cells, compares exact image fibers to the symbolic description, and independently generates all factors through length \(27\) by scanning long mechanical prefixes. Expected output:

`STURMIAN_TORTOISE_VERIFY_OK 8 648 rotation_cell_census prefix_independent_scan n_le_81`

The program evaluates its irrational slopes with high-precision decimal approximations. Its results are finite consistency tests, not the justification for the infinitely quantified theorem; the proof above is the source of the all-length conclusion.

## Relationship to prior work

Campbell and Rampersad, *Subword enumeration up to stack-sorting equivalence* (2026), introduce one-tortoise factor complexity, prove a bounded-deficit theorem for recurrent bounded-gap binary words of linear complexity, and determine it for paperfolding and Thue–Morse words. Their Section 4 connects collisions to left-special suffixes; their conclusion explicitly asks for Sturmian variants. The present result gives the exact deficit and every collision fiber for two natural Sturmian slope ranges, including the Fibonacci word.

De Luca and Fici, *On the Lie complexity of Sturmian words* (2022), study entirely different equivalence classes: cyclic conjugacy classes for which all rotations occur. Their result does not imply the tortoise-image spectrum. For instance, \(1001\) and \(0101\) are tortoise-equivalent Fibonacci factors but are not cyclic conjugates.

## Limitations

The classification excludes \(\alpha<1/3\) and the rational boundary values \(1/3,1/2\); longer initial zero runs below one-third permit additional collision types. It considers exactly one application of the binary tortoise operation, not repeated applications, nonbinary alphabets, or all binary infinite words. Searches and full-text comparisons cannot rule out an unindexed equivalent result. No independent mathematical audit has been performed.

## References

1. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811, first posted 28 April 2026; inspect Sections 2–4 and 7, https://arxiv.org/html/2604.25811v2 .
2. A. De Luca and G. Fici, *On the Lie complexity of Sturmian words*, *Theoretical Computer Science* 938 (2022), 81–85, arXiv:2206.00995, https://arxiv.org/html/2206.00995v2 .
3. C. Defant and N. Kravitz, *Stack-sorting for words*, *Australasian Journal of Combinatorics* 77 (2020), 51–68 (definition of the tortoise operation as cited in Reference 1).
