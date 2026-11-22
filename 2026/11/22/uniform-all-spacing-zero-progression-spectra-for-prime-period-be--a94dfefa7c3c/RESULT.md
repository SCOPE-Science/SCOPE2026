# Uniform all-spacing zero progression spectra for prime-period Bell numbers

## Finding
Let \(B_n\) be the Bell numbers, initialized by \(B_0=1\). For a prime \(p\), put
\[
N_p=\frac{p^p-1}{p-1}=1+p+\cdots+p^{p-1}.
\]
Assume that the least index period of \((B_n\bmod p)\) equals \(N_p\). For every nonzero spacing \(h\in\mathbb Z/N_p\mathbb Z\) and length \(1\le\ell\le p\), let \(C_{p,\ell}(h)\) count starting indices \(n\in\mathbb Z/N_p\mathbb Z\) such that
\[
B_{n+jh}\equiv0\pmod p\qquad(0\le j<\ell).
\]
Then the *entire progression spectrum is independent of the nonzero spacing*:
\[
\boxed{C_{p,\ell}(h)=\frac{p^{p-\ell}-1}{p-1}.}
\]
In particular, every nonzero spacing has exactly one start of an \((p-1)\)-term zero progression, but none has a \(p\)-term zero progression. For larger lengths there are likewise none. The formula includes spacings that are not units modulo \(N_p\). For \(p=5\), where \(N_p=781\), the counts at lengths one through five are \(156,31,6,1,0\) for **each** of the \(780\) nonzero spacings. The familiar consecutive-zero case \(h=1\) is previously known and is not claimed as new.

## Assumptions and scope
Here a progression is indexed cyclically modulo the least period; its step must be nonzero modulo \(N_p\). Bell numbers count set partitions, and satisfy Touchard's congruence
\[
B_{n+p}\equiv B_{n+1}+B_n\pmod p\qquad(n\ge0).
\]
The **full-period hypothesis is indispensable** in the stated derivation and is not asserted for every prime. It is established for many specific primes by Montgomery, Nahm and Wagstaff, including all primes below \(126\). Hence the displayed result is unconditional for \(p=2,3,5,7\) and the other verified primes, but is conditional at a general prime for which the full-period question remains unsettled. No unverified period conjecture is used.

## Proof
**1. Irreducible Artin–Schreier model.** Consider \(f(X)=X^p-X-1\) over \(\mathbb F_p\). Choose a root \(\rho\) in an algebraic closure. The equation \(\rho^p=\rho+1\) shows that the Frobenius conjugates are \(\rho,\rho+1,\ldots,\rho+p-1\), all distinct. The Frobenius orbit has length exactly \(p\), so \(f\) is irreducible and \(K=\mathbb F_p(\rho)=\mathbb F_{p^p}\). Consequently \(1,\rho,\ldots,\rho^{p-1}\) is an \(\mathbb F_p\)-basis of \(K\).

**2. Trace realization.** Write \(\operatorname{Tr}:K\to\mathbb F_p\) for the field trace. Its bilinear pairing \((x,y)\mapsto\operatorname{Tr}(xy)\) is nondegenerate, because \(K/\mathbb F_p\) is separable. Therefore there is a unique \(c\in K\) satisfying
\[
\operatorname{Tr}(c\rho^j)=B_j\bmod p\qquad(0\le j<p).
\]
The right-hand sequence \(\operatorname{Tr}(c\rho^n)\) satisfies the Touchard recurrence (since \(\rho^p=\rho+1\)); equality of the first \(p\) terms gives
\[
B_n\equiv\operatorname{Tr}(c\rho^n)\pmod p\quad(n\ge0).
\]
Also \(c\ne0\), because \(B_0=1\). For any positive integer \(d\), periodicity with shift \(d\) is equivalent to
\[
\operatorname{Tr}(c(\rho^d-1)\rho^n)=0\quad(0\le n<p),
\]
which by the basis and nondegeneracy is equivalent to \(\rho^d=1\). Hence the assumed least Bell period \(N_p\) is the multiplicative order of \(\rho\). Note also that the product of the conjugates is \(\rho^p-\rho=1\), so \(\rho\) has norm one, as expected.

**3. Projective representatives.** Since \(N_p\equiv1\pmod{p-1}\), we have \(\gcd(N_p,p-1)=1\). The group \(H=\langle\rho\rangle\subset K^*\), of order \(N_p\), therefore meets \(\mathbb F_p^*\) only in \(1\). Moreover \(|H|(p-1)=p^p-1=|K^*|\), so each one-dimensional \(\mathbb F_p\)-subspace of \(K\) contains exactly one element of \(H\). Multiplication by the fixed \(c\ne0\) preserves this property; the \(N_p\) elements \(c\rho^n\) represent all projective points of \(K\) exactly once.

