# Exact residue multiplicities of Fibonacci numbers modulo powers of eleven

## Finding

Let \(F_0=0\), \(F_1=1\), and \(F_{n+2}=F_{n+1}+F_n\). For every \(k\ge1\), the least period of \(F_n\) modulo \(11^k\) is \(P_k=10\cdot11^{k-1}\). Define its exact residue frequency
\[
M_k(y)=\#\{0\le n<P_k:F_n\equiv y\pmod{11^k}\}.
\]
Put \(c(0)=1\), \(c(1)=3\), \(c(2)=2\), \(c(3)=c(8)=c(10)=1\), and \(c(r)=0\) at other classes \(r\pmod {11}\). Choose the unique \(s\in\mathbb Z_{11}\) with \(s^2=5\) and \(s\equiv7\pmod {11}\); set \(\kappa=2/s\in\mathbb Z_{11}\), so \(\kappa\equiv5\pmod{121}\). For \(e\ge1\), define
\[
R_e(z)=\#\{u\pmod{11^e}:u^2\equiv z\pmod{11^e}\},\qquad R_0(0)=1.
\]

**Theorem (complete fibers).** For \(y\pmod{11}\),
\[
M_1(y)=c(y)+\mathbf1_{y=5}.
\]
For every \(k\ge2\) and \(y\pmod{11^k}\),
\[
\boxed{M_k(y)=c(y\bmod11)+11\,\mathbf1_{y\equiv\kappa\pmod{121}}\,R_{k-2}\!\left(\frac{y-\kappa}{242}\bmod11^{k-2}\right).}
\tag{1}
\]
The quotient occurs only when \(121\mid y-\kappa\); it denotes the unique residue after division by \(121\) and multiplication by \(2^{-1}\) modulo \(11^{k-2}\). Thus (1) is independent of the chosen integer representatives of \(y\) and \(\kappa\). For exponent zero the quotient belongs to the trivial ring.

The root counts are explicit: for \(e\ge1\), \(R_e(0)=11^{\lfloor e/2\rfloor}\); for nonzero \(z\pmod{11^e}\), \(R_e(z)=2\cdot11^j\) when \(\nu_{11}(z)=2j<e\) and its unit part is a square modulo \(11\), and zero otherwise.

**Corollary (exact finite support).** For \(k\ge2\), the number of attained residues is
\[
\boxed{6\cdot11^{k-1}+1+5\sum_{j=0}^{\lfloor(k-3)/2\rfloor}11^{k-3-2j},}
\tag{2}
\]
with an empty sum understood as zero. The first six support sizes, at \(k=1,2,3,4,5,6\), are \(7,67,732,8042,88457,973017\). The associated limiting value-set density is the **previously known** \(145/264\), not a new claim. By contrast, (1) determines every index frequency, including the unbounded singular fibers of size \(11^{1+\lfloor(k-2)/2\rfloor}\) at the central residue \(y\equiv\kappa\pmod{11^k}\) (with some off-center fibers larger at odd \(k\)).

## Assumptions and scope

All index counts use the *shortest complete period*, with indices from zero. The prime is fixed to \(11\), and the recurrence has the stated classical initial conditions; no claim is made for other primes or general Lucas parameters. Square-root congruences include zero and are interpreted at exponent zero as specified. The focus is preimage multiplicity, not merely residue-set membership or limiting Haar measure.

## Proof

**1. Exact periods.** Put \(A=\begin{psmallmatrix}1&1\\1&0\end{psmallmatrix}\). Direct recurrence multiplication gives
\[
A^{10}=\begin{pmatrix}89&55\\55&34\end{pmatrix}=I+11C,
\quad C=\begin{pmatrix}8&5\\5&3\end{pmatrix}.
\]
The matrix \(A\pmod{11}\) has exact order \(10\), as checked by its first-return Fibonacci state \((F_{10},F_{11})\equiv(0,1)\pmod{11}\) and the nonreturn at proper divisors \(1,2,5\). Since \(C\not\equiv0\pmod{11}\), binomial lifting at the odd prime \(11\) gives exact order \(11^{k-1}\) to \(A^{10}\) modulo \(11^k\). The scalar Fibonacci period equals the order of \(A\): if the pair \((F_N,F_{N+1})\) first returns to \((0,1)\), then the symmetric Fibonacci matrix formula forces \(A^N=I\). This proves \(P_k\).

