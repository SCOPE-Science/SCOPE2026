# Independent mathematical audit

## correctness

PASS

For agent i with a own and b other iid Bernoulli(p_i) goods, realized EF1 is precisely Y_i<=X_i+1 where X_i~Bin(a,p_i), Y_i~Bin(b,p_i); independent agents make both fairness probabilities multiply. At m=4, direct binomial expansions yield f(p_1)f(p_2) for 2:2 and g(p_singleton) for 1:3. Any 0:4 is strictly improved by moving one good. Since g strictly decreases on (0,1), singleton goes to the lower p. Rearranging g(s)>f(s)f(t) yields t^2(1-t)^2>H(s), with strictly increasing H, unique quartic threshold s_c≈0.2032804404095 and symmetric nonmonotone t interval. For fixed m with p_i=eps*lambda_i, violation first requires two other-valued goods, giving quadratic loss lambda1² C(m-a,2)+lambda2² C(a,2)+O(eps), uniformly over finite a choices; its discrete consecutive difference proves the unique/two-candidate optimizer rule. Independently checked exact rational four-good gap 7902186119/10^12, threshold, polynomial factoring. Finite checks corroborate rather than replace exact binomial argument.

## originality

PASS

The sharp realized-EF1 four-good phase and general fixed-m squared rare-event allocation law are not implied by known exact-envy-freeness maximization or same-realization shared-good EF1 balancing. The distinct random utility coupling and target matter. Primary 2026 Igarashi-Oh text was inaccessible, so O PASS is qualified best-of-knowledge, not certification.

## value

PASS

Optimizing realized EF1 probability for preassigned uncertain binary goods is a natural fair-allocation risk problem. The smallest four-good symmetry-breaking horizon, sharp nonmonotone two-probability phase boundary and exact quadratic small-risk allocation rule across every fixed m supply a meaningful classification, not a cosmetic parameter substitution or mere tiny numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
