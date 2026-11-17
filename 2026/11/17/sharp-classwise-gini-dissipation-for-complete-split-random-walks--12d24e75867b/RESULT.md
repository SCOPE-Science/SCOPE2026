# Sharp classwise Gini dissipation for complete-split random walks

## Finding

Let \(c,s\ge1\) be integers and let the unweighted complete-split graph be \(K_c\vee\overline{K_s}\). Its vertex set is partitioned into a clique \(C\) of size \(c\) and an independent set \(I\) of size \(s\), with all edges between the parts. Write \(N=c+s\) and \(d=N-1\). Let \(P=D^{-1}A\) be the loopless simple-random-walk averaging matrix acting on real vertex signals.

For any vertex subset \(U\), put
\[
G_U(f)=\sum_{\{u,v\}\subset U}|f(u)-f(v)|,
\]
and write \(G=G_{C\cup I}\). Then **for every real vertex signal \(f\)**,
\[
\boxed{G(Pf)+\frac{s-1}{d}G_C(f)+\frac{s}{d}G_I(f)\le\frac{s}{d}G(f).}
\tag{1}
\]
When \(c,s\ge2\), both additional dissipation coefficients in (1) are separately optimal with the principal coefficient fixed. For every integer \(m\ge1\), the exact attained operator seminorm on real signals modulo constants is
\[
\boxed{\|P^m\|_{G\to G}=\left(\frac{s}{c+s-1}\right)^m.}
\tag{2}
\]
If \(s\ge2\), equality in \(G(P^m f)\le(s/d)^mG(f)\) for nonconstant \(f\) holds exactly when \(f\) is constant separately on \(C\) and on \(I\). For \(s=1\), equality holds for every signal. In particular, a single step strictly contracts every nonconstant real signal in the \(G\) seminorm whenever \(c\ge2\), whereas \(c=1\) has sharp coefficient one for all powers.

## Assumptions and scope

The graph is finite, undirected, unweighted and loopless. Every clique vertex has degree \(d=c+s-1\); every independent-set vertex has degree \(c\). All signals are real. Both \(G\) and the restricted seminorms are unnormalized complete-pair sums. The operator seminorm is the supremum of \(G(P^m f)/G(f)\) over real signals with \(G(f)>0\); constants have zero seminorm and are preserved by \(P\). The formula includes the star case \(c=1\), the complete-graph case \(s=1\), and the two-vertex graph \(c=s=1\).

## Proof

**1. Binary-cut expression.** Let \(S\subsetneq C\cup I\) be nonempty, with \(a=|S\cap C|\), \(b=|S\cap I|\), and \(k=a+b\). For \(f=\mathbf1_S\), each selected clique vertex receives \((k-1)/d\), each unselected clique vertex receives \(k/d\), and every independent-set vertex receives \(a/c\). Hence, with the convention that empty multiplicities give zero,
\[
F_a(b):=G(P\mathbf1_S)=\frac{a(c-a)}d+s\left[a\left|\frac{a+b-1}{d}-\frac ac\right|+(c-a)\left|\frac{a+b}{d}-\frac ac\right|\right].
\tag{3}
\]
Also \(G(\mathbf1_S)=k(N-k)\), \(G_C(\mathbf1_S)=a(c-a)\), and \(G_I(\mathbf1_S)=b(s-b)\).

**2. A sharp cut deficit.** For fixed \(a\), the right-hand side of (3) is convex as a real function of \(b\) on \([0,s]\). Put \(R_a(b)=(s/d)(a+b)(N-a-b)\). This is a strictly concave quadratic in \(b\). Direct substitution, using \(d\ge c\), gives
\[
F_a(0)=\frac{a(c-a+s^2)}d,
\quad
R_a(0)-F_a(0)=\frac{a(c-a)(s-1)}d.
\tag{4}
\]
Complementing a cut does not change its output variation, so \(F_a(s)=F_{c-a}(0)\), and the other endpoint has the same deficit \(a(c-a)(s-1)/d\). Convexity gives
\[
F_a(b)\le\left(1-\frac bs\right)F_a(0)+\frac bsF_a(s).
\]
The exact quadratic-chord identity is
\[
R_a(b)=\left(1-\frac bs\right)R_a(0)+\frac bsR_a(s)+\frac{s}{d}b(s-b).
\]
Subtracting yields the **all-cut quantitative bound**
\[
\frac{s}{d}G(\mathbf1_S)-G(P\mathbf1_S)
\ge\frac{s-1}{d}G_C(\mathbf1_S)+\frac{s}{d}G_I(\mathbf1_S).
\tag{5}
\]
The derivation also works for \(s=1\), when the integer choices of \(b\) are only the endpoints.

