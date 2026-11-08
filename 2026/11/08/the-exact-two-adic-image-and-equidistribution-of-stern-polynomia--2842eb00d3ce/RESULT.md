# The exact two-adic image and equidistribution of Stern polynomials at \(-2\)

## Finding

Let the Stern polynomials be \(B_0(t)=0\), \(B_1(t)=1\), \(B_{2n}(t)=tB_n(t)\), and \(B_{2n+1}(t)=B_n(t)+B_{n+1}(t)\). Put \(a_n=B_n(-2)\), and for every integer \(k\ge1\) define
\[
\mathcal C_k=\{(a,b)\in(\mathbb Z/2^k\mathbb Z)^2:b-5a\equiv1\pmod{2^{\min(k,3)}}\}.
\]
Then the exact consecutive residue-pair image is
\[
\{(a_n,a_{n+1})\bmod 2^k:n\ge0\}=\mathcal C_k,
\qquad |\mathcal C_k|=2^{2k-\min(k,3)}.
\]
Every residue pair in \(\mathcal C_k\) occurs infinitely often and with the natural density \(1/|\mathcal C_k|\). Thus, for every \(u\in\mathbb Z/2^k\mathbb Z\),
\[
\lim_{N\to\infty}\frac1N\#\{0\le n<N:a_n\equiv u\pmod{2^k}\}=2^{-k}.
\]
The consecutive-pair closure in \(\mathbb Z_2^2\) is \(\{(a,b):b-5a\equiv1\pmod8\}\), a clopen set with two-dimensional normalized Haar measure \(1/8\). The scalar values \(\{a_n\}\) are dense and equidistributed in \(\mathbb Z_2\).

## Assumptions and scope

The index \(n\) is a nonnegative integer, \(k\) a positive integer, all congruences are over the stated power-of-two modulus, and the natural density is taken along *all* initial intervals \([0,N)\), not merely dyadic subsequences. An affine state is an ordered pair; binary transition digits are read from most significant to least significant, allowing leading zero digits.

## Proof

**1. Binary state maps and an invariant.** Write \(v_n=(a_n,a_{n+1})\). The polynomial recurrence gives the two integral linear maps
\[
L(a,b)=(-2a,a+b),\qquad R(a,b)=(a+b,-2b),\qquad
v_{2n}=L(v_n),\quad v_{2n+1}=R(v_n).
\]
For \(\ell(a,b)=b-5a\) direct subtraction gives
\[
\ell(L(a,b))=\ell(a,b)+16a,\qquad
\ell(R(a,b))=\ell(a,b)-8b.
\]
Since \(v_0=(0,1)\), induction gives \(\ell(v_n)\equiv1\pmod8\). This proves the inclusion into \(\mathcal C_k\) for every \(k\). It also shows that \(\ell(v_n)\) is always a unit in \(\mathbb Z_2\).

**2. All projective residues can be prescribed.** For a state with odd \(\ell\), let \(x=a/\ell\in\mathbb Z_2\). Applying the two transitions gives
\[
f_0(x)=\frac{-2x}{1+16x},\qquad f_1(x)=\frac{1+6x}{-7-40x}.
\]
The denominators are odd. The image of \(f_0\) is exactly \(2\mathbb Z_2\), and that of \(f_1\) is exactly \(1+2\mathbb Z_2\): for even \(y\), the unique preimage under \(f_0\) is \(-(y/2)/(1+8y)\); for odd \(y\), the unique preimage under \(f_1\) is \(-(1+7y)/[2(3+20y)]\). Moreover each branch satisfies
\[
\nu_2(f_i(x)-f_i(y))=\nu_2(x-y)+1
\quad (x\ne y),
\]
because both Möbius determinants equal \(-2\). Consequently, each branch maps the classes modulo \(2^j\) bijectively onto the classes of its parity modulo \(2^{j+1}\). Starting from \(x=0\), the \(2^j\) words of length \(j\) yield precisely one representative of each residue modulo \(2^j\), by induction on \(j\). Thus any required projective residue \(x\bmod2^k\) can be reached by one word of length \(k\).

**3. Every unit scale allowed by the invariant can be prepared.** Fix \(k\ge1\) and perform the word consisting of one \(R\) followed by \(k\) letters \(L\), starting from any vertical state \((0,u)\). Induction shows that, modulo \(2^k\), the resulting vector is
\[
(0,\lambda u),\qquad \lambda=-5/3\in\mathbb Z_2^\times.
\]
Indeed \(R(0,u)=(u,-2u)\); after \(k\) applications of \(L\), the first coordinate is \((-2)^k u\), and the second is \(u(-2+\sum_{j=0}^{k-1}(-2)^j)\), which is \(\lambda u\) modulo \(2^k\). Since \(\lambda=1-8/3\), we have \(\nu_2(\lambda-1)=3\), whence \(\nu_2(\lambda^{2^j}-1)=3+j\) for all \(j\ge0\) by successive factorization (the second factor is \(2\bmod4\)). Therefore \(\lambda\bmod2^k\) generates the entire group \(1+8\mathbb Z/2^k\mathbb Z\) for \(k\ge3\), and that group is trivial for \(k\le3\). Repeating the block yields every vertical \((0,u)\bmod2^k\) with \(u\equiv1\pmod{2^{\min(k,3)}}\).

