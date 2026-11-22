# A sharp safe-prime threshold for five primitive roots in every arithmetic step

## Finding

**Theorem.** Let \(p=2q+1\) be a prime for which \(q\) is also prime (a *safe prime*). The following property holds if and only if \(p\ge107\):

\[
\forall d\in\mathbb F_p^\times\quad\exists a\in\mathbb F_p\quad
\operatorname{ord}_p(a+jd)=p-1\quad(0\le j\le4).
\]

In particular, every nonzero common difference occurs in a five-term arithmetic progression consisting entirely of primitive roots. The largest exceptional safe prime is \(p=83\): the difference \(d=3\) fails there, even though some other differences succeed.

## Assumptions and scope

A primitive root is an element of multiplicative order \(p-1\) in \(\mathbb F_p^\times\). All five terms and additions are interpreted modulo \(p\); the step \(d\) is nonzero. For the character-sum argument assume \(p\ge7\), so that \(q\) is odd and the five shifts \(0,1,2,3,4\) are distinct. The prime \(p=5\) is dealt with by the finite certificate. No assumption is made about the infinitude of safe primes.

## Proof

**1. Primitive roots at a safe prime.** The cyclic group \(\mathbb F_p^\times\) has order \(2q\). Let \(\chi\) be its quadratic character, with \(\chi(0)=0\). For odd \(q\), an element with \(\chi(x)=-1\) has order either \(2\) or \(2q\); the unique element of order \(2\) is \(-1\). Thus
\[
\operatorname{ord}_p(x)=p-1
\quad\Longleftrightarrow\quad
\chi(x)=-1\ \text{and}\ x\ne-1.
\tag{1}
\]

Fix \(d\in\mathbb F_p^\times\) and write \(a=dt\). The five desired terms are \(d(t+j)\). Let \(\varepsilon=-\chi(d)\). Their being quadratic nonresidues is equivalent to \(\chi(t+j)=\varepsilon\) for each \(j=0,\ldots,4\). At most five values of \(t\) have a forbidden term \(d(t+j)=-1\), namely \(t=-d^{-1}-j\). It will suffice to prove that each of the two fixed-sign sets
\[
B_\varepsilon=\{t\in\mathbb F_p:\chi(t+j)=\varepsilon\text{ for all }0\le j\le4\}
\]
has more than five elements.

**2. A uniform five-sign character bound.** Define the nonnegative weighted count
\[
M_\varepsilon=\frac1{32}\sum_{t\in\mathbb F_p}\prod_{j=0}^4(1+\varepsilon\chi(t+j)).
\]
For \(t\notin\{0,-1,-2,-3,-4\}\), the summand is exactly the indicator of \(B_\varepsilon\). At each of the five excluded roots the summand is between \(0\) and \(1/2\). Consequently
\[
\# B_\varepsilon\ge M_\varepsilon-\frac52.
\tag{2}
\]

Expand the product. The empty subset contributes \(p\), and the five singleton sums vanish. For each pair of distinct indices \(i,j\), the standard quadratic identity gives
\[
\sum_{t\in\mathbb F_p}\chi((t+i)(t+j))=-1.
\]
There are ten such pairs, so their aggregate contribution is \(-10\). For a subset \(I\) of size \(r=3,4,5\), the polynomial \(\prod_{j\in I}(T+j)\) has \(r\) distinct simple roots and is not a square. The quadratic Weil bound therefore yields
\[
\left|\sum_{t\in\mathbb F_p}\chi\!\left(\prod_{j\in I}(t+j)\right)\right|\le(r-1)\sqrt p.
\]
The ten triples, five quadruples and one quintuple contribute in total at worst \((10\cdot2+5\cdot3+1\cdot4)\sqrt p=39\sqrt p\). Thus, for either sign,
\[
M_\varepsilon\ge\frac{p-10-39\sqrt p}{32},\qquad
\#B_\varepsilon\ge\frac{p-90-39\sqrt p}{32}.
\tag{3}
\]

