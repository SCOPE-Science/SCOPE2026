# Uniform local admissibility of Lucas-balancing Carmichael prime triples

## Finding

Let \(C_0=1\), \(C_1=3\), and \(C_{j+2}=6C_{j+1}-C_j\). **For every fixed positive even integer \(n\), the Korselt-compatible three-form family associated with \((C_n,C_{n+1},C_{n+2})\) contains an explicitly specified admissible triple of positive affine-linear forms.** In particular, assuming Dickson's conjecture on admissible prime tuples, there are infinitely many distinct Carmichael numbers of the form
\[
(1+aC_n)(1+aC_{n+1})(1+aC_{n+2}),\qquad a\in\mathbb Z_{>0},
\]
with each of the three displayed factors prime, for **every** fixed such \(n\).

More explicitly, put \(A=C_n\), \(B=C_{n+1}\), \(D=C_{n+2}\), \(M=AD\),
\[
k_0=\frac{25M+7}{48},\qquad e\in\{0,1\},\quad e\equiv k_0\pmod 2,
\qquad K=k_0+eM.
\]
Then \(k_0\) is a positive integer, \(K\) is positive and even, and the three polynomials
\[
L_A(u)=1+AB(K+2Mu),\quad
L_B(u)=1+B^2(K+2Mu),\quad
L_D(u)=1+DB(K+2Mu)
\]
are admissible: for every prime \(\ell\) there is a residue \(u\pmod\ell\) with \(\ell\nmid L_A(u)L_B(u)L_D(u)\). If all three are prime, their product is a Carmichael number.

## Assumptions and scope

Indices \(n\) are fixed, even, and at least \(2\); \(u\) ranges over nonnegative integers. A set of positive-slope integral linear forms is *admissible* if its product has no fixed prime divisor. The unconditional assertion is admissibility and the Carmichael conclusion whenever the three values are prime. Infinitely many simultaneous primes is **conditional** on Dickson's conjecture, not proved here. The three factors are strictly increasing because \(0<A<B<D\), so they are distinct.

## Proof

**1. Recurrence identities.** Direct substitution in the recurrence shows \(C_jC_{j+2}-C_{j+1}^2=8\) for every \(j\ge0\): the left side is invariant under shifting \(j\), and its value at \(j=0\) is \(1\cdot17-3^2=8\). Moreover, \(\gcd(C_j,C_{j+1})=1\), by the Euclidean algorithm and the initial values. The recurrence modulo \(48\) has the repeating pattern \(1,3,17,3\). Consequently, for even \(n\),
\[
M=AD=B^2+8\equiv17\pmod{48},\quad B\equiv3\pmod{48},\quad \gcd(M,48)=1.
\]
Also \(\gcd(A,D)=\gcd(A,6B)=1\): \(\gcd(A,B)=1\) and \(\gcd(A,6)=1\), because \(A\equiv1\) or \(17\pmod{48}\). Thus \(A\), \(B\), \(D\) are pairwise coprime; every prime dividing \(M\) is at least \(5\) and divides exactly one of \(A,D\).

As \(M\equiv17\pmod{48}\), the number \((25M+7)/48\) is integral, since \(25\cdot17+7=432\) is divisible by \(48\). It satisfies \(48k_0=25M+7\). Since \(M\) is odd, adding \(eM\) makes \(K\) even; hence \(k(u)=K+2Mu\) is even for every integer \(u\), and \(48k(u)\equiv7\pmod M\).

**2. The local obstruction calculation.** Fix any prime \(\ell\). If \(\ell=2\), all three coefficients \(AB,B^2,DB\) are odd, but \(k(u)\) is even, hence each form is \(1\pmod2\). If \(\ell\mid B\), all three forms are \(1\pmod\ell\), including at \(\ell=3\).

Suppose \(\ell\mid M\). Then \(\ell\ge5\), so \(48\) is invertible modulo \(\ell\), and the congruence for \(k(u)\) gives \(k(u)\equiv7/48\pmod\ell\). Also \(B^2=M-8\equiv-8\pmod\ell\), so \(L_B(u)\equiv1-8(7/48)=-1/6\not\equiv0\pmod\ell\). If \(\ell\mid A\), the recurrence gives \(D\equiv6B\pmod\ell\). Thus \(L_A(u)\equiv1\) and \(L_D(u)\equiv1+6B^2(7/48)=-6\pmod\ell\). If \(\ell\mid D\), the same argument exchanges \(A,D\). The three residues are therefore \(1,-1/6,-6\) in some order, all nonzero modulo primes \(\ell\ge5\).

