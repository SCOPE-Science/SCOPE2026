# Exact Gaussian-rational logarithmic-value spectrum and dense fibers for the polar arithmetic derivative

## Finding

For the ordinary arithmetic derivative on the rationals extended to Gaussian rationals by Kovič's **polar convention**, let \(D\) denote that extension and \(L(z)=D(z)/z\) for every nonzero \(z\in\mathbb Q(i)\). Define
\[
\mathcal R=\left\{\frac ab\in\mathbb Q:\ \gcd(a,b)=1,\ b>0,\ v_2(b)\le2,\ v_\ell(b)\le1\ \text{for every odd prime }\ell\right\}.
\]
Here \(v_p(b)\) denotes the usual exponent of \(p\) in the positive integer \(b\). **Then the exact image of \(L\) is \(\mathcal R\), and every nonempty level set \(L^{-1}(r)\subset\mathbb Q(i)^\times\) is dense in \(\mathbb C\).** Thus the nonzero Gaussian-rational solutions of \(D(z)=rz\) exist exactly for \(r\in\mathcal R\), and each such solution set is dense in the complex plane.

For instance, \(L(1+i)=1/4\), \(L(3/(1+i))=1/12\), while the equation \(D(z)=z/8\) has **no** solution in \(\mathbb Q(i)^\times\). The corresponding image on \(\mathbb Q^\times\) is the already-known set of rationals with squarefree reduced denominator, including denominator \(1\).

## Assumptions and scope

The derivative on positive rationals is the standard one determined by \(D(p)=1\) for ordinary rational primes and the Leibniz rule. For \(q=\prod_p p^{e_p}\in\mathbb Q_{>0}\), with finitely supported integer exponents, this means
\[
\frac{D(q)}q=\sum_p\frac{e_p}{p}.
\]
On the positive real radicals required to differentiate moduli, use the established rule \(D(q^{1/2})/q^{1/2}=D(q)/(2q)\). Kovič's polar extension sets \(D(e^{i\theta})=0\) for points on the unit circle and uses the Leibniz rule on \(z=|z|e^{i\theta}\); equivalently \(D(z)=zD(|z|)/|z|\). This is **not** the different Gaussian-prime convention assigning derivative \(1\) to every canonical Gaussian irreducible.

The domain is exactly \(\mathbb Q(i)^\times\) (nonzero complex numbers with rational real and imaginary parts), not arbitrary radical extensions or all complex numbers. The zero vector is not counted as a nonzero eigenvector; \(D(0)=0\) does not create additional logarithmic values. The image consists of rational real numbers only.

## Proof

**1. Norm formula.** For \(z=a+ib\) with \(a,b\in\mathbb Q\), \(z\ne0\), put \(N=z\overline z=a^2+b^2\in\mathbb Q_{>0}\). Since \(|z|=N^{1/2}\), the polar rule gives
\[
L(z)=\frac{D(|z|)}{|z|}=\frac12\frac{D(N)}N=\frac12\sum_p\frac{v_p(N)}p.
\]
Here the integer valuations \(v_p(N)\) are allowed to be negative. Norm multiplicativity implies \(L(zw)=L(z)+L(w)\) for all nonzero Gaussian rationals.

**2. Necessary denominator condition.** The right-hand side is a finite integer linear combination of \(1/4\) and \(1/(2p)\) for odd primes \(p\). Hence its reduced denominator divides \(4m\) for some odd squarefree \(m\), so it belongs to \(\mathcal R\). The exponent of \(2\) cannot exceed \(2\), and no odd prime may occur more than once.

**3. Sufficiency by Bézout.** Conversely, let \(r=a/b\in\mathcal R\) in lowest terms and write \(b=2^\nu m\), with \(0\le\nu\le2\) and odd squarefree \(m\). Then \(A=4mr\in\mathbb Z\). The finite integer list
\[
m,\qquad\left\{\frac{4m}{p}:p\mid m\right\}
\]
has greatest common divisor \(1\): any prime dividing \(m\) is absent from the corresponding second entry, and \(m\) is odd. Therefore integers \(c_0\) and \(c_p\) exist with
\[
A=mc_0+\sum_{p\mid m}\frac{4m}{p}c_p.
\]
(The sum is empty when \(m=1\), in which case \(A=4r\) and \(c_0=A\).) Dividing by \(4m\) gives \(r=c_0/4+\sum_{p\mid m}c_p/p\). Since \(L(1+i)=1/4\) and \(L(p)=1/p\) for every positive rational prime \(p\), the Gaussian rational
\[
z_0=(1+i)^{c_0}\prod_{p\mid m}p^{c_p}
\]
is nonzero and satisfies \(L(z_0)=r\). Negative integer exponents are legitimate in \(\mathbb Q(i)\). This proves that the image equals \(\mathcal R\).