If \(p\ge2000\), then \(p-250>39\sqrt p\). Indeed \(2000-250=1750>39\sqrt{2000}\) because \(1750^2=3062500>3042000=39^2\cdot2000\), and \(t-250-39\sqrt t\) is strictly increasing on \([2000,\infty)\). Equation (3) therefore implies \(\#B_\varepsilon>5\) for both signs. Discarding the at most five values of \(t\) that give a term \(-1\), there is a remaining \(t\), and (1) proves the assertion for every safe prime \(p\ge2000\) and every nonzero step.

**3. Exhaustive lower range and sharpness.** The attached standalone `verify.py` checks every integer \(5\le p<2000\). It tests primality by trial division up to the exact integer square root, recognizes safe primes by checking both \(p\) and \((p-1)/2\), and determines primitive roots \(x\) using the equivalence
\[
x\text{ has order }2q\quad\Longleftrightarrow\quad
x^2\not\equiv1\pmod p\text{ and }x^q\not\equiv1\pmod p.
\tag{4}
\]
It exhausts all \(d=1,\ldots,p-1\) and all \(a=1,\ldots,p-1\), testing all five terms. Of the 37 safe primes in this finite range, exactly the seven \(5,7,11,23,47,59,83\) have at least one failing difference; the remaining 30 (starting at \(107\)) have none. The complete failing-difference lists at the two largest exceptions are
\[
\begin{aligned}
p=59 &: \{2,19,24,25,26,33,34,35,40,57\},\\
p=83 &: \{3,20,40,43,63,80\}.
\end{aligned}
\]
To see the last obstruction independently of the program, at \(p=83\) the indices starting five consecutive quadratic nonresidues are exactly \(t\in\{52,53,54\}\). Because \(3\) is a quadratic residue modulo \(83\), a primitive-root progression with step \(3\) would have one of these three normalized starting indices. But for every such \(t\), at least one of \(3(t+j)\), \(0\le j\le4\), is \(-1\pmod{83}\): the five forbidden indices are \(\{51,52,53,54,55\}\). This proves the failure at \(83\), hence the sharpness of \(107\).

Combining the infinite character bound and the finite exhaustive certificate completes the theorem. \(\square\)

## Verification

Run `python3 verify.py` in a directory containing the attached `verify.py`. It uses only Python's standard library, and prints all safe primes below \(2000\), the number of failing differences at each one, the two exceptional difference lists and PASS assertions. The exhaustive search is not used as a proof beyond its stated finite range. The analytic proof covers every larger prime without computational assumptions.

## Relationship to prior work

Carella (first public arXiv date 2019-10-05) studies prescribed configurations of primitive roots, with an asymptotic existence theorem for sufficiently large primes, not an exact sharp threshold for all nonzero differences at safe primes. Jarso and Trudgian prove a general four-consecutive-elements theorem and identify the five-consecutive case as substantially harder. Lemos, Neumann and Ribas study prescribed-step primitive progressions in nontrivial extension fields, providing explicit classifications for shorter lengths and asymptotic guarantees for larger lengths; their extension-degree hypothesis does not include prime fields.

An indexed 2026 result establishes *four*-term primitive-root progressions for all differences at safe primes \(p\ge47\); that assertion alone cannot guarantee a fifth primitive element. The present five-term threshold is \(107\), with a six-difference obstruction at \(83\). OEIS A268397 concerns the least prime admitting some length-specific run with step one, which does not test the universal-step property.

## Limitations

The conclusion is restricted to prime moduli with \((p-1)/2\) prime, and to exactly five consecutive positions in an arbitrary nonzero step. It does not settle five primitive elements for general finite fields or general prime moduli, nor prove infinitely many safe primes exist. The finite portion relies on a fully specified exhaustive checker; a separate formal certification has not been provided.

## References

1. N. A. Carella, *Configurations Of Consecutive Primitive Roots*, arXiv:1910.02308 (first posted 2019-10-05), https://arxiv.org/abs/1910.02308.
2. T. Jarso and T. Trudgian, *Four consecutive primitive elements in a finite field*, arXiv:2109.11691 (first posted 2021-09-23), https://arxiv.org/abs/2109.11691.
3. A. Lemos, V. Neumann and S. Ribas, *On arithmetic progressions in finite fields*, arXiv:2208.02876 (first posted 2022-08-04), https://arxiv.org/abs/2208.02876.
4. OEIS A268397, *Smallest prime with at least a specified number of consecutive primitive roots*, https://oeis.org/A268397.
5. *Four-primitive-root progressions at every step in safe-prime fields*, public finding index entry (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-four-primitive-root-progressions-at-every-step-in-safe-prime-fie--4b3a1ebd1831.
