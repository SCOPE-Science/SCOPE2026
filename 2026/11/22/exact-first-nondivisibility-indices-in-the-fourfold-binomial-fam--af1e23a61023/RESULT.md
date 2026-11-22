# Exact first nondivisibility indices in the fourfold binomial family

## Finding
For every positive integer \(b\), define \(f_4(b)\) to be zero if \(bn+1\) divides \(\binom{(b+4)n}{4n}\) for every positive integer \(n\), and otherwise the least positive \(n\) at which this divisibility fails. Then
\[
 f_4(b)=\begin{cases}
 0,&b\text{ even},\\[2pt]
 \displaystyle\frac{2^{2\lfloor(\nu_2(b+3)-1)/2\rfloor+1}+1}{3},&b\text{ odd}.
 \end{cases}
\]
Here \(\nu_2\) denotes the exponent of two dividing a positive integer. Thus the first-failure index depends only on the two-adic order of \(b+3\), with successive odd/even orders sharing a plateau. The positive first-failure indices form exactly \(1,3,11,43,171,\ldots\), and all occur.

## Assumptions and scope
Integers \(b,n\) are positive; binomial coefficients are ordinary integers. No finite upper bound on \(b\), \(n\), or \(\nu_2(b+3)\) is assumed. The theorem concerns the **first** failure of the full divisibility \(bn+1\mid\binom{(b+4)n}{4n}\), not the valuation at every later index and not the number of later failures. The exact first-failure function belongs to the classical divisibility problem introduced by Z.-W. Sun.

## Proof
Put \(m=bn+1\), \(M=(b+4)n\), and \(B=\binom M{4n}\). The integer identity
\[
4nB=m\binom M{4n-1},\qquad \gcd(m,n)=1
\]
shows that \(m/\gcd(m,4)\) divides \(B\). If \(b\) is even, \(m\) is always odd; hence \(m\mid B\) for all \(n\).

Suppose \(b\) is odd. Even \(n\) give odd \(m\) and no failure. For odd \(n\), writing \(E=\binom{(b+4)n}{4n-1}\), the identity gives
\[
\nu_2(B)-\nu_2(m)=\nu_2(E)-2.
\]
All odd-prime valuations of \(B\) already dominate those of \(m\). Consequently **failure is equivalent to \(\nu_2(E)\le1\)**. By Kummer's theorem this is equivalent to at most one binary carry when adding \(4n-1\) and \(bn+1\).

Let \(k=\nu_2(b+3)\ge1\), and let \(h=2\lfloor(k-1)/2\rfloor+1\), the largest positive odd integer no greater than \(k\). Define \(n_h=(2^h+1)/3\), a positive odd integer. If \(h=1\), there is no positive \(n<n_h\). For \(h\ge3\), we prove the following carry lemma:

**Carry lemma.** For any odd \(h\ge3\) and odd positive \(n<n_h\), the addition of \(4n-1\) and \(1-3n\pmod{2^h}\) makes at least two carries among its lowest \(h\) binary positions.

Here is a finite-state proof, with a complete transition and an independently executable certificate in `checker.py`. Read the \(h\) digits of \(n\) from least to most significant, forcing the first to be one. Maintain a state \((R,M,S,u,v,C,T)\), initially \((-1,1,-1,0,0,0,0)\). The states \(R,M,S\) are signed carry quotients for \(4n-1\), \(1-3n\), and \(3n-1\), respectively; \(u,v\) delay the last two input bits, \(C\) is the binary addition carry, and \(T\) is the addition-carry count capped at two. For a new bit \(d\in\{0,1\}\), put
\[
 a=v+R,\quad c=M-3d,\quad
 \rho=a\bmod2,\quad\mu=c\bmod2,\quad
 C'=\left\lfloor\frac{\rho+\mu+C}{2}\right\rfloor
\]
(with residues in \(\{0,1\}\)) and update
\[
 (R,M,S,u,v,C,T)\longmapsto
 \left(\left\lfloor\frac a2\right\rfloor,
 \left\lfloor\frac c2\right\rfloor,
 \left\lfloor\frac{S+3d}{2}\right\rfloor,
 d,u,C',\min\{2,T+C'\}\right).