**4. A dense positive-real zero class.** Two positive rationals
\[
u=\frac4{27}=2^2 3^{-3},\qquad v=\frac4{3125}=2^2 5^{-5}
\]
obey \(L(u)=L(v)=0\) because \(2/2-3/3=0\) and \(2/2-5/5=0\). Their positive logarithms in absolute value are incommensurable: if \(\log u/\log v\) were rational, some nonzero integral powers would satisfy \(u^j=v^k\); comparing the \(3\)-adic valuation would force \(j=0\) and then the \(5\)-adic valuation would force \(k=0\), a contradiction. Thus the additive subgroup \(\mathbb Z\log u+\mathbb Z\log v\) is dense in \(\mathbb R\) by the standard irrational-rotation argument. Exponentiating, \(\{u^jv^k:j,k\in\mathbb Z\}\) is dense in \(\mathbb R_{>0}\). Its elements all have logarithmic derivative zero.

**5. A dense angular zero class and all fibers.** For \(t\in\mathbb Q\),
\[
w_t=\frac{1-t^2+2it}{1+t^2}\in\mathbb Q(i),\qquad w_t\overline{w_t}=1.
\]
The rational parametrization of the unit circle shows that these \(w_t\) are dense in \(\{z\in\mathbb C:|z|=1\}\), and the norm formula yields \(L(w_t)=0\). The products \(u^jv^k w_t\) therefore form a dense subset of \(\mathbb C\) (their radii are dense in the positive reals, their arguments are dense on the circle, and radii approach zero). They lie in the zero class. For any \(r\in\mathcal R\), multiplying by the fixed \(z_0\) from Step 3 carries these products into the level set \(L^{-1}(r)\), still densely covering \(\mathbb C\). For \(r\notin\mathcal R\), Step 2 shows that the level set is empty. This finishes the proof.

## Verification

The accompanying standalone Python program `VERIFY.py` uses exact rational arithmetic. It checks the denominator necessity for \(5{,}280\) explicit nonzero Gaussian rationals, constructs and verifies examples on \(452\) admitted rational levels, tests both independent rational zero-class generators, and confirms the examples at \(1/4\), \(1/12\) and the denominator obstruction at \(1/8\). It prints `VERIFY_OK` on success. Its finite checks are corroboration only: the Bézout and density arguments prove the unrestricted theorem.

## Relationship to prior work

Ufnarovski and Åhlander (2003), Theorem 18, already characterize the rational-domain logarithmic values by squarefree reduced denominator. That is used as background and is **not** claimed as a new rational-domain classification. They also give the full rational zero-derivative kernel (Theorem 15), which supplies context for the positive-real density construction.

Kovič (2012), Proposition 1(iii), defines precisely the polar Gaussian-rational extension used here and Definition 3 introduces its logarithmic classes. His Proposition 12 observes that the formal radical \(p^{pr}\) has logarithmic derivative \(r\) for every rational \(r\). Such a radical need not belong to the fixed Gaussian-rational domain: for example the level \(1/8\) is empty there. The present finding supplies the missing **domain-specific** exact image and the density of every nonempty class. The known rational results and the stated polar rule are credited to their sources, rather than counted as new proof content.

Dahl, Olsson and Loiko (2011) establish unboundedness of ordinary rational derivatives in every interval; that does not determine these fixed-logarithmic-value Gaussian-rational fibers. Literature employing canonical Gaussian-prime derivatives concerns a distinct operator.

## Limitations

The result is specific to the polar extension with zero derivative on the full unit circle, and to its nonzero Gaussian-rational domain. No assertion is made for arbitrary derivatives on the unit circle, for the Gaussian-prime normalization, or for unrestricted complex inputs. Density is topological, not a quantitative equidistribution rate, and this theorem does not classify solutions to nonhomogeneous arithmetic differential equations. Bibliographic searches cannot rule out independently published equivalent formulations; historical priority remains provisional. No independent audit of this proof is asserted.

## References

1. V. Ufnarovski and B. Åhlander, *How to Differentiate a Number*, Journal of Integer Sequences **6** (2003), Article 03.3.4, Theorems 14–18. https://www.kurims.kyoto-u.ac.jp/EMIS/journals/JIS/VOL6/Ufnarovski/ufnarovski.pdf
2. J. Kovič, *The Arithmetic Derivative and Antiderivative*, Journal of Integer Sequences **15** (2012), Article 12.3.8, Proposition 1, Definition 3, Proposition 12. https://cs.uwaterloo.ca/journals/JIS/VOL15/Kovic/kovic4.pdf
3. N. Dahl, J. Olsson and A. Loiko, *Investigations on the properties of the arithmetic derivative* (2011), https://arxiv.org/abs/1108.4762
