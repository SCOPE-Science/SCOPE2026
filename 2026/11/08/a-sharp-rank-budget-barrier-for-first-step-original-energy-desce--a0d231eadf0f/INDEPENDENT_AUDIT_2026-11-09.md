# Independent mathematical audit

## correctness

PASS

With z=H^(1/2)x and B=h H^(1/2)(I+hL)^(-1)H^(1/2) positive definite, the coherently initialized SAV step is z1=(I-B/(1+eta))z where eta=z^TBz/(||z||^2+2C)>0 for z!=0. Thus beta_max(B)<=2 guarantees strict energy decrease for every nonzero z; if beta>2, arbitrarily small eigenvector inputs give increase since eta->0. Congruence plus inverse ordering gives beta_max(B)<=2 iff h(H-2L) preceq 2I without assuming H,L commute. Courant-Fischer applied to ker L dimension >= d-r gives lambda_max(H-2L)>=lambda_(r+1)(H), attained by half the leading r spectral components. Boundary eta>0 is essential and correctly handled. Finite noncommuting NumPy checks in inspected verify.py supplement this argument; diagonal H=diag(9,4,1) gives rank1 hmax=1/2 and rank2 hmax=2.

## originality

PASS

Best-of-knowledge PASS: the identified SAV literature covers the algorithm, modified-energy dissipation, conservative original-objective sufficient bounds and low-rank approximations, whereas the exact necessary-and-sufficient first-step spectral bound including noncommuting L and optimal rank budget is a sharper classification. Full Sagawa source was not accessible and this remains an explicit priority risk; no demonstrated dominating theorem was found.

## value

PASS

An exact original-energy first-step safety frontier and optimal rank-versus-step-size cost tradeoff isolate a meaningful gap between auxiliary modified-energy dissipation and actual quadratic descent; min-max extremizers and arbitrarily-small-data necessity are reusable structural statements rather than a routine renamed lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
