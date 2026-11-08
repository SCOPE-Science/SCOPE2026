# Two a-number strata with minimal geometric automorphisms in genus-six Artin--Schreier curves

## Finding

**Theorem.** Let \(k\) be an algebraically closed field of characteristic \(3\), and let \(X_f\) be the smooth projective model of \(y^3-y=f(x)\), where \(f\in k[x]\) has degree \(7\). Removing monomials whose positive exponents are divisible by \(3\) by Artin--Schreier coboundaries, and then removing the constant term, gives
\[
 f(x)=a_7x^7+a_5x^5+a_4x^4+a_2x^2+a_1x,\qquad a_7\ne0.
\]
Then \(g(X_f)=6\), its \(3\)-rank is zero, and
\[
 a(X_f)=\begin{cases}4,&a_5=0,\\3,&a_5\ne0.\end{cases}
\]
Here \(a(X_f)=\dim_k\ker(\mathcal C)\), where \(\mathcal C\) is the Cartier operator on holomorphic differentials.

Both a-number values occur for explicitly defined curves over \(\mathbb F_3\) whose **full geometric** automorphism group is \(C_3\):
\[
 X_4:\ y^3-y=x^7+x^2,\qquad a(X_4)=4;
\]
\[
 X_3:\ y^3-y=x^7+x^5+x^2,\qquad a(X_3)=3.
\]
In each case all geometric automorphisms are \((x,y)\mapsto(x,y+c)\) for \(c\in\mathbb F_3\). Consequently the *entire* set of a-numbers occurring in the characteristic-three genus-six, zero-\(3\)-rank Artin--Schreier locus is \(\{3,4\}\), and neither value requires an extra automorphism.

## Assumptions and scope

The ground field is algebraically closed of characteristic \(3\), except that the exhibited equations are over the prime field \(\mathbb F_3\). Genus, a-number, rank, and automorphism groups are **geometric** invariants. An Artin--Schreier curve here means a cyclic separable degree-three cover of \(\mathbb P^1\) with the specified equation and smooth projective normalization. The condition of one pole follows automatically for a rank-zero Artin--Schreier cover; genus \(6\) then forces unique pole order \(7\). No assertion is made about arbitrary genus-six curves outside this locus.

## Proof

**1. Reduction, genus, rank, and differentials.** Over the perfect field \(k\), replacing \(y\) by \(y+h(x)\) removes terms of degrees \(6\) and \(3\), and a constant, without changing the cover. The genus formula for a degree-three one-pole cover of order \(7\) gives \(g=(3-1)(7-1)/2=6\). Deuring--Shafarevich gives \(3\)-rank \((s-1)(3-1)=0\) for \(s=1\) pole. At the unique point above infinity, the valuation of \(x\) is \(-3\), that of \(y\) is \(-7\), and that of \(dx\) is \(10\): the different exponent is \((3-1)(7+1)=16\), and \(\operatorname{div}(dx)=\pi^*\operatorname{div}(dx_{\mathbb P^1})+16P=-6P+16P=10P\). Therefore
\[
 \{dx,\ x\,dx,\ x^2dx,\ x^3dx,\ y\,dx,\ xy\,dx\}
\]
is a basis of holomorphic differentials (its six distinct pole-order weights are at most \(10\), and \(g=6\)).

**2. Exact Cartier matrix.** In characteristic three, \(\mathcal C(x^jdx)=0\) unless \(j\equiv2\pmod3\), in which case \(\mathcal C(x^{3i+2}dx)=x^i dx\). Since \(y=y^3-f(x)\), the Cartier identity \(\mathcal C(g^3\omega)=g\mathcal C(\omega)\) gives
\[
 \begin{aligned}
 \mathcal C(dx)&=\mathcal C(x\,dx)=\mathcal C(x^3dx)=0,\\
 \mathcal C(x^2dx)&=dx,\\
 \mathcal C(y\,dx)&=-a_2^{1/3}dx-a_5^{1/3}x\,dx,\\
 \mathcal C(xy\,dx)&=-a_1^{1/3}dx-a_4^{1/3}x\,dx-a_7^{1/3}x^2dx.
 \end{aligned}
\]
The last image contains a nonzero \(x^2dx\) component because \(a_7\ne0\). The first nonzero image is \(dx\). A third independent image exists precisely when \(a_5\ne0\), because then \(\mathcal C(y\,dx)\) has a nonzero \(x\,dx\) component. The Cartier rank is therefore \(2\) or \(3\), respectively. Subtracting from genus \(6\) proves the a-number dichotomy. This argument handles *every* coefficient choice in the specified reduced form, not merely the two examples.

**3. Reduction of the full geometric automorphism problem.** The exceptional Artin--Schreier covers excluded from the Valentini--Madan rational-subfield theorem cannot have the present one-pole data: in characteristic \(3\), the one-pole exceptional family has pole order dividing \(4\), whereas ours is \(7\), and the other families have positive \(3\)-rank. The nonexceptionality criterion appears explicitly as Lemma 3.2(i) of Tafazolian--Kazemifard [1]. It follows that **every** geometric automorphism (not just those preserving a chosen fibration by assumption) has the form
\[
 (x,y)\mapsto(Ax+B,uy+h(x)),\qquad A\in k^\times,\ B\in k,\ u\in\mathbb F_3^\times,\ h\in k[x],\ \deg h\le2,
\]
with the polynomial identity
\[
 f(Ax+B)-u f(x)=h(x)^3-h(x).
\]
Comparing leading coefficients shows \(u=A^7\), so \(A^{14}=1\). Write \(c_i\) for the coefficient of \(x^i\) on the left. Since \(h=h_2x^2+h_1x+h_0\), necessary and sufficient nonconstant-coefficient conditions are \(c_5=c_4=0\), \(c_6+c_2^3=0\), and \(c_3+c_1^3=0\); the constant equation always has a solution over \(k\).

