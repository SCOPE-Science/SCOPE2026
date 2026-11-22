# The \(p\)-primary Fourier and Smith spectra of cyclic sets in random mappings

## Finding
Let \(p\ge3\) be an odd prime, let \(a\ge1\), and set \(n=p^a\). For every map \(f:[n]\to[n]\), let \(C(f)\subseteq[n]\) consist of those vertices lying on a directed cycle of the functional graph, including fixed points. Put
\[
\mu_n(A)=\#\{f:[n]\to[n]:C(f)=A\},\qquad
(T_n h)(x)=\sum_{A\subseteq[n]}\mu_n(A)h(x\oplus1_A),
\]
where \(x\in\mathbb F_2^n\), \(1_A\) is the incidence vector, and addition is coordinatewise modulo two. Write \(\lambda_n(S)=\sum_A\mu_n(A)(-1)^{|A\cap S|}\), and \(b=\nu_p((n-1)!)\).

**Theorem.** For every \(S\subseteq[n]\), with \(k=|S|\), the exact valuations are
\[
\nu_p(\lambda_n(S))=
\begin{cases}
an,&k=0,\\
b+\nu_p(k),&1\le k\le n-1,\\
b+a,&k=n.
\end{cases}
\]
In particular no multiplier vanishes, and \(T_n\) is invertible over \(\mathbb Q\), \(\mathbb R\), and \(\mathbb Q_p\). Over the local ring \(\mathbb Z_{(p)}\), its exact Smith elementary-divisor exponents are \(an\) once, \(b+a\) once, and \(b+\nu_p(k)\) with multiplicity \(\binom nk\) for each \(1\le k<n\). Exponents equal to zero represent unit factors.

Equivalently, for \(1\le k<n\), after removing the common factor \(p^b\), the \(k\)-th Walsh shell has exact valuation \(\nu_p(k)\). The normalized convolution \(p^{-b}T_n\) is integral; reduction modulo \(p\) has rank exactly
\[
\sum_{\substack{1\le k<n\\p\nmid k}}\binom nk.
\]
The non-normalized determinant is nonzero, and its \(p\)-adic valuation is the sum of the stated Smith exponents with multiplicities.

## Assumptions and scope
All maps, including maps with loops and multiple directed cycles, are counted once. The kernel is **multiplicity weighted**; it is not the indicator of possible cyclic vertex subsets. Characters are the unnormalized Walsh functions \(x\mapsto(-1)^{|S\cap\operatorname{supp}(x)|}\). The prime is odd and the number of labelled vertices is precisely a positive power of that same prime. No statement is made for arbitrary composite vertex numbers or for the prime two.

## Proof
For \(A\ne\varnothing\) with \(r=|A|\), the functional graphs with cyclic set exactly \(A\) correspond bijectively to a permutation of \(A\) and a directed forest on \([n]\) rooted at \(A\), pointing towards those roots. The forest count is \(r n^{n-r-1}\), with value one at \(r=n\). Therefore
\[
\mu_n(A)=r!\,r\,n^{n-r-1}\quad(1\le r<n),\qquad \mu_n([n])=n!,\qquad\mu_n(\varnothing)=0.
\]
This is also the uniform specialization of the known exact cyclic-set distribution. Let \(c_r\) denote these coefficients and define the binary Krawtchouk numbers
\[
K_r(k;n)=[z^r](1-z)^k(1+z)^{n-k}.
\]
Counting subsets by their intersection with \(S\) yields the exact integer formula
\[
\lambda_n(S)=\sum_{r=1}^n c_r K_r(k;n).
\]
The two terminal identities are
\[
K_{n-1}(k;n)=(-1)^k(n-2k),\qquad K_n(k;n)=(-1)^k.
\]

Set \(n=p^a\) and \(b=\nu_p((n-1)!)\). If \(r=n-1-m\ge1\) for \(m\ge1\), then \(\nu_p(n-d)=\nu_p(d)\) for each \(1\le d<n\). Comparing \(r!\) with \((n-1)!\) gives
\[
\nu_p(c_r)=b+ma-\nu_p(m!)+\nu_p(r).
\]
For an odd prime, \(\nu_p(m!)\le m-1\) when \(m\ge1\), and \(\nu_p(m!)\le m-2\) when \(m\ge2\). Consequently every coefficient with \(r\le n-2\) is divisible by \(p^{b+a}\), while every coefficient with \(r\le n-3\) is divisible by \(p^{b+2a}\). Also \(c_n=n!\) is divisible by \(p^{b+a}\).

