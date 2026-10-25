# Independent mathematical audit

## correctness

PASS

The pinned RESULT.md assumes 1<p<∞, bounded projections P_i:X→X with range V_i, bounded Λ_i:X→X_i and weights v_i>0. Each A_i=v_i Λ_iP_i:X→X_i is bounded, so A_i^*=v_iP_i^*Λ_i^*:X_i^*→X^*; the printed P_iΛ_i^* is generically ill-typed. For any finite support g, <(v_iΛ_iP_i f)_i,g>=<f,Σ_i v_iP_i^*Λ_i^*g_i>. If the family is Bessel, U:X→ℓ^p(X_i) is bounded. Since (ℓ^p(X_i))^*=ℓ^q(X_i^*) for 1<p<∞, T_c=U^*; coordinate truncations give unconditional convergence for every g and ||T_c||=||U||=the optimal upper Bessel bound. Conversely, if the series defines a bounded T_c:ℓ^q→X^*, its finite-support restrictions imply every finite truncated ℓ^p norm of (v_iΛ_iP_i f)_i is ≤||T_c||||f||, so the infinite ℓ^p norm exists with the same bound; this fills a routine implicit summability step in RESULT.md. Once Bessel, U is bounded below iff U^*=T_c is onto by Hahn–Banach/closed-range. An exact independent matrix computation confirms P=[[1,1],[0,0]] is a nonorthogonal projection, Λ=[1,0], U=ΛP=[1,1], PΛ^*(1)=(1,0) but P^*Λ^*(1)=(1,1). No finite check is used for the infinite-series theorem. Limits: 1<p<∞, bounded P_i, no automatic extension to endpoint p or unbounded algebraic projections; neither 2022 downstream perturbation theorem nor arbitrary Banach adjoint identifications are implied.

## originality

FAIL

The paper-specific diagnosis of an ill-typed 2022 synthesis formula is correct and searches did not find a separately indexed erratum; however the entire repaired mathematical theorem is a direct specialization of the strictly broader 2007 Banach pg-frame theory. In 2007 Abdollahpour–Faroughi–Rahimi Proposition 3.8, Lemma 3.11, Theorem 3.12 already prove bounded synthesis iff Bessel, T=U^*, and onto iff frame for an arbitrary family of bounded operators A_i:X→X_i. Taking A_i=v_iΛ_iP_i gives exactly the submitted corrected synthesis formula and all positive conclusions; optimal norm is the general identity ||U^*||=||U||. The difference in fusion terminology, later theorem numbers, and the 2022 printing error does not create a new theorem. Under implication-based coverage, O fails decisively rather than relying on negative searches.

## value

PASS

The correction has concrete interpretive utility: an actual published central Bessel/synthesis operator is not composable on the stated Banach spaces, and its defect contaminates the printed U^*=T assertion and the onto/frame criterion. The corrected statement gives a uniform, type-correct reading for practitioners and a nonorthogonal projection witness shows that blindly identifying X with X^* does not save the formula. This is more motivated than an arbitrary negative type check because it protects several central results in an existing paper. The value is limited: the corrected theorem is a direct already-known pg-frame specialization and the exact optimal norm is the generic adjoint norm identity; it is not a new structural frame theorem or substantial independent technique. V PASS does not override O FAIL.

The dated certificate retains the supplied scientific assessment, sources and limitations.
