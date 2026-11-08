# Exact square–triangular residue overlap and nonsquare excess at every modulus

## Finding
For each integer \(n\ge1\), let \(\mathcal S_n=\{x^2\bmod n:x\in\mathbb Z\}\) and \(\mathcal T_n=\{y(y+1)/2\bmod n:y\in\mathbb Z\}\). Write \(C(n)=|\mathcal S_n\cap\mathcal T_n|\), with \(C(1)=1\). The function \(C\) is multiplicative. Its prime-power factors have the following exact forms.

For every odd prime \(p\) and \(k\ge1\), put \(\varepsilon_p=(2/p)\) and \(\eta_p=(-2/p)\), where the parentheses denote the Legendre symbol, and set
\[
A_{p,k}=1+\frac{p-1}{2}\sum_{j=1}^{\lfloor(k-1)/2\rfloor}p^{k-2j-1}.
\]
(The empty sum is zero.) Then
\[
\boxed{C(p^k)=\frac{p^{k-1}(p-3-\varepsilon_p-\eta_p)}4+\frac{3+\eta_p}{2}A_{p,k}.}
\]
For the dyadic prime powers,
\[
\boxed{C(2^k)=\begin{cases}(2^{k-1}+5)/3,&k\ge1\text{ odd},\\(2^{k-1}+4)/3,&k\ge2\text{ even}.\end{cases}}
\]
In particular, every residue modulo \(2^k\) is triangular, although not every one is square.

For odd primes the formula specializes to
\[
\boxed{C(p)=\begin{cases}(p+3)/4,&p\equiv1,5\pmod8,\\(p+5)/4,&p\equiv3\pmod8,\\(p+1)/4,&p\equiv7\pmod8.\end{cases}}
\]
Define the *nonsquare excess* for \(n\ge3\) by
\[
R(n)=\frac{(|\mathcal T_n|-C(n))/C(n)}{(n-|\mathcal S_n|)/|\mathcal S_n|}.
\]
All denominators here are nonzero. The preceding formula together with the standard square-image count \(|\mathcal S_n|\) and the identity \(|\mathcal T_n|=2^{v_2(n)}\prod_{p^k\parallel n,\ p\text{ odd}}|\mathcal S_{p^k}|\) determines \(R(n)\) for every \(n\ge3\). At primes it gives the exact three-branch law
\[
\boxed{R(p)=\begin{cases}(p+1)/(p+3),&p\equiv1,5\pmod8,\\(p+1)(p-3)/((p-1)(p+5)),&p\equiv3\pmod8,\\(p+1)/(p-1),&p\equiv7\pmod8.\end{cases}}
\]
Thus the prime-class curves are rational identities, not merely numerical fits.

## Assumptions and scope
The images include the zero residue and are sets of **distinct residue classes**, not representation counts and not reductions of the integer square-triangular Pell sequence. The numerator \(y(y+1)\) is always even in the integers before reducing modulo \(n\). Prime powers have \(k\ge1\); the modulus \(n=1\) has its single residue class. The excess statistic is undefined at \(n=1,2\) because every residue is a square there. All formulas are unconditional.

## Proof
**1. Reduction to prime powers.** For coprime \(u,v\), a residue is a square (respectively triangular) modulo \(uv\) exactly when its reductions are so modulo each factor. Indeed, choose independent square roots (respectively triangular parameters) and combine them using the Chinese remainder theorem. Consequently \(C(uv)=C(u)C(v)\).

**2. Character count at odd primes.** Fix an odd prime \(p\). A residue \(r\) is triangular modulo \(p^k\) precisely when \(8r+1\) is a square modulo \(p^k\), since \((2y+1)^2=8\,y(y+1)/2+1\) and \(2\) is invertible. Let \(\chi\) be the quadratic character modulo \(p\), extended by \(\chi(0)=0\). For \(r\not\equiv0,-1/8\pmod p\), simultaneous representability is equivalent to \(\chi(r)=\chi(8r+1)=1\). Expanding the product of character indicators gives the number of such generic residue classes:
\[
G_p=\frac14\sum_{r\in\mathbb F_p}\bigl(1+\chi(r)\bigr)\bigl(1+\chi(8r+1)\bigr)-\frac12-\frac{1+\chi(-1/8)}4.
\]
The two linear character sums vanish, and \(\sum_r\chi(r)\chi(8r+1)=-\chi(8)=-\varepsilon_p\), as follows by completing the square in the nonsingular quadratic polynomial \(8r^2+r\). Also \(\chi(-1/8)=\eta_p\). Therefore \(G_p=(p-3-\varepsilon_p-\eta_p)/4\). Every generic successful residue has exactly \(p^{k-1}\) successful lifts, because both square classes are units and Hensel lifting preserves unit squareness.

