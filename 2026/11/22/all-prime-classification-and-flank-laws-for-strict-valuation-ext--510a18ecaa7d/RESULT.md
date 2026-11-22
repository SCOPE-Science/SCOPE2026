# All-prime classification and flank laws for strict valuation extrema of ternary Fuss–Catalan numbers

## Finding
For every nonnegative integer \(n\), define the ternary Fuss–Catalan number
\[
F_n=\frac{1}{2n+1}\binom{3n}{n},\qquad V_p(n)=\nu_p(F_n),
\]
where \(p\) is any rational prime. For every integer \(n\ge1\), call \(n\) a **strict peak** when \(V_p(n)>V_p(n-1)\) and \(V_p(n)>V_p(n+1)\), and a **strict valley** when both inequalities reverse.

All the strict peaks are given by this exhaustive classification:

| Prime | Peak indices | Left drop \(L=V_p(n)-V_p(n-1)\) | Right drop \(R=V_p(n)-V_p(n+1)\) |
|---|---|---|---|
| \(2\) | \(n\equiv3\pmod4\) | \(\nu_2(3n-1)-1\) | \(\nu_2(n+1)\) |
| \(3\) | \(n\equiv8\pmod9\) | \(1\) | \(\nu_3(n+1)-1\) |
| \(5\) | \(n\equiv4\pmod5\) | \(\nu_5(3n-2)\) | \(\nu_5(n+1)\) |
| \(11\) | \(n\equiv4\pmod{11}\) | \(\nu_{11}(3n-1)\) | \(\nu_{11}(2n+3)\) |
| \(13\) | \(n\equiv5\pmod{13}\) | \(\nu_{13}(3n-2)\) | \(\nu_{13}(2n+3)\) |

**No other prime has a strict peak.** The only strict valleys, for any prime, are \(p=3\), \(n\equiv4\pmod9\). At each valley the preceding-minus-current valuation is \(\nu_3(2n+1)-1\), and the following-minus-current valuation equals \(1\). All these drops and rises are positive.

The strict-peak density at a prime \(p\) is therefore \(1/4,1/9,1/5,1/11,1/13\), respectively, for the five displayed primes, and zero for the others; the strict-valley density is \(1/9\) at \(3\), zero otherwise.

The complete limiting **joint flank distribution**, conditional on the peak indices, is as follows. For each \(p\in\{5,11,13\}\),
\[
\Pr(L=1,R=1)=\frac{p-2}{p},\qquad
\Pr(L=j,R=1)=\Pr(L=1,R=j)=\frac{p-1}{p^j}\quad(j\ge2).
\]
There are no other positive drop pairs. At \(p=3\), \(L=1\) always and \(\Pr(R=j)=2/3^j\) for \(j\ge1\). At the \(p=3\) valleys the right rise is one, and the left rise has this same law. At \(p=2\), precisely the pairs
\[
(L,R)=(j,2)\quad(j\ge2),\qquad (L,R)=(1,j)\quad(j\ge3)
\]
occur, with respective conditional probabilities \(2^{-j}\) and \(2^{-(j-1)}\). Each distribution sums to one. In particular, at primes \(5,11,13\) the smaller flank drop is **always exactly one**, although either larger flank can have arbitrarily high valuation.

## Assumptions and scope
All primes are positive rational primes, not restricted by any upper bound; all indices are integers \(n\ge1\). The valuation is the standard nonnegative exponent in the positive integer \(F_n\). A local extremum is *strict* with respect to both immediate index neighbors. Probabilities are **conditional natural densities** within the indicated infinite arithmetic progression of indices, equivalently the limit of the proportion among such indices below \(X\) as \(X\to\infty\). The claim is not about real magnitude of \(F_n\), nor about weak extrema or all prime-power residue values.

