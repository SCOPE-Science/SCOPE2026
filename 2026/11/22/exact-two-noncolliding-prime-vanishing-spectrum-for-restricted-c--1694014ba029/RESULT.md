# Exact two-noncolliding-prime vanishing spectrum for restricted coprime representations

## Finding
For an integer \(n\ge13\) and a squarefree product \(P\) of primes at least \(5\) (including \(P=1\)), put
\[
 g_P(2n)=\#\{h\in\mathbb Z:1\le h\le n,\ \gcd(h(2n-h),6P)=1\},
 \qquad k(n,P)=\omega(P/\gcd(P,n)).
\]
The complete vanishing spectrum with at most two *noncolliding* prime factors is
\[
 \boxed{\{2n\ge26:\ \exists P\text{ squarefree},\ k(n,P)\le2,\ g_P(2n)=0\}
       =\{26,28,34,40,46\}.}
\]
In the notation \(J(k)\) for the maximum of this vanishing set at noncolliding-support budget \(k\) (zero if the set is empty), this determines \(J(0)=J(1)=0\) and \(J(2)=46\). Each of the five zeros requires exactly two noncolliding factors. Explicit vanishing supports for the five displayed even integers, in increasing order, are
\[
 (P_{26},P_{28},P_{34},P_{40},P_{46})=(455,385,935,935,1955).
\]
The classification is unconditional given the published all-zero restrictions in Theorem 4.9 of Salazar (2026); the finite remainder is certified by an exhaustive exact-arithmetic program included with this result.

## Assumptions and scope
All integers \(n\ge13\) and all finite squarefree products \(P\) of distinct primes \(\ge5\) are covered, with no bound on the sizes of prime factors in \(P\). A prime \(q\mid P\) is *colliding* when \(q\mid n\) and *noncolliding* otherwise. Count noncolliding prime factors without multiplicity. The claim is about nonexistence/existence of any admissible unordered decomposition \(2n=h+(2n-h)\), with \(1\le h\le n\); it does not assert a distribution for the number of representations or for support sizes exceeding two.

## Proof
**1. Published infinite cutoff.** Let \(c=\omega(\gcd(P,n))\), \(k=\omega(P/\gcd(P,n))\). Salazar's Theorem 4.9 in arXiv:2611.10059v1 states that any zero with \(n\ge13\) has \(k\ge1\) and satisfies
\[
 (c+1)!<\frac{5(2k+3)}3\,3^k,\qquad
 n<(2(c+k)+3)(2^c3^k-1)+2. \tag{1}
\]
The right sides are increasing in \(k\ge0\). For \(k\le2\), the first inequality implies \((c+1)!<105\), hence \(c\le3\). The second then bounds \(n\) by the following strict thresholds at \(c=0,1,2,3\), respectively:
\[
 n<58,\qquad n<155,\qquad n<387,\qquad n<925. \tag{2}
\]
Thus every possible zero has \(13\le n\le924\), with the corresponding restriction in (2).

**2. Enrichment of colliding support.** For a given vanishing \(P\), adjoin every prime \(q\ge5\) dividing \(n\). This changes neither \(k\) nor the fact that \(g_P(2n)=0\), since requiring coprimality at additional primes cannot introduce a representation. The enriched squarefree support has
\[
 c=c(n):=\#\{q\ge5:q\text{ prime},\ q\mid n\}.
\]
Consequently (1)–(2) apply with this full value \(c(n)\). This is an essential step: using only the original, possibly smaller, value of \(c\) would not justify discarding any \(n\).

