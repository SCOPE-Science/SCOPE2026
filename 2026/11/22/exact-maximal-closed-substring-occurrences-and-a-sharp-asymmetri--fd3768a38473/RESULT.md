# Exact maximal-closed-substring occurrences and a sharp asymmetric extremum in five-run binary words

## Finding

For arbitrary positive integers \(a,b,c,d,e\), let
\[
W=0^a1^b0^c1^d0^e,\qquad n=a+b+c+d+e.
\]
Let \(K(W)\) count **occurrences** of maximal closed substrings (MCSs), not merely distinct factor values. With \([E]\) equal to one when \(E\) is true and zero otherwise, the exact five-parameter law is
\[
\boxed{K(W)=5+\min(a,c)+\min(c,e)+\min(b,d)-[c\le a]-[c\le e]+[b\ne d]+\max(0,\min(a,e)-c).}
\]
There is an explicit, complete set of endpoint intervals below. In particular, the sharp maximum among all binary words of length \(n\) with **exactly five nonempty runs** is
\[
\boxed{\max K(W)=\begin{cases}
6,&n=5,\\
4+\left\lfloor(2n+1)/3\right\rfloor,&n\ge6,
\end{cases}}
\]
and the minimum is exactly \(6\) for every \(n\ge5\). The asymmetric extremum exceeds the symmetric-subfamily maximum by one exactly when \(n\equiv1\pmod3\), for \(n\ge7\), and equals it at other lengths.

## Assumptions and scope

The binary alphabet is ordered only for notation. All five run lengths are **positive**, and the word is linear, not circular. A word of length one is closed; a longer word is closed precisely when some nonempty proper border occurs **exactly twice** in the word, as its prefix and suffix, allowing overlapping occurrences. An MCS is a closed occurrence for which neither available one-symbol extension, to its left or right, is closed. The complement of the displayed word covers five-run words beginning with one.

For endpoint classification use zero-based, half-open intervals \([i,j)\) and put \(N=a+b+c+d+e\). Every MCS is exactly one of the following pairwise disjoint families:

1. **Whole runs:** \([0,a)\), \([a,a+b)\), \([a+b,a+b+c)\), \([a+b+c,a+b+c+d)\), \([a+b+c+d,N)\).
2. **First three-run center:** \([a-t,a+b+t)\) for \(1\le t\le\min(a,c)\), omitting \(t=c\).
3. **Middle three-run center:** \([a+b-u,a+b+c+u)\) for \(1\le u<\min(b,d)\).
4. **Last three-run center:** \([a+b+c-t,a+b+c+d+t)\) for \(1\le t\le\min(c,e)\), omitting \(t=c\).
5. **Four-run bridges when \(b\ne d\):** precisely \([a-\min(a,c),a+b+c+\min(b,d))\) and \([a+b-\min(b,d),a+b+c+d+\min(c,e))\). When \(b=d\), neither is maximal.
6. **Five-run long-unary-border family:** \([a-t,a+b+c+d+t)\), for every integer \(c<t\le\min(a,e)\).
7. **Five-run nonunary-border singleton, when \(b=d\):** \([a-\min(a,c),a+b+c+d+\min(c,e))\). When \(b\ne d\), this family is empty.

Empty parameter ranges contribute no occurrences. The listed intervals are distinct because of their transition counts and non-overlapping run parameters.

## Proof

**Closed factors by transition count.** A constant word is closed, and every maximal constant occurrence is precisely a whole run. A two-run factor has no border, hence is open. A three-run factor is closed precisely when its outer run lengths agree: any border is unary, and unequal outer lengths create an additional overlapping occurrence of their shortest common unary border. A four-run factor beginning in a zero run has the shape \(0^x1^b0^c1^y\); it is closed precisely when \(x\le c\) and \(y\le b\), with its unique longest border \(0^x1^y\) occurring at the two \(01\) transitions. Symmetrically, the last-four-run factor \(1^u0^c1^d0^v\) is closed precisely for \(u\le d\), \(v\le c\).

