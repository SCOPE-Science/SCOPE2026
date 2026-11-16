# Sharp endpoint projection growth for crown-graph independent-set convolution

## Finding

For every integer \(n\ge3\), take the crown graph \(H_n=K_{n,n}\setminus M\), where \(M\) is a perfect matching, and let \(A_n\subseteq\mathbb F_2^{2n}\) consist of its independent-set incidence vectors. Write \(C_n\) for unnormalized additive convolution by \(1_{A_n}\). Its Walsh multipliers at \((u,v)\in\mathbb F_2^n\times\mathbb F_2^n\) are exactly
\[
W_n(u,v)=2^n\mathbf1_{u=0}+2^n\mathbf1_{v=0}+n-1-2|u+v|,
\]
where additions are binary and \(|\cdot|\) denotes Hamming weight.

For even \(n\), all multipliers are nonzero, \(C_n\) is invertible, its smallest absolute multiplier is \(1\), and the minimum projection norm onto its range equals \(1\). For odd \(n\), put \(m=(n-1)/2\) and \(N=2^n\). Precisely the \((N-2)\binom nm\) frequencies with \(u\ne0\), \(v\ne0\), and \(|u+v|=m\) vanish; the minimum nonzero absolute multiplier is \(2\), and
\[
\operatorname{rank}C_n=N^2-(N-2)\binom nm,
\qquad \|C_n^\dagger\|_{2\to2}=\tfrac12.
\]
The vanished-frequency fraction is asymptotic to \(\sqrt{2/(\pi n)}\) along odd lengths.

The novel endpoint result is an exact formula and a growth law for the smallest possible norm of any projection (not necessarily translation invariant) onto \(\operatorname{ran}C_n\), simultaneously in real or complex \(\ell^1\) and \(\ell^\infty\). Put
\[
K_m(t)=\sum_{j=0}^{m}(-1)^j\binom tj\binom{n-t}{m-j},\quad
B=\binom nm,\quad L=2^{m+1}B,
\]
using the convention \(\binom ab=0\) outside its range, and
\[
D=\sum_{a,b=0}^n\binom na\binom nb\big|K_m(a)+K_m(b)\big|.
\]
For odd \(n\) the sharp minimum projection norm is the explicit integer sum
\[
\boxed{\Lambda_n=1+\frac{D+(N-4)L-2(N-2)B}{N^2}.}
\]
Moreover,
\[
1+\frac{2(N-2)(L-B)}{N^2}\le\Lambda_n
\le1+\frac{3L}{N},
\]
so \(\Lambda_n=\Theta(2^{n/2}/\sqrt n)\) as odd \(n\to\infty\). Thus the convolution range has asymptotically full relative dimension while its minimum endpoint projection norm grows exponentially in half the dimension parameter.

## Assumptions and scope

The crown graph has labelled shores \(a_1,\ldots,a_n\) and \(b_1,\ldots,b_n\), and edges \(a_i b_j\) precisely when \(i\ne j\). For \(z=(x,y)\in\mathbb F_2^{2n}\), the indicator \(1_{A_n}(z)\) is \(1\) exactly when the represented vertex subset is independent. Convolution uses counting measure, \((C_nf)(z)=\sum_{w\in A_n}f(z+w)\), not probability normalization. The Fourier transform is \(\widehat f(u,v)=\sum_{x,y}f(x,y)(-1)^{u\cdot x+v\cdot y}\). Consequently the multiplier magnitudes above are eigenvalue magnitudes for convolution on counting-measure \(\ell^2\).

The projection constant is the infimum of the operator norms of **all** linear projections onto the specified range, not just orthogonal or translation-invariant projections. For finite-dimensional spaces the minimum is attained. The same formula applies over either scalar field \(\mathbb R\) or \(\mathbb C\).

## Proof

**Independent-set classification and spectral nullity.** A set meeting both shores cannot contain distinct matching indices on its two shores. Hence the independent sets consist exactly of all \((x,0)\), all \((0,y)\), and the \(n\) additional vectors \((e_i,e_i)\), with the empty set counted once. Character summation gives the stated multiplier formula. At \(u=0\ne v\), or its transpose, its value is at least \(N-1-n>0\) for \(n\ge3\); at \(u=v=0\) it equals \(2N+n-1\). At \(u,v\ne0\) it equals \(n-1-2|u+v|\). The latter is odd for even \(n\). For odd \(n=2m+1\), it vanishes exactly on the stated Hamming-distance shell. Each nonzero shell vector \(w=u+v\) has exactly \(N-2\) admissible choices for \(u\), excluding \(0\) and \(w\). This proves the nullity and rank. The displayed minima \(1\) and \(2\) are attained by selecting nonzero \(u,v\) with Hamming distance \((n-2)/2\) when \(n\) is even and \((n-3)/2\) when odd. For \(n=3\), take \(u=v\ne0\). The inverse norm is the reciprocal spectral gap. Stirling's central-binomial approximation proves the nullity fraction.