**3. Exhaustive prime-cover equivalence.** Define the base survivors
\[
 H_n=\{1\le h\le n:\gcd(h(2n-h),6n)=1\}.
\]
For each prime \(q\ge5\) not dividing \(n\), let
\[
 M_{n,q}=\{h\in H_n:q\mid h(2n-h)\}.
\]
Adding the complete colliding support removes exactly those \(h\) not in \(H_n\). All remaining exclusions must come from at most two noncolliding primes. Therefore a zero with \(k\le2\) exists **if and only if** there are zero, one or two such primes whose sets \(M_{n,q}\) cover \(H_n\). It is sufficient to consider \(q\le2n\), because every factor \(h\) and \(2n-h\) is between \(1\) and \(2n-1\). Conversely, a covering pair determines a valid squarefree support by adjoining every prime \(\ge5\) dividing \(n\). Neither direction involves a heuristic or a finite sampling of possible unbounded supports.

**4. Exact finite exhaustion and witnesses.** The accompanying `verify.py` uses an elementary exact prime sieve, integer \(\gcd\), and bit masks for \(H_n\). It scans every \(13\le n\le924\) meeting \(c(n)\le3\) and (2). There are exactly \(207\) such inputs: \(8\), \(109\), \(82\), \(8\) with \(c(n)=0,1,2,3\), respectively. It creates each prime mask \(M_{n,q}\) for \(5\le q\le2n\), \(q\nmid n\), and exhausts all unordered pairs plus a dummy empty mask representing fewer than two primes. The complete per-input minima are recorded in `small_support_certificate.csv` and independently recomputed from the definitions by the checker. The minimum number of uncovered base survivors is zero exactly for
\[
 n\in\{13,14,17,20,23\}.
\]
Direct substitution verifies \(g_{455}(26)=g_{385}(28)=g_{935}(34)=g_{935}(40)=g_{1955}(46)=0\). Each support has exactly two noncolliding prime factors. For each of these five inputs no single noncolliding prime covers \(H_n\); the displayed positive-support witnesses are therefore minimal in noncolliding count. Equation (1), steps 2–3 and complete enumeration together prove the asserted infinite classification.

## Verification
Run `python3 verify.py` with `small_support_certificate.csv` in the same directory, using only the Python standard library. The program recalculates all \(207\) candidate rows, compares their exact integer fields against the bundled certificate, confirms the five and only five zero minima, verifies the stated colliding-factor counts, and directly recomputes the five zero values of \(g_P\). The expected successful marker is `RESTRICTED_COPRIME_J2_OK`. The finite code does **not** prove the published analytic inequalities (1), which are imported from the cited theorem; it exhausts precisely the finite domain that those inequalities imply.

## Relationship to prior work
Salazar, *Prime supports and vanishing in restricted coprime representations*, arXiv:2611.10059v1 (first publicly submitted 2026-11-06), defines the invariant \(J(k)\), establishes global bounds, and proves the decisive restrictions (1), but does not state the exact value of \(J(2)\) or the five-instance classification. Salazar, *Exact Formulas for Restricted Coprime Representations of Even Integers with Squarefree Modulus \(6P\)*, arXiv:2609.22305v1 (2026-09-15), provides exact counting formulas and positivity criteria; its general CRT formula alone does not enumerate the sharp two-noncolliding-factor vanishing spectrum. The novelty asserted here is solely the complete small-support classification and its exact first attainable maximum, not the imported cutoff or CRT framework.

## Limitations
The proof depends on the correctness of the cited Theorem 4.9; the bundled verifier separately checks the finite exhaustive component, not the original theorem's analytic proof. The classification concerns \(2n\ge26\) and at most two noncolliding factors, not all supports, and does not identify all distinct witnessing support sets. The full set of all possible witness products remains larger than the five selected examples. Independent validation and a comprehensive search of unindexed literature have not occurred.

## References
1. A. M. Salazar, *Prime supports and vanishing in restricted coprime representations*, arXiv:2611.10059v1, 2026-11-06, Theorem 4.9. https://arxiv.org/abs/2611.10059
2. A. M. Salazar, *Exact Formulas for Restricted Coprime Representations of Even Integers with Squarefree Modulus \(6P\)*, arXiv:2609.22305v1, 2026-09-15. https://arxiv.org/abs/2609.22305
