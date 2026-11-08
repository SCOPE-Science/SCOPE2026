# Catalan residues fill every \(p\)-adic ring when \(2\) is a primitive root

## Finding
Let \(C_n=\frac{1}{n+1}\binom{2n}{n}\) be the Catalan numbers. For any odd prime \(p\) satisfying \(\operatorname{ord}_{p^2}(2)=p(p-1)\), and every integer \(k\ge1\),
\[
\{C_n\bmod p^k:n\ge0\}=\mathbb Z/p^k\mathbb Z.
\]
Every one of these residue classes occurs for infinitely many indices. Hence the \(p\)-adic closure of the Catalan numbers is the whole ring \(\mathbb Z_p\). The hypothesis holds, in particular, at \(p=3,5,11\). This is a sufficient condition, not a classification of all primes with full Catalan value images.

## Assumptions and scope
An odd prime \(p\) is fixed and \(2\) is required to generate \((\mathbb Z/p^2\mathbb Z)^\times\). By the standard lifting theorem for primitive roots, \(2\) then generates \((\mathbb Z/p^k\mathbb Z)^\times\) for every \(k\ge1\). Fix any target modulus \(p^k\). Put \(h=(p+1)/2\), so \(1<h<p\). Write \(\nu_p\) for the usual valuation. The assertion concerns existence and infinite recurrence of index witnesses, not their frequency, minimal size, or density in the indices.

## Proof
**Separated-digit binomial-unit lemma.** Fix an odd prime \(p\), integers \(k\ge1\), \(r\ge1\), and choose \(L\ge2k+3\). Given digits \(d_1,\ldots,d_r\in\{1,h\}\), put
\[
n=\sum_{i=1}^r d_i p^{Li},\qquad
v=\#\{i:d_i=h\},\qquad b_d=\binom{2d}{d}.
\]
Then
\[
\nu_p\binom{2n}{n}=v,\qquad
p^{-v}\binom{2n}{n}\equiv\prod_{i=1}^r p^{-\mathbf1_{d_i=h}}b_{d_i}\pmod{p^k}.
\]
The first identity follows from Kummer's criterion: doubling a digit \(1\) gives no carry, whereas doubling the digit \(h\) gives exactly one carry; the zero gaps absorb all carries. For clarity, the prime-power congruence can be obtained from the standard prime-to-\(p\) factorial block formula. Put \(U_p(m)=\prod_{1\le j\le m,\,p\nmid j}j\) and \(F_p(m)=m!/p^{\nu_p(m!)}\). Removing multiples of \(p\) successively gives the exact identity
\[
F_p(m)=\prod_{t\ge0}U_p(\lfloor m/p^t\rfloor).
\]
For odd \(p\), the product of all units in one complete block of length \(p^k\) is \(-1\pmod{p^k}\). Thus \(U_p(m+p^k)\equiv-U_p(m)\pmod{p^k}\). In the ratio \(F_p(2n)/F_p(n)^2\), each factor associated with \(t\) depends, modulo \(p^k\), only on the \(k\)-digit window of \(n\) beginning at \(t\), the corresponding doubled window and its incoming carry; complete-block signs cancel between windows outside their supports. The gaps of length at least \(L-2\ge2k+1\) isolate these windows. Each isolated window is exactly the one arising from \(\binom{2d p^{Li}}{d p^{Li}}\), and after cancelling complete unit blocks its contribution equals \(p^{-\mathbf1_{d=h}}\binom{2d}{d}\) modulo \(p^k\). Multiplying the nonoverlapping contributions proves the displayed congruence. This is the separated-window specialization of the classical prime-power Lucas/Granville factorial-block method; no finite numerical experiment is used to infer it.

Now \(n\equiv0\pmod{p^k}\) for the prescribed \(L\). Thus \((n+1)^{-1}\equiv1\pmod{p^k}\). Since \(b_1=2\) and \(\nu_p(b_h)=1\), define the \(p\)-adic unit \(u=b_h/p\). The lemma implies
\[
C_n\equiv p^v u^v2^{r-v}\pmod{p^k},
\]
where the right-hand congruence is meaningful even for \(v\ge k\).

To represent a nonzero target \(a\pmod{p^k}\), let \(0\le v<k\) be its exact \(p\)-adic valuation. Since \(2\) generates all units modulo \(p^{k-v}\), select a nonnegative integer \(t\) such that
\[
2^t\equiv (a/p^v)u^{-v}\pmod{p^{k-v}}.
\]
Use \(v\) digits equal to \(h\) and \(t\) digits equal to \(1\), with zeros between the occupied positions. Then \(C_n\equiv a\pmod{p^k}\). To represent zero, use at least \(k\) digits equal to \(h\). The empty digit configuration represents the unit \(1\) through \(C_0=1\), but for infinitely many positive witnesses one can instead take \(t>0\) divisible by \(\varphi(p^k)\). The same operation, adding any multiple of \(\varphi(p^{k-v})\) extra digits \(1\), yields infinitely many witnesses for each nonzero target; additional \(h\)-blocks preserve a zero target. All hypotheses are preserved as the indices grow.

Finally, \(2\) has order \(4\) modulo \(5\) and \(2^4=16\not\equiv1\pmod{25}\), and has order \(10\) modulo \(11\) with \(2^{10}=1024\not\equiv1\pmod{121}\). The primitive-root lifting criterion gives the two unconditional instances. The \(p=3\) instance follows likewise.

## Verification
The standalone integer-arithmetic program `verify_catalan.py` verifies the complete observed residue sets at \(p=3,5,11\) for prime-power moduli not exceeding \(500\) using the first \(4000\) Catalan numbers. It also tests the separated-block valuation and unit congruences for bounded indices and independently checks an index with mixed \(p=5\) digits. Successful local replay returned `VERIFY_OK`. The proof above, not the finite enumeration, supplies the unrestricted statement.

## Relationship to prior work
Rowland and Yassawi (2013, Section 3.1) computed Catalan automata modulo prime powers and posed their specific no-forbidden-residue question at \(p=3\). Burns (2017, Theorem/Corollary 2.2) established complete coverage modulo every prime \(p\ge5\), not over every power \(p^k\). Classical prime-power binomial congruences (Granville and related Lucas extensions) provide the separated-block arithmetic input, but do not by themselves state the Catalan universal-image conclusion. A previously obtained complete result for \(p=3\) is subsumed here; the new scope is the entire explicitly defined primitive-root class, including \(p=5\) and \(p=11\). In particular, the claim is not that individual Catalan coefficients or the primality criterion are new.

## Limitations
It is not proved here that infinitely many primes satisfy the primitive-root hypothesis, nor that the hypothesis is necessary. This argument makes no assertion about primes with nonprimitive \(2\), index frequencies, or minimal representing indices. An unindexed historical prime-power covering theorem could supersede the present result; priority remains subject to independent literature review. Independent validation has not been performed.

## References
1. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635v1, first publicly available 2013-10-31, especially Sections 3.1 and 5.2; Journal de Théorie des Nombres de Bordeaux 27 (2015), 245–288.
2. R. Burns, *The Catalan numbers have no forbidden residue modulo primes*, arXiv:1703.02705v1, first publicly available 2017-03-08, especially Section 2.
3. A. Granville, *Binomial coefficients modulo prime powers*, Canadian Mathematical Society Conference Proceedings 20 (1997), 253–275; classical prime-power digit/block background.
