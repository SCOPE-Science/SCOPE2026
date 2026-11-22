# Sharp periodic \(BV\)-to-\(L^2\) error of box-averaged hat interpolation

## Finding
For each integer \(N\ge6\), set \(h=1/N\) on the unit circle \(\mathbb T=\mathbb R/\mathbb Z\), and let \(\varphi(u)=\max(1-|u|,0)\). Define the centered box-averaged, periodic linear-hat quasi-interpolant
\[
(P_N f)(x)=\sum_{k=0}^{N-1}\left(\frac1h\int_{kh-h/2}^{kh+h/2}f(y)\,dy\right)\sum_{m\in\mathbb Z}\varphi(Nx-k-mN),
\]
where the integral is periodic. For every real \(f\in BV(\mathbb T)\), with full circular variation \(V(f)=|Df|(\mathbb T)\),
\[
\boxed{\|f-P_Nf\|_{L^2(\mathbb T)}^2\le\frac{3}{28N}\,V(f)^2.}
\]
The constant is sharp. Apart from nonzero scaling and addition of constants, **all** nonconstant equality functions are the indicators of the open circular arcs
\[
\boxed{\left(\frac{k+1/14}{N},\frac{k+13/14}{N}\right),\qquad k=0,\ldots,N-1.}
\]
Their complementary arcs represent the same equality functions under scaling and addition of constants. Thus the worst jump pair lies strictly inside a single mesh cell, at phase offsets \(1/14\) and \(13/14\), not at knots or cell midpoints. The inequality and extremizer classification hold simultaneously for every \(N\ge6\).

## Assumptions and scope
The circle has Lebesgue measure one; values on sets of measure zero are immaterial. Variation is the total mass of the distributional derivative on the circle, so a nontrivial arc indicator has variation exactly two. The reconstruction averages over a *full cell-width* centered box at each knot and then uses the periodic cardinal hats. It preserves constants, is positive, and is not the \(L^2\)-orthogonal projector onto linear splines. The bound concerns real-valued inputs and the ordinary unweighted \(L^2\) norm. The restriction \(N\ge6\) ensures that for the shorter of the two arcs connecting any pair of jumps, the error layers do not overlap across its complementary arc; it is a sufficient locality assumption, not a claim of failure for smaller meshes.

## Proof
**1. Reduction to two jumps.** Let \(T=I-P_N\). Every real periodic \(BV\) function has a signed derivative measure \(\mu=Df\) of mass zero. Its Jordan components both have mass \(m=V(f)/2\). Choose a probability coupling \(\pi\) of these normalized components. The positively oriented circular arc indicator \(\mathbf1_{[s,t)}\) has derivative \(\delta_s-\delta_t\); therefore \(f\), modulo a constant, equals \(m\int\mathbf1_{[s,t)}\,d\pi(s,t)\). Linearity and the Hilbert-space triangle inequality give
\[
\|Tf\|_2\le\frac{V(f)}2\sup_{s\ne t}\|T\mathbf1_{[s,t)}\|_2.
\]
The reverse bound is obtained by testing a single arc. Thus the squared sharp coefficient is one quarter of the maximum squared residual of an arc.

**2. Rescale one cell to unit length.** On \(\mathbb R\), use centered box averages of width one and cardinal-hat reconstruction \(P\). Write \(e_s=(I-P)\mathbf1_{[s,\infty)}\). It is supported in \([\lfloor s\rfloor-1,\lfloor s\rfloor+2]\), with actual distance from the jump to either edge at most \(3/2\). For \(0\le u\le1/2\), direct calculation gives
\[
\|e_u\|_{L^2(\mathbb R)}^2=J(u)=\frac{6u^3-5u^2+1}{6},\qquad
\|e_{1-u}\|_2^2=J(u)\le\frac16.
\]
Indeed, for \(0\le u\le1/2\), the three nonzero pieces of \(e_u\) are \(-(1/2-u)(x+1)\) on \([-1,0]\), \(-(1/2-u)-(1/2+u)x\) on \([0,u]\), and \((1/2+u)(1-x)\) on \([u,1]\). For \(1/2\le u\le1\), they are \(-(3/2-u)x\) on \([0,u]\), \(1-(3/2-u)x\) on \([u,1]\), and \((u-1/2)(2-x)\) on \([1,2]\).

