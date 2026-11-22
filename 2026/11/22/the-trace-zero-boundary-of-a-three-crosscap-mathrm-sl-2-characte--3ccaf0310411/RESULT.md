# The trace-zero boundary of a three-crosscap \(\mathrm{SL}_2\)-character variety is an algebraic cylinder

## Finding

Let \(\Gamma=\langle A,B,C\mid A^2B^2C^2=1\rangle\), and let \(X=\operatorname{Hom}(\Gamma,\mathrm{SL}_2(\mathbb C))//\mathrm{SL}_2(\mathbb C)\) denote the affine GIT character variety. Write \(D=(\operatorname{tr}C=0)_{\mathrm{red}}\subset X\). There is an isomorphism of reduced complex affine varieties

\[D\simeq\operatorname{Spec}\mathbb C[t,t^{-1},u]\simeq\mathbb G_m\times\mathbb A^1.\]

In standard seven trace coordinates

\[\begin{aligned}a&=\operatorname{tr}A,&b&=\operatorname{tr}B,&c&=\operatorname{tr}C,&p&=\operatorname{tr}(AB),\\q&=\operatorname{tr}(BC),&r&=\operatorname{tr}(CA),&s&=\operatorname{tr}(ABC),\end{aligned}\]

the trace morphism embeds \(D\) as the affine subvariety cut out **exactly** by

\[c=p=0,\quad a^2+b^2=4,\quad 2q=as,\quad 2r=bs.\]

The inverse coordinates are \(t=(a+ib)/2\) and \(u=s/(2i)\); notably \(t\ne0\). The map retaining only \((a,b,c,p)\) identifies every \(\mathbb A^1\)-fiber with a single point on the conic \(a^2+b^2=4,\ p=c=0\). Consequently the trace-zero boundary is a smooth, irreducible surface whose **one-dimensional image** is a proper closed subvariety of the naive four-trace hypersurface section \(c=0\), which itself has dimension two and extraneous points.

## Assumptions and scope

The base field is \(\mathbb C\), and all matrices have determinant one. The word “character variety” means the **categorical affine quotient** by simultaneous conjugation; two non-closed representation orbits can have the same character. We describe the reduced boundary \(D\), not any possible nonreduced nilpotent structure of its scheme-theoretic preimage. The generators and order of the single relation are fixed. There is no assertion about unrelated boundary components or positive characteristic.

## Proof

**1. The matrix equation forces commutativity.** If \(\operatorname{tr}C=0\), the Cayley–Hamilton identity in \(\mathrm{SL}_2\) gives \(C^2=-I\); the relation becomes \(A^2B^2=-I\). Since \(A^2=-B^{-2}\), the matrix \(A^2\) commutes with \(B\). If \(a=\operatorname{tr}A\ne0\), then \(A^2=aA-I\), so \(A=(A^2+I)/a\) commutes with \(B\). If \(a=0\), then \(A^2=-I\) and \(B^2=I\); in characteristic zero a determinant-one involution is scalar, so \(B=\pm I\) and commutativity still follows. Therefore \(A\) and \(B\) always commute.

**2. A canonical regular-semisimple slice.** Put \(T=AB\). Commutativity yields \(T^2=-I\). As \(\det T=1\), the two eigenvalues of \(T\) are \(i,-i\), each once. Simultaneous conjugation sends \(T\) to \(T_0=\operatorname{diag}(i,-i)\). Since \(A\) and \(B\) commute with \(T\), they become diagonal and are **uniquely** of the form

\[A=\begin{pmatrix}t&0\\0&t^{-1}\end{pmatrix},\qquad B=\begin{pmatrix}i/t&0\\0&-it\end{pmatrix},\qquad t\in\mathbb C^*.\]

All trace-zero determinant-one matrices \(C\) take the form

\[C=\begin{pmatrix}u&v\\w&-u\end{pmatrix},\qquad u^2+vw=-1.\]

Conversely, every such triple satisfies \(A^2B^2C^2=I\). These equations give the entire set-theoretic representation boundary, not merely a generic chart: no assumption that \(a\), \(t-1\), \(v\), or \(w\) is nonzero was made.

**3. Take the GIT quotient rather than orbit classes.** The orbit of \(T_0\) is \(\mathrm{SL}_2/H\), where \(H=Z_{\mathrm{SL}_2}(T_0)\cong\mathbb G_m\) is the diagonal torus. The reduced boundary representation variety is the associated homogeneous bundle over that orbit with fiber

\[F=\operatorname{Spec}\frac{\mathbb C[t,t^{-1},u,v,w]}{(u^2+vw+1)}.\]

Passing to the categorical quotient by \(\mathrm{SL}_2\) is equivalently quotienting \(F\) by \(H\). Conjugation by \(\operatorname{diag}(\lambda,\lambda^{-1})\) fixes \(t,u\) and sends \(v\mapsto\lambda^2v\), \(w\mapsto\lambda^{-2}w\). A weight-zero monomial in \(v,w\) is a power of \(vw\), and \(vw=-1-u^2\) in \(F\). Hence the invariant coordinate ring is **exactly**

\[\mathbb C[F]^H=\mathbb C[t,t^{-1},u].\]

Characteristic-zero reductivity makes invariants exact, so quotienting the representation variety by \(\operatorname{tr}C=0\) agrees with the trace-zero closed fiber of the quotient; taking the reduced structure gives the displayed \(D\). This argument includes the special fibers \(u=\pm i\), where some nonclosed orbits have a common closed GIT representative.

**4. Calculate the trace embedding.** In the displayed matrices,

\[a=t+t^{-1},\quad b=i(t^{-1}-t),\quad c=p=0,\quad s=2iu,\quad q=iau,\quad r=ibu.\]

Thus \(a^2+b^2=4\), \(2q=as\), and \(2r=bs\). Conversely the affine equations in the claim yield \(t=(a+ib)/2\), \(t^{-1}=(a-ib)/2\), and \(u=s/(2i)\); the conic relation guarantees the two reciprocal expressions multiply to one. This supplies the inverse polynomial/Laurent morphism, proving **closed immersion and surjectivity onto that explicit locus**, without appealing merely to equality on points. Projection to \((a,b,c,p)\) forgets only \(u\), so its fibers are exactly affine lines over the indicated conic.

## Verification

The supplied standalone exact-arithmetic checker, `verify.py`, symbolically confirms the determinant, group relation, trace formulas, and Laurent inverse identities. It also checks three exact example triples including the coordinate boundary \(v=0\). The crucial inference from the matrix identity to commutativity and the torus-invariant ring calculation are **proved above**; finite examples do not replace those arguments. A reader can execute `python verify.py` with Python 3 and SymPy installed.

## Relationship to prior work

Yinxi Chen, *An Explicit Equation for the SL2(C) Character Variety of RP2#RP2#RP2* (arXiv:2611.08513, first submitted 14 October 2026), establishes the four-trace equation \(c^2=abp-a^2-b^2+4\) and an open description away from \(c=0\). Its §5.2 proves the matrix identity \(A^2B^2=-I\) on the boundary, and expressly leaves the full boundary matrix/GIT classification open. The present finding resolves precisely that remaining reduced-boundary classification and corrects the naive identification of the full hypersurface section with the actual character boundary; neither the equation nor the matrix reduction is claimed as new.

Benyash-Krivets and Chernousov (1997) investigate components, dimensions, and birational geometry of representation/character varieties of compact non-orientable surface groups; the inspected text does not supply this seven-trace boundary embedding. Baraglia and Hekmati (arXiv:1602.06996) calculate global \(E\)-polynomials for \(\mathrm{SL}_2\)-character varieties of non-orientable surfaces, including the three-crosscap case, but do not give this explicit trace-zero reduced closed stratum. These broader results are compatible with, but do not directly identify, the asserted divisor.

## Limitations

The result is over \(\mathbb C\), concerns a single marked trace-zero generator, and specifies only the reduced boundary. The scheme-theoretic multiplicity of the divisor in a hypothetical nonreduced model has not been computed. Quotient points parametrize closed conjugacy orbits, not every individual nonclosed representation orbit. The historical priority comparison is strongest for the inspected sources, and unindexed earlier classifications of special representation slices remain a residual novelty risk. The proof does not assert the initiating paper's entire four-trace hypersurface is a correct global model.

## References

1. Y. Chen, *An Explicit Equation for the SL2(C) Character Variety of RP2#RP2#RP2*, arXiv:2611.08513 (2026), §§2–5.2. https://arxiv.org/abs/2611.08513
2. D. Baraglia and P. Hekmati, *Arithmetic of Singular Character Varieties and Their E-Polynomials*, arXiv:1602.06996 (2016), Theorem 1.4 and §§5.2, 6.7. https://arxiv.org/abs/1602.06996
3. V. V. Benyash-Krivets and V. I. Chernousov, *Representation varieties of the fundamental groups of non-orientable surfaces*, Sbornik: Mathematics 188 (1997), 997–1039. https://www.mathnet.ru/links/c0e6f6316f4e1e38715eaf171cbb6d83/sm242_eng.pdf
