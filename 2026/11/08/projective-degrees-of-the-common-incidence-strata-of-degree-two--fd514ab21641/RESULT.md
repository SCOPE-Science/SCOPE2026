# Projective degrees of the common incidence strata of degree-two Chow varieties

## Finding
Let \(n\ge 3\) and \(1\le p\le n-2\). In the standard Chow-form projective embedding over \(\mathbb C\), let \(Q_{p,n}\) and \(R_{p,n}\) be the reduced irreducible components of \(C_{p,2}(\mathbb P^n)\) consisting respectively of quadric cycles and unordered sums of two linear \(p\)-planes. Let
\[
 Z_{p,n}=(Q_{p,n}\cap R_{p,n})_{\mathrm{red}}.
\]
Then \(Z_{p,n}\) is exactly the irreducible variety of unordered pairs \(\{E_1,E_2\}\) of \(p\)-planes with \(\dim\langle E_1,E_2\rangle\le p+1\), and
\[
 \dim Z_{p,n}=(p+2)(n-p-1)+2p+2.
\]
For \(r=p+2\), \(N=n+1\), \(b=r(N-r)\), \(D=b+2r-2\), and every \(r\)-element subset \(I\subseteq\{0,1,\ldots,n\}\), put
\[
 T_I=\sum_{a\in I}a,\qquad
 \Delta_I=\prod_{a\in I,\,z\notin I}(z-a),\qquad
 h_{I,j}=[t^j]\prod_{a\in I}(1-at)^{-1}.
\]
(The coefficient convention includes \(h_{I,0}=1\) and \(0^0=1\).) Its **projective degree** is the following explicit, finite, rational-arithmetic expression, which is always a positive integer:
\[
 \boxed{\displaystyle
 \deg Z_{p,n}={1\over2}\sum_{|I|=r}{1\over\Delta_I}
 \sum_{\substack{i,j\ge0\\i+j\le b}}
 {D!\,h_{I,i}h_{I,j}(-2T_I)^{b-i-j}
 \over (r-1+i)!(r-1+j)!(b-i-j)!}.}
\]
The degrees obey the Plücker-duality symmetry
\[
 \boxed{\deg Z_{p,n}=\deg Z_{n-p-1,n}.}
\]
In the line-pair case \(p=1\), put \(a=n-1\), \(c=a-1\), and
\[
 J_i=\binom{2a-i}{a-i}-\binom{2a-i}{a+1}
 \quad(0\le i\le c),
\]
where an out-of-range binomial coefficient is zero. Then the degree has the further binomial-only formula
\[
 \boxed{\displaystyle
 \deg Z_{1,n}={1\over2}\sum_{i=0}^{a-1}
 \binom{3a+1}{2a-i}J_iJ_{a-1-i}.}
\]
Exact values include
\[
\begin{array}{c|r}
(p,n)&\deg Z_{p,n}\\\hline
(1,3)&140\\
(1,4),(2,4)&6300\\
(1,5),(3,5)&288288\\
(2,5)&4036032\\
(1,6)&13453440\\
(2,6),(3,6)&2744501760
\end{array}
\]

## Assumptions and scope
All varieties are reduced complex projective varieties, and degrees use the ambient \(\mathcal O(1)\) from the degree-two Chow-form embedding. A linear \(p\)-plane is the projectivization of a \((p+1)\)-dimensional vector subspace. The intersection \(Z_{p,n}\) is the **reduced common support** of the two Chow components; the theorem makes no assertion about the nilpotent structure or intersection multiplicity of their scheme-theoretic intersection. The parameter restrictions ensure that the quadric and pair components are distinct and both exist.

## Proof
**1. Support and dimension.** Every degree-two irreducible \(p\)-cycle is a quadric hypersurface in a linear \((p+1)\)-plane. If a degree-two cycle is also a sum of linear \(p\)-planes, its two summands must lie in such a \((p+1)\)-plane. Conversely, two hyperplanes in that \((p+1)\)-plane define a reducible quadric and hence belong to both closures. Equal summands also arise as a limit. Thus \(Z_{p,n}\) is the asserted incidence locus.

