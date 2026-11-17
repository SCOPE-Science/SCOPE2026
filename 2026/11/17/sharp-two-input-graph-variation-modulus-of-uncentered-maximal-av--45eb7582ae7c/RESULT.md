# Sharp two-input graph-variation modulus of uncentered maximal averaging on finite stars

## Finding

Let \(S_{k+1}\) be the finite unit-edge star with a hub and \(k\ge1\) leaves, equipped with counting measure. The **uncentered graph-ball Hardy–Littlewood maximal operator** on nonnegative real vertex signals is the maximum of the averages over all graph-distance balls containing the evaluation vertex. With edge total variation \(\operatorname{TV}(u)=\sum_{i=1}^k|u(v_i)-u(o)|\), its exact global two-input modulus is
\[
\boxed{\sup_{f,g\ge0,\ \operatorname{TV}(f-g)>0}
\frac{\operatorname{TV}(\widetilde Mf-\widetilde Mg)}{\operatorname{TV}(f-g)}=
\begin{cases}
\tfrac12,&k=1,\\
1,&k=2,\\
\tfrac54,&k=3,\\
\tfrac{k}{2},&k\ge4.
\end{cases}}
\]
Each sharp constant is attained by two explicitly described nonnegative signals. Hence this two-input stability modulus first exceeds one at three leaves and subsequently grows linearly with branching. This is a pairwise perturbation theorem, not an estimate of \(\operatorname{TV}(\widetilde Mf)/\operatorname{TV}(f)\).

## Assumptions and scope

The vertices are \(o,v_1,\ldots,v_k\), with edges precisely \(\{o,v_i\}\) and unit shortest-path distance. A closed graph ball is \(B(a,r)=\{v:d(a,v)\le r\}\), for any center vertex and \(r\ge0\). For nonnegative \(f\),
\[
(\widetilde Mf)(v)=\max_{a,r:\,v\in B(a,r)}\frac{1}{|B(a,r)|}\sum_{w\in B(a,r)}f(w).
\]
The admissible input pairs are independent nonnegative real functions; no bound is claimed for the absolute-value maximal operator on *unrestricted signed* pairs. Set \(d_i=f(v_i)-f(o)\), \(m=(\sum_i d_i)/(k+1)\), and \(a=\max_i d_i\). The complete ball list yields
\[
(\widetilde Mf)(o)=f(o)+H(d),\quad
(\widetilde Mf)(v_i)=f(o)+L_i(d),
\]
where \(H(d)=\max\{0,a/2,m\}\) and \(L_i(d)=\max\{d_i,d_i/2,m\}\). Define the edge-coordinate map \(F_i(d)=L_i(d)-H(d)\). Then
\[
\operatorname{TV}(f-g)=\|d(f)-d(g)\|_1,\qquad
\operatorname{TV}(\widetilde Mf-\widetilde Mg)=\|F(d(f))-F(d(g))\|_1.
\]
Every \(d\in\mathbb R^k\) corresponds to some *nonnegative* \(f\), by adding a sufficiently large common baseline. Thus the desired modulus is exactly the global \(\ell_1\)-Lipschitz constant of \(F\), with no hidden restriction on edge-coordinate vectors.

## Proof

**Branch reduction.** The map \(F\) is continuous and piecewise linear. Along a line segment joining two arbitrary edge-coordinate vectors it traverses finitely many linearity regions. Therefore its global \(\ell_1\)-Lipschitz constant is at most the largest matrix \(\ell_1\)-operator norm among strict active branches, and it suffices to bound the absolute column sums of their Jacobians. Boundary branches and ties follow by continuity. Write \(e_i\) for coordinate rows and \(u=(1,\ldots,1)/(k+1)\). A leaf's active row is one of \(e_i,e_i/2,u\); the hub's active row is one of \(0,e_j/2,u\).

**Hub chooses zero.** This requires every \(d_i\le0\), so each leaf chooses either \(e_i/2\) or \(u\). For any column, the absolute column sum of the edge map is at most
\[
\frac12+\frac{k-1}{k+1}.
\]
This is at most the displayed proposed modulus for every \(k\ge2\).

**Hub chooses the global mean.** Here \(m>0\), so each leaf chooses either its own \(e_i\) or \(u\). In any column, the absolute column sum is at most
\[
\frac{k}{k+1}+\frac{k-1}{k+1}=\frac{2k-1}{k+1}.
\]
It is \(1\) for \(k=2\), \(5/4\) for \(k=3\), and no greater than \(k/2\) when \(k\ge4\).

**Hub chooses a pair.** Suppose the uniquely maximizing pair is \(\{o,v_j\}\), so \(d_j>0\), \(H=d_j/2>m\) and the row at \(v_j\) is exactly \(e_j\). In column \(j\), the latter leaf contributes \(1/2\) and every other leaf contributes at most \(1/2\), giving \(k/2\). In each column \(\ell\ne j\), the leaf \(v_j\) contributes zero, \(v_\ell\) contributes at most one, and each of the other \(k-2\) leaves at most \(1/(k+1)\); hence the bound \((2k-1)/(k+1)\). This proves the required bound for \(k=2\) and all \(k\ge4\).

