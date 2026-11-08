# Variance rigidity under balanced path-fibre refinements

## Finding

Let \(n\ge3\) and let \(F_0,\ldots,F_{n-1}\) be finite nonempty metric spaces, each of diameter at most \(2\). Form their disjoint union \(X\), retaining each internal metric and setting
\[
d(x,y)=|i-j|\qquad(x\in F_i,\ y\in F_j,\ i\ne j).
\]
Assign each fibre probability \(1/n\) and assign its points arbitrary strictly positive conditional probabilities. Then the sharp variance of a real-valued \(1\)-Lipschitz function is
\[
\boxed{\sup_{\operatorname{Lip}(f)\le1}\operatorname{Var}_{\mu}(f)=\frac{n^2-1}{12}.}
\]
For every \(n\ge4\), all maximizers are exactly \(f(x)=c+i\) or \(f(x)=c-i\) for all \(x\in F_i\), with \(c\in\mathbb R\).

For \(n=3\), all maximizers have an arbitrary common middle-fibre value \(c\); every endpoint-fibre value belongs to \(\{c-1,c+1\}\), and the endpoint conditional means sum to \(2c\). These conditions are necessary and sufficient *among functions respecting the stated internal metrics*. Consequently, the sharp uniqueness transition occurs at four fibres. The variance-preservation threshold is also sharp: with two two-point fibres, each of internal distance \(2\), and cross distance \(1\), uniform measures yield sharp variance \(1/2\), greater than the two-point path value \(1/4\).

The result applies in particular to the layered graph \(P_n[\overline{K_m}]\) for every \(m\ge2\), whose fibres are independent sets and successive fibres induce complete bipartite graphs.

## Assumptions and scope

