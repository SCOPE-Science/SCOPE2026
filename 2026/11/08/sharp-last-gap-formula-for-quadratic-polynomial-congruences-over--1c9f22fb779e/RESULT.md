# Sharp last-gap formula for quadratic polynomial congruences over every residue ring

## Finding

For integers \(m\ge 2\) and \(n\ge 1\), let \(\mathcal Q_{m,n}\) denote the polynomial functions \((\mathbb Z/m\mathbb Z)^n\to\mathbb Z/m\mathbb Z\) represented by integer polynomials of total degree at most two. For \(f\in\mathcal Q_{m,n}\), let \(Z(f)=\#\{x\in(\mathbb Z/m\mathbb Z)^n:f(x)=0\}\). Define
\[
\delta_p(n)=\begin{cases}
1/2,&p=2,\ n=1,\\
1/4,&p=2,\ n\ge2,\\
(p-2)/p,&p\ge3,
\end{cases}
\qquad
\delta(m,n)=\min_{p\mid m}\delta_p(n),
\]
where the minimum runs over distinct prime divisors of \(m\). Then the largest number of zeros among all **nonzero polynomial functions** in \(\mathcal Q_{m,n}\) is exactly
\[
\boxed{\max_{f\in\mathcal Q_{m,n},\ f\not\equiv0} Z(f)=m^n(1-\delta(m,n)).}
\]
The zero function has \(m^n\) zeros. Hence the gap between the two largest *distinct* attainable zero counts is precisely \(m^n\delta(m,n)\). In particular, for every \(q\ge1\), the gap at modulus \(2^q\) is \(2^{q-1}\) for one variable and \(2^{qn-2}\) for every \(n\ge2\). This proves the last-gap pattern proposed by Surowka and Regan and gives its exact extension to arbitrary composite moduli.

## Assumptions and scope

The coefficients and evaluation variables are ordinary residue classes modulo \(m\); the *total polynomial degree* is at most two, and no variable-domain restriction is imposed. The expression \(f\not\equiv0\) means nonzero as a function, not merely nonzero as a formal polynomial: for example, some nonzero formal polynomials induce the zero function over a ring with zero divisors. The count is over the complete \(m^n\)-point residue grid. A nonzero constant function is allowed and has no zeros. The result includes prime and composite moduli, with \(m=1\) excluded.

## Proof

**1. Reduction to local rings.** By the Chinese remainder theorem, a polynomial function modulo \(m\) has a component modulo every \(p^r\parallel m\). If the global function is nonzero, at least one local component is nonzero. For that prime \(p\), the fraction of global arguments on which the function is nonzero is at least the fraction of local arguments on which its \(p^r\)-component is nonzero. It suffices to show that every nonzero quadratic polynomial function modulo \(p^r\) has nonzero support at least \(\delta_p(n)\).

**2. Normalization by the least valuation of values.** Fix \(p^r\) and a nonzero function represented by an integer quadratic polynomial \(f\). Let \(k\), with \(0\le k<r\), be the minimum of \(v_p(f(x))\) over integral arguments, with valuations truncated at \(r\). Every value of \(f\) is divisible by \(p^k\), and some value is not divisible by \(p^{k+1}\). The Newton expansion for a degree-two integer polynomial reads
\[
 f(x)=c+\sum_i A_i x_i+\sum_i B_i\binom{x_i}{2}
 +\sum_{i<j}C_{ij}x_ix_j.
\]
All coefficients here are integer linear combinations of the values \(f(0),f(e_i),f(2e_i),f(e_i+e_j)\), so each is divisible by \(p^k\). Thus \(g=f/p^k\) is an integer-valued quadratic polynomial with **integer** Newton-basis coefficients. Its reduction modulo \(p\) is nonzero as a function because of the minimality of \(k\). Wherever \(g(x)\not\equiv0\pmod p\), necessarily \(f(x)\not\equiv0\pmod{p^r}\).

**3. Odd primes.** If \(p\) is odd, \(\binom{x_i}{2}\) is an ordinary polynomial of degree two over \(\mathbb F_p\). Therefore \(g\bmod p\) is a nonzero polynomial function represented by a polynomial of total degree at most two. Since \(2<p\), the Schwartz--Zippel bound gives at most \(2p^{n-1}\) zeros among the \(p^n\) arguments. The support fraction of \(f\) is at least \((p-2)/p\) for every \(r\ge1\).

**4. The prime two.** If \(r\ge2\), the residues \(x_i\bmod4\) are uniformly distributed. Set \(u_i=x_i\bmod2\) and \(v_i=\lfloor x_i/2\rfloor\bmod2\); then these are independent uniform binary bits and \(\binom{x_i}{2}\equiv v_i\pmod2\). Consequently \(g\bmod2\) is a nonzero Boolean polynomial
\[
 c'+\sum_i\alpha_i u_i+\sum_i\beta_i v_i
 +\sum_{i<j}\gamma_{ij}u_iu_j
\]
of degree at most two in the \(2n\) bits. Any nonzero Boolean polynomial of degree at most two has support at least one quarter: if it is not constant, one of its coordinate differences is a nonzero affine Boolean function and hence is nonzero on at least half the grid; on each pair where this difference is nonzero, at least one of the original two values is nonzero. When \(n=1\), the displayed expression is affine in the two bits and therefore has support at least one half. If \(r=1\), then \(k=0\); in the Newton expansion of the original integral polynomial each \(B_i\) is even. Reduction modulo two therefore depends only on the \(u_i\) and gives the same bounds. Thus every nonzero local quadratic function has support at least \(1/4\) for \(n\ge2\) and at least \(1/2\) for \(n=1\).

**5. Attainment, including composite moduli.** Choose a prime \(p\mid m\) attaining the minimum defining \(\delta(m,n)\). If \(p\) is odd, take \(f(x)=(m/p)x_1(x_1-1)\pmod m\). It is nonzero precisely when \(x_1\not\equiv0,1\pmod p\), so its nonzero support fraction is \((p-2)/p\). If \(p=2\) and \(n=1\), take \(f(x)=(m/2)x_1\); its support consists exactly of the odd \(x_1\). If \(p=2\) and \(n\ge2\), take \(f(x)=(m/2)x_1x_2\); its support consists exactly of arguments with \(x_1,x_2\) both odd. All witnesses vanish in the other prime-power CRT components. Their support fractions are exactly \(\delta(m,n)\), proving equality.

## Verification

The companion file `verify.py` exhaustively tests the support gap against all coefficient choices in sixteen \((m,n)\) configurations: \((2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2),(5,1),(5,2),(6,1),(6,2),(7,1),(7,2),(8,1),(8,2),(9,1)\). This is \(450011\) total coefficient arrays, including those representing the zero function. It independently checks the explicit sharpness witnesses for each \(2\le m\le100\) and \(n\in\{1,2,3\}\). Run `python3 verify.py` with Python 3 and no third-party dependencies. Exhaustive finite checks are not substitutes for the unrestricted proof.

## Relationship to prior work

Surowka and Regan (2014), Section 8, explicitly conjecture the last-gap formula for quadratic polynomial zero counts over powers of two, with different one-variable and higher-variable exponents, and note that composite moduli beyond prime powers appear less transparent. Their main theorems concern divisibility and symmetry of counts, rather than this sharp largest-gap bound. The classical Schwartz--Zippel estimate and the finite-field Reed--Muller minimum-distance result give the odd-prime reduction, but do not by themselves establish the prime-power, even-modulus, or arbitrary-residue-ring cases. The two-adic Newton-basis reduction and CRT attainability bridge that gap. Pujol--Rifà--Solov'eva (2008) construct quaternary Reed--Muller-like codes through Plotkin constructions and a Gray map; those codes are not automatically the full evaluation family of all integral quadratic polynomials on \((\mathbb Z/4\mathbb Z)^n\).

## Limitations

Only total degree at most two is addressed. The theorem determines the **largest** and **second-largest distinct** zero counts, not the full distribution of all attainable root counts, nor the classification or multiplicities of all extremizing polynomials. Distinct formal coefficient vectors may represent the same polynomial function. The proof is self-contained apart from the standard Schwartz--Zippel bound, whose elementary degree-two case follows by induction on the number of variables. The historical-priority comparison cannot exclude an obscure coding-theoretic reformulation of the exact residue-ring theorem; an independent literature audit is still needed.

## References

1. Robert L. Surowka and Kenneth W. Regan, *Polynomials Modulo Composite Numbers: Ax-Katz type theorems for the structure of their solution sets*, arXiv:1404.4852, submitted 18 April 2014; especially Sections 2 and 8. https://arxiv.org/abs/1404.4852
2. Abhishek Bhowmick and Shachar Lovett, *List decoding Reed-Muller codes over small fields*, arXiv:1407.3433, submitted 13 July 2014; the finite-field minimum-distance framework in Section 1. https://arxiv.org/abs/1407.3433
3. Parikshit Gopalan, *A Fourier-analytic approach to Reed-Muller decoding*, FOCS 2010, DOI:10.1109/FOCS.2010.71; finite-field quadratic case. https://doi.org/10.1109/FOCS.2010.71
4. J. Pujol, J. Rifà and F. I. Solov'eva, *Construction of Z4-linear Reed-Muller codes*, arXiv:0801.3024, submitted 19 January 2008; related but differently constructed quaternary codes. https://arxiv.org/abs/0801.3024
