# Exact candidate-pole index fibres for Schinzel's reciprocal sextic

## Finding

Let \(f(X)=X^6-2X^4-6X^3-2X^2+1\) and let \(\alpha>1\) be its unique largest positive root. Number its conjugates as in Serrano Holgado (2023): \(\alpha_1=\alpha\), \(\alpha_2=\alpha^{-1}\), \(\alpha_3=u\) with \(\Im u>0\) and \(|u|>1\), \(\alpha_4=\bar u\), \(\alpha_5=\bar u^{-1}\), and \(\alpha_6=u^{-1}\). Consider the candidate-pole indexation map \(\iota:\mathbb N_0^5\to\Omega_0\) associated with this Perron number, where the target is one horizontal fundamental strip of height \(2\pi/\log\alpha\).

For an index \(\mathbf k=(k_2,k_3,k_4,k_5,k_6)\), set
\[
A=2k_2+k_4+k_5+2k_6,\qquad B=2k_2+k_3+2k_5+k_6.
\]
Its image is the unique fundamental-strip representative of
\[
-\frac{A\log u+B\log\bar u}{\log\alpha}
\pmod{2\pi i/\log\alpha}.
\]
Two indices have the same image **if and only if** their ordered pairs \((A,B)\) coincide. Every nonnegative pair occurs. Thus the sites with real part \(-h/2\) consist of exactly \(h+1\) different candidate sites, one for each \((A,B)\) with \(A+B=h\).

Write \(N(A,B)\) for the number of indices reaching that site. The **entire exact fibre distribution** is
\[
\boxed{\sum_{A,B\ge0}N(A,B)x^Ay^B
=\frac{1}{(1-x^2y^2)(1-y)(1-x)(1-xy^2)(1-x^2y)}.}
\]
The total number \(S_h\) of indices whose candidate site has real part \(-h/2\), counting repetitions, therefore satisfies
\[
\boxed{\sum_{h\ge0}S_ht^h=\frac{1}{(1-t)^2(1-t^3)^2(1-t^4)},\qquad
S_h=\frac{h^4}{864}+O(h^3).}
\]
In particular, the average fibre over the \(h+1\) distinct sites on that line is asymptotic to \(h^3/864\); the finite fibres are not uniformly bounded.

## Assumptions and scope

The source indexation map is defined for a Perron number through the candidate points in the meromorphic expansion of a recurrence zeta function. Here the *minimal polynomial and its ordered conjugates* determine that indexation; the result is independent of the coefficients of any particular recurrence with this minimal polynomial. The fundamental strip is \(\Omega_0=\{s:-\pi/\log\alpha<\Im s\le\pi/\log\alpha\}\). Equality is of representative sites in this strip, **not** equality of distinct analytic residues.

The term *candidate site* is essential: a pole of an individual expansion summand need not remain a pole of the final zeta function after cancellations, and some coefficients of the recurrence may make summands vanish. No conclusion about actual analytic poles or their orders is claimed.

## Proof

**1. Algebraic conjugates and a rank-two description.** The polynomial is reciprocal and admits the identity
\[
f(X)=(X^3-1)^2-2(X^2+X)^2
=(X^3+\sqrt2(X^2+X)-1)(X^3-\sqrt2(X^2+X)-1).
\]
The first cubic has roots \(\alpha_2,u,\bar u\); hence \(\alpha_2u\bar u=1\), i.e. \(u\bar u=\alpha\). Reciprocity supplies the stated inverse pairs. Serrano Holgado's Section 6 establishes the real-root ordering and the Perron property. For independent algebraic verification, the supplied checker proves irreducibility over \(\mathbb F_{11}\) using \(X^{11^6}\equiv X\pmod f\) and \(\gcd(f,X^{11^2}-X)=\gcd(f,X^{11^3}-X)=1\); consequently \(f\) is irreducible over \(\mathbb Q\).

For the source indexation map (formula (2.3)), the multiplicative quantity specifying the candidate site modulo the imaginary period is \(\prod_{i=2}^6(\alpha_i/\alpha)^{k_i}\). Express each factor using \(u\bar u=\alpha\):
\[
\begin{array}{c|ccccc}
i&2&3&4&5&6\\\hline
\alpha_i/\alpha&u^{-2}\bar u^{-2}&\bar u^{-1}&u^{-1}&u^{-1}\bar u^{-2}&u^{-2}\bar u^{-1}.
\end{array}
\]
This gives precisely the linear forms \(A,B\). Since \(|u|^2=\alpha\), its real part is \(-(A+B)/2\).

