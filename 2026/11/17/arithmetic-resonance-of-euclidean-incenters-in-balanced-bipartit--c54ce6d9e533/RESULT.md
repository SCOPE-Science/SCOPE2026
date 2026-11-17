# Arithmetic resonance of Euclidean incenters in balanced bipartite snowflake free spaces

## Finding
Fix an even integer \(m=2h\ge2\) and a real parameter \(1<t<2\). Let \(M=A\sqcup B\), with \(|A|=|B|=m\), and metric \(d(a,b)=1\) across the two parts and \(d(x,y)=t\) for distinct points within the same part. Let \(K_{m,t}\) denote the unit ball of the **real** Lipschitz-free space on \(M\), represented in the canonical Euclidean hyperplane
\[
H=\{z\in\mathbb R^{2m}:\sum_{x\in M}z_x=0\},
\]
with each molecule represented by \((e_x-e_y)/d(x,y)\). Set
\[
R_m(t)^2=\frac m4\bigl(t^2+(2-t)^2\bigr),\qquad
\mathcal R_h=\left\{\frac{2v}{u+v}:1\le u<v\le h,\quad u,v\in\mathbb Z\right\}.
\]
Then the **global** Euclidean inradius of \(K_{m,t}\) is \(r_m(t)=1/R_m(t)\), and the origin is a maximum-ball center. The number of facets touching this origin-centered maximal ball is
\[
\boxed{T_m(t)=2\binom m h^2+4\sum_{\substack{1\le u<v\le h\\ t=2v/(u+v)}}\binom m{h+u}\binom m{h-v}.}
\]
The affine dimension of the entire set \(\mathcal I_{m,t}\) of optimal ball centers is
\[
\boxed{\dim\operatorname{aff}\mathcal I_{m,t}=\begin{cases}1,&t\notin\mathcal R_h,\\0,&t\in\mathcal R_h.\end{cases}}
\]
Thus the incenter is **unique exactly at the finite rational resonance set** \(\mathcal R_h\). Outside resonance, \(\mathcal I_{m,t}\) is a nondegenerate segment parallel to \(\mathbf{1}_A-\mathbf{1}_B\), centered at zero. In particular, at \(m=4\) the single interior resonance is \(t=4/3\), where contact facets jump from \(72\) to \(88\) and the one-dimensional center segment collapses to the origin. As \(m\) ranges over even integers, the union of these resonance sets is dense in \((1,2)\).

A quantitative strengthening describes the collapse. Let \(L_m(t)>0\) be the half-width defined by
\[
\mathcal I_{m,t}=\{z(\mathbf{1}_A-\mathbf{1}_B):|z|\le L_m(t)\}
\]
for a nonresonant \(t\). If \(t_0=2v/(u+v)\) is a resonance with **coprime** integers \(1\le u<v\le h\), then
\[
\boxed{\lim_{\substack{t\to t_0\\t\notin\mathcal R_h}}
\frac{L_m(t)}{(t-t_0)^2}=
\frac{(u+v)^3}{16muvR_m(t_0)^2}.}
\]

## Assumptions and scope
A Lipschitz potential is a real function \(f:M\to\mathbb R\), taken modulo additive constants. Its zero-sum representative is \(P_Hf=f-(\sum_xf(x)/(2m))\mathbf1\). The polar of \(K_{m,t}\) is the Lipschitz ball \(L=\{f:\ |f(x)-f(y)|\le d(x,y)\}\) modulo constants. A polar vertex corresponds to a facet of \(K_{m,t}\) with equation \(\langle P_Hf,z\rangle=1\) and Euclidean distance \(1/\|P_Hf\|_2\) from the origin. The metric is the strictly snowflaked complete-bipartite shortest-path metric: its within-part graph distance is two and its cross-part distance is one. We use the *fixed canonical Euclidean metric* on \(H\), not an arbitrarily optimized Hilbert norm, John ellipsoid, or Banach–Mazur distance.

The claimed theorem treats all even \(m\ge2\) and every real \(1<t<2\). The endpoint cases \(t=1\) (equilateral) and \(t=2\) (ordinary complete-bipartite graph) are not included. The number \(T_m(t)\) counts distinct *primal facets* tangent to the ball, not vertices of the primal ball. The full set of optimum centers and its affine dimension are taken inside \(H\).

## Proof
**1. Exhaustive polar vertex classification.** Call an unordered pair tight for \(f\) if equality holds in its Lipschitz inequality. An element \(f\in L\) is extreme precisely when its graph of tight pairs is connected. If that graph is connected, the tight differences along a spanning tree determine \(f\) modulo constants, so a nontrivial midpoint decomposition is impossible. If disconnected, the values on a tight component not containing a chosen base point can be perturbed by a sufficiently small \(\pm\varepsilon\) without disturbing any tight relation; the finitely many cross-component inequalities have positive slack. This proves both directions.

