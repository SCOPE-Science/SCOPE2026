# Two four-variable theories of finite four-dimensional symplectic point graphs

## Finding

For every prime power \(q\ge2\), let \(G_q\) be the finite simple undirected graph whose vertices are the one-dimensional subspaces of a four-dimensional vector space over \(\mathbb F_q\), equipped with a nondegenerate alternating bilinear form \(B\). Distinct projective points \([u]\) and \([v]\) are adjacent if and only if \(B(u,v)=0\). In the pure adjacency/equality language, without counting quantifiers, the complete classification is
\[
G_q\equiv_{\mathrm{FO}^{4}}G_r\quad\Longleftrightarrow\quad(q=2\ \Longleftrightarrow\ r=2)
\qquad(q,r\text{ prime powers }\ge2).
\]
At width three, \(G_q\equiv_{\mathrm{FO}^{3}}G_r\) for every \(q,r\ge2\). Both assertions hold at unrestricted quantifier depth. Thus the family has exactly one three-variable theory and two four-variable theories, separated by the four-clique sentence.

## Assumptions and scope

\(\mathbb F_q\) is an arbitrary finite field, including characteristic two. Projective points are nonzero vectors modulo multiplication by nonzero scalars. \(B\) is nondegenerate and alternating; all such forms in dimension four are linearly equivalent. Adjacency is irreflexive, even though \(B(u,u)=0\). A formula belongs to \(\mathrm{FO}^{k}\) when it uses at most \(k\) distinct reusable variable names, regardless of quantifier depth. No line elements, parameters, function symbols, or counting operators are present.

## Proof

**Three-variable equivalence.** There are \(v=(q+1)(q^2+1)\) vertices. Each vertex has \(k=q(q+1)\) neighbors; two adjacent vertices have \(\lambda=q-1\) common neighbors, and two nonadjacent vertices have \(\mu=q+1\) common neighbors. This follows by counting projective points in the polar hyperplanes and their intersections. For any two distinct stationary vertices, all four possible adjacency patterns of a third vertex, distinct from both, occur: if the pair is adjacent, the four counts (adjacent to both, first only, second only, neither) are \((q-1,q^2,q^2,q^2(q-1))\); for a nonadjacent pair they are \((q+1,q^2-1,q^2-1,q^2(q-1))\). Each is positive for \(q\ge2\). Equality cases and one stationary vertex also have identical extension possibilities. Thus Duplicator maintains adjacency and equality indefinitely with three pebbles, including between different orders.

**Four-variable strategy.** We prove a uniform stronger extension lemma. Temporarily enrich the graph with an auxiliary ternary relation \(T(a,b,c)\), meaning that representative vectors span a subspace of dimension at most two. This is an invariant used to describe a strategy; it is not a symbol of the theorem's language. For \(q,r\ge3\), any ordered triple of pebbled projective points in \(G_q,G_r\) with the same equality pattern, pairwise adjacency pattern and \(T\)-value has the same set of realizable one-point extensions, classified by: equality with stationary points; adjacency to each stationary point; and the three values \(T(a,b,x),T(a,c,x),T(b,c,x)\). Consequently an extra pebble can always be answered, and all triple \(T\)-information is retained. This gives a permanent four-pebble strategy.

Here is a field-uniform proof of the extension lemma; only vanishing versus nonvanishing of form values matters. Write \(U_{ab}=\langle a,b\rangle\), taking nonzero representatives. When stationary points repeat, there are at most two distinct representatives. For a pair, the projective line \(\mathbf P(U_{ab})\) has \(q+1\ge4\) points; the orthogonality patterns of points on the line and off it follow from the surjective map \(x\mapsto(B(x,a),B(x,b))\). If \(B(a,b)=0\), off-line points cannot be orthogonal to both; if \(B(a,b)\ne0\), an off-line point can realize every zero/nonzero pattern. These possibilities, together with equalities, do not depend on \(q\ge3\).

Suppose next that the three stationary points are distinct but linearly dependent. They lie on a common projective line, so all three two-point spans coincide. Write \(c=\alpha a+\beta b\) with \(\alpha,\beta\ne0\). Every point outside that line has the three form values \(f_a=B(x,a),f_b=B(x,b),f_c=\alpha f_a+\beta f_b\). If the line is totally isotropic, an off-line point cannot have \(f_a=f_b=0\), while a point on the line distinct from the three is orthogonal to all of them. If the line is nonisotropic, each pair \((f_a,f_b)\) occurs off the line (add a nonzero vector in the orthogonal complement), and every fourth point on the line is nonorthogonal to all three. With two nonzero coefficients, the cases \(f_c=0\) and \(f_c\ne0\) when \(f_a,f_b\ne0\) both occur for \(q\ge3\). There is at least one fourth point on the line. Hence every requested extension type depends only on which of the three stationary pairs are adjacent.

