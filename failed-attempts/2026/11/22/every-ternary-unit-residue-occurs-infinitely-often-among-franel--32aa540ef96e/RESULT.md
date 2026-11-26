# Every ternary unit residue occurs infinitely often among Franel numbers

## Finding
Define the Franel numbers by
\[
f_n=\sum_{j=0}^n\binom{n}{j}^{3}\qquad(n\ge0).
\]
For every integer \(k\ge1\), the residue set of the values \(f_n\) modulo \(3^k\) is exactly the set of units \((\mathbb Z/3^k\mathbb Z)^\times\). In fact, **every unit residue occurs infinitely often**. Consequently, the closure of \(\{f_n:n\ge0\}\) in the three-adic integers is exactly \(\mathbb Z_3^\times\), and its Haar measure is \(2/3\).

The witnesses can be chosen with only the ternary digits zero and one, using at most \(\varphi(3^k)=2\cdot3^{k-1}\) ones, with at least \(k\) zeros between successive ones. A finite explicit (though very large) bound is also available: write \(h=\varphi(3^k)\), \(J=h(h-1)+1\). Every unit residue modulo \(3^k\) has a positive witness
\[
0<n<3^{(k+1)J+1}.
\]

## Assumptions and scope
The binomial coefficients are ordinary nonnegative integer binomial coefficients; the index \(n\) ranges over all nonnegative integers. A three-adic unit means an element not divisible by three. No assertion is made about natural densities of index sets or the least index realizing a residue.

## Proof
**1. The elementary obstruction.** Since \(x^3\equiv x\pmod3\), the binomial theorem gives
\[
f_n\equiv\sum_{j=0}^n\binom nj=2^n\equiv(-1)^n\pmod3.
\]
Thus every Franel number is a three-adic unit.

**2. A prime-power block.** Let \(B=3^L\) with \(L\ge1\). For \(0<j<B\), the base-three digits of \(B-1\) are all twos, so Lucas's theorem gives \(3\nmid\binom{B-1}{j-1}\). The identity
\[
\binom Bj=\frac Bj\binom{B-1}{j-1}
\]
therefore yields the exact valuation
\[
\nu_3\!\left(\binom Bj\right)=L-\nu_3(j).
\]
Every interior binomial coefficient is divisible by three; consequently its cube vanishes modulo 27. The two endpoints contribute one each:
\[
f_{3^L}\equiv2\pmod{27}.\tag{1}
\]
For any \(k\ge1\), the residue \(u_L=f_{3^L}\pmod{3^k}\) has multiplicative order exactly \(h=2\cdot3^{k-1}\). Indeed, \(u_L\equiv2\pmod9\) implies \(\nu_3(u_L^2-1)=1\) for any integer representative congruent to 2 modulo 27. The lifting-the-exponent lemma gives
\[
\nu_3(u_L^{2\cdot3^t}-1)=t+1\quad(t\ge0),
\]
which, together with \(u_L\equiv-1\pmod3\), proves the order assertion (including \(k=1\)). Hence **every** such prime-power value is a generator of \((\mathbb Z/3^k\mathbb Z)^\times\).

**3. A separated-block congruence.** Fix \(k\ge1\) and \(L\ge k\). Put \(B=3^L\) and \(q=3^{L-k+1}\). From the exact valuation above, \(\binom Bj\equiv0\pmod{3^k}\) for every integer \(j\) not divisible by \(q\), including the convention that binomial coefficients outside \(0\le j\le B\) are zero. For every \(0\le a<q\), Vandermonde's identity and the fact that \(0\le s\le a<q\) imply
\[
\binom{B+a}{mq+t}\equiv
\begin{cases}
\binom B{mq}\binom at,&0\le t\le a,\\
0,&a<t<q,
\end{cases}
\pmod{3^k}
\]
for the relevant nonnegative indices \(m,t\), with zero out-of-range binomial coefficients. The reason is that, in the Vandermonde expansion, a nonzero summand modulo \(3^k\) must have \(q\mid(mq+t-s)\), forcing \(s=t\). Cubing this congruence and summing over all indices now factors the two sums:
\[
\boxed{f_{3^L+a}\equiv f_{3^L}f_a\pmod{3^k}}\qquad(0\le a<3^{L-k+1}).\tag{2}
\]

