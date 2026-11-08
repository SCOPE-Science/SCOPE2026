# The Fano-linear hyperflex spectrum of ordinary plane quartics in characteristic two

## Finding
Let \(k\) be algebraically closed of characteristic \(2\), and let \(C\subset\mathbb P^2_k\) be a smooth ordinary plane quartic (equivalently, one with seven geometric bitangent lines). A **hyperflex bitangent** is a line whose scheme-theoretic intersection with \(C\) is \(4P\) for one point \(P\). Then the number of hyperflex bitangents is **exactly one of** \(0,1,3,7\); every value occurs. If there are exactly three, their lines are concurrent. The possible hyperflex-line sets, in the intrinsic Fano plane of seven bitangents, are precisely the empty set, a singleton, a three-line pencil at a Fano point, or the entire set. Each possibility is realized by a smooth ordinary quartic.

More precisely, using a Fano coordinate frame, every such quartic is represented by
\[
 C_Q:\quad Q(x,y,z)^2=xyz(x+y+z),\qquad Q=ax^2+by^2+cz^2+dxy+eyz+fzx.
\]
The seven hyperflex conditions are exactly
\[
 e=0,\ f=0,\ d=0,\ e+f=0,\ d+f=0,\ d+e=0,\ d+e+f=0.
\]
If \(r=\dim_{\mathbb F_2}\langle d,e,f\rangle\), their number is \(2^{3-r}-1\). All four ranks \(r\in\{0,1,2,3\}\) can occur on the smooth locus. The incidence statement is invariant under changing the Fano coordinate frame.

## Assumptions and scope
The field is algebraically closed and has characteristic exactly \(2\). Ordinary means that the Jacobian has \(2\)-rank \(3\); for a smooth plane quartic this is equivalent to possessing seven geometric bitangents. Hyperflex is contact order exactly four at a single smooth point, not an ordinary two-contact bitangent. The claim concerns reduced geometric hyperflex lines, not a flat length-28 characteristic-zero bitangent scheme. No assertion is made for nonordinary quartics (with fewer geometric bitangents), or for arbitrary positive-characteristic quartics.

## Proof
**1. Universal normal form and smoothness.** By the normal-form theorem of Nart and Ritzenthaler [1], after a projective change of coordinates any smooth ordinary plane quartic is \(C_Q:Q^2=H\), with \(H=xyz(x+y+z)\). For completeness, differentiation in characteristic \(2\) yields
\[
 (\partial_x H,\partial_y H,\partial_z H)=(yz(y+z),xz(x+z),xy(x+y)),
\]
whose simultaneous projective zero set is the seven points of \(\mathbb P^2(\mathbb F_2)\). The quartic is smooth if and only if
\[
 abc(a+b+d)(b+c+e)(a+c+f)\ne0,
 \qquad a+b+c+d+e+f\ne1.
\]
Indeed at the first six points \(H=0\) and at \([1:1:1]\) one has \(H=1\). This proves the nondegeneracy conditions directly and confirms those in [1].

**2. All seven bitangents.** Four lines \(x=0,y=0,z=0,x+y+z=0\) are bitangents because \(H\) vanishes upon restriction and \(C_Q\) restricts to \(Q^2\). The three diagonal lines \(x+y=0,y+z=0,x+z=0\) are also bitangents because \(H\) restricts to a square on each. No other line is bitangent: restricting \(Q^2+H\) to a line gives a square if and only if the restriction of \(H\) is a square. For a line not a factor of \(H\), the four pairwise distinct factor-lines of \(H\) must meet it in two pairs of coincident points. The only such lines connect opposite vertices of the complete quadrangle and are exactly the stated three diagonal lines. (If all four intersections coincide, three factor-lines would be concurrent, which they are not.) Smoothness excludes a component line. The displayed seven therefore exhaust all geometric bitangents, consistently with [1, Proposition 1.1].