Finally suppose \(a,b,c\) are linearly independent. The alternating form on their three-dimensional span \(U\) has rank two: its rank is even, and a three-dimensional totally isotropic subspace cannot exist in a nondegenerate four-dimensional symplectic space. Write \(f_i=B(x,i)\), and let \(r\) span the one-dimensional radical of \(B|_U\). Then \(U=r^{\perp}\). Thus the linear map \(x\mapsto(f_a,f_b,f_c)\) is onto \(\mathbb F_q^3\), and a given form-value triple can be realized by \(x\notin U\) exactly when \(B(x,r)\ne0\). If \(x\notin U\), none of the three new ternary dependence flags holds. If \(x\in U\) but lies on none of the three two-point spans, its coefficients in the basis \((a,b,c)\) are all nonzero.

There are three possibilities for the number of nonzero entries among \(B(a,b),B(a,c),B(b,c)\):

1. Exactly one, say \(B(a,b)\ne0\). Then \(r\) is a multiple of \(c\). For points outside all three two-point spans, the possible zero/nonzero patterns of \((f_a,f_b,f_c)\) are precisely: \(f_c\ne0\) with \(f_a,f_b\) arbitrary, or \(f_c=0\) with both \(f_a,f_b\ne0\). The latter is realized inside \(U\) using three nonzero coefficients.
2. Exactly two, say \(B(a,b),B(a,c)\ne0\). Then \(r\) has nonzero coefficients at \(b,c\) and zero coefficient at \(a\). For points outside the three pair-spans, precisely the patterns in which at least one of \(f_b,f_c\) is nonzero occur. When both are nonzero they can be chosen to avoid the single linear relation \(B(x,r)=0\), since \(q\ge3\).
3. All three nonzero. All eight zero/nonzero patterns occur outside the three pair-spans. Every nonzero pattern can be realized with \(B(x,r)\ne0\); for the all-zero pattern choose \(x=r\), whose three coefficients are nonzero, so it lies in \(U\) but on none of the pair-spans.

For a new \(x\) on exactly one pair-span, say \(U_{ab}\), but distinct from stationary points, both adjacencies to \(a,b\) are fixed by whether \(B(a,b)=0\). Its adjacency to \(c\) is constant true if \(B(c,a)=B(c,b)=0\), constant false if exactly one of these values is zero, and can be either true or false if both are nonzero. In the final case the linear form \(B(c,\cdot)\) vanishes at one of the \(q-1\) eligible projective points on the line, but not at the remaining \(q-2\ge1\). Thus all extension options, including the three ternary dependence flags, are independent of the field order as long as \(q\ge3\). This completes the lemma and the four-pebble argument.

**Sharp exception.** If four distinct projective points are mutually adjacent, their representing vectors span a totally isotropic subspace, whose dimension is at most two. Such a projective line has \(q+1\) points. The four-clique sentence therefore holds exactly when \(q\ge3\). It uses four variables, separating \(G_2\) from all larger members.

## Verification

Run `python3 verify.py` from the package directory. The standalone finite-field implementation constructs the graphs over orders \(2,3,4,5\), computes all enhanced three-stationary extension types exhaustively at order three, and samples reproducibly at orders four and five. It checks equality of the observed extension catalogues and independently confirms the four-clique boundary. Its finite checks corroborate, but do not prove, the field-uniform extension lemma. The abstract algebraic case analysis above is the proof for all prime powers and unbounded quantifier depth.

## Relationship to prior work

The classical symplectic point graph construction and its strongly regular parameters are standard. General finite-variable pebble games provide the logical equivalence criterion. Brouwer, Ihringer and Kantor study the combinatorial 4-vertex condition, including collinearity graphs of generalized quadrangles, but that condition constrains a finite collection of induced-pattern counts and does not by itself supply the permanent four-pebble correspondence across different field orders. The new assertion is the exact cross-order classification in pure counting-free \(\mathrm{FO}^{4}\), with one exceptional field order. It is distinct from results for characteristic-two nonorthogonality graphs in arbitrary dimensions.

## Limitations

This concerns four-dimensional symplectic vector spaces and their point-only orthogonality graphs. It does not classify graphs in higher symplectic dimensions, point-line incidence languages, logics with counting, or five-variable theories. The three-variable part uses only the strongly regular parameters; the field-uniform four-variable lemma is the nontrivial assertion. The literature comparison is substantial but not an exhaustive historical-priority certification; an unidentified stronger fixed-variable result could subsume it. Independent mathematical verification has not been performed.

## References

1. Anuj Dawar and Bjarki Holm, *Pebble games with algebraic rules*, arXiv:1205.0913 (first posted 2012-05-04), https://arxiv.org/abs/1205.0913.
2. A. E. Brouwer, F. Ihringer and W. M. Kantor, *Strongly regular graphs satisfying the 4-vertex condition*, arXiv:2107.00076 (first posted 2021-06-30), https://arxiv.org/html/2107.00076v2.
3. A. E. Brouwer, *Symplectic graphs*, https://aeb.win.tue.nl/graphs/Sp.html.
4. Michael Giudici, *Generalised quadrangles*, 2010-05-02, https://symomega.wordpress.com/2010/05/02/generalised-quadrangles/.