Now take \((A,B)\in\mathcal C_k\) and put \(d=B-5A\), a unit. Step 2 supplies a transition word \(w\) such that \(v_w=(a_w,b_w)\) has \(a_w/(b_w-5a_w)\equiv A/d\pmod{2^k}\). Write \(d_w=b_w-5a_w\equiv1\pmod8\). Step 3 supplies the vertical state \((0,u)\) with \(u\equiv d/d_w\pmod{2^k}\); the same linear word sends it to \(u v_w=(A,B)\bmod2^k\). Thus \(\mathcal C_k\) is the complete image. Repeating a whole period of the vertical scaling block before \(w\) produces arbitrarily many distinct indices with the same target state, proving infinite occurrence.

**4. Uniform distribution.** On the finite set \(\mathcal C_k\), take the Markov chain with equal probability for \(L\) and \(R\). Every target \((A,B)\) has exactly two labeled predecessors: if \(A\) is even, it lies only in the image of \(L\), and \(-2a=A\) has two solutions modulo \(2^k\), each yielding \(b=B-a\); if \(A\) is odd, it lies only in the image of \(R\), and \(-2b=B\) has two solutions, each yielding \(a=A-b\). The opposite parity of \(A,B\), forced by the defining congruence, ensures the preimages have \(\ell\equiv1\pmod{2^{\min(k,3)}}\). Explicitly, for \(L\) preimages \(\ell=B+3A\equiv B-5A\), while for \(R\) preimages \(\ell=-3B-5A\equiv B-5A\) because \(B\) is even. Thus every state has exactly two incoming labeled edges and the uniform distribution is stationary.

By Step 3 the state \(v_0=(0,1)\) reaches every member of \(\mathcal C_k\). Because the uniform distribution assigns positive mass to every state and is stationary, the chain has no transient states. Hence the finite chain has one communicating class; it is irreducible. Since \(L(v_0)=v_0\), it is also aperiodic. Its transition powers therefore converge uniformly from every initial state to the uniform law. The \(2^r\) binary words of length \(r\), including leading zeros, correspond bijectively to indices \(0\le n<2^r\); their state distribution is the \(r\)-step Markov law from \(v_0\). This proves uniformity over dyadic initial intervals.

For unrestricted \(N\), decompose \([0,N)\) into the aligned binary subintervals given by the binary expansion of \(N\), at most one of each length \(2^j\). Within a block of length \(2^j\), the leading binary prefix fixes an initial state and the remaining \(j\) digits execute exactly \(j\) random transitions. Uniform convergence of the finite Markov chain makes the normalized distribution within every sufficiently large block arbitrarily close to uniform, independently of its prefix. The total length of all blocks below a fixed size \(2^J\) is less than \(2^J\), negligible as \(N\to\infty\). Thus the full natural density of each state is \(1/|\mathcal C_k|\).

**5. Projections and closure.** For a fixed first coordinate \(A\bmod2^k\), the congruence defining \(\mathcal C_k\) has precisely \(2^{k-\min(k,3)}\) second-coordinate solutions. Dividing by \(2^{2k-\min(k,3)}\) gives \(2^{-k}\). The inverse limit of the finite images is exactly \(\{(a,b)\in\mathbb Z_2^2:b-5a\equiv1\pmod8\}\), since each finite compatible neighborhood is attained. The index-eight congruence has Haar measure \(1/8\).

## Verification

Run `python3 verify.py` using an ordinary Python 3 standard library. The checker separately computes the recurrence and the entire modular state graph for \(1\le k\le8\), compares each graph with the proposed residue coset, checks the two incoming transitions for every state, independently verifies the projective branch images and inverse formulas through \(k=9\), verifies the cyclic scale \(\lambda\) and checks dyadic empirical convergence. Finite computation supports the theorem but does not replace the proof for all \(k\) and all \(N\).

## Relationship to prior work

Ulas, *On certain arithmetic properties of Stern polynomials* (first public version 2011), studied the same recurrence, proving explicit values at \(0,-1,1,2\), polynomial congruences, and degree properties. Its Section 5, Theorem 5.1, evaluates at \(2\), not the negative evaluation \(-2\); the complete two-adic pair image and natural equidistribution are not in its examined statements. Gawron (2014), on the same polynomials, studied rational roots, degree patterns, and reciprocal polynomials, not this evaluation-residue distribution. Reznick (2006) proved modular equidistribution for consecutive terms of the classical *Stern diatomic sequence* at \(t=1\), whose matrices have unit determinant and whose primitive-pair support differs from the affine coset for \(t=-2\). The state-space proof here depends crucially on the determinant \(-2\) contractions and an independent unit-scaling loop; it is neither a statement nor a direct corollary of those results. It remains possible that another publication gives an equivalent result, and no exhaustive historical uniqueness claim is made.

## Limitations

All classifications are for the fixed specialization \(t=-2\) and moduli \(2^k\). No assertion is made about other specializations or odd primes. The finite verifier is not a proof of infinite surjectivity or equidistribution; those are established by the structural argument. No independent mathematical audit has been conducted.

## References

1. M. Ulas, *On certain arithmetic properties of Stern polynomials*, arXiv:1102.5109v1 (24 February 2011); *Publicationes Mathematicae Debrecen* **79** (2011), 55–81, DOI:10.5486/PMD.2011.4922. https://arxiv.org/abs/1102.5109 ; https://publi.math.unideb.hu/paper/1586/download/10_5486_PMD_2011_4922.pdf
2. M. Gawron, *A note on the arithmetic properties of Stern polynomials*, arXiv:1401.3553v1 (15 January 2014). https://arxiv.org/pdf/1401.3553
3. B. Reznick, *Regularity properties of the Stern enumeration of the rationals*, arXiv:math/0610601 (2006). https://arxiv.org/abs/math/0610601