For any arc replace it by its complement if necessary, making its scaled length at most \(N/2\). Integer grid translation makes its left endpoint \(s\in[0,1)\), and write its right endpoint \(t>s\). Since the complementary gap has length at least \(N/2\ge3\), the periodized error layers do not overlap across that gap. Consequently its squared error on the circle, divided by \(h\), equals
\[
Q(s,t)=\|e_s-e_t\|_{L^2(\mathbb R)}^2.
\]

**3. Both jumps inside the same cell.** Suppose \(0\le s<t\le1\). Put \(d=t-s\), \(a=|[s,t]\cap[0,1/2]|\) and \(b=|[s,t]\cap[1/2,1]|\). Only nodal averages at zero and one can be nonzero. Integration of the two corresponding hats gives the exact identity
\[
Q(s,t)=d-2\left[a\left(d-\frac{t^2-s^2}{2}\right)+b\frac{t^2-s^2}{2}\right]
+\frac23(a^2+b^2)+\frac13ab.
\]
If both endpoints lie in the same half-cell, this is at most \(d-d^2/3\le5/12<3/7\). Otherwise \(a=1/2-s\), \(b=t-1/2\), \(d=a+b\), and the identity simplifies to
\[
Q(s,t)=d-\frac7{12}d^2-\left(d-\frac14\right)(a-b)^2.
\]
For \(d\ge1/4\), this is at most \(d-7d^2/12\le3/7\), with equality exactly when \(d=6/7\) and \(a=b=3/7\). For \(d\le1/4\), it is at most \(d+d^2/4\le17/64<3/7\). Hence the only same-cell maximizer is \((s,t)=(1/14,13/14)\), with \(Q=3/7\).

**4. Exclude endpoints in different cells.** Write \(t=k+v\), \(k\ge1\), \(0\le v\le1\), and use \(J(s),J(v)\le1/6\). Positive enhancement in \(Q=\|e_s-e_t\|^2\) occurs only where the residual of the left step is positive and that of the right step is negative, namely between the endpoints. Discarding negative contributions gives an upper bound \(J(s)+J(v)+2K\), where \(K\) integrates this positive overlap. If \(k\ge3\), \(K=0\), so \(Q\le1/3\). If \(k=2\), the overlap can occur only for \(s\ge1/2\), \(v\le1/2\), and is \(K=(s-1/2)(1/2-v)/6\), giving \(Q\le5/12\).

It remains to handle \(k=1\), in four half-cell regimes. For \(s\le1/2\), \(v\le1/2\),
\[
K=(1/2+s)(1/2-v)\left(\frac16-\frac{s^2}{2}+\frac{s^3}{3}\right),\quad
Q\le F(s):=\frac{(2s+1)(2s^3+3s^2-8s+5)}{12}<\frac37.
\]
For \(s\le1/2\), \(v\ge1/2\), there is no positive overlap, so \(Q\le1/3\). For \(s\ge1/2\), \(v\le1/2\), direct integration on \([s,1]\cup[1,1+v]\) gives
\[
K=\frac{s(s-1)(2v-1)(2s^2-s+2)-v(2s-1)(v-1)(2v^2-3v+3)}{12}<\frac1{21},
\]
so \(Q<1/3+2/21=3/7\). Finally, for \(s\ge1/2\), \(v\ge1/2\),
\[
K=(s-1/2)(3/2-v)\left(\frac{v^2}{2}-\frac{v^3}{3}\right),\quad
Q\le G(v):=\frac{(2v-3)(2v^3-9v^2+4v-2)}{12}<\frac37.
\]
All three strict polynomial inequalities here have rational interval certificates: express \(3/7-F\) in degree-four Bernstein form on \([0,1/4]\) and \([1/4,1/2]\); the minimum coefficient is respectively \(1/672\) and \(47/1792\). For \(3/7-G\), the corresponding minima on \([1/2,3/4]\) and \([3/4,1]\) are \(47/1792\) and \(1/672\). For \(1/21-K\), the minimum of all 25 tensor-product degree-four Bernstein coefficients on \([1/2,1]\times[0,1/2]\) is \(1/1344\). Since Bernstein basis functions are nonnegative and sum to one, these are exact *continuum* positivity proofs, not sampled numerical evidence. Their full coefficient reconstruction is in `verify.py`.

