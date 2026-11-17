# Exact closed-factor census and sharp quadratic density for five-run binary words

## Finding

A finite word is **closed** if it has length at most one, or if some proper nonempty factor occurs in it exactly twice, as its prefix and suffix. Let \(C(w)\) be the number of **distinct** closed contiguous factors of \(w\), counting the empty factor once.

**Theorem.** For all positive integers \(a,b,c,d,e\), let
\[
 w=0^a1^b0^c1^d0^e,\qquad n=a+b+c+d+e,
\]
and set \(x=\min(a,c)\), \(y=\min(c,e)\), and \(z=\min(b,d)\). Then
\[
 \boxed{C(w)=n+1+z(x+y)+\mathbf1_{b=d}\bigl(xy-\min(x,y)\bigr).}
\]
In particular, if \(M_5(n)\) denotes the maximum of \(C(w)\) among **exactly five-run** binary words of length \(n\), then
\[
 \boxed{\lim_{n\to\infty}\frac{M_5(n)}{n^2}=\frac18.}
\]
The convergence concerns all integers \(n\ge5\), not just a subsequence. Both statements remain valid after exchanging the symbols \(0\) and \(1\).

## Assumptions and scope

The alphabet has exactly two letters. A run is a maximal constant-symbol block, and all five exponents are positive; this rules out collapsing runs. Factors are contiguous, including repeated occurrences but counted only once as distinct words. The empty factor is included; changing that convention subtracts one. There is no quotient by reversal, complement, or cyclic rotation. The theorem is for **linear** words and the closed-factor definition above. It makes no claim about the global exact maximum over all binary words with an unrestricted number of runs.

## Proof

Write \(p=\max(a,c,e)\), \(q=\max(b,d)\), \(h=\min(x,y)=\min(a,c,e)\), and \(I=\mathbf1_{b=d}\). We classify distinct closed factors by the number of constant-symbol runs in the **factor**; every factor has at most five.

**One run.** The empty factor and constant factors contribute exactly \(1+p+q\). A two-run factor starts and ends with different letters, so it has no nonempty border and is not closed.

**Three runs.** A factor \(0^i1^j0^k\) or \(1^i0^j1^k\) is closed precisely when \(i=k\). Indeed, any nonempty border is a pure constant block; if one endpoint run is longer, its shortest common endpoint run occurs internally as well. Conversely, equal endpoint runs give exactly two occurrences of that border. Thus the first three runs supply \(x\) distinct \(0^i1^b0^i\); the last three supply \(y\) distinct \(0^i1^d0^i\); the middle three supply \(z\) distinct \(1^i0^c1^i\). The first two collections overlap exactly when \(b=d\), in which case they share \(h\) elements. The three-run contribution is
\[
 x+y+z-Ih.
\]

**Four runs.** In the first four runs, a four-run factor necessarily has the form \(0^i1^b0^c1^j\) with \(1\le i\le a\) and \(1\le j\le d\). Any nonempty border starts in \(0\) and ends in \(1\), hence it must be exactly \(0^i1^j\) and exist if and only if \(i\le c\) and \(j\le b\). There are then precisely two occurrences, one at each \(01\) boundary. This gives \(xz\) closed factors. Symmetrically the last four runs provide \(yz\) closed factors beginning in \(1\); these families are disjoint. The four-run contribution is \(z(x+y)\).

**Five runs.** Every five-run factor is \(v=0^i1^b0^c1^d0^j\), where \(1\le i\le a\) and \(1\le j\le e\). If \(b=d\), every choice \(i\le c\) and \(j\le c\) gives a border \(0^i1^b0^j\) occurring at precisely the two different \(01\) boundaries; there are \(xy\) such choices. If this mixed-symbol border cannot occur, a closed factor can only have a pure-zero border. It occurs only at the two endpoints exactly when \(i=j>c\), accounting for \(\max(0,\min(a,e)-c)\) further choices. These two families are disjoint, so the five-run contribution is
\[
 Ixy+\max\bigl(0,\min(a,e)-c\bigr).
\]
No additional types of border are possible: a mixed-symbol border must traverse the two central blocks of ones, which forces \(b=d\), while a pure-zero border is controlled by the three zero runs.