Let \(T=\operatorname{Gr}(r,\mathbb C^N)\), \(S\) its tautological rank-\(r\) bundle, and \(P=\mathbb P(S^\vee)\), with the convention that \(P\) parameterizes lines of \(S^\vee\). The smooth irreducible incidence space \(\widetilde B=P\times_TP\) parametrizes ordered pairs of hyperplanes in a common \(r\)-space. For a generic pair of *distinct* hyperplanes, their span is the unique \(r\)-space containing them. Forgetting that span and ordering therefore gives a generically finite morphism \(\widetilde B\to Z_{p,n}\) of degree exactly two. Its dimension is
\[
 \dim\widetilde B=r(N-r)+2(r-1)=D,
\]
and the same holds for its image. In particular, \(Z_{p,n}\) is irreducible. The codimensions in the two components are respectively \(p(p+1)/2\) in \(Q_{p,n}\) and \(p(n-p-1)\) in \(R_{p,n}\).

**2. The actual Chow polarization.** Write \(x,y\) for the first Chern classes of the tautological quotient lines \(S/E_1,S/E_2\) on \(\widetilde B\), equivalently the pullbacks of \(c_1(\mathcal O_P(1))\). Put \(c_1=c_1(S)\). The Plücker hyperplane class of the individual \((p+1)\)-subspace \(E_i\) is
\[
 c_1(\det E_i^\vee)=x_i-c_1,
\]
by the exact sequence \(0\to E_i\to S\to S/E_i\to0\). Chow forms multiply when cycles are added; the Chow hyperplane class pulled back to the *ordered* pair incidence space is therefore
\[
 H=(x-c_1)+(y-c_1)=x+y-2c_1.
\]
This twist matters: the relative hyperplane class of the projective bundle of quadratic forms is only \(x+y\), not the Chow polarization. The degree-two generic mapping degree then gives
\[
 \boxed{\quad 2\deg Z_{p,n}=\int_{\widetilde B}(x+y-2c_1)^D.\quad}
\]

**3. Finite evaluation.** For projectivization by lines, the projective-bundle pushforward identity is
\[
 \pi_*(x^{r-1+i})=s_i(S^\vee),\qquad i\ge0,
\]
with negative indices giving zero. Expanding the \(D\)-th power and pushing successively from the two projective bundles yields
\[
 2\deg Z_{p,n}=\int_T
 \sum_{i+j\le b}
 {D!\over(r-1+i)!(r-1+j)!(b-i-j)!}
 s_i(S^\vee)s_j(S^\vee)(-2c_1)^{b-i-j}.
\]
For the coordinate torus with pairwise distinct integer weights \(0,1,\ldots,n\), the fixed points of \(T\) are indexed by the \(r\)-subsets \(I\). At \(I\), the roots of \(S\) are the weights \(a\in I\), so \(s_i(S^\vee)\) evaluates to \(h_{I,i}\), \(c_1\) to \(T_I\), and the equivariant Euler class of \(T_T\) to \(\Delta_I\). Equivariant localization gives exactly the finite formula. Because the left-hand side is twice a projective degree, all cancellations are exact and the result is a positive integer.

**4. Duality.** The annihilator map \(E\mapsto E^\perp\) sends \(\operatorname{Gr}(p+1,\mathbb C^{n+1})\) to \(\operatorname{Gr}(n-p,(\mathbb C^{n+1})^\vee)\). Two distinct \(E_i\) span a \((p+2)\)-space precisely when their annihilators meet in codimension one in each. This identifies the two incidence loci for indices \(p\) and \(n-p-1\). On Plücker coordinate spaces it is induced by a linear duality after choosing a volume form. Taking the symmetric products preserves the sum of Plücker hyperplane classes, hence preserves the Chow-form projective degree. This proves the symmetry.

