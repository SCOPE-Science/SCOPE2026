# Independent mathematical audit

## correctness

PASS

For a 2-(v,k,lambda) incidence matrix, BB*= (r-lambda)I+lambda J has square root S=a I+delta J with a=sqrt(r-lambda)>0, d=sqrt(rk), delta=(d-a)/v=lambda/(a+d). The polar-like factorization B=UV* with U=S^(1/2), V=B* S^(-1/2) has constant row squared norms K=tr(S)/v and H=tr(S)/b. Schatten Holder gives Phi(w,z)<=sqrt(KH)=Gamma, attained at uniform weights. The exact equality condition for Frobenius Holder is normalized Gram equality X*X/K=Y*Y/H, equivalent to B D_z B*=(v/b) S D_w S, valid even if some weights vanish. Fixed block size gives sum_{j!=i} M_ij=(k-1)M_ii, yielding [(k-1)a^2+(2k-v)a delta] w_i=a delta+(v-k)delta^2. Coefficient positive: for v>2k, (k-1)a^2=lambda(v-k) and a delta<lambda/2 give lower bound lambda v/2. Thus all point weights w=1/v; pair-block equations Q z=lambda/b determine all block weights, including boundaries. Column sums of Q ensure sum z=1, uniform z strictly positive gives affine dimension b-rank Q, Steiner lambda=1 implies uniqueness. Independently formed exact 15x20 Q for all triples on 6 points; its rational rank is 15 (kernel dim5), and the eight-transversal-triple signed trade satisfies Qh=0. These support but do not replace general proof.

## originality

PASS

The numerical Schur norm and standard invariant optimal-weight existence are known. Prior published projective-plane rigidity covers only symmetric lambda=1 projective incidences, while the audited theorem handles every finite 2-design, including repeated indexed blocks and arbitrary trade-polytope nonuniqueness. The identification of the full optimal block-weight face with the nonnegative pair-trade polytope is not implied by the reviewed prior projective-plane theorem. General Schatten equality classifications might provide an alternate proof but do not by themselves state the combinatorial restriction for all designs.

## value

PASS

Classifying every maximizer, not just the known sharp norm value, is a natural exact question for a highly structured but broad family of matrices. The universal rigidity of point weights versus nontrivial combinatorial trade freedom of block weights connects analysis, design theory, and linear algebra and supplies an exact dimension and concrete positive/zero boundary optimizers. The classification is stronger than a textbook application of an inequality and includes nonsymmetric designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
