# Independent mathematical audit

## correctness

PASS

Conditioning on the number m of cyclic vertices gives a uniform m-subset and uniform permutation on it; ordered disjoint length-ell cycle collections have exact factorial mean ell^(-r) for m>=r*ell and zero otherwise. The rooted-forest count m*n^(n-m-1) is constant across cyclic sets/permutations (including m=n). Summing the exact law Pr(L=m)=m(n)_m/n^(m+1) telescopes to Pr(L>=s)=(n)_s/n^s. Conditional expectations, threshold covariance, fixed-label independence, Cov(F^2,L)=(E L-1)/n, and fixed-s Gaussian-scale asymptotic follow. Own independent exact checker tested 103 admissible moment cases at n=2..5; original verify.py enumerates n=2..6 but this was read rather than rerun. Finite data not used as proof.

## originality

FAIL

Hansen–Jaworski (2010), pp.342–344, explicitly supply the conditional uniform permutation of cyclic vertices and identify its conditional cycle-count law as well known. The standard exact uniform-permutation cycle factorial-moment identity E[(C_ell)_r]=ell^(-r) when m>=r*ell (zero otherwise) immediately yields the submitted master identity by substituting m=L. The remaining claimed covariances are direct conditional-expectation and tail-telescoping consequences, and fixed-label first-order independence follows by the familiar (m/n)*(1/m)=1/n exchangeability computation. These are consequences of the published structural theorem plus elementary permutation counting; absence of identical phrasing is not novelty.

## value

FAIL

Although the fixed-point first-moment orthogonality versus second-moment dependence is an instructive probability illustration, the package supplies only short algebraic corollaries of the published exact conditional-permutation model and textbook cycle-count factorial moments. It neither resolves a distinct motivated open invariant nor adds a nontrivial structural lemma beyond that model; its finite replay and exact presentation do not make a new mathematically substantive contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