**4. Automorphisms of the a-number-four example.** For \(f=x^7+x^2\), the \(x^4\)-coefficient is \(c_4=2A^4B^3\), hence \(B=0\). Now \(c_6=0\) and \(c_2=A^2-A^7\), so \(c_6+c_2^3=0\) gives \(A^5=1\). Together with \(A^{14}=1\) this yields \(A=1\), since \(\gcd(5,14)=1\). Thus \(u=1\), and \(h^3-h=0\) forces \(h=c\in\mathbb F_3\). There are exactly three automorphisms.

**5. Automorphisms of the a-number-three example.** For \(f=x^7+x^5+x^2\), the \(x^5\)-coefficient gives \(A^5=A^7=u\). Thus \(A^2=1\) and \(u=A\). The \(x^4\)-coefficient is \(2A^4(B^3+B)\), so \(B^3+B=0\). The \(x^6\)- and \(x^2\)-coefficients are \(c_6=B\) and \(c_2=B^3+1-A\). Consequently the necessary identity \(c_6+c_2^3=0\) becomes \(2B+1-A=0\). If \(A=-1\), this requires \(B=-1\), contrary to \(B^3+B=0\). Hence \(A=1\) and \(B=0\), and again only the three constants \(h\in\mathbb F_3\) remain. This exhausts *geometric* automorphisms in both examples.

## Verification

The companion `verify.py` checks, using exact polynomial arithmetic over \(\mathbb F_3\), that the coefficient conditions for a geometric automorphism on each example have reduced Gröbner basis \(\{B,A-1\}\) (after imposing \(A^{14}=1\)), and independently checks the two Cartier matrix ranks by finite-field elimination. Run `python3 verify.py` with SymPy installed (tested using SymPy 1.14). The expected final line is `CERTIFICATE_OK`. The infinite/all-coefficient a-number statement follows from the displayed Cartier matrix; the automorphism proof uses the cited nonexceptionality theorem rather than assuming it in the script.

## Relationship to prior work

Tafazolian--Kazemifard [1, Theorem 1.1, Lemma 3.2, Lemma 3.3] determine when minimal geometric automorphisms can occur and exhibit one characteristic-three genus-six example, \(y^3-y=x^7+x^4\), but do not determine a-numbers for these curves. Their Question 7.5 explicitly asks whether one can prescribe an a-number while retaining the minimal group. The present result resolves that question at the exact natural stratum \((p,g,\gamma)=(3,6,0)\), including a complete classification of its possible a-numbers.

Duque-Rosero--Lorenzo García--Malmskog--Scheidler [2, Example 4.7] already give the **same genus-six standard-form family** and its isomorphism constraints, and therefore provide stronger contextual information than a generic citation about Artin--Schreier curves. They do **not** give the Cartier-rank dichotomy or identify both a-number strata with full geometric automorphism group \(C_3\). In particular the occurrence of the coefficient \(a_5\) in the family is not itself a computation of the a-number.

Farnell--Pries [3] establish a constant-a-number result under \(p\equiv1\pmod L\), inapplicable for \(p=3\) and unique pole order \(L=7\). Booher--Cais [4] provide bounds and examples for a-numbers of Artin--Schreier covers, including a different small-characteristic example exhibiting two a-numbers; they do not determine the above genus-six \(C_3\)-automorphism intersection. The computations of the present exact two models and the simultaneous rigidity statement do not follow from the cited assertions alone. General Cartier formulas are classical and are **not** claimed to be new here.

## Limitations

The result is restricted to characteristic three, genus six, and the Artin--Schreier locus with one pole (equivalently, zero \(3\)-rank). It neither determines Newton polygons nor gives a general prescription at other genus and rank values. The a-number computation is elementary once a differential basis is known; the substantive conclusion is the complete natural stratum and realization of both outcomes with *minimal full geometric automorphisms*. Existing general algorithms for Cartier operators might also recover the matrix upon specialized substitution, so historical priority of this precise combination should be regarded as provisional pending wider expert review. No independent mathematical audit has been performed.

## References

1. S. Tafazolian and A. Kazemifard, *Artin--Schreier Curves of Prescribed p-Rank Without Extra Automorphisms*, arXiv:2610.13279, first posted 2026-10-09, especially Lemmas 3.2--3.3 and Question 7.5. https://arxiv.org/pdf/2610.13279
2. J. Duque-Rosero, E. Lorenzo García, B. Malmskog, R. Scheidler, *Computing Invariants of Artin-Schreier Curves*, arXiv:2602.22435, especially Example 4.7. https://arxiv.org/pdf/2602.22435
3. S. Farnell and R. Pries, *Families of Artin-Schreier curves with Cartier-Manin matrix of constant rank*, arXiv:1202.4183, especially Theorem 1.1. https://arxiv.org/pdf/1202.4183
4. J. Booher and B. Cais, *a-Numbers of Curves in Artin-Schreier Covers*, arXiv:1807.10313, especially Section 7. https://arxiv.org/pdf/1807.10313
