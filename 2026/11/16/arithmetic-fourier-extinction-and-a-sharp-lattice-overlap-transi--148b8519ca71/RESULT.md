# Arithmetic Fourier extinction and a sharp lattice-overlap transition for clipped squares

## Finding

Let \(0<a<1\) and define the centrally symmetric octagon
\[
P_a=\{(x,y)\in\mathbb R^2:|x|\le1,\ |y|\le1,\ |x|+|y|\le2-a\}.
\]
For integers \(m,n\), let \(F_a(m,n)=\int_{P_a}\exp[-2\pi i(mx+ny)]\,dx\,dy\). The complete integer-frequency Fourier transform is
\[
F_a(m,n)=\begin{cases}
4-2a^2,&(m,n)=(0,0),\\[1mm]
\dfrac{\cos(2\pi am)-\cos(2\pi an)}{\pi^2(m^2-n^2)},&m^2\ne n^2,\\[2mm]
-\dfrac{a\sin(2\pi am)}{\pi m},&m^2=n^2,\ m\ne0.
\end{cases}
\]
Consequently, for \((m,n)\ne(0,0)\), the coefficient vanishes exactly when
\[
\big[m^2\ne n^2\ \text{ and }\ a(m-n)\in\mathbb Z\ \text{or}\ a(m+n)\in\mathbb Z\big]
\quad\text{or}\quad
\big[m^2=n^2\ \text{ and }\ 2am\in\mathbb Z\big].
\]
Here the first bracket means \(m^2\ne n^2\) and at least one of the two divisibility conditions. In particular, **for irrational \(a\) every integer-frequency Fourier coefficient is nonzero**, while for \(a=p/q\) in lowest terms, \(1\le p<q\), \(q\ge2\), the zero criterion is
\[
m^2\ne n^2:\ q\mid(m-n)\ \text{or}\ q\mid(m+n),
\qquad m^2=n^2\ne0:\ q\mid2m.
\]
The exceptions on both diagonals are essential. The limiting proportion of nonzero integer Fourier coefficients in centered frequency squares is
\[
\lim_{M\to\infty}\frac{\#\{(m,n)\in[-M,M]^2\cap\mathbb Z^2:F_a(m,n)\ne0\}}{(2M+1)^2}
=1-\frac2q+\frac{\gcd(q,2)}{q^2}
\]
for rational \(a=p/q\), and equals \(1\) for irrational \(a\). All rational numerators with the same reduced denominator have the same Fourier zero set. Thus the nonzero integer frequencies are pairwise nonorthogonal as exponentials in \(L^2(P_a)\) for irrational \(a\); for rational \(a=p/q\), the infinite family of frequencies \(q\mathbb Z^2\) is pairwise orthogonal.

Define the integer-lattice translate coverage \(W_a(x)=\sum_{k\in\mathbb Z^2}\mathbf1_{P_a}(x+k)\). For Lebesgue-almost every \(x\) in \([0,1)^2\), \(W_a\in\{2,3,4\}\), and the exact proportions are, with \(h=(a-\tfrac12)_+=\max(a-\tfrac12,0)\),
\[
\Pr(W_a=2)=4h^2,\quad
\Pr(W_a=3)=2a^2-8h^2,\quad
\Pr(W_a=4)=1-2a^2+4h^2.
\]
In particular, double coverage first occupies positive area **exactly when \(a>1/2\)**. The associated exact global lattice Fourier-energy identity is
\[
\boxed{\sum_{(m,n)\in\mathbb Z^2\setminus\{(0,0)\}}|F_a(m,n)|^2
=2a^2-4a^4+8\left(a-\tfrac12\right)_+^2.}
\]
This makes the critical overlap transition visible as a second-derivative jump of the total nonconstant Fourier energy.

## Assumptions and scope

All area integrals use Lebesgue measure; Fourier frequencies are integer vectors and the exponential normalization is \(\exp(-2\pi i\,\cdot)\). The boundaries of polygons and triangles are ignored when counting coverage because they have zero area. The parameter satisfies \(0<a<1\), so all eight sides are nondegenerate. No claim concerns the entire real-frequency zero set, nor all possible non-integer exponential orthogonal systems. For an irrational number the statement concerns **integer-frequency** orthogonality only. Reduced rational denominators are at least two.

For a fully explicit finite zero count, put \(N_r(M)=\#\{j\in\mathbb Z:-M\le j\le M,\ j\equiv r\pmod q\}\) for \(r\in\mathbb Z/q\mathbb Z\), and \(g=\gcd(2,q)\). The number of **zero** Fourier coefficients in \([-M,M]^2\cap\mathbb Z^2\), for any integer \(M\ge0\) and rational \(a=p/q\), equals
\[
\sum_{r\bmod q}N_r(M)^2
+\sum_{r\bmod q}N_r(M)N_{-r}(M)
-\sum_{\substack{r\bmod q\\2r\equiv0\ (\mathrm{mod}\ q)}}N_r(M)^2
-1-4\left(M-\left\lfloor\frac{M}{q/g}\right\rfloor\right).
\]
The last two terms remove the origin and the apparent congruence zeros on the two exceptional diagonals.

## Proof

**1. Corner-triangle Fourier identity.** Removing the four corner triangles of side length \(a\) from \([-1,1]^2\) produces \(P_a\). The square's Fourier coefficient is zero for every nonzero integer pair. Use inward corner coordinates \((u,v)\) with \(u,v\ge0\) and \(u+v\le a\). Summing their four exponential integrands gives \(4\cos(2\pi m u)\cos(2\pi n v)\). Therefore, for nonzero integer frequencies,
\[
F_a(m,n)=-4\int_0^a\int_0^{a-u}\cos(2\pi mu)\cos(2\pi nv)\,dv\,du.
\]
Integration in \(v\) followed by product-to-sum identities, with a continuous limit when \(m^2=n^2\), gives precisely the displayed trigonometric formula. In the diagonal case the integral equals \(a\sin(2\pi am)/(4\pi m)\). The origin coefficient is area \(4-4(a^2/2)=4-2a^2\).

**2. Exact arithmetic zero set.** When \(m^2\ne n^2\), the denominator is nonzero, so the coefficient vanishes exactly if \(\cos(2\pi am)=\cos(2\pi an)\). The identity \(\cos(2\pi x)=\cos(2\pi y)\iff x-y\in\mathbb Z\) or \(x+y\in\mathbb Z\) yields the two congruence alternatives. For \(m^2=n^2\ne0\), direct use of the diagonal formula instead gives \(2am\in\mathbb Z\). If \(a\) is irrational all these relations are impossible at nonzero integer frequencies. If \(a=p/q\) in lowest terms, they are exactly the stated divisibility alternatives. The inner product of two integer exponentials is the Fourier coefficient at the frequency difference (up to conjugation); hence the pairwise orthogonality dichotomy follows. For rational \(a=p/q\), all differences inside \(q\mathbb Z^2\) satisfy the true zero criterion, including those on the diagonals.

**3. Frequency counts.** Off the two diagonals, the rational zero set is the union of residue lines \(m-n\equiv0\pmod q\) and \(m+n\equiv0\pmod q\). Their intersection consists of \(m\equiv r,\ n\equiv r\) with \(2r\equiv0\pmod q\). Inclusion-exclusion on \([-M,M]^2\) gives the three sums in the finite count. The origin is not a zero, hence subtract one. On either diagonal, there are \(2M-2\lfloor M/(q/g)\rfloor\) nonzero integer coordinates that would have been falsely counted as zeros; subtract this number for each diagonal. This proves the displayed exact count. Each residue class has \((2M+1)/q+O(1)\) representatives, so the congruence union has density \((2q-g)/q^2\) while the diagonal corrections are \(O(M)\). Taking complements yields the asserted positive-coefficient density.

**4. Exact lattice-coverage distribution.** On the unit square in coordinates \((x,y)\in(0,1)^2\), the original square \([-1,1]^2\) has coverage exactly four. The four removed-corner regions project to four right triangles given by
\[
x+y<a,\qquad x+y>2-a,\qquad y-x>1-a,\qquad x-y>1-a.
\]
Each has area \(a^2/2\). Opposite triangles have disjoint interiors since \(a<1\), and every adjacent pair overlaps precisely when \(a>1/2\), in an area-\((a-1/2)^2\) triangle; there are exactly four adjacent pairs. No triple overlap is possible. If \(X\) is the number of removed triangles covering a uniform point in the unit square, then \(X\in\{0,1,2\}\), \(W_a=4-X\), \(\mathbb E X=2a^2\), and \(\Pr(X=2)=4(a-1/2)_+^2\). Solving for all three probabilities gives the coverage law.

**5. Parseval and the sharp transition.** The periodization \(W_a\) is in \(L^2([0,1)^2)\) and its Fourier coefficients are exactly \(F_a(m,n)\) at every integer frequency. Hence Parseval gives
\[
\sum_{(m,n)\ne(0,0)}|F_a(m,n)|^2
=\int_{[0,1)^2}|W_a-\mathbb EW_a|^2
=\operatorname{Var}(X).
\]
The triangle count has \(\mathbb EX=2a^2\) and \(\mathbb EX^2=2a^2+8(a-1/2)_+^2\). Subtracting \((\mathbb EX)^2\) proves the claimed Fourier-energy identity. Below \(a=1/2\), the positive-part term is zero; above it, the second derivative increases by \(16\), proving the sharp non-smooth phase transition.

## Verification

Run `python3 verify.py` with the standard Python library. The package checker tests the exact rational zero count for 252 pairs of denominators and frequency cutoffs, compares the rational zero criterion with the trigonometric coefficients at 20,519 instances, separately approximates twelve triangle Fourier integrals, checks occupancy proportions at four apertures, and compares partial Parseval sums to the closed total energy at two apertures. These finite computations corroborate, but do not replace, the complete elementary proof above.

## Relationship to prior work

Lev and Liu's 2019 work (arXiv:1902.00876, first posted February 3, 2019; original primary Fourier-analysis classification 42B10) develops the relation between spectral polytopes and translation equidecomposability, with a Stokes-type Fourier expansion. Liu's 2018 work (arXiv:1809.03440) treats general periodic and multiple planar translational tilings. Diaz–Le–Robins (arXiv:1602.08593) provides a broad combinatorial-Stokes algorithm for Fourier transforms of polytopes. General Fourier integration, integer-lattice Parseval, and translate/zero duality are background and not claimed as new. The distinct specific contribution is the **joint complete rational/irrational integer-frequency extinction law, exact finite support counts, and the coupled sharp occupancy/energy transition for this entire continuously varying octagonal family**. The inspected general theorems do not give these classifications as stated.

## Limitations

Historical priority is provisional: a disguised equivalent example in polygonal diffraction, elementary Fourier-integral tables, or tiling/covariogram literature might cover some or all of the explicit formulas. The theorem concerns only the integer lattice and this one-parameter geometric family; it does not assert a classification of arbitrary orthogonal frequencies, global spectrality, or optimal lattice coverings. The cutoff arithmetic is independent of the numerator only for the zero set, not the nonzero Fourier coefficient values. Endpoints \(a=0,1\) are excluded because the octagon degenerates. The support-density limits are asymptotic; finite boxes use the displayed exact correction formula.

## References

1. N. Lev and B. Liu, *Spectrality of polytopes and equidecomposability by translations*, arXiv:1902.00876, first posted 2019-02-03, https://arxiv.org/abs/1902.00876 .
2. B. Liu, *Periodic structure of translational multi-tilings in the plane*, arXiv:1809.03440, first posted 2018-09-10, https://arxiv.org/abs/1809.03440 .
3. R. Diaz, Q.-N. Le, and S. Robins, *Fourier transforms of polytopes, solid angle sums, and discrete volume*, arXiv:1602.08593, first posted 2016-02-27, https://arxiv.org/abs/1602.08593 .