Suppose the oscillation of \(f\) on \(A\) equals \(t\), and translate so that its extreme heights are \(0\) and \(t\). Every \(B\)-value then lies in \([t-1,1]\) by the cross-part constraints. An intermediate \(A\)-height is incident to no tight edge, whereas a \(B\)-height strictly between \(t-1\) and \(1\) is also isolated: inside \(B\), all heights differ by at most \(2-t<t\). Thus tight connectedness forces every \(A\)-height to be \(0\) or \(t\), with both present, and every \(B\)-height to be \(t-1\) or \(1\). Conversely each such choice has a connected tight graph. There is an analogous disjoint family with \(B\) as the strong part. Both parts cannot simultaneously oscillate by \(t\), since one such oscillation restricts the other to length \(2-t<t\).

If neither part contains an internal tight pair, the connected tight graph uses only cross-part edges. Along a tight path joining two vertices in the same part, the potential changes by an **even integer**, while its same-part oscillation is less than \(t<2\). Hence each part is constant. Its two constants must differ by exactly \(1\), giving two further polar vertices. These are all the extreme potentials; the full list is also established in prior facet-enumeration work, and is used here as geometric input.

**2. Norm profile and sharp radius.** For a strong-\(A\) vertex, subtract \(t/2\) from all coordinates. Then the \(A\)-coordinates are signs times \(t/2\), and the \(B\)-coordinates are signs times \((2-t)/2\). Let \(k\) be the number of positive coordinates in \(A\), and \(j\) the number in \(B\). Put \(a=k-h\), \(b=j-h\), so \(-h+1\le a\le h-1\) and \(-h\le b\le h\), both integers. The squared centered normal length is exactly
\[
\|P_Hf\|_2^2=\frac m4\bigl(t^2+(2-t)^2\bigr)
-\frac{[ta+(2-t)b]^2}{2m}
=R_m(t)^2-\frac{[ta+(2-t)b]^2}{2m}.
\]
The strong-\(B\) family has the same formula with parts interchanged. Each constant-on-parts vertex has squared centered norm \(m/2<R_m(t)^2\) for \(t>1\). For both strong families, balanced sign patterns \(a=b=0\) exist (since \(m\) is even) and attain exactly \(R_m(t)^2\). Therefore \(R_m(t)\) is the maximum polar-vertex norm, so the ball of radius \(1/R_m(t)\) at zero lies in every polar facet halfspace. An opposite pair of maximal polar vertices forces any translated ball to have radius at most \(1/R_m(t)\), proving global optimality, not merely origin-centered optimality.

**3. Contacts and arithmetic resonances.** In either strong family equality is precisely \(ta+(2-t)b=0\). For \(1<t<2\), a nonzero integral solution has \((a,b)=(u,-v)\) or \((-u,v)\), where \(1\le u\le h-1\), \(1\le v\le h\), and \(t=2v/(u+v)\). Because \(t>1\), necessarily \(v>u\). The zero solution gives \(\binom mh^2\) balanced assignments in each strong family. Each nonzero pair contributes \(2\binom m{h+u}\binom m{h-v}\) assignments per strong family. This gives the stated exact contact count, including multiple representations of a rational resonance, without double-counting because each sign profile is distinct.

**4. Every optimal center.** A point \(z\in H\) is a center for the already established maximal radius iff, for every polar vertex \(f\),
\[
\langle P_Hf,z\rangle\le1-\|P_Hf\|_2/R_m(t).
\]
At maximum-norm vertices the right side vanishes, and the existence of the negative vertex forces equality. The balanced contacting normals span precisely
\[
W_A\oplus W_B=\{z\in H:\sum_{a\in A}z_a=0=\sum_{b\in B}z_b\}.
\]
Indeed, independently swapping one positive and one negative coordinate in either part generates every coordinate difference within that part, while all balanced normals have zero mean separately on each part. This has dimension \(2m-2\) inside the \((2m-1)\)-dimensional \(H\), leaving the line generated by \(w=\mathbf{1}_A-\mathbf{1}_B\). At a resonance, an additional contacting normal has a nonzero block-sum, so its scalar product with \(w\) is nonzero and the contact normals span all of \(H\). This proves center uniqueness at resonance. Off resonance, every noncontact polar vertex has positive slack, and there are finitely many of them; hence a small nonzero interval of \(z w\) obeys all inequalities. Central symmetry forces that interval to be centered at zero, proving the asserted one-dimensional affine center family.