**5. The line-pair formula.** For \(p=1\), the incidence of meeting lines in \(\operatorname{Gr}(2,n+1)^2\) is the expected-codimension \((n-2)\) degeneracy locus of \(E_1\oplus E_2\to\mathbb C^{n+1}\) of rank at most three. Thom--Porteous gives its fundamental class as
\[
 \sum_{i=0}^{n-2}\sigma_i(E_1)\sigma_{n-2-i}(E_2),
\]
where \(\sigma_i=c_i(\mathbb C^{n+1}-E)\) is the special Schubert class. Put \(a=n-1\). The Grassmannian \(\operatorname{Gr}(2,n+1)\) has dimension \(2a\), and Pieri's rule together with the reflection principle for two-row Young tableaux gives
\[
 \int_{\operatorname{Gr}(2,n+1)}\sigma_1^{2a-i}\sigma_i
 =\binom{2a-i}{a-i}-\binom{2a-i}{a+1}=J_i.
\]
The power of \(H=H_1+H_2\) required by the degree is \(3a+1\). Expanding it, integrating termwise, and dividing by two for unordered pairs gives the stated finite binomial sum.

## Verification
The included standard-library program `CHECK.py` computes the first incidence-bundle expression by exact rational equivariant localization. Independently it computes a *different* Grassmannian-square integral: the Thom--Porteous class of the rank degeneracy locus of \(E_1\oplus E_2\to\mathbb C^N\) multiplied by the Chow polarization \((H_1+H_2)^D\). It checks their agreement for all \(n=3,4,5,6,7\) and \(1\le p\le n-2\), compares the line-pair binomial formula, and checks duality. The program returns `TWO_INDEPENDENT_INTERSECTION_DEGREE_FORMULAS_OK 15`, `DUALITY_AND_LINE_PAIR_BINOMIAL_FORMULAS_OK`, `CHECK_OK`. The finite computation is corroborative: Steps 1--5 are the proof for all allowed \((p,n)\).

## Relationship to prior work
Chen, Hu and Ma (2026, arXiv:2610.39498), especially §§3--4, describe the quadric and pair parameter spaces and their incidence correspondence, and compute cohomological information. Their parameter-space hyperplane identity \(j^*\mathcal O_{\mathbb P(\mathrm{Sym}^2S^\vee)}(1)=x+y\) concerns the *relative quadratic-form* polarization. The present exact projective intersection degrees require the actual Chow twist \(x+y-2c_1(S)\) and evaluation of the top intersection for every \((p,n)\). The degree of the intersection locus is not determined by the degrees of the individual irreducible components alone.

Bürgisser, Kohn, Lairez and Sturmfels (2015, arXiv:1508.07219) compute defining ideals and component degrees in the \((p,n)=(1,3)\) case, including the pair component degree \(140\). The equality \(\deg Z_{1,3}=140\) is consistent with their calculation but does not assert their component-degree result as new. The general support description of the intersection is classical; novelty is claimed only for the *evaluated projective degree formulas* for the reduced common stratum, the binomial specialization, and the uniform numerical classification, not for the incidence parameterization or standard projective-bundle and Thom--Porteous tools.

## Limitations
This result does not compute the scheme-theoretic intersection ideal or nonreduced intersection multiplicities, Hilbert polynomials, singularities, or projective degrees of higher-degree cycle spaces. The formulas use the standard Chow-form embedding; another embedding changes the numerical degrees. Exact calculations in a finite range cannot establish historical novelty for arbitrary parameters; specialized older Schubert-calculus tables may deserve further comparison.

## References
1. Y. Chen, W. Hu, D. Ma, *Poincaré series of degree-two Chow varieties*, arXiv:2610.39498v1 (first submitted 2026-10-29), https://arxiv.org/abs/2610.39498.
2. P. Bürgisser, K. Kohn, P. Lairez, B. Sturmfels, *Computing the Chow Variety of Quadratic Space Curves*, arXiv:1508.07219v2 (2015), https://arxiv.org/abs/1508.07219.
3. W. Fulton, *Intersection Theory*, second edition (1998), for projective-bundle pushforward and Thom--Porteous formulas.
4. W. Fulton, *Young Tableaux* (1997), for the Grassmannian Pieri rule and tableaux interpretations.
