# Independent mathematical audit

## correctness

PASS

The inequalities for roots e_i-e_j require coordinate range at most one. Conversely, for integer sum-zero z the inner product on this range-bounded set is at most the sum of positive coordinates of z, which is half its l1 norm and at most half its squared Euclidean norm. This gives the exact Voronoi cell, the projection of [0,1]^N, whose norm maximum occurs at a projected indicator with cardinality nearest N/2. The simple roots are a lattice basis by the partial-sum inversion t_i=x_1+...+x_i. Within the open cube in t, the simplex for σ is the closure of t_{σ(1)}>...>t_{σ(n)}. Put t_0=t_N=0. Since x_j=t_j-t_{j-1}, the interior coordinate floors are m_1=0, m_N=-1, and m_j=-1 precisely when p_{j-1}<p_j for internal j; this gives k=-sum m and all vertices v in m+{0,1}^N with sum zero. Each such vertex has displacement from c=m+(k/N)1 given by a weight-k binary vector minus its mean, hence squared radius k(N-k)/N. Affine independence makes the sphere unique and ball convexity gives the radius upper bound without asserting pointwise minimum enclosing spheres. For any independent frame the translates of the packet by the sublattice it spans triangulate H. If a simplex has vertices v_i in a radius-R ball about c and x=sum λ_i v_i, then sum λ_i||x-v_i||²=sum λ_i||v_i-c||²-||x-c||²≤R². Thus some lattice vertex is at distance at most R and μ≤κ, giving equality for the exhibited basis. The inverse permutation bijection, ascent counting and symmetry give the Eulerian multiplicities and balanced peak, including the two equal central radii when N is odd. The finite checker was inspected, not executed. Its finite norm identities are not a substitute for the universal proof; its Voronoi sample uses integer test points and is only a very weak supplementary check.

## originality

FAIL

The result is a direct consequence of existing type-A alcove triangulation and root-lattice Delaunay geometry in partial-sum coordinates, together with Xue's general comparison. The prior sources need not name κ for this mechanical implication. Critically, the older triangulation is not an arbitrary periodic triangulation: its restriction to a unit cube in the partial-sum coordinates is literally the packet from the one fixed simple-root basis. The same identification transfers the classical Eulerian hypersimplex counts to the packet's spheres. The exhibited adaptation is correct but does not leave a distinct exact invariant or claim under the scientific originality standard.

## value

FAIL

Knowing sharp behavior of κ on a canonical infinite family is a good question, and the fixed-frame/relaxed distinction matters. But the partial-sum coordinate map simply writes the classical Delaunay-refining type-A alcove triangulation in its natural lattice frame. Equality and the shell counts attach known radii and Eulerian volumes to those same simplices. No independently unknown invariant, mechanism or classification remains in the frozen claim, so no repair is proposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
