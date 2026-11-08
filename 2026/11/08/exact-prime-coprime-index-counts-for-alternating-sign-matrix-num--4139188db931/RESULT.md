# Exact prime-coprime index counts for alternating sign matrix numbers

## Finding

Let \(A_n\) be the number of \(n\times n\) alternating sign matrices, with \(A_0=1\). For a prime \(p\ge5\) and integer \(r\ge0\), define the natural prime-coprimality counting invariant
\[
C_p(r)=\#\{n\in\mathbb Z:0\le n<p^r,\ p\nmid A_n\}.
\]
Put \(b_p=(2p+1)/3\) if \(p\equiv1\pmod6\), and \(b_p=(2p-1)/3\) if \(p\equiv5\pmod6\). Then, for every \(r\ge0\),
\[
\boxed{C_p(r)=\begin{cases}
b_p^r,&p\equiv1\pmod6,\\
b_p^r+2\dfrac{b_p^r-1}{b_p-1},&p\equiv5\pmod6.
\end{cases}}
\]
In particular the natural density of indices for which \(p\nmid A_n\) is zero, but those indices have exact growth exponent \(\log_p b_p\) on prime-power intervals.

More precisely, let \(K_p\subseteq\mathbb Z_p\) be the closure of the nonnegative indices \(n\) with \(p\nmid A_n\). The minimum number of radius-\(p^{-r}\) balls needed to cover \(K_p\) is exactly \(C_p(r)\); consequently its upper and lower \(p\)-adic box-counting dimensions agree and equal \(\log_p b_p\). No assertion about its Hausdorff dimension is required.

## Assumptions and scope

An alternating sign matrix has entries in \(\{0,1,-1\}\), each row and column sums to one, and nonzero entries alternate in sign. The classical product enumeration is
\[
A_n=\prod_{j=0}^{n-1}\frac{(3j+1)!}{(n+j)!}.
\]
Throughout, \(p\ge5\) is prime. The count uses \(0\le n<p^r\), so the endpoint \(p^r\) is excluded. The index \(n=0\) is included; for \(r=0\), it is the sole index. The cases \(p=2,3\) are excluded from the theorem.

## Proof

**1. Nonnegative prime-power layers.** For an integer \(m=p^a\) with \(a\ge1\), put
\[
L_m=\left\lfloor\frac{m+1}{3}\right\rfloor,
\qquad h_m(t)=\max\{0,\min(t-L_m,m-L_m-t)\},\quad0\le t<m.
\]
Legendre's factorial-valuation identity applied to the product enumeration gives
\[
\nu_p(A_n)=\sum_{a\ge1}h_{p^a}(n\bmod p^a).
\tag{1}
\]
For completeness, write the increment at scale \(m\) as
\[
\delta_m(n)=\left\lfloor\frac{3n+1}{m}\right\rfloor+\left\lfloor\frac n m\right\rfloor-\left\lfloor\frac{2n+1}{m}\right\rfloor-\left\lfloor\frac{2n}{m}\right\rfloor.
\]
It has period \(m\), because shifting \(n\) by \(m\) changes the four floors by \(3,1,2,2\) respectively. Direct comparison of the four floors over \(0\le n<m\) shows that their cumulative sum, starting at zero, increases by one between \(L_m\) and the middle, decreases by one symmetrically, and vanishes outside the middle interval; it is precisely \(h_m\). The cumulative sum over a whole period is zero. Summing the increments and then the Legendre layers proves (1). This is the classical periodic triangular-layer formula established by Frey and Sellers and independently appearing in related factorial-quotient work; equation (1) is used as a prior result, not proposed as new.

