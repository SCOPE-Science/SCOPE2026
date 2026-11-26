# Exact initial non-repetitive complexity and first-collision witnesses in the period-doubling word

## Finding

Let \(p=p_0p_1p_2\cdots\) be the binary fixed point beginning with \(0\) of the substitution \(\sigma(0)=01\), \(\sigma(1)=00\). For each positive integer \(n\), write \(F_n(i)=p_i\cdots p_{i+n-1}\) and let \(I(n)\) be the first index \(j\ge1\) such that \(F_n(j)=F_n(i)\) for some \(0\le i<j\). Thus \(I(n)\) is the standard initial non-repetitive complexity: the length-\(n\) factors at starts \(0,\ldots,I(n)-1\) are pairwise distinct and the next repeats one of them.

**Theorem.** We have \(I(1)=2\). For every \(n\ge2\), put \(q=2^{\lfloor\log_2 n\rfloor}\). Then

\[
I(n)=\begin{cases}
3q/2,&q\le n<3q/2,\\
2q,&3q/2\le n<2q.
\end{cases}
\]

Moreover, the first repeated length-\(n\) factor has a **unique previous occurrence** among the earlier starting positions, and the pair \((i,j)\) of earlier and repeated starts is exactly \((q,3q/2)\) in the first case and \((0,2q)\) in the second case. For \(n=1\), the pair is \((0,2)\). Equivalently, \(I(n)=2I(\lfloor n/2\rfloor)\) for all \(n\ge4\), with \(I(1)=2,I(2)=3,I(3)=4\).

In particular,

\[
\liminf_{n\to\infty}\frac{I(n)}n=1,\qquad
\limsup_{n\to\infty}\frac{I(n)}n=\frac32.
\]

## Assumptions and scope

Indexing is zero-based; factors are ordinary contiguous words, with exact literal equality (not Abelian or cyclic equality). All lengths \(n\) are positive integers, and the infinite word is the one-sided period-doubling fixed point with the stated zero/one normalization. The first repeated factor is counted by its **start position** \(j\), not by the end position of the corresponding finite prefix. The result concerns this particular fixed point; shifting it changes the initial-complexity function in general.

## Proof

The substitution gives the identities \(p_{2a}=0\) and \(p_{2a+1}=1-p_a\) for every \(a\ge0\). Hence no two adjacent letters of \(p\) equal \(1\). Also \(p\) has no length-four zero factor: such a factor would include two consecutive odd positions with zero entries, forcing two consecutive source entries equal to \(1\), a contradiction.

For \(n\ge4\), no length-\(n\) factor starting at an even position equals one starting at an odd position. Indeed, the even-start factor has zero in every even relative position, whereas the odd-start factor has zero in every odd relative position. Equality would force the common factor to be all zero, contrary to the absence of \(0000\).

For \(m\ge2\), the explicit substitution block forms show that

\[
\begin{aligned}
F_{2m}(2a)&=\sigma(F_m(a)),\\
F_{2m}(2a+1)&=(1-p_a)\,0\,(1-p_{a+1})\,0\cdots(1-p_{a+m-1})\,0,\\
F_{2m+1}(2a)&=\sigma(F_m(a))\,0,\\
F_{2m+1}(2a+1)&=(1-p_a)\,0\cdots0\,(1-p_{a+m}).
\end{aligned}
\]

The displayed patterns are injective encodings of the source factors. Consequently, for a fixed parity, two length-\(2m\) factors agree exactly when the corresponding length-\(m\) source factors agree; two length-\(2m+1\) even-start factors likewise correspond to length \(m\), while two odd-start factors correspond to length \(m+1\).

