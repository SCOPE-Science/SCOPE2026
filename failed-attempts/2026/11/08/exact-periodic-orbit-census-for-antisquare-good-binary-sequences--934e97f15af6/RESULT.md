# Exact periodic-orbit census for antisquare-good binary sequences

## Finding

Call a binary word an *antisquare* if it has the form \(u\overline{u}\), where \(u\) is a nonempty binary word and the bar exchanges the two bits. Let \(X\) be the closed, shift-invariant set of two-sided binary sequences in which the only antisquares permitted are `01` and `10`. Write \(\sigma\) for the left shift and \(P_n=|\operatorname{Fix}(\sigma^n)|\) for every integer \(n\ge1\). Thus \(P_n\) counts words of length \(n\), with a marked initial position, whose bi-infinite periodic repetitions belong to \(X\); words of smaller minimal period are included.

The complete periodic-point distribution has the **rational square zeta function**
\[
\boxed{\zeta_X(z):=\exp\!\left(\sum_{n\ge1}\frac{P_n}{n}z^n\right)
       =\frac{1}{(1-z-z^4-z^6)^2}.}
\]
Equivalently, with \(P_j=0\) when \(j\le0\),
\[
\boxed{P_n=P_{n-1}+P_{n-4}+P_{n-6}
         +2[n=1]+8[n=4]+12[n=6]\quad(n\ge1).}
\]
Here \([S]\) is one if \(S\) holds and zero otherwise. The initial counts \(P_1,\ldots,P_{12}\) are
\[
2,\ 2,\ 2,\ 10,\ 12,\ 26,\ 30,\ 42,\ 56,\ 92,\ 134,\ 202.
\]
The number \(O_n\) of distinct shift orbits of *minimal* period \(n\) therefore is the exact integer
\[
\boxed{O_n=\frac1n\sum_{d\mid n}\mu(d)P_{n/d}\quad(n\ge1),}
\]
where \(\mu\) is the Möbius function. In particular \(O_1=2\), \(O_2=O_3=0\), and \(O_4=O_5=2\).

A second exact formula, without recurrence, is
\[
\boxed{P_n=2+2n\sum_{m=1}^{\lfloor n/4\rfloor}
\frac1m\sum_{j=0}^{\min(m,\lfloor(n-4m)/2\rfloor)}
\binom mj\binom{n-3m-2j-1}{m-1}.}
\]
Every sum is empty if its upper limit is below its lower limit.

## Assumptions and scope

The alphabet is precisely \(\{0,1\}\); the allowed order-one antisquares are precisely `01` and `10`. All two-sided sequences, including constant sequences, are admitted. Positions are marked in \(P_n\), whereas \(O_n\) identifies cyclic rotations. The assertion is for **all** integers \(n\ge1\), not only primitive-period words. The formal power series identity holds in \(\mathbb{Q}[[z]]\), without requiring analytic convergence.

## Proof

**1. Periodic good words have a finite forbidden description.** Let
\[
\mathcal F=\{0011,1100,0110,1001,010101,101010,001011,110100\}.
\]
The minimal-antisquare classification and Theorem 19 in Baranwal–Currie–Mol–Ochem–Rampersad–Shallit establish that avoidance of \(\mathcal F\) implies goodness: the first six exclusions remove all minimal antisquares of orders two and three, while every minimal antisquare of larger order contains `001011` or `110100`. Conversely, a bi-infinite good sequence containing `001011` must have the exceptional heteroclinic form of their Proposition 18; its complement-symmetric analogue handles `110100`. Neither exceptional sequence is periodic. Therefore, for each finite word \(w\), the bi-infinite periodic repetition \(w^\mathbb{Z}\) belongs to \(X\) **if and only if** it avoids every factor in \(\mathcal F\), across the cyclic boundary as well.

**2. Cyclic change codes classify these points.** Set \(c_i=w_i\oplus w_{i+1}\), taking subscripts modulo \(n\). The finite Pansiot-code equivalence in the same primary paper converts the exclusions in \(\mathcal F\) into avoidance of `010`, `101`, `11111`, `01110` in \(c\). Repeating \(c\) periodically, every occurrence of `1` consequently belongs to a run of **exactly two or four** ones, and each intervening run of zeros has length **at least two**. The sole cyclic code without ones is the all-zero code. An all-one code is impossible because the periodic extension contains `11111`.

Every admissible cyclic code contains an even number of ones, so \(\bigoplus_{i=0}^{n-1}c_i=0\). Hence it lifts to exactly two cyclic binary words \(w\), determined by the arbitrary first bit. The all-zero code lifts to the two constant binary sequences.

