# Exact constant-coefficient fibers of irreducible projective polynomials

## Finding

Let \(q\ge 2\) be a prime power, \(d\ge2\) an integer and \(\ell\mid(q-1)\). Put \(m=q-1\), \(U=(q^d-1)/(q-1)\), and \(n=(q^d-1)/\ell\). Consider monic sparse polynomials over \(\mathbb F_q\) of the form

\[
G(X)=X^n+\sum_{j=0}^{d-1}a_jX^{(q^j-1)/\ell}.
\]

Fix a generator \(\eta\) of \(\mathbb F_q^\times\). For each nonzero prescribed constant \(c=a_0\), define the unique \(r\in\{0,\ldots,m-1\}\) by \(\eta^r=(-1)^d c\), and set \(h=\gcd(m,n)\). The **exact number** \(C_{q,d,\ell}(c)\) of irreducible polynomials of this form is

\[
C_{q,d,\ell}(c)=
\begin{cases}
\displaystyle\frac{U}{d}\prod_{\substack{p\mid n\\p\nmid m}}\left(1-\frac1p\right),&\gcd(r,h)=1,\\[5pt]
0,&\gcd(r,h)>1,
\end{cases}
\]

where products run over **distinct rational primes**. Thus all *attainable* nonzero constant coefficients have the same multiplicity, and the number of attainable coefficients is

\[
(q-1)\prod_{p\mid\gcd(q-1,n)}\left(1-\frac1p\right).
\]

In particular, **every** nonzero constant coefficient occurs if and only if

\[
\ell=q-1\quad\text{and}\quad\gcd(d,q-1)=1.
\]

The total number, summed over nonzero constants, is \(\ell\varphi(n)/d\), recovering the previously known unrestricted count.

## Assumptions and scope

All statements concern the special case in which the Frobenius base and coefficient field are equal (\(\sigma=q\)); no assertion is made for unequal Frobenius and coefficient fields. All \(q\) are prime powers, including characteristic two. The restriction \(d\ge2\) is essential to the cited correspondence. The case \(c=0\) is excluded: since \(n>1\), such a polynomial is divisible by \(X\).

The generator \(\eta\) fixes a labeling of constant coefficients; a different generator permutes these labels. The support condition can also be expressed intrinsically: for every rational prime \(p\mid\gcd(q-1,n)\), the multiplicative order of \((-1)^dc\) has its full \(p\)-primary exponent \(v_p(q-1)\). The formula does not depend on the generator.

## Proof

**1. The polynomial--root correspondence.** Write an ordinary monic polynomial as \(A(T)=T^d+\sum_{j=0}^{d-1}a_jT^j\). Associate the \(q\)-linearized polynomial \(\Delta_q(A)(X)=X^{q^d}+\sum_{j=0}^{d-1}a_jX^{q^j}\). For \(\ell\mid q-1\), it satisfies

\[
\Delta_q(A)(X)=XG(X^\ell).
\]

The coefficient of \(X\) in \(\Delta_q(A)\), and the constant of \(G\), both equal \(a_0=A(0)\). The irreducibility criterion in Kuttner--Wang [1, Lemmas 3.1--3.3 and Theorem 3.4, specialized to \(q=\sigma\)] gives a bijection between irreducible \(G\) and monic irreducible \(A\) of degree \(d\) whose root \(\beta\in\mathbb F_{q^d}^\times\) satisfies

\[
\operatorname{ord}(\beta^\ell)=\frac{q^d-1}{\ell}=n.
\]

For clarity, the key degree mechanism is the Frobenius orbit of a nonzero root \(\alpha\) of \(\Delta_q(A)\): the least \(k>0\) for which \((\alpha^\ell)^{q^k}=\alpha^\ell\) equals \(\operatorname{ord}(\beta^\ell)\). Hence \(G\) is irreducible exactly when that orbit has length \(n\). The converse, including the need that \(A\) is irreducible, is covered by [1, Lemmas 3.2--3.3]; it is not inferred merely from an orbit experiment.

**2. Translate the constant into a norm constraint.** Let \(N=q^d-1=\ell n=mU\) and choose a generator \(\Gamma\) of the cyclic group \(\mathbb F_{q^d}^\times\). Without loss of generality choose the generator \(\eta=\Gamma^U\): changing generators only multiplies the discrete logarithm \(r\) by a unit modulo \(m\), leaving the final coprimality test unchanged. Writing \(\beta=\Gamma^e\), the order condition in Step 1 is

\[
\gcd(e,n)=1.
\]

Since \(A(0)=(-1)^d\operatorname{Norm}_{\mathbb F_{q^d}/\mathbb F_q}(\beta)\) and \(\operatorname{Norm}(\Gamma)=\Gamma^U=\eta\), the prescribed constant is exactly \(e\equiv r\pmod m\). There are \(U\) choices \(e=r+mj\) modulo \(N\), with \(0\le j<U\).

