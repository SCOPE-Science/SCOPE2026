# Nonzero central bracket fibers of finite Schrödinger Lie algebras

## Finding

Let \(q\) be an odd prime power and \(n\ge1\). In the finite Schrödinger Lie algebra \(L=\mathfrak{sch}_n(\mathbb F_q)\), write \(z\) for the standard Heisenberg central generator and set
\[
N_c=\#\{(A,B)\in L^2:[A,B]=cz\}.
\]
For **every nonzero** \(c\in\mathbb F_q\), the exact ordered-bracket fiber is
\[
\boxed{N_c=q^{2n+1}\bigl[(q^{2n}-1)+(q+1)(q^2-1)(q^n-1)\bigr].}
\]
The first term counts pairs with both \(\mathfrak{sl}_2\)-components zero; the second counts those with a nonzero commuting pair of nilpotent \(\mathfrak{sl}_2\)-components. No other \(\mathfrak{sl}_2\)-components occur in a nonzero central bracket. As a companion identity,
\[
\boxed{N_0-N_c=q^{2n+2}(q^4+q^3-q)>0.}
\]
The previously available full element-centralizer census of this same algebra already determines \(N_0\); the **new content** is \(N_c\) for nonzero central targets and the precise decomposition of the fiber through projective nilpotent directions.

## Assumptions and scope

Take \(V=(\mathbb F_q^2)^{\oplus n}\), with coordinates \((u_{x_i},u_{y_i})\) and nondegenerate alternating form
\[
\omega(u,v)=\sum_{i=1}^n(u_{x_i}v_{y_i}-u_{y_i}v_{x_i}).
\]
The action of \(\mathfrak{sl}_2(\mathbb F_q)\) on \(V\) is diagonal and standard. Set \(L=\mathfrak{sl}_2(\mathbb F_q)\oplus V\oplus\mathbb F_q z\) and use the bracket
\[
[(X,u,a),(Y,v,b)]=([X,Y],Xv-Yu,\omega(u,v)z).
\]
Here \(a,b\in\mathbb F_q\) are unconstrained central coordinates. This is the standard convention \([x_i,y_j]=\delta_{ij}z\). The count concerns **ordered** element pairs, includes pairs with zero entries, and is only claimed for odd characteristic. It does not determine the off-center bracket fibers.

## Proof

**1. Separate the Lie-algebra components.** A bracket equals \(cz\) precisely when \([X,Y]=0\), \(Xv-Yu=0\), and \(\omega(u,v)=c\). The central coordinates \(a,b\) are arbitrary, contributing a factor \(q^2\).

**2. The zero-\(\mathfrak{sl}_2\) case.** If \(X=Y=0\) and \(c\ne0\), then \(u\ne0\). There are \(q^{2n}-1\) possibilities for \(u\), and nondegeneracy of \(\omega\) gives exactly \(q^{2n-1}\) solutions \(v\) to \(\omega(u,v)=c\). This contributes \(q^2(q^{2n}-1)q^{2n-1}\).

**3. All other commuting pairs have a common direction.** For odd characteristic, the centralizer of each nonzero \(X\in\mathfrak{sl}_2(\mathbb F_q)\) **inside** \(\mathfrak{sl}_2\) is the one-dimensional span of \(X\). This follows directly by solving \([X,Y]=0\), or from the fact that the full matrix centralizer is \(\mathbb F_q I\oplus\mathbb F_q X\), whose trace-zero part is \(\mathbb F_qX\). Thus any commuting pair \((X,Y)\ne(0,0)\) has a unique projective line \(\langle T\rangle\) and a unique coefficient pair \((\alpha,\beta)\in\mathbb F_q^2\setminus\{(0,0)\}\) after a fixed representative \(T\ne0\) is chosen: \(X=\alpha T\), \(Y=\beta T\).