**3. Count the nonconstant cyclic codes with a marked run.** A successive zero-run followed by one-run has ordinary length generating function
\[
A(z)=(z^2+z^3+\cdots)(z^2+z^4)=\frac{z^4(1+z^2)}{1-z}.
\]
For a cyclic code with exactly \(m\ge1\) zero-runs and \(m\) one-runs in its length-\(n\) period, marking one zero-run start yields \(m\) possible marks. Conversely, choose the marked position in \(n\) ways and an ordered list of \(m\) zero/one run pairs whose lengths sum to \(n\). This is a bijective count of marked codes (even when the code has smaller minimal period), giving
\[
P_n-2=2n\sum_{m\ge1}\frac1m[z^n]A(z)^m.
\]
Expansion of \((1+z^2)^m(1-z)^{-m}\) proves the displayed binomial formula; the upper limits come from the minimum length four per run pair.

**4. Sum the logarithm.** The constant words contribute \(2\sum_{n\ge1}z^n/n=-2\log(1-z)\). Step 3 gives
\[
\begin{aligned}
\sum_{n\ge1}\frac{P_n}{n}z^n
 &=-2\log(1-z)+2\sum_{m\ge1}\frac{A(z)^m}{m}\\
 &=-2\log(1-z)-2\log(1-A(z))\\
 &=-2\log(1-z-z^4-z^6).
\end{aligned}
\]
Exponentiating proves the rational zeta identity. Taking the logarithmic derivative gives
\[
\sum_{n\ge1}P_nz^n
 =\frac{2(z+4z^4+6z^6)}{1-z-z^4-z^6},
\]
which yields the recurrence with boundary terms. Finally, every orbit of minimal period \(d\) contributes \(d\) points to \(P_n\) for each \(n\) divisible by \(d\). Möbius inversion gives the stated exact \(O_n\).

**5. Independent exact finite-state derivation.** The original forbidden set \(\mathcal F\) has maximum factor length six. Take the 32 binary five-bit states and adjoin a bit whenever the resulting six-bit suffix contains none of the forbidden words. If \(M\) is the corresponding 32-by-32 zero-one adjacency matrix, then \(P_n=\operatorname{tr}(M^n)\) for all \(n\ge1\). Exact Newton-identity calculation of its characteristic polynomial gives
\[
\det(xI-M)=x^{20}(x+1)^2(x^2-x+1)^2(x^3-x^2-1)^2,
\]
and hence \(\det(I-zM)=(1-z-z^4-z^6)^2\). The standard determinant/trace identity supplies a second proof of the zeta formula.

## Verification

Run `python3 VERIFY.py` from the directory containing this document. The standalone script uses only Python's standard library and independently constructs the 32-state forbidden-factor graph. It checks the trace counts and marked-run formula through length 40, checks Möbius inversion through length 40, computes its characteristic polynomial using exact Newton identities, enumerates all binary cyclic words of lengths one through sixteen, compares direct antisquare checks at lengths one through ten, and tests the finite Pansiot-code correspondence through length eleven. Exact script output:

`VERIFY_OK transfer_states=32 transfer_edges=44 matrix_trace_n=1..40 characteristic_polynomial_degree=32 run_pair_formula_n=1..40 mobius_orbits_n=1..40 brute_periodic_words=131070 direct_antisquare_cases=2046 finite_pansiot_cases=4094`

The infinite result is established by the symbolic proof above, not inferred from the finite checks.

## Relationship to prior work

Baranwal, Currie, Mol, Ochem, Rampersad and Shallit, *Antisquares and Critical Exponents* (first public 2022), provide the minimal-antisquare classification, the exceptional nonperiodic configurations, the finite Pansiot-code restrictions, and an asymptotic growth result for **finite linear** good words. These foundations are essential and explicitly credited. Their Theorem 19 identifies the supergolden exponential growth rate, but does not state the exact periodic-point counts, the all-period Möbius orbit census, or the rational-square dynamical zeta function here. Cyclic boundary conditions and the exceptional nonperiodic branch require separate treatment; the linear recurrence alone is not a periodic-point count.

The OEIS entry A307732 tabulates unrestricted finite linear good words, not length-labeled periodic points or primitive circular orbits. Circular square-avoidance is a different predicate from antisquare-avoidance. No claim is made that the underlying forbidden-list or Pansiot representation is new.

## Limitations

The theorem concerns periodic points of the full good subshift, not the total number of good finite factors or the number of arbitrary aperiodic sequences. The 32-state certificate is finite and exact, but the printed short diagnostic tables are not by themselves an infinite proof. Bibliographic searches cannot rule out a previously unindexed equivalent orbit formula. The result does not classify the remaining aperiodic part of the subshift and does not assert independent mathematical validation.

## References

- A. Baranwal, J. Currie, L. Mol, P. Ochem, N. Rampersad and J. Shallit, *Antisquares and Critical Exponents*, Discrete Mathematics & Theoretical Computer Science **25** (2023), Article 11; arXiv:2209.09223, first submitted 2022-09-19. https://arxiv.org/abs/2209.09223 ; DOI: 10.46298/dmtcs.10063. Especially Section 6, Proposition 18 and Theorem 19 in Section 7.
- OEIS Foundation, A307732, *Number of length-n binary words containing no antisquares except 01 and 10*. https://oeis.org/A307732 . This enumerates ordinary finite words, not periodic points.