Every factor spanning all five runs has the form \(0^x1^b0^c1^d0^y\), with \(1\le x\le a\), \(1\le y\le e\). If its unique witnessing longest border is unary, it must be \(0^t\). Having exactly two occurrences of that border is equivalent to \(x=y=t>c\): unequal outer lengths yield multiple overlapping copies inside the longer run, while \(t\le c\) supplies an additional middle-run copy. If the border is not unary, it has to cross a \(01\) transition in each of its two occurrences; there are exactly two such transitions in the factor. This forces \(b=d\), \(x\le c\), and \(y\le c\); conversely \(0^x1^b0^y\) then witnesses closedness exactly twice. These two five-run classes are disjoint. No further border is possible because all the available run transitions have been accounted for.

**Maximality.** In the first three-run family \(0^t1^b0^t\), unequal outer zeros prevent a one-sided zero extension from remaining closed. At \(t=c\) there is instead an available right extension by one from the next one-run, and its border \(0^c1\) makes it closed; this removes exactly that endpoint. The last three-run family analogously loses \(t=c\) to a left extension. In the central family \(1^u0^c1^u\), all parameters \(u<\min(b,d)\) are maximal. The endpoint \(u=\min(b,d)\) is not: it can extend through a neighboring zero on at least one side and stay closed.

The first four-run closed factor can be extended while closed by increasing its initial zero tail (when \(x<c\) and one zero remains on the left), or its final one tail (when \(y<b\) and one one remains on the right). Its only maximally extended candidate therefore uses \(x=\min(a,c)\), \(y=\min(b,d)\). If \(b=d\), one zero immediately to its right extends that candidate into a closed five-run factor with a nonunary border, so it is not an MCS; if \(b\ne d\), this extension is open. The mirror analysis gives the second four-run bridge and the same \(b=d\) suppression.

Every five-run unary-border factor with \(x=y=t>c\) is maximal: extending one outer zero-run breaks equality and creates a third occurrence of any common unary border, while a nonunary border is impossible at those parameters. In the nonunary five-run family, increasing either outer tail while maintaining closedness is possible precisely until that tail reaches \(\min(a,c)\) or \(\min(c,e)\), respectively; hence exactly the indicated endpoint is maximal. In all these arguments unavailable boundary extensions are automatically harmless. This proves the complete list.

**Counting.** The whole runs contribute \(5\); three-run centers contribute \(\min(a,c)-[c\le a]\), \(\min(b,d)-1\), and \(\min(c,e)-[c\le e]\). The two four-run bridges contribute \(2[b\ne d]\); the five-run families contribute \(\max(0,\min(a,e)-c)+[b=d]\). Since \(2[b\ne d]+[b=d]-1=[b\ne d]\), summation gives the displayed exact law.

**Sharp fixed-length bounds.** Put \(s=a+c+e\), \(t=b+d\), and \(x=\min(a,e)\), \(y=\max(a,e)\). The zero-run contribution is
\[
H=x+\min(c,y)-[c\le x]-[c\le y]
=\begin{cases}x+c-2,&c\le x,\\x+c-1,&x<c\le y,\\x+y,&c>y.\end{cases}
\]
For every \(s\ge3\), these cases give \(3H\le2s-2\): when \(c\le x\), use \(s\ge2x+c\) and \(c\le x\); when \(x<c\le y\), use \(s\ge x+2c\); when \(c>y\), use \(2c\ge x+y+2\). Hence \(H\le\lfloor(2s-2)/3\rfloor\). This is sharp for every \(s\ge4\): take \((x,y,c)=(k,k,k+1)\), \((k,k,k+2)\), or \((k-1,k,k+1)\) as \(s=3k+1\), \(3k+2\), or \(3k\), respectively. The final family is valid for \(k\ge2\). At \(s=3\), only \((a,c,e)=(1,1,1)\) occurs and \(H=0\).

