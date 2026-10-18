# A single product seed forces a dense quadratic-irrational almost-sure spectrum

## Finding
Consider the \([0,1]\)-valued Łukasiewicz predicate logic studied by Badia, Caicedo, and Noguera, expanded by the ordinary product connective, under their random finite-model semantics. Let \(A_{\mathrm{as}}\) be its set of almost-sure truth values and put
\[
\alpha=\frac{\sqrt5-1}{2}.
\]
Then
\[
(\mathbb Z+\mathbb Z\alpha)\cap[0,1]\subseteq A_{\mathrm{as}}.
\]
Consequently, every nonempty open interval in \((0,1)\) contains infinitely many quadratic irrational almost-sure truth values.

## Assumptions and scope
The probability model is the one used for the infinitely valued case by Badia, Caicedo, and Noguera: each predicate is sampled from a Borel probability measure on \([0,1]\) assigning positive measure to every nontrivial interval, and finite models carry the induced product measure. The added product is the continuous ordinary multiplication connective. No claim is made here about full product Łukasiewicz logic with its discontinuous residuated implication.

The statement also does not answer whether pure infinitely valued Łukasiewicz predicate logic, without the product connective, has any irrational almost-sure value.

## Proof
Badia, Caicedo, and Noguera prove that the extrema of every continuous term operation are almost-sure values. Their Example 35 applies this to Łukasiewicz logic with product and obtains
\[
\alpha=\frac{\sqrt5-1}{2}
=\inf_{v\in[0,1]}\bigl(\neg v\vee(v\cdot v)\bigr)
\in A_{\mathrm{as}}.
\]
They also observe in their final remarks that \(A_{\mathrm{as}}\) is a subalgebra of the truth-value algebra. Hence every value obtained from \(\alpha\) by a Łukasiewicz term also lies in \(A_{\mathrm{as}}\).

Fix integers \(m,n\), and define
\[
f_{m,n}(x)=\min\!\bigl(1,\max(0,mx+n)\bigr).
\]
This is a continuous piecewise-linear map with integer coefficients. By McNaughton's theorem, as recalled in Mundici's characterization of free MV-algebras, \(f_{m,n}\) is a unary Łukasiewicz term function. Therefore, whenever \(m\alpha+n\in[0,1]\),
\[
m\alpha+n=f_{m,n}(\alpha)\in A_{\mathrm{as}}.
\]
This proves
\[
(\mathbb Z+\mathbb Z\alpha)\cap[0,1]\subseteq A_{\mathrm{as}}.
\]

It remains to identify the topological and arithmetic nature of this subset. Let \(F_0=0,F_1=1\) be the Fibonacci numbers. Since \(\alpha^2=1-\alpha\), induction gives
\[
\alpha^r=(-1)^{r-1}\bigl(F_r\alpha-F_{r-1}\bigr)
\qquad(r\ge1).
\]
Thus every \(\alpha^r\) belongs to \(\mathbb Z+\mathbb Z\alpha\), and \(\alpha^r\to0\).

Given a nonempty open interval \((a,b)\subset(0,1)\), choose \(r\) so large that \(\delta=\alpha^r<b-a\), and set
\[
k=\left\lfloor\frac a\delta\right\rfloor+1.
\]
Then
\[
a<k\delta\le a+\delta<b,
\]
so \(k\alpha^r\in(\mathbb Z+\mathbb Z\alpha)\cap(a,b)\). Taking arbitrarily large \(r\) gives infinitely many such points: if \(k\alpha^r=\ell\alpha^s\) with \(r\ne s\), then a nonzero power of \(\alpha\) would be rational, impossible because \(\alpha\) is quadratic irrational.

Finally, if \(m\alpha+n\in(0,1)\) with integers \(m,n\), then \(m\ne0\): the only integers in \((0,1)\) are none. If \(m\alpha+n\) were rational, then \(\alpha\) would be rational. Hence every interior point of \((\mathbb Z+\mathbb Z\alpha)\cap[0,1]\) is irrational; because it lies in \(\mathbb Q(\sqrt5)\), it is quadratic irrational.

## Verification
The proof separates into three independently checkable ingredients.

1. The source theorem supplies the seed \(\alpha\) and states that \(A_{\mathrm{as}}\) is a subalgebra.
2. McNaughton's theorem supplies the unary term \(f_{m,n}\) for every integer pair \((m,n)\).
3. The Fibonacci identity above gives an explicit sequence of positive group elements tending to \(0\), which proves density without invoking an external equidistribution theorem.

The accompanying `verify.py` checks the Fibonacci identity symbolically in the quadratic ring \(\mathbb Z[\alpha]\) for the first 100 powers and performs a high-precision finite sanity check of interval hitting. The infinite statement is established by the proof, not by the finite computation.

## Relationship to prior work
Badia, Caicedo, and Noguera prove that all rationals are almost-sure values in pure infinitely valued Łukasiewicz logic, and their Example 35 exhibits the single irrational value \(\alpha\) after adding product. They also explicitly note that the set of almost-sure values is a subalgebra and ask for an algebraic characterization of that subalgebra.

The present deduction combines that irrational seed with the classical McNaughton description of unary MV-term functions. The result is stronger than the isolated example: one product-generated irrational forces the entire clipped additive group
\[
(\mathbb Z+\mathbb Z\alpha)\cap[0,1]
\]
into the almost-sure spectrum, so irrational almost-sure values occur densely, indeed infinitely often in every open interval.

Targeted searches for dense irrational almost-sure spectra, quadratic-irrational almost-sure values, the golden-ratio example combined with McNaughton terms, and exact formulations involving \(\mathbb Z+\mathbb Z\alpha\) did not locate this consequence as a stated theorem.

## Limitations
This is a structural corollary rather than a classification of \(A_{\mathrm{as}}\). It gives a countable dense subset contained in \(A_{\mathrm{as}}\), but it does not determine whether additional algebraic or transcendental values occur.

The conclusion depends on the continuous product expansion used in Example 35. It does not settle the source paper's open question about irrational almost-sure values in pure Łukasiewicz logic, and it does not establish a zero-one law for the expansion by the discontinuous product residuum.

Because the deduction from subalgebra closure and McNaughton's theorem is short, uncatalogued folklore among MV-algebra specialists remains the main originality risk.

## References
1. Guillermo Badia, Xavier Caicedo, and Carles Noguera, “Asymptotic truth-value laws in many-valued logics,” arXiv:2306.13904, first posted 2023-06-24; Journal of Symbolic Logic 90 (2025), 1756–1778, DOI: 10.1017/jsl.2024.46.
2. Daniele Mundici, “A Characterization of the free n-generated MV-algebra,” Archive for Mathematical Logic 45 (2006), 239–247, DOI: 10.1007/s00153-004-0273-8.