Adding the contributions yields
\[
 C(w)=1+p+q+x+y+z-Ih+z(x+y)+Ixy+\max(0,\min(a,e)-c).
\]
The elementary identities
\[
 p+x+y+\max(0,\min(a,e)-c)=a+c+e,
 \qquad q+z=b+d
\]
reduce this expression to the claimed exact formula.

For the sharp density, put \(m=x+y\). Since \(c\ge\max(x,y)\), \(a\ge x\), and \(e\ge y\), while \(b+d\ge2z\),
\[
 n\ge x+y+\max(x,y)+2z\ge\frac32m+2z.
\]
The correction \(I(xy-h)\) is at most \(xy\le m^2/4\). Consequently
\[
 C(w)-(n+1)\le zm+xy
 \le \frac m2\left(n-\frac32m\right)+\frac{m^2}{4}
 =\frac{mn-m^2}{2}\le\frac{n^2}{8}.
\]
For every positive integer \(k\), take
\[
 w_k=0^{2k}1^k0^{2k}1^k0^{2k},\qquad |w_k|=8k.
\]
The exact formula gives \(C(w_k)=8k^2+6k+1\). For an arbitrary \(n\ge8\), choose \(k=\lfloor n/8\rfloor\) and append \(n-8k\) zeros to the last run. This preserves the five-run property and all old closed factors, so \(M_5(n)\ge8k^2+6k+1\). Together with \(M_5(n)\le n^2/8+n+1\), this proves the full limit \(1/8\).

## Verification

The bundled standard-library script `verify.py` independently enumerates all distinct factors and checks closedness by counting border occurrences, rather than by relying on the classified run families. It verifies the formula for all \(5^5=3125\) run-length vectors with each entry between 1 and 5, plus 160 seeded larger cases. It also checks the exhibited asymptotic family at 24 sizes and enumerates the exact maximum among five-run words for each length from 5 through 17. Execute `python3 verify.py` in the directory holding the bundled file. Expected output starts `VERIFY_OK`.

These tests are finite consistency checks only. The unlimited parameter ranges and sharp asymptotic follow from the proof, not from computational extrapolation.

## Relationship to prior work

Badkobeh, Fici and Lipták established that bitonic binary words (at most three runs) have the minimum possible number \(n+1\) of distinct closed factors, and gave a four-run family witnessing quadratic growth. Their treatment does not state the present exact formula for all five-run exponents. Parshina and Puzynina subsequently proved a global asymptotic maximum of \(n^2/6\) for unrestricted words and cited the five-run family \(0^k10^k10^k\) as a quadratic-growth example. Their unrestricted estimate does not determine the sharp five-run constant \(1/8\), nor the exact correction arising when the two inner run lengths agree. Thus the current result concerns a natural fixed-run boundary, rather than a new unrestricted bound.

## Limitations

The result applies to exactly five alternating binary runs, with every run nonempty. The sharp constant \(1/8\) is asymptotic; no exact all-length expression for the maximizer \(M_5(n)\) is claimed. Nothing is asserted about six or more runs, multiletter alphabets, or cyclic factors. Historical priority is assessed against the inspected sources and search results; lack of a discovered equivalent is not a mathematical proof of novelty.

## References

1. G. Badkobeh, G. Fici, Z. Lipták, *On the Number of Closed Factors in a Word*, arXiv:1305.6395 (first public posting 2013-05-28), especially Sections 4 and 5 and Theorem 25. https://arxiv.org/abs/1305.6395
2. O. Parshina, S. Puzynina, *Finite and infinite closed-rich words*, arXiv:2111.00863 (first public posting 2021-11-01), especially Section 2, Example 1 and Section 4. https://arxiv.org/abs/2111.00863