**3. The two exceptional branches.** Over \(r\equiv0\pmod p\), \(8r+1\equiv1\pmod p\), hence every such \(r\) automatically has triangular representability. The number of square residues \(r\equiv0\pmod p\) modulo \(p^k\) is
\[
A_{p,k}=1+\sum_{\substack{j\ge1\\2j<k}}\frac{p-1}{2}p^{k-2j-1},
\]
by classifying the even valuations \(v_p(r)=2j\) and the zero residue. For the other exceptional branch \(8r+1\equiv0\pmod p\), the unit \(r\) is square if and only if \(\eta_p=1\); if so, the affine bijection \(r\mapsto8r+1\) shows that exactly \(A_{p,k}\) such classes are triangular. The branches are disjoint. Adding the generic lifts and \((1+(1+\eta_p)/2)A_{p,k}\) gives the displayed odd-prime-power formula.

**4. Powers of two.** For \(m=2^k\), the integers \(T(j)=j(j+1)/2\), \(0\le j<m\), give distinct residues modulo \(m\). If \(0\le a<b<m\), then
\[
2(T(b)-T(a))=(b-a)(a+b+1),
\]
and the two factors on the right have opposite parity. If \(b-a\) is even, its \(2\)-adic valuation is below \(k\); if it is odd, the even factor \(a+b+1\) is below \(2m\), so its valuation is at most \(k\). In either case the product has valuation at most \(k\), and \(T(b)-T(a)\) has valuation strictly below \(k\). Thus the triangular map covers all residues modulo \(2^k\), so \(C(2^k)=|\mathcal S_{2^k}|\). An odd square modulo \(2^t\) has \(1\), \(1\), and \(2^{t-3}\) possible unit values when \(t=1\), \(t=2\), and \(t\ge3\), respectively. Decomposing even valuations of squares yields the recurrence \(C(2^k)=C(2^{k-2})+2^{k-3}\) for \(k\ge3\), with \(C(2)=C(4)=2\). Solving it gives the stated parity formulas.

**5. Excess.** For odd \(p^k\), \(r\mapsto8r+1\) is a bijection, hence \(|\mathcal T_{p^k}|=|\mathcal S_{p^k}|\); for \(2^k\), every residue is triangular. The Chinese remainder theorem determines \(|\mathcal T_n|\) and \(|\mathcal S_n|\) multiplicatively. At an odd prime, both images have size \((p+1)/2\). Inserting the three cases of \(C(p)\) into the definition of \(R(p)\) and simplifying proves the rational formulas. The denominator \(C(n)\) is positive since the zero class belongs to both images, and \(n-|\mathcal S_n|>0\) for \(n\ge3\).

## Verification
The complete standalone program `verify.py` uses exact integer arithmetic and tests the theorem for all \(1999\) moduli \(2\le n\le2000\), checks the prime nonsquare-excess identity for \(34\) odd primes below \(151\), and separately tests \(34\) prime-power cases up to \(30000\). All tests passed. This is finite corroboration; the proof above supplies the unrestricted result. Run `python3 verify.py` using only Python's standard library.

## Relationship to prior work
Wright (2013) studies quadratic-residue patterns using multiplicative characters and supplies archival context for quadratic-character correlation methods; its objects are prime-density questions about prescribed progressions, not the simultaneous square/triangular image at each modulus. Wang and Sun (2015) relate representations by sums of squares and triangular numbers but do not establish this image-intersection count. Ulness (2022, especially Theorem 5 and Section 7.2) identifies triangular residues by the quadratic test and defines the same nonsquare-excess statistic. Its Section 7.2 reports numerical prime-class curves and empirical rational fits, whereas the theorem here determines the exact rational prime classes and the all-modulus prime-power product. The classical count of quadratic residues modulo prime powers is an input, not claimed as new.

## Limitations
These formulas count residue classes, not pairs of representations and not global integer square-triangular values. They do not resolve the numerical claim about uniform bounds on the excess statistic for all growing moduli; the formula could be used to study that problem separately. Historical originality remains provisional, particularly because a mathematically equivalent character-correlation formula could have appeared under other terminology. The 2022 publisher HTML returned access throttling; the relevant Theorem 5 and Section 7.2 were examined in indexed full-text passages, but exhaustive inspection of that article was not possible.

## References
1. Steve Wright, *On the density of primes with a set of quadratic residues or non-residues in given arithmetic progression*, arXiv:1304.2191, first posted April 8, 2013; https://arxiv.org/abs/1304.2191.
2. Min Wang and Zhi-Hong Sun, *On the number of representations of n as a linear combination of four triangular numbers II*, arXiv:1511.00478, first posted November 2, 2015; https://arxiv.org/abs/1511.00478.
3. Darin J. Ulness, *Structure of Triangular Numbers Modulo m*, AppliedMath 2 (2022), 326–358, DOI:10.3390/appliedmath2030020, especially Theorem 5 and Section 7.2; https://www.mdpi.com/2673-9909/2/3/20.