**5. Sharpness and equality.** The unique arc geometry in steps 3–4 has \(Q=3/7\). Rescaling yields arc squared error \(3/(7N)\), while its variation equals two. This gives \(3/(28N)\). In the derivative-measure coupling of step 1, equality in the Hilbert triangle inequality requires almost every contributing arc residual to be the same positive ray. The only maximizing arcs are cell translates of the displayed short arc or their complements. Residuals for distinct cell translates have different supports and are not scalar multiples; a complement gives the opposite residual. Therefore the derivative measure is supported on exactly one optimal ordered jump pair, proving the complete equality classification.

## Verification
The self-contained Python 3 standard-library program `verify.py` uses exact `Fraction` arithmetic. It reconstructs all four univariate Bernstein certificates and the 25-coefficient tensor certificate, checks the same-cell identity against exact rational node integrations, verifies \(Q(1/14,13/14)=3/7\), and performs 3,379 exact rational finite-mesh pulse comparisons at mesh sizes 6, 7, 8, and 10. The finite comparisons are supplementary checks; the continuum inequalities follow from the analytical reductions and the exact Bernstein certificates. Run `python3 verify.py` from this directory.

## Relationship to prior work
The centered local-average \(Q_1\) interpolation construction is motivated by Nochetto–Salgado's 2012 open manuscript and the 2015 published version with Bartels, which establish total-variation diminution and general approximation estimates. The 2012 preprint's Theorem 3.9 provides nonspecific geometric constants in an \(L^1\) variation estimate, as well as general \(L^p\)-based estimates; it does not state the sharp real one-dimensional periodic \(BV\)-to-\(L^2\) coefficient or classify maximizing two-jump arcs. Nagler–Cerejeiras–Forster analyze a different Schoenberg operator, built from point evaluations at Greville knots on an interval, and establish spectral and modulus-of-smoothness results, not this local box-average reconstruction. Earlier sharp \(L^1\)/\(L^\infty\) real-line estimates for related hat reconstructions concern different target norms and single-jump responses; neither those constants nor their interpolation bounds imply the exact periodic \(L^2\) two-jump interaction and location. The manuscript comparisons support distinctness but do not establish global historical priority.

## Limitations
No theorem is asserted for \(N<6\), nonuniform meshes, nonperiodic boundary treatments, complex-valued variation, or box widths other than one mesh cell. The result proves an exact mathematical bound and all its equality cases, but no independent audit or exhaustive survey of all historical and unindexed literature has occurred. The 2015 journal version of the motivating manuscript could not be read in full; a lawful open 2012 version was materially inspected. The included exact-rational checks are reproducibility aids and not a replacement for the proof.

## References
1. R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069v1, first posted November 5, 2012. https://arxiv.org/abs/1211.1069 ; inspected §§3–4, especially (3.3)–(3.4), Theorem 3.9.
2. S. Bartels, R. H. Nochetto and A. J. Salgado, *A total variation diminishing interpolation operator and applications*, Mathematics of Computation 84 (2015), 2569–2587, DOI:10.1090/mcom/2942. Metadata and abstract checked; journal full text not fully inspected.
3. J. Nagler, P. Cerejeiras and B. Forster, *Lower bounds for the approximation with variation-diminishing splines*, arXiv:1402.2403v1, February 11, 2014. https://arxiv.org/abs/1402.2403 ; inspected introduction, operator definition and principal statements.