**2. Distinctness of different exponent pairs.** The ratio \(u/\bar u\) is not a root of unity. To see this, put \(K=\mathbb Q(\sqrt2)\). Because \(\alpha_2\) has degree six over \(\mathbb Q\) and satisfies the first cubic, \(\sqrt2=(1-\alpha_2^3)/(\alpha_2^2+\alpha_2)\) belongs to \(\mathbb Q(\alpha_2)\). Thus that cubic is irreducible of degree three over \(K\). There is a \(K\)-embedding of its splitting field into an algebraic closure sending \(u\) to \(\alpha_2\); it sends \(\bar u\) to one of the other two cubic roots. If \(u/\bar u\) were a root of unity, the image would still have complex absolute value one. Yet \(|\alpha_2|=\alpha^{-1}\) while \(|u|=|\bar u|=\alpha^{1/2}\), a contradiction.

If \(u^{-A}\bar u^{-B}=u^{-A'}\bar u^{-B'}\), absolute values give \(A+B=A'+B'\). Dividing then yields \((u/\bar u)^{A-A'}=1\), so \(A=A'\) and \(B=B'\). Conversely equal pairs clearly give equal sites. All nonnegative pairs are attained by choosing \(k_4=A\), \(k_3=B\), and the remaining indices zero.

**3. Fibre and diagonal enumerators.** Every index independently contributes one of the five nonnegative exponent vectors
\[
(2,2),\ (0,1),\ (1,0),\ (1,2),\ (2,1).
\]
Their multivariate geometric series give the displayed rational generating function coefficient by coefficient. Because \(\Re(s)=-(A+B)/2\), setting \(x=y=t\) counts all indices along one line. The five weights are \(4,1,1,3,3\), giving the diagonal generating function. Its sole order-five pole on the unit circle is at \(t=1\), with leading part \(1/[36(1-t)^5]\); all other unit-circle poles have lower order. Thus \(S_h=h^4/(36\cdot4!)+O(h^3)=h^4/864+O(h^3)\). Dividing by \(h+1\) proves the average-fibre asymptotic.

## Verification

Run `python3 check.py` with a standard Python 3 interpreter. The standalone checker verifies an exact finite-field irreducibility certificate, compares the bivariate product with a separate bounded five-index enumeration through total weight \(45\), and checks diagonal totals by a third independent summation. It prints `PASS` for the checks and small-line tables. These finite checks are not substitutes for the all-level proof above.

## Relationship to prior work

Serrano Holgado's 2023 study defines the indexation map and proves general finiteness and the criterion for injectivity (Proposition 3.1 and Theorem 4.4). Its Section 6 presents the same Schinzel sextic and a rank-four module of relations, but does not state the exact sextic fibre generating function or the line-by-line index-count asymptotic above. It also derives a different explicit fibre formula for quartic Salem numbers. The present calculation builds on those results while quantifying all sextic collisions rather than merely asserting their existence or finite size.

The earlier 2023 paper by Serrano Holgado and Navas Vicente establishes the meromorphic continuation and the candidate-point framework for general recurrence sequences, without this specific coefficient-count distribution.

## Limitations

The indexation counts potential singular sites for the expansion, not necessarily true poles of any chosen recurrence zeta function. No claim of independent review or exhaustive coverage of unpublished literature is made. The originality comparison is to the inspected primary literature and relevant searches; an equivalent unindexed enumeration may exist. The result is specialized to the named sextic and does not assert an analogous formula for all reciprocal Perron polynomials.

## References

1. Á. Serrano Holgado, *A connection between the poles of the zeta function of a recurrence sequence and the module of relations of its roots*, arXiv:2311.08632, initially public 15 November 2023, https://arxiv.org/html/2311.08632v1. Especially Sections 2, 3, 4, and 6.
2. Á. Serrano Holgado and L. M. Navas Vicente, *The Zeta Function of a Recurrence Sequence of Arbitrary Degree*, Mediterranean Journal of Mathematics 20 (2023), article 224, https://doi.org/10.1007/s00009-023-02427-w.
3. M. Drmota and M. Skałba, *Relations between polynomial roots*, Acta Arithmetica 71 (1995), 65–77, https://doi.org/10.4064/aa-71-1-65-77 (origin of the Schinzel example, as credited in Reference 1).