## Proof
**1. An exact difference identity.** Direct cancellation of factorials gives for every \(n\ge0\)
\[
\frac{F_{n+1}}{F_n}=\frac{3(3n+1)(3n+2)}{2(n+1)(2n+3)}.
\]
Set \(J_p(n)=V_p(n+1)-V_p(n)\). Applying \(\nu_p\) to this rational identity yields, with all numerator and denominator terms positive,
\[
J_p(n)=\nu_p(3)+\nu_p(3n+1)+\nu_p(3n+2)-\nu_p(2)-\nu_p(n+1)-\nu_p(2n+3).\tag{1}
\]
A strict peak at \(n\ge1\) is equivalent to \(J_p(n-1)>0>J_p(n)\), and a strict valley to \(J_p(n-1)<0<J_p(n)\).

**2. All primes at least five.** Here the factors \(2\) and \(3\) are units. If \(J_p(n-1)>0\), at least one of \(3n-2,3n-1\) is divisible by \(p\). If \(J_p(n)<0\), at least one of \(n+1,2n+3\) is divisible by \(p\). For both properties simultaneously, the four pairwise integer linear combinations are, up to sign, \(5\), \(13\), \(4\), and \(11\):
\[
(3n-2)-3(n+1)=-5,\quad
2(3n-2)-3(2n+3)=-13,
\]
\[
(3n-1)-3(n+1)=-4,\quad
2(3n-1)-3(2n+3)=-11.
\]
Thus \(p\in\{5,11,13\}\). At \(p=5\), the relevant simultaneous zero is \((3n-2,n+1)\) when \(n\equiv4\pmod5\); at \(p=11\), it is \((3n-1,2n+3)\) when \(n\equiv4\pmod{11}\); at \(p=13\), it is \((3n-2,2n+3)\) when \(n\equiv5\pmod{13}\). Substituting these classes in (1) and verifying all other numerator/denominator factors are units gives the displayed *exact* positive left/right drops, proving necessity and sufficiency at every prime at least five.

For a valley at a prime at least five, \(J_p(n-1)<0\) forces \(p\mid n(2n+1)\), while \(J_p(n)>0\) forces \(p\mid(3n+1)(3n+2)\). No such pair of linear factors can vanish together: evaluating the second product at \(n=0\) gives \(2\), and the combinations \(3(2n+1)-2(3n+1)=1\) and \(3(2n+1)-2(3n+2)=-1\) preclude common roots. Hence there are no such valleys.

**3. The exceptional prime three.** Equation (1) specializes to
\[
J_3(n)=1-\nu_3(n+1)-\nu_3(2n+3).
\]
It equals \(+1\) exactly for \(n\equiv1\pmod3\); it is negative exactly for \(n\equiv3,8\pmod9\); it is zero at all other indices. Hence \(J_3(n-1)>0>J_3(n)\) precisely for \(n\equiv8\pmod9\), whereas \(J_3(n-1)<0<J_3(n)\) precisely for \(n\equiv4\pmod9\). The explicit drops and rises follow by substituting these classes in the displayed formula for \(J_3\).

**4. The exceptional prime two.** Equation (1) specializes to
\[
J_2(n)=\nu_2(3n+1)+\nu_2(3n+2)-1-\nu_2(n+1).
\]
For \(n\equiv0,1,2,3\pmod4\), respectively, the jump is \(0\), \(\nu_2(3n+1)-2\ge0\), \(\nu_2(3n+2)-1\ge1\), and \(-\nu_2(n+1)<0\). Therefore it is negative precisely for \(n\equiv3\pmod4\), and its immediately previous jump is positive there. There are no negative-to-positive transitions, so no strict valleys. Substitution in the jump formula yields the claimed drops.

