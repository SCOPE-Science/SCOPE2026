# Exact variable width for identifying prime-order cyclic groups

## Finding

For primes \(p\), let \(\mathcal G_p=(\mathbb Z/p\mathbb Z;R,0)\), where \(R(a,b,c)\) means \(a+b=c\) modulo \(p\). In this relational language, three variable names suffice to distinguish every pair of different primes in counting-free first-order logic. The least width for identifying \(\mathcal G_p\) **relative to the prime-order family** is one for \(p=2\), two for \(p=3,5\), and three for every \(p\ge7\). The three-name construction gives the upper bound; the earlier elementary-abelian two-variable classification [1] supplies the lower bound for \(p\ge7\).

## Assumptions and scope

Equality and the constant \(0\) are available; addition and inverse are not term-forming function symbols. Names can be reused under quantifiers, depth is unrestricted, and there are no counting quantifiers. Identification is only within the prime-order cyclic family. No optimal rank bound is asserted.

## Three names suffice

For a positive integer \(n\), define a formula \(D_n(a,b)\) with free names \(a,b\) and using names from \(\{x,y,z\}\). For any two distinct names \(a,b\) from this set, use \(D_1(a,b)=(a=b)\) and, with \(c\) the spare name, use
\[
D_{n+1}(a,b)=\exists c\,\bigl(R(c,a,b)\land D_n(a,c)\bigr).
\]
Here \(D_n(a,c)\) is constructed for the ordered pair of names \((a,c)\); it may bind \(b\) locally, but cannot bind \(a\) or capture the occurrence of \(b\) in the other conjunct. Induction gives \(D_n(a,b)\) iff the value of \(b\) is \(n\) times the value of \(a\). For each prime \(r\ge2\), the sentence
\[
\exists x\,\bigl(x\ne0\land \exists y\,[R(y,x,0)\land D_{r-1}(x,y)]\bigr)
\]
uses only the three names and asserts that a nonzero element is killed by \(r\). This holds in \(\mathcal G_p\) exactly when \(p=r\). The case \(r=2\) uses the base formula \(D_1\).

## Lower bounds and small primes

The earlier theorem [1], restricted to elementary abelian groups of dimension one, gives the four width-two theories \(2\), \(3\), \(5\), and all \(p\ge7\). For clarity, its prime-order restriction can be checked directly. At odd prime order, with a nonzero stationary element \(x\), the two-name atomic data of \(y\) is determined by whether \(y\) is one of \(0,x,2x,x/2,-x\), or lies outside them. Indeed, after taking account of equality, a nontrivial ternary atom on \(0,x,y\) tests doubling, halving, negation, or two-torsion. The five specified choices are distinct at \(p\ge7\), and the outside class is nonempty; stationary zero only distinguishes zero from nonzero. This supplies matching two-pebble replacements forever. Thus no prime \(p\ge7\) is identifiable at width two.

The following width-one or width-two sentences also show the small cases explicitly. Let
\[
\begin{aligned}
\alpha &:=\exists x\,(x\ne0\land R(x,x,0)),\\
\beta &:=\exists x\exists y\,(x\ne0\land R(x,x,y)\land R(x,y,0)),\\
\gamma &:=\exists x\exists y\,(x\ne0\land y\ne0\land y\ne x\land\neg R(x,x,y)\land\neg R(y,y,x)\land\neg R(x,y,0)).
\end{aligned}
\]
Within the prime family, \(\alpha\) identifies \(p=2\), \(\beta\) identifies \(p=3\), and \(\gamma\) holds exactly at \(p\ge7\): at \(p=5\) the four nonzero possibilities are \(x,2x,x/2,-x\); at \(p=3\) the only nonzero choice distinct from \(x\) is \(-x\); at \(p=2\) even that choice does not exist. Hence \(\neg\alpha\land\neg\beta\land\neg\gamma\) identifies \(p=5\). With one name the only nonconstant tests on an element reduce to \(x=0\) and \(R(x,x,0)\), and they agree on corresponding zero and nonzero elements across all odd primes. A one-pebble replacement therefore always matches, so neither \(p=3\) nor \(p=5\) is identifiable with one variable. The ground atoms involving only \(0\) agree at all primes. This proves the exact width statement.

## Verification

`python3 verify_prime_logic.py` enumerates all 27 ternary atomic substitutions from two variable names and zero and checks the previously known width-two theories in 14 prime examples through order 43. It checks 49 evaluations of three-name prime-torsion formulas over the first seven primes. The recorded output is `verification_output.txt`. The finite tests are corroboration; the formula induction and permanent matching argument give the unrestricted conclusions.

## Relationship to prior work

The width-two classes are credited to the broader indexed result [1], not asserted as a separate new classification. Gomaa [2], Definition 3.1 and Theorem 3.8, uses the same relational vocabulary and gives a five-pebble distinguishing strategy with a bound on rounds. The three-name formula here instead retains an anchor and reuses two names for successive multiples, without aiming at the short rank in that construction. The addition-chain theorem [3] improves rank without a width-three guarantee, and the exact rank-three partition [4] bounds rank rather than the number of reusable variable names. The retained result is the exact width at unrestricted rank, especially the sharp three-name boundary for every prime at least seven. An earlier equivalent three-name construction not identified in these comparisons remains possible.

## References

1. *Six complete two-variable theories of finite elementary abelian groups*, Resultary, Finding, [record](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-six-complete-two-variable-theories-of-finite-elementary-abelian--6c093e091e17).
2. W. Gomaa, *Model Theory and Complexity Theory*, University of Maryland dissertation, 2007, Definition 3.1 and §3.5, Theorems 3.7–3.8, [repository](https://drum.lib.umd.edu/items/b8c06e8c-d2da-4d80-923e-0bd02e2a8440).
3. *Addition chains shrink the prime cyclic EF gap to sublinear overhead*, Resultary, [record](https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-addition-chains-shrink-the-prime-cyclic-ef-gap-to-sublinear-over--caee94fcc353).
4. *Seven rank-three theories of prime cyclic groups*, Resultary, [record](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-seven-rank-three-theories-of-prime-cyclic-groups--9e6c5933b276).