\]
After \(h\) digits, \(S=\lfloor(3n-1)/2^h\rfloor\), and \(T\) counts (up to two) the binary carries in the low \(h\) positions. Direct finite set propagation produces four states after three digits, eleven after five digits, and precisely the **same eleven-state set after every additional pair of digits**; the exact two-step closure and the eleven states are checked in `checker.py`. At both odd-depth reachable sets, every state with \(S=0\) has \(T=2\). This proves the lemma for arbitrarily large odd \(h\), because \(n<n_h\) is exactly \(3n-1<2^h\), hence \(S=0\).

Since \(b\equiv-3\pmod{2^h}\), the lowest \(h\) binary positions of \(bn+1\) and \(1-3n\) coincide. The lemma therefore forces at least two carries in \((4n-1)+(bn+1)\) for every earlier positive odd \(n<n_h\), proving divisibility at all earlier indices.

Finally write \(b+3=2^h q\). The maximality of odd \(h\le k\) ensures \(\nu_2(q)\in\{0,1\}\). At \(n=n_h\), the identity \(3n_h-1=2^h\) gives
\[
 4n_h-1=2^h+n_h,\qquad bn_h+1=2^h(qn_h-1).
\]
Their low \(h\) bits do not interact, and above position \(h\) the addition is exactly \(1+(qn_h-1)=qn_h\). Thus Kummer's binary carry count equals \(\nu_2(qn_h)=\nu_2(q)\le1\). The divisibility fails at \(n_h\), and all earlier indices work. This gives the announced formula. For odd \(h\), choosing \(b=2^h-3>0\) (when \(h\ge3\)) realizes each higher threshold; the first threshold occurs at \(b=1\).

## Verification
Run `python checker.py` with Python 3 and no third-party packages. The checker reconstructs the exact four-state depth-three and eleven-state depth-five reachable sets, proves their two-step closure, and checks that none of their accepted terminal states has fewer than two carries. This is a finite exhaustive certificate for the all-\(h\) carry lemma, **not** an extrapolation from small values of \(h\). It separately tests the signed-carry interpretation on literal integers, checks first failures across odd \(b<2002\) against Kummer's digit formula, and compares integer binomial divisibility directly over \(1\le b<76\) and \(1\le n<28\). The last tests are supportive finite cross-checks only.

## Relationship to prior work
Sun introduced the family of divisibility problems and the first-failure function. Guo and Krattenthaler, *Some divisibility properties of binomial and q-binomial coefficients*, arXiv:1301.7651v3, Theorem 2.1, show infinitely many failures when a prime dividing the first coefficient parameter does not divide the second and provide an upper bound. Those statements do not specify the least failure for the entire \(a=4\) family. The present theorem gives the exact minimum for every \(b\), including a two-adic odd/even plateau not determined by that upper bound.

## Limitations
The result does not give a complete classification of later failures or extend to arbitrary first parameters \(a\). Its historical novelty is conditional on the literature comparisons described in `REVIEW.md` and `AUDIT.json`; no independent literature or proof audit has been carried out. An earlier unpublished or unindexed determination of this fixed-parameter family cannot be excluded. The originating 2012 paper and the later 2013 proof were inspected in their available full texts; priority in unindexed or other earlier work remains uncertain.

## References
1. Z.-W. Sun, *On divisibility concerning binomial coefficients*, arXiv:1005.1054, first submitted 2010-05-06. Establishes the general divisibility context.
2. Z.-W. Sun, *On divisibility of binomial coefficients*, Journal of the Australian Mathematical Society 93 (2012), 189–201; DOI: 10.1017/S1446788712000171; first verified public online date 2012-09-19. Introduces the precise first-failure problem.
3. V. J. W. Guo and C. Krattenthaler, *Some divisibility properties of binomial and q-binomial coefficients*, arXiv:1301.7651v3 (initial public version 2013-01-31), especially Sections 1, 2, 4 and 7.
4. E. Kummer, classical carry theorem for binomial valuations (1852).
