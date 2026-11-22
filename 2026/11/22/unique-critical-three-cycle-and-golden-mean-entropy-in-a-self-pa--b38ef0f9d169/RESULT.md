# Unique critical three-cycle and golden-mean entropy in a self-parameterized tent map

## Finding

Consider the self-parameterized tent map introduced by Paul and collaborators,
\[
T_C(x)=\left(\frac{37}{25}+\frac{C+x}{4}\right)\min\{x,1-x\},\qquad 0\le x\le1,\quad 0\le C\le1.
\]
There is **exactly one** control in this range for which the turning point \(1/2\) has *least* period three:
\[
C_*=\frac{100\sqrt{337}-1789}{450}=0.1039021668\ldots.
\]
At that control its critical orbit is \(1/2\mapsto h\mapsto \ell\mapsto1/2\), where
\[
\ell=\frac{\sqrt{337}-7}{36},\qquad h=\frac{\sqrt{337}+11}{36}=\ell+\frac12.
\]
The four intervals with endpoints \(0,\ell,1/2,h,1\) form a finite Markov partition with adjacency matrix
\[
M=\begin{pmatrix}1&1&0&0\\0&0&1&0\\0&1&1&0\\1&0&0&0\end{pmatrix}.
\]
The map has the **exact topological entropy**
\[
h_{\mathrm{top}}(T_{C_*}|_{[0,1]})=\log\left(\frac{1+\sqrt5}{2}\right).
\]
The invariant core \([\ell,h]\) is topologically mixing. Every trajectory starting at \(0<x<1\) enters this core after finitely many iterations; the two endpoints \(0,1\) instead map to the fixed point \(0\) at time zero or one. The claim concerns the exact real interval map, not its digitized implementations.

## Assumptions and scope

The seed tent map is \(2C'\min\{x,1-x\}\) with dynamic control \(C'=0.74+0.125(x+C)\), as in the 2021 conference paper and 2023 journal elaboration. All iteration arithmetic is exact real arithmetic. The external control remains fixed during iteration. The map sends \([0,1]\) into itself for every \(C\in[0,1]\): its unique maximum is attained at \(x=1/2\), with height at most \(0.9275\). The primary assertion is the unique postcritical three-cycle and its exact Markov entropy and absorbing mixing core, not a claim that every orbit is aperiodic.

## Proof

**1. Critical equation and uniqueness.** Write \(A=37/25+C/4\), so \(37/25\le A\le173/100\). The map has the two polynomial branches
\[
L_A(x)=Ax+\frac{x^2}{4},\quad 0\le x\le\frac12;\qquad
R_A(x)=\left(A+\frac x4\right)(1-x),\quad\frac12\le x\le1.
\]
The first image of the turning point \(c=1/2\) is \(h_A=A/2+1/16\), which lies strictly between \(1/2\) and \(1\) throughout this parameter range. Its second image lies strictly between \(0\) and \(1/2\) and equals
\[
\ell_A=R_A(h_A)=-\frac{(8A-15)(72A+1)}{1024}.
\]
Direct expansion of the third iterate on the left branch gives
\[
T_C^3(c)-c=\frac{(8A-7)(72A-647)(576A^2-560A-463)}{4194304}.
\]
In the specified interval, \(8A-7>0\) and \(72A-647<0\); the last quadratic is strictly increasing and crosses zero exactly once. Its unique admissible root is \(A_*=(35+4\sqrt{337})/72\), corresponding to the stated \(C_*\). At this parameter, direct substitution gives \(0<\ell<c<h<1\) with the stated values; since the three points are distinct, \(c\) has least period three. On either side of \(C_*\), the third critical image is, respectively, above or below \(c\).

