# Frobenius descent and the zeta function of a characteristic-five resolved elliptic self-product

## Finding

The smooth proper crepant algebraic-space resolution \(\widehat Y\) of the characteristic-five self-product described below has complete Hasse–Weil zeta function

\[
Z(\widehat Y/\mathbb F_5,T)=\frac{1}{(1-T)(1-125T)(1-5T)^{24}(1+5T)^{18}(1-25T)^{24}(1+25T)^{18}}.
\]

In particular, its geometric degree-two Frobenius representation has \(+5\) and \(-5\) eigenvalues of multiplicities \(24\) and \(18\). For all integers \(r\ge1\),

\[
\#\widehat Y(\mathbb F_{5^r})=1+5^{3r}+(5^r+5^{2r})\bigl(24+18(-1)^r\bigr).
\]

The first four counts are \(306,42926,2047626,260573126\), for extension degrees \(1,2,3,4\) respectively.

## Assumptions and scope

Work over \(k=\mathbb F_5\). Let \(S\to\mathbb P^1_k\) be the relatively minimal rational elliptic surface with affine Weierstrass equation

\[
y^2=4x^3+3t(t+2)^3x+3t^4(t+2)^2.
\]

It has fibers of Kodaira types \(\mathrm{III}\) at \(t=0\), \(\mathrm{IV}\) at \(t=3\) and nonsplit \(\mathrm I_5\) at \(t=\infty\). The fiber product \(Y=S\times_{\mathbb P^1}S\) has a smooth proper crepant resolution \(\widehat Y\to Y\) in algebraic spaces defined over \(k\). Specifically take the compatible local resolutions and algebraization in [1, Lemmas 4.1, 5.1]. The projective big resolution \(B\) of the partial model in [1, Lemma 4.1] is related to \(\widehat Y\) by

\[
B\simeq\operatorname{Bl}_{C}\widehat Y,\qquad C\cong\mathbb P^1_k,\qquad N_{C/\widehat Y}\cong\mathcal O_{\mathbb P^1}(-1)^{\oplus2}.
\]

These are the specified \(k\)-models, rather than arbitrary twists or arbitrary resolutions defined only after scalar extension. Theorem 4.3 of [1] gives the Betti numbers of \(B\) as \((1,0,43,0,43,0,1)\), and those of \(\widehat Y\) as \((1,0,42,0,42,0,1)\). The theorem concerns \(\widehat Y\), **not** the Kummer quotient or the smooth projective Calabi–Yau \(X_5\) from [1, Theorem 1.1].

## Proof

**1. The rational points of the singular self-product.** For \(t\in\mathbb F_5\), the rational-point count of its Weierstrass fiber is

\[
n_t=6+\sum_{x\in\mathbb F_5}\chi_5\left(4x^3+3t(t+2)^3x+3t^4(t+2)^2\right),
\]

where \(\chi_5(0)=0\). At infinity use \(4x^3+3x+3\). Direct evaluation at \(t=0,1,2,3,4,\infty\) gives Weierstrass counts \((6,3,4,6,5,7)\). The explicit resolved-fiber formulas in [1, Section 4] change the \(\mathrm{III}\) count to \(11\), leave the \(\mathrm{IV}\) count at \(6\), and give \(7\) for the nonsplit \(\mathrm I_5\) fiber. Consequently the six minimal-regular-fiber counts are \((11,3,4,6,5,7)\), and

\[
\#Y(\mathbb F_5)=11^2+3^2+4^2+6^2+5^2+7^2=256.
\]

**2. The projective resolution corrections.** The ordinary triple point over the \(\mathrm{IV}\times\mathrm{IV}\) fiber is replaced by the smooth cubic surface

\[
E:\quad x(x^2-2y^2)=z(z^2-2w^2)\subset\mathbb P^3_k.
\]

The map \((x,y)\mapsto x^3-2xy^2\) has exactly five preimages for every \(b\in\mathbb F_5\): for \(b=0\), this follows because \(2\) is nonsquare, and for \(b\ne0\) the map \(\lambda\mapsto\lambda^3\) permutes \(\mathbb F_5^\times\). Thus

\[
\#E(\mathbb F_5)=\frac{\sum_{b\in\mathbb F_5}5^2-1}{4}=31,
\]

so the cubic replacement adds \(30\) points. Over the nonsplit \(\mathrm I_5\times\mathrm I_5\) fiber, Frobenius reflects each five-component cycle and fixes exactly one of its five geometric nodes; of the \(25\) product nodes, one is \(k\)-rational. Its small resolution adds one \(\mathbb P^1(k)\) in place of a point, yielding \(+5\); the other nodes have nontrivial Frobenius orbits and contribute no \(k\)-points. At \(\mathrm{III}\times\mathrm{III}\), the two initial exceptional lines in the projective partial resolution are defined over \(k\), giving \(+2\cdot5=10\). Finally, the terminal node on that partial model is replaced in \(B\) by the quadric \(cd=u^2+v^2\) in \(\mathbb P^3_k\). Since \(-1\) is a square in \(k\), this quadric is split with \((5+1)^2=36\) rational points, producing an increment of \(35\). Therefore

\[
\#B(\mathbb F_5)=256+30+5+10+35=336.
\]

