# Independent mathematical audit

## correctness

PASS

For S=Σx_j² the i-th absolute Jacobian row sum is (T_i+x_i H_i)/S^(3/2), where T_i and H_i are the squares and the sum over the other coordinates. At fixed x_i,T_i it increases with H_i, whose exact maximum is attained by the in-box common value c=√(T_i/(n−1)). Set m=n−1 and let u=x_i/c. The minimal feasible c is a for u≥1 and a/u for u≤1, with 1/r≤u≤r where r=b/a. On u≤1 the derivative sign is that of m(1+2u)−2u²−u³≥(1−u)(1+3u+u²); on u≥1 it is that of m−3u−2u². Thus the exact row maximum is attained at u=min(r,max(1,(√(8n+1)−3)/4)), with c=a. The transition occurs at m>5. Integration gives the same upper bound over input pairs; choose interior points tending to the extremizer, then take feasible symmetric differences in the sign direction (1,−1,…,−1) with shrinking steps. The selected row tends to its norm, proving sharpness even at a corner. When r=q_n>1, the level aq_n equals b; the word ‘interior’ applies to that distinguished level only for strict r>q_n (the formula itself includes the equality case correctly). For fixed r the maximizer eventually has u=r, giving √n aL→1+r. For r_n/√n→κ>0, u/√n→v=min(κ,1/√2) and aL→v/(1+v²)^(3/2), equalling 2/(3√3) at saturation. The constant map at n=1 and singleton domain a=b correctly have minimal Lipschitz constant zero. The unsmoothed unit-gain RMS output multiplies this constant by √n. The supplied script was inspected, not executed; the audit uses the analytic optimization and limiting argument, not sample tests.

## originality

PASS

The Jacobian, unregularized RMS scaling and unrestricted radial-retraction estimates are prior material. The exact constrained absolute-coordinate positive-box coefficient, dependence on contrast, and seven-coordinate transition are not established by those statements. No distinct exact positive-box result was located in the checked sources.

## value

PASS

The full common-bounds positive box and absolute coordinate perturbation are natural in assessing direction and raw RMS transforms when inputs are bounded away from zero. The exact sharp modulus, rather than a spectral or local upper bound, tells when adding contrast can worsen stability and when further contrast cannot affect the worst case. The uniform-to-one-outlier transition and differing fixed-contrast and high-contrast scaling are meaningful predictions not present in the standard derivative formula. The contribution is the constrained optimization, not another derivation of that derivative or a general machine-learning robustness claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