**Exact range projector.** For odd \(n\), let \(Z\) be the zero-frequency set and \(Q\) the orthogonal projection onto the Fourier characters in \(Z\). Its convolution kernel is
\[
q(x,y)=N^{-2}\left[N\mathbf1_{x=y}K_m(|y|)-K_m(|x|)-K_m(|y|)\right].
\]
To derive this, write \(w=u+v\) and sum characters over \(u\in\mathbb F_2^n\setminus\{0,w\}\). The complete \(u\)-sum is \(N\mathbf1_{x=y}\); the two omitted terms produce the last two Krawtchouk sums. Thus the range projector \(P=I-Q\) has convolution kernel \(p(x,y)=\mathbf1_{(x,y)=0}-q(x,y)\).

Every linear projection \(T\) onto this translation-invariant range can be averaged over translations without increasing its \(\ell^1\) or \(\ell^\infty\) operator norm. The averaged projection is a translation-invariant projection onto the same range; Fourier diagonalization makes it uniquely \(P\). Both endpoint norms of convolution by \(p\) equal \(\sum_{x,y}|p(x,y)|\) (choose signs on one row or column for equality). Therefore \(P\) realizes the minimum among all projections.

**Sharp formula.** Since \(q(0,0)=(N-2)B/N^2\in(0,1)\), split the absolute-kernel sum into the origin, the nonzero diagonal, and off-diagonal pairs. With \(L_*=\sum_{t=0}^n\binom nt|K_m(t)|\), their contributions respectively are \(1-(N-2)B/N^2\), \((N-2)(L_*-B)/N^2\), and \((D-2L_*)/N^2\). The Krawtchouk duality identity
\[
\binom nt K_m(t)=\binom nm K_t(m)
\]
and the generating function
\[
\sum_{t=0}^n K_t(m)z^t=(1-z)^m(1+z)^{m+1}=(1-z^2)^m(1+z)
\]
show \(K_t(m)=(-1)^{\lfloor t/2\rfloor}\binom m{\lfloor t/2\rfloor}\). In particular \(L_*=2^{m+1}B=L\), yielding the boxed norm formula.

**Exponential endpoint growth.** For uniformly random independent \(X,Y\in\mathbb F_2^n\), \(\mathbb E K_m(|Y|)=0\), since \(m>0\). Jensen's inequality gives \(D\ge NL\); the triangle inequality gives \(D\le2NL\). Substituting proves the two explicit bounds. The exact identity \(L/N=2^{-m}\binom{2m+1}m\sim (2/\sqrt\pi)2^{n/2}/\sqrt n\) then establishes \(\Theta(2^{n/2}/\sqrt n)\) along the odd integers.

## Verification

A standalone Python 3 checker `check_crown.py` independently enumerates the labelled independent sets and applies integer Walsh butterflies for every \(n=3,4,5,6,7\). It verifies all \(21,824\) multipliers, all nullity and spectral-gap formulas, the Krawtchouk duality specialization at each odd test length, and the endpoint formula against a second inverse transform of the zero-frequency indicator for \(n=3,5\). Exact sample projection constants are \(49/16\) at \(n=3\) and \(733/128\) at \(n=5\). All-length conclusions rely on the algebraic proof, not on finite tests.

## Relationship to prior work

The unsigned independence polynomial of the crown graph, \(2(1+z)^n+nz^2-1\), is already recorded in standard reference tables. It determines unweighted independent-set counts, **not** the entire signed incidence-character spectrum, its zero-set projector, or the endpoint projection constant. General Fourier methods on the Boolean cube (de Wolf, 2008) supply the underlying transform/convolution formalism. Alexander and Mink (2013 preprint) develop general independent-set enumeration but do not state the specialized spectral projection formula in the inspected passages or searchable text. Related Fourier and graph projection results on other kernels or different cut/cycle spaces do not imply this result by the same parameters. The elementary classification of crown-graph independent sets is known and is **not** claimed as new; the accepted contribution is the explicit range-projector norm and its exponential asymptotic order alongside its exact spectral nullity.

## Limitations

The precise leading asymptotic constant in \(\Lambda_n\) is not determined, only sharp exponential order and explicit finite-length values. No extension to all matching-deleted incomplete bicliques, alternate vertex weights, or \(\ell^p\) projection constants for \(1<p<\infty\) is proved. Exhaustive historical priority has not been established; a specialized multivariate hard-core projection formula could subsume these identities. No independent mathematical validation is claimed.

## References

1. Ronald de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Graduate Surveys 1 (2008), published 2008-09-25, DOI: 10.4086/toc.gs.2008.001, https://cims.nyu.edu/~regev/toc/articles/gs001/gs001.pdf.
2. James Alexander and Tim Mink, *A New Method for Enumerating Independent Sets of a Fixed Size in General Graphs*, arXiv:1308.3242, first submitted 2013-08-14, https://arxiv.org/abs/1308.3242.
3. Wolfram MathWorld, *Independence Polynomial*, crown-graph entry, https://mathworld.wolfram.com/IndependencePolynomial.html (online reference, publication date not asserted).
4. Wolfram MathWorld, *Crown Graph*, https://mathworld.wolfram.com/CrownGraph.html (online reference, publication date not asserted).