**5. Exact joint densities.** For \(p=5,11,13\), write the peak progression as \(n=c+pt\) with \(t\ge0\). The two drops equal \(1+\nu_p(a+bt)\) and \(1+\nu_p(d+et)\), with \(b,e\) units modulo \(p\) and with *different* roots modulo \(p\). In each complete set of \(p^k\) consecutive \(t\)'s, both valuations equal zero at \(p-2\) residue classes modulo \(p\); if one is positive, the other is zero. A fixed affine unit-root linear factor has valuation exactly \(j-1\) on proportion \((p-1)/p^j\), for \(j\ge2\). This proves the exhaustive joint distribution. For \(p=3\), writing a peak as \(n=8+9t\) gives \(R=1+\nu_3(t+1)\), and writing a valley as \(n=4+9t\) gives left rise \(1+\nu_3(1+2t)\), each with the stated geometric law.

For \(p=2\), write \(n=3+4t\). Then \(L=1+\nu_2(2+3t)\), \(R=2+\nu_2(t+1)\). If \(t\) is even, \(R=2\) and \(L\ge2\); if \(t\) is odd, \(L=1\) and \(R\ge3\). Unit-slope linear congruences give \(\Pr(L=j,R=2)=2^{-j}\) for \(j\ge2\), and \(\Pr(L=1,R=j)=2^{-(j-1)}\) for \(j\ge3\). Each density is obtained from exact counts modulo a prime power, so the limits exist. This completes all cases.

## Verification
Run `python3 verify.py` using Python 3 standard library. It independently computes the valuations through Legendre's factorial formula, checks the rational jump identity at more than a third of a million prime-index pairs, verifies peak/valley classification and drop formulas for eighteen primes and indices below twenty thousand, and directly checks integer Fuss–Catalan values for small indices. The recorded execution returned `PASS: 2160972 exact assertions over 18 primes, n < 20000`. These are finite checks only; the all-prime and unbounded-index claims are established by the proof above.

## Relationship to prior work
Lin's 2011 paper gives combinatorial interpretations of Fuss–Catalan numbers. Konvalinka's work on generalized Catalan divisibility establishes a digit-sum valuation formula when the arity is a power of the same prime (in particular, arity three at prime three), but does not evaluate local strict-peak/valley classes or joint flank distributions across all primes. Published dyadic and ternary Fuss–Catalan valuation-spectrum results provide *one-point block histograms*, block maxima and Gaussian laws; such histograms do not specify the adjacency ordering needed to determine local extrema. The present result evaluates the complete prime support, exact index congruence classes, and conditional paired-flank laws, not merely the factorial quotient itself or its single-index valuation.

## Limitations
This result does not address weak extrema, non-consecutive index gaps, different arities, or magnitude extrema. Its mathematical novelty is the evaluated all-prime local-extrema classification and associated joint-drop densities; the ratio identity and standard valuation facts are not new. Historical-priority searches cannot rule out an equivalent result in unindexed literature or in an inaccessible related thesis; independent mathematical audit has not been performed. No numerical computation is offered as evidence for the infinite quantifiers.

## References
- C.-H. Lin, *Some Combinatorial Interpretations and Applications of Fuss–Catalan Numbers*, International Scholarly Research Notices (first published 2011-11-14), DOI: https://doi.org/10.5402/2011/534628 .
- M. Konvalinka, *Divisibility of generalized Catalan numbers*, Journal of Combinatorial Theory, Series A 114 (2007), 1089–1100, lawful author manuscript: https://users.fmf.uni-lj.si/konvalinka/wcatalan.pdf .
- *Exact dyadic two-adic valuation census of ternary Fuss–Catalan numbers*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-dyadic-two-adic-valuation-census-of-ternary-fuss-catalan-n--7f423ce9ed57/RESULT.md .
- *Exact ternary valuation spectra of ternary Fuss–Catalan numbers*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-ternary-valuation-spectra-of-ternary-fuss-catalan-numbers--38f9bdc99cfd/RESULT.md .
- *Exact dyadic two-adic valuation spectra of ternary Fuss-Catalan numbers*, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-exact-dyadic-two-adic-valuation-spectra-of-ternary-fuss-catalan--02997d82d076/RESULT.md .