For \(t\ge2\), write \(V=\min(b,d)+[b\ne d]\). Then \(V\le\lfloor(t+1)/2\rfloor\), with equality for appropriate near-balanced lengths. If \(t\ge3\),
\[
3(H+V)\le(2s-2)+\frac{3(t+1)}2\le2(s+t)-2,
\]
and for \(t=2\) we have \(V=1\), giving the same final inequality. Thus \(K=5+H+V\le4+\lfloor(2n+1)/3\rfloor\). Equality holds for \(n\ge7\) by taking \((b,d)=(1,2)\) and choosing \((a,c,e)\) with \(s=n-3\) to attain the sharp zero-run bound. For \(n=6\), \((a,b,c,d,e)=(1,1,2,1,1)\) attains eight. For \(n=5\), the unique run-length tuple has six MCSs. Finally \(H\ge0\) from its three cases and \(V\ge1\), so \(K\ge6\), attained for every \(n\ge5\) by \((a,b,c,d,e)=(n-4,1,1,1,1)\).

For comparison, specializing the exact five-parameter law to the symmetric restriction \(a=e,b=d\) and optimizing gives maximal count \(\lfloor2n/3\rfloor+4\) for \(n\ge6\). Our unrestricted maximum is larger by one when \(n\equiv1\pmod3\). A concrete witness at \(n=3k+1\ge7\) is \((a,b,c,d,e)=(k-1,1,k,2,k-1)\), with \(2k+5\) MCS occurrences.

## Verification

The self-contained `verify.py` constructs each five-run word, independently enumerates every contiguous interval, tests its closedness using overlapping border occurrences, checks both one-character extensions, and compares the exact endpoint set with the seven symbolic families. It checks all \(6^5=7776\) positive five-tuples with coordinates at most six, then 2000 deterministic seeded larger tuples with coordinates up to seventeen. It also checks the exact min/max laws by complete positive-composition enumeration for all lengths \(5\) through \(42\). Execute `python3 verify.py` using Python 3 and standard-library modules only; `verification_output.txt` records the run. Finite tests do not replace the all-parameter proof.

## Relationship to prior work

Fischer and Köppl [1] give output-sensitive MCS algorithms, motivating a symbolic output-count law. Umezaki, Shibata, Nakashima, and Inenaga [2] characterize valid longest-border pairs and give compact enumeration from arbitrary run-length encodings, but do not derive the present five-parameter endpoint classification or the sharp extremum over all five-run compositions. The established four-run exact MCS formula [3] does not classify factors spanning five runs. The distinct-closed-factor census for five-run words [4] counts **different strings**, not maximal **occurrences**; its proof supplies a useful transition-based comparison but does not establish the one-sided maximality filtering or the extremum. The symmetric five-run restriction is recovered by setting \(a=e\) and \(b=d\); it excludes asymmetric residue-one witnesses attaining one additional MCS at fixed length.

## Limitations

The classification concerns linear, positive-length, alternating **binary five-run words**, not arbitrary run counts, circular words, or factor-value counts. The exact extremum is within this restricted family; it is not an unrestricted extremal MCS theorem. The six-run and general-alphabet analogues are not proved. General RLE algorithms can enumerate each individual instance, and unpublished or unindexed symbolic five-run specializations may exist. The work has not received independent mathematical validation.

## References

[1] J. Fischer and D. Köppl, *Output-Sensitive Enumeration of Maximal Closed Substrings in Linear Space*, first public October 28, 2026, arXiv:2610.38114v1. https://arxiv.org/html/2610.38114v1

[2] H. Umezaki, H. Shibata, Y. Nakashima, and S. Inenaga, *Compact Enumeration of Maximal Closed Substrings in Run-Length Encoded Strings*, first public July 3, 2026, arXiv:2607.02838v1. https://arxiv.org/abs/2607.02838

[3] *Exact maximal-closed-substring spectrum for binary four-run words*, publicly available November 8, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-maximal-closed-substring-spectrum-for-binary-four-run-word--5387a5bb0a25

[4] *Closed-factor spectrum and sharp density for five-run binary words*, publicly available October 25, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-closed-factor-spectrum-and-sharp-density-for-five-run-binary-wor--26670ba71617