**3. Count coprime exponents in a fixed norm class.** Let \(p\) be a rational prime dividing \(n\). If \(p\mid m\), every \(e=r+mj\) satisfies \(p\mid e\) precisely when \(p\mid r\). Thus a constant is impossible if \(\gcd(r,h)>1\). Otherwise, for each \(p\mid n\) with \(p\nmid m\), there is exactly one forbidden class of \(j\pmod p\), because \(m\) is invertible modulo \(p\). Every such \(p\) divides \(U\), as \(n=(m/\ell)U\) and \(p\nmid m\). Therefore \(j\) ranges over an integral number of full Chinese-remainder cycles, giving the exact number of qualifying roots

\[
U\prod_{\substack{p\mid n\\p\nmid m}}\left(1-\frac1p\right).
\]

**4. Divide by Frobenius orbit length.** Because \(n\ge U>q^{d-1}\), an element whose \(\ell\)-th power has order \(n\) cannot lie in any proper subfield of \(\mathbb F_{q^d}\). Each qualifying \(\beta\) consequently has degree \(d\); its Frobenius conjugacy class has exactly \(d\) elements, all with the same norm. Dividing the preceding exact count by \(d\) gives \(C_{q,d,\ell}(c)\). This also proves the displayed rational-looking expression is an integer.

**5. Support and sharp all-constants criterion.** The admissible exponents modulo \(m\) are those coprime to \(h\); their number is \(m\prod_{p\mid h}(1-1/p)\). They comprise all \(m\) residues if and only if \(h=1\). Now \(n=(m/\ell)U\), so \(\gcd(m,n)=1\) forces \(m/\ell=1\), i.e. \(\ell=m\), and then \(\gcd(m,U)=1\). Since \(U=1+q+\cdots+q^{d-1}\equiv d\pmod m\), this last condition is \(\gcd(m,d)=1\). Conversely those two conditions imply \(h=1\). Summing the nonzero fiber counts gives the total \(\ell\varphi(n)/d\).

## Verification

The bundled `verify.py` is a standard-library-only checker. It enumerates all cyclic exponents of \(\mathbb F_{q^d}^{\times}\) using their abstract cyclic group, partitions them by norm exponent, tests \(\gcd(e,n)=1\), and verifies the exact formula in 96 complete parameter systems with \(q\in\{2,3,4,5,7,8,9,11,13,16\}\), \(d\in\{2,3,4\}\), and admissible \(\ell\) under the stated size ceiling. Separately it enumerates the actual sparse polynomials in 14 complete small prime-field parameter systems, tests irreducibility using an independent polynomial-arithmetic implementation of Rabin's criterion, and compares the exact constant fibers after explicit discrete logarithms. Execute `python verify.py`. These finite checks corroborate but do not replace Steps 1--5, which are valid for all stated parameters.

For illustration, with \((q,d,\ell)=(5,2,4)\), precisely the two constants \(2\) and \(3\) occur, with two irreducible polynomials each. With \((q,d,\ell)=(3,3,2)\), both nonzero constants occur, with four irreducibles each.

## Relationship to prior work

Kuttner--Wang [1] give the exact unrestricted number \(\ell\varphi((q^d-1)/\ell)/d\) when \(q=\sigma\) and prove the essential irreducibility/order correspondence. The new object is the **full distribution by a prescribed constant coefficient**: the total count alone cannot identify forbidden constants or the all-constants threshold. The count is a norm-fiber refinement of their theorem, not a new proof of the unrestricted enumeration. Projectively primitive polynomials [2], restricted norm counts for general irreducibles [3], and primitive polynomials with prescribed constants [4] are related antecedents; their known statements do not supply this precise \(\ell\)-projective coefficient-fiber classification. The finite cyclic-group norm method is elementary once the correspondence is established.

## Limitations

The extension to \(\sigma\ne q\), prescribed additional coefficients, and irreducibles with zero constant are not claimed. The result uses the irreducibility/order correspondence from [1] as a cited proved lemma. Earlier norm-restricted counting arguments may give this result implicitly; unindexed or unpublished prior coverage remains an originality risk. No external independent mathematical audit has been performed.

## References

[1] S. Kuttner and Q. Wang, *Irreducible Projective Polynomials*, arXiv:2611.18927v1 (first submitted 2026-11-13), https://arxiv.org/abs/2611.18927.

[2] L. Amadio Guidi, P. Lindqvist and G. Micheli, *Full Orbit Sequences in Affine Spaces via Fractional Jumps and Pseudorandom Number Generation*, https://ora.ox.ac.uk/objects/uuid:03524a20-dcb9-48d0-9489-c0a42ed17b3f/files/mf56b366f7ce66cb9a3a32dd1b0df7821.

[3] *Irreducible Polynomials with Prescribed Trace and Restricted Norm*, arXiv:0710.2767, https://arxiv.org/abs/0710.2767.

[4] A. K. Sharma, *On the Existence of Primitive Polynomials* \(f(X)=g(X)+\lambda\) *over Finite Fields*, arXiv:2608.07262, https://arxiv.org/abs/2608.07262.