**2. Nine regular index classes.** Write \(L_i=F_{i-1}+F_{i+1}\), with \(L_0=2\), for the Lucas numbers. Since \(A^{10}=I+11C\), the convergent matrix logarithm \(\log(A^{10})=11C+11^2D\), for integral \(D\), and its exponential show for all distinct \(t,t'\in\mathbb Z_{11}\) and \(0\le i<10\) that
\[
\frac{F_{i+10t}-F_{i+10t'}}{11(t-t')}\equiv8L_i\pmod{11}.
\tag{3}
\]
The congruence can also be checked from \((F_{i+10}-F_i)/11=8F_i+5F_{i-1}\), with the standard extension to \(i=0\); reduction modulo \(11\) agrees with \(8L_i\). From the ten initial values \(F_i\pmod{11}\), the only index with \(L_i\equiv0\pmod{11}\) is \(i=5\). Thus for \(i\ne5\), the normalized map \(t\mapsto (F_{i+10t}-F_i)/11\) is an exact \(11\)-adic isometry, and therefore a bijection modulo every \(11^e\). Consequently each regular index class contributes exactly one solution \(t\pmod{11^{k-1}}\) to a target in its initial residue disk. Counting those classes gives precisely \(c(y\bmod11)\). The direct initial list is \((0,1,1,2,3,5,8,2,10,1)\pmod{11}\).

**3. Quadratic normal form at the one singular index class.** In \(\mathbb Z_{11}\), set \(\alpha=(1+s)/2\). Its fifth power is \(\alpha^5=(11+5s)/2\equiv1\pmod{11}\). Define \(\ell=\log(\alpha^5)\). Hensel lifting gives \(s\equiv73\pmod{121}\), so \(\alpha^5\equiv67\pmod{121}\), hence \(\ell/11\equiv6\pmod{11}\). For every \(t\in\mathbb Z_{11}\), Binet's formula (the exponent \(5+10t\) is odd on nonnegative integer inputs) yields the analytic interpolation
\[
F_{5+10t}=\kappa\cosh((1+2t)\ell).
\tag{4}
\]
Put \(a=\kappa(\ell/11)^2/4\); then \(a\equiv1\pmod{11}\). Hensel's lemma supplies a unique \(u\in1+11\mathbb Z_{11}\) with \(u^2=a\). With \(\rho(z)=\sinh(z)/z\) (and \(\rho(0)=1\)), let
\[
V(t)=u(1+2t)\rho((1+2t)\ell/2).
\]
The hyperbolic identity \(\cosh z-1=2\sinh^2(z/2)\) gives the **exact** equality
\[
F_{5+10t}=\kappa+242V(t)^2.
\tag{5}
\]
Because \(\ell\in11\mathbb Z_{11}\), the power series of \(\rho((1+2t)\ell/2)-1\) has all coefficients divisible by \(121\). In particular its difference at \(t,t'\) is divisible by \(121(t-t')\). Therefore
\[
\frac{V(t)-V(t')}{t-t'}\equiv2u\not\equiv0\pmod{11},
\]
so \(V\) is an exact isometry and bijects \(\mathbb Z/11^e\mathbb Z\) with itself at each exponent \(e\ge0\). This proves (5) converts the singular residue equation at exponent \(k\ge2\) to \(V(t)^2\equiv(y-\kappa)/242\pmod{11^{k-2}}\). Each root modulo \(11^{k-2}\) has exactly \(11\) lifts in the index parameter \(t\pmod{11^{k-1}}\). This contributes \(11R_{k-2}\) and proves (1). At \(k=1\), the singular branch contributes exactly once to residue \(5\), proving the separate boundary formula.

**4. Root counts and support.** A nonzero square modulo \(11^e\) has even valuation \(2j<e\), with a nonzero quadratic-residue unit modulo \(11\). Hensel's lemma gives exactly two roots for that unit at exponent \(e-2j\), each with \(11^j\) lifts. Zero has \(11^{\lfloor e/2\rfloor}\) roots. The distinct square values number \(1+5\sum_{j=0}^{\lfloor(e-1)/2\rfloor}11^{e-2j-1}\). In (1) the six regular disks are disjoint from the singular square disk, proving (2). Their limiting density is \(6/11+1/264=145/264\), agreeing with the earlier image-set result.

## Verification

The supplied standalone Python program uses exact integer Fibonacci iteration to enumerate all indices of each least period for exponents \(1\le k\le6\), comparing *every* residue multiplicity with formula (1) and verifying that no prime-divisor reduction of the proposed period closes the Fibonacci state. It independently enumerates square roots for exponents \(1,2,3\). All checks pass, including \(1{,}610{,}510\) indices and \(1{,}771{,}561\) residue classes at exponent six. These finite checks corroborate but do not prove the all-level statements, which follow from steps 1–4.

Run: `python check_fib11.py` using a standard Python 3 interpreter.

## Relationship to prior work

Rowland and Yassawi's prime-eleven analysis proves the regular **image disks**, the singular **attained-value tree**, and the limiting **value-set density** \(145/264\); these results are explicitly credited. Bragman and Rowland extend this density framework to other primes. Neither inspected theorem gives the number of index preimages of **each** target modulo \(11^k\) in its exact least period. In particular, equal attained-value sets do not determine the regular frequencies \(1,2,3\), the precise singular square-root multiplicities, or their finite-exponent normalization. The present formula is a quantitative pushforward law, not a new proof or rebranding of the existing density.

Carlip and Somer (2007) develop bounds on frequency distributions under distinct regularity and multiplier assumptions; their Theorem 6.1 does not directly apply to the classical Fibonacci sequence, which is its own generalized Fibonacci sequence and has Wall exponent one at eleven. A related 1999 chapter on frequency **bounds** could not be read in full; the possibility that a general result there specializes to the present exact formula remains an explicit priority risk. Bundschuh and Bundschuh classify exact frequencies at the different prime three. Published separate work on classical Lucas **numbers modulo seven** has an analogous square-fiber form, but concerns a different sequence and prime, and does not imply (1).

## Limitations

The classification applies only to classical Fibonacci numbers and prime powers of eleven. No independent external mathematical audit has been performed. The exact formulas are newly established here from disclosed identities and do not claim historical originality for the underlying eleven-adic support tree, image density, recurrence period, or standard square-root counting. Unread full text of the 1999 Carlip–Somer chapter leaves some originality uncertainty.

## References

1. Nicholas Bragman and Eric Rowland, *Limiting density of the Fibonacci sequence modulo powers of \(p\)*, arXiv:2202.00704, first public posting 2022-02-01. https://arxiv.org/abs/2202.00704.
2. Eric Rowland and Reem Yassawi, *\(p\)-adic asymptotic properties of constant-recursive sequences*, arXiv:1602.00176 (2016), especially Lemmas 17–19 and Theorem 20. https://ericrowland.github.io/papers/p-adic_asymptotic_properties_of_constant-recursive_sequences.pdf.
3. Walter Carlip and Lawrence Somer, *Bounds for frequencies of residues of second-order recurrences modulo prime powers*, Mathematica Bohemica 132 (2007), 137–175, especially Theorem 6.1. https://dml.cz/bitstream/handle/10338.dmlcz/134189/MathBohem_132-2007-2_3.pdf.
4. Walter Carlip and Lawrence Somer, *Bounds for frequencies of residues of regular second-order recurrences modulo prime powers*, Number Theory in Progress 2 (1999), 691–719. DOI:10.1515/9783110285581.691. Full text not verified.
5. Ralf Bundschuh and Peter Bundschuh, *Distribution of Fibonacci and Lucas numbers modulo \(3^k\)*, Fibonacci Quarterly 49 (2011), 201–210. https://fq.math.ca/Papers1/49-3/Bundschuh2.pdf.
6. *Exact seven-adic Lucas residue fibers and the \(41/56\) range measure*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-seven-adic-lucas-residue-fibers-and-the-41-56-range-measur--be34cdadeedf.
