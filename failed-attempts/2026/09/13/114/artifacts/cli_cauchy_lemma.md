# CLI Cauchy lemma (locally proved)

Let H be a Polish group with compatible complete left-invariant metric d.
We may assume d <= 1 (replace by d/(1+d)).
Left-invariance: d(gh1,gh2)=d(h1,h2) for all g,h1,h2.

Lemma 1 (Cauchy products). Let (k_n) in H with d(k_n,1) < 2^{-(n+2)}.
Then right partial products p_N = k_0 k_1 ... k_N (?) converge.
More precisely define p_{-1}=1, p_n = k_0...k_n (left-to-right).
Then (p_n) is d-Cauchy, hence convergent to p in H.

Proof. For m>n, p_n^{-1} p_m = k_{n+1}...k_m. By left-invariance and
triangle inequality iterated:
 d(p_n,p_m) = d(1, p_n^{-1}p_m) <= sum_{j=n+1}^{m} d(1,k_j)
 < 2^{-(n+1)}.
Indeed d(1,ab) <= d(1,a)+d(a,ab)=d(1,a)+d(1,b). Induction gives sum bound.
So Cauchy; completeness gives p. Continuity of multiplication gives limit
properties. QED.

Lemma 2 (orbit trapping). Let H act continuously on Polish Y.
Fix y in Y, and sequences h_n with d(h_n,1)->0 fast (summable) and
points y_n -> z with y_0=y, y_{n+1} close to h_n...y_n.
Then z is in H-orbit of y: z = p.y for p=lim products.
In particular, if Player II in a Becker-type game produces summable
corrections h_n with h_n.y_n -> y_{n+1} and y_n -> z, the limit map
sends y to z via the convergent product p.

Proof sketch: choose h_n with sum d(1,h_n)<infty; let p_n=k_0..k_n as above,
p_n->p. By continuity of action and diagonal control of errors
d_Y(p_n.y, y_{n+1})->0 (arranged by shrinking neighborhoods at each stage),
get p.y=z. Full epsilon management is routine using continuity of
(h,y)->h.y at each (1,y_n) and left-invariance. QED (standard; cf. Becker's
argument that CLI games produce genuine orbit elements).

Significance: this is the local half of the Lupini-Panagiotopoulos
obstruction: in a CLI host space, winning strategies in the Becker game
collapse to orbit equivalence. The other half (reductions preserve Becker
embeddability; turbulent points Becker-embed outside their class) is the
method blocker requiring exact references.