For \(k=3\), the coarse estimate \(k/2\) for column \(j\) must be improved. **At least one of the other two leaves selects the global mean.** To see this, put \(a=d_j>0\), and write the other coordinates \(b,c\). Since the hub selects \(a/2\), we have \(b+c<a\). If both other leaves selected their own direct values, then \(b,c\ge0\) and \(b,c\ge m\) would imply \(b+c\ge2m=(a+b+c)/2\), hence \(b+c\ge a\), a contradiction. If one leaf selected its negative half value and the other its positive direct value, say \(c\le0\) and \(c/2\ge m\) with \(b\ge0\), then \(c\ge a+b>0\), again impossible. If both selected negative half values, their inequalities yield \(b\ge a+c\) and \(c\ge a+b\), hence \(a\le0\), impossible. Thus one of the two leaves selects \(u\), contributing only \(|1/(k+1)-1/2|=1/4\) in column \(j\), instead of \(1/2\). That column is bounded by \(1/2+1/2+1/4=5/4\); every other column is already bounded by \((2k-1)/(k+1)=5/4\).

**One-leaf case.** When \(k=1\), directly \(F_1(d)=d/2\) for either sign of \(d\), and the constant is exactly \(1/2\).

**Attainment.** For \(k=1,2,3\), set \(f(o)=0\) and all leaf values equal to \(1\). Set \(g=f+\varepsilon\mathbf1_{\{v_1\}}\), where \(\varepsilon=1/10\). For \(k=1\), the output edge difference has magnitude \(\varepsilon/2\). For \(k=2,3\), the hub selects the full-graph average and all leaves select singletons for both inputs; the output edge-difference components are \(k\varepsilon/(k+1)\) at \(v_1\) and \(-\varepsilon/(k+1)\) at every other leaf. Their total absolute sum equals \((2k-1)\varepsilon/(k+1)\), giving respectively \(1\) and \(5/4\). For \(k\ge4\), set \(f(o)=3\), \(f(v_1)=4\), and \(f(v_i)=0\) for \(i>1\), again with \(g=f+\varepsilon\mathbf1_{\{v_1\}}\). The hub strictly selects the pair \(\{o,v_1\}\); leaf \(v_1\) selects its singleton; all other leaves select their two-vertex hub pairs. These choices remain strict after the perturbation because \(2(1+\varepsilon)<3(k-3)\). Consequently the output edge-difference vector has components \(\varepsilon/2,-\varepsilon/2,\ldots,-\varepsilon/2\), attaining \(k\varepsilon/2\). Since the input difference has variation \(\varepsilon\), all asserted constants are attained.

## Verification

Run `python verify_star_two_input.py` with the Python standard library. It independently enumerates graph balls, checks the analytical branch map against direct ball averages for 3,905 rational edge-coordinate vectors, tests 39,098 exact-rational input pairs, checks 11,949 strict-branch Jacobian norms, and verifies the exact nonnegative attaining pairs for all \(1\le k\le23\). These computations support but do not replace the unrestricted case analysis above.

## Relationship to prior work

Bober–Carneiro–Hughes–Pierce, arXiv:1005.3030, prove sharp **single-input** variation contraction for the uncentered maximal operator on the entire one-dimensional integer lattice. Madrid, arXiv:1512.04112, derives further sharp one-dimensional variation inequalities. Neither result treats branching stars or a **difference of two maximal images**. Soria–Tradacete, arXiv:1410.6204, study the **centered** finite-graph maximal operator and its \(\ell_p\) constants, not the present uncentered two-input variation invariant. González-Riquelme–Madrid, arXiv:2005.03146, determine one-input \(p\)-variation constants for the **centered** graph maximal operator, including stars.

The closest located result for precisely the same uncentered star graph-ball averaging family is *Sharp total variation amplification for uncentered maximal averages on finite star graphs* (published-finding corpus public record `b063c98cacfd`), which proves the one-input constant \(C_k=(k^2-k+2)/(2(k+1))\). Its proof concerns \(\operatorname{TV}(\widetilde Mf)/\operatorname{TV}(f)\), not the pairwise modulus. For \(k\ge4\), the present modulus exceeds that constant by exactly \((k-1)/(k+1)\). The one-input theorem cannot control the two-input quotient because the nonlinearity prevents replacing differences of outputs by the output of a difference. Other known two-input statements for centered stars and uncentered short cycles concern genuinely different graph-ball selections. A preexisting equivalent under general max-affine or nonlinear BV terminology has not been ruled out absolutely.

## Limitations

The claim is for finite unweighted stars, uniform vertex averaging, nonnegative real signals, and unweighted edge total variation. The nonnegative restriction matters: for the standard maximal operator defined using absolute values, arbitrary signed pairs may differ by a constant while their output difference has nonzero variation, preventing a finite estimate using only the input-difference seminorm. The theorem does not determine constants on arbitrary trees, nonuniform vertex measures or other graph families. It does not classify every maximizing pair. Literature coverage is subject to potential unindexed antecedents and does not constitute independent priority certification.

## References

1. J. Bober, E. Carneiro, K. Hughes, L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030, first public posting 2010-05-17. https://arxiv.org/abs/1005.3030
2. J. Madrid, *Sharp inequalities for the variation of the discrete maximal function*, arXiv:1512.04112, first public posting 2015-12-13. https://arxiv.org/abs/1512.04112
3. J. Soria, P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204, first public posting 2014-10-22. https://arxiv.org/abs/1410.6204
4. C. González-Riquelme, J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146, first public posting 2020-05-06. https://arxiv.org/abs/2005.03146
5. *Sharp total variation amplification for uncentered maximal averages on finite star graphs*, published-finding corpus public mathematical record `b063c98cacfd`. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-total-variation-amplification-for-uncentered-maximal-avera--b063c98cacfd