Finally, if \(\ell\nmid2BM\), then \(\ell\ge5\), and each nonconstant linear form \(1+BC_i(K+2Mu)\) excludes at most one residue of \(u\pmod\ell\). Three forms exclude at most three residues, strictly fewer than \(\ell\). Thus a residue avoiding all three exists. These cases exhaust all primes and prove admissibility for each even \(n\).

**3. The Carmichael property for prime values.** Put \(a=Bk(u)\), \(p_A=1+aA\), \(p_B=1+aB\), \(p_D=1+aD\), and \(N=p_Ap_Bp_D\). Suppose all three values are prime. They are distinct odd primes. For each \(i\in\{A,B,D\}\), with \(j,k\) the other two indices, expansion modulo \(ai\) gives
\[
N-1\equiv a(j+k+ajk)\pmod{ai}.
\]
For \(i=B\), the bracket is \(A+D+aAD=B(6+k(u)M)\), divisible by \(B\). For \(i=A\), using \(D\equiv6B\pmod A\) and \(B^2\equiv-8\pmod A\), the bracket is congruent to \(B(7-48k(u))\pmod A\), which vanishes because \(A\mid M\mid48k(u)-7\). The same argument for \(i=D\) uses \(A\equiv6B\pmod D\). Therefore \(p_A-1\), \(p_B-1\), and \(p_D-1\) each divide \(N-1\). Korselt's criterion implies that \(N\) is Carmichael.

**4. Conditional infinitude.** The three integral linear forms have distinct positive slopes. Under Dickson's conjecture, an admissible set of three such forms takes simultaneous prime values at infinitely many positive integers \(u\). Their products strictly increase with \(u\), giving infinitely many distinct Carmichael numbers for each fixed even \(n\).

## Verification

The accompanying `verify_local_admissibility.py` independently reproduces the recurrence identities and constructs the three forms. It checks all \(17\) even indices \(n\in\{2,4,\ldots,34\}\) and all \(37\) primes below \(160\), testing every residue \(u\pmod\ell\) for a nonzero triple product; it also checks the stronger expected local counts. As an independent nonvacuous example for \(n=2\), the integer \(k=7136252\) corresponds to \(u=363\) and gives the three primes \(12010312117\), \(69942405853\), and \(407644122997\), whose product satisfies Korselt's divisibilities. These finite calculations do **not** replace the proof for all indices and primes.

Run with `python3 verify_local_admissibility.py` (Python 3 standard library; no network access or external packages needed).

## Relationship to prior work

Bensella's November 2026 preprint gives the **necessary and sufficient Korselt congruence**, conditional on primality, and parametrizes its integer solutions; it explicitly does not assert infinitely many prime triples in these families. The present result proves the previously unresolved **local nonobstruction** for each even-index ray and hence a Dickson-conditional infinitude statement. Chernick's classical Dickson-conditional construction and Wright's general Carmichael-prime-factor results address other prime forms or the number of prime factors; their general implication alone does not establish admissibility of this specific recurrence-constrained triple. Results about *Lucas–Carmichael numbers* require \(p+1\mid N+1\), a different property from Korselt's \(p-1\mid N-1\), and do not imply this claim.

## Limitations

The theorem proves admissibility unconditionally but **does not prove infinitely many prime triples unconditionally**; the infinitude statement relies on unproved Dickson's conjecture. It provides no prime-triple asymptotic and does not classify all Carmichael products of this type. Earlier work supplies the underlying Korselt parametrization. A separate independent proof assessment and an exhaustive search of unindexed literature have not been conducted.

## References

1. H. Bensella, *A Korselt Characterization of Carmichael Numbers of the Form \((aC_n+1)(aC_{n+1}+1)(aC_{n+2}+1)\)*, arXiv:2611.02054v1 (first posted 2026-11-01), https://arxiv.org/abs/2611.02054.
2. T. Wright, *Factors of Carmichael Numbers and an Even Weaker \(k\)-Tuples Conjecture*, Bull. Aust. Math. Soc. **99** (2019), 376–384, https://doi.org/10.1017/S0004972719000133.
3. J. Chernick, *On Fermat's simple theorem*, Bull. Amer. Math. Soc. **45** (1935), 269–274; its Dickson-conditional application is described in Wright (2019).
4. A. Korselt, *Problème chinois*, L'intermédiaire des mathématiciens **6** (1899), 142–143.