Choose \(r,s\in\mathbb F_q\) with \(r\alpha+s\beta=1\), and define
\[
w=\alpha v-\beta u,\qquad t=ru+sv.
\]
The change \((u,v)\mapsto(t,w)\) is invertible and has determinant one in the two copy coordinates. Therefore \(\omega(t,w)=\omega(u,v)\). The remaining equations become \(Tw=0\) and \(\omega(t,w)=c\). When \(c\ne0\), necessarily \(w\ne0\). For each \(w\in\ker(T|_V)\setminus\{0\}\), there are precisely \(q^{2n-1}\) choices of \(t\). Hence the fiber contribution per fixed nonzero coefficient pair is \((|\ker(T|_V)|-1)q^{2n-1}\).

**4. Only nilpotent lines contribute.** For a nonzero trace-zero \(2\times2\) matrix \(T\) in odd characteristic, either \(\det T\ne0\), when \(\ker(T|_V)=0\), or \(\det T=0\), when \(T\) is rank-one nilpotent and \(|\ker(T|_V)|=q^n\). There are \(q^2-1\) nonzero nilpotent matrices: writing \(T=\begin{psmallmatrix}a&b\\c&-a\end{psmallmatrix}\), their equation is \(a^2+bc=0\); counting over \(a,b,c\) yields \(q^2\) solutions including zero. Thus the projective nilpotent cone consists of \((q^2-1)/(q-1)=q+1\) lines. Each line contributes \(q^2-1\) nonzero coefficient pairs. Including the free \(a,b\) central coordinates gives the nonzero-\(\mathfrak{sl}_2\) contribution
\[
q^2(q+1)(q^2-1)(q^n-1)q^{2n-1}.
\]
Adding Step 2 proves the boxed nonzero-fiber formula.

**5. Exact zero-fiber excess.** Repeat the same count with target \(c=0\). For each nonzero \(w\), the symplectic equation has exactly \(q^{2n-1}\) solutions for **every** prescribed scalar; hence these contributions cancel in \(N_0-N_c\). The extra zero solutions arise exactly from \(u=0\) in Step 2 or \(w=0\) in Step 3, and number \(q^{2n}\) per commuting ordered pair \((X,Y)\) in \(\mathfrak{sl}_2\), before the factor \(q^2\). There are
\[
q^3+(q^3-1)q=q^4+q^3-q
\]
commuting ordered pairs in \(\mathfrak{sl}_2(\mathbb F_q)\) because every nonzero element has a \(q\)-element centralizer. Multiplication gives the second boxed formula. This completes the proof.

## Verification

The standalone program `verify_central_fibers.py` independently enumerates \(\mathfrak{sl}_2\)-components, \(V\)-components and bracket equations from the displayed basis structure constants. It checks the complete central fiber for \((q,n)=(3,1),(3,2),(5,1)\), with expected scalar-count lists respectively \((10449,1944,1944)\), \((158193,81648,81648)\), and \((540625,75000,75000,75000,75000)\). These exact finite tests are consistency checks, not a substitute for the proof for arbitrary \(q,n\).

## Relationship to prior work

Sosnov's November 12, 2026 preprint [1] defines the same Schrödinger Lie algebra, proves a criterion for bracket width one in terms of sums of squares, and investigates uniqueness of addition. It does not provide the number of ordered presentations of a prescribed nonzero central bracket. An earlier centralizer-rank census for this same family determines the **zero** bracket fiber (commuting probability) but does not determine nonzero central fibers; that prior component is credited, not claimed as new. Fulman and Guralnick [2] enumerate commuting pairs in several classical Lie algebras, rather than prescribed nonzero central fibers in these semidirect Heisenberg extensions. Published results on Takiff and mirabolic Lie-algebra bracket fibers concern different Lie algebras and do not furnish the formula here without a new transfer argument. These comparisons limit, but do not eliminate, unindexed historical priority risks.

## Limitations

The result is confined to odd-characteristic finite fields, central bracket targets, and the stated normalization of the Heisenberg generator. It does not give full off-central fiber distributions, extension to characteristic two, or a classification of all Lie-algebra commutator maps. Independent audit has not been performed. Literature indexing cannot certify absolute historical priority.

## References

[1] G. Sosnov, *Uniqueness of addition in Schrödinger algebras*, arXiv:2611.16812v1 (first public version November 12, 2026), https://arxiv.org/html/2611.16812v1.

[2] J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499 (2016), https://arxiv.org/abs/1611.05499.