For \(1\le k<n\), the \(r=n-1\) term gives
\[
\lambda_n(S)\equiv (n-1)!(n-1)(-1)^k(n-2k)\pmod{p^{b+a}}.
\]
Because \(0<k<p^a\) and \(p\) is odd, \(\nu_p(n-2k)=\nu_p(k)<a\); \(n-1\) is a \(p\)-adic unit. The displayed leading term has valuation \(b+\nu_p(k)\), strictly below that of the remainder, proving the interior case.

For \(k=n\), the two terminal contributions combine as
\[
c_{n-1}K_{n-1}(n;n)+c_nK_n(n;n)=(n-1)!n(n-2).
\]
The \(r=n-2\) contribution is divisible by \(p^{b+2a}\): its coefficient has valuation at least \(b+a\), and \(K_{n-2}(n;n)=-\binom n2\) has valuation \(a\). All earlier contributions have valuation at least \(b+2a\). Therefore
\[
\lambda_n([n])\equiv(n-1)!n(n-2)\pmod{p^{b+2a}},
\]
whose right side has valuation \(b+a\). Finally, \(\lambda_n(\varnothing)=n^n\) counts every self-map, so its valuation is \(an\). This completes the valuation proof, including the boundary \(n=p=3\).

Let \(H\) be the Walsh matrix on \(\mathbb F_2^n\). It satisfies \(H^2=2^nI\), so both \(H\) and \(2^{-n}H\) are invertible over \(\mathbb Z_{(p)}\), because \(p\) is odd. Fourier diagonalization \(HT_nH^{-1}=\operatorname{diag}(\lambda_n(S))\) is therefore a valid equivalence over that local ring. Removing the unit part from each nonzero diagonal entry proves the asserted complete \(p\)-primary Smith exponent multiset. In particular the normalized mod-\(p\) rank equals the number of characters with \(\nu_p(\lambda_n(S))=b\), exactly those whose weights are not divisible by \(p\).

## Verification
Run `python3 verify.py` from the directory containing the supplied script. It independently enumerates all self-maps and applies a direct Walsh transform through dimension six, comparing with the rooted-forest/Krawtchouk formula. It tests the exact multiplier valuations and normalized residues in 46 odd-prime-power dimensions through 169, and separately performs finite-field elimination on the full convolution matrices at dimensions three, five, and seven. The supplied run passed 7,435 exact assertions. These finite tests are reproducibility checks; the proof above, rather than the cutoff, establishes all parameter values.

## Relationship to prior work
The distribution of cyclic vertex sets of a random mapping, including its equivalence with a path-vertex set in a randomly marked rooted tree, is classical and is explicitly described by Pitman (2001, formula (27) and relation (49)). Hansen and Jaworski (2010; preprint circulated in 2005) study random mappings conditioned on numbers of cyclic vertices and use the permutation-and-forest construction. The present statement concerns a different object: the **full binary character spectrum of the multiplicity-weighted cyclic-set distribution and its precise local Smith invariants at prime-power vertex orders**. The previously known profile formula is an essential starting input, not claimed as new. The uniform factorial-divisibility argument and its all-shell exact-valuation conclusion are the additional result. This distinction should be checked against any unindexed signed cyclic-set enumeration.

## Limitations
The complete integer Smith form away from \(p\), real inverse norms, and invertibility for vertex sizes that are not odd prime powers are not determined. The theorem does not say that the unnormalized convolution is invertible as a matrix over \(\mathbb Z_p\); its nontrivial Smith factors obstruct that. The provenance of the underlying mapping enumeration is classical; an equivalent published modular specialization remains a historical-priority risk. No independent mathematical review is asserted.

## References
1. J. Pitman, *Random mappings, forests, and subsets associated with Abel–Cayley–Hurwitz multinomial expansions*, University of California, Berkeley Technical Report 593, 2001, particularly formulae (5), (27), and (49). https://statistics.berkeley.edu/sites/default/files/tech-reports/593.pdf
2. J. C. Hansen and J. Jaworski, *Random mappings with a given number of cyclical points*, *Ars Combinatoria* **94** (2010), 341–359; earlier manuscript circulated in 2005. https://citeseerx.ist.psu.edu/document?doi=0ff92f6476b95f9f070109f13bcc618e381cb42f&repid=rep1&type=pdf
3. M. Elsheikh and M. Giesbrecht, *Relating p-adic eigenvalues and the local Smith normal form*, arXiv:1401.1773 (2014). Here the Smith result follows directly from local invertibility of the Walsh matrix, without requiring a general eigenvalue-to-Smith theorem. https://arxiv.org/abs/1401.1773