Each summand of (1) is nonnegative. Thus \(p\nmid A_n\) if and only if for every \(a\ge1\), with \(m=p^a\),
\[
n\bmod m\in I_m:=[0,L_m]\cup[m-L_m,m-1].
\tag{2}
\]
The intervals in (2) are disjoint because \(2L_m<m\). For \(0\le n<p^r\), every layer with \(a>r\) vanishes: indeed, \(n<p^r\le L_{p^{r+1}}\le L_{p^a}\), and \(n\bmod p^a=n\). Therefore (2) only needs to be checked through \(a=r\).

**2. Lifting admissible residues.** Let \(S_a\subseteq[0,p^a-1]\) be the integers whose residues satisfy (2) at every level \(1\le j\le a\). Put \(c_a=|S_a|\), \(c_0=1\). Every admissible residue \(u\in S_a\) lifts to an integer \(t p^a+u\), with \(0\le t<p\); whether this lift survives depends solely on the top-level interval \(I_{p^{a+1}}\).

Write \(m=p^a\) and \(L=L_m\). Its lower and upper admissible components contain \(S_a^{\mathrm{lo}}=S_a\cap[0,L]\) and \(S_a^{\mathrm{hi}}=S_a\cap[m-L,m-1]\). These partition \(S_a\). Both endpoints \(L\) and \(m-L\) belong to \(S_a\): this is immediate at \(a=1\); the endpoint identities below propagate the assertion to every subsequent scale.

**3. Prime class \(p\equiv1\pmod6\).** Write \(p=3d+1\). Since every \(p^a\equiv1\pmod3\), one has
\[
L_{pm}=dm+L.
\]
At the next level all \(d\) digits \(t=0,\ldots,d-1\) are permitted for any \(u\in S_a\), and all \(d\) digits \(t=2d+1,\ldots,3d\) likewise. The two boundary digits \(t=d\) and \(t=2d\) permit exactly \(S_a^{\mathrm{lo}}\) and \(S_a^{\mathrm{hi}}\), respectively. Hence
\[
c_{a+1}=2d c_a+|S_a^{\mathrm{lo}}|+|S_a^{\mathrm{hi}}|=(2d+1)c_a.
\]
At level one the interval \(I_p\) has \(2L_p+1=2d+1\) elements, giving \(c_r=(2d+1)^r=b_p^r\), also at \(r=0\). Endpoint admissibility propagates because \(L_{pm}\bmod m=L\) and \((pm-L_{pm})\bmod m=m-L\).

**4. Prime class \(p\equiv5\pmod6\).** Write \(p=3d+2\), with \(d\ge1\). The exact identity, valid for either residue of \(m\) modulo three, is
\[
L_{pm}=(d+1)m-L.
\]
The full unrestricted digits \(t=0,\ldots,d-1\) and \(t=2d+2,\ldots,3d+1\) contribute \(2d c_a\). At \(t=d\), the condition is \(u\le m-L\), accepting all of \(S_a^{\mathrm{lo}}\) and the one valid upper endpoint \(u=m-L\). At \(t=2d+1\), the condition is \(u\ge L\), accepting all of \(S_a^{\mathrm{hi}}\) and the one valid lower endpoint \(u=L\). The two extra endpoints are distinct because \(2L<m\). The endpoint identity also gives \(L_{pm}\bmod m=m-L\) and \((pm-L_{pm})\bmod m=L\); induction proves both exceptional endpoints remain admissible. Therefore
\[
c_{a+1}=(2d+1)c_a+2.
\]
Initially \(c_1=2L_p+1=2d+3\), so this recurrence also holds from \(c_0=1\). Solving yields
\[
c_r=(2d+1)^r+2\frac{(2d+1)^r-1}{2d},
\]
which is the asserted second formula. Finally, \(c_r=C_p(r)\) by the truncation observation in step 1.