The blowup \(B\to\widehat Y\) replaces \(C\cong\mathbb P^1\) with \(\mathbb P(N_{C/\widehat Y})\cong\mathbb P^1\times\mathbb P^1\) as a variety over \(k\), so its point-count increment is \((5+1)^2-(5+1)=30\). Therefore

\[
\#\widehat Y(\mathbb F_5)=336-30=306.
\]

Equivalently, the equivariant small resolution of the \(\mathrm{III}\times\mathrm{III}\) collision in [1, Lemma 5.1] has three \(k\)-rational exceptional projective lines, giving a combined increment \(3\cdot5=15\) directly on \(\widehat Y\).

**3. Quadratic saturation.** The projective variety \(B\) has no odd-degree \(\ell\)-adic cohomology and \(b_2(B)=43\) by [1, Theorem 4.3]. The same source computes \(\#B(\mathbb F_{25})=43576\). Hard Lefschetz with a \(k\)-rational ample class identifies its degree-four Frobenius eigenvalues with \(5\) times the degree-two eigenvalues. Over \(\mathbb F_{25}\), the Lefschetz formula gives

\[
43576=1+25^3+(1+25)\operatorname{Tr}\bigl(F_{25}\mid H^2(B_{\overline k},\mathbb Q_\ell)\bigr).
\]

Hence this trace equals \(1075=43\cdot25\). Purity makes all \(43\) complex absolute values equal to \(25\), and equality in the triangle inequality forces *every* eigenvalue of \(F_{25}\) on \(H^2(B)\) to equal \(25\). Therefore the eigenvalues of \(F_5\) are all \(+5\) or \(-5\).

Now apply the trace formula over \(k\) to the newly established \(\#B(k)=336\):

\[
336=1+5^3+(1+5)\operatorname{Tr}\bigl(F_5\mid H^2(B_{\overline k},\mathbb Q_\ell)\bigr).
\]

It follows that the trace equals \(35\). With \(43\) eigenvalues each in \(\{+5,-5\}\), their multiplicities are uniquely \(25\) and \(18\). The blowup formula for the rational center \(C\) removes exactly one Tate eigenvalue \(+5\) from degree two and one \(+25\) from degree four; it leaves all odd cohomology unchanged. Thus the multiplicities for \(\widehat Y\) are \(24\) and \(18\), with degree-four eigenvalues equal to five times the degree-two eigenvalues. Taking alternating determinants of \(1-TF_5\) on étale cohomology proves the zeta formula and its point-count identity for every \(r\ge1\).

## Verification

The accompanying standalone script `check_zeta.py` uses only integer arithmetic. It exhaustively counts each rational Weierstrass fiber over \(\mathbb F_5\), enumerates the exceptional cubic through its binary cubic form, and independently repeats the fiber and exceptional-surface enumerations over \(\mathbb F_{25}=\mathbb F_5[\iota]/(\iota^2-2)\). It confirms \(\#Y(\mathbb F_5)=256\), \(\#E(\mathbb F_5)=31\), \(\#B(\mathbb F_5)=336\), \(\#\widehat Y(\mathbb F_5)=306\), and the published quadratic counts \(43576\) and \(42926\) for \(B\) and \(\widehat Y\). The script also checks the first four consequences of the zeta formula. Infinite extension-degree validity follows from the cohomological proof, not from enumeration.

To reproduce: `python3 check_zeta.py`.

## Relationship to prior work

The smooth proper crepant resolution, its Betti numbers, the fiber types, the geometry of the replacement loci and the \(\mathbb F_{25}\) point count are established in [1]; they are not new claims. The cubic replacement's arithmetic has also been calculated independently, and its point count is only an input here. The new conclusion is the base-field point count of the **whole** resolution, the resulting signed degree-two and degree-four Frobenius multiplicities, and the complete zeta function over every finite extension. The earlier article [2] studies characteristic-zero local crepant constructions and their reductions, while [3] computes zeta functions of other Kummer threefolds formed as finite quotients of triple elliptic-curve products; neither supplies this particular self-fiber-product formula.

## Limitations

This is an arithmetic result for the specified \(\mathbb F_5\) model of the smooth proper algebraic-space resolution. It does not compute the zeta function of the distinct projective Kummer quotient resolution \(X_5\). The proof uses [1] for existence, cohomology, projective big-resolution construction and quadratic-extension point count; it is not a new independent derivation of those deeper geometric inputs. The claim is valid for all extension degrees after those inputs, but does not classify all algebraic-space resolutions or their arithmetic twists. The finite script is diagnostic, not an independent proof of the geometric inputs.

## References

1. D. Burek, T. Chmiel, S. Cynk, and M. Oczko, *A projective Calabi–Yau threefold in characteristic 5 non-liftable to characteristic 0*, arXiv:2611.15943v1 (publicly submitted 2026-11-11), particularly Lemmas 4.1 and 5.1, Theorem 4.3 and the point-count tables in Section 4. https://arxiv.org/html/2611.15943v1
2. D. Burek and S. Cynk, *Crepant resolutions of fiber products and Kummer fibrations of rational elliptic surfaces with non-reduced fibers*, arXiv:2609.12522v1 (2026). https://arxiv.org/abs/2609.12522
3. D. Burek, *Zeta function of some Kummer Calabi–Yau 3-folds*, Manuscripta Mathematica 174 (2024), 703–730, first published 2023-12-07, doi:10.1007/s00229-023-01524-0. https://link.springer.com/article/10.1007/s00229-023-01524-0