**2. Markov partition and entropy.** At \(A=A_*\), exact endpoint identities are
\[
T(0)=0,\quad T(\ell)=c,\quad T(c)=h,\quad T(h)=\ell,\quad T(1)=0.
\]
The branch is increasing left of \(c\) and decreasing right of it. Therefore the images of the successive closed partition intervals \(I_0=[0,\ell]\), \(I_1=[\ell,c]\), \(I_2=[c,h]\), \(I_3=[h,1]\) are, respectively, \(I_0\cup I_1\), \(I_2\), \(I_1\cup I_2\), and \(I_0\). This is precisely the displayed transition matrix. Away from the unique turning point, \(|T'(x)|\ge A_*>1\); the derivative is \(A+x/2\) on the left and \(1/4-A-x/2\) on the right. Hence inverse cylinders shrink geometrically, so this finite Markov partition is generating. The standard interval Markov entropy formula yields \(h_{\mathrm{top}}=\log\rho(M)\). Direct determinant calculation gives
\[
\det(zI-M)=z(z-1)(z^2-z-1),
\]
whose spectral radius is \((1+\sqrt5)/2\).

**3. Mixing core and finite absorption.** The union \(I_1\cup I_2=[\ell,h]\) is forward invariant. Its two-cell transition matrix is \(\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)\), whose square has strictly positive entries; expansion and the Markov-cylinder construction imply topological mixing of the restriction. If \(0<x<\ell\), then \(T(x)=Ax+x^2/4>x\) and \(T([0,\ell])=[0,c]\). Such an orbit must cross \(\ell\) in finitely many steps: otherwise it would increase to a fixed point in \((0,\ell]\), but \(T(x)>x\) there. Any \(h<x<1\) maps into \((0,\ell)\), while points already in \([\ell,h]\) stay there. This proves finite absorption for all \(0<x<1\). Finally \(T(0)=T(1)=0\).

## Verification

The accompanying `verify.py` uses exact symbolic identities in \(\mathbb Q(\sqrt{337})\) to replay the third critical iterate, its factorization, every partition endpoint image, the admissibility inequalities, and the characteristic polynomial and primitivity of the Markov matrices. Run `python verify.py` with Python 3 and SymPy. The infinitely many orbit assertions follow from the proof above, not numerical sampling or the checker alone.

## Relationship to prior work

The 2021 original conference paper and the expanded 2023 journal paper of Paul and collaborators provide this specific self-parameterized tent formula and numerical bifurcation, Lyapunov, correlation and entropy-indicator plots; neither inspected full text gives the unique exact postcritical control or the golden-mean Markov classification. General kneading and finite-Markov interval-map entropy theory supplies the theorem used to convert the newly constructed partition into an exact entropy, but it does not supply this family's parameter computation. The exact-control classification is distinct from previously recorded attracting cycles in the self-parameterized *logistic* map and exact Markov entropy anchors for the different Lawnik–Berezowski M-map.

## Limitations

The parameter is one algebraic control in a given design interval. No global entropy-versus-control curve, invariant density, or robustness of the symbolic partition to parameter perturbation is asserted. The mixing claim concerns the invariant core, not the full interval with its fixed endpoint. The calculation does not support a claim about cryptographic security or any finite-precision implementation. Independent mathematical audit and exhaustive bibliographic priority verification have not been performed.

## References

1. P. S. Paul, A. Dhungel, M. Sadia, M. R. Hossain, B. J. Muldrey and M. S. Hasan, *Self-Parameterized Chaotic Map: A Hardware-efficient Scheme Providing Wide Chaotic Range*, IEEE ICECS 2021. Open conference full text: https://confcats-event-sessions.s3.amazonaws.com/icecs21/papers/2160.pdf .
2. P. S. Paul, A. Dhungel, M. Sadia, M. R. Hossain and M. S. Hasan, *Self-Parameterized Chaotic Map for Low-Cost Robust Chaos*, Journal of Low Power Electronics and Applications 13 (2023), article 18. https://doi.org/10.3390/jlpea13010018 .
3. L. Alsedà, J. Llibre and M. Misiurewicz, *Combinatorial Dynamics and Entropy in Dimension One*, World Scientific (2000), standard Markov-partition entropy framework.