**3. Extension from cuts to all real signals.** Order the distinct values of an arbitrary real \(f\) as \(\lambda_1<\cdots<\lambda_q\), and put \(S_j=\{v:f(v)\ge\lambda_{j+1}\}\). Then
\[
f=\lambda_1\mathbf1+\sum_{j=1}^{q-1}(\lambda_{j+1}-\lambda_j)\mathbf1_{S_j}.
\]
For each \(U\subseteq C\cup I\), the exact discrete layer-cake identity is
\[
G_U(f)=\sum_{j=1}^{q-1}(\lambda_{j+1}-\lambda_j)G_U(\mathbf1_{S_j}).
\tag{6}
\]
Because \(P\mathbf1=\mathbf1\), the triangle inequality gives \(G(Pf)\le\sum_j(\lambda_{j+1}-\lambda_j)G(P\mathbf1_{S_j})\). Applying (5) and then (6) proves (1), for all dimensions and all real inputs.

**4. Sharpness, rigidity and powers.** If \(f=\mathbf1_I\), then \(Pf=(s/d)\mathbf1_C\). Modulo constants, this is \(-(s/d)f\); thus \(G(P^m f)=(s/d)^mG(f)\) for every integer \(m\ge1\). Inequality (1) implies \(\|P\|_G\le s/d\); submultiplicativity of the induced quotient norm proves the matching upper bound for every power, giving (2).

For \(c,s\ge2\), choosing a cut consisting of one clique vertex and no independent vertex makes (5) an equality with \(G_C>0\) and \(G_I=0\); choosing one independent vertex and no clique vertex makes it an equality with \(G_C=0\) and \(G_I>0\). Neither dissipation coefficient can therefore be increased while the others remain fixed. For \(s\ge2\), (1) implies that equality at one step forces \(G_C(f)=G_I(f)=0\), equivalently classwise constancy. Every nonconstant classwise-constant signal attains equality because \(P\) multiplies the class contrast by \(-s/d\). If equality holds at power \(m\), the first-step inequality must also be an equality; this proves the rigidity for all powers. If \(s=1\), the graph is complete and \(P=(J-I)/c\), so all quotient-space signals are multiplied by \(-1/c\), making all inputs equality cases.

Finally \(s/d<1\) exactly when \(c\ge2\). For \(c=1\), the class-contrast eigenvalue is \(-1\), giving persistent periodic variation. This proves all assertions.

## Verification

The standalone `verify_split_gini.py` implements the actual random-walk matrix and unnormalized Gini sums using exact rational arithmetic. It tests every nontrivial vertex subset for \(1\le c,s\le6\) and \(c+s\le10\), checks the two additional dissipation terms, classwise equality, and four successive powers. It also verifies exact eigenmode sharpness for larger class sizes and compares the full inequality on randomly constructed rational input vectors. Invoke `python verify_split_gini.py` with Python 3; no external packages are required. These finite checks support the calculation but are not the proof in arbitrary dimensions.

## Relationship to prior work

Ipsen and Selee, *Ergodicity Coefficients Defined by Vector Norms* (2011), develop general coefficient-of-ergodicity bounds for stochastic matrices, primarily expressed through ordinary \(\ell_p\) norms. De Pasquale, Smith, Bullo and Valcher, *Dual Seminorms, Ergodic Coefficients and Semicontraction Theory* (2022 preprint, 2024 publication), formulate incidence-matrix seminorms and their general induced-operator theory. Those frameworks motivate measuring consensus differences by seminorms, but the inspected results do not give (1), its optimal two-part coefficients, the exact split-graph power formula (2), or the equality classification. Work on spectrally optimal kernels for complete split graphs optimizes a different operator family and objective; it does not directly imply the exact norm of the fixed degree-normalized loopless walk. This comparison is limited by incomplete access to some narrowly related published material and does not establish exhaustive historical uniqueness.

## Limitations

The result does not cover other split graphs with missing cross edges, nonuniform clique or cross weights, holding probabilities, independently weighted pairwise variations, or continuous-time heat norms. The sharpness assertions apply to the specified unweighted complete-split family and the unnormalized complete-pair Gini seminorm only. Exact positive-time bounds for \(\exp[t(P-I)]\) are not asserted.

## References

1. I. C. F. Ipsen and T. M. Selee, *Ergodicity Coefficients Defined by Vector Norms*, SIAM Journal on Matrix Analysis and Applications 32 (2011), 153–200. DOI: 10.1137/090752948; electronically published 2011-03-09.
2. G. De Pasquale, K. D. Smith, F. Bullo and M. E. Valcher, *Dual Seminorms, Ergodic Coefficients and Semicontraction Theory*, arXiv:2201.03103 (first public preprint 2022-01-09); IEEE Transactions on Automatic Control 69 (2024), 3040–3053.