**5. Quadratic center-width pinching.** Fix a resonance \(t_0=2v/(u+v)\) with coprime positive integers \(u<v\). Every newly contacting profile there has \((a,b)=(ku,-kv)\) or its negative for an integer \(k\ge1\) admitted by the bounds, and either strong-part choice. For that profile, the deviation \(ta+(2-t)b\) has absolute value \(k(u+v)|t-t_0|\). Consequently its facet-radius slack satisfies
\[
1-\frac{\|P_Hf\|_2}{R_m(t)}
=\frac{k^2(u+v)^2}{4mR_m(t_0)^2}(t-t_0)^2+o((t-t_0)^2).
\]
At \(t=t_0\), the absolute pairing with \(w\) is \(2ktu\), converging to \(2kt_0u=4kuv/(u+v)>0\). Since opposite profiles supply both sides of the constraint on the center segment, the bound on its half-width from a profile of multiple \(k\) is asymptotic to
\[
\frac{k(u+v)^3}{16muvR_m(t_0)^2}(t-t_0)^2.
\]
The primitive profile \(k=1\) is permitted and is smallest. Every vertex that was noncontact at \(t_0\) has a strictly positive facet slack there; finiteness and continuity ensure none can dominate these quadratic bounds nearby. Balanced contacts pair to zero with \(w\) for all \(t\). Taking the minimum therefore proves the claimed precise limit. Finally, rational numbers \(v/u>1\) yield the dense set \(2v/(u+v)\in(1,2)\) as the allowed even size increases. \(\square\)

## Verification
The included standalone program `verify_biclique_resonance.py` enumerates all analytically classified polar potentials with **exact rational arithmetic**, computes centered squared norms and contact-normal ranks by exact elimination, and cross-checks the predicted counts for eight profiles with \(m\in\{2,4,6\}\), including rational resonance and nonresonance cases. An independent route reconstructs all dual vertices from their original halfspace inequalities using `scipy.spatial.HalfspaceIntersection` for four smaller profiles, comparing norm maxima, contact counts, and ranks. The exact vertex enumeration covers 33,120 profiles (counted with repetitions across parameter choices); halfspace reconstruction additionally verifies the counts in four profiles. The program does not attempt to certify all real parameters or the quadratic asymptotic by finite sampling; these are established by the preceding algebraic proof.

Run `python verify_biclique_resonance.py` with Python 3 and NumPy/SciPy installed for the independent halfspace cross-check. The exact-arithmetic portions require only the Python standard library. Expected final line: `BALANCED_BICLIQUE_RESONANT_INCENTERS_ALL_CHECKS_PASS`.

## Relationship to prior work
The published *Sharp facet-count transitions for snowflaked complete bipartite metrics* (identifier `2026/10/11/SCOPE-sharp-facet-count-transitions-for-snowflaked-complete-bipartite--e855a74da4ce`) already gives, for arbitrary unequal part sizes, the **complete classification of dual vertices** and their total number \(2(2^m-1)(2^n-1)\) throughout \(1<t<2\). Neither that strong vertex result nor the total-facet formula is claimed as original here. The present new step is the exact centered Euclidean norm profile, full classification of its equality cases via finite rational resonances, rank of the contacting normals, resulting unique-versus-segment incenter theorem, and quadratic center-width pinching. The prior vertex classification makes the computation possible, but does not itself provide those values or structural transitions.

Higashitani, Jochemko and Michałek (arXiv:1807.07678v1, first public 2018-07-20) classify facets of the symmetric edge polytope for the **ordinary graph-metric endpoint** \(t=2\), where the primal unit ball changes combinatorial type. Their theorem does not extend to the open snowflake regime. Alexander, Fradelizi, García-Lirola and Zvavitch (arXiv:1911.10642) investigate general finite-metric free-ball geometry, Hanner structure and volume product, not this fixed-Euclidean inradius or a rational-resonance center-locus collapse. General Lipschitz-polytope combinatorics developed by Gordon and Petrov are used as background, not claimed here. The known Banach–Mazur distance of the ordinary complete-bipartite transportation space optimizes over quadratic forms and concerns a different metric regime and invariant.

## Limitations
The theorem is for finite balanced two-part metrics with **even** part size and the strictly interior parameter \(1<t<2\). It does not compute the inball geometry for odd or unequal part sizes. The canonical Euclidean norm is essential; no invariant Banach–Mazur optimization is asserted. The result gives the affine dimension and asymptotic width of the entire incenter set, but not a simple exact piecewise formula for the segment width at every nonresonant parameter. Historic equivalents under maximum-variance, transportation, and polyhedral duality terminology remain a bibliographic risk; searching sources and a mathematical implication comparison cannot establish absolute priority. Exact finite checks corroborate, and do not replace, the all-parameter argument. Independent mathematical validation has not been performed.

## References
1. *Sharp facet-count transitions for snowflaked complete bipartite metrics*, research result, 2026-10-11; full mathematical statement and proof at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-facet-count-transitions-for-snowflaked-complete-bipartite--e855a74da4ce .
2. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, first public 2018-07-20; https://arxiv.org/abs/1807.07678 .
3. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, first public 2019-11-24; https://arxiv.org/abs/1911.10642 .
4. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, arXiv:1608.06848, 2016; https://arxiv.org/abs/1608.06848 .
5. *Maximal Hilbert distortion for complete-bipartite transportation spaces*, 2026-10-11; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-maximal-hilbert-distortion-for-complete-bipartite-transportation--203c5ca21810 .
