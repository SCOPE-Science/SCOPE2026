# The sharp product-multiple cutoff for primitive two-generator representations

## Finding
For coprime integers \(a,b\ge2\), call \(n\) primitively representable if \(n=ax+by\) for \(x,y\in\mathbb Z_{\ge0}\) with \(\gcd(x,y)=1\). Define the universal product-multiple cutoff to be the least integer \(k\ge2\) for which some coprime \(a,b\ge2\) make \(kab\) non-primitively-representable.

**The cutoff is exactly \(16\).** More precisely, for every coprime pair \(a,b\ge2\) and every integer \(2\le k\le15\), \(kab\) has a primitive representation. At \(k=16\), \(a=273=3\cdot7\cdot13\) and \(b=55=5\cdot11\) give \(16ab=240240\), which has none. For every positive integer \(m\) coprime to \(273\), the pair \((273,55m)\) is a further counterexample at \(k=16\).

## Assumptions and scope
The generators \(a,b\) are positive integers at least \(2\) with \(\gcd(a,b)=1\); both coefficients are required to be nonnegative integers, with coefficient gcd equal to \(1\). The result concerns targets that are positive integral multiples of the generator product, not arbitrary targets or the maximum missing target. No condition that the generators be prime is imposed. The exceptional example is explicit and the universal assertion holds for *all* coprime generators, not merely bounded ranges.

## Proof
**Parametrization and criterion.** Suppose \(ax+by=kab\). Reducing modulo \(b\) and \(a\), respectively, and using \(\gcd(a,b)=1\), one gets \(b\mid x\) and \(a\mid y\). Thus every nonnegative coefficient solution is uniquely
\[
(x,y)=(b(k-t),at),\qquad t\in\{0,1,\ldots,k\}.
\]
A common prime divisor of \(b(k-t)\) and \(at\) must divide one of \((a,b)\), \((a,k-t)\), \((b,t)\), or \((k-t,t)\); the first is ruled out. Consequently, the solution indexed by \(t\) is primitive if and only if
\[
\gcd(k,t)=\gcd(a,k-t)=\gcd(b,t)=1.\tag{1}
\]
The endpoint indices \(t=0,k\) never qualify because \(a,b\ge2\).

**Universal range.** If \(k=2\), taking \(t=1\) gives \((x,y)=(b,a)\), which is primitive. For \(k\ge3\), the candidate \(t=1\) is primitive when \(\gcd(a,k-1)=1\), and \(t=k-1\) is primitive when \(\gcd(b,k-1)=1\). In particular, if \(k-1\) is a prime power then at least one endpoint candidate works, because \(a\) and \(b\) are coprime. All integers \(2\le k\le15\) are thereby covered except \(k\in\{7,11,13,15\}\).

For any exceptional \(k\), failure of both endpoint candidates forces two different prime divisors of \(k-1\) to lie on opposite sides of the coprime pair. Interchanging \(a,b\) and replacing \(t\) by \(k-t\) if necessary, only the following situations remain:

* \(k=7\), \(2\mid a\) and \(3\mid b\): take \(t=4\), for which \(k-t=3\) and \(t=4\).
* \(k=11\), \(2\mid a\) and \(5\mid b\): if \(3\nmid b\), take \(t=6\) (so \(k-t=5\)); if \(3\mid b\), take \(t=8\) (so \(k-t=3\), and \(3\nmid a\)).
* \(k=13\), \(2\mid a\) and \(3\mid b\): take \(t=4\), so \(k-t=9\).
* \(k=15\), \(2\mid a\) and \(7\mid b\): take \(t=8\), so \(k-t=7\).

Every listed candidate meets all three gcd conditions in (1). This exhausts \(2\le k\le15\), with no computation needed for the universal statement.

**Sharpness.** Choose \(a=273\) and \(b=55\). The only indices coprime to \(16\) in \([1,15]\) are \(1,3,5,7,9,11,13,15\). For \(t=1,3,7,9,13\), respectively, \(16-t=15,13,9,7,3\) has a factor in \(\{3,7,13\}\), so \(\gcd(a,16-t)>1\). For \(t=5,11,15\), \(\gcd(b,t)>1\). Thus (1) fails for every \(t\); even indices fail \(\gcd(16,t)=1\), and the endpoints are nonprimitive. Therefore \(240240\) has no primitive representation. Replacing \(b\) with \(55m\) and requiring \(\gcd(m,273)=1\) preserves coprimality of the generators and every previous nonprimitivity obstruction. This gives infinitely many exceptional generator pairs.

## Verification
The standalone standard-library program `verify.py` checks the criterion against direct coefficient gcds; it enumerates all coprime \(2\le a,b\le120\) and \(2\le k\le15\), giving \(119448\) cases; it independently enumerates all \(17\) nonnegative coefficient solutions at \((a,b,k)=(273,55,16)\) and verifies that none is primitive. It additionally checks a finite sample of the infinite counterexample family. Running `python verify.py` prints `VERIFY_OK`. The universal assertion and infinite family are proved above independently of these finite tests.

## Relationship to prior work
Grace Natalie Jaffe, *Denominators in the Farey Sequence, the Stern Sequence, and the Frobenius Problem with Relatively Prime Multipliers* (arXiv:2610.17267v1, first public 2026-10-12), identifies primitive coefficient representations with a Farey/Stern problem, proves that their global Frobenius threshold exists (Theorem 4.3), and establishes particular values and upper bounds (Sections 5–7). The present statement isolates a different question: *which multiples of the product of the two generators are primitively representable for every coprime generator pair?* The exact first breakdown at \(16\) is not implied by the cited finiteness, upper bounds, special-generator formulas, or global-growth bounds; the latter measure the largest absent target rather than membership at the specific targets \(kab\).

## Limitations
No assertion is made about which multipliers \(k>16\) are universal, how often nonprimitive product multiples occur, or the exact global primitive Frobenius threshold of the exceptional pair. A missing result from searches cannot rule out unpublished or unindexed equivalent treatments of this elementary classification. The counterexample family is infinite but does not claim any density. Finite numerical enumeration supplies corroboration, not the proof for all generators.

## References
1. G. N. Jaffe, *Denominators in the Farey Sequence, the Stern Sequence, and the Frobenius Problem with Relatively Prime Multipliers*, arXiv:2610.17267v1 (2026), https://arxiv.org/abs/2610.17267 (especially Sections 2–7).
2. Classical linear Diophantine parametrization and coprimality properties, derivable directly from Bézout's identity; see https://www.southampton.ac.uk/~wright/1001/coprime-integers.html .
