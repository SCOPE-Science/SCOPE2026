# Exact logarithmic covering law for irrational contracted-rotation Cantor attractors

## Finding

Let \(0<\lambda<1\), let \(\theta\in(0,1)\) be irrational, and let \(\delta=\delta(\lambda,\theta)\) be the unique translation for which the contracted rotation \(f(x)=\{\lambda x+\delta\}\) has rotation number \(\theta\). If \(K\subset[0,1]\) is the closure of its limiting Cantor attractor and \(N_K(r)\) is the minimum number of *closed intervals of diameter at most* \(r\) covering \(K\), then
\[
\boxed{N_K(r)=\frac{\log(1/r)}{\log(1/\lambda)}+O_{\lambda}(1)\quad (r\downarrow0).}
\]
The leading coefficient is independent of the irrational rotation number. Thus the ordinary box dimension is zero, but the exact logarithmic covering scale is nonzero. The bounded remainder is uniform in \(\theta\) when \(\lambda\) is fixed.

## Assumptions and scope

Take \(0<\lambda<1\), \(0<\theta<1\) irrational, and
\[
\delta=(1-\lambda)\left(1+\sum_{k\ge1}\big(\lfloor(k+1)\theta\rfloor-\lfloor k\theta\rfloor\big)\lambda^k\right).
\]
Then \(1-\lambda<\delta<1\). Write \(c=(1-\delta)/\lambda\in(0,1)\). On \([0,1]\) the two affine branches are \(x\mapsto\lambda x+\delta\) for \(0\le x<c\) and \(x\mapsto\lambda x+\delta-1\) for \(c\le x\le1\). The discontinuity itself is immaterial to the compact limiting set: use one-sided closed images and take the intersection of their iterated unions. The result concerns the Euclidean metric on \([0,1]\); the circle metric is not being used.

## Proof

**1. Atom count.** For every admissible branch word of length \(n\), let its generation-\(n\) image atom be the closure of the set of endpoints reached after that ordered itinerary. This is a nonempty closed interval of length at most \(\lambda^n\). The separation property makes distinct atoms disjoint. The irrational contracted rotation has one Cantor minimal component, with Sturmian itinerary language: the number of admissible words of length \(n\) is precisely \(n+1\). Every such word recurs on the minimal Cantor component, hence each corresponding atom meets \(K\). Equivalently, the atom-to-itinerary assertion is Lemma 4.1 of Calderón–Villar-Sepúlveda (2023), combined with the Sturmian factor complexity. Consequently, exactly \(n+1\) generation-\(n\) atoms meet and cover \(K\).

**2. Uniform gap.** The images of the two entire branches have closed hulls \([\delta,1]\) and \([0,\lambda+\delta-1]\); their separation is exactly \(g=1-\lambda>0\). Consider two distinct length-\(n\) image atoms. If their final branch symbols differ, their distance is at least \(g\). If those symbols agree, each is the image under the same increasing similarity of ratio \(\lambda\) of a subset of distinct preceding atoms. Thus the distance is at least \(\lambda\) times the preceding separation. Induction from length one proves that the distance between any two distinct generation-\(n\) atoms is at least \(g\lambda^{n-1}\). Restriction to a branch cannot decrease the separation of two disjoint intervals before applying the common affine similarity.

**3. Two-sided covering bounds.** Since all \(n+1\) atoms have diameter at most \(\lambda^n\),
\[
N_K(r)\le n+1\quad\text{whenever }r\ge\lambda^n.
\]
Since each meets \(K\) and distinct atoms are separated by at least \(g\lambda^{n-1}\), one interval of diameter \(r<g\lambda^{n-1}\) cannot meet two of them; hence
\[
N_K(r)\ge n+1\quad\text{whenever }0<r<g\lambda^{n-1}.
\]
Let \(L=\log(1/\lambda)>0\), \(t=\log(1/r)/L\). Choosing integer levels within a bounded distance of \(t\) in these inequalities gives \(t-O_\lambda(1)\le N_K(r)\le t+O_\lambda(1)\). This proves the stated asymptotic, including independence of \(\theta\).

## Verification

The analytic proof applies to every irrational \(\theta\) and every \(0<\lambda<1\); no finite experiment is used as proof of that statement. The accompanying `CHECKER.py` reconstructs the canonical golden-rotation example with \(\lambda=1/2\), using high-precision decimal arithmetic and the published Sturmian translation series. For generations \(1\) through \(18\) it checks \(n+1\) nonempty atoms, diameters at most \(\lambda^n\), and inter-atom gaps at least \((1-\lambda)\lambda^{n-1}\). Finite checks are consistency evidence only.

## Relationship to prior work

Bugeaud–Kim–Laurent–Nogueira (2020) define this family, give the unique-translation Sturmian series, and study Diophantine properties of the Cantor sets. Calderón–Villar-Sepúlveda (2023) prove that injective piecewise-contracting attractors have zero Hausdorff and lower box dimensions, providing an upper covering estimate through itinerary complexity. Their Lemma 4.1 supplies the atom/word correspondence. The present result combines those ingredients with a *matching, uniform geometric separation lower bound*, yielding a sharp logarithmic covering law rather than merely vanishing box dimension. No precedence claim is made beyond the sources checked.

## Limitations

This is not a positive box dimension or positive-dimensional Hausdorff-gauge theorem. The estimate is additive \(O_\lambda(1)\), and does not assert existence of a constant term. It applies only to irrational rotation parameters in this affine two-branch family, not to arbitrary injective piecewise contractions, rational mode-locked parameters, or more general Cantor attractors. Equivalent calculations could exist in unindexed literature.

## References

1. A. E. Calderón and E. Villar-Sepúlveda, *Piecewise contracting maps on the interval: Hausdorff dimension, entropy and attractors*, arXiv:2309.09154v1 (first public 2023-09-17), esp. Lemmas 3.2, 3.3, 4.1 and Theorem 4.5; https://arxiv.org/pdf/2309.09154.
2. Y. Bugeaud, D. H. Kim, M. Laurent and A. Nogueira, *On the Diophantine nature of the elements of Cantor sets arising in the dynamics of contracted rotations*, arXiv:2001.00380v1 (2020), esp. Section 1 and the Sturmian coding; https://arxiv.org/pdf/2001.00380.
3. M. Laurent and A. Nogueira, *Rotation number of contracted rotations*, Journal of Modern Dynamics 12 (2018), 175–191, doi:10.3934/jmd.2018007. Checked abstract and reference list; full text not independently examined.