**4. All units and infinitely many indices.** Fix \(k\) and let \(h=2\cdot3^{k-1}\). Consider the infinitely many exponents \(L_j=(k+1)j\), \(j\ge1\). By Step 2, each \(f_{3^{L_j}}\pmod{3^k}\) lies among the finitely many generators of the unit group. Thus some generator \(u\) appears for infinitely many exponents \(L_j\). For any desired unit residue \(r\), choose \(1\le t\le h\) with \(u^t\equiv r\pmod{3^k}\), and select any \(t\) of those exponents in increasing order. The ternary number \(n\) formed by summing the corresponding powers of three has the stated digit restrictions. At each insertion of the next larger power \(3^L\), the lower part \(a\) is a sum of smaller distinct ternary powers with exponents at most \(L-k-1\), so \(0\le a<3^{L-k+1}\). Applying (2) successively yields
\[
f_n\equiv u^t\equiv r\pmod{3^k}.
\]
Because the identical-generator exponents form an infinite set, these witnesses can be chosen with arbitrarily large largest ternary position, giving infinitely many distinct indices.

**5. An explicit witness bound.** Among the first \(J=h(h-1)+1\) exponents \(L_j=(k+1)j\), the pigeonhole principle guarantees that at least \(h\) yield the same generator: there are at most \(h\) possible residue values. Taking the required \(t\le h\) among them gives the preceding construction with largest position \(\le(k+1)J\). Hence its sum is strictly less than \(3^{(k+1)J+1}\), as claimed. This completes the proof. \(\square\)

## Verification
The included standalone C++17 program `check_franel.cpp` independently constructs \(f_n\pmod{729}\) for all \(0\le n<6561\), tests the parity obstruction for all these indices, confirms the complete unit residue image modulo \(3,9,27,81,243\), and compares 4,893 separated-block congruences directly. `CHECKS.txt` records the actual successful output. Finite checks are supplementary and do not establish the universal quantifiers in the theorem; the proof above does.

## Relationship to prior work
Schulte, Van Schalkwyk and Yang establish the nondivisibility of Franel numbers by three, which is an already known necessary restriction on the value set. A published prime-power Franel theorem determines \(\nu_3(f_{3^a}-2)=3\) at all positive exponents; in particular, the prime-power generator congruence in Step 2 is already covered, and is not asserted as new. Krattenthaler and Müller provide modulo-nine congruence classifications for generalized Apéry/Franel numbers. Beukers constructs prime-power linear schemes for combinatorial sequences including Franel numbers. The novelty asserted here is the **complete all-prime-power image and infinite occurrence of every allowed residue**, not the digit method in general or any previous congruence. Related results for different sequences, including Catalan and central trinomial numbers, do not imply this statement for Franel numbers.

## Limitations
No claim is made about optimal witness sizes, index density, or equidistribution. A very large explicit bound is provided solely for existence. The literature comparison has a residual risk that an equivalent value-image theorem could be implicit in previously published general automata or congruence machinery; independent literature review has not been performed.

## References
1. F. Beukers, *\(p\)-Linear schemes for sequences modulo \(p^r\)*, arXiv:2211.15240, first submitted 2022-11-28. https://arxiv.org/abs/2211.15240
2. C. Krattenthaler and T. W. Müller, *Generalised Apéry numbers modulo 9*, arXiv:1401.1444 (2014). https://arxiv.org/abs/1401.1444
3. B. Schulte, J. van Schalkwyk, and H. Yang, *On the divisibility and valuations of Franel numbers*, 2014 mathematical research report, https://slmath-production-assets.sfo3.digitaloceanspaces.com/system/cms/files/81/files/original/Research_Reports_2014_MSRI-UP_%28Single_File%29.pdf