**5. Closed set and density.** A residue class modulo \(p^r\) meets \(K_p\) exactly when it lies in \(S_r\): if it does, its least nonnegative representative itself has \(p\nmid A_n\), by step 1; if it does not, every integer in the class has a positive layer in (1). Thus the number of radius-\(p^{-r}\) balls meeting \(K_p\) is \(c_r\). Both formulas have \(c_r\asymp b_p^r\), so the box-counting dimension is \(\log_p b_p\). Since \(b_p<p\), \(c_r/p^r\to0\); comparing an arbitrary interval \([0,N)\) with adjacent prime-power endpoints proves ordinary natural density zero. This completes the proof.

## Verification

A standalone standard-library program `verify.py` evaluates \(\nu_p(A_n)\) from factorial valuations independently of the digit-layer recurrence, for thirteen primes from five through forty-seven and prime-power index ranges. It compares all \(160861\) individual indices with the predicted counts, checks endpoint-prefix admissibility, and emits `VERIFY_OK` when all assertions hold. Representative exact counts are \(C_5(1),\ldots,C_5(6)=(5,17,53,161,485,1457)\), \(C_7(1),\ldots,C_7(5)=(5,25,125,625,3125)\), and \(C_{11}(1),\ldots,C_{11}(4)=(9,65,457,3201)\). The verifier establishes finite checks only; the unrestricted proof is above.

Reproduce with `python3 verify.py` alongside this document, without third-party libraries.

## Relationship to prior work

The integer product formula is the alternating sign matrix enumeration theorem of Zeilberger. Cartwright and Kupka's 2002 work and Frey and Sellers' preprint dated January 15, 2002 already characterize each prime-divisibility event and give equivalent nonnegative local layers; those achievements are acknowledged in step 1. Frey and Sellers also proved that each prescribed valuation occurs at infinitely many indices when \(p>3\). Sun and Moll studied the valuations at two and three; Beyerstedt, Moll and Sun developed explicit prime-power periodic components; Heuberger and Prodinger derived precise analytic expressions for individual valuations, with first-listed MSC 11A63.

The present result concerns a different *global counting invariant*: the exact number of coprime indices below every prime power, the exceptional boundary correction when \(p\equiv5\pmod6\), and the consequent metric entropy of the full prime-coprime index closure. None of the inspected works states the all-prime closed-form count or its resulting box dimension. Because the membership test was already known, this claim is a quantitative consequence of prior structural machinery, not a new individual-index divisibility criterion. Historical priority beyond inspected works is not certified.

## Limitations

The formula is restricted to primes at least five and to initial intervals of prime-power length; no pointwise asymptotic constant for arbitrary real cutoffs is claimed. The box-counting dimension is established, but a Hausdorff-dimension formula is not claimed. The historical literature might contain an unlocated equivalent counting identity; independent validation is not performed.

## References

- D. Zeilberger, “Proof of the alternating sign matrix conjecture,” *Electronic Journal of Combinatorics*, R13 (1995/1996), https://doi.org/10.37236/1271 .
- D. D. Frey and J. A. Sellers, “Prime Power Divisors of the Number of \(n\times n\) Alternating Sign Matrices,” preprint dated January 15, 2002, https://www.d.umn.edu/~jsellers/p23.pdf .
- D. I. Cartwright and J. G. Kupka, “When Factorial Quotients are Integers,” *Gazette of the Australian Mathematical Society* 29 (2002), 19–26, https://research.monash.edu/en/publications/when-factorial-quotients-are-integers .
- X. Sun and V. H. Moll, “The p-adic valuations of sequences counting alternating sign matrices,” arXiv:0901.4564v1 (2009), https://arxiv.org/abs/0901.4564 .
- C. Heuberger and H. Prodinger, “A precise description of the p-adic valuation of the number of alternating sign matrices,” arXiv:0908.0149v1 (2009), https://arxiv.org/abs/0908.0149 .
- E. Beyerstedt, V. H. Moll and X. Sun, “The p-adic valuation of the ASM numbers,” *Journal of Integer Sequences* 14 (2011), Article 11.8.7, https://cs.uwaterloo.ca/journals/JIS/VOL14/Moll/moll2.pdf .