Each \(F_i\) is a *metric* with its own distances; empty fibres are forbidden and every atom has strictly positive mass. Cross-fibre distances depend only on indices. The diameter restriction guarantees that this prescription defines a metric: for points in one fibre, the only potentially new triangle inequality uses a point in a different fibre and follows from \(d(x,x')\le2\le2|j-i|\). All other triangles follow from the line metric. The probability measure is exactly uniform across the index set, not necessarily uniform within any fibre. Variance is \(\mathbb E_\mu[(f-\mathbb E_\mu f)^2]\).

For an arbitrary admissible \(f\), let \(m_i\) and \(v_i\) denote the conditional mean and variance in \(F_i\). Define \(\delta_{ij}\ge0\) for \(i<j\) by
\[
\delta_{ij}=\begin{cases}
1-(m_i-m_j)^2-v_i-v_j,&j=i+1,\\
(j-i)^2-(m_i-m_j)^2-2(v_i+v_j),&j\ge i+2.
\end{cases}
\]
The theorem includes the exact nonnegative deficit decomposition, for \(n\ge4\):
\[
\boxed{
n^2\left(\frac{n^2-1}{12}-\operatorname{Var}_\mu f\right)
=\sum_{i<j}\delta_{ij}+(n-3)(v_0+v_{n-1})
+(n-4)\sum_{i=1}^{n-2}v_i.}
\]
This gives quantitative stability without any regularity or cardinality assumptions on the fibres.

## Proof

**1. Two-point bounds.** Draw independently \(U_i\) and \(U_j\) from the conditional distributions on two distinct fibres. For consecutive fibres, every cross distance is \(1\); hence
\[
(m_i-m_{i+1})^2+v_i+v_{i+1}
=\mathbb E[(f(U_i)-f(U_{i+1}))^2]\le1.
\]
For a nonconsecutive pair with gap \(h=j-i\ge2\), all values on their union have range at most \(h\): cross differences are bounded by \(h\), and same-fibre differences by \(2\le h\). The equal mixture of their conditional laws therefore has variance at most \(h^2/4\) by the elementary range-variance bound. Its variance is \((v_i+v_j)/2+(m_i-m_j)^2/4\), giving
\[
(m_i-m_j)^2+2(v_i+v_j)\le h^2.
\]
Thus every specified \(\delta_{ij}\) is nonnegative.

**2. Exact summation.** The usual pair-differences identity gives
\[
n^2\operatorname{Var}_\mu f
=\sum_{0\le i<j<n}(m_i-m_j)^2+n\sum_i v_i.
\]
Summing the bounds in step 1 and counting each variance contribution gives
\[
\sum_{i<j}(j-i)^2-n^2\operatorname{Var}_\mu f
=\sum_{i<j}\delta_{ij}
+\sum_i\bigl[n-2-\deg_{P_n}(i)\bigr]v_i.
\]
The path endpoints have degree \(1\), all internal indices degree \(2\), and \(\sum_{i<j}(j-i)^2=n^2(n^2-1)/12\). This proves the boxed identity when \(n\ge4\), and hence the upper bound. It is attained by either unit-slope index function, since \(|i-j|\) is precisely the inter-fibre distance.

**3. Equality rigidity for \(n\ge4\).** For \(n\ge5\), every coefficient of \(v_i\) in the deficit is positive. Therefore each conditional variance vanishes; strict positivity of every atomic mass makes \(f\) constant on each fibre. Since every pair deficit vanishes, the two endpoint means have distance \(n-1\), and the consecutive differences are bounded in magnitude by \(1\). Equality in the triangle inequality forces the entire sequence of means to rise or fall with unit slope.

For \(n=4\), the endpoint variance coefficients are positive but the two interior coefficients are zero. Equality nevertheless forces \(v_0=v_3=0\) and \(\delta_{03}=0\), hence \(|m_3-m_0|=3\). If \(m_3=m_0+3\), every value in \(F_1\) lies simultaneously in \([m_0-1,m_0+1]\) by its distance from \(F_0\) and in \([m_3-2,m_3+2]\) by its distance from \(F_3\). These intervals intersect only at \(m_0+1\). Similarly every value in \(F_2\) equals \(m_0+2\). The decreasing case follows by negation. This proves the complete classification.

**4. Exactly three fibres.** Put \(a=m_0-m_1\), \(b=m_2-m_1\), and \(\lambda_{01}=1-a^2-v_0-v_1\), \(\lambda_{12}=1-b^2-v_1-v_2\), both nonnegative by step 1. An exact expansion yields
\[
9\left(\frac23-\operatorname{Var}_\mu f\right)
=(a+b)^2+3v_1+3(\lambda_{01}+\lambda_{12}).
\]
The upper bound \(2/3\) follows, with equality requiring \(a+b=0\), \(v_1=0\), and both \(\lambda\)'s zero. Strictly positive atomic masses imply that the middle fibre is constant at \(c\) and every endpoint value differs from \(c\) by exactly \(1\). The remaining equation \(a+b=0\) is exactly the endpoint-mean balance. Conversely, such a function is \(1\)-Lipschitz whenever it respects the internal fibre distances, and all displayed deficits vanish.

**5. Sharpness at two fibres.** Take two fibres of two points each, internal distance \(2\) and cross distance \(1\), with uniform measure. Values \((-1,1)\) on the first fibre and \((0,0)\) on the second are feasible and have mean zero and variance \(1/2\). To verify the exact value, write the two values in the first fibre as \(p\pm a\), and in the second as \(q\pm b\), with \(a,b\ge0\). The four cross-edge constraints are equivalent to \(|p-q|+a+b\le1\). The uniform variance is \( (p-q)^2/4+(a^2+b^2)/2\), at most \( (|p-q|+a+b)^2/2\le1/2\). The exhibited function attains equality. This space is the graph metric of \(K_{2,2}\). No assertion about the threshold for nonuniform fibre totals is made.

## Verification

The standalone `verify_path_fibre_spread.py` performs exact-rational enumeration of normalized integer Lipschitz profiles for independent-fibre and clique-fibre graph examples with three to five layers, checks their sharp variances and all equality cases, checks the nonnegative deficit identity on each enumerated profile, tests two additional nonuniform conditional-probability examples, and checks a two-layer counterexample. Its final marker is `ALL_PATH_FIBRE_VARIANCE_CHECKS_OK`. Finite enumeration is supporting evidence; the proof above establishes the infinite family and arbitrary conditional measures.

## Relationship to prior work

Alon, Boppana and Spencer introduced graph spread and established that the ordinary \(n\)-vertex path has spread \((n^2-1)/12\). Addario-Berry, Janson and McDiarmid explicitly review that fact and study random graph spread, Cartesian-product identities and related graph metrics. The present statement is not simply the path result: it treats a larger metric space with arbitrary-size nontrivial metric fibres and independent conditional masses, proves that their internal variance cannot improve the sharp constant from three layers onward, and completely classifies the equality configurations including a four-layer rigidity threshold and a deficit identity. Targeted searches of graph-spread literature and related indexed mathematical records did not identify this precise result, but they do not establish global novelty.

## Limitations

The cross distances must be exactly those of consecutive integer indices, the fibre diameters at most \(2\), and the fibre total masses exactly equal. Conditional measures must charge all atoms to obtain the stated pointwise equality classification. Nonuniform masses across fibres, arbitrary base graphs, and higher moments are not addressed. The statement is a mathematical derivation with computational corroboration, not an independent external validation. Equivalent formulations outside the checked literature remain possible.

## References

1. N. Alon, R. Boppana and J. Spencer, *An asymptotic isoperimetric inequality*, Geometric and Functional Analysis **8** (1998), 411–436. Original paper: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf .
2. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156 (first posted 2009-02-06), later *Combinatorics, Probability and Computing* (2014). https://arxiv.org/abs/0902.1156 .