**4. Independence at every nonzero spacing.** Fix \(h\not\equiv0\pmod{N_p}\) and put \(\beta=\rho^h\). Then \(\beta\notin\mathbb F_p\), because \(H\cap\mathbb F_p^*=\{1\}\). As \([K:\mathbb F_p]=p\) is prime, \(\beta\) has minimal polynomial of degree \(p\), and therefore \(1,\beta,\ldots,\beta^{\ell-1}\) are linearly independent for each \(\ell\le p\). It follows from nondegeneracy of the trace pairing that the \(\ell\) functionals
\[
y\longmapsto\operatorname{Tr}(y\beta^j),\qquad0\le j<\ell,
\]
are independent. Their common kernel is an \(\mathbb F_p\)-linear subspace of dimension exactly \(p-\ell\).

**5. Count.** The simultaneous congruences for a starting index \(n\) say precisely that \(y=c\rho^n\) lies in that common kernel. The kernel contains \(p^{p-\ell}-1\) nonzero vectors and hence \((p^{p-\ell}-1)/(p-1)\) projective points. By Step 3 each such point corresponds to exactly one starting residue \(n\). This proves the formula. At \(\ell=p\) the kernel is zero, proving the sharp exclusion, and at \(\ell=p-1\) it is one-dimensional, proving unique existence.

## Verification
The standalone file `checker.py` evaluates Bell residues by both the integer binomial recurrence and Touchard's congruence, verifies the cycle, and checks the claimed counts **for every nonzero spacing** at \(p=2,3,5\): respectively \(2\), \(12\), and \(780\) spacings. These yield \(4+36+3900=3940\) exact progression-count comparisons. It additionally verifies the known consecutive quadruple start \(587\) at \(p=5\). Run with `python checker.py`. This finite computation checks examples and implementations; Steps 1–5, not enumeration, prove the general statement.

## Relationship to prior work
Layman's 1985 work identified the unique maximal **consecutive** block of \(p-1\) Bell zeros modulo a prime; OEIS A175923 records its first starting indices, including \(587\) for \(p=5\). No novelty is claimed for \(h=1\). Montgomery–Nahm–Wagstaff (2010) study least Bell periods and verify the full period for many primes. Gallardo–Rahavandrainy (2014) give a finite-field trace description of Bell residues and describe the consecutive-zero phenomenon. The present result establishes **all nonzero spacings simultaneously**, each entire length spectrum, and the uniform nonunit-spacing case. The two-site count is also consistent with the classical projective Singer difference-set construction; two-site incidence alone does not determine higher-site intersections. The field-theoretic trace and independence machinery is classical and is not presented as new. Existing general studies of finite-field recurring sequences may contain equivalent all-spacing formulations, so historical-priority assessment remains qualified.

## Limitations
The full-period assumption is not proved at all primes. The theorem concerns zero residues, not a full distribution of nonzero Bell residues, and cyclic progression starts rather than the first occurrence of an integer progression. The related Layman (1985) and Shparlinski (1991) primary full texts could not be inspected; a broader historical theorem may subsume the evaluated spectrum. No claim of independent verification or proof certification is made.

## References
- P. Montgomery, S. Nahm, S. S. Wagstaff Jr., *The period of the Bell numbers modulo a prime*, Mathematics of Computation 79 (2010), 1793–1800. DOI: https://doi.org/10.1090/S0025-5718-10-02340-9 . Public 2010 source record: https://www.cerias.purdue.edu/apps/reports_and_papers/view/4336 .
- L. H. Gallardo and O. Rahavandrainy, *Bell Numbers Modulo a Prime Number, Traces and Trinomials*, Electronic Journal of Combinatorics 21(4) (2014), P4.49. https://doi.org/10.37236/3532 .
- M. Car, L. H. Gallardo, O. Rahavandrainy and L. N. Vaserstein, *About the period of Bell numbers modulo a prime*, Bull. Korean Math. Soc. 45 (2008), 143–155. https://doi.org/10.4134/BKMS.2008.45.1.143 .
- J. W. Layman, *Maximum Zero Strings of Bell Numbers Modulo Primes*, Journal of Combinatorial Theory A 40 (1985), 161–168. https://doi.org/10.1016/0097-3165(85)90055-X .
- OEIS A175923, Bell zero-run first occurrence indices, https://oeis.org/A175923 .
- R. J. McEliece, *Linear Recurring Sequences Over Finite Fields*, PhD thesis (1967), https://thesis.caltech.edu/3856/ .