Write \(I(s)\) for the first repeat index at source length \(s\). For length \(2m\), the earliest repeated **even** start is \(2I(m)\), and the earliest repeated **odd** start is \(2I(m)+1\). For length \(2m+1\), the earliest repeated even start is \(2I(m)\) and the earliest repeated odd start is \(2I(m+1)+1\). Initial non-repetitive complexity is nondecreasing with factor length, so \(I(m+1)\ge I(m)\). Since equal factors of opposite parity are impossible, the earliest repeat in both cases occurs at the even start \(2I(m)\). Thus \(I(n)=2I(\lfloor n/2\rfloor)\) for every \(n\ge4\). Its previous start is twice the previous start in the shorter source problem; before this repeat all factors are distinct, so the previous occurrence is unique.

Direct examination of the initial symbols \(01000101\cdots\) gives \((I(1),i)=(2,0)\), \((I(2),i)=(3,2)\), and \((I(3),i)=(4,0)\), where \(i\) is the unique previous start. Iterating the recurrence reduces each \(n\ge2\) to \(2\) if its binary representation begins with \(10\), or to \(3\) if it begins with \(11\). For \(q=2^{\lfloor\log_2n\rfloor}\), these are precisely the ranges \(q\le n<3q/2\) and \(3q/2\le n<2q\). Iterating the witness-position doubling simultaneously gives \((q,3q/2)\) or \((0,2q)\). This establishes the formula and witnesses.

Finally, the quotient \(I(n)/n\) has lower accumulation value \(1\) as \(n\) approaches either upper endpoint of a constant plateau, and upper accumulation value \(3/2\) at \(n=q\), while the piecewise formula bounds all quotients between \(1\) and \(3/2\). This proves both limits.

## Verification

The included `verify.py` independently constructs the substitution word and the arithmetic form \(p_i=\nu_2(i+1)\bmod2\) for the first 16384 positions, and checks agreement. It enumerates every first repeated factor and its unique earlier start for all lengths \(1\le n\le1024\), comparing them with the theorem. It additionally checks the four parity-sensitive desubstitution comparisons directly for lengths \(2m\) and \(2m+1\) with \(2\le m\le39\), \(0\le a,b<16\). Run with `python3 verify.py`; no third-party dependencies are required.

These computations are finite corroboration, not a proof for unrestricted \(n\); the unrestricted proof is the substitution-injectivity and cross-parity argument above.

## Relationship to prior work

Nicholson and Rampersad introduced explicit computations of initial non-repetitive complexity for the Thue–Morse, Fibonacci, and Tribonacci words in *Initial non-repetitive complexity of infinite words* (arXiv:1507.08206, first posted July 29, 2015). That inspected paper does not analyze the period-doubling word.

OEIS A366462 concerns the **largest** unique-factor window located anywhere in the period-doubling word, and A367184 records its first attaining starting position. Their listed fact that dyadic windows can attain the maximum at position zero supplies a partially overlapping consequence for power-of-two lengths. Neither table states or directly implies the complete initial first-collision profile and the earlier-position witness for all \(n\); notably at length \(3\), the longest unique window begins at \(1\), whereas the present initial complexity is \(4\). A presentation on automatic sequences and grouped factors also reports existence of windows containing all factors exactly once for certain lengths, but that is an existential starting-position property rather than the first-repeat index at the fixed origin.

## Limitations

The claim concerns the exact, unshifted binary period-doubling word only. It gives the location of the first collision but not all subsequent collision times. The finite checks cannot exclude a mathematical error in the all-length reasoning. Possible unindexed publications or computations specifically on initial factor collisions remain a historical-priority risk; no claim of independent audit or exhaustive literature coverage is made.

## References

1. J. Nicholson and N. Rampersad, *Initial non-repetitive complexity of infinite words*, arXiv:1507.08206 (first public version July 29, 2015). https://arxiv.org/pdf/1507.08206
2. OEIS A096268, *Period-doubling sequence*. https://oeis.org/A096268
3. OEIS A366462, *Longest unique-factor window in the period-doubling sequence*. https://oeis.org/A366462
4. OEIS A367184, *First starting position of a longest unique-factor window*. https://oeis.org/A367184
5. J. Shallit, *Decidability and Enumeration in Automatic Sequences*, slides 37–39 on grouped factors. https://cs.uwaterloo.ca/~shallit/Talks/csr.pdf