**3. Hyperflex equations.** The intersection on any of these lines equals twice the zero divisor of the binary quadratic \(Q|_L\). A binary quadratic in characteristic \(2\) has a repeated geometric root exactly when its mixed coefficient vanishes. Restricting \(Q\) to the seven lines in the order \(x,y,z,x+y,y+z,x+z,x+y+z\) gives mixed coefficients \(e,f,d,e+f,d+f,d+e,d+e+f\). Each vanishing is equivalent to contact divisor \(4P\), proving the seven conditions. These tests involve no characteristic-zero Hessian argument.

**4. Fano-linear classification and incidence.** The seven displayed forms are exactly the nonzero \(\mathbb F_2\)-linear combinations of \(d,e,f\). Thus the set of hyperflex bitangents identifies with the nonzero kernel of the linear map
\[
 \mathbb F_2^3\longrightarrow k,\qquad (u,v,w)\longmapsto ud+ve+wf.
\]
Its kernel has dimension \(3-r\), so the cardinality is \(2^{3-r}-1\). If that dimension is \(2\), its three nonzero vectors sum to zero. Under the Fano correspondence between these vectors and the bitangent line coefficients, the corresponding three line equations sum to zero, hence their lines pass through the same point. Kernel dimension \(0,1,2,3\) gives, respectively, an empty set, a singleton, a concurrent triple, or all seven lines.

**5. Realization.** Fix any triple \((d,e,f)\) having the desired \(\mathbb F_2\)-span rank \(r=0,1,2,3\). The seven smoothness exclusions of Step 1 eliminate finitely many proper affine hypersurfaces in \((a,b,c)\)-space, and hence their complement is nonempty over infinite \(k\). Such triples exist because \(k\) contains \(\mathbb F_8\); the exact witnesses for all four ranks in the accompanying verifier even lie over \(\mathbb F_8\). This proves sharpness.

## Verification
The included standalone script uses exact arithmetic in \(\mathbb F_8=\mathbb F_2[t]/(t^3+t+1)\) to enumerate all \(512\) ordered triples \((d,e,f)\), compare seven hyperflex indicators with the rank formula, verify the distribution of ranks \((1,49,294,168)\), and find a smooth witness for every possible hyperflex count using the seven exact nondegeneracy conditions. It also verifies that the three hyperflex lines are concurrent in the three-hyperflex case. Its recorded output is included and can be regenerated with Python 3; no external packages are required. The infinite-field assertions are proved in Steps 1--5, not inferred from finite enumeration.

## Relationship to prior work
The seven-bitangent characterization and universal \(Q^2=xyz(x+y+z)\) normal form are previously established by Wall [2] and Nart--Ritzenthaler [1]. In particular, neither the normal form nor the list of seven bitangents is claimed as new. The result here refines them by **complete hyperflex-contact incidence**, a different invariant: the allowed cardinalities, Fano subspace constraint, and realization in every stratum. The full accessible Nart--Ritzenthaler paper does not present a hyperflex classification. Pacini--Testa [3] study hyperinflection configurations in other characteristics and explicitly exclude characteristic \(2\). Duursma [4] focuses on Klein twists, not all ordinary plane quartics. These comparisons do not establish historical priority against every specialist source.

## Limitations
A complete inspection of Wall's 1995 primary paper was unavailable; its older normal-form treatment may contain equivalent incidental statements. The refinement is an elementary but global contact-order classification derived from established normal forms, not a new classification of ordinary quartics. Only self-review is reported; independent scientific audit has not been performed. The method relies essentially on characteristic \(2\) and does not treat nonordinary curves.

## References
[1] E. Nart and C. Ritzenthaler, *Non hyperelliptic curves of genus three over finite fields of characteristic two*, first posted 2003-12-18, arXiv:math/0312366 (especially Section 1 and Proposition 1.1), https://arxiv.org/html/math/0312366v2 .

[2] C. T. C. Wall, *Quartic curves in characteristic 2*, Math. Proc. Cambridge Philos. Soc. 117 (1995), 393--414, DOI:10.1017/S0305004100073254 .

[3] M. Pacini and D. Testa, *Plane quartics with at least 8 hyperinflection points*, first posted 2013-01-09, arXiv:1301.1865, https://arxiv.org/abs/1301.1865 .

[4] I. M. Duursma, *Twisted Klein curves modulo 2*, arXiv:math/0302154, https://arxiv.org/abs/math/0302154 .
